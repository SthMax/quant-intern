#!/usr/bin/env python3
"""Safe stdlib CPU arithmetic, using archived source inputs; no network/GPU/subprocess."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SRC = ROOT / 'knowledge-base/sources/TECH-078/upstream'
a = json.loads((HERE / 'assumptions.json').read_text())
c = json.loads((SRC / 'calculations/configs/models/deepseek-v4.1-flash/config.json').read_text())['text_config']
GiB = 2**30
checks = []

def check(name, observed, expected):
    ok = observed == expected
    checks.append(dict(name=name, observed=observed, expected=expected, passed=ok))
    if not ok:
        raise AssertionError(name)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def spark_case(n):
    s = a['spark']; prompt = n-a['reserved_output_tokens']
    coeff = 4*s['full_attention_layers']*s['query_heads']*s['head_dim']
    cold_pairs = prompt*(prompt+1)//2
    kv1 = s['full_attention_layers']*2*s['kv_heads']*s['head_dim']
    warm=[]
    for new in a['warm_new_tokens']:
        history=prompt-new
        pairs=new*history+new*(new+1)//2
        warm.append(dict(new_tokens=new, cached_history_tokens=history,
            causal_attention_pairs=pairs, qk_pv_matrix_flops=coeff*pairs,
            qk_pv_min_effective_TFLOPS_for_5s=coeff*pairs/5/1e12,
            qk_pv_min_effective_TFLOPS_for_10s=coeff*pairs/10/1e12,
            fraction_of_cold_attention_work=pairs/cold_pairs))
    return dict(context_tokens=n, prompt_tokens=prompt, reserved_output_tokens=a['reserved_output_tokens'],
        raw_full_attention_kv_bytes={'fp8':kv1*n,'bf16':kv1*2*n},
        active_recurrent_and_conv_state_bytes=s['recurrent_and_convolution_state_bytes'],
        raw_kv_plus_one_active_state_gib={'fp8':(kv1*n+s['recurrent_and_convolution_state_bytes'])/GiB,
                                        'bf16':(kv1*2*n+s['recurrent_and_convolution_state_bytes'])/GiB},
        logged_pool_token_fraction_single=n/s['observed_fp8_kv_token_pool'],
        logged_pool_token_fraction_three=3*n/s['observed_fp8_kv_token_pool'],
        logged_pool_fits_one=n<=s['observed_fp8_kv_token_pool'],
        logged_pool_fits_three=3*n<=s['observed_fp8_kv_token_pool'],
        cold_causal_attention_pairs=cold_pairs,cold_qk_pv_matrix_flops=coeff*cold_pairs,
        warm=warm)

def ds_case(n, batch):
    owners=c['kv_source_layer_ids']; ratios=c['compress_ratios'][:c['num_hidden_layers']]
    entries=sum(n//ratios[i] for i in owners)
    main=288; index=68; local=528; win=c['sliding_window']
    global_p=entries*(main+index)
    global_b=entries*(c['head_dim']+c['index_head_dim'])*2
    global_h=entries*(584+132)
    align=lambda v: ((v+575)//576)*576
    block_bytes=3*(align(32*584)+align(32*132))+align(64*584)+align(64*132)
    global_ha=((n+63)//64)*block_bytes
    swa=c['num_hidden_layers']*min(n,win)*local
    b_swa=c['num_hidden_layers']*min(n,win)*c['head_dim']*2
    compressor=sum(2*ratios[i]*c['head_dim']*4 for i in owners if ratios[i]>1)
    token_ids=n*8
    mainread=sum(min(n,win)*local+(min(n//r,c['index_topk'])*main if r else 0) for r in ratios)
    cap=c['candidate_topk_blocks']*c['candidate_block_size']
    indexread=sum((n//ratios[i] if i<=c['candidate_source_layer_id'] else min(n//ratios[i],cap))*index
                  for i in c['index_source_layer_ids'])
    refscan=sum(n//ratios[i]*c['index_head_dim']*2 for i in c['index_source_layer_ids'])
    transfer={str(bw):global_p*batch/(bw*1e9) for bw in a['deepseek']['declared_transfer_payload_bandwidth_GBps']}
    return dict(context_tokens=n, independent_sessions=batch, global_entries_per_session=entries,
        book_production_global_bytes=batch*global_p,
        reference_bf16_global_bytes=batch*global_b,
        current_vllm_hopper_global_bytes_per_replicated_rank=batch*global_h,
        current_vllm_hopper_page_aligned_bytes_per_replicated_rank=batch*global_ha,
        book_swa_bytes=batch*swa,
        book_compressor_fp32_bytes=batch*compressor, reference_engram_token_history_bytes=batch*token_ids,
        book_production_state_budget_bytes=batch*(global_p+swa+compressor+token_ids),
        reference_bf16_state_budget_bytes=batch*(global_b+b_swa+compressor+token_ids),
        book_encoder_swa_only_bytes=batch*swa//2,
        book_decode_main_logical_read_bytes_per_step=batch*mainread,
        book_decode_index_logical_read_bytes_per_step=batch*indexread,
        book_decode_total_logical_read_bytes_per_step=batch*(mainread+indexread),
        reference_index_full_scan_bytes_per_step=batch*refscan,
        global_payload_transfer_seconds=transfer,
        decode_total_logical_read_BW_GBps_at_20tps=batch*(mainread+indexread)*20/1e9)

spark=[spark_case(n) for n in a['context_tokens']]
deep=[ds_case(n,b) for n in a['context_tokens'] for b in a['deepseek']['resident_users_sensitivity']]
# Verify current Qwen dimensions against the previously archived official config.
qc=json.loads((ROOT/a['spark']['qwen_config_source']).read_text())
qc=qc.get('text_config',qc)
for label,key in [('query_heads','num_attention_heads'),('kv_heads','num_key_value_heads'),('head_dim','head_dim')]:
    check('qwen_'+label,a['spark'][label],qc[key])
check('qwen_full_layers',a['spark']['full_attention_layers'],qc['layer_types'].count('full_attention'))
linear=qc['layer_types'].count('linear_attention')
rstate=linear*qc['linear_num_value_heads']*qc['linear_key_head_dim']*qc['linear_value_head_dim']*4
width=2*qc['linear_num_key_heads']*qc['linear_key_head_dim']+qc['linear_num_value_heads']*qc['linear_value_head_dim']
conv=linear*width*(qc['linear_conv_kernel_dim']-1)*2
check('qwen_active_state_payload',a['spark']['recurrent_and_convolution_state_bytes'],rstate+conv)
# Check independently derived values against archived author outputs, not copied constants alone.
up=json.loads((SRC/'calculations/results/v41-throughline.json').read_text())
for old in up['cache_cases']:
    row=next(x for x in old['models'] if x['model']=='deepseek-v4.1-flash')
    new=ds_case(old['length'],1)
    check(f"book_global_{old['length']}",new['book_production_global_bytes'],row['global_history_bytes'])
    check(f"book_swa_{old['length']}",new['book_swa_bytes'],row['local_window_bytes'])
    check(f"book_main_read_{old['length']}",new['book_decode_main_logical_read_bytes_per_step'],row['decode_main_history_read_bytes'])
    check(f"book_index_read_{old['length']}",new['book_decode_index_logical_read_bytes_per_step'],row['decode_index_history_read_bytes'])
# The book's '1m' is 1,048,576. Our main comparison uses 1,000,000.
forward=json.loads((SRC/'calculations/results/v41-forward-decode-1m-ced.json').read_text())
for newfield,oldfield in [('book_production_state_budget_bytes','production_state_after'),('reference_bf16_state_budget_bytes','state_after')]:
    check('book_1048576_'+oldfield,ds_case(1048576,1)[newfield],forward[oldfield]['resident_bytes'])
check('even_global_slope',ds_case(1000000,1)['book_production_global_bytes'],890000000)
check('bf16_global_slope',ds_case(1000000,1)['reference_bf16_global_bytes'],3200000000)
check('hopper_global_slope',ds_case(1000000,1)['current_vllm_hopper_global_bytes_per_replicated_rank'],1790000000)
check('hopper_page_aligned_slope',ds_case(1000000,1)['current_vllm_hopper_page_aligned_bytes_per_replicated_rank'],1827000000)
check('compressor_fixed_bytes',ds_case(1000000,1)['book_compressor_fp32_bytes'],24576)
check('qwen_bf16_512k_raw_bytes',spark[2]['raw_full_attention_kv_bytes']['bf16'],34359738368)
check('qwen_fp8_512k_raw_bytes',spark[2]['raw_full_attention_kv_bytes']['fp8'],17179869184)
# Published checkpoint result is a source input; no model weights downloaded or revalidated.
ck=json.loads((SRC/'calculations/results/v41-flash-n8192-b1.json').read_text())['checkpoint']
check('published_checkpoint_component_sum',sum(ck['bytes_by_component'].values()),ck['tensor_payload_bytes'])
engram_tables=sum(c['engram_num_embeddings'])*(c['engram_head_dim']+c['engram_head_dim']//32)
engram_other=ck['bytes_by_component']['engram']-engram_tables
weights=dict(author_published_component_payload_bytes=ck['bytes_by_component'],
    independent_engram_tables_bytes=engram_tables, engram_other_component_bytes=engram_other,
    text_plus_dspark_bytes=ck['tensor_payload_bytes']-ck['bytes_by_component']['vision'],
    illustrative_gpu_backbone_dspark_and_engram_projections_bytes=ck['bytes_by_component']['backbone']+ck['bytes_by_component']['dspark']+engram_other,
    scope='Book published checkpoint file accounting; loader residency/dtype conversion/sharding must be checked per backend.')
# Restore transmission demand; compare one-time restore vs all 8192 decode steps.
restore=[dict(context_tokens=n, sessions=20, book_global_transfer_once_GB=ds_case(n,20)['book_production_global_bytes']/1e9,
              book_global_transfer_each_step_8192_TB=ds_case(n,20)['book_production_global_bytes']*8192/1e12)
         for n in a['context_tokens']]
# A chapter-11 teaching trace, deliberately not a resource quote or measured fleet workload.
agent_example=dict(arrival_tasks_per_s=0.1, rounds=3, model_s_per_round=60, tool_wall_s_per_round=10,
                   tool_cpu_s_per_round=4, environment_GiB=2,
                   task_wall_s=210, mean_resident_tasks=21, mean_active_model_calls=18,
                   mean_busy_cpu_cores=1.2, mean_resident_environment_GiB=42,
                   model_call_context_tokens=1000000,
                   note='Self-declared steady-state teaching inputs; no queue, failures or burst headroom; active calls and resident tasks differ.')
result=dict(schema_version=1, as_of=a['as_of'], evidence_kind='independent_cpu_resource_recalculation_not_measured_performance',
    spark_cases=spark, deepseek_cases=deep, deepseek_weight_ledger=weights, restore_frequency_cases=restore,
    agent_resource_example=agent_example,
    external_observation_ratios=dict(ttft_1m_capacity_to_500k=4815.8/1470.1,input_ratio=999936/500000,
        stable_500k_decode_output_8192_seconds_at_recorded_mean=8192/14.82,
        note='Final value is arithmetic at a reported mean, not a measured 8192-output request; 1M decode omitted because capacity probe output is only 64.'),
    provenance=[dict(path=str(p.relative_to(ROOT)),sha256=sha(p)) for p in [HERE/'assumptions.json',Path(__file__),SRC/'calculations/configs/models/deepseek-v4.1-flash/config.json',SRC/'calculations/results/v41-throughline.json',SRC/'calculations/results/v41-flash-n8192-b1.json',ROOT/a['spark']['qwen_config_source'],ROOT/'knowledge-base/sources/TECH-080/vllm__models__deepseek_v41__attention.py']])
(HERE/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
(HERE/'validation.json').write_text(json.dumps(dict(status='passed',checks=checks,tests_count=len(checks),scope='Arithmetic and identities only; no execution benchmark, quality test or procurement verification'),ensure_ascii=False,indent=2)+'\n')
print('Passed',len(checks),'checks; wrote',len(spark),'Spark and',len(deep),'DeepSeek resource rows')
for x in spark:
    print('Spark',x['context_tokens'],'FP8/BF16 GiB',x['raw_kv_plus_one_active_state_gib'],'attention TFLOPs',round(x['cold_qk_pv_matrix_flops']/1e12,3),'warm1k/8k TFLOPs',[round(w['qk_pv_matrix_flops']/1e12,3) for w in x['warm']])
for x in deep:
    if x['independent_sessions']==20:
        print('DeepSeek20',x['context_tokens'],'global_prod/reference/current_GB',[round(x[k]/1e9,4) for k in ['book_production_global_bytes','reference_bf16_global_bytes','current_vllm_hopper_global_bytes_per_replicated_rank']],'payload_decode_GB/step',round(x['book_decode_total_logical_read_bytes_per_step']/1e9,4))
print(weights)
