"""CPU-only, standard-library analysis; no model/network/GPU execution.

Published token pools already include that runtime's allocation decisions.
Apply an explicit 10% token-working-set reserve to those pools; do not add a second
15% byte-layout reserve. Static source-derived byte layouts are a separate audit.
"""
import csv
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
KB = HERE.parents[2]
SOURCES = KB / "sources"
CONTEXTS = [131072, 262144, 524288, 1000000]
ACTIVES = [1, 5, 20, 30, 50]
OUT = 8192
RESERVE = 0.10


def read(path):
    return json.loads(path.read_text())


def fit_two_columns(x1, x2, y):
    a, b, c = sum(v*v for v in x1), sum(u*v for u, v in zip(x1, x2)), sum(v*v for v in x2)
    d, e = sum(u*v for u, v in zip(x1, y)), sum(u*v for u, v in zip(x2, y))
    det = a*c-b*b
    return (d*c-b*e)/det, (a*e-b*d)/det


def round_up(n, unit):
    return math.ceil(n/unit)*unit


def main():
    source_paths = [SOURCES / "TECH-079/config.json", SOURCES / "TECH-079/model.safetensors.index.json", SOURCES / "TECH-084/benchmarks.json", HERE.parent / "dgx-spark-qwen27-external-2026-10-12/summary.json"]
    config = read(source_paths[0])["text_config"]
    total_weights = read(source_paths[1])["metadata"]["total_size"]
    engram = sum(config["engram_num_embeddings"])*(config["engram_head_dim"]+config["engram_head_dim"]//32)
    raw = read(source_paths[2])
    groups = {}
    for hw, tp in [("h100", 8), ("h200", 4), ("h200", 8)]:
        rows = sorted([x for x in raw if x["hardware"] == hw and x["framework"] == "vllm" and x["decode_tp"] == tp and not x["disagg"] and x["model"] == "dsv41flash" and x["benchmark_type"] == "agentic_traces" and x["offload_mode"] == "off"], key=lambda x: x["conc"])
        groups[(hw, tp)] = rows

    def anchor(hw, tp, per_replica_active):
        eligible = [r for r in groups[(hw, tp)] if r["conc"] >= per_replica_active]
        return eligible[0] if eligible else None

    layouts = []
    for source, ratio in zip(config["kv_source_layer_ids"], [2, 2, 2, 1]):
        main_bytes = round_up((64//ratio)*584, 576)
        index_bytes = round_up((64//ratio)*132, 576)
        layouts.append({"source_layer": source, "ratio": ratio, "main_page_bytes": main_bytes, "index_page_bytes": index_bytes})
    bytes_per_token = sum(x["main_page_bytes"]+x["index_page_bytes"] for x in layouts)/64
    swa_per_active_rank = (40+3)*math.ceil((128+5+1)/32)*round_up(32*584, 576)

    hardware = [("H100-8-TP8", "h100", 8, 1), ("H200-4-TP4", "h200", 4, 1), ("H200-8-TP8", "h200", 8, 1), ("H200-8-2xTP4", "h200", 4, 2), ("H100-16-2xTP8", "h100", 8, 2), ("H100-24-3xTP8", "h100", 8, 3), ("H100-32-4xTP8", "h100", 8, 4)]
    rows, limits = [], []
    for hid, hw, tp, replicas in hardware:
        for active in ACTIVES:
            per = math.ceil(active/replicas)
            a = anchor(hw, tp, per)
            pool = a["metrics"]["kv_cache_pool_tokens"] if a else None
            for resident_multiplier in [1, 2]:
                resident = resident_multiplier*active
                rper = math.ceil(resident/replicas)
                maxc = min(1000000, int((pool*(1-RESERVE)/rper)//64)*64) if pool else None
                limits.append({"hardware":hid,"gpus":tp*replicas,"replicas":replicas,"tp":tp,"active_requests":active,"resident_sessions":resident,"max_context_capacity_only":maxc,"input_budget_at_max":max(0,maxc-OUT) if maxc else None,"anchor_id":a['id'] if a else None,"anchor_concurrency":a['conc'] if a else None,"pool_tokens_per_replica":pool,"operational_reserve_fraction":RESERVE,"speed_verified_at_target_context":False})
                for c in CONTEXTS:
                    rows.append({**limits[-1],"context_tokens":c,"history_input_tokens":c-OUT,"output_reserve":OUT,"fits_cache_budget":rper*c <= pool*(1-RESERVE) if pool else None,"required_system_decode_tps_for_10_per_user":active*10,"required_system_decode_tps_for_20_per_user":active*20,"required_global_kv_bytes_each_rank_static_layout":rper*c*bytes_per_token,"cold_ttft_seconds":None,"warm_1k_p95_seconds":None,"decode_tps_at_target_context":None,"experience_status":"requires matched full-context measurement; capacity only"})

    maxusers = []
    for hid, hw, tp, replicas in hardware:
        for c in CONTEXTS:
            for margin in [0.0, RESERVE]:
                feasible = []
                for users in range(1, 257):
                    per = math.ceil(users/replicas)
                    a = anchor(hw, tp, per)
                    if a and per*c <= a['metrics']['kv_cache_pool_tokens']*(1-margin):
                        feasible.append(users)
                maxusers.append({"hardware":hid,"context_tokens":c,"reserve_fraction":margin,"max_active_and_resident_users_capacity_only":max(feasible,default=0),"pool_selection":"next observed concurrency at or above active users per replica"})

    spark = read(source_paths[3])
    # Cold engine durations from the provided prefill-rate denominators.
    n = [50000, 100000, 300000, 500000]
    rate = [795.1, 691.7, 455.6, 340.3]
    seconds = [x/r for x, r in zip(n,rate)]
    # Scale N by one million for numerical conditioning.
    a,b = fit_two_columns([x/1e6 for x in n], [(x/1e6)**2 for x in n], seconds)
    d_n = [100000,300000,500000]
    d_t = [1/20.11,1/17.23,1/14.82]
    da,db = fit_two_columns([1,1,1], [x/1e6 for x in d_n], d_t)
    F = lambda x: a*x/1e6+b*(x/1e6)**2
    tokenpool = spark['startup']['estimated_shared_kv_token_pool']
    poolbytes = spark['startup']['kv_pool_gib']*2**30
    spark_rows = []
    for kv,bpt,pool in [('fp8',32768,tokenpool),('bf16',65536,tokenpool//2)]:
        for resident,active in [(1,1),(3,1),(3,3)]:
            for c in CONTEXTS:
                inp = c-OUT
                spark_rows.append({"kv":kv,"resident_sessions":resident,"active_requests":active,"context_tokens":c,"input_history_tokens":inp,"pure_attention_kv_bytes":resident*c*bpt,"pool_tokens":pool,"pool_identity":"observed FP8 service" if kv=='fp8' else "engineering proxy: halve FP8 token pool, preserving non-token overhead; reload must verify", "fits_capacity_proxy_with_10pct_reserve":resident*c <= pool*(1-RESERVE),"pure_kv_fits_measured_59_73_gib_pool":resident*c*bpt <= poolbytes,"single_fp8_mtp3_decode_shape_estimate":1/(da+db*(c-OUT/2)/1e6) if kv=='fp8' and active==1 else None,"shape_estimate_scope":"interpolation below 500K; extrapolation above; not direct measurement or p95", "single_fp8_cold_prefill_fit_seconds":F(inp) if kv=='fp8' and active==1 else None,"ideal_cache_1k_prefill_difference_seconds":F(inp)-F(inp-1024) if kv=='fp8' and active==1 else None,"ideal_cache_8k_prefill_difference_seconds":F(inp)-F(inp-8192) if kv=='fp8' and active==1 else None,"warm_ttft_measured":False,"single_user_20plus_verified_for_exact_case":False})

    selected = []
    for rid in ['442505','442757','442751','442750','442758']:
        r = next(x for x in raw if x['id']==rid);m=r['metrics']
        selected.append({k:r[k] for k in ['id','hardware','framework','decode_tp','num_decode_gpu','conc','image','date','run_url']} | {k:m.get(k) for k in ['mean_input_tokens','p95_input_tokens','mean_output_tokens_actual','output_tput_tps','input_tput_tps','total_tput_tps','median_intvty','mean_ttft','p95_ttft','server_gpu_cache_hit_rate','kv_cache_pool_tokens']} | {'acceptance':'synthetic 3.51; verified in startup log for H100-C20, H200-TP4-C32, H200-TP8-C32','scope':'AgentX multi-turn replay; concurrency is live sessions, not all are simultaneously generating; length is variable'})

    result={"as_of":"2026-10-12","evidence_policy":"No new GPU measurements; null SLA fields are intentionally unavailable.","source_sha256":{str(p.relative_to(KB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths},"deepseek_architecture":{"checkpoint_bytes":total_weights,"engram_host_bytes":engram,"non_engram_checkpoint_bytes":total_weights-engram,"logical_global_kv_bytes_per_token_production_fp4":890,"hopper_unpadded_global_kv_bytes_per_token":1790,"hopper_page_bytes_for_64_tokens":int(bytes_per_token*64),"hopper_padded_global_kv_bytes_per_token_each_tp_rank":bytes_per_token,"hopper_source_pages":layouts,"swa_dspark_per_active_rank_bytes_budget":swa_per_active_rank,"cache_replication":"Each TP rank owns the single KV latent and index; no division by TP in this analysis; DCP not assumed.","memory_budget_note":"The public token-pool anchors, not static 1827 B/token, drive admission. They incorporate their own runtime layout/grouping/graphs. Current static source serves as an audit and version-change sensitivity."},"capacity_limits":limits,"capacity_matrix":rows,"max_users_capacity_only":maxusers,"published_replay_examples":selected,"spark_fit":{"prefill_a_seconds_per_million":a,"prefill_b_seconds_per_million_squared":b,"decode_step_a_seconds":da,"decode_step_b_seconds_per_million":db,"prefill_fit_input_lengths":n,"prefill_fit_engine_seconds":seconds,"cold_fit_residual_seconds":[F(x)-y for x,y in zip(n,seconds)],"not_p95":True,"limits":"Cold fit is empirical shape interpolation; differencing assumes exact prefix/state reuse and no queue. No assertion that vLLM warm kernels have identical efficiency; no BF16-KV/MTP uplift inferred."},"spark_matrix":spark_rows}
    result['post_graph_budget_sensitivity'] = []
    for rid, allocated_gib, strict_gib, active_per_replica in [('442505',12.36,10.34,20),('442751',35.16,32.49,20),('442758',62.86,60.20,20),('442751',35.16,32.49,10)]:
        r = next(x for x in raw if x['id']==rid)
        adjusted = r['metrics']['kv_cache_pool_tokens']*strict_gib/allocated_gib
        result['post_graph_budget_sensitivity'].append({'anchor_id':rid,'allocated_kv_gib':allocated_gib,'post_graph_log_kv_gib_for_92pct_budget':strict_gib,'projected_reloaded_pool_tokens':int(adjusted),'active_per_replica':active_per_replica,'max_context_with_10pct_token_reserve':min(1000000,int(adjusted*.9/active_per_replica)//64*64),'scope':'Linear token-pool rescaling sensitivity; new allocator startup and graph capture must confirm. Reserving tokens within an allocated pool does not free HBM.'})
    (HERE/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    for filename,records in [('capacity-matrix.csv',rows),('spark-matrix.csv',spark_rows),('capacity-limits.csv',limits)]:
        with (HERE/filename).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    assert engram==202758032400
    assert total_weights==510286023000
    assert bytes_per_token==1827
    assert len(rows)==7*5*2*4
    assert len(spark_rows)==2*3*4
    assert all(x['history_input_tokens']+OUT==x['context_tokens'] for x in rows)
    assert all(x['max_context_capacity_only'] is None or x['max_context_capacity_only']<=1000000 for x in limits)
    assert all(x['cold_ttft_seconds'] is None and x['decode_tps_at_target_context'] is None for x in rows)
    assert all(abs(x)<1 for x in result['spark_fit']['cold_fit_residual_seconds'])
    validation={'status':'passed','checks':['source SHA-256 frozen','DeepSeek checkpoint and Engram byte arithmetic','Hopper four source page alignment','280 enterprise and 24 Spark rows','history plus 8192 output equals context','no unmeasured TTFT/decode populated','cold curve residual <1 second on the four input anchors'],'matrix_rows':len(rows),'spark_rows':len(spark_rows),'new_gpu_execution':False}
    (HERE/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(validation,ensure_ascii=False))


if __name__ == '__main__':
    main()
