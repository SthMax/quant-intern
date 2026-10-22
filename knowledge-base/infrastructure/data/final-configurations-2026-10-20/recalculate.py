"""Final presentation data: CPU-only arithmetic, no inference or network calls."""
import csv
import hashlib
import importlib.util
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
KB = HERE.parents[2]
SOURCES = KB / 'sources'
OLD = HERE.parent / 'week7-deployment-2026-10-12'
RAG = HERE.parent / 'scenario-2-rag-2026-09-23'
CONTEXTS = [131072, 262144, 524288, 1000000]
OUTPUT = 8192
RESERVE = .10
GIB = 2**30

def read(p):
    return json.loads(p.read_text())

def write(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def csvout(name, rows):
    with (HERE / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

def main():
    old = read(OLD / 'results.json')
    measured = read(HERE.parent / 'dgx-spark-qwen27-external-2026-10-12/summary.json')
    prices = read(HERE.parent / 'hardware-prices-2026-10-12.json')
    spark_price = read(OLD / 'spark-price.json')
    rag_inputs = read(RAG / 'assumptions.json')
    spec = importlib.util.spec_from_file_location('archived_rag', RAG / 'calculate_capacity.py')
    rag_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rag_module)
    model = next(m for m in rag_inputs['models'] if m['id'] == 'Qwen3.8-27B-FP8')
    conf = next(c for c in rag_inputs['configurations'] if c['id'] == 'H2')
    gpu = rag_inputs['gpus'][conf['gpu']]
    state = rag_module.state_bytes(model)
    bpt = rag_module.kv_bytes_per_token(model)
    pool = 84 * .9 - 31 - 6

    spark_windows = []
    for r in old['spark_matrix']:
        if r['kv'] != 'fp8' or r['resident_sessions'] != 1:
            continue
        c = r['context_tokens']
        speed = r['single_fp8_mtp3_decode_shape_estimate']
        spark_windows.append(dict(context_tokens=c, input_history_tokens=c-OUTPUT,
            output_reserve_tokens=OUTPUT, decode_shape_tokens_s=speed,
            cold_prefill_shape_s=r['single_fp8_cold_prefill_fit_seconds'],
            exact_prefix_append_1024_prefill_shape_s=r['ideal_cache_1k_prefill_difference_seconds'],
            exact_prefix_append_8192_prefill_shape_s=r['ideal_cache_8k_prefill_difference_seconds'],
            output_8192_generation_shape_s=OUTPUT/speed,
            cold_plus_8192_generation_shape_s=r['single_fp8_cold_prefill_fit_seconds']+OUTPUT/speed,
            meets_20_tokens_s_target=speed >= 20,
            evidence='empirical_shape_calculation; extrapolated_above_500000_input',
            precision='FP8_weights_FP8_full_attention_KV_MTP3',
            warm_conditions='exact_prefix_and_recurrent_state_reuse; excludes_restore_queue_first_decode'))
    spark_exact = []
    for r in measured['single_requests']:
        spark_exact.append(dict(input_tokens=r['input_tokens'], output_tokens=r['output_tokens_per_request'],
            total_context_tokens=r['input_tokens']+r['output_tokens_per_request'], active_requests=1,
            metric_scope='whole_request_decode_excluding_TTFT', decode_total_tokens_s=r['mean_decode_tokens_s'],
            decode_per_request_tokens_s=r['mean_decode_tokens_s'], ttft_s=r['mean_ttft_s'],
            evidence='external_measurement_summary', quality_tested=False))
    for r in measured['three_simultaneous_requests']:
        for scope, total, each in [
            ('common_decode_window',r['common_window_total_tokens_s'],r['common_window_mean_per_request_tokens_s']),
            ('whole_request_decode_mean_excluding_TTFT',None,r['full_decode_mean_per_request_tokens_s'])]:
            spark_exact.append(dict(input_tokens=r['input_tokens_per_request'],output_tokens=r['output_tokens_per_request'],
                total_context_tokens=r['input_tokens_per_request']+r['output_tokens_per_request'],active_requests=3,
                metric_scope=scope,decode_total_tokens_s=total,decode_per_request_tokens_s=each,ttft_s=None,
                evidence='external_measurement_summary',quality_tested=False))
    cap = measured['capacity_probe']
    spark_exact.append(dict(input_tokens=cap['input_tokens'],output_tokens=cap['output_tokens'],
        total_context_tokens=cap['total_tokens'],active_requests=1,metric_scope='64_token_capacity_probe',
        decode_total_tokens_s=cap['short_decode_tokens_s'],decode_per_request_tokens_s=cap['short_decode_tokens_s'],
        ttft_s=cap['ttft_s'],evidence='external_capacity_probe_not_steady_speed',quality_tested=False))
    for r in measured['cli_benchmark']:
        spark_exact.append(dict(input_tokens=r['input_tokens_per_request'],output_tokens=r['output_tokens_per_request'],
            total_context_tokens=r['input_tokens_per_request']+r['output_tokens_per_request'],active_requests=r['concurrency'],
            metric_scope='end_to_end_output_including_prefill',decode_total_tokens_s=r['end_to_end_output_tokens_s'],
            decode_per_request_tokens_s=None,ttft_s=r['mean_ttft_s'],evidence='external_measurement_summary',quality_tested=False))

    spark_sharing = []
    fp8pool = measured['startup']['estimated_shared_kv_token_pool']
    for dtype, pooltokens, tokenbytes in [('FP8', fp8pool, 32768), ('BF16', fp8pool//2, 65536)]:
        for resident in [1,3]:
            for c in CONTEXTS:
                used = resident*c
                spark_sharing.append(dict(kv_dtype=dtype,resident_sessions=resident,context_tokens=c,
                    observed_or_proxy_pool_tokens=pooltokens,workload_tokens=used,
                    working_set_fraction=used/pooltokens,reserved_fraction=RESERVE,
                    remaining_fraction_after_reserve=1-RESERVE-used/pooltokens,
                    fits_10pct_reserve=used<=pooltokens*(1-RESERVE),
                    raw_full_attention_payload_gb=used*tokenbytes/1e9,
                    evidence='observed_pool_projection' if dtype=='FP8' else 'half_FP8_pool_proxy_reload_required'))

    rag_capacity = []
    for label, c, out in [('8K_input_600_output',8792,600),('131K_total_8K_output',131072,8192),('262K_total_8K_output',262144,8192)]:
        raw = c*bpt + state
        budget = raw*1.15
        percard = math.floor(pool*1e9/budget)
        rag_capacity.append(dict(workload=label,context_tokens=c,input_tokens=c-out,output_tokens=out,
            full_attention_kv_gb=c*bpt/1e9,fixed_recurrent_and_conv_state_gb=state/1e9,
            cache_budget_per_session_gb=budget/1e9,cache_pool_gb_per_generation_gpu=pool,
            memory_only_sessions_per_gpu=percard,configured_batch_limit=32,
            simultaneously_admitted_max_three_replicas=min(percard,32)*3,
            twenty_resident_cache_gb=20*budget/1e9,twenty_residents_fit=7*budget<=pool*1e9,
            evidence='analytical_90pct_memory_6GB_runtime_15pct_payload_margin'))
    rag_performance=[]
    for efficiency in rag_inputs['efficiency_scenarios']:
        for c in [1,20]:
            r=rag_module.calculate_case(conf,model,gpu,efficiency,rag_inputs['workload'],c)
            rag_performance.append(dict(config='4x6000D_3gen_1aux',model=model['id'],kv_dtype='BF16_FP16',mtp=False,
                input_tokens=8192,output_tokens=600,submitted_requests=c,efficiency=efficiency['id'],
                per_request_decode_min_tokens_s=r['per_request_decode_tps_min'],
                per_request_decode_max_tokens_s=r['per_request_decode_tps_max'],
                phase_sum_decode_total_tokens_s=r['decode_only_total_tps'],
                output_end_to_end_tokens_s=r['burst_output_tps_including_prefill_and_retrieval'],
                last_ttft_s=r['burst_ttft_last_s'],last_completion_s=r['burst_e2e_last_s'],
                evidence='conditional_analytical_model_not_device_measurement'))

    # One strict post-graph profile per topology; no hidden change with resident count.
    anchors=[('H100_8_TP8','442505',8,1,12.36,10.34),
             ('H200_4_TP4','442751',4,1,35.16,32.49),
             ('H200_8_TP8','442758',8,1,62.86,60.20),
             ('H200_8_2xTP4','442751',4,2,35.16,32.49)]
    raw = read(SOURCES/'TECH-084/benchmarks.json')
    company=[]
    for name,rid,tp,reps,allocated,strict in anchors:
        r=next(r for r in raw if r['id']==rid)
        obs_pool=r['metrics']['kv_cache_pool_tokens']
        strict_pool=obs_pool*strict/allocated
        for residents in [20,40]:
            per=math.ceil(residents/reps)
            for c in CONTEXTS:
                company.append(dict(config=name,tp=tp,replicas=reps,gpus=tp*reps,
                    active_requests_target=20,resident_sessions=residents,context_tokens=c,
                    input_history_tokens=c-OUTPUT,output_reserve_tokens=OUTPUT,
                    anchor_id=rid,anchor_concurrency=r['conc'],allocated_kv_gib_per_gpu=allocated,
                    post_graph_strict_kv_gib_per_gpu=strict,observed_pool_tokens_per_replica=obs_pool,
                    strict_pool_tokens_per_replica=math.floor(strict_pool),
                    allocated_pool_fit_with_10pct_token_reserve=per*c<=obs_pool*.9,
                    strict_pool_fit_with_10pct_token_reserve=per*c<=strict_pool*.9,
                    strict_uniform_memory_context_tokens=math.floor(strict_pool*.9/per/64)*64,
                    admitted_context_cap_tokens=min(1000000,math.floor(strict_pool*.9/per/64)*64),
                    global_kv_payload_gb_per_rank=per*c*1827/1e9,
                    global_kv_payload_gb_all_ranks=residents*c*1827*tp/1e9,
                    evidence='public_old_image_pool_plus_linear_postgraph_budget_sensitivity',
                    speed_identity='target_defined_200_or_400_system_decode_tokens_s_not_1M_measurement'))
    replay=old['published_replay_examples']
    targets=[]
    for active in [5,20,30,50]:
        for speed in [10,20]:
            for c in CONTEXTS:
                targets.append(dict(active_requests=active,context_tokens=c,per_user_decode_target_tokens_s=speed,
                    required_system_decode_tokens_s=active*speed,output_tokens_per_call=OUTPUT,
                    generation_only_seconds_per_call=OUTPUT/speed,
                    generation_only_max_calls_per_hour=active*speed*3600/OUTPUT,
                    fresh_input_tokens_total=active*(c-OUTPUT),
                    required_fresh_prefill_tokens_s_for_5min=active*(c-OUTPUT)/300,
                    required_fresh_prefill_tokens_s_for_15min=active*(c-OUTPUT)/900,
                    required_fresh_prefill_tokens_s_for_30min=active*(c-OUTPUT)/1800,
                    evidence='service_target_backcalculation_not_predicted_or_measured_performance'))
    host=[]
    for topology,tp,reps,copies in [('TP8',8,1,1),('two_independent_TP4',4,2,2),('same_service_TP4_DP2_shared_Engram',4,2,1)]:
        engram=202758032400*copies
        offload=640*GIB
        other=256*10**9
        host.append(dict(topology=topology,tp=tp,replicas=reps,engram_host_copies=copies,
            engram_table_gb=engram/1e9,host_cache_quota_gib_total=640,
            other_host_memory_reserve_gb=256,nominal_host_memory_gb=1536,
            unassigned_nominal_host_memory_gb=1536-(engram+offload+other)/1e9,
            twenty_active_plus_twenty_waiting_global_kv_gb=40*1000000*1827*tp/1e9,
            global_payload_plus_15pct_preparation_gib=40*1000000*1827*tp*1.15/GIB,
            evidence='analytical_partition_not_peak_host_measurement',
            sharing_conditions='cpu_offload_DP_gt_1_shared_IPC_dev_shm_capacity_same_node' if copies==1 and reps==2 else 'no_cross_service_dedup_assumed'))
    restores=[]
    for tp in [4,8]:
        for sessions in [1,20]:
            payload=sessions*1000000*1827*tp/1e9
            for bw in [12,24,48]:
                restores.append(dict(system='Hopper_DeepSeek',tp=tp,sessions=sessions,context_tokens=1000000,
                    payload_scope='global_KV_rank_replicas_only',payload_gb=payload,
                    assumed_host_gpu_effective_gb_s=bw,assumed_ssd_effective_gb_s=6,
                    cpu_to_gpu_payload_seconds=payload/bw,
                    ssd_then_cpu_to_gpu_serial_payload_seconds=payload/6+payload/bw,
                    evidence='conditional_transfer_arithmetic_not_latency_measurement'))
    for c in CONTEXTS:
        payload=c*32768/1e9
        restores.append(dict(system='Spark_Qwen_FP8',tp=1,sessions=1,context_tokens=c,
            payload_scope='full_attention_KV_only_excludes_recurrent_checkpoints',payload_gb=payload,
            assumed_host_gpu_effective_gb_s=None,assumed_ssd_effective_gb_s=6,
            cpu_to_gpu_payload_seconds=None,ssd_then_cpu_to_gpu_serial_payload_seconds=payload/6,
            evidence='conditional_SSD_to_unified_memory_arithmetic_no_external_PCIe_GPU_hop'))
    tools=[]
    for rate in [.05,.1,.2]:
        for model_seconds in [60,120]:
            total=3*(model_seconds+10)
            tools.append(dict(arrival_tasks_per_second=rate,rounds=3,model_wall_s_per_round=model_seconds,
                tool_wall_s_per_round=10,tool_core_seconds_per_round=4,resident_env_gib=2,
                average_live_tasks=rate*total,average_model_phase_tasks=rate*3*model_seconds,
                average_tool_phase_tasks=rate*3*10,average_busy_cpu_cores=rate*3*4,
                average_environment_gib=rate*total*2,
                evidence='Little_law_teaching_scenario_no_queue_retry_or_headroom'))
    hardware=[]
    for r in prices['server_cases']:
        hardware.append({k:r[k] for k in ['id','gpu','cpu','host_ram_gb','total_cny','rounded_outward_wan_cny','price_class']})
    summary=dict(as_of='2026-10-20',timezone='Asia/Shanghai',anonymous=True,
        evidence_policy='Measured, empirical calculation, conditional analysis and service target are distinct.',
        context_convention={'windows':CONTEXTS,'output_reserve':OUTPUT,'K_label':'131K=131072;262K=262144;512K=524288','M_label':'1M=1000000'},
        versions={'latest_vllm_release':'0.32.0','latest_release_date':'2026-10-18','DeepSeek_tagged_support_since':'0.30.0',
                  'same_node_DP_shared_Engram_since':'0.31.0','archive':'TECH-089',
                  'vllm_0_32_output_change':'max_tokens_is_cap_not_reservation_gateway_must_reserve_8192',
                  'old_DeepSeek_benchmark_image':'vllm/vllm-openai:nightly-cd10ed6f9f6b37a8ace9cf380007e66fe12ec0c3',
                  'LMCache_dev_revision':'64b05b8af88d5fc13b375cdc06b5425cd56dea47'},
        scenario1={'hardware':'DGX Spark GB10 128GB unified memory 4TB NVMe','model':'Qwen/Qwen3.8-27B-FP8',
                   'measured_branch':'FP8 weights + FP8 full-attention KV + MTP3, prefix caching disabled',
                   'full_precision_branch':'FP8 weights + BF16/FP16 KV, no inherited MTP speed',
                   'observed_pool_tokens':fp8pool,'pool_reserve_fraction':.1,'hardware_cny_2026_10_12':spark_price['china_cash_budget_cny'],
                   'personal_implementation_cny':[10000,20000],'shared_implementation_cny':[20000,37500],
                   'single_user_target_tokens_s':20,'single_512K_estimate_tokens_s':spark_windows[2]['decode_shape_tokens_s'],
                   'context_quality_evaluated':False},
        scenario2={'hardware':'4x RTX PRO 6000D Server 84GB; 3x TP1 generation + 1x embedding/reranker; 1TB host RAM; 2x16-32-core 128GB support nodes',
                   'model':model['id'],'kv_dtype':'BF16/FP16','MTP':False,'hardware_wan_cny':[74,141],
                   'hardware_price_basis':'2026-10-12 carry-forward of 2026-09-21/23 D estimates; not refreshed market price',
                   'Onyx_initial_excluding_license_wan_cny':[84.5,158],
                   'Milvus_custom_initial_wan_cny':[91.5,168.5],
                   'Onyx_annual_license':'L_quote_required','cache_pool_gb_per_generation_gpu':pool,
                   'long_context_memory_only_admission':{'131072':9,'262144':3},
                   'storage':'GPU node 2x1.92TB system + 2x3.84TB enterprise NVMe; each support node 2x3.84TB mirrored; NAS reused',
                   'network':'dual-port25GbE GPU node plus10/25GbE support nodes; dedicated BMC'},
        scenario3={'model':'deepseek-ai/DeepSeek-V4.1-Flash','hardware':'8x H200 141GB SXM NVSwitch; 2x EPYC9454; 1536GB host RAM',
                   'topologies':['TP8','two independent TP4 services','TP4 x DP2 in one shared-Engram service'],
                   'main_active_users':20,'target_context_each':1000000,'target_context_is_capacity_candidate':True,
                   'hardware_wan_cny':[291,304],'incremental_two_tool_cpu_nodes_wan_cny':[12,26],
                   'native_checkpoint_bytes':510286023000,'engram_table_bytes':202758032400,
                   'non_Engram_checkpoint_bytes':307527990600,'Hopper_global_kv_bytes_per_token_rank':1827,
                   'Hopper_1M_global_kv_gb_per_rank':1.827,'full_1M_decode_evidence':'service target backcalculation; no matched measurement',
                   'A100_engine':'pinned modified vLLM SM80 adaptation; independent qualification',
                   'host_cache_candidate_quota_gib':640,'tool_servers_do_not_replicate_GPU_server_CPU_RAM':True},
        hardware_2026_10_12=hardware)
    slide_data=dict(as_of=summary['as_of'],page_map={
        'P02':{'title':'三种部署方式','data':['summary.json']},
        'P06':{'title':'负载与上下文','data':['summary.json','company-targets.csv']},
        'P10':{'title':'Spark模型与运行条件','data':['summary.json']},
        'P11':{'title':'单人生成与首次等待','data':['spark-measured.csv','spark-windows.csv'],'legend':'solid=external measured; dashed=empirical calculation;1M 64-token point separate'},
        'P12':{'title':'追加输入与前缀复用','data':['spark-windows.csv'],'legend':'append1024/8192 calculations exclude restore queue first decode'},
        'P13':{'title':'统一内存和SSD','data':['spark-sharing.csv','restoration-budgets.csv']},
        'P14':{'title':'三人共享','data':['spark-measured.csv','spark-sharing.csv'],'legend':'resident capacity vs common decode vs whole-request rate'},
        'P15':{'title':'Spark费用','data':['summary.json']},
        'P18':{'title':'知识库相同硬件与两种实施','data':['rag-capacity.csv','rag-performance.csv','summary.json']},
        'P20':{'title':'模型权重、Engram与KV','data':['summary.json','host-budget.csv']},
        'P21':{'title':'20人四档容量','data':['company-capacity.csv'],'legend':'post-graph strict pool estimate +10% token reserve; old fixed image'},
        'P22':{'title':'等待工具与缓存恢复','data':['company-capacity.csv','restoration-budgets.csv','host-budget.csv']},
        'P23':{'title':'已有回放与20路目标','data':['company-replay.csv','company-targets.csv'],'legend':'140-157K high-hit synthetic DSpark replay vs separately defined 1M targets'},
        'P24':{'title':'GPU与CPU工具池','data':['tool-cpu.csv','summary.json'],'legend':'Little law teaching example; actual average CPU distinct from allocated cores'},
        'P26':{'title':'公司整机预算','data':['summary.json']},
        'P27-P29':{'title':'成本模型输入','data':['summary.json','company-targets.csv','rag-performance.csv']}})
    outputs=[('spark-windows.csv',spark_windows),('spark-measured.csv',spark_exact),('spark-sharing.csv',spark_sharing),
        ('rag-capacity.csv',rag_capacity),('rag-performance.csv',rag_performance),('company-capacity.csv',company),
        ('company-replay.csv',replay),('company-targets.csv',targets),('host-budget.csv',host),
        ('restoration-budgets.csv',restores),('tool-cpu.csv',tools)]
    for name, rows in outputs:
        if name=='company-replay.csv':
            keys=list(dict.fromkeys(k for r in rows for k in r))
            rows=[{k:r.get(k) for k in keys} for r in rows]
        csvout(name,rows)
    write('summary.json',summary)
    write('slide-data.json',slide_data)
    source_paths=[OLD/'results.json',OLD/'spark-price.json',HERE.parent/'dgx-spark-qwen27-external-2026-10-12/summary.json',
        RAG/'assumptions.json',RAG/'calculate_capacity.py',HERE.parent/'hardware-prices-2026-10-12.json',
        SOURCES/'TECH-079/config.json',SOURCES/'TECH-079/model.safetensors.index.json',SOURCES/'TECH-084/benchmarks.json',
        SOURCES/'TECH-089/vllm-0.32-attention.py',SOURCES/'TECH-089/vllm-0.32-engram-config.py',
        SOURCES/'TECH-089/lmcache-qwen-series.rst',SOURCES/'TECH-089/lmcache-deepseek-v41.rst']
    checks=[]
    def check(condition, name):
        assert condition,name
        checks.append(name)
    check(all(r['input_history_tokens']+OUTPUT==r['context_tokens'] for r in spark_windows),'Spark input plus output equals exact total context')
    check(all(r['input_history_tokens']+OUTPUT==r['context_tokens'] for r in company),'Company exact total context includes output')
    check(cap['input_tokens']+cap['output_tokens']==1000000,'1M capacity probe is 999936+64, not an 8K-output speed sample')
    check(bpt==65536 and state==153944064,'Qwen27 full precision KV and complete recurrent/convolution state arithmetic')
    check([r['simultaneously_admitted_max_three_replicas'] for r in rag_capacity[1:]]==[9,3],'RAG long histories preserve 15 percent cache preparation')
    check(abs(rag_capacity[0]['twenty_resident_cache_gb']-16.793141248)<1e-8,'20 short RAG requests cache total')
    check(len(company)==4*2*4,'Company capacity rows cover four topologies, two resident counts, four windows')
    check(all(r['strict_pool_fit_with_10pct_token_reserve'] for r in company if r['config'].startswith('H200_8') and r['resident_sessions']==20),'Both H2008 layouts fit twenty full 1M sessions under strict rescaling')
    check(all(not r['strict_pool_fit_with_10pct_token_reserve'] for r in company if r['context_tokens']==1000000 and r['resident_sessions']==40),'Forty full 1M resident sessions require offload or new capacity')
    check(all(r['unassigned_nominal_host_memory_gb']>0 for r in host),'Host planning partitions fit nominal 1536GB without counting tool-node RAM')
    check(all(r['required_system_decode_tokens_s']==r['active_requests']*r['per_user_decode_target_tokens_s'] for r in targets),'20 users at 10 or20 tokens/s require200 or400 output tokens/s')
    check(all(abs(r['average_busy_cpu_cores']-r['arrival_tasks_per_second']*12)<1e-10 for r in tools),'Tool CPU core seconds separate from environment lifetime')
    check(all(not r['meets_20_tokens_s_target'] for r in spark_windows),'Full-window empirical estimates do not silently assert20+ target achieved')
    check(summary['scenario3']['native_checkpoint_bytes']-summary['scenario3']['engram_table_bytes']==summary['scenario3']['non_Engram_checkpoint_bytes'],'Native checkpoint/Engram decomposition')
    check((SOURCES/'TECH-089/vllm-0.32-attention.py').read_bytes()==(SOURCES/'TECH-080/vllm__models__deepseek_v41__attention.py').read_bytes(),'vLLM0.32 attention source matches previously audited Hopper layout')
    check('dp_shared_memory' in (SOURCES/'TECH-089/vllm-0.32-engram-config.py').read_text(),'Shared Engram configuration present in tagged0.32')
    check('Not yet validated with LMCache' in (SOURCES/'TECH-089/lmcache-deepseek-v41.rst').read_text(),'DeepSeek LMCache MTP validation caveat retained')
    write('validation.json',dict(status='passed',as_of='2026-10-20',checks=checks,
        output_rows={name:len(rows) for name,rows in outputs},new_gpu_execution=False,new_weights_downloaded=False,
        source_sha256={str(p.relative_to(KB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}))
    print(json.dumps({'status':'passed','checks':len(checks),'output_rows':{name:len(rows) for name,rows in outputs}},ensure_ascii=False))

if __name__=='__main__':
    main()
