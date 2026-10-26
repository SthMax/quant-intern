from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from copy import deepcopy
from PIL import ImageFont
import json,hashlib,re,math
from english_copy import TITLES
R=Path(__file__).resolve().parent.parent;B=R/'build';(B/'qa').mkdir(parents=True,exist_ok=True)
SOURCE=R.parent/'color-revision-2026-10-26/output/asset-management-llm-story-colors.pptx'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='e0dd5d80c18d5f391968245f79d70941c87e8180faf44e86f3a123f31cfd4faa'
M=json.loads((R/'src/english-manifest.json').read_text());N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'};A=N['a'];P=N['p'];U=9525
with ZipFile(SOURCE) as z:entries=z.infolist();data={e.filename:z.read(e.filename) for e in entries}
fit=[];unfit=[];adjustments=[]
def pt(x):return x*75

def position(s,x=None,y=None,w=None,h=None):
 f=s.find('./p:spPr/a:xfrm',N)
 if f is None:f=s.find('./p:xfrm',N)
 if f is None:return
 o=f.find('./a:off',N);e=f.find('./a:ext',N)
 for k,v in [('x',x),('y',y)]:
  if v is not None:o.set(k,str(round(v*U)))
 for k,v in [('cx',w),('cy',h)]:
  if v is not None:e.set(k,str(round(v*U)))
def geometry(s):
 f=s.find('./p:spPr/a:xfrm',N)
 if f is None:f=s.find('./p:xfrm',N)
 o=f.find('./a:off',N);e=f.find('./a:ext',N)
 return [int(o.get('x'))/U,int(o.get('y'))/U,int(e.get('cx'))/U,int(e.get('cy'))/U]
def setsize(s,size):
 b=s.find('./p:txBody',N)
 if b is None:b=s
 for r in b.iter():
  if E.QName(r).localname in ['rPr','defRPr','endParaRPr']:r.set('sz',str(round(pt(size))))
def replacebody(body,value):
 ps=body.findall('./a:p',N)
 if not ps:return
 idx=body.index(ps[0]);templates=[deepcopy(x) for x in ps]
 for q in ps:body.remove(q)
 for j,line in enumerate(value.split('\n')):
  q=deepcopy(templates[min(j,len(templates)-1)]);runs=q.findall('./a:r',N)
  if runs:
   run=deepcopy(runs[0])
   for child in list(q):
    if E.QName(child).localname not in ['pPr','endParaRPr']:q.remove(child)
   ts=run.findall('./a:t',N)
   if ts:ts[0].text=line
   else:E.SubElement(run,f'{{{A}}}t').text=line
   for t in ts[1:]:run.remove(t)
   end=q.find('./a:endParaRPr',N);q.insert(q.index(end) if end is not None else len(q),run)
  else:
   for child in list(q):
    if E.QName(child).localname not in ['pPr','endParaRPr']:q.remove(child)
   run=E.SubElement(q,f'{{{A}}}r');E.SubElement(run,f'{{{A}}}t').text=line
  body.insert(idx+j,q)
def fonts(root):
 for x in root.iter():
  local=E.QName(x).localname
  if local in ['latin','ea','cs'] and 'typeface' in x.attrib:x.set('typeface','Arial')
  if 'lang' in x.attrib:x.set('lang','en-US')
  if 'altLang' in x.attrib:x.set('altLang','en-US')
def fobj(size,bold):return ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',round(size))
def estimate(s,size):
 body=s.find('./p:txBody',N);bp=body.find('./a:bodyPr',N);x,y,w,h=geometry(s)
 w-=sum(int(bp.get(k,'0'))/U for k in ['lIns','rIns']);h-=sum(int(bp.get(k,'0'))/U for k in ['tIns','bIns'])
 p=body.find('./a:p',N);r=p.find('.//a:rPr',N);bold=r is not None and r.get('b')=='1';font=fobj(size,bold)
 count=0;maxword=0
 for q in body.findall('./a:p',N):
  val=''.join(q.xpath('.//a:t/text()',namespaces=N));words=val.split();line='';n=1
  for word in words:
   maxword=max(maxword,font.getlength(word))
   if line and font.getlength(line+' '+word)>w: n+=1;line=word
   else:line=(line+' '+word).strip()
  count+=n
 return count*size*1.16,h,count,maxword,w

