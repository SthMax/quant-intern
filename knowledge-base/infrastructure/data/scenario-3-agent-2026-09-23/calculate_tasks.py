"""Uncalibrated event simulation for multi-turn Agent work; no model execution.

Each model replica forms FIFO batches, prefills the batch, then decodes it.
Shorter outputs finish first. New calls join the next batch. Tools use a finite
worker pool. Exact task-local prefixes live in a bounded LRU between calls.
"""
import heapq
import json
from collections import OrderedDict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def cache_gb(model, tokens, settings):
    return (model['kv_bytes_token'] * tokens + model['state_bytes']) / 1e9 * settings['cache_padding_factor']


def communication(config, model, tokens):
    tp = config['tp']
    if tp == 1:
        return 0.0
    count = config['collectives_per_layer'] * model['layers']
    volume_gb = count * (2 * (tp - 1) / tp) * tokens * model['hidden'] * 2 / 1e9
    return count * config['collective_latency_us'] / 1e6 + volume_gb / config['link_gb_s']


def batch_profile(calls, config, model, gpu, efficiency, settings):
    tflops = (gpu['effective_tflops'][efficiency['id']] * config['tp']
              * config['compute_efficiency'] * model['compute_factor'])
    bandwidth = (gpu['bandwidth_gb_s'] * config['tp']
                 * efficiency['bandwidth_fraction'] * config['memory_efficiency'])
    prefill_flops, new_tokens = 0.0, 0
    for call in calls:
        size, cached = call['input'], call['cached']
        new = size - cached
        new_tokens += new
        prefill_flops += 2 * model['active_params_billion'] * 1e9 * new * settings['linear_compute_margin']
        prefill_flops += (model['full_attention_layers'] * model['query_heads']
                         * model['kv_dim_sum'] * (size ** 2 - cached ** 2))
        if model['sliding_layers']:
            prefill_flops += 2 * model['sliding_layers'] * model['query_heads'] * model['kv_dim_sum'] * 128 * new
    prefill = prefill_flops / (tflops * 1e12) + communication(config, model, new_tokens)
    elapsed, previous, completion_offsets, first_step = 0.0, 0, {}, None
    for end in sorted({call['output'] for call in calls}):
        active = [call for call in calls if call['output'] > previous]
        batch = len(active)
        contexts = sum(call['input'] + (previous + end) / 2 for call in active)
        union = 1 - (1 - model['top_k'] / model['experts']) ** batch
        weight_gb = model['non_expert_gb'] + model['expert_pool_gb'] * union
        kv_gb = contexts * model['kv_bytes_token'] / 1e9
        state_reads = 2 if model['kind'] == 'linear_moe' else 1
        state_gb = state_reads * batch * model['state_bytes'] / 1e9
        traffic_gb = weight_gb + kv_gb + state_gb + batch * settings['other_activation_gb_per_request']
        flops = 2 * model['active_params_billion'] * 1e9 * batch * settings['linear_compute_margin']
        flops += 2 * model['full_attention_layers'] * model['query_heads'] * model['kv_dim_sum'] * contexts
        if model['sliding_layers']:
            flops += 2 * model['sliding_layers'] * model['query_heads'] * model['kv_dim_sum'] * 128 * batch
        step = max(traffic_gb / bandwidth, flops / (tflops * 1e12))
        step += communication(config, model, batch) + model['kernel_ms'][efficiency['id']] / 1000
        first_step = step if first_step is None else first_step
        elapsed += (end - previous) * step
        for call in active:
            if call['output'] == end:
                completion_offsets[call['task']] = prefill + elapsed
        previous = end
    return dict(prefill_s=prefill, decode_s=elapsed, first_step_s=first_step,
                first_token_s=prefill + first_step,
                completion_offsets=completion_offsets, total_s=prefill + elapsed)


def batch_times(calls, config, model, gpu, efficiency, settings):
    profile = batch_profile(calls, config, model, gpu, efficiency, settings)
    return profile['first_token_s'], profile['completion_offsets'], profile['total_s']


