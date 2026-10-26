from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,hashlib,re,sys
R=Path(__file__).resolve().parent.parent
plan=json.loads((R/'src/color-map.json').read_text());source=(R/plan['source']).resolve();final=R/'output/asset-management-llm-story-colors.pptx'
if not final.exists():final=R/'build/candidate.pptx'
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','m':'http://schemas.microsoft.com/office/powerpoint/2015/09/main'}
def canon(x):return E.tostring(x,method='c14n')
def namemap(x):return {s.find('./p:nvSpPr/p:cNvPr',N).get('name'):s for s in x.findall('.//p:sp',N)}
def tx(x):return x.xpath('.//a:t/text()',namespaces=N)
rows=[];all_added=[];colors=[];links=0
with ZipFile(source) as a,ZipFile(final) as b:
 assert a.namelist()==b.namelist()
 changed=[p for p in a.namelist() if a.read(p)!=b.read(p)]
 assert all(re.fullmatch(r'ppt/slides/slide\d+\.xml',p) for p in changed),changed
 for i in range(1,34):
  part=f'ppt/slides/slide{i}.xml';x=E.fromstring(a.read(part));y=E.fromstring(b.read(part));old=namemap(x);new=namemap(y);d=plan['slides'][i-1]
  assert set(old)<=set(new)
  added=set(new)-set(old);assert all(n.startswith('!!story.') for n in added)
  for name,s in old.items():
   assert tx(s)==tx(new[name]),(i,name,'text changed')
   assert canon(s.find('./p:spPr/a:xfrm',N))==canon(new[name].find('./p:spPr/a:xfrm',N)),(i,name,'geometry changed')
   assert canon(s.find('./p:nvSpPr',N))==canon(new[name].find('./p:nvSpPr',N)),(i,name,'identity/link changed')
   if name.startswith(('!!nav.','!!map.','!!task.','!!heading','!!subtitle','!!page','!!example','!!footer','!!source')):assert canon(s)==canon(new[name]),(i,name,'navigation/head changed')
  # Remove only added marker effects before comparing the original timing tree.
  oldtim=x.find('./p:timing',N);newtim=y.find('./p:timing',N)
  if oldtim is not None:
   from copy import deepcopy
   reduced=deepcopy(newtim);newids={new[n].find('./p:nvSpPr/p:cNvPr',N).get('id') for n in added}
   for par in list(reduced.findall('.//p:par',N)):
    ids={t.get('spid') for t in par.findall('.//p:spTgt',N)}
    if ids and ids<=newids:par.getparent().remove(par)
   builds=reduced.find('./p:bldLst',N)
   if builds is not None:
    for child in list(builds):
     if child.get('spid') in newids:builds.remove(child)
   assert canon(oldtim)==canon(reduced),(i,'original animation changed')
  else:assert newtim is None,(i,'unexpected new animation')
  for expr in ['.//m:morph','.//a:hlinkClick','.//p:graphicFrame']:
   assert [canon(t) for t in x.findall(expr,N)]==[canon(t) for t in y.findall(expr,N)],(i,expr)
  assert a.read(f'ppt/notesSlides/notesSlide{i}.xml')==b.read(f'ppt/notesSlides/notesSlide{i}.xml')
  names=[n.get('name') for n in y.findall('.//p:cNvPr',N) if n.get('name','').startswith('!!')];assert len(names)==len(set(names)),i
  for root in d['neutral_roots']:
   prefix='!!'+root
   for name,s in new.items():
    if name==prefix or name.startswith(prefix+'.'):
     geom=s.find('./p:spPr/a:prstGeom',N);v=s.find('./p:spPr/a:solidFill/a:srgbClr',N)
     if geom is not None and geom.get('prst')=='rect' and v is not None:assert v.get('val') in ['F3F7FA','FFFFFF'],(i,name,v.get('val'))
     # Identity text inside a mixed sample box is an explicit object exception.
     if not (i==27 and name=='!!dev.samples.body'):
      assert not set(s.xpath('./p:txBody//a:srgbClr/@val',namespaces=N))&{'317F7B','7363A6'},(i,name,'role has story color')
  assert not set(y.xpath('.//a:srgbClr/@val',namespaces=N))&{'DCEFEA','E8E3F2'},(i,'old ambiguous tint')
  for name,s in new.items():
   cc=set(s.xpath('.//a:srgbClr/@val',namespaces=N))&{'317F7B','7363A6','EFF6F4','F3F0F8'}
   if cc:colors.append({'page':i,'object':name,'colors':sorted(cc)})
  links+=len(y.findall('.//a:hlinkClick',N));all_added+=list(added)
  rows.append({'page':i,'original_texts_preserved':True,'notes_identical':True,'navigation_and_stage_identical':True,'original_animation_identical_after_excluding_new_marker_targets':True,'new_story_shapes':len(added)})
 assert 'LLM解析询价记录' in '\n'.join(tx(E.fromstring(b.read('ppt/slides/slide11.xml'))))
 assert '交易员提供收到的报价' in '\n'.join(tx(E.fromstring(b.read('ppt/slides/slide11.xml'))))
assert links==407
report={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'final_sha256':hashlib.sha256(final.read_bytes()).hexdigest(),'slides':33,'internal_links':links,'new_story_shapes':len(all_added),'original_business_text_geometry_tables_and_notes_preserved':True,'navigation_progress_modified':False,'original_animation_order_and_targets_preserved':True,'old_ambiguous_teal_and_lavender_tints_remaining':False,'slide_checks':rows,'story_color_objects':colors}
(R/'build/qa/color-and-content-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['slide_checks','story_color_objects']},ensure_ascii=False))
