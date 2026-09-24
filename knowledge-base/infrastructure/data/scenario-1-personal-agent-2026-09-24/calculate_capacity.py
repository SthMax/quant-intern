"""Personal/shared workstation budgets; no model, hardware or Agent execution.

Uses Scenario 1's arithmetic with explicit precision, UMA reserves, 1/3 request
bursts and cold/exact-prefix probes. Price observations keep their original date.
"""
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]


def load_method(path):
    spec = importlib.util.spec_from_file_location('rag_math', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def capacity(a, config, model, count, method, context_tokens, extra_states=0):
    w = a['workload']
    available = config['physical_memory_gb'] - config['os_and_tools_reserve_gb']
    if config['configured_gpu_cap_gb'] is not None:
        available = min(available, config['configured_gpu_cap_gb'])
    engine_budget = available * w['memory_fraction']
    pool = engine_budget - model['resident_weights_gb'] - config['runtime_reserve_gb']
    state = method.state_bytes(model) * (1 + extra_states)
    bpt = method.kv_bytes_per_token(model)
    memory_context = max(0, math.floor((pool * 1e9 / w['cache_padding_factor'] / count - state) / bpt / 256) * 256)
    limit = model['extended_context_limit'] if context_tokens > model['native_context_limit'] else model['native_context_limit']
    bounded = min(memory_context, limit)
    quota_gb = count * (context_tokens * bpt + state) / 1e9 * w['cache_padding_factor']
    return dict(config=config['id'], model=model['id'], resident_sequences=count,
        target_context_tokens=context_tokens,
        extension_required=context_tokens > model['native_context_limit'],
        model_limit_for_configuration=limit,
        extra_state_copies_per_sequence=extra_states,
        engine_memory_budget_gb=engine_budget, weights_gb=model['resident_weights_gb'],
        runtime_reserve_gb=config['runtime_reserve_gb'], cache_pool_gb=pool,
        kv_bytes_per_token=bpt, state_bytes_per_sequence=state,
        memory_only_total_context_tokens=count * memory_context,
        bounded_total_context_tokens=count * bounded,
        context_tokens_per_sequence=bounded,
        target_cache_gb=quota_gb, target_fits=quota_gb <= pool and context_tokens <= limit,
        target_cache_headroom_gb=pool - quota_gb,
        qualification='Architecture payload budget plus 15% allowance, not measured engine allocation.')


def serving(a, config, model, efficiency, probe, count, method):
    w = {**a['workload'], 'input_tokens': probe['input_tokens'], 'output_tokens': probe['output_tokens']}
    cap = capacity(a, config, model, count, method, probe['context_tokens'], w['extra_state_copies_per_sequence'])
    identity = dict(config=config['id'], model=model['id'], precision=config['precision'],
        efficiency=efficiency['id'], concurrent_requests=count, probe=probe['id'],
        context_profile=probe['context_profile'], context_tokens=probe['context_tokens'], mode=probe['mode'],
        input_tokens=w['input_tokens'], cached_tokens=probe['cached_tokens'], output_tokens=w['output_tokens'],
        extra_state_copies_per_sequence=w['extra_state_copies_per_sequence'],
        target_cache_gb=cap['target_cache_gb'], cache_pool_gb=cap['cache_pool_gb'],
        extension_required=cap['extension_required'])
    assert w['input_tokens'] + w['output_tokens'] == probe['context_tokens']
    if not cap['target_fits']:
        return {**identity, 'feasible': False, 'reason': 'Full simultaneous context and stated checkpoint reserve exceed the configured cache pool.'}
    gpu = {'bandwidth_gb_s': config['bandwidth_gb_s'], 'effective_tflops': config['effective_tflops']}
    b = method.batch_metrics(model, gpu, efficiency, w, count)
    cached = probe['cached_tokens']
    if cached:
        flops = method.prefill_flops(model, w['input_tokens'], w['linear_compute_margin'])
        flops -= method.prefill_flops(model, cached, w['linear_compute_margin'])
        b['prefill_s'] = count * flops / (b['effective_tflops'] * 1e12)
    used = cap['target_cache_gb']
    total = b['prefill_s'] + b['decode_s'] + config['control_s']
    output = count * w['output_tokens']
    return dict(**identity, feasible=True,
        prefill_s=b['prefill_s'], decode_s=b['decode_s'],
        prefill_uncached_input_tps=count * (w['input_tokens'] - cached) / b['prefill_s'],
        decode_total_tps=b['decode_total_tps'], per_request_decode_tps=b['decode_tps_per_stream'],
        ttft_s=config['control_s'] + b['prefill_s'] + b['step_s'],
        completion_s=total, whole_request_output_tps=output / total,
        requests_per_s=count / total, active_cache_gb=used,
        bytes_and_timing_audit={k: b[k] for k in ['weight_read_gb_per_step', 'kv_read_gb_per_step',
            'recurrent_read_write_gb_per_step', 'other_activation_read_gb_per_step',
            'effective_bandwidth_gb_s', 'effective_tflops', 'memory_time_ms', 'compute_time_ms', 'fixed_overhead_ms']})


def main():
    a = json.loads((ROOT / 'assumptions.json').read_text())
    dep = REPO / a['method_dependency']
    assert hashlib.sha256(dep.read_bytes()).hexdigest() == a['method_dependency_sha256']
    method = load_method(dep)
    result = dict(status=a['status'], serving=[], capacity=[], costs=[])
    for c in a['configurations']:
        models = [m for m in a['models'] if m['precision'] == c['precision']]
        for m in models:
            for n in a['workload']['concurrency_levels']:
                for profile in a['context_profiles']:
                    for copies in [0, 8, 32]:
                        result['capacity'].append(capacity(a, c, m, n, method, profile['context_tokens'], copies))
                for e in a['efficiency_scenarios']:
                    for probe in a['probes']:
                        result['serving'].append(serving(a, c, m, e, probe, n, method))
        if c['id'].endswith('-FP8'):
            continue
        cost = a['setup_budget'];unit = c['unit_price_cny']
        personal_setup = [d * cost['day_cost_cny'] for d in cost['personal_days']]
        shared_setup = [d * cost['day_cost_cny'] for d in cost['shared_team_days']]
        independent_setup = [d * cost['day_cost_cny'] for d in cost['three_independent_days']]
        result['costs'].append(dict(config=c['id'], unit_hardware_cny=unit,
            personal_hardware_and_setup_cny=[unit[i] + personal_setup[i] for i in [0,1]],
            shared_team_hardware_and_setup_cny=[unit[i] + shared_setup[i] for i in [0,1]],
            three_personal_hardware_cny=[x * 3 for x in unit],
            three_personal_hardware_and_setup_cny=[unit[i] * 3 + independent_setup[i] for i in [0,1]]))
    result['definitions'] = dict(
        prefill='Uncached input tokens / prefill duration; exact cached prefixes are excluded from the numerator.',
        decode='All equal-length simultaneous streams; total / active requests = per-request rate.',
        whole_request='All outputs / control + prefill + decode; no tools or multi-turn task time included.',
        capacity='Input + history + output. Main admission includes one live state plus eight checkpoint state copies; 0/32 extra copies are sensitivities. 524288 requires a separately configured YaRN extension.',
        shared_vs_independent='One shared machine uses batch 3; three separate machines each use batch 1. Their RAM is not pooled.')
    for c in result['serving']:
        if not c['feasible']:
            continue
        assert math.isclose(c['decode_total_tps'] / c['concurrent_requests'], c['per_request_decode_tps'])
        assert c['ttft_s'] < c['completion_s']
        assert math.isclose(c['whole_request_output_tps'] * c['completion_s'], c['output_tokens'] * c['concurrent_requests'])
    (ROOT / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f"Wrote {len(result['serving'])} serving cases, {len(result['capacity'])} memory cases and six cost comparisons.")


if __name__ == '__main__':
    main()
