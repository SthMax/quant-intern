#!/usr/bin/env python3
"""Deterministic source/arithmetic audit; never imports or runs upstream code.

Run from any directory with Python standard library only. Output is a research
calculation and source inventory, not a GPU benchmark or model-quality test.
"""
import ast
import csv
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[2] / "sources" / "TECH-077"
FILES = SOURCE / "files"
REVISION = "580568edd6f84537ff042ded4ee842b892bf3ff4"


def source_ref(name, start, end):
    return {
        "file": name,
        "lines": [start, end],
        "url": f"https://github.com/shi3z/deepseekv4.1-A100-custom/blob/{REVISION}/{name}#L{start}-L{end}",
    }


def main():
    cfg = json.loads((SOURCE / "official-inference-config.json").read_text())
    metadata = json.loads((SOURCE / "metadata.json").read_text())
    hashes = {
        name: hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
        for name in metadata["files"]
    }
    assert all(hashes[name] == row["sha256"] for name, row in metadata["files"].items())
    bench_src = (FILES / "dsv41/bench_jev.py").read_text()
    tree = ast.parse(bench_src)
    helper = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "run_jev_simulation_or_direct")
    runner = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    calls = [n for n in ast.walk(runner) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == helper.name]
    assert len(calls) == 2
    assert all(len(n.args) == 2 and not n.keywords for n in calls)
    constants = {}
    for n in helper.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) and isinstance(n.value, ast.Constant):
            constants[n.targets[0].id] = n.value.value
    assert {k: constants[k] for k in ("t_cache_hit_ms", "t_prefill_ms", "t_scoring_per_batch", "max_batch")} == {
        "t_cache_hit_ms": 0.08, "t_prefill_ms": 11.4, "t_scoring_per_batch": 12.5, "max_batch": 32
    }
    jev = []
    for fields, tokens, ar_ms, reported_tps in [(3,22,2018.8,917.4),(10,78,4204.1,3252.7),(30,238,9773.3,9924.9),(100,798,30745.8,12979.8)]:
        ms = constants["t_cache_hit_ms"] + constants["t_prefill_ms"] + math.ceil(fields / constants["max_batch"]) * constants["t_scoring_per_batch"]
        jev.append({"fields":fields,"readme_output_tokens":tokens,"hardcoded_total_ms":ms,"calculated_effective_tokens_s":tokens/(ms/1000),"readme_effective_tokens_s":reported_tps,"speedup_against_readme_ar_time":ar_ms/ms,"status":"simulation_default_path_not_measured_latency"})

    capacity = []
    for context in (131072,262144,524288,1000000,1048576):
        per_slot = sum((context // cfg["compress_ratios"][owner]+1) * (cfg["head_dim"]+cfg["index_head_dim"])*2 for owner in cfg["kv_source_layers"])
        for active in (1,5,8,20,30,50):
            slots = active + 1
            capacity.append({"context_tokens":context,"active_requests":active,"allocated_slots_including_scratch":slots,"compressed_kv_index_bytes_per_gpu_per_slot":per_slot,"compressed_kv_index_gib_per_gpu_all_slots":per_slot*slots/2**30,"four_gpu_aggregate_gib":per_slot*slots*4/2**30,"scope":"BF16 compressed KV and index keys only; full mirrors; no weights, SWA, graph, RoPE, scratch or DSpark"})

    one_expert_layer = 3*cfg["dim"]*cfg["moe_inter_dim"]*(0.5+1/32)
    expert_column = int(one_expert_layer*cfg["n_layers"])
    expert_memory = {"per_expert_per_layer_bytes":int(one_expert_layer),"per_expert_across_40_layers_bytes":expert_column,"per_expert_across_40_layers_gib":expert_column/2**30,"shards_92_95_99_98_gib":[expert_column*n/2**30 for n in (92,95,99,98)],"shards_100_100_100_84_gib":[expert_column*n/2**30 for n in (100,100,100,84)],"twelve_experts_freed_gib":12*expert_column/2**30,"engram_host_bytes":sum(cfg["engram_num_embeddings"])*(cfg["engram_head_dim"]+cfg["engram_head_dim"]//32),"assumption":"Official config dimensions applied to current loader shapes; author checkpoint was not received."}
    expert_memory["engram_host_gib"] = expert_memory["engram_host_bytes"]/2**30

    prefill = []
    for tokens, seconds, reported in [(2048,4.27,479.5),(4096,7.38,555.2),(8192,13.74,596.0),(32768,82.75,396.0),(65536,168.39,389.2),(131072,361.48,362.6),(262144,841.28,311.6),(524288,2156.68,243.1),(819200,4198.87,195.1),(983040,5582.28,176.1),(1000000,5729.20,174.54)]:
        prefill.append({"input_tokens":tokens,"readme_seconds":seconds,"calculated_tokens_s":tokens/seconds,"readme_tokens_s":reported,"status":"author_report_arithmetic_checked_raw_trace_absent"})
    concurrency = []
    for users,horizon,wall,peak in [(1,1048576,50.3,50.3),(2,1048576,70.7,78.2),(4,65536,86.8,98.4),(8,131072,119.2,119.9),(16,32768,127.4,269.3),(24,32768,141.4,321.9),(32,16384,159.8,376.5),(64,8192,167.5,475.6)]:
        concurrency.append({"workers":users,"configured_max_context":horizon,"actual_prompt_tokens":None,"readme_wall_output_tokens_s":wall,"readme_peak_engine_tokens_s":peak,"wall_divided_by_workers":wall/users,"peak_divided_by_workers":peak/users,"status":"author_report_short_prompts; horizons_are_not_actual_input; divisions_not_measured_per_user"})

    # A transparent arithmetic counterexample to the general proposition that
    # replaying W inputs through any number of W-window layers is exact.
    # This is NOT the DeepSeek network and measures no DeepSeek quality error.
    # The official report explicitly intends approximate bounded replay;
    # therefore this example explains that design, not a model/runtime bug.
    def sliding_average(values, window=2):
        return [sum(values[max(0,i-window+1):i+1])/len(values[max(0,i-window+1):i+1]) for i in range(len(values))]
    sequence = [1.0,2.0,3.0,4.0]
    full = sliding_average(sliding_average(sequence))[-1]
    tail = sliding_average(sliding_average(sequence[-2:]))[-1]
    assert full != tail
    ced = {"toy_model":"two causal sliding-average layers, window=2", "input":sequence,"full_last_output":full,"tail_only_last_output":tail,"equivalent":False,"custom_runtime_tail_layers":19,"official_architecture_decoder_layers":20,"actual_window":128,"single_last_output_receptive_span_custom_path":1+19*127,"all_final_128_states_conservative_input_span_custom_path":128+19*127,"interpretation":"Illustrates intentional approximate bounded replay, as declared in official report sections 2.2 and 3.2.2 (PDF pages 9 and 20). Non-equivalence itself is not a runtime bug or evidence of model failure. Does not quantify errors in DeepSeek logits or tasks; implementation truncation boundaries and task quality need separate verification. Global sparse inherited KV remains an additional attention branch."}
    sources = {
        "jev_default_cli":source_ref("dsv41/bench_jev.py",196,293),
        "jev_main_calls_and_consistency":source_ref("dsv41/bench_jev.py",302,378),
        "jev_actual_http_benchmark":source_ref("examples/benchmarks/bench_jev_structured.py",158,242),
        "jev_first_token_scoring":source_ref("dsv41/jev.py",505,544),
        "full_mirror_allocation":source_ref("dsv41/load.py",286,421),
        "expert_allocation":source_ref("dsv41/load.py",181,208),
        "ced_sequential":source_ref("dsv41/model.py",2349,2407),
        "ced_pipeline":source_ref("dsv41/model.py",2517,2550),
        "global_attention_at_ratio_one":source_ref("dsv41/model.py",1263,1319),
        "serial_prefill_then_decode":source_ref("dsv41/engine.py",4415,4574),
        "buffered_chat_stream":source_ref("dsv41/serve.py",237,267),
        "peak_metric":source_ref("dsv41/stats.py",403,449),
    }
    result = {"as_of":"2026-10-12","upstream_revision":REVISION,"official_structural_reference_revision":metadata["official_config"]["revision"],"execution":"Only this standard-library audit ran; no upstream import, API benchmark, model or GPU execution.","source_sha256":hashes,"jev_default_path":{"call_lines":[n.lineno for n in calls],"constants":constants,"rows":jev},"capacity":capacity,"weight_storage":expert_memory,"readme_prefill_arithmetic":prefill,"readme_concurrency":concurrency,"ced_dependency_counterexample":ced,"one_million_chunk_arithmetic":{"full_chunks":1000000//2048,"correct_tail":1000000%2048,"readme_tail":496,"readme_sum":488*2048+496},"source_anchors":sources,"validation":{"all_source_hashes_match":True,"jev_default_calls_exclude_engine":True,"hardcoded_formula_verified":True,"toy_receptive_field_counterexample_passed":True,"gpu_performance_reproduced":False}}
    (HERE/"audit-results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    for name,rows in [("cache-capacity",capacity),("readme-prefill",prefill),("readme-concurrency",concurrency),("jev-formula",jev)]:
        with (HERE/f"{name}.csv").open("w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print(json.dumps({"source_files_verified":len(hashes),"capacity_cases":len(capacity),"prefill_claims_checked":len(prefill),"concurrency_claims_catalogued":len(concurrency),"jev_cases":len(jev),"gpu_benchmark_run":False},ensure_ascii=False))


if __name__ == "__main__":
    main()
