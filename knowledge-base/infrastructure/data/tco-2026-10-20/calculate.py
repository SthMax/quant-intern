"""CPU-only three-year cash/resource budget. Python standard library; no network/GPU.

Run: python3 knowledge-base/infrastructure/data/tco-2026-10-20/calculate.py
The acceptance gate and rates are budget assumptions, never measured task quality.
"""
import copy
import csv
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
KB = HERE.parents[2]
INPUT = json.loads((HERE / "inputs.json").read_text())
SPARK = json.loads((HERE.parent / "week7-deployment-2026-10-12/results.json").read_text())["spark_fit"]


def trajectory(p, hit_ds=None, hit_claude=None, hit_local=None):
    t, c = p["trajectory"], p["cache"]
    hd = c["deepseek_eligible_prefix_hit_probability"] if hit_ds is None else hit_ds
    hc = c["claude_eligible_prefix_hit_probability"] if hit_claude is None else hit_claude
    hl = c["local_eligible_prefix_hit_probability"] if hit_local is None else hit_local
    rows = []
    for r in range(t["rounds"]):
        n = t["initial_input_tokens"] + r * (t["new_user_tool_tokens_per_followup"] + t["output_tokens_per_round_including_thinking_and_tool_arguments"])
        ds_eligible = n-t["new_user_tool_tokens_per_followup"] if r else 0
        cl_eligible = n-t["new_user_tool_tokens_per_followup"]-t["output_tokens_per_round_including_thinking_and_tool_arguments"] if r else 0
        ds_hit, cl_hit, local_hit = ds_eligible*hd, cl_eligible*hc, ds_eligible*hl
        rows.append({"round": r+1, "submitted_input": n, "new_external_input": t["initial_input_tokens"] if r == 0 else t["new_user_tool_tokens_per_followup"], "output": t["output_tokens_per_round_including_thinking_and_tool_arguments"], "deepseek_hit": ds_hit, "deepseek_miss": n-ds_hit, "claude_hit": cl_hit, "claude_write": n-cl_hit, "local_hit": local_hit, "local_prefill": n-local_hit, "local_eligible": ds_eligible})
    return rows


def api_cost(p, provider, rows):
    """CNY per complete trajectory, including planned tax reserve; retries outside."""
    ap = p["api"][provider]
    if provider == "deepseek":
        rates = ap["offpeak"]
        peak = 1+ap["fraction_peak"]*(ap["peak_multiplier"]-1)
        components = {"input_miss": sum(x["deepseek_miss"] for x in rows)*rates["input_miss"]/1e6*peak, "input_hit": sum(x["deepseek_hit"] for x in rows)*rates["input_hit"]/1e6*peak, "output": sum(x["output"] for x in rows)*rates["output"]/1e6*peak}
    else:
        rates = ap["rates"]
        write = rates["cache_write_1h"] if p["cache"]["claude_write_ttl_minutes"] == 60 else rates["cache_write_5m"]
        tm = p["cache"]["claude_token_multiplier_vs_reference"]
        components = {"cache_write": sum(x["claude_write"] for x in rows)*write/1e6*tm, "input_hit": sum(x["claude_hit"] for x in rows)*rates["input_hit"]/1e6*tm, "output": sum(x["output"] for x in rows)*rates["output"]/1e6*tm}
    factor = p["fx_usd_cny"]*(1+p["api_tax_reserve_fraction"])*(1-ap["discount"])
    return {k: v*factor for k,v in components.items()}


def spark_F(n):
    return SPARK["prefill_a_seconds_per_million"]*n/1e6+SPARK["prefill_b_seconds_per_million_squared"]*(n/1e6)**2


def work_seconds(p, scale, rows):
    if scale == "company":
        a = p["scale"][scale]["local"]
        prefill = sum(x["local_prefill"] for x in rows)/a["planning_prefill_uncached_tokens_s"]
        decode = sum(x["output"] for x in rows)/a["planning_decode_output_tokens_s"]
    else:
        h = p["cache"]["local_eligible_prefix_hit_probability"]
        prefill = sum(spark_F(x["submitted_input"])-h*spark_F(x["local_eligible"]) for x in rows)
        decode = sum(x["output"]*(SPARK["decode_step_a_seconds"]+SPARK["decode_step_b_seconds_per_million"]*(x["submitted_input"]+x["output"]/2)/1e6) for x in rows)
    repeat = 1+p["trajectory"]["extra_full_trajectory_equivalents_per_target_task"]
    return {"prefill_seconds": prefill*repeat, "decode_seconds": decode*repeat, "total_seconds": (prefill+decode)*repeat}


