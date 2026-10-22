"""Independent Decimal reversal of published TCO; does not import calculate.py.

Uses closed-form arithmetic-series token totals, derives each year's node count,
then reconstructs cash/resource rows and break-even from fixed + variable costs.
"""
import csv
import hashlib
import json
import re
from decimal import Decimal as D, ROUND_CEILING
from pathlib import Path

HERE = Path(__file__).resolve().parent
KB = HERE.parents[2]
P = json.loads((HERE/"inputs.json").read_text())
R = json.loads((HERE/"results.json").read_text())
S = json.loads((HERE.parent/"week7-deployment-2026-10-12/results.json").read_text())["spark_fit"]
N = lambda x: D(str(x))
Q = P["trajectory"]
n, a, u, o = map(N, [Q["rounds"], Q["initial_input_tokens"], Q["new_user_tool_tokens_per_followup"], Q["output_tokens_per_round_including_thinking_and_tool_arguments"]])
d = u+o
s1 = n*(n-1)/2
s2 = n*(n-1)*(2*n-1)/6
input_sum = n*a+d*s1
input_sq = n*a*a+2*a*d*s1+d*d*s2
eligible_ds = input_sum-a-(n-1)*u
eligible_ds_sq = input_sq-a*a-2*u*(input_sum-a)+(n-1)*u*u
eligible_cl = input_sum-(a+(n-1)*d)
repeat = 1+N(Q["extra_full_trajectory_equivalents_per_target_task"])
fx_tax = N(P["fx_usd_cny"])*(1+N(P["api_tax_reserve_fraction"]))
per = {"input": input_sum, "new_external": a+(n-1)*u, "output": n*o, "deepseek_hit": eligible_ds*N(P["cache"]["deepseek_eligible_prefix_hit_probability"]), "claude_hit": eligible_cl*N(P["cache"]["claude_eligible_prefix_hit_probability"]), "local_hit": eligible_ds*N(P["cache"]["local_eligible_prefix_hit_probability"])}
per["deepseek_miss"] = per["input"]-per["deepseek_hit"]
per["claude_write"] = per["input"]-per["claude_hit"]
per["local_prefill"] = per["input"]-per["local_hit"]
ds_rates = P["api"]["deepseek"]["offpeak"]
peak = 1+N(P["api"]["deepseek"]["fraction_peak"])*(N(P["api"]["deepseek"]["peak_multiplier"])-1)
cl_rates = P["api"]["claude"]["rates"]
units = {"deepseek": (per["deepseek_miss"]*N(ds_rates["input_miss"])+per["deepseek_hit"]*N(ds_rates["input_hit"])+per["output"]*N(ds_rates["output"]))/D(1000000)*peak*fx_tax*repeat,
         "claude": (per["claude_write"]*N(cl_rates["cache_write_1h"])+per["claude_hit"]*N(cl_rates["input_hit"])+per["output"]*N(cl_rates["output"]))/D(1000000)*fx_tax*repeat}


def close(actual, expected, label, tolerance="0.02"):
    assert abs(N(actual)-expected) <= D(tolerance), (label, str(actual), str(expected))


def work(scale):
    if scale == "company":
        hw = P["scale"][scale]["local"]
        return repeat*(per["local_prefill"]/N(hw["planning_prefill_uncached_tokens_s"])+per["output"]/N(hw["planning_decode_output_tokens_s"]))
    f_all = N(S["prefill_a_seconds_per_million"])*input_sum/D(1000000)+N(S["prefill_b_seconds_per_million_squared"])*input_sq/D(10**12)
    f_old = N(S["prefill_a_seconds_per_million"])*eligible_ds/D(1000000)+N(S["prefill_b_seconds_per_million_squared"])*eligible_ds_sq/D(10**12)
    decode = o*(n*N(S["decode_step_a_seconds"])+N(S["decode_step_b_seconds_per_million"])*(input_sum+n*o/2)/D(1000000))
    return repeat*(f_all-N(P["cache"]["local_eligible_prefix_hit_probability"])*f_old+decode)


