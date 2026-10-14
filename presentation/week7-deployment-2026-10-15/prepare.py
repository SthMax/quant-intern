"""Bind slide numbers to approved notes and preserved research calculations."""
from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
paths={
 'notes':HERE/'speaker-notes.md',
 'deployment':REPO/'knowledge-base/infrastructure/data/week7-deployment-2026-10-12/results.json',
 'spark_test':REPO/'knowledge-base/infrastructure/data/dgx-spark-qwen27-external-2026-10-12/summary.json',
 'server_prices':REPO/'knowledge-base/infrastructure/data/hardware-prices-2026-10-12.json',
 'spark_price':REPO/'knowledge-base/infrastructure/data/week7-deployment-2026-10-12/spark-price.json',
 'a100':REPO/'knowledge-base/infrastructure/data/deepseek-a100-project-2026-10-12/mechanism-analysis.json',
 'book':REPO/'knowledge-base/infrastructure/data/ai-infra-book-2026-10-12/results.json',
 'tokha':REPO/'knowledge-base/sources/TECH-088/tokha-ablation.md',
 'kepler':REPO/'knowledge-base/sources/TECH-088/kepler-performance.md',
}
d=json.loads(paths['deployment'].read_text());s=json.loads(paths['spark_test'].read_text());p=json.loads(paths['server_prices'].read_text());a=json.loads(paths['a100'].read_text());v={};prov={}
def add(k,display,src,field):
 v[k]=str(display);prov[k]={'display':str(display),'source':str(paths[src].relative_to(REPO)),'field_or_method':field}
for x in d['spark_matrix']:
 if x['kv']=='fp8' and x['resident_sessions']==1 and x['active_requests']==1:
  label={131072:'131',262144:'262',524288:'512',1000000:'1M'}[x['context_tokens']]
  add('SparkD'+label,f"{x['single_fp8_mtp3_decode_shape_estimate']:.1f}",'deployment',f'spark_matrix context={x["context_tokens"]}; single_fp8_mtp3_decode_shape_estimate')
  add('SparkP'+label,f"{x['single_fp8_cold_prefill_fit_seconds']/60:.1f}",'deployment',f'spark_matrix context={x["context_tokens"]}; cold_prefill_fit/60 minutes')
  for k,field in [('New1','ideal_cache_1k_prefill_difference_seconds'),('New8','ideal_cache_8k_prefill_difference_seconds')]:
   add('Spark'+k+label,f"{x[field]:.0f}",'deployment',f'spark_matrix context={x["context_tokens"]}; {field}, rounded seconds')
add('Pool',f"{s['startup']['estimated_shared_kv_token_pool']/1e6:.2f}",'spark_test','startup.estimated_shared_kv_token_pool /1e6')
add('PoolExact',f"{s['startup']['estimated_shared_kv_token_pool']:,}",'spark_test','startup.estimated_shared_kv_token_pool')
for x in d['post_graph_budget_sensitivity'][:3]:
 label={'442505':'H100','442751':'H200four','442758':'H200eight'}[x['anchor_id']]
 add(label+'Strict',f"{x['max_context_with_10pct_token_reserve']:,}",'deployment','post_graph_budget_sensitivity anchor='+x['anchor_id'])
 if x['max_context_with_10pct_token_reserve']<1000000:add(label+'K',f"{x['max_context_with_10pct_token_reserve']/1000:.0f}",'deployment','post_graph_budget_sensitivity; rounded K tokens')
for x in p['server_cases']:
 label={'A1008-SXM-refurb':'A100Price','H1008-SXM':'H100Price','H2004-NVL':'H200fourPrice','H2008-SXM':'H200eightPrice'}[x['id']]
 add(label,'-'.join(map(str,x['rounded_outward_wan_cny'])),'server_prices',x['id']+'; rounded_outward_wan_cny')
nb=a['native_checkpoint_budget']
for k,field,div,fmt in [('NativeGB','checkpoint_bytes',1e9,'.2f'),('EngramGB','engram_host_bytes',1e9,'.2f'),('GPUWeightsGB','remaining_checkpoint_bytes',1e9,'.2f'),('GPUWeightsGiB','remaining_checkpoint_gib',1,'.2f'),('PerCard','ideal_four_gpu_weight_gib_each',1,'.2f')]:
 add(k,format(nb[field]/div,fmt),'a100','native_checkpoint_budget.'+field)
for k,num in [('AblationBase',2842.48),('AblationDense',2926.08),('AblationComm',2970.50)]:
 assert f'{num:,.2f}' in paths['tokha'].read_text();add(k,f'{num:,.2f}','tokha','published C128 two-run mean')
assert len(d['capacity_matrix'])==280 and nb['checkpoint_bytes']-nb['engram_host_bytes']==nb['remaining_checkpoint_bytes']
(HERE/'data').mkdir(exist_ok=True)
(HERE/'data/slide-data.tex').write_text('% Generated from preserved research inputs.\n'+''.join('\\expandafter\\def\\csname val:'+k+'\\endcsname{'+val+'}\n' for k,val in v.items()))
manifest={'prepared':'2026-10-14','presentation_date':'2026-10-15','notes_status':'User approved before Beamer authoring','sources':{str(path.relative_to(REPO)):{'sha256':hashlib.sha256(path.read_bytes()).hexdigest()} for path in paths.values()},'figures':prov,'main_slides':20,'appendix_slides':5,'scope':'No new GPU experiment; dates and workload conditions stay with their results.'}
(HERE/'data/source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'Prepared {len(v)} bound values from {len(paths)} sources.')
