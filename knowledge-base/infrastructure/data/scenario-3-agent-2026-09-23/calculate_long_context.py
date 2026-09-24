"""Company Agent: resident-task context budgets and full-window inference.

The MiMo publisher-native mixed-precision artifact is retained. KV uses two
bytes with sliding-window reclamation. This is analytical, not a GPU run.
"""
import hashlib
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from calculate_tasks import batch_profile
from calculate_kv_capacity import capacity, cache_layout

ROOT = Path(__file__).resolve().parent
CONFIG_IDS = ['A2', 'A3', 'A4', 'A5']
COUNTS = [5, 20, 30, 50]
WINDOWS = [262144, 524288]
OUTPUT = 8192


def infer(a, config, count, window, efficiency, mode):
    model = next(m for m in a['models'] if m['id'] == config['model'])
    layout = cache_layout(model, config['tp'])
    cached = 0 if mode == 'cold' else window - OUTPUT - 1024
    settings = a['scheduler']
    cap = capacity(a, config, count, 'architecture_reclaimed')
    groups, failures = [], []
    for replica in range(config['replicas']):
        batch = len(range(replica, count, config['replicas']))
        required = batch * (window * layout['history_bytes_per_token_per_replica']
                            + layout['fixed_bytes_per_sequence_per_replica']) / 1e9 * settings['cache_padding_factor']
        pool = cap['cache_pool_gb_per_replica']
        if required > pool:
            failures.append(f'Replica {replica}: cache need {required:.3f} GB exceeds {pool:.3f} GB.')
        if batch > settings['max_batch']:
            failures.append(f'Replica {replica}: {batch} active requests exceed max_batch {settings["max_batch"]}.')
        groups.append(dict(replica=replica, requests=batch, cache_required_gb=required,
                           cache_pool_gb=pool))
    result = dict(config=config['id'], model=model['id'], concurrent_tasks=count,
        context_tokens_per_task=window, input_tokens_per_request=window-OUTPUT,
        output_tokens_per_request=OUTPUT, cached_tokens_per_request=cached,
        mode=mode, efficiency=efficiency['id'], groups=groups,
        feasible=not failures, constraints=failures,
        maximum_equal_context_tokens=cap['equal_context_tokens_per_sequence'])
    if failures:
        return result
    for g in groups:
        calls = [dict(task=i, input=window-OUTPUT, output=OUTPUT, cached=cached) for i in range(g['requests'])]
        phase = batch_profile(calls, config, model, a['gpus'][config['gpu']], efficiency, settings)
        g.update(prefill_s=phase['prefill_s'], decode_s=phase['decode_s'],
            per_request_decode_tps=OUTPUT/phase['decode_s'],
            ttft_s=phase['first_token_s']+settings['control_seconds_per_call'],
            completion_s=phase['total_s']+settings['control_seconds_per_call'])
    end = max(g['completion_s'] for g in groups)
    events=[]
    for g in groups:
        rate=g['requests']*g['per_request_decode_tps']
        events.extend([(g['prefill_s'],rate),(g['prefill_s']+g['decode_s'],-rate)])
    rate=peak=0.0
    for _,delta in sorted(events):
        rate+=delta
        peak=max(peak,rate)
    result.update(prefill_uncached_total_tps=count*(window-OUTPUT-cached)/max(g['prefill_s'] for g in groups),
        decode_total_tps=peak,
        decode_phase_rate_sum_tps=sum(g['requests']*g['per_request_decode_tps'] for g in groups),
        all_groups_decode_overlap=max(g['prefill_s'] for g in groups)<min(g['prefill_s']+g['decode_s'] for g in groups),
        per_request_decode_tps_min=min(g['per_request_decode_tps'] for g in groups),
        per_request_decode_tps_max=max(g['per_request_decode_tps'] for g in groups),
        ttft_last_s=max(g['ttft_s'] for g in groups), batch_completion_s=end,
        whole_request_output_tps=count*OUTPUT/end)
    return result


def main():
    a = json.loads((ROOT/'assumptions.json').read_text())
    configs = [c for c in a['configurations'] if c['id'] in CONFIG_IDS]
    result = dict(status='Uncalibrated long-context analysis; no target-device test',
        context_definition='Input + output per task; 8192 tokens reserved and generated in full-window probe',
        runtime_condition='BF16/FP16 KV; sliding-window layers retain their window, not complete history; no CPU offload',
        precision_policy='MiMo publisher-native MXFP4/FP8/BF16 is permitted by user; Qwen personal/RAG minimum 8-bit is separate.',
        assumptions_sha256=hashlib.sha256((ROOT/'assumptions.json').read_bytes()).hexdigest(),
        capacity=[], cases=[])
    for c in configs:
        m = next(m for m in a['models'] if m['id']==c['model'])
        layout = cache_layout(m, c['tp'])
        for n in COUNTS:
            for mode in ['architecture_reclaimed', 'retain_all_sliding_history']:
                row = capacity(a, c, n, mode)
                quota = (262144*layout['history_bytes_per_token_per_replica']+layout['fixed_bytes_per_sequence_per_replica'])/1e9*a['scheduler']['cache_padding_factor']
                row['memory_resident_tasks_at_262k'] = math.floor(row['cache_pool_gb_per_replica']/quota)*c['replicas']
                row['active_requests_at_262k'] = min(math.floor(row['cache_pool_gb_per_replica']/quota),a['scheduler']['max_batch'])*c['replicas']
                if mode=='retain_all_sliding_history':
                    quota=262144*layout['all_history_bytes_per_token_per_replica']/1e9*a['scheduler']['cache_padding_factor']
                    row['memory_resident_tasks_at_262k']=math.floor(row['cache_pool_gb_per_replica']/quota)*c['replicas']
                    row['active_requests_at_262k']=min(math.floor(row['cache_pool_gb_per_replica']/quota),a['scheduler']['max_batch'])*c['replicas']
                result['capacity'].append(row)
            for window in WINDOWS:
                for e in a['efficiency_scenarios']:
                    for mode in ['cold','warm1k']:
                        result['cases'].append(infer(a,c,n,window,e,mode))
    for x in result['cases']:
        assert x['input_tokens_per_request']+x['output_tokens_per_request']==x['context_tokens_per_task']
        if x['feasible']:
            assert math.isclose(x['whole_request_output_tps']*x['batch_completion_s'],x['concurrent_tasks']*OUTPUT)
    (ROOT/'long-context-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(f"Wrote {len(result['cases'])} long-context cases and {len(result['capacity'])} resident-context budgets.")


if __name__=='__main__':
    main()
