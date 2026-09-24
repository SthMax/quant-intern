"""Architecture payload budgets and an audit of the existing A0 decode estimate.

This computes conditional memory budgets, not a serving engine's block layout
or measured speed. Model limits and independent replica pools are explicit.
"""
import hashlib
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from calculate_tasks import batch_profile

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]
CONFIGS = {
    'Qwen3.6-35B-A3B-FP8': 'knowledge-base/sources/TECH-070/qwen35/config.json',
    'MiMo-V2.6-Flash-RL': 'knowledge-base/sources/TECH-065/config.json',
    'MiMo-V2.6-Pro-RL': 'knowledge-base/sources/TECH-064/config.json',
}


def cache_layout(model, tp):
    path = REPO / CONFIGS[model['id']]
    source = json.loads(path.read_text())
    c = source.get('text_config', source)
    # Sum physical heads over all TP ranks, including replication if TP > heads.
    heads = max(c['num_key_value_heads'], tp)
    assert max(c['num_key_value_heads'], tp) % min(c['num_key_value_heads'], tp) == 0
    if model['kind'] == 'linear_moe':
        full = c['layer_types'].count('full_attention')
        linear = c['layer_types'].count('linear_attention')
        per_token = full * heads * c['head_dim'] * 2 * 2
        recurrent = (linear * c['linear_num_value_heads'] * c['linear_key_head_dim']
                     * c['linear_value_head_dim'] * 4)
        conv_dim = (2 * c['linear_num_key_heads'] * c['linear_key_head_dim']
                    + c['linear_num_value_heads'] * c['linear_value_head_dim'])
        conv = linear * conv_dim * (c['linear_conv_kernel_dim'] - 1) * 2
        fixed = recurrent + conv
        all_history = per_token
    else:
        full = c['hybrid_layer_pattern'].count(0)
        sliding = c['hybrid_layer_pattern'].count(1)
        per_token = full * heads * (c['head_dim'] + c['v_head_dim']) * 2
        sliding_per_token = (sliding * max(c['swa_num_key_value_heads'], tp)
                            * (c['swa_head_dim'] + c['swa_v_head_dim']) * 2)
        fixed = sliding_per_token * c['sliding_window_size']
        all_history = per_token + sliding_per_token
        recurrent = conv = 0
    return dict(model=model['id'], source_config=CONFIGS[model['id']],
        config_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        kv_dtype='BF16/FP16, 2 bytes', native_context_limit=c['max_position_embeddings'],
        history_bytes_per_token_per_replica=per_token,
        fixed_bytes_per_sequence_per_replica=fixed,
        recurrent_bytes=recurrent, convolution_bytes=conv,
        all_history_bytes_per_token_per_replica=all_history)


def capacity(a, config, count, mode):
    model = next(m for m in a['models'] if m['id'] == config['model'])
    gpu, settings = a['gpus'][config['gpu']], a['scheduler']
    layout = cache_layout(model, config['tp'])
    total_gpu_gb = gpu['nominal_memory_gb'] * config['tp'] * config['replicas']
    pool = (gpu['nominal_memory_gb'] * config['tp'] * settings['memory_fraction']
            - model['resident_weights_gb'] - model['engine_reserve_gb_per_gpu'] * config['tp'])
    bpt = layout['history_bytes_per_token_per_replica']
    fixed = layout['fixed_bytes_per_sequence_per_replica']
    if mode == 'retain_all_sliding_history' and model['sliding_layers']:
        bpt, fixed = layout['all_history_bytes_per_token_per_replica'], 0
    groups = []
    for replica in range(config['replicas']):
        n = len(range(replica, count, config['replicas']))
        if not n:
            continue
        # Round down to 256-token planning increments, not an engine block claim.
        memory_context = math.floor((pool * 1e9 / settings['cache_padding_factor'] / n - fixed) / bpt / 256) * 256
        context = min(memory_context, layout['native_context_limit'])
        used = n * (context * bpt + fixed) * settings['cache_padding_factor'] / 1e9
        assert 0 < context <= layout['native_context_limit'] and used <= pool
        groups.append(dict(replica=replica, resident_sequences=n,
            memory_only_tokens_per_sequence=memory_context,
            bounded_tokens_per_sequence=context,
            input_history_budget_with_8k_output_reserve=max(0, context - 8192),
            cache_gb_used_at_bounded_limit=used))
    return dict(config=config['id'], model=model['id'], mode=mode, layout=layout,
        total_gpu_gb=total_gpu_gb, weights_total_gb=model['resident_weights_gb'] * config['replicas'],
        engine_reserve_total_gb=model['engine_reserve_gb_per_gpu'] * config['tp'] * config['replicas'],
        unallocated_fraction_gb=total_gpu_gb * (1 - settings['memory_fraction']),
        cache_pool_gb_per_replica=pool, cache_pool_gb_total=pool * config['replicas'],
        payload_budget_gb_total=pool * config['replicas'] / settings['cache_padding_factor'],
        resident_sequences=count, groups=groups,
        total_memory_only_tokens=sum(g['memory_only_tokens_per_sequence'] * g['resident_sequences'] for g in groups),
        total_bounded_tokens=sum(g['bounded_tokens_per_sequence'] * g['resident_sequences'] for g in groups),
        equal_context_tokens_per_sequence=min(g['bounded_tokens_per_sequence'] for g in groups))


