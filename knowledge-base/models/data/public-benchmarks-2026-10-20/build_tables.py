"""Rebuild evidence tables and editable SVG figures from archived public sources.

No model endpoint is called. Python with lxml is required for HTML extraction.
"""
import csv, hashlib, json, pathlib, shutil
from lxml import html

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
SRC = ROOT / 'knowledge-base/sources/TECH-091'

def write_csv(name, rows):
    with (HERE/name).open('w', newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def table(key):
    root=html.fromstring((SRC/'benchmarks'/key/'source.html').read_bytes())
    return [[' '.join(c.text_content().split()) for c in row.xpath('./th|./td')]
            for row in root.xpath('//table')[0].xpath('.//tr')]

extract_rows=list(csv.DictReader((SRC/'benchmarks/extractbench/leaderboard.csv').open()))
wanted=['Qwen3.8 27B','Qwen3.6 35B','DeepSeek V4.1 Flash','GLM-5.3 Flash','Kimi K3','Gemma4 26B']
conditions={
 'Qwen3.8 27B':('Qwen3.8-27B-FP8','qwen3_8_27b_fp8_vllm_extract_oneshot_structured_output_file','self-hosted vLLM','not explicitly set; endpoint default',32768,'150 dpi'),
 'Qwen3.6 35B':('Qwen3.6-35B-A3B-FP8','qwen3_6_35b_a3b_fp8_vllm_extract_oneshot_structured_output_file','self-hosted vLLM','not explicitly set; endpoint default',32768,'150 dpi'),
 'Gemma4 26B':('Gemma-4-26B-A4B','gemma4_26b_vllm_extract_oneshot_structured_output_file','self-hosted vLLM','not explicitly set; endpoint default',32768,'100 dpi'),
 'DeepSeek V4.1 Flash':('DeepSeek-V4.1-Flash (not 1017)','deepseek_v4_1_flash_extract_oneshot_structured_output_file','DeepSeek API; deepseek-flash','disabled',65536,'150 dpi'),
 'GLM-5.3 Flash':('GLM-5.3-Flash','glm_5_3_flash_extract_oneshot_structured_output_file','z.ai API; glm-5.3-flash','on; effort not explicitly set',131072,'raw file_url'),
 'Kimi K3':('Kimi-K3','kimi_k3_extract_oneshot_structured_output_file','Fireworks API; accounts/fireworks/models/kimi-k3','not explicitly set; provider default',131072,'150 dpi'),
}
out=[]
for name in wanted:
 r=next(r for r in extract_rows if r['Provider']==name)
 m,p,e,t,b,d=conditions[name]
 out.append({'model':m,'overall_f1':r['Overall'],'short_f1':r['Short'],'medium_f1':r['Medium'],'long_f1':r['Long'],
             'long_precision':r['P_Long'],'long_recall':r['R_Long'],'pipeline':p,'endpoint':e,'thinking':t,'max_output_tokens':b,
             'input':d,'temperature':0,'benchmark':'ExtractBench original; 370 documents; macro value F1',
             'code_revision':'56b8fdd91b2cf3648caf75c717c68441ecf4d43f','model_revision_at_run':'not disclosed',
             'source':'https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/leaderboard.csv'})
write_csv('extractbench.csv',out)

finance_names=['Qwen 3.8 27B','DeepSeek V4.1 Flash','DeepSeek V4.1 Flash 1017','GLM 5.3 Flash','GLM 5.3','MiMo V2.6 Flash','MiMo V2.6 Pro','Kimi K3']
ft=table('vals-fabv2');write_csv('finance-agent-full-snapshot.csv',[dict(zip(ft[0],r)) for r in ft[1:] if len(r)==len(ft[0])])
finance=[]
for n in finance_names:
 r=next(r for r in ft[1:] if r[1]==n)
 finance.append({'model':n,'partial_credit_pct':r[2].rstrip('%'),'cost_usd_per_test':r[3].lstrip('$'),'duration':r[5],
                 'benchmark_version':'Finance Agent v2','page_updated':'2026-10-18','metric':'dealbreaker-gated severity-weighted partial credit',
                 'harness':'shared default; six tools; 2h task timeout','thinking_at_run':'not disclosed per model on benchmark page',
                 'model_revision_at_run':'API model label; weight SHA not disclosed','source':'https://www.vals.ai/benchmarks/fabv2'})
write_csv('finance-agent-v2.csv',finance)

aa=[]
aa_models=[('aa-deepseek-qwen',1,'DeepSeek-V4.1-Flash','max'),('aa-deepseek-qwen',2,'Qwen3.8-27B','xhigh'),
           ('aa-glm-kimi',1,'GLM-5.3-Flash','label has no effort suffix'),('aa-glm-kimi',2,'Kimi-K3','max'),
           ('aa-mimo-qwen',1,'MiMo-V2.6-Flash','label has no effort suffix'),('aa-gemma-qwen',2,'Gemma-4-31B','reasoning')]
for key,col,name,effort in aa_models:
 rows=table(key); lookup={r[0]:r[col] for r in rows if len(r)>col}
 for metric in ['AA-LCR v1.1','AutomationBench-AA','Terminal-Bench 4.0','SciCode','GDP.pdf']:
  aa.append({'model':name,'reasoning_label':effort,'benchmark':metric,'score_pct':lookup[metric].rstrip('%'),
             'retrieval_date':'2026-10-20','source':next(r['requested_url'] for r in json.loads((SRC/'aa-retrievals.json').read_text()) if key in r.get('path','')),
             'note':'SciCode is marked Under review on source; not used as principal recommendation'})
write_csv('artificial-analysis.csv',aa)

biz=[]
for n,g,p,f,i,s,stable in [('Qwen3.8-27B',42,74,93.3,28,32.7,10),('DeepSeek-V4.1-Flash',46.7,92,96.7,9.3,43.3,26),('GLM-5.3-Flash',48,79.3,87.3,29.3,43.3,22)]:
 biz.append({'model':n,'goal_pct':g,'process_pct':p,'protection_pct':f,'intermediate_failure_pct':i,'strict_success_pct':s,
             'pass_power_3_pct':stable,'tasks':50,'runs_per_task':3,'user_simulator':'DeepSeek-V4.1-Flash',
             'reasoning_at_run':'not fully disclosed per model in paper; repository template is not a run log',
             'source':'https://arxiv.org/html/2610.20424v1#S5.T1','table':'Table 1; pass^3 from section 5.2'})
write_csv('bizbench.csv',biz)

rele=[]
for n,score in [('DeepSeek-V4.1-Flash',82.4),('GLM-5.3-Flash',82.4),('GLM-5.3',84),('Kimi-K3',80.8),('MiMo-V2.6-Pro',80),('MiMo-V2.6-Flash',76),('Gemma-4-31B-it',70.4),('Gemma-4-26B-A4B-it',68.8)]:
 rele.append({'model':n,'finance_knowledge_accuracy_pct':score,'task':'ReLE Chinese finance basic knowledge','snapshot_version':'v5.12.7; 2026-10-15',
              'thinking_tools_harness':'not disclosed per row','model_revision_at_run':'model label only; not frozen SHA',
              'usage':'supplement only; Qwen3.8-27B absent; cannot infer 0',
              'source':'https://github.com/jeinlee1991/chinese-llm-benchmark/blob/main/leaderboard/金融基础知识.md'})
write_csv('chinese-finance-supplement.csv',rele)

# Preserve only the source files actually inspected for ExtractBench conditions.
repo=ROOT/'.research-workspace/repos/extractbench-final-2026-10-20'
paths=['src/extract_bench/inference/pipelines/extract.py']+[
 'src/extract_bench/inference/providers/extract/'+n+'.py' for n in ['vllm_extract','deepseek_oneshot_extract','glm_zai_extract','kimi_extract']]
files=[]
for p in paths:
 target=SRC/'benchmarks/extractbench/files'/p;target.parent.mkdir(parents=True,exist_ok=True)
 if (repo/p).exists():
  shutil.copyfile(repo/p,target)
 elif not target.exists():
  raise FileNotFoundError(f'Archived source file is missing: {target}')
 files.append({'path':str(target.relative_to(SRC)),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
               'url':'https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/'+p})
(SRC/'code-manifest.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')

# Macro-average reconciliation makes the short-heavy weighting visible.
checks=[]
for r in out:
 recomputed=sum(float(r[k])*n for k,n in [('short_f1',252),('medium_f1',98),('long_f1',20)])/370
 checks.append({'model':r['model'],'published_overall':float(r['overall_f1']),'recomputed_from_rounded_splits':round(recomputed,4),
                'difference':round(recomputed-float(r['overall_f1']),4)})
 assert abs(recomputed-float(r['overall_f1']))<0.011
(HERE/'checks.json').write_text(json.dumps({'extractbench_macro':checks,'short_weight':252/370,'long_weight':20/370,'models_called':0},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'extractbench_rows':len(out),'finance_rows':len(finance),'aa_rows':len(aa),'bizbench_rows':len(biz),'models_called':0}))