def calculate(p, scale, volume="base", year1_override=None, fixed_one_node=False):
    s = p["scale"][scale]
    a, b, common = s["local"], s["api"], s["common"]
    v = s["volume_scenarios"][volume]
    first = v["year1_target_tasks"] if year1_override is None else year1_override
    rows = trajectory(p)
    work = work_seconds(p, scale, rows)
    capacity = p["service_hours_per_year"]*3600*p["planning_utilization_ceiling"]/work["total_seconds"]
    per = {k: api_cost(p, k, rows) for k in ["deepseek", "claude"]}
    repeat = 1+p["trajectory"]["extra_full_trajectory_equivalents_per_target_task"]
    initial_common = common["tool_cpu_capex_cny"]
    state = {"local": [], "deepseek": [], "claude": []}
    last_nodes = 0
    for year in range(1, 4):
        tasks = first*(1+v["annual_growth"])**(year-1)
        needed = max(1, math.ceil(tasks/capacity-1e-12))
        nodes = 1 if fixed_one_node else needed
        added = nodes-last_nodes
        busy_hours = tasks*work["total_seconds"]/3600
        average_busy = busy_hours/nodes
        energy_kwh = nodes*a["wall_idle_kw"]*a["powered_hours_per_year"]+(a["wall_active_kw"]-a["wall_idle_kw"])*busy_hours
        electricity = energy_kwh*a["pue"]*a["electricity_cny_per_kwh"]
        common_energy = common["tool_cpu_average_kw"]*common["tool_cpu_powered_hours"]*common["pue"]*common["tariff"]
        local = {"year": year, "target_tasks": tasks, "nodes": nodes, "required_nodes_under_envelope": needed, "capacity_envelope_pass": tasks <= capacity*nodes, "hardware_cny": added*a["hardware_mid_cny"], "common_tool_hardware_cny": initial_common if year == 1 else 0, "facility_initial_cny": added*a["facility_initial_cny"], "implementation_labor_cny": ((a["implementation_person_days"]+(nodes-1)*a.get("expansion_implementation_person_days", a["implementation_person_days"])) if year == 1 else added*a.get("expansion_implementation_person_days", a["implementation_person_days"]))*p["person_day_cny"], "operations_labor_cny": (a["annual_operations_person_days"]+(nodes-1)*a.get("annual_operations_person_days_per_additional_node", a["annual_operations_person_days"]))*p["person_day_cny"], "electricity_cny": electricity, "common_tool_electricity_cny": common_energy, "rack_cny": nodes*a["annual_rack_excluding_power_cny"], "software_support_cny": nodes*a["annual_software_support_cny"], "busy_hours": busy_hours, "busy_fraction_service_hours_per_node": average_busy/p["service_hours_per_year"], "prefill_work_hours": tasks*work["prefill_seconds"]/3600, "decode_work_hours": tasks*work["decode_seconds"]/3600, "required_average_uncached_prefill_tps": tasks*sum(x["local_prefill"] for x in rows)*repeat/(p["service_hours_per_year"]*3600), "required_average_output_tps": tasks*sum(x["output"] for x in rows)*repeat/(p["service_hours_per_year"]*3600)}
        fields = [k for k in local if k.endswith("_cny")]
        local["total_cny"] = sum(local[k] for k in fields)
        local["labor_cny"] = local["implementation_labor_cny"]+local["operations_labor_cny"]
        local["nonlabor_outlay_cny"] = local["total_cny"]-local["labor_cny"]
        state["local"].append(local)
        for provider in per:
            escalation = (1+p["api"][provider]["price_change_per_year"])**(year-1)
            api = {"year": year, "target_tasks": tasks, "common_tool_hardware_cny": initial_common if year == 1 else 0, "implementation_labor_cny": b["implementation_person_days"]*p["person_day_cny"] if year == 1 else 0, "operations_labor_cny": b["annual_operations_person_days"]*p["person_day_cny"], "platform_cny": b["annual_platform_cny"], "security_premium_cny": b["annual_security_premium_cny"], "network_cny": b["annual_incremental_network_cny"], "common_tool_electricity_cny": common_energy}
            api.update({"token_"+k+"_cny": amount*tasks*repeat*escalation for k,amount in per[provider].items()})
            tools = p["api"][provider].get("provider_tools", {})
            api["provider_tools_cny"] = tasks*(tools.get("search_successful_requests_per_target_task", 0)*tools.get("usd_per_successful_search", 0)+tools.get("fetch_successful_requests_per_target_task", 0)*tools.get("usd_per_successful_fetch", 0))*p["fx_usd_cny"]*(1+p["api_tax_reserve_fraction"])
            api["total_cny"] = sum(val for key,val in api.items() if key.endswith("_cny"))
            api["labor_cny"] = api["implementation_labor_cny"]+api["operations_labor_cny"]
            api["nonlabor_outlay_cny"] = api["total_cny"]-api["labor_cny"]
            state[provider].append(api)
        last_nodes = nodes
    totals = {}
    tasks3 = sum(x["target_tasks"] for x in state["local"])
    for route, years in state.items():
        amount = sum(y["total_cny"] for y in years)
        totals[route] = {"three_year_total_cny": amount, "three_year_labor_cny": sum(y["labor_cny"] for y in years), "three_year_nonlabor_outlay_cny": sum(y["nonlabor_outlay_cny"] for y in years), "three_year_token_cny": sum(sum(v for k,v in y.items() if k.startswith("token_")) for y in years), "cny_per_target_accepted_task_conditional": amount/tasks3 if tasks3 else None, "capacity_envelope_pass": all(x["capacity_envelope_pass"] for x in state["local"]) if route == "local" else None}
    return {"scale": scale, "volume": volume, "measured_task_quality_pass": None, "measured_service_level_pass": None, "budget_status": "conditional_on_quality_and_service_envelope", "three_year_target_tasks": tasks3, "annual_capacity_target_tasks_per_node_under_assumptions": capacity, "per_target_task_work": work, "token_price_per_full_trajectory_cny": per, "annual": state, "totals": totals}


