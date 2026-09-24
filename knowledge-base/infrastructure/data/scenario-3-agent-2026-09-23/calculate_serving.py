"""Serving-only analytical estimates using the Agent simulation's GPU model.

One simultaneous burst, identical input/output lengths, cold cache, no tools.
Prefill and decode phase rates have separate denominators. Wall-clock rates
include both phases and the configured service control delay. No GPU is run.
"""
import hashlib
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from calculate_tasks import batch_profile, cache_gb

ROOT = Path(__file__).resolve().parent


def estimate(a, config, efficiency, count, input_tokens, output_tokens):
    model = next(m for m in a['models'] if m['id'] == config['model'])
    gpu, settings = a['gpus'][config['gpu']], a['scheduler']
    cap = (gpu['nominal_memory_gb'] * config['tp'] * settings['memory_fraction']
           - model['resident_weights_gb'] - model['engine_reserve_gb_per_gpu'] * config['tp'])
    groups = []
    for replica in range(config['replicas']):
        batch = len(range(replica, count, config['replicas']))
        if not batch:
            continue
        reservation = batch * cache_gb(model, input_tokens + output_tokens, settings)
        assert batch <= settings['max_batch'] and reservation <= cap
        calls = [dict(task=i, input=input_tokens, cached=0, output=output_tokens) for i in range(batch)]
        phase = batch_profile(calls, config, model, gpu, efficiency, settings)
        # Identical sequences use one constant mean decode step in this model.
        step = phase['decode_s'] / output_tokens
        assert math.isclose(step, phase['first_step_s'])
        groups.append(dict(replica=replica, requests=batch,
            reserved_cache_gb=reservation, cache_pool_gb=cap,
            prefill_s=phase['prefill_s'], decode_s=phase['decode_s'],
            decode_step_s=step, per_request_decode_tps=1 / step,
            ttft_s=phase['first_token_s'] + settings['control_seconds_per_call'],
            completion_s=phase['total_s'] + settings['control_seconds_per_call']))
    prefill_span = max(g['prefill_s'] for g in groups)
    decode_span = max(g['decode_s'] for g in groups)
    total_s = max(g['completion_s'] for g in groups)
    total_input, total_output = count * input_tokens, count * output_tokens
    # Equal group sizes make the phase and wall-clock comparisons unambiguous.
    equal_groups = len({g['requests'] for g in groups}) == 1
    return dict(config=config['id'], model=model['id'], efficiency=efficiency['id'],
        concurrent_requests=count, input_tokens_per_request=input_tokens,
        output_tokens_per_request=output_tokens, cache='cold', groups=groups,
        prefill_phase_input_tps=total_input / prefill_span,
        decode_phase_output_tps=total_output / decode_span if equal_groups else None,
        per_request_decode_tps_min=min(g['per_request_decode_tps'] for g in groups),
        per_request_decode_tps_max=max(g['per_request_decode_tps'] for g in groups),
        ttft_first_s=min(g['ttft_s'] for g in groups),
        ttft_last_s=max(g['ttft_s'] for g in groups),
        batch_completion_s=total_s,
        wall_clock_input_tps=total_input / total_s,
        wall_clock_output_tps=total_output / total_s,
        wall_clock_total_tps=(total_input + total_output) / total_s,
        burst_requests_per_s=count / total_s,
        equal_active_group_sizes=equal_groups)


def main():
    a = json.loads((ROOT / 'assumptions.json').read_text())
    cases = [estimate(a, c, e, n, size, 600)
             for c in a['configurations'] for e in a['efficiency_scenarios']
             for n in [1, 5, 20, 30] for size in [8192, 32768]]
    for case in cases:
        assert case['ttft_last_s'] < case['batch_completion_s']
        assert math.isclose(case['wall_clock_output_tps'], case['burst_requests_per_s'] * 600)
        if case['equal_active_group_sizes']:
            assert math.isclose(case['decode_phase_output_tps'] / case['concurrent_requests'],
                                case['per_request_decode_tps_min'])
            assert case['wall_clock_output_tps'] < case['decode_phase_output_tps']
    result = dict(
        status='Uncalibrated analytical serving estimates; no actual GPU execution',
        workload='One simultaneous cold-cache burst; identical sequences; no tools or retries; no prior queue',
        definitions={
            'prefill_phase_input_tps': 'All uncached input tokens / time until all groups finish prefill',
            'decode_phase_output_tps': 'All output tokens / common decode phase duration; only equal-sized active groups',
            'per_request_decode_tps': '1 / modelled mean decode step; excludes prefill and service delay',
            'wall_clock_output_tps': 'All output tokens / complete burst duration including prefill and service delay',
            'wall_clock_total_tps': 'Input plus output tokens / same complete burst duration',
            'burst_requests_per_s': 'Requests / complete burst duration; finite burst, not sustained-load capacity',
            'ttft': 'Model first token, which can be reasoning or tool arguments; excludes client network latency'},
        assumptions_sha256=hashlib.sha256((ROOT / 'assumptions.json').read_bytes()).hexdigest(),
        simulation_code_sha256=hashlib.sha256((ROOT / 'calculate_tasks.py').read_bytes()).hexdigest(),
        checks=['batch and cache capacity', 'phase timing identities', 'throughput token conservation',
                'equal-batch decode total / concurrency equals per-request decode'],
        cases=cases)
    (ROOT / 'serving-results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f'Wrote {len(cases)} serving cases; phase and token checks passed.')


if __name__ == '__main__':
    main()
