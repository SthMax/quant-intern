"""Apply reviewed copy edits to the generated draft and rebuild presenter notes."""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parent
p=ROOT/'data/slides.json';d=json.loads(p.read_text())
changes=json.loads((ROOT/'editorial/chinese-teacher-replacements.json').read_text())
for c in changes:
 target=d['slides'][c['slide_id']-1]
 for key in c['path'][:-1]:target=target[key]
 key=c['path'][-1]
 assert target[key]==c['old'],(c['slide_id'],c['path'])
 numbers=lambda value: re.findall(r'\d+(?:[.,]\d+)*',re.sub(r'(H100|H200|A100)(?=\d)',r'\1 ',value))
 assert numbers(c['old'])==numbers(c['new']),(c['slide_id'],'numbers')
 target[key]=c['new']
# Source-backed display clarifications identified during visual and content review.
d['slides'][22]['foot']='公开回放输入140K–157K、前缀命中约95%；载荷传输带宽24／6GB/s为假设。'
d['slides'][22]['rows'][4]=['20份会话同时读回','内存→GPU，总载荷146.16GB；约6.1秒']
d['slides'][17]['foot']='9月预算与条件计算，10月统一配置口径；性能数值为工程估算。'
d['slides'][3]['outcomes']=['富国披露：相关研报工作从一周以上缩短至3小时以内。','鹏华披露：营销审核修改建议的最新采纳率为91%。']
d['slides'][3]['notes']+=' 富国报告相关研报流程由一周以上缩短至3小时以内；鹏华报告989条有效修改建议、最新采纳率91%。均为公司自报的原项目整体流程／建议采纳口径。'
d['slides'][12]['foot']='假设SSD有效6GB/s；512K全注意力KV载荷读取约2.86秒，另计递推状态与调度。'
d['slides'][12]['readback_example']='512K载荷17.18GB ÷ 6GB/s ≈ 2.86秒'
d['slides'][7]['chart']['format']='0.00'
d['slides'][7]['chart']['title']='Finance Agent v2'
for c in d['slides'][29]['charts']:c['format']='0.00'
# Final visual-reading pass: keep complete Chinese phrases and product names together.
d['slides'][7]['side'][2]='对照：GLM Flash\n与MiMo Flash'
d['slides'][12]['side_title']='实现方式与状态要求'
d['slides'][15]['nodes'][0][1]='文件与权限（ACL）'
d['slides'][18]['right'][3]='CPU执行并保存产物'
d['slides'][26]['rows'][1][1]='统一检索、出处\n撤权同步'
d['slides'][26]['rows'][1][2]='接入与权限\n索引与平台'
d['slides'][26]['rows'][2][1]='较大模型\n多用户工具任务'
d['slides'][28]['rows'][3][0]='DeepSeek每计划任务\ntoken费'
d['slides'][28]['rows'][4][0]='Sonnet5.5每计划任务\ntoken费'
d['slides'][28]['foot']='基准假设：可复用前缀命中率95%；汇率7.00，API token费另加6%预算准备金。'
d['slides'][32]['rows'][1][1]='模型筛选与对照：\nQwen、DeepSeek、GLM'
d['slides'][34]['rows'][0][0]='Qwen3.8-27B／\nQwen3.6-35B-A3B'
d['slides'][35]['rows'][0][1]='Open WebUI／LobeHub\nCherry Studio'
d['slides'][35]['rows'][3][1]='Hermes／OpenClaw\nOpenCode／pi'
d['slides'][35]['rows'][5][1]='MLX／llama.cpp\nKTransformers'
d['slides'][40]['rows'][4][0]='技术资源／\n分析师工时价值'
# Keep the same complete phrases when the PPTX is rendered by LibreOffice.
d['slides'][22]['rows'][2][0]='1M会话：内存→GPU'
d['slides'][23]['rows'][0][0]='8×A100 80GB SXM\n（翻新）'
d['slides'][26]['rows'][0][1]='本地文件、代码\n连续会话'
d['slides'][30]['cols'][3]='本地／DeepSeek／Sonnet\n（万元）'
d['slides'][40]['rows'][0][0]='DeepSeek低峰\n未命中／命中／输出'
d['slides'][40]['rows'][1][0]='Sonnet\n输入／1h写／读／输出'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
parts=['# 最终汇报逐页讲稿\n\n2026年10月20日。34页正文与8页备查附录。\n']
for x in d['slides']:
 parts.append(f"## {x['id']:02d} {x['title'].replace(chr(10),' ')}\n\n{x['notes']}\n\n**接续：**{x['transition']}\n")
 if x['sources']:parts.append('\n来源：'+ ' · '.join(f'[{u.split("/")[2]}]({u})' for u in x['sources'])+'\n')
(ROOT/'speaker-notes.md').write_text('\n'.join(parts))
meta=json.loads((ROOT/'data/source-manifest.json').read_text())
meta.update(notes='Chinese-teacher review applied; source-backed clarifications added in visual review',editorial_replacements=len(changes),slides_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),speaker_notes_sha256=hashlib.sha256((ROOT/'speaker-notes.md').read_bytes()).hexdigest())
(ROOT/'data/source-manifest.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(f'Applied {len(changes)} copy edits; 42-page notes regenerated.')