def audit_a0(a):
    c = next(c for c in a['configurations'] if c['id'] == 'A0')
    m = next(m for m in a['models'] if m['id'] == c['model'])
    e = next(e for e in a['efficiency_scenarios'] if e['id'] == 'base')
    g, s = a['gpus'][c['gpu']], a['scheduler']
    batch, context = 20, 8192 + 600 / 2
    union = 1 - (1 - m['top_k'] / m['experts']) ** batch
    weights = m['non_expert_gb'] + m['expert_pool_gb'] * union
    kv = batch * context * m['kv_bytes_token'] / 1e9
    state = 2 * batch * m['state_bytes'] / 1e9
    other = batch * s['other_activation_gb_per_request']
    bandwidth = g['bandwidth_gb_s'] * e['bandwidth_fraction']
    compute = (2 * m['active_params_billion'] * 1e9 * batch * s['linear_compute_margin']
               + 2 * m['full_attention_layers'] * m['query_heads'] * m['kv_dim_sum'] * batch * context)
    memory_s = (weights + kv + state + other) / bandwidth
    compute_s = compute / (g['effective_tflops']['base'] * m['compute_factor'] * 1e12)
    step = max(memory_s, compute_s) + m['kernel_ms']['base'] / 1000
    phase = batch_profile([dict(task=i, input=8192, output=600, cached=0) for i in range(batch)], c, m, g, e, s)
    assert math.isclose(step, phase['first_step_s'])
    return dict(status='Reconstruction of the old conditional estimate, not a measured capability',
        batch=batch, average_context=context, expert_union_fraction=union,
        weights_read_gb_per_step=weights, kv_read_gb_per_step=kv,
        recurrent_read_write_gb_per_step=state, other_traffic_gb_per_step=other,
        total_traffic_gb_per_step=weights + kv + state + other,
        effective_bandwidth_gb_s=bandwidth, memory_time_ms=memory_s * 1000,
        compute_time_ms=compute_s * 1000, fixed_overhead_ms=m['kernel_ms']['base'],
        step_ms=step * 1000, aggregate_decode_tps=batch / step,
        per_request_decode_tps=1 / step,
        whole_burst_output_tps=batch * 600 / (phase['total_s'] + s['control_seconds_per_call']),
        uncalibrated=['60% effective bandwidth', 'uniform independent expert routing',
                     'one memory read per distinct expert in a batch',
                     'max(memory time, compute time) with fixed 3 ms overhead'])


def main():
    a = json.loads((ROOT / 'assumptions.json').read_text())
    cases = [capacity(a, c, n, mode) for c in a['configurations']
             for n in [5, 20, 30, 50]
             for mode in ['architecture_reclaimed', 'retain_all_sliding_history']]
    result = dict(status='Conditional architecture payload capacity; physical engine blocks need profiling',
        units='Decimal GB; tokens count input + history + generated tokens once per sequence, not once per GPU',
        scope='Disjoint resident sequences; balanced TP; reclaimed inactive prefixes; no draft model or CPU offload',
        assumptions_sha256=hashlib.sha256((ROOT / 'assumptions.json').read_bytes()).hexdigest(),
        page_reserve_factor=a['scheduler']['cache_padding_factor'],
        mamba_note='One FP32 recurrent state and one BF16 convolution state per live sequence; prefix checkpoints and allocator padding are additional physical costs',
        user_comparison={'model': 'Qwen3.8-27B', 'gpu': '4 x A100 40GB', 'tp': 4,
                         'single_request_observed_tps_approx': 40,
                         'dtype_context_framework': 'not recalled'},
        a0_decode_audit=audit_a0(a), cases=cases)
    (ROOT / 'kv-capacity-results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f'Wrote {len(cases)} capacity cases and A0 decode audit.')


if __name__ == '__main__':
    main()
