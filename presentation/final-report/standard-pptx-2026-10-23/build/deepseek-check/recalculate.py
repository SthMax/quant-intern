from decimal import Decimal as D
from pathlib import Path
import json
source=Path('../narrative-drafts-2026-10-22/d-revised-4-data.json')
d=json.loads(source.read_text())
inputs=[100000+10000*i for i in range(8)]
assert sum(inputs)==1080000
f=D('0.8')+D('0.2')*D('0.5')
price=[D('.30')*f,D('.006')*f,D('1.20')*f]
fee=(D('.216')*price[0]+D('.864')*price[1]+D('.016')*price[2])*D('7')*D('1.1')
results=[]
for s in d['scenarios']:
 tasks=s['people']*5*250*3
 cost=D(tasks)*fee+D(435000)
 assert abs(float(cost)-s['api_total_cny']['deepseek'])<1e-7
 results.append({'people':s['people'],'tasks_day':s['people']*5,'tasks_year':s['people']*5*250,'tasks_three_year':tasks,'api_calls_three_year_before_retry':tasks*8,'budgeted_api_call_equivalent':float(D(tasks*8)*D('1.1')),'call_cost_cny':float(D(tasks)*fee),'fixed_cny':435000,'total_cny':float(cost),'total_10k_cny':float(cost/D(10000))})
fresh=(D(156000)+D(924000)*D('.1'))*D('1.1')
assert fresh==273240
out={'checked_date':'2026-10-23','model':'DeepSeek-V4.1-Flash-1017','alias':'deepseek-flash','pricing_url':'https://api-docs.deepseek.com/quick_start/pricing/','cache_url':'https://api-docs.deepseek.com/guides/kv_cache/','benchmark_url':'https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-1017-vs-deepseek-v4-1-flash','input_tokens_by_round':inputs,'input_total':1080000,'output_total_including_reasoning_tools_text':16000,'uncached_input':216000,'cached_input':864000,'price_usd_million_peak':{'input':.30,'cache':.006,'output':1.20},'weighted_factor':float(f),'task_fee_cny':float(fee),'scenarios':results,'local_fresh_input_per_planned_task':float(fresh),'local_busy_hours_day_50_people':float((fresh/D(8000)+D(17600)/D(400))*D(250)/D(3600)),'aa_gdpval_v21':{'DeepSeek V4.1 Flash (Max)':1600,'DeepSeek V4.1 Flash 1017 (Max)':1746},'sample_data_match':True,'source_formula_match':True}
Path('build/deepseek-check/recalculated.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('Independent Decimal recalculation passed for task definitions, token quantities, annual scales and costs.')