def layout(i,S):
 def at(n,**kw):position(S['!!'+n],**kw)
 def sz(n,v):setsize(S['!!'+n],v)
 # Use the full vertical space in centered buttons and bands.
 for s in S.values():
  bp=s.find('./p:txBody/a:bodyPr',N)
  if bp is not None and bp.get('anchor')=='ctr':bp.set('tIns','0');bp.set('bIns','0')
 # Header and navigation adaptation, without new controls.
 for n,s in S.items():
  if n.startswith('!!story.header.'):
   k=n.split('.')[2]
   if n.endswith('.bar'):position(s,x=(1105 if k=='issuer' else 1265) if i in [3,29,30] else 1120)
   elif n.endswith('.name'):position(s,x=(1119 if k=='issuer' else 1279) if i in [3,29,30] else 1134,w=(133 if k=='issuer' else 173) if i in [3,29,30] else 160);setsize(s,22 if i in [3,29,30] else 24)
   elif n.endswith('.qualifier'):position(s,x=1305,w=147);setsize(s,20)
 if '!!example' in S:at('example',x=1460,w=72);sz('example',18)
 if i==33:
  sz('nav.next',21);bp=S['!!nav.next'].find('./p:txBody/a:bodyPr',N);bp.set('lIns',str(6*U));bp.set('rIns',str(6*U))
 if i==3:sz('map.route.title',27);at('map.route.title',h=70)
 # English role headers and short line labels.
 for n,s in S.items():
  if n.endswith('.role'):setsize(s,24)
  if n.endswith('.body') and n.startswith('!!comment.'):
   x,y,w,h=geometry(s);position(s,y=y-9,h=h+9);setsize(s,22)
 # Two versions of the same document retain matching IDs and field locations.
 if i in [15,18]:
  coords={'product':(341,373,47),'period':(417,449,35),'view':(493,525,112),'risk':(651,683,66)}
  for key,(ly,vy,vh) in coords.items():
   at('clientDoc.label.'+key,y=ly,h=28);at('clientDoc.value.'+key,y=vy,h=vh)
   at('clientDoc.highlight.'+key,y=ly-6,h=vy+vh-ly+5)
  if i==18:
   replacebody(S['!!clientDoc.value.view'].find('./p:txBody',N),'Company A’s volume growth reflects\nchannel restocking. Monitor whether\nrestocking continues and track\nraw-material costs.')
 if i in [16,17]:
  at('clientDoc.label.view',h=57)
  replacebody(S['!!clientDoc.label.period'].find('./p:txBody',N),'Source\nversion');at('clientDoc.label.period',h=57)
  replacebody(S['!!clientDoc.label.risk'].find('./p:txBody',N),'Risk\ndisclosure');at('clientDoc.label.risk',h=57)
 # A wider quote-record panel keeps both provenance and the quoted amounts readable.
 if i==11:
  at('trade.intent',h=80)
  specs={'trade.llm.query':(426,320),'trade.system':(786,340),'trade.llm.quote':(1166,366)}
  for base,(x,w) in specs.items():
   at(base,x=x,w=w);at(base+'.role',x=x+20,w=w-40);at(base+'.body',x=x+20,w=w-40)
  replacebody(S['!!trade.llm.query.role'].find('./p:txBody',N),'LLM parses the request')
  replacebody(S['!!trade.llm.quote.body'].find('./p:txBody',N),'The trader provides this quote:\nBond A: clean price 100.20\nRMB 20m face value available\nExtract bond, price, face value')
  sz('trade.llm.quote.body',23)
  at('trade.query.call.line',x=755,w=21);at('trade.query.call.tip',x=770)
  for base,c in [('trade.quote.merge',956),('trade.chat.merge',1349)]:at(base+'.line',x=c);at(base+'.tip',x=c-6)
  at('story.issuer.holdings.data',x=796);at('story.issuer.quote.record',x=1176)
 if i==4:
  at('research.evidence.2.text',h=94);at('research.evidence.3.text',h=94)
 if i==5:
  at('driver.tools',x=1380,w=152)
  bp=S['!!driver.tools'].find('./p:txBody/a:bodyPr',N)
  bp.set('lIns',str(8*U));bp.set('rIns',str(8*U))
 if i==8:
  sz('research.evidence.1.label',21);at('research.evidence.2.text',h=34);at('research.evidence.3.text',h=62);at('story.issuer.source.group',h=310)
 if i==9:sz('trade.intent.role',22);sz('trade.compare.role',22)
 if i==10:
  for n in S:
   if n.endswith('.role'):setsize(S[n],22)
 if i==15:
  at('client.user',w=1106,h=36);sz('client.user',23)
  replacebody(S['!!client.llm.body'].find('./p:txBody',N),'Select the views\nDraft the update\nfor client use');sz('client.llm.body',23)
 if i==18:
  at('review.inputs',h=145);at('review.inputs.body',y=303,h=82);sz('review.inputs.body',23)
  at('review.tool',y=406);at('review.tool.role',y=421);at('review.tool.body',y=467)
 if i==19:
  for j in range(3):at(f'risk.question.{j}',h=175);at(f'risk.question.{j}.body',h=102)
 if i==21:
  at('risk.evidence.mail.text',h=86);at('story.issuer.event.mail',h=145)
  at('risk.evidence.system',h=150)
  at('risk.evidence.system.body',y=464,h=94);at('story.issuer.holdings.data',y=467,h=88)
 if i==17:
  replacebody(S['!!comment.view.body'].find('./p:txBody',N),'Restocking drove growth.\nAdd the driver and uncertainty\nover its duration.')
  replacebody(S['!!comment.risk.body'].find('./p:txBody',N),'Specify NAV volatility\nand the risk of capital loss.')
 if i==23:
  # Highlight the same business additions in the English wording.
  font=fobj(26,False)
  at('ops.compare.mark.driver',x=822+font.getlength('Company A’s volume growth reflects '),w=font.getlength('channel restocking')+3)
  at('ops.compare.mark.watch',x=822+font.getlength('Monitor whether '),w=font.getlength('restocking continues')+3)
  replacebody(S['!!ops.compare.new.line2'].find('./p:txBody',N),'Monitor whether restocking continues\nand track raw-material costs.')
  # The long English second line needs two lines; move it slightly up and allocate space.
  at('ops.compare.new.line2',y=677,h=62);at('ops.compare.mark.watch',y=677)
  at('story.client.version.v2',h=138)
  sz('ops.compare.new.line1',24);sz('ops.compare.new.line2',24)
  font=fobj(24,False)
  at('ops.compare.mark.driver',x=822+font.getlength('Company A’s volume growth reflects '),w=font.getlength('channel restocking')+3,h=31)
  at('ops.compare.mark.watch',x=822+font.getlength('Monitor whether '),w=font.getlength('restocking continues')+3,h=31)
 if i==24:
  at('changeLog.title',w=474);sz('changeLog.title',29)
 if i==27:
  # Keep the input file marker next to its English label.
  at('story.client.development.sample',h=32)
 if i==28:
  for j in range(3):
   at(f'other.{j}.company',x=730,w=802)
   at(f'other.{j}.title',w=280);sz(f'other.{j}.title',30)
 if i==31:
  at('arch.data',h=61);sz('arch.data',25)
  at('arch.model',h=175);at('arch.tools',h=175)
  at('arch.model.body',h=100)
 if i==32:
  for j in range(3):at(f'phase.{j}.roles',w=334,h=70);at(f'phase.{j}.outputs',w=632,h=78)