def local_year(scale, tasks, nodes, old_nodes, year):
    s = P["scale"][scale]
    hw, c = s["local"], s["common"]
    added = nodes-old_nodes
    busy = tasks*work(scale)/D(3600)
    electric = (N(nodes)*N(hw["wall_idle_kw"])*N(hw["powered_hours_per_year"])+(N(hw["wall_active_kw"])-N(hw["wall_idle_kw"]))*busy)*N(hw["pue"])*N(hw["electricity_cny_per_kwh"])
    common_power = N(c["tool_cpu_average_kw"])*N(c["tool_cpu_powered_hours"])*N(c["pue"])*N(c["tariff"])
    impl_days = (N(hw["implementation_person_days"])+N(nodes-1)*N(hw.get("expansion_implementation_person_days", hw["implementation_person_days"]))) if year == 1 else N(added)*N(hw.get("expansion_implementation_person_days", hw["implementation_person_days"]))
    ops_days = N(hw["annual_operations_person_days"])+N(nodes-1)*N(hw.get("annual_operations_person_days_per_additional_node", hw["annual_operations_person_days"]))
    total = N(added)*(N(hw["hardware_mid_cny"])+N(hw["facility_initial_cny"]))+N(c["tool_cpu_capex_cny"] if year == 1 else 0)+(impl_days+ops_days)*N(P["person_day_cny"])+electric+common_power+N(nodes)*(N(hw["annual_rack_excluding_power_cny"])+N(hw["annual_software_support_cny"]))
    return total


def api_fixed(scale):
    s=P["scale"][scale];b=s["api"];c=s["common"]
    common_power=N(c["tool_cpu_average_kw"])*N(c["tool_cpu_powered_hours"])*N(c["pue"])*N(c["tariff"])
    return N(c["tool_cpu_capex_cny"])+N(b["implementation_person_days"])*N(P["person_day_cny"])+3*(N(b["annual_operations_person_days"])*N(P["person_day_cny"])+N(b["annual_platform_cny"])+N(b["annual_security_premium_cny"])+N(b["annual_incremental_network_cny"])+common_power)


annual_tokens=[];three_year=[];audit_cases=[]
for case in R["cases"]:
    scale, volume=case["scale"],case["volume"]
    spec=P["scale"][scale]["volume_scenarios"][volume]
    capacity=N(P["service_hours_per_year"])*3600*N(P["planning_utilization_ceiling"])/work(scale)
    close(case["annual_capacity_target_tasks_per_node_under_assumptions"],capacity,"annual capacity")
    count=D(0);old=0;nodes_by_year=[]
    for year in range(1,4):
        tasks=N(spec["year1_target_tasks"])*(1+N(spec["annual_growth"]))**(year-1)
        count+=tasks
        nodes=max(1,int((tasks/capacity).to_integral_value(rounding=ROUND_CEILING)))
        nodes_by_year.append(nodes)
        published=case["annual"]["local"][year-1]
        close(published["target_tasks"],tasks,"growth")
        assert published["nodes"] == nodes
        close(published["total_cny"],local_year(scale,tasks,nodes,old,year),"independent local year")
        old=nodes
        volumes={k:val*tasks*repeat for k,val in per.items()}
        annual_tokens.append({"scale":scale,"volume":volume,"year":year,"target_tasks":str(tasks),"nodes_under_assumed_envelope":nodes,**{k+"_tokens":str(v) for k,v in volumes.items()}})
        for provider in units:
            paid=case["annual"][provider][year-1]
            token_amount=sum(N(v) for k,v in paid.items() if k.startswith("token_"))
            close(token_amount,tasks*units[provider],"annual token charge")
            assert paid["provider_tools_cny"] == 0
        for route,years in case["annual"].items():
            y=years[year-1]
            subtotal=sum(N(v) for k,v in y.items() if k.endswith("_cny") and k not in ["total_cny","labor_cny","nonlabor_outlay_cny"])
            close(y["total_cny"],subtotal,"annual sum")
    three_year.append({"scale":scale,"volume":volume,"target_tasks":str(count),**{k+"_tokens":str(val*count*repeat) for k,val in per.items()},"nodes_by_year":"/".join(map(str,nodes_by_year))})
    for provider in units:
        close(case["totals"][provider]["three_year_total_cny"],api_fixed(scale)+count*units[provider],"independent three-year API")
    for route,detail in case["totals"].items():
        close(detail["cny_per_target_accepted_task_conditional"],N(detail["three_year_total_cny"])/count,"cost per target task", ".0000001")
    audit_cases.append({"scale":scale,"volume":volume,"tasks":str(count),"nodes_by_year":nodes_by_year,"input_tokens_including_extra_trajectories":str(per["input"]*count*repeat),"output_tokens_including_extra_trajectories":str(per["output"]*count*repeat),"local_full_TCO_cny":case["totals"]["local"]["three_year_total_cny"],"deepseek_full_TCO_cny":case["totals"]["deepseek"]["three_year_total_cny"],"claude_global_counterfactual_TCO_cny":case["totals"]["claude"]["three_year_total_cny"]})