def sensitivity(p):
    changes = [
        ("local_cache_cold", lambda q: q["cache"].update(local_eligible_prefix_hit_probability=0)),
        ("all_cache_eligible_hit_50pct", lambda q: q["cache"].update(local_eligible_prefix_hit_probability=.5, deepseek_eligible_prefix_hit_probability=.5, claude_eligible_prefix_hit_probability=.5)),
        ("all_cache_eligible_hit_100pct", lambda q: q["cache"].update(local_eligible_prefix_hit_probability=1, deepseek_eligible_prefix_hit_probability=1, claude_eligible_prefix_hit_probability=1)),
        ("retry_zero", lambda q: q["trajectory"].update(extra_full_trajectory_equivalents_per_target_task=0)),
        ("retry_50pct", lambda q: q["trajectory"].update(extra_full_trajectory_equivalents_per_target_task=.5)),
        ("rounds_4", lambda q: q["trajectory"].update(rounds=4)),
        ("rounds_16", lambda q: q["trajectory"].update(rounds=16)),
        ("output_8k_each_round", lambda q: q["trajectory"].update(output_tokens_per_round_including_thinking_and_tool_arguments=8000)),
        ("service_window_8760h", lambda q: (q.update(service_hours_per_year=8760), q["scale"]["personal"]["local"].update(powered_hours_per_year=8760))),
        ("long_500k_12round_16knew_4kout", lambda q: q["trajectory"].update(initial_input_tokens=500000, rounds=12, new_user_tool_tokens_per_followup=16000, output_tokens_per_round_including_thinking_and_tool_arguments=4000)),
        ("deepseek_all_offpeak", lambda q: q["api"]["deepseek"].update(fraction_peak=0)),
        ("deepseek_all_peak", lambda q: q["api"]["deepseek"].update(fraction_peak=1)),
        ("claude_5min_write", lambda q: q["cache"].update(claude_write_ttl_minutes=5)),
        ("claude_tokens_0_8", lambda q: q["cache"].update(claude_token_multiplier_vs_reference=.8)),
        ("claude_tokens_1_3", lambda q: q["cache"].update(claude_token_multiplier_vs_reference=1.3)),
        ("api_tax_zero", lambda q: q.update(api_tax_reserve_fraction=0)),
        ("api_tax_13pct", lambda q: q.update(api_tax_reserve_fraction=.13)),
        ("api_price_halves_each_year", lambda q: [q["api"][k].update(price_change_per_year=-.5) for k in ["deepseek", "claude"]]),
        ("api_price_doubles", lambda q: [q["api"][k].update(discount=-1) for k in ["deepseek", "claude"]]),
        ("api_security_allowance_50k_year", lambda q: [q["scale"][k]["api"].update(annual_security_premium_cny=50000) for k in ["personal", "company"]]),
        ("company_envelope_half", lambda q: q["scale"]["company"]["local"].update(planning_prefill_uncached_tokens_s=4000, planning_decode_output_tokens_s=200)),
        ("company_envelope_double", lambda q: q["scale"]["company"]["local"].update(planning_prefill_uncached_tokens_s=16000, planning_decode_output_tokens_s=800)),
        ("tariff_pue_low", lambda q: [q["scale"][k]["local"].update(electricity_cny_per_kwh=.6, pue=1.1) for k in ["personal", "company"]]),
        ("tariff_pue_high", lambda q: [q["scale"][k]["local"].update(electricity_cny_per_kwh=1.2, pue=1.6) for k in ["personal", "company"]]),
        ("hardware_low", lambda q: [q["scale"][k]["local"].update(hardware_mid_cny=q["scale"][k]["local"]["hardware_range_cny"][0]) for k in ["personal", "company"]]),
        ("hardware_high", lambda q: [q["scale"][k]["local"].update(hardware_mid_cny=q["scale"][k]["local"]["hardware_range_cny"][1]) for k in ["personal", "company"]]),
        ("operations_person_days_half", lambda q: [q["scale"][k][r].update(annual_operations_person_days=q["scale"][k][r]["annual_operations_person_days"]*.5) for k in ["personal", "company"] for r in ["local", "api"]]),
        ("operations_person_days_double", lambda q: [q["scale"][k][r].update(annual_operations_person_days=q["scale"][k][r]["annual_operations_person_days"]*2) for k in ["personal", "company"] for r in ["local", "api"]])
    ]
    rows = []
    for name, change in changes:
        q = copy.deepcopy(p); change(q)
        for scale in ["personal", "company"]:
            r = calculate(q, scale)
            rows.append({"sensitivity": name, "scale": scale, "local_total_cny": r["totals"]["local"]["three_year_total_cny"], "deepseek_total_cny": r["totals"]["deepseek"]["three_year_total_cny"], "claude_total_cny": r["totals"]["claude"]["three_year_total_cny"], "local_nodes_year3": r["annual"]["local"][-1]["nodes"], "annual_capacity_per_node": r["annual_capacity_target_tasks_per_node_under_assumptions"], "capacity_evidence": "unknown_long_context_rate; company node count is only algebraic envelope" if "long_" in name else "engineering_envelope_or_Spark_fit; not task SLA measurement"})
    for row in rows:
        if row["sensitivity"].startswith("long_"):
            row["unvalidated_algebraic_local_cny"] = row["local_total_cny"]
            row["local_total_cny"] = None
            row["local_nodes_year3"] = None
            row["annual_capacity_per_node"] = None
            row["capacity_evidence"] = "long-context service rates unmeasured; no qualified local task cost or node count"
    return rows


