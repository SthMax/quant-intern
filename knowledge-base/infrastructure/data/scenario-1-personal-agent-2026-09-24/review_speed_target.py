"""Single-user 20 token/s screening. No hardware measurement or MTP uplift.

This isolates memory traffic and declared fixed/TP overhead. Matrix-compute
and real kernel effects require device testing. Procurement status is separate.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PROFILES=[
 dict(id='mac_max',name='M5 Max 128GB',bandwidth=614,memory_budget=93.6,weights=30,tp=1,parallel_eff=1,procurement='Existing W4 dated Chinese price input'),
 dict(id='mac_ultra',name='M5 Ultra 256GB',bandwidth=1200,memory_budget=201.6,weights=30,tp=1,parallel_eff=1,procurement='Existing W6 dated Chinese price input'),
 dict(id='rtx5000',name='RTX PRO 5000 72GB',bandwidth=1344,memory_budget=72*.9,weights=31,tp=1,parallel_eff=1,procurement='Existing W7 analytical OEM tower'),
 dict(id='6000d',name='RTX PRO 6000D 84GB',bandwidth=1398,memory_budget=84*.9,weights=31,tp=1,parallel_eff=1,procurement='Server SKU, existing HPE China/HK evidence; fit to proper server chassis'),
 dict(id='2x6000d',name='2 x RTX PRO 6000D, TP2',bandwidth=1398,memory_budget=2*84*.9,weights=31,tp=2,parallel_eff=.75,procurement='Analytical two-GPU server; PCIe P2P/topology and OEM quote to be verified'),
 dict(id='rtx6000_reference',name='RTX PRO 6000 96GB',bandwidth=1792,memory_budget=96*.9,weights=31,tp=1,parallel_eff=1,procurement='Technical comparison only; not interchangeable with China/HK 6000D SKU'),
 dict(id='h200',name='H200 NVL 141GB',bandwidth=4800,memory_budget=141*.9,weights=31,tp=1,parallel_eff=1,procurement='Licensed-delivery server route from existing research; not a desktop air-cooled card'),
]
WINDOWS=[131072,262144,524288]
EFFICIENCY=[('low',.45,.004),('base',.60,.002),('high',.75,.001)]
# From archived Qwen3.8-27B architecture; state is unchanged by KV precision.
STATE=153944064
KV_BF16=65536
TARGET=20
rows=[]
for c in PROFILES:
 for context in WINDOWS:
  for kv in ['bf16','8bit']:
   ratio=1 if kv=='bf16' else (.53125 if c['id'].startswith('mac') else .5)
   bpt=KV_BF16*ratio
   pool=c['memory_budget']-c['weights']-6*c['tp']
   cache_gb=(context*bpt+9*STATE)/1e9*1.15
   for name,util,overhead in EFFICIENCY:
    average_context=context-4096  # 8192 reserved outputs, average decode position
    traffic=c['weights']+average_context*bpt/1e9+2*STATE/1e9+.05
    bw=c['bandwidth']*c['tp']*c['parallel_eff']*util
    # Dense TP2: two collectives/layer, 64 layers, BF16 hidden dimension 5120.
    comm=0 if c['tp']==1 else 128*30e-6+(128*2*(c['tp']-1)/c['tp']*5120*2/1e9)/24
    step=traffic/bw+overhead+comm
    fits=cache_gb<=pool
    rows.append(dict(config=c['id'],context_tokens=context,kv=kv,efficiency=name,
      cache_gb=cache_gb,cache_pool_gb=pool,memory_fits=fits,traffic_gb_per_step=traffic,
      effective_bandwidth_gb_s=bw,overhead_s=overhead,communication_s=comm,
      required_effective_bandwidth_for_20=traffic/(1/TARGET-overhead-comm),
      estimated_tps=1/step if fits else None,meets_20_in_this_case=fits and 1/step>=TARGET))
r=dict(status='Uncalibrated memory-side screening; not benchmarks or promised service',
 objective='Single active user >=20 output tokens/s; compare full 262K and 524K sessions',
 assumptions={'weight_bits_min':8,'kv_options':['BF16/FP16','8-bit (MLX metadata allowance or FP8)'],
  'extra_state_copies':8,'cache_overhead_factor':1.15,'mtp_gain_assumed':0,
  'tp2_parallel_efficiency':.75,'tp2_collectives_per_layer':2,'tp2_collective_latency_us':30,'tp2_link_gb_s':24,
  'precision_quality':'8-bit KV requires quality/calibration check; it does not imply four-bit model weights'},
 profiles=PROFILES,cases=rows,
 sources={'rtx6000':'https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/',
 'qwen_recipe':'https://recipes.vllm.ai/Qwen/Qwen3.8-27B',
 'fp8_kv':'https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/',
 'existing_hardware':'knowledge-base/infrastructure/data/hardware-prices-2026-09-21.json'})
assert len(rows)==126
for x in rows:
 if x['estimated_tps'] is not None:
  assert abs(x['estimated_tps']*(x['traffic_gb_per_step']/x['effective_bandwidth_gb_s']+x['overhead_s']+x['communication_s'])-1)<1e-10
(ROOT/'speed-target-review.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
for c in PROFILES:
 for kv in ['bf16','8bit']:
  vals=[next(x for x in rows if x['config']==c['id'] and x['context_tokens']==w and x['kv']==kv and x['efficiency']=='base') for w in [262144,524288]]
  print(c['id'],kv,[round(x['estimated_tps'],1) if x['memory_fits'] else 'does not fit' for x in vals])
