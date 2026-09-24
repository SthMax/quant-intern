"""Scenario estimates, not benchmarks. Run with Python 3; writes results.json.

Cold-cache, text-only, independent TP1 replicas. Each burst batch completes
prefill before decode; queued batches run afterward. Continuous batching may
improve this batch barrier schedule. Efficiency factors are explicit inputs.
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def recurrent_state_bytes(model):
    return (model['linear_layers'] * model['linear_value_heads']
            * model['linear_key_dim'] * model['linear_value_dim'] * 4)


def convolution_state_bytes(model):
    channels = (2 * model['linear_key_heads'] * model['linear_key_dim']
                + model['linear_value_heads'] * model['linear_value_dim'])
    return model['linear_layers'] * channels * (model['linear_conv_kernel_dim'] - 1) * 2


def state_bytes(model):
    return recurrent_state_bytes(model) + convolution_state_bytes(model)


def kv_bytes_per_token(model):
    return model['full_attention_layers'] * 2 * model['kv_heads'] * model['head_dim'] * 2


def prefill_flops(model, input_tokens, linear_margin):
    # 2P per token plus a declared margin for non-matmul/linear-attention work.
    projection = 2 * model['active_params_billion'] * 1e9 * input_tokens * linear_margin
    # Causal QK + AV: 2 * L * query_heads * head_dim * sequence_length^2.
    attention = (2 * model['full_attention_layers'] * model['query_heads']
                 * model['head_dim'] * input_tokens ** 2)
    return projection + attention


def batch_metrics(model, gpu, scenario, workload, batch):
    input_tokens, output_tokens = workload['input_tokens'], workload['output_tokens']
    context = input_tokens + output_tokens / 2
    bw = gpu['bandwidth_gb_s'] * scenario['bandwidth_fraction']
    effective_tflops = gpu['effective_tflops'][scenario['id']]
    effective_tflops *= model['compute_factor']
    if model['kind'] == 'moe':
        # Uniform independent routing within each layer: union of selected experts.
        fraction = 1 - (1 - model['top_k'] / model['experts']) ** batch
        weight_read = model['non_expert_gb'] + model['expert_pool_gb'] * fraction
    else:
        fraction = None
        weight_read = model['resident_weights_gb']
    kv_read = batch * context * kv_bytes_per_token(model) / 1e9
    recurrent_read_write = 2 * batch * state_bytes(model) / 1e9
    activation_read = batch * workload['other_activation_gb_per_step_per_request']
    memory_seconds = (weight_read + kv_read + recurrent_read_write + activation_read) / bw
    decode_flops = (2 * model['active_params_billion'] * 1e9 * batch
                    * workload['linear_compute_margin'])
    decode_flops += (4 * model['full_attention_layers'] * model['query_heads']
                     * model['head_dim'] * context * batch)
    compute_seconds = decode_flops / (effective_tflops * 1e12)
    step_seconds = max(memory_seconds, compute_seconds) + scenario['step_overhead_ms'][model['kind']] / 1000
    prefill_seconds = batch * prefill_flops(model, input_tokens, workload['linear_compute_margin']) / (effective_tflops * 1e12)
    decode_seconds = output_tokens * step_seconds
    return {
        'batch': batch,
        'expert_union_fraction': fraction,
        'weight_read_gb_per_step': weight_read,
        'kv_read_gb_per_step': kv_read,
        'recurrent_read_write_gb_per_step': recurrent_read_write,
        'state_note': 'Read/write budget includes both recurrent and convolution state.',
        'other_activation_read_gb_per_step': activation_read,
        'effective_bandwidth_gb_s': bw,
        'memory_time_ms': memory_seconds * 1000,
        'compute_time_ms': compute_seconds * 1000,
        'fixed_overhead_ms': scenario['step_overhead_ms'][model['kind']],
        'effective_tflops': effective_tflops,
        'prefill_s': prefill_seconds,
        'decode_s': decode_seconds,
        'step_s': step_seconds,
        'decode_tps_per_stream': 1 / step_seconds,
        'decode_total_tps': batch / step_seconds,
        'completion_s': prefill_seconds + decode_seconds,
        'mixed_request_capacity_rps': batch / (prefill_seconds + decode_seconds),
    }


def busy_seconds(intervals):
    """Wall-clock union of phase intervals on independent replicas."""
    end, total = 0.0, 0.0
    for start, stop in sorted(intervals):
        total += max(0.0, stop - max(start, end))
        end = max(end, stop)
    return total


def context_capacity(config, model, gpu, workload, concurrency):
    replicas = config['generation_gpus']
    pool = (gpu['nominal_memory_gb'] * workload['memory_fraction']
            - model['resident_weights_gb'] - workload['engine_reserve_gb'])
    record = dict(config=config['id'], model=model['id'], resident_sequences=concurrency,
        generation_replicas=replicas, kv_bytes_per_token=kv_bytes_per_token(model),
        recurrent_state_bytes=recurrent_state_bytes(model),
        convolution_state_bytes=convolution_state_bytes(model),
        fixed_state_bytes_per_sequence=state_bytes(model),
        generation_gpu_memory_gb=gpu['nominal_memory_gb'] * replicas,
        weights_total_gb=model['resident_weights_gb'] * replicas,
        engine_reserve_total_gb=workload['engine_reserve_gb'] * replicas,
        unallocated_fraction_gb=gpu['nominal_memory_gb'] * replicas * (1 - workload['memory_fraction']),
        cache_budget_balance_gb_per_replica=pool,
        cache_pool_gb_per_replica=max(0, pool),
        cache_pool_gb_total=max(0, pool) * replicas,
        native_context_limit=model['native_context_limit'])
    if pool <= 0:
        return {**record, 'feasible': False, 'reason': 'Weights plus stated runtime reserve exceed the 90% memory budget.'}
    groups = []
    for i in range(replicas):
        count = concurrency // replicas + (i < concurrency % replicas)
        if not count:
            continue
        memory_tokens = max(0, math.floor((pool * 1e9 / workload['cache_padding_factor'] / count
            - state_bytes(model)) / kv_bytes_per_token(model) / 256) * 256)
        bounded = min(memory_tokens, model['native_context_limit'])
        groups.append(dict(replica=i, sequences=count, memory_only_context_tokens=memory_tokens,
            bounded_context_tokens=bounded,
            used_cache_gb=count * (bounded * kv_bytes_per_token(model) + state_bytes(model)) / 1e9 * workload['cache_padding_factor']))
    common = min(g['bounded_context_tokens'] for g in groups)
    return {**record, 'feasible': common > 0, 'groups': groups,
        'memory_only_total_tokens': sum(g['sequences'] * g['memory_only_context_tokens'] for g in groups),
        'bounded_total_tokens': sum(g['sequences'] * g['bounded_context_tokens'] for g in groups),
        'uniform_context_tokens_per_request': common,
        'uniform_total_tokens': common * concurrency,
        'workload_fits_all_resident': common >= workload['input_tokens'] + workload['output_tokens'],
        'input_budget_with_600_output_tokens': max(0, common - workload['output_tokens']),
        'workload_cache_gb_total': concurrency * ((workload['input_tokens'] + workload['output_tokens'])
            * kv_bytes_per_token(model) + state_bytes(model)) / 1e9 * workload['cache_padding_factor']}


def calculate_case(config, model, gpu, scenario, workload, concurrency):
    replicas = config['generation_gpus']
    cache_per_request = ((workload['input_tokens'] + workload['output_tokens'])
                         * kv_bytes_per_token(model) + state_bytes(model)) / 1e9 * workload['cache_padding_factor']
    available = (gpu['nominal_memory_gb'] * workload['memory_fraction']
                 - model['resident_weights_gb'] - workload['engine_reserve_gb'])
    memory_limit = max(0, math.floor(available / cache_per_request))
    limit = min(memory_limit, workload['max_batch_per_replica'])
    if not limit:
        return {'feasible': False, 'reason': 'No cache headroom under stated reserve.'}
    counts = [concurrency // replicas + (i < concurrency % replicas) for i in range(replicas)]
    if workload['input_tokens'] + workload['output_tokens'] > model['native_context_limit']:
        return {'feasible': False, 'reason': 'Request exceeds native model context limit.'}
    all_first_tokens, all_completions, batches = [], [], []
    prefill_intervals, decode_intervals, decode_events = [], [], []
    steady_rps, decode_tps = 0.0, 0.0
    for replica, count in enumerate(counts):
        elapsed = 0.0
        remaining = count
        first_batch = True
        while remaining:
            size = min(remaining, limit)
            b = batch_metrics(model, gpu, scenario, workload, size)
            prefill_intervals.append((elapsed, elapsed + b['prefill_s']))
            decode_intervals.append((elapsed + b['prefill_s'], elapsed + b['completion_s']))
            decode_events.extend([(elapsed + b['prefill_s'], b['decode_total_tps']),
                                  (elapsed + b['completion_s'], -b['decode_total_tps'])])
            # retrieval_s is a per-request delay, assumed to run in parallel across users.
            ttft = scenario['retrieval_s'] + elapsed + b['prefill_s'] + b['step_s']
            completion = scenario['retrieval_s'] + elapsed + b['completion_s']
            all_first_tokens.extend([ttft] * size)
            all_completions.extend([completion] * size)
            batches.append({**b, 'replica': replica, 'model_start_s': elapsed,
                            'model_decode_start_s': elapsed + b['prefill_s'], 'model_end_s': elapsed + b['completion_s']})
            if first_batch:
                steady_rps += b['mixed_request_capacity_rps']
                decode_tps += b['decode_total_tps']
                first_batch = False
            elapsed += b['completion_s']
            remaining -= size
    one = batch_metrics(model, gpu, scenario, workload, 1)
    final_s = max(all_completions)
    rate, peak = 0.0, 0.0
    for _, delta in sorted(decode_events):
        rate += delta
        peak = max(peak, rate)
    prefill_busy, decode_busy = busy_seconds(prefill_intervals), busy_seconds(decode_intervals)
    return {
        'feasible': True,
        'generation_replicas': replicas,
        'concurrency': concurrency,
        'memory_limit_per_replica': memory_limit,
        'batch_limit_per_replica': limit,
        'cache_gb_per_request': cache_per_request,
        'cache_pool_gb_per_replica': available,
        'requests_per_replica': counts,
        'single_request_ttft_s_no_queue': scenario['retrieval_s'] + one['prefill_s'] + one['step_s'],
        'single_stream_decode_tps': one['decode_tps_per_stream'],
        'single_request_e2e_s_no_queue': scenario['retrieval_s'] + one['completion_s'],
        'burst_ttft_last_s': max(all_first_tokens),
        'burst_e2e_last_s': final_s,
        'burst_output_tps_including_prefill_and_retrieval': concurrency * workload['output_tokens'] / final_s,
        'decode_only_total_tps': decode_tps,
        'decode_only_total_tps_note': 'Sum of the first batches\' phase rates. Use decode_peak_total_tps for the maximum simultaneous rate.',
        'prefill_phase_busy_wall_s': prefill_busy,
        'prefill_phase_input_tps': concurrency * workload['input_tokens'] / prefill_busy,
        'decode_phase_busy_wall_s': decode_busy,
        'decode_phase_window_output_tps': concurrency * workload['output_tokens'] / decode_busy,
        'decode_peak_total_tps': peak,
        'per_request_decode_tps_min': min(b['decode_tps_per_stream'] for b in batches),
        'per_request_decode_tps_max': max(b['decode_tps_per_stream'] for b in batches),
        'model_only_ttft_last_s': max(all_first_tokens) - scenario['retrieval_s'],
        'model_only_completion_last_s': final_s - scenario['retrieval_s'],
        'model_only_burst_output_tps': concurrency * workload['output_tokens'] / (final_s - scenario['retrieval_s']),
        'burst_request_rps_including_retrieval': concurrency / final_s,
        'mixed_llm_capacity_rps': steady_rps,
        'planning_admission_rps_at_70pct': steady_rps * workload['admission_utilization'],
        'queue_note': 'Burst includes later batch waiting. No stochastic P95 or steady-arrival queue prediction.',
        'batches': batches,
    }


def main():
    inputs = json.loads((ROOT / 'assumptions.json').read_text())
    result = {'method': 'analytical scenarios; not measurements or statistical confidence intervals',
              'memory_policy': '90% GPU memory; 15% cache payload overhead; recurrent plus convolution state',
              'cases': [], 'context_capacity': [], 'memory_policy_sensitivity': []}
    for config in inputs['configurations']:
        gpu = inputs['gpus'][config['gpu']]
        for model in inputs['models']:
            for c in inputs['workload']['concurrency_levels']:
                result['context_capacity'].append(context_capacity(config, model, gpu, inputs['workload'], c))
            for scenario in inputs['efficiency_scenarios']:
                for c in inputs['workload']['concurrency_levels']:
                    metrics = calculate_case(config, model, gpu, scenario, inputs['workload'], c)
                    result['cases'].append({'config': config['id'], 'model': model['id'], 'efficiency': scenario['id'], 'concurrency': c, **metrics})
    config = next(c for c in inputs['configurations'] if c['id'] == 'H1')
    model = next(m for m in inputs['models'] if m['kind'] == 'moe')
    scenario = next(e for e in inputs['efficiency_scenarios'] if e['id'] == 'base')
    for count in [20, 50]:
        w = {**inputs['workload'], 'memory_fraction': 0.95}
        result['memory_policy_sensitivity'].append(dict(config='H1', model=model['id'], concurrent_requests=count,
            memory_fraction=0.95, note='Separate tight-memory scenario; retains 15% cache overhead and complete states.',
            **calculate_case(config, model, inputs['gpus']['L20'], scenario, w, count)))
    result['storage_example'] = {
        'documents_assumed': 100000, 'chunks_per_document_assumed': 20,
        'vector_dimension': 1024, 'bytes_per_dimension': 4,
        'raw_vector_gb': 100000 * 20 * 1024 * 4 / 1e9,
        'excluded': 'text, scalar/inverted indexes, HNSW overhead, replicas, source images and backups',
    }
    costs = inputs['cost_assumptions']
    support = [costs['support_nodes_count'] * x for x in costs['per_support_node_wan_cny']]
    result['costs'] = {'class': 'D, analytical acquisition + initial implementation; recurring operations excluded', 'configurations': []}
    for config in inputs['configurations']:
        hardware = [config['gpu_server_budget_wan_cny'][i] + support[i] for i in (0, 1)]
        enterprise = [hardware[i] + costs['enterprise_days'][i] * costs['day_cost_cny'] / 10000 for i in (0, 1)]
        custom = [hardware[i] + costs['custom_days'][i] * costs['day_cost_cny'] / 10000 for i in (0, 1)]
        result['costs']['configurations'].append({
            'config': config['id'], 'hardware_wan_cny': hardware,
            'enterprise_initial_excluding_license_wan_cny': enterprise,
            'custom_initial_wan_cny': custom,
            'enterprise_license_sensitivity': [
                {'annual_license_assumption_wan_cny': fee, 'first_year_acquisition_and_initial_implementation_wan_cny': [x + fee for x in enterprise]}
                for fee in costs['onyx_license_sensitivity_annual_wan']
            ],
        })
    # Long-input and CPU-layer sensitivities share the exact equations.
    result['input_length_sensitivity'] = []
    config = next(x for x in inputs['configurations'] if x['id'] == 'H2')
    scenario = next(x for x in inputs['efficiency_scenarios'] if x['id'] == 'base')
    for model in inputs['models']:
        for tokens in [4096, 8192, 32768]:
            w = {**inputs['workload'], 'input_tokens': tokens}
            result['input_length_sensitivity'].append({'config': 'H2', 'model': model['id'], 'input_tokens': tokens, **calculate_case(config, model, inputs['gpus'][config['gpu']], scenario, w, 20)})
    (ROOT / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f"Wrote {len(result['cases'])} capacity cases and input-length sensitivities to {ROOT / 'results.json'}")


if __name__ == '__main__':
    main()