def break_even(p, scale, provider):
    # Algebraic one-node crossing; then check that crossing against all three years.
    r0 = calculate(p, scale, year1_override=0, fixed_one_node=True)
    r1 = calculate(p, scale, year1_override=1, fixed_one_node=True)
    delta0 = r0["totals"]["local"]["three_year_total_cny"]-r0["totals"][provider]["three_year_total_cny"]
    delta1 = r1["totals"]["local"]["three_year_total_cny"]-r1["totals"][provider]["three_year_total_cny"]
    slope = delta1-delta0
    y1 = -delta0/slope if slope < 0 else None
    at = calculate(p, scale, year1_override=y1, fixed_one_node=True) if y1 else None
    return {"scale": scale, "provider": provider, "one_node_algebraic_year1_tasks": y1, "one_node_algebraic_three_year_tasks": at["three_year_target_tasks"] if at else None, "fits_one_node_annual_envelope": at["totals"]["local"]["capacity_envelope_pass"] if at else False, "annual_capacity_per_node": r1["annual_capacity_target_tasks_per_node_under_assumptions"], "interpretation": "只在同质量、同服务和固定费率下成立；超出机器包络的交点不能作为可实现回本量"}


def write_csv(name, records):
    fields = list(dict.fromkeys(k for row in records for k in row))
    with (HERE/name).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(records)


