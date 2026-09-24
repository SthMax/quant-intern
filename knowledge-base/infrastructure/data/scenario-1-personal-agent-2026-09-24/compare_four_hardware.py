"""Four requested hosts, Qwen3.8-27B FP8-family weights, full-precision KV.

Analytical scenarios, not hardware benchmarks. Run with Python 3. All GB are
decimal. No quantized KV, CPU offload, sliding-window eviction or MTP uplift.
"""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]
SOURCE = REPO / 'knowledge-base/sources/TECH-070/qwen27/config.json'
PRICE_SOURCE = ROOT.parent / 'hardware-prices-2026-09-21.json'
cfg = json.loads(SOURCE.read_text())['text_config']
full_layers = cfg['layer_types'].count('full_attention')
linear_layers = cfg['layer_types'].count('linear_attention')
KV_BYTES = full_layers * 2 * cfg['num_key_value_heads'] * cfg['head_dim'] * 2
RECURRENT = (linear_layers * cfg['linear_num_value_heads']
             * cfg['linear_key_head_dim'] * cfg['linear_value_head_dim'] * 4)
CONV = (linear_layers * (2 * cfg['linear_num_key_heads'] * cfg['linear_key_head_dim']
                        + cfg['linear_num_value_heads'] * cfg['linear_value_head_dim'])
        * (cfg['linear_conv_kernel_dim'] - 1) * 2)
STATE = RECURRENT + CONV
WINDOWS = [131072, 262144, 524288]
OUTPUT = 8192
WEIGHTS = 31.0
SCENARIOS = [('low', .45, .004), ('base', .60, .002), ('high', .75, .001)]
PROFILES = [
    dict(id='6000d', name='1 x RTX PRO 6000D 84GB', memory_gb=84,
         os_tools_gb=0, bw_gb_s=1398, tp=1, tp_efficiency=1,
         effective_tflops_per_device=dict(low=60, base=100, high=145),
         weights_format='Official block-scaled FP8; 31 GB from archived tensor inventory'),
    dict(id='2x6000d', name='2 x RTX PRO 6000D 84GB, TP2', memory_gb=168,
         os_tools_gb=0, bw_gb_s=1398, tp=2, tp_efficiency=.75,
         effective_tflops_per_device=dict(low=60, base=100, high=145),
         weights_format='One official FP8 model sharded by TP2; not two replicas'),
    dict(id='mac_ultra', name='M5 Ultra 80-GPU-core, 256GB / 2TB', memory_gb=256,
         os_tools_gb=32, bw_gb_s=1200, tp=1, tp_efficiency=1,
         effective_tflops_per_device=dict(low=16, base=32, high=50),
         weights_format='MLX MXFP8, converted from BF16; 31 GB engineering budget, not measured artifact size'),
    dict(id='spark', name='NVIDIA DGX Spark, 128GB / 4TB', memory_gb=128,
         os_tools_gb=24, bw_gb_s=273, tp=1, tp_efficiency=1,
         effective_tflops_per_device=dict(low=12, base=24, high=40),
         weights_format='Official block-scaled FP8; ARM64 / SM121 engine build'),
]


def pool(p, fraction=.9):
    return (p['memory_gb'] - p['os_tools_gb']) * fraction - WEIGHTS - 6 * p['tp']


def cache(context, count=1):
    return (context * KV_BYTES + 9 * STATE) * count / 1e9 * 1.15


def token_capacity(p, count=1, fraction=.9):
    return max(0, math.floor((pool(p, fraction) * 1e9 / 1.15 / count - 9 * STATE)
                            / KV_BYTES / 256) * 256)


def tp_communication(p, tokens=1, chunks=1):
    if p['tp'] == 1:
        return 0.0
    collectives = 2 * cfg['num_hidden_layers']
    payload_gb = (collectives * 2 * (p['tp'] - 1) / p['tp']
                  * cfg['hidden_size'] * 2 * tokens / 1e9)
    return collectives * 30e-6 * chunks + payload_gb / 24


def prefill_flops(n):
    return (2 * 27e9 * n * 1.15
            + 2 * full_layers * cfg['num_attention_heads'] * cfg['head_dim'] * n * n)


