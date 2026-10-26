from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from copy import deepcopy
import json,hashlib
R=Path(__file__).resolve().parent.parent
plan=json.loads((R/'src/color-map.json').read_text());source=(R/plan['source']).resolve()
assert hashlib.sha256(source.read_bytes()).hexdigest()==plan['source_sha256']
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
A=N['a'];P=N['p'];C=plan['colors']
with ZipFile(source) as z:entries=z.infolist();original={e.filename:z.read(e.filename) for e in entries}
with ZipFile(R/'build/overlays.pptx') as z:overlays={i:E.fromstring(z.read(f'ppt/slides/slide{i}.xml')) for i in range(1,34)}
content=dict(original);audit=[];appearance=[]
def fill(shape,color):
 props=shape.find('./p:spPr',N)
 for n in list(props):
  if E.QName(n).localname in ['solidFill','noFill','gradFill','blipFill','pattFill','grpFill']:props.remove(n)
 f=E.Element(f'{{{A}}}solidFill');E.SubElement(f,f'{{{A}}}srgbClr',val=color)
 # DrawingML fill follows geometry and precedes line/effects.
 pos=next((i for i,n in enumerate(props) if E.QName(n).localname in ['ln','effectLst','effectDag','scene3d','sp3d','extLst']),len(props));props.insert(pos,f)
def text(shape,color,paragraph=None):
 body=shape.find('./p:txBody',N)
 if body is None:return
 if paragraph is None:target=body
 else:target=body.findall('./a:p',N)[paragraph]
 for v in target.findall('.//a:solidFill/a:srgbClr',N):v.set('val',color)
def line(shape,color):
 props=shape.find('./p:spPr',N);ln=props.find('./a:ln',N)
 if ln is None:ln=E.SubElement(props,f'{{{A}}}ln',w='9525')
 if int(ln.get('w','0'))==0:ln.set('w','9525')
 for n in list(ln):
  if E.QName(n).localname in ['solidFill','noFill','gradFill','pattFill']:ln.remove(n)
 f=E.Element(f'{{{A}}}solidFill');E.SubElement(f,f'{{{A}}}srgbClr',val=color);ln.insert(0,f)
for d in plan['slides']:
 i=d['page'];part=f'ppt/slides/slide{i}.xml';slide=E.fromstring(original[part]);tree=slide.find('./p:cSld/p:spTree',N);shapes=slide.findall('.//p:sp',N)
 byname={s.find('./p:nvSpPr/p:cNvPr',N).get('name'):s for s in shapes};changed=set()
 for root in d['neutral_roots']:
  prefix='!!'+root;matched=[(n,s) for n,s in byname.items() if n==prefix or n.startswith(prefix+'.')]
  assert matched,(i,'missing neutral root',root)
  for n,s in matched:
   geom=s.find('./p:spPr/a:prstGeom',N)
   if s.find('./p:spPr/a:solidFill',N) is not None and geom is not None and geom.get('prst')=='rect':fill(s,C['neutral'])
   text(s,C['ink']);changed.add(n)
 for n in d['text_neutral']:
  s=byname['!!'+n];text(s,C['ink']);changed.add('!!'+n)
 for rule in d['styles']:
  s=byname[rule['name']]
  if 'fill' in rule:fill(s,rule['fill'])
  if 'text' in rule:text(s,rule['text'],rule.get('paragraph'))
  if 'line' in rule:line(s,rule['line'])
  changed.add(rule['name'])
 maxid=max(int(x.get('id')) for x in slide.findall('.//p:cNvPr',N))
 new=[];new_ids={}
 for s in overlays[i].find('./p:cSld/p:spTree',N):
  if E.QName(s).localname not in ['sp','cxnSp']:continue
  clone=deepcopy(s);nv=clone.find('.//p:cNvPr',N);name=nv.get('name');assert name.startswith('!!story.') and name not in byname,(i,name)
  maxid+=1;nv.set('id',str(maxid));tree.append(clone);new.append(name);new_ids[name]=str(maxid)
 # Add matching entrance effects for new body markers. Existing effects remain in place.
 timing=slide.find('./p:timing',N)
 source_ids={q.get('name'):q.get('id') for q in slide.findall('.//p:cNvPr',N)}
 timer=max([int(q.get('id')) for q in timing.findall('.//p:cTn',N)] or [0]) if timing is not None else 0
 for o in d['overlays']:
  owner=o['appear_with'];assert owner in source_ids,(i,owner)
  ownerid=source_ids[owner];target=None
  if timing is not None:
   target=next((t for t in timing.findall('.//p:spTgt',N) if t.get('spid')==ownerid),None)
  if target is None:
   appearance.append({'page':i,'marker':o['name'],'owner':owner,'delay_ms':None,'mode':'static with static source object'});continue
  effect=target
  while effect is not None and effect.tag!=f'{{{P}}}par':effect=effect.getparent()
  assert effect is not None
  clone=deepcopy(effect)
  for ct in clone.findall('.//p:cTn',N):timer+=1;ct.set('id',str(timer))
  for sp in clone.findall('.//p:spTgt',N):assert sp.get('spid')==ownerid;sp.set('spid',new_ids[o['name']])
  effect.getparent().append(clone)
  builds=timing.find('./p:bldLst',N)
  sourcebuild=next((b for b in builds if b.get('spid')==ownerid),None) if builds is not None else None
  if sourcebuild is not None:
   cb=deepcopy(sourcebuild);cb.set('spid',new_ids[o['name']]);builds.append(cb)
  cond=effect.find('./p:cTn/p:stCondLst/p:cond',N);delay=int(cond.get('delay','0'))
  appearance.append({'page':i,'marker':o['name'],'owner':owner,'delay_ms':delay,'mode':'same entrance time as source object'})
 names=[x.get('name') for x in slide.findall('.//p:cNvPr',N) if x.get('name','').startswith('!!')];assert len(names)==len(set(names)),i
 if changed or new:content[part]=E.tostring(slide,xml_declaration=True,encoding='UTF-8',standalone=True)
 audit.append({'page':i,'neutral_roots':d['neutral_roots'],'restyled_shapes':sorted(changed),'added_story_shapes':new})
with ZipFile(R/'build/candidate.pptx','w') as z:
 for e in entries:z.writestr(e,content[e.filename])
(R/'build/qa/appearance-bindings.json').write_text(json.dumps(appearance,ensure_ascii=False,indent=2))
(R/'build/qa/color-application.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
print(json.dumps({'pages':33,'restyled_shapes':sum(len(x['restyled_shapes']) for x in audit),'new_story_shapes':sum(len(x['added_story_shapes']) for x in audit),'candidate_sha256':hashlib.sha256((R/'build/candidate.pptx').read_bytes()).hexdigest()}))
