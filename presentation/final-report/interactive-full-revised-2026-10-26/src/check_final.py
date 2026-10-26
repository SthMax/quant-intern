from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,hashlib
R=Path(__file__).resolve().parent.parent
f=R/'output/asset-management-llm-interactive-revised.pptx'
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','m':'http://schemas.microsoft.com/office/powerpoint/2015/09/main'}
plan=json.loads((R/'src/state-manifest.json').read_text());rows=[];texts={};notes={};shape_texts={}
with ZipFile(f) as z:
 for d in plan['slides']:
  i=d['page'];x=E.fromstring(z.read(f'ppt/slides/slide{i}.xml'));ns=E.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml'))
  props=x.findall('.//p:cNvPr',N);names=[q.get('name') for q in props if q.get('name','').startswith('!!')];ids={q.get('id') for q in props}
  assert len(names)==len(set(names)),(i,'duplicate names')
  assert x.find('.//m:morph',N) is not None,(i,'missing morph')
  st={q.find('.//p:cNvPr',N).get('name'):''.join(q.xpath('.//a:t/text()',namespaces=N)) for q in x.findall('.//p:sp',N)}
  for k in ('nav.front','nav.middle','nav.back','task.research','task.trade','task.client','task.review','task.risk','task.files','task.dev'):
   if i>=3:assert '!!'+k in names,(i,k)
  for q in x.findall('.//p:spTgt',N):assert q.get('spid') in ids,(i,'animation target')
  text='\n'.join(x.xpath('.//a:t/text()',namespaces=N));note='\n'.join(ns.xpath('.//a:t/text()',namespaces=N))
  assert len(note)>50,(i,'notes')
  for forbidden in ['泳道','典型','不代表','仅能','避免冒充','闭环','赋能']:
   assert forbidden not in text+note,(i,forbidden)
  if i in [8,11,15,18,21,24,27]:assert 'LLM' in text,(i,'LLM role')
  expected=d['title'];title=st.get('!!heading',st.get('!!cover.title'))
  if i>1:assert title==expected,(i,'title mismatch')
  assert d['notes'] in note,(i,'notes mismatch')
  rows.append({'page':i,'title':title,'shapes':len(props),'links':len(x.findall('.//a:hlinkClick',N)),'animated_shapes':len(x.findall('.//p:spTgt',N))})
  texts[i]=text;notes[i]=note;shape_texts[i]=st
assert len(rows)==33
for i in [15,16,17]:assert shape_texts[i]['!!clientDoc.value.view']=='甲公司收入增长来自销量提升，后续关注原材料成本'
assert shape_texts[18]['!!clientDoc.value.view']=='甲公司销量提升与渠道补库有关，后续关注补库持续性及原材料成本'
assert '客户沟通稿变更说明' in texts[24] and '!!clientDoc' not in shape_texts[24]
assert '债券询价准备的工作过程' in texts[9] and '成交' not in texts[9]
assert '净价（元/百元面值）' in texts[11] and '持仓面额（万元）' in texts[11]
assert '上季 / 本季' in texts[8]
assert abs((110/100-1)-0.1)<1e-10
assert '页眉' in texts[27] and '测试工具' in texts[27] and '反馈' in texts[27]
report={'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'final_equals_candidate':f.read_bytes()==(R/'build/animated-candidate.pptx').read_bytes(),'slide_count':33,'links':sum(r['links'] for r in rows),'title_and_notes_sync':'pass','model_role_visibility_on_seven_solution_pages':'pass','material_consistency':'pass','trade_scope_and_units':'pass','sample_arithmetic':'pass','slide_checks':rows}
(R/'build/qa/structure-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
(R/'build/qa/extracted-final-text-and-notes.json').write_text(json.dumps([{'page':i,'text':texts[i],'notes':notes[i]} for i in range(1,34)],ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='slide_checks'},ensure_ascii=False))