crossings=[]
for published in R["break_even"]:
    scale,provider=published["scale"],published["provider"]
    hw=P["scale"][scale]["local"]
    fixed=sum(local_year(scale,D(0),1,0 if y==1 else 1,y) for y in [1,2,3])
    variable=work(scale)/D(3600)*(N(hw["wall_active_kw"])-N(hw["wall_idle_kw"]))*N(hw["pue"])*N(hw["electricity_cny_per_kwh"])
    crossing=(fixed-api_fixed(scale))/(units[provider]-variable)
    growth=N(P["scale"][scale]["volume_scenarios"]["base"]["annual_growth"])
    year1=crossing/sum((1+growth)**i for i in [0,1,2])
    close(published["one_node_algebraic_three_year_tasks"],crossing,"closed-form crossing", ".01")
    close(published["one_node_algebraic_year1_tasks"],year1,"crossing annual growth", ".01")
    capacity=N(P["service_hours_per_year"])*3600*N(P["planning_utilization_ceiling"])/work(scale)
    fits=year1*(1+growth)**2 <= capacity
    assert published["fits_one_node_annual_envelope"] == fits
    close(fixed+crossing*variable,api_fixed(scale)+crossing*units[provider],"cost equality at crossing", ".000001")
    crossings.append({"scale":scale,"provider":provider,"closed_form_three_year_tasks":str(crossing),"fits_assumed_one_node_envelope":fits})

# Every curve point is independently reconstructed including capacity steps.
with (HERE/"volume-curve.csv").open() as f:
    for point in csv.DictReader(f):
        scale=point["scale"];growth=N(P["scale"][scale]["volume_scenarios"]["base"]["annual_growth"])
        cap=N(P["service_hours_per_year"])*3600*N(P["planning_utilization_ceiling"])/work(scale)
        old=0;local=D(0);tasktotal=D(0)
        for year in [1,2,3]:
            tasks=N(point["year1_tasks"])*(1+growth)**(year-1)
            nodes=max(1,int((tasks/cap).to_integral_value(rounding=ROUND_CEILING)))
            local+=local_year(scale,tasks,nodes,old,year);old=nodes;tasktotal+=tasks
        close(point["local_cny"],local,"curve cost with expansion")
        for provider in units:
            close(point[provider+"_cny"],api_fixed(scale)+tasktotal*units[provider],"curve API")

ledger=json.loads((HERE.parent/"hardware-prices-2026-10-12.json").read_text())
server=next(x for x in ledger["server_cases"] if x["id"]=="H2008-SXM")
close(P["scale"]["company"]["local"]["hardware_mid_cny"],sum(N(x) for x in server["total_cny"])/2,"hardware ledger")
for relative,sha in R["source_sha256"].items():
    assert hashlib.sha256((KB/relative).read_bytes()).hexdigest()==sha
for case in R["a100_budget_only"]:
    assert case["result"]["totals"]["local"]["cny_per_target_accepted_task_conditional"] is None
    assert case["result"]["totals"]["local"]["capacity_envelope_pass"] is None
for s in R["sensitivity"]:
    if s["sensitivity"].startswith("long_"):
        assert s["local_total_cny"] is None and s["local_nodes_year3"] is None
for file in [KB/"infrastructure/tco-analysis-2026-10-20.md",HERE/"README.md",KB/"sources/TECH-090/original.md"]:
    for target in re.findall(r'\]\(([^)]+)\)',file.read_text()):
        if '://' not in target:
            assert (file.parent/target).exists(),(str(file),target)
metadata=json.loads((KB/"sources/TECH-090/metadata.json").read_text())
for name,detail in metadata["files"].items():
    assert hashlib.sha256((KB/"sources/TECH-090"/name).read_bytes()).hexdigest()==detail["sha256"]

for name,rows in [("annual-token-volumes.csv",annual_tokens),("three-year-token-volumes.csv",three_year)]:
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
audit={"status":"passed","method":"Independent Decimal closed-form token series and fixed/variable cost reversal; no import of calculate.py","per_target_task_tokens_including_extra_trajectories":{k:str(v*repeat) for k,v in per.items()},"independent_decimal_per_target_task_cny":{k:str(v) for k,v in units.items()},"case_audit":audit_cases,"break_even_audit":crossings,"checks":["低中高三年增长与输入、缓存写读、输出独立反算","54行年度分项与每任务成本复核","301行曲线按整数节点扩容逐项复核","四个固定+变动成本临界值独立反推并验证容量","供应商Search/Fetch基准调用为0，本地工具无供应商附加费","A100与长context未测合格任务成本保持null","来源SHA-256与正文文件链接有效"],"company_planning_rate_identity":"400 decode + 8000 uncached prefill tokens/s is an assumed envelope for 100K–170K trajectory, not 1M measured throughput","new_external_calls":False}
(HERE/"independent-audit.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({"status":"passed","case_audit":audit_cases,"break_even_audit":crossings},ensure_ascii=False,indent=2))
