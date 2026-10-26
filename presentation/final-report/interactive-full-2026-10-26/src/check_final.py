from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,hashlib,re
R=Path(__file__).resolve().parent.parent
f=R/'output/asset-management-llm-interactive-full.pptx'
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','m':'http://schemas.microsoft.com/office/powerpoint/2015/09/main'}
plan=json.loads((R/'src/state-manifest.json').read_text())
rows=[]
with ZipFile(f) as z:
 for d in plan['slides']:
  i=d['page'];x=E.fromstring(z.read(f'ppt/slides/slide{i}.xml'));ns=E.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml'))
  props=x.findall('.//p:cNvPr',N);names=[q.get('name') for q in props if q.get('name','').startswith('!!')];ids={q.get('id') for q in props}
  assert len(names)==len(set(names)),(i,'names')
  assert x.find('.//m:morph',N) is not None,(i,'morph')
  shape_text={q.find('.//p:cNvPr',N).get('name'):''.join(q.xpath('.//a:t/text()',namespaces=N)) for q in x.findall('.//p:sp',N)}
  for k in ('nav.front','nav.middle','nav.back','task.research','task.trade','task.client','task.review','task.risk','task.files','task.dev'):
   if i>=3:assert '!!'+k in names,(i,k)
  for q in x.findall('.//p:spTgt',N):assert q.get('spid') in ids,(i,'animation')
  assert len(''.join(ns.xpath('.//a:t/text()',namespaces=N)))>50,(i,'notes')
  if i in [15,16,17,18,24]:
   expected='产品A精选混合型基金' if i in [18,24] else '产品A精选'
   assert shape_text['!!clientDoc.value.product']==expected
   assert shape_text['!!clientDoc.value.view']=='甲公司收入增长来自销量提升，后续关注原材料成本'
  rows.append({'page':i,'title':shape_text.get('!!heading',shape_text.get('!!cover.title')),'native_shapes':len(props),'links':len(x.findall('.//a:hlinkClick',N)),'animated_shapes':len(x.findall('.//p:spTgt',N)),'notes':True})
assert len(rows)==33
report={'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'final_equals_candidate':f.read_bytes()==(R/'build/animated-candidate.pptx').read_bytes(),'slide_count':33,'links':sum(x['links'] for x in rows),'slide_checks':rows,'material_consistency':'pass','native_powerpoint_test':'root performs separately'}
(R/'build/qa/structure-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='slide_checks'},ensure_ascii=False))