def main():
    rows = trajectory(INPUT)
    results = [calculate(INPUT, scale, volume) for scale in ["personal", "company"] for volume in ["low", "base", "high"]]
    a100 = []
    for kind in ["new", "reuse"]:
        q = copy.deepcopy(INPUT)
        a, spec = q["scale"]["company"]["local"], q["a100_sensitivity"]
        a.update(hardware_mid_cny=spec["new_hardware_mid_cny"] if kind == "new" else spec["reuse_incremental_refit_cny"], implementation_person_days=spec["implementation_person_days"], annual_operations_person_days=spec["annual_operations_person_days"], wall_active_kw=spec["wall_active_kw"], wall_idle_kw=spec["wall_idle_kw"])
        if kind == "reuse":
            a["annual_software_support_cny"] += spec["reuse_annual_support_cny"]
        r = calculate(q, "company", fixed_one_node=True)
        # A100 power allowance is independent of unverified service throughput.
        for year in r["annual"]["local"]:
            old = year["electricity_cny"]
            year["electricity_cny"] = spec["budget_average_wall_kw"]*a["powered_hours_per_year"]*a["pue"]*a["electricity_cny_per_kwh"]
            delta = year["electricity_cny"]-old
            year["total_cny"] += delta
            year["nonlabor_outlay_cny"] += delta
            year["capacity_envelope_pass"] = None
            for key in ["required_nodes_under_envelope", "busy_hours", "busy_fraction_service_hours_per_node", "prefill_work_hours", "decode_work_hours", "required_average_uncached_prefill_tps", "required_average_output_tps"]:
                year[key] = None
        total = r["totals"]["local"]
        total["three_year_total_cny"] = sum(y["total_cny"] for y in r["annual"]["local"])
        total["three_year_nonlabor_outlay_cny"] = sum(y["nonlabor_outlay_cny"] for y in r["annual"]["local"])
        total["capacity_envelope_pass"] = None
        total["cny_per_target_accepted_task_conditional"] = None
        r["annual_capacity_target_tasks_per_node_under_assumptions"] = None
        r["per_target_task_work"] = None
        r["budget_status"] = "cost_only_capacity_and_service_unverified"
        a100.append({"kind": kind, "result": r, "status": spec["capacity_status"], "same_envelope_is_not_asserted": True})
    curves = []
    for scale, steps in [("personal", range(100, 10101, 100)), ("company", range(5000, 1000001, 5000))]:
        for v in steps:
            r = calculate(INPUT, scale, year1_override=v)
            curves.append({"scale": scale, "year1_tasks": v, "tasks_3yr": r["three_year_target_tasks"], "local_cny": r["totals"]["local"]["three_year_total_cny"], "deepseek_cny": r["totals"]["deepseek"]["three_year_total_cny"], "claude_cny": r["totals"]["claude"]["three_year_total_cny"], "nodes_year1": r["annual"]["local"][0]["nodes"], "nodes_year3": r["annual"]["local"][-1]["nodes"], "envelope_not_task_SLA": True})
    times = []
    for r in [x for x in results if x["volume"] == "base"]:
        for m in INPUT["manual_time_sensitivity"]["net_minutes_saved_per_target_task"]:
            hours = r["three_year_target_tasks"]*m/60
            for conversion in INPUT["manual_time_sensitivity"]["cash_conversion_fraction"]:
                times.append({"scale": r["scale"], "net_minutes_saved_per_task": m, "hours_released_3yr": hours, "illustrative_time_value_cny": hours*INPUT["manual_time_sensitivity"]["illustrative_cny_per_hour"], "cash_conversion_fraction": conversion, "conditional_cash_saving_cny": hours*INPUT["manual_time_sensitivity"]["illustrative_cny_per_hour"]*conversion})
    summary = [{"scale": r["scale"], "volume": r["volume"], "tasks_3yr": r["three_year_target_tasks"], "route": route, **v} for r in results for route,v in r["totals"].items()]
    annual = [{"scale": r["scale"], "volume": r["volume"], "route": route, **year} for r in results for route,years in r["annual"].items() for year in years]
    sensitivities = sensitivity(INPUT)
    break_evens = [break_even(INPUT, s, provider) for s in ["personal", "company"] for provider in ["deepseek", "claude"]]
    source_paths = [HERE/"inputs.json", KB/"sources/TECH-090/deepseek-pricing.md", KB/"sources/TECH-090/claude-pricing.md", HERE.parent/"hardware-prices-2026-10-12.json", HERE.parent/"week7-deployment-2026-10-12/results.json", KB/"sources/TECH-092/api/deepseek-open-platform-terms.md", KB/"sources/TECH-092/api/anthropic-sales-2025.md", KB/"sources/TECH-092/api/deepseek-1017-news.md", HERE.parent/"final-source-refresh-2026-10-20/model-artifact-comparison.json"]
    artifact = {"as_of": INPUT["as_of"], "round_ledger": rows, "cases": results, "sensitivity": sensitivities, "break_even": break_evens, "a100_budget_only": a100, "time_value_separate_from_cash": times, "source_sha256": {str(p.relative_to(KB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}, "new_gpu_execution": False}
    (HERE/"results.json").write_text(json.dumps(artifact, ensure_ascii=False, indent=2)+"\n")
    bars = []
    for case in [c for c in results if c["volume"] == "base"]:
        for route, years in case["annual"].items():
            groups = {"硬件与设施": ["hardware_cny", "common_tool_hardware_cny", "facility_initial_cny"], "实施人工": ["implementation_labor_cny"], "持续运维人工": ["operations_labor_cny"], "用电机位软件": ["electricity_cny", "common_tool_electricity_cny", "rack_cny", "software_support_cny", "platform_cny", "security_premium_cny", "network_cny"]}
            for label, keys in groups.items():
                val = sum(y.get(k, 0) for y in years for k in keys)
                bars.append({"scale": case["scale"], "route": route, "category": label, "cny": val, "wan_cny": val/10000, "target_tasks_3yr": case["three_year_target_tasks"]})
            tools_val = sum(y.get("provider_tools_cny", 0) for y in years)
            bars.append({"scale": case["scale"], "route": route, "category": "供应商联网工具", "cny": tools_val, "wan_cny": tools_val/10000, "target_tasks_3yr": case["three_year_target_tasks"]})
            val = sum(v for y in years for k,v in y.items() if k.startswith("token_"))
            bars.append({"scale": case["scale"], "route": route, "category": "API token费", "cny": val, "wan_cny": val/10000, "target_tasks_3yr": case["three_year_target_tasks"]})
            assert abs(sum(b["cny"] for b in bars if b["scale"] == case["scale"] and b["route"] == route)-case["totals"][route]["three_year_total_cny"]) < 1e-6
    for filename, records in [("presentation-bars.csv", bars), ("round-ledger.csv", rows), ("summary.csv", summary), ("annual-costs.csv", annual), ("sensitivity.csv", sensitivities), ("volume-curve.csv", curves), ("time-value.csv", times)]:
        write_csv(filename, records)
    assert all(a["result"]["totals"]["local"]["capacity_envelope_pass"] is None and a["result"]["totals"]["local"]["cny_per_target_accepted_task_conditional"] is None for a in a100)
    assert all(s["local_total_cny"] is None for s in sensitivities if s["sensitivity"].startswith("long_"))
    assert sum(x["submitted_input"] for x in rows) == 1080000
    assert sum(x["new_external_input"] for x in rows) == 156000
    assert sum(x["output"] for x in rows) == 16000
    assert all(abs(x["deepseek_hit"]+x["deepseek_miss"]-x["submitted_input"]) < 1e-8 for x in rows)
    assert all(abs(x["claude_hit"]+x["claude_write"]-x["submitted_input"]) < 1e-8 for x in rows)
    assert all(abs(x["local_hit"]+x["local_prefill"]-x["submitted_input"]) < 1e-8 for x in rows)
    assert all(y["busy_fraction_service_hours_per_node"] <= INPUT["planning_utilization_ceiling"]+1e-9 for r in results for y in r["annual"]["local"])
    assert all(abs(sum(y["total_cny"] for y in r["annual"][route])-r["totals"][route]["three_year_total_cny"]) < 1e-6 for r in results for route in r["totals"])
    check = {"status": "passed", "checks": ["8轮context与新增token各记一次", "每轮输入=cache hit+miss/write", "含重试的输入输出与工作量同口径", "三年分项合计与总额一致", "容量按prefill与decode工时相加后检查70%包络", "公司高情景自动预算扩容，A100预算未标记验收通过", "无GPU或付费API调用"], "cases": len(results), "annual_rows": len(annual), "sensitivity_rows": len(sensitivities), "curve_rows": len(curves)}
    (HERE/"validation.json").write_text(json.dumps(check, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"validation": check, "summary": summary, "break_even": break_evens}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