def simulate(config, model, gpu, task, efficiency, cache_mode, settings, tasks):
    cap_gb = (gpu['nominal_memory_gb'] * config['tp'] * settings['memory_fraction']
              - model['resident_weights_gb'] - model['engine_reserve_gb_per_gpu'] * config['tp'])
    replicas = [{'queue': deque(), 'active': {}, 'cache': OrderedDict()} for _ in range(config['replicas'])]
    events, sequence = [], 0

    def event(at, kind, task_id, turn):
        nonlocal sequence
        sequence += 1
        heapq.heappush(events, (at, sequence, kind, task_id, turn))

    for tid in range(tasks):
        event(0, 'ready', tid, 0)
    tool_slots = [0.0] * settings['tool_slots']
    heapq.heapify(tool_slots)
    finished, first_tokens = {}, {}
    records = []
    counters = dict(input_tokens=0, cached_input_tokens=0, output_tokens=0,
                    model_calls=0, model_group_busy_s=0.0, tool_busy_s=0.0,
                    tool_queue_s=0.0, model_queue_s=0.0, cache_evictions=0,
                    peak_reserved_cache_gb=0.0, max_batch_seen=0)
    while events:
        now = events[0][0]
        while events and abs(events[0][0] - now) < 1e-9:
            _, _, kind, tid, turn = heapq.heappop(events)
            unit = replicas[tid % config['replicas']]
            if kind == 'ready':
                unit['queue'].append((tid, turn, now))
            else:
                request = unit['active'].pop(tid)
                if cache_mode['stable_prefix_fraction']:
                    unit['cache'][tid] = (request['input'] + request['output'], request['reservation_gb'])
                duration = task['tool_seconds'][turn]
                if duration:
                    available = heapq.heappop(tool_slots)
                    start = max(now, available)
                    next_time = start + duration
                    heapq.heappush(tool_slots, next_time)
                    counters['tool_queue_s'] += start - now
                    counters['tool_busy_s'] += duration
                else:
                    next_time = now
                if turn + 1 < len(task['inputs']):
                    event(next_time, 'ready', tid, turn + 1)
                else:
                    finished[tid] = next_time
        # Dispatch after processing all events at this time, so simultaneous arrivals batch.
        for unit in replicas:
            if unit['active'] or not unit['queue']:
                continue
            calls, reservation = [], 0.0
            while unit['queue'] and len(calls) < settings['max_batch']:
                tid, turn, ready_at = unit['queue'][0]
                size, output = task['inputs'][turn], task['outputs'][turn]
                needed = cache_gb(model, size + output, settings)
                if needed > cap_gb:
                    return dict(feasible=False, reason='A single request exceeds the configured cache pool.', config=config['id'], task=task['id'])
                if reservation + needed > cap_gb:
                    break
                unit['queue'].popleft()
                old = unit['cache'].pop(tid, (0, 0))[0]
                reusable = 0 if turn in task['cache_reset_turns'] else min(size, old)
                cached = int(reusable * cache_mode['stable_prefix_fraction'] // 256) * 256
                request = dict(task=tid, turn=turn, ready_at=ready_at, input=size,
                               output=output, cached=cached, reservation_gb=needed)
                calls.append(request)
                reservation += needed
            while unit['cache'] and reservation + sum(v[1] for v in unit['cache'].values()) > cap_gb:
                unit['cache'].popitem(last=False)
                counters['cache_evictions'] += 1
            peak = reservation + sum(v[1] for v in unit['cache'].values())
            counters['peak_reserved_cache_gb'] = max(counters['peak_reserved_cache_gb'], peak)
            first_offset, ends, duration = batch_times(calls, config, model, gpu, efficiency, settings)
            start = now + settings['control_seconds_per_call']
            counters['model_group_busy_s'] += duration + settings['control_seconds_per_call']
            counters['max_batch_seen'] = max(counters['max_batch_seen'], len(calls))
            for call in calls:
                tid, turn = call['task'], call['turn']
                unit['active'][tid] = call
                first_tokens.setdefault(tid, start + first_offset)
                counters['model_calls'] += 1
                counters['input_tokens'] += call['input']
                counters['cached_input_tokens'] += call['cached']
                counters['output_tokens'] += call['output']
                counters['model_queue_s'] += start - call['ready_at']
                if tid == 0:
                    records.append(dict(turn=turn + 1, ready_s=call['ready_at'], start_s=start,
                                        first_token_s=start + first_offset, end_s=start + ends[tid],
                                        input_tokens=call['input'], cached_tokens=call['cached'],
                                        output_tokens=call['output'], batch=len(calls)))
                event(start + ends[tid], 'done', tid, turn)
    assert len(finished) == tasks
    last = max(finished.values())
    mean = sum(finished.values()) / tasks
    # A long-run resource-work bound, separate from the finite burst completion rate.
    model_work = counters['model_group_busy_s'] / tasks
    tool_work = counters['tool_busy_s'] / tasks
    model_cap = config['replicas'] * 3600 / model_work
    tool_cap = settings['tool_slots'] * 3600 / tool_work if tool_work else float('inf')
    admission = min(model_cap, tool_cap) * settings['admission_utilization']
    return dict(feasible=True, config=config['id'], model=model['id'], task=task['id'],
                concurrent_tasks=tasks, efficiency=efficiency['id'], cache_mode=cache_mode['id'],
                task_completion_mean_s=mean, task_completion_last_s=last,
                first_model_token_first_s=min(first_tokens.values()),
                first_model_token_last_s=max(first_tokens.values()),
                burst_tasks_per_hour=tasks / last * 3600,
                all_model_output_tps=counters['output_tokens'] / last,
                model_busy_fraction=counters['model_group_busy_s'] / (last * config['replicas']),
                tool_busy_fraction=counters['tool_busy_s'] / (last * settings['tool_slots']),
                effective_input_cache_fraction=counters['cached_input_tokens'] / counters['input_tokens'],
                planning_admission_tasks_per_hour=admission,
                cache_pool_gb_per_replica=cap_gb, counters=counters, first_task_trace=records,
                qualification='Synthetic machine-only task trace; not observed quality, P95, or vendor performance.')


def main():
    a = json.loads((ROOT / 'assumptions.json').read_text())
    output = dict(status=a['status'], cases=[], costs=[], sensitivities=[])
    for config in a['configurations']:
        model = next(m for m in a['models'] if m['id'] == config['model'])
        gpu = a['gpus'][config['gpu']]
        for task in a['task_templates']:
            for efficiency in a['efficiency_scenarios']:
                for cache in a['cache_scenarios']:
                    for count in a['concurrency_levels']:
                        output['cases'].append(simulate(config, model, gpu, task, efficiency, cache, a['scheduler'], count))
        cost = a['cost']
        central_hw = [config['gpu_increment_wan'][i] + cost['central_worker_nodes'] * cost['worker_per_node_wan'][i] for i in (0, 1)]
        desktop_hw = [config['gpu_increment_wan'][i] + cost['desktop_gateway_nodes'] * cost['worker_per_node_wan'][i] for i in (0, 1)]
        output['costs'].append(dict(config=config['id'], incremental_central_hardware_wan=central_hw,
            incremental_central_with_implementation_wan=[central_hw[i] + cost['central_development_days'][i] * cost['day_cost_cny'] / 10000 for i in (0, 1)],
            combined_s1_s2_central_hardware_wan=[central_hw[i] + cost['prior_scenario1_h2_hardware_wan'][i] for i in (0, 1)],
            incremental_desktop_hardware_wan=desktop_hw,
            incremental_desktop_with_implementation_wan=[desktop_hw[i] + cost['desktop_development_days'][i] * cost['day_cost_cny'] / 10000 for i in (0, 1)]))
    config = next(c for c in a['configurations'] if c['id'] == 'A2')
    model = next(m for m in a['models'] if m['id'] == config['model'])
    task = next(t for t in a['task_templates'] if t['id'] == 'T2')
    eff = next(e for e in a['efficiency_scenarios'] if e['id'] == 'base')
    cache = next(c for c in a['cache_scenarios'] if c['id'] == 'reuse70')
    for name, count, slots, output_scale in [('base', 20, 8, 1), ('two_model_branches', 40, 8, 1), ('tools_4', 20, 4, 1), ('tools_16', 20, 16, 1), ('double_completion_budget', 20, 8, 2)]:
        inputs, extra_prefix = [], 0
        for turn, size in enumerate(task['inputs']):
            if turn in task['cache_reset_turns']:
                extra_prefix = 0
            inputs.append(size + extra_prefix)
            extra_prefix += task['outputs'][turn] * (output_scale - 1)
        t = {**task, 'inputs': inputs, 'outputs': [x * output_scale for x in task['outputs']]}
        output['sensitivities'].append({'name': name, 'interpretation': 'Two branches = two independent T2 traces per parent; parent joining/review needs extra calls.' if name == 'two_model_branches' else 'One input variable changed.', **simulate(config, model, a['gpus'][config['gpu']], t, eff, cache, {**a['scheduler'], 'tool_slots': slots}, count)})
    (ROOT / 'results.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(f"Wrote {len(output['cases'])} task cases, costs and sensitivities.")


if __name__ == '__main__':
    main()