def evaluate(p, context, name, util, overhead, fraction=.9):
    avg_context = context - OUTPUT / 2
    traffic = WEIGHTS + avg_context * KV_BYTES / 1e9 + 2 * STATE / 1e9 + .05
    bw = p['bw_gb_s'] * p['tp'] * p['tp_efficiency'] * util
    tf = p['effective_tflops_per_device'][name] * p['tp'] * p['tp_efficiency']
    flops = (2 * 27e9 * 1.15 + 4 * full_layers * cfg['num_attention_heads']
             * cfg['head_dim'] * avg_context)
    comm = tp_communication(p)
    step = max(traffic / bw, flops / (tf * 1e12)) + overhead + comm
    fits = cache(context) <= pool(p, fraction)
    probes = []
    if fits:
        n = context - OUTPUT
        for mode, reused in [('cold', 0), ('warm1k', n - 1024)]:
            delta = n - reused
            seconds = ((prefill_flops(n) - prefill_flops(reused)) / (tf * 1e12)
                       + tp_communication(p, delta, math.ceil(delta / 2048)))
            probes.append(dict(mode=mode, input_tokens=n, cached_tokens=reused,
                newly_processed_tokens=delta, analytical_prefill_seconds=seconds,
                prefill_new_tokens_per_second=delta / seconds,
                ttft_compute_proxy_seconds=seconds + step,
                qualification='Compute-budget proxy; excludes queue, model load, tool and host overhead; not a measured TTFT'))
    return dict(config=p['id'], context_tokens=context, efficiency=name,
        memory_fraction=fraction, cache_gb=cache(context), cache_pool_gb=pool(p, fraction),
        memory_fits=fits, memory_headroom_gb=pool(p, fraction) - cache(context),
        traffic_gb_per_step=traffic, effective_bandwidth_gb_s=bw,
        effective_tflops=tf, compute_step_s=flops / (tf * 1e12),
        communication_s=comm, fixed_overhead_s=overhead,
        decode_tokens_s=1 / step if fits else None,
        arithmetic_decode_tokens_s_before_capacity_gate=1 / step,
        decode_ms_per_token=step * 1000 if fits else None,
        decode_only_seconds_for_8192=OUTPUT * step if fits else None,
        target_20_met_in_scenario=fits and 1 / step >= 20,
        required_bandwidth_fraction_for_20=(traffic / (.05 - overhead - comm)
            / (p['bw_gb_s'] * p['tp'] * p['tp_efficiency'])),
        ideal_memory_only_tps=p['bw_gb_s'] * p['tp'] / traffic,
        prefill_probes=probes)


def prices():
    old = json.loads(PRICE_SOURCE.read_text())
    mac = next(x for x in old['workstations'] if x['id'] == 'W6')
    gpu4 = next(x for x in old['server_scenarios']['cases'] if x['id'] == 'G3')
    # Only the GPU component scales with quantity, never the complete 4-GPU server.
    unit = [x / 4 for x in gpu4['components']['gpu']]
    results = []
    for ident, n in [('6000d', 1), ('2x6000d', 2)]:
        bom = dict(gpu=[n * x for x in unit], cpu_16_to_32_cores=[8000, 16000],
            host_ram_128gb_rdimm=[16000, 34000], nvme_2x2tb=[3000, 6000],
            nic_10gbe=[1500, 3500],
            chassis_motherboard_risers=[18000, 32000] if n == 1 else [25000, 45000],
            psu_forced_air_cooling_cables=[8000, 16000] if n == 1 else [12000, 24000])
        service = [4000, 8000] if n == 1 else [6000, 12000]
        subtotal = [sum(v[i] for v in bom.values()) for i in range(2)]
        total = [subtotal[i] * 1.23 + service[i] for i in range(2)]
        results.append(dict(config=ident, price_class='D_component_budget_not_quote',
            components_exvat_assumed_cny=bom, subtotal_exvat_cny=subtotal,
            hardware_vat_preparation=.13, price_contingency=.10,
            delivery_and_3year_hardware_support_tax_included_cny=service,
            total_cny=total, rounded_outward_wan=[math.floor(total[0]/1000)/10, math.ceil(total[1]/1000)/10],
            scope='Integrator server, existing rack/network; 128GB CPU RAM separate from GPU memory, 4TB raw NVMe; no inference offload',
            qualification='GPU uses existing 50k–85k D input per card; host components are new analytical allowances. Not an HPE OEM quote or validated OEM BOM. Supplier must match passive cooling and true TP2 PCIe P2P topology.'))
    results.extend([
        dict(config='mac_ultra', price_class='A_official_dated_2026_09_21',
             total_cny=[mac['unit_price_cny']] * 2, scope=mac['price_scope_note'],
             source=mac['source_url']),
        dict(config='spark', price_class='C_foreign_list_converted_plus_D_local_budget',
             usd_list=4699, fx_usd_cny_scenario=7.0, converted_cny=4699 * 7,
             converted_plus_13percent_tax_preparation_cny=4699 * 7 * 1.13,
             china_delivery_budget_cny=[40000, 50000],
             scope='NVIDIA-branded 128GB / 4TB; US listing out of stock on observation; domestic delivered price not obtained',
             qualification='40k–50k is a D planning allowance for currency, tax, delivery and channel/service uncertainty; GX10/PGX prices are separate products',
             source='https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/')])
    return results