for d in M['slides']:
 i=d['page'];part=f'ppt/slides/slide{i}.xml';x=E.fromstring(data[part]);S={s.find('./p:nvSpPr/p:cNvPr',N).get('name'):s for s in x.findall('.//p:sp',N)}
 for e in d['shapes']:replacebody(S[e['name']].find('./p:txBody',N),e['english'])
 fonts(x);layout(i,S)
 if i==11:
  table=x.find('.//a:tbl',N)
  for rr,row in enumerate(table.findall('./a:tr',N)):
   row.set('h',str((80 if rr==0 else 46)*U))
   for cc,cell in enumerate(row.findall('./a:tc',N)):
    replacebody(cell.find('./a:txBody',N),d['table'][rr][cc]);setsize(cell,22 if rr==0 else 23)
    pr=cell.find('./a:tcPr',N)
    pr.set('marT',str(6*U));pr.set('marB',str(6*U))
  fonts(table)
 # Keep all targets intact; only localize tooltip text.
 for h in x.findall('.//a:hlinkClick',N):
  old=h.get('tooltip','');m=re.search(r'(\d+)',old)
  if m:h.set('tooltip',f'Slide {m.group(1)}: {TITLES[int(m.group(1))]}')
 for nv in x.findall('.//p:cNvPr',N):
  if nv.get('descr') and re.search('[\u4e00-\u9fff]',nv.get('descr')):nv.set('descr','Illustrative asset management research workspace')
 for name,s in S.items():
  body=s.find('./p:txBody',N)
  if body is None or not ''.join(tx for tx in s.xpath('./p:txBody//a:t/text()',namespaces=N)):continue
  props=body.find('.//a:rPr',N)
  if props is None:props=body.find('.//a:defRPr',N)
  if props is None:continue
  orig=float(props.get('sz','1800'))/75;size=orig
  if name=='!!heading':minimum=38
  elif name.startswith('!!story.header.') or name in ['!!source','!!page','!!example']:minimum=min(orig,18)
  elif name.startswith('!!nav.') or name.startswith('!!task.'):minimum=min(orig,21)
  else:minimum=min(orig,23)
  while True:
   need,avail,lines,mw,width=estimate(s,size)
   if need<=avail+1 and mw<=width+1:break
   if size-0.5<minimum:break
   size-=0.5
  if size!=orig:setsize(s,size);fit.append({'page':i,'name':name,'from':orig,'to':size,'lines':lines})
  if need>avail+1 or mw>width+1:unfit.append({'page':i,'name':name,'size':size,'lines':lines,'needed':round(need,1),'available':round(avail,1),'width':round(width,1),'text':' / '.join(s.xpath('./p:txBody//a:t/text()',namespaces=N))})
 data[part]=E.tostring(x,xml_declaration=True,encoding='UTF-8',standalone=True)
 note=E.fromstring(data[f'ppt/notesSlides/notesSlide{i}.xml'])
 for s in note.findall('.//p:sp',N):
  ph=s.find('./p:nvSpPr/p:nvPr/p:ph',N)
  if ph is not None and ph.get('type')=='body':replacebody(s.find('./p:txBody',N),d['notes'])
 fonts(note);data[f'ppt/notesSlides/notesSlide{i}.xml']=E.tostring(note,xml_declaration=True,encoding='UTF-8',standalone=True)
for name in list(data):
 if re.fullmatch(r'ppt/theme/theme\d+\.xml',name):
  x=E.fromstring(data[name]);fonts(x);data[name]=E.tostring(x,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(B/'candidate.pptx','w') as z:
 for e in entries:z.writestr(e,data[e.filename])
(B/'qa/fit-adjustments.json').write_text(json.dumps({'font':'Arial','adjustments':fit,'needs_review':unfit},ensure_ascii=False,indent=2))
print(json.dumps({'slides':33,'font_adjustments':len(fit),'needs_review':len(unfit),'candidate_sha256':hashlib.sha256((B/'candidate.pptx').read_bytes()).hexdigest()}))
