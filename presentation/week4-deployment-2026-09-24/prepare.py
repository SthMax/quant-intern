"""Select presentation figures from the three scenario calculations."""
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
BASE = REPO / 'knowledge-base/infrastructure'
SOURCES = [
 'scenario-2-enterprise-rag-2026-09-23.md',
 'scenario-3-company-agent-2026-09-23.md',
 'scenario-1-personal-agent-2026-09-24.md',
 'data/scenario-2-rag-2026-09-23/results.json',
 'data/scenario-3-agent-2026-09-23/long-context-results.json',
 'data/scenario-3-agent-2026-09-23/results.json',
 'data/scenario-1-personal-agent-2026-09-24/results.json',
 'data/hardware-prices-2026-09-21.json',
 'data/scenario-1-personal-agent-2026-09-24/four-hardware-comparison.json',
]
def read(name): return json.loads((BASE / name).read_text())
s1=read(SOURCES[3]); s2serve=read(SOURCES[4]); s2=read(SOURCES[5]); s3=read(SOURCES[6])
values={}; evidence={}
def put(key, value, source, selector):
 values[key]=str(value); evidence[key]={'display':str(value),'source':source,'selection':selector}
def range_text(xs, decimals=0):
 return '-'.join(f'{x:.{decimals}f}' for x in xs)
for cid in ['H2','H3','H4']:
 x=next(x for x in s1['cases'] if x['config']==cid and x['model']=='Qwen3.8-27B-FP8' and x['efficiency']=='base' and x['concurrency']==20)
 c=next(x for x in s1['costs']['configurations'] if x['config']==cid)
 for label,field,fmt in [('First','burst_ttft_last_s','.1f'),('End','burst_e2e_last_s','.1f'),('Rate','per_request_decode_tps_min','.0f'),('Total','decode_peak_total_tps',',.0f'),('Wall','burst_output_tps_including_prefill_and_retrieval',',.0f')]:put('S1'+cid+label,format(x[field],fmt),SOURCES[3],f'{cid}/Qwen27/base/C20/{field}')
 put('S1'+cid+'Price',range_text(c['hardware_wan_cny']),SOURCES[3],f'{cid}/hardware_wan_cny')
 for label,field in [('Enterprise','enterprise_initial_excluding_license_wan_cny'),('Custom','custom_initial_wan_cny')]:put('S1'+cid+label,'-'.join(f'{v:g}' for v in c[field]),SOURCES[3],f'{cid}/{field}')
a0=next(x for x in s2['costs'] if x['config']=='A0')
for key,field in [('CentralWorkers','incremental_central_hardware_wan'),('DesktopGateway','incremental_desktop_hardware_wan')]:put(key,range_text(a0[field]),SOURCES[5],f'A0/zero-new-GPU/{field}')
for cid in ['A2','A3','A4','A5']:
 x=next(x for x in s2serve['cases'] if x['config']==cid and x['efficiency']=='base' and x['concurrent_tasks']==20 and x['context_tokens_per_task']==262144 and x['mode']=='warm1k')
 c=next(x for x in s2['costs'] if x['config']==cid)
 for label,field,fmt in [('First','ttft_last_s','.1f'),('End','batch_completion_s','.1f'),('Rate','per_request_decode_tps_min','.0f'),('Total','decode_total_tps',',.0f'),('Wall','whole_request_output_tps',',.0f')]:put('S2'+cid+label,format(x[field],fmt),SOURCES[4],f'{cid}/base/C20/262K/warm1k/{field}')
 for label,field in [('NewPrice','incremental_central_hardware_wan'),('Combined','combined_s1_s2_central_hardware_wan'),('Setup','incremental_central_with_implementation_wan')]:put('S2'+cid+label,range_text(c[field]),SOURCES[5],f'{cid}/{field}')
 for count in [5,20,30,50]:
  k=next(z for z in s2serve['capacity'] if z['config']==cid and z['resident_sequences']==count and z['mode']=='architecture_reclaimed')
  put('Agent'+cid+'C'+str(count),f"{k['equal_context_tokens_per_sequence']:,}",SOURCES[4],f'{cid}/resident{count}/equal_context_tokens_per_sequence')
four=read(SOURCES[8])
for cid,key in [('6000d','One'),('2x6000d','Two'),('mac_ultra','Mac'),('spark','Spark')]:
 for window,label in [(131072,'131'),(262144,'262'),(524288,'524')]:
  x=next(x for x in four['cases'] if x['config']==cid and x['context_tokens']==window and x['efficiency']=='base')
  rate=x['decode_tokens_s']
  if rate is None:
   x=next(x for x in four['single_6000d_95percent_memory'] if x['efficiency']=='base');rate=x['decode_tokens_s']
  put('F'+key+label,f'{rate:.1f}',SOURCES[8],f'{cid}/C1/{window}/base; 6000d524 uses95percent memory')
 cap=next(x for x in four['capacities'] if x['config']==cid and x['resident_sessions']==1)
 put('F'+key+'Cache',f"{cap['cache_pool_gb']:.1f}",SOURCES[8],f'{cid}/cache_pool_gb')
 c=next(x for x in four['prices'] if x['config']==cid)
 if cid in ['6000d','2x6000d']:display=range_text(c['rounded_outward_wan'],1)
 elif cid=='mac_ultra':display=f"{c['total_cny'][0]/10000:.2f}"
 else:display=range_text([v/10000 for v in c['china_delivery_budget_cny']],0)
 put('F'+key+'Price',display,SOURCES[8],f'{cid}/hardware cash budget CNY / 10000')
(ROOT/'data/slide-data.tex').write_text('% Generated from scenario JSON; do not edit.\n'+''.join('\\expandafter\\def\\csname val:'+k+'\\endcsname{'+v+'}\n' for k,v in values.items()))
manifest={'as_of':'2026-09-24','price_observed':'2026-09-21 / 2026-09-24; exact observation and estimate types in scenario sources','performance_status':'uncalibrated engineering estimates','sources':{str((BASE/name).relative_to(REPO)):{'sha256':hashlib.sha256((BASE/name).read_bytes()).hexdigest()} for name in SOURCES},'figures':evidence,'order':[1,2,3],'main_slides':12,'appendix_slides':4}
(ROOT/'data/source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'Prepared {len(values)} sourced display values for 16 slides.')