def main():
    cases = [evaluate(p, c, *s) for p in PROFILES for c in WINDOWS for s in SCENARIOS]
    tight = [evaluate(PROFILES[0], 524288, *s, fraction=.95) for s in SCENARIOS]
    capacities = []
    for p in PROFILES:
        for count in [1, 3]:
            maximum = token_capacity(p, count)
            capacities.append(dict(config=p['id'], resident_sessions=count,
                cache_pool_gb=pool(p), memory_only_tokens_per_session=maximum,
                memory_only_total_tokens=maximum * count,
                per_session_capped_at_selected_524k= min(maximum, 524288),
                fits_262k=cache(262144, count) <= pool(p),
                fits_524k=cache(524288, count) <= pool(p)))
    assert KV_BYTES == 65536 and STATE == 153944064
    assert len(cases) == 36 and len(capacities) == 8
    assert all(x['decode_tokens_s'] is None for x in cases if not x['memory_fits'])
    assert all(x['memory_fits'] for x in tight)
    for p in PROFILES:
        vals = [x for x in cases if x['config'] == p['id'] and x['efficiency'] == 'base']
        assert all(a['arithmetic_decode_tokens_s_before_capacity_gate'] > b['arithmetic_decode_tokens_s_before_capacity_gate']
                   for a,b in zip(vals, vals[1:]))
    r = dict(as_of='2026-09-24', status='Analytical sensitivity scenarios; no local hardware/model run',
        supersedes='Mixed-hardware / quantized-KV selection in speed-target-review.json; previous calculation retained as history',
        assumptions=dict(model='Qwen3.8-27B', weights_gb=WEIGHTS,
            mac_weights_note='MXFP8 engineering budget; actual conversion footprint unmeasured',
            kv_dtype='BF16/FP16', kv_bytes_token=KV_BYTES,
            recurrent_dtype='FP32', convolution_dtype='BF16/FP16', state_bytes=STATE,
            extra_state_copies=8, cache_padding=1.15, main_memory_fraction=.9,
            runtime_reserve_gb_per_device=6, output_tokens=OUTPUT,
            single_active_user=True, speculative_decoding=False,
            native_context=262144, extended_context=524288, extension='YaRN factor 2',
            tp2_efficiency=.75, tp2_link_gb_s=24, tp2_collective_latency_us=30,
            effective_tflops_note='Engineering assumptions carried from earlier scenario math, not vendor peaks',
            uncertainty='45/60/75% are sensitivity choices, not a measured range or confidence interval',
            prefill_note='F(N)-F(K) assumes all named prefix KV and recurrent checkpoint are reusable; first model loading and queue are excluded'),
        sources=dict(config=str(SOURCE.relative_to(REPO)),
            config_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            price_ledger=str(PRICE_SOURCE.relative_to(REPO)),
            price_ledger_sha256=hashlib.sha256(PRICE_SOURCE.read_bytes()).hexdigest(),
            evidence='knowledge-base/sources/TECH-075/four-hardware-evidence.md'),
        profiles=PROFILES, cases=cases, single_6000d_95percent_memory=tight,
        capacities=capacities, prices=prices())
    (ROOT/'four-hardware-comparison.json').write_text(json.dumps(r, ensure_ascii=False, indent=2)+'\n')
    for p in PROFILES:
        rows=[x for x in cases if x['config']==p['id'] and x['efficiency']=='base']
        print(p['id'], 'decode:', [round(x['decode_tokens_s'],2) if x['memory_fits'] else 'capacity gate' for x in rows],
              'KV pool:', round(pool(p),2), 'capacity:', token_capacity(p), '3-session capacity:', token_capacity(p,3))
        for x in rows:
            print(' ',x['context_tokens'], 'range', [round(y['decode_tokens_s'],1) if y['memory_fits'] else None
                  for y in cases if y['config']==p['id'] and y['context_tokens']==x['context_tokens']],
                  'prefill', [(y['mode'], round(y['prefill_new_tokens_per_second'],1), round(y['ttft_compute_proxy_seconds'],1)) for y in x['prefill_probes']])
    for p in r['prices']:
        print('price',p['config'],p.get('total_cny',p.get('china_delivery_budget_cny')))


if __name__ == '__main__':
    main()
