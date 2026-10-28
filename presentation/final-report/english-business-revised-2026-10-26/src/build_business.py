from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from copy import deepcopy
from PIL import ImageFont
import json,hashlib,re,math
R=Path(__file__).resolve().parent.parent; B=R/'build'; (B/'qa').mkdir(parents=True,exist_ok=True)
SOURCE=R.parent/'english-2026-10-26/output/asset-management-llm-interactive-en.pptx'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='86822d1bb55cf9ac3d5a0b4894705be6b68966d44c6851ca7d16501a6bae146d'
M=json.loads((R/'src/business-manifest.json').read_text())
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}; A=N['a']; P=N['p']; U=9525
with ZipFile(SOURCE) as z: entries=z.infolist();data={e.filename:z.read(e.filename) for e in entries}
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


def layout(i,S,x):
 def at(n,**kw):position(S['!!'+n],**kw)
 def txt(n,v):replacebody(S['!!'+n].find('./p:txBody',N),v)
 def add(n,text,src,xp,yp,w,h,size=23):
  s=deepcopy(S['!!'+src]); nv=s.find('./p:nvSpPr/p:cNvPr',N);nv.set('id',str(9000+len(added)));nv.set('name','!!business.'+n)
  for a in nv.findall('./a:hlinkClick',N):nv.remove(a)
  replacebody(s.find('./p:txBody',N),text);position(s,x=xp,y=yp,w=w,h=h);setsize(s,size)
  s.find('./p:txBody/a:bodyPr',N).set('anchor','t')
  x.find('./p:cSld/p:spTree',N).append(s);S['!!business.'+n]=s
  sourceid=S['!!'+src].find('./p:nvSpPr/p:cNvPr',N).get('id')
  matches=x.xpath('.//p:par[p:cTn/p:childTnLst/p:set/p:cBhvr/p:tgtEl/p:spTgt[@spid="'+sourceid+'"]]',namespaces=N)
  if matches:
   par=deepcopy(matches[0]); start=max(int(e.get('id')) for e in x.findall('.//p:cTn',N))+1
   for j,e in enumerate(par.findall('.//p:cTn',N)):e.set('id',str(start+j))
   par.find('.//p:spTgt',N).set('spid',nv.get('id'));matches[0].getparent().append(par)
  added.append({'slide':i,'id':nv.get('id'),'name':nv.get('name'),'appearance_source_id':sourceid,'appearance_bound':bool(matches)})
 # The longer full breadcrumbs stop before the running-example labels.
 if '!!subtitle' in S:at('subtitle',w=1032)
 if '!!heading' in S:
  need,avail,lines,mw,w=estimate(S['!!heading'],44)
  if lines>1:at('heading',y=21,h=103)
 for n,s in S.items():
  if n.endswith('.qualifier'):position(s,x=1305,w=150,h=51,y=119)
 if i in [3,29]:
  for n,s in S.items():
   if n.endswith('.outcome'):position(s,h=62)
  if i==3:
   at('map.route2.text',h=60)
  else:
   for task,y in [('trade',435),('client',559),('risk',435),('dev',435)]:
    at('task.'+task,y=y);at('task.'+task+'.outcome',y=y+59)
   for name in ['front','middle','back']:at('map.'+name,h=472)
   at('recommend.body',y=712,h=70)
 if i==4:
  at('research.evidence.1.text',h=78);at('research.evidence.3.text',h=116)
 if i==5:at('driver.llm.title',h=76);at('driver.result',y=711,h=72)
 if i==7:at('elements.stat',h=80,y=661);at('elements.user',y=749,h=40)
 if i==8:
  # A larger evidence column and output band keep complete financial and analytical prose legible.
  at('research.evidence.1.text',h=70)
  for k,y in [('rule',440),('label',450),('text',486)]:at('research.evidence.2.'+k,y=y)
  for k,y in [('rule',526),('label',536),('text',572)]:at('research.evidence.3.'+k,y=y)
  at('research.evidence.3.text',h=85);at('story.issuer.source.group',h=347)
  for k in ['research.llm','research.tool']:at(k,h=327)
  at('research.material.in1',y=470);at('research.material.in2',y=595);at('research.material.bus',h=227)
  at('research.toResult.line',y=643,h=12);at('research.toResult.tip',y=649)
  at('research.result',y=663,h=111);at('story.issuer.analysis',y=663,h=111)
  at('research.result.title',x=446,y=673,w=203,h=90);at('research.result.text',x=677,y=670,w=840,h=100)
  at('research.user',y=777,h=34);setsize(S['!!research.user'],23)
 if i==9:
  for base in ['trade.intent','trade.query','trade.inquire','trade.compare']:
   gx,gy,gw,gh=geometry(S['!!'+base]);at(base,h=340);at(base+'.role',h=70);at(base+'.body',y=gy+88,h=244)
  at('trade.system.role',h=65)
 if i==10:
  for n in S:
   if n.endswith('.body') and n.startswith('!!trade.case'):
    xx,yy,ww,hh=geometry(S[n]);position(S[n],h=hh+35)
 if i==11:
  for base in ['trade.llm.query','trade.system','trade.llm.quote']:
   at(base,y=310,h=226);at(base+'.role',y=320,h=61);at(base+'.body',y=386,h=143)
  at('trade.result.title',w=750,h=41,y=548)
  at('trade.user',y=739,h=58);setsize(S['!!trade.user'],24)
  at('story.issuer.holdings.data',y=388,h=128)
  at('story.issuer.quote.record',y=418,h=86)
 if i==12:at('client.material0',h=110)
 if i==13:at('client.views.head',h=80);at('client.views.result.text',h=85)
 if i==14:
  at('tender.llm.role',h=66);xx,yy,ww,hh=geometry(S['!!tender.llm.body']);at('tender.llm.body',y=yy+25,h=hh-25)
  at('tender.answer.body',h=200)
 if i in [15,16,17,18]:
  if i in [16,17]:
   at('clientDoc.label.view',w=140,h=70)
   at('clientDoc.value.view',h=99)
  if i==15:
   at('client.input.manager',h=95);at('client.input.product',h=95)
 if i==16:at('review.reference.label',h=65)
 if i==17:
  txt('review.case','Penghua suggests edits based on review rules.\nYingmi supports initial checks, revision and repeat review.')
  at('review.case',y=746,h=56);setsize(S['!!review.case'],23)
  add('review.umbrella','LLM-assisted review','comment.meta.role',1174,243,358,34,25)
  at('comment.view.body',h=112);at('comment.view',h=164)
  at('comment.risk',y=625,h=115);at('comment.risk.role',y=633);at('comment.risk.body',y=670,h=65)
  # Concise equivalent keeps the full meaning in the bounded comment panel.
  txt('comment.view.body','Identify channel restocking as the sales volume driver. Retain uncertainty over its continuation.')
 if i==18:
  # Widen the final document and allocate five lines to the client investment view.
  for n,s in S.items():
   if n.startswith('!!clientDoc'):
    xx,yy,ww,hh=geometry(s);position(s,x=xx-26,w=ww+26)
  at('story.client.document',x=976)
  at('clientDoc.value.view',h=130);at('clientDoc.highlight.view',h=168)
  at('clientDoc.label.risk',y=668);at('clientDoc.value.risk',y=698,h=49);at('clientDoc.highlight.risk',y=662,h=86)
  at('review.inputs.body',h=114);at('review.inputs',h=170)
  at('review.tool',y=426,h=134);at('review.tool.role',y=437,h=60);at('review.tool.body',y=500,h=54)
  at('review.llm',y=573,h=170);at('review.llm.role',y=583,h=60);at('review.llm.body',y=647,h=90);setsize(S['!!review.llm.body'],23)
  at('review.toRevision.line',x=954,w=17);at('review.toRevision.tip',x=965)
  at('review.user',y=759,h=38);setsize(S['!!review.user'],23)
 if i==19:
  for j in [0,1]:at(f'risk.question.{j}.body',h=125);at(f'risk.question.{j}',h=198)
 if i==20:
  at('risk.rules.tool.role',h=62);xx,yy,ww,hh=geometry(S['!!risk.rules.tool.body']);at('risk.rules.tool.body',y=yy+30,h=hh)
  at('risk.rules.explain',h=76)
 if i==21:
  at('risk.result.body',h=302);at('risk.user',h=60,y=740);setsize(S['!!risk.user'],24)
 if i==23:
  at('ops.form',h=246);at('ops.form.body',h=179)
  at('ops.stat',y=587,h=168);setsize(S['!!ops.stat'],25)
  at('ops.compare.old.label',y=450);at('ops.compare.old.text',y=494,h=66);at('story.client.version.v1',y=450,h=110)
  at('ops.compare.new.label',y=574,h=36)
  txt('ops.compare.new.line1','Channel restocking supported Company A’s\nsales volume growth.')
  txt('ops.compare.new.line2','We are monitoring whether restocking continues,\nalongside raw-material costs.')
  at('ops.compare.new.line1',y=616,h=58);at('ops.compare.new.line2',y=679,h=58)
  at('story.client.version.v2',y=574,h=163)
  font=fobj(24,False)
  at('ops.compare.mark.driver',x=822,y=616,w=font.getlength('Channel restocking')+2,h=29)
  at('ops.compare.mark.watch',x=822+font.getlength('We are monitoring '),y=679,w=font.getlength('whether restocking continues')+2,h=29)
 if i==24:
  at('ops.tool.role',h=52);at('ops.tool.body',y=444,h=65);at('ops.tool',h=131)
  at('changeLog.title',h=70);at('changeLog.object',y=337);at('changeLog.rule',y=380)
  at('changeLog.driver.label',y=391);at('changeLog.watch.body',h=74)
 if i==25:at('dev.request',h=95,y=210)
 if i==26:at('dev.case2',h=78);at('dev.case.result',h=72)
 if i==27:
  for base in ['dev.samples','dev.generate','dev.test','dev.feedback','dev.revise','dev.deliver']:
   xx,yy,ww,hh=geometry(S['!!'+base]);at(base+'.role',h=65);at(base+'.body',y=yy+83,h=hh-90)
 if i==28:
  for j in range(3):at(f'other.{j}.flow.1',h=105)
 if i==32:
  for j in range(3):
   txt(f'phase.{j}.title', ' '.join(S[f'!!phase.{j}.title'].xpath('./p:txBody//a:t/text()',namespaces=N)))
  add('phase.teams','Participating teams','phase.0.roles',521,286,334,27,20)
  add('phase.outputs','Deliverables','phase.0.roles',900,286,632,27,20)
  at('phase.0.roles',y=320,h=60);at('phase.0.outputs',y=320,h=60);at('phase.0.rule',y=389)
 if i==33:at('evaluation.0.body',h=96)


 # Final reflow pass: keep the established type sizes and give content sufficient room.
 if i==2:
  at('scope.output1',h=80)
  txt('scope.work2','Query systems and run tasks');txt('scope.work3','Draft documents and code')
 if i==4:
  txt('research.evidence.1.text','Revenue (RMB m): 100 / 110\nSales volume (m units): 1.0 / 1.1');at('research.evidence.1.text',h=88)
 if i==7:at('element.0.label',h=58)
 if i==8:
  at('research.evidence.1.text',h=78)
  txt('research.evidence.1.text','Revenue (RMB m): 100 / 110\nSales volume (m units):\n1.0 / 1.1')
  for k,y in [('rule',439),('label',445),('text',478)]:at('research.evidence.2.'+k,y=y)
  for k,y in [('rule',513),('label',519),('text',552)]:at('research.evidence.3.'+k,y=y)
  at('research.evidence.3.text',h=110)
  txt('research.result.text','Sales volume drove revenue growth [1]. Restocking supported shipments [2], but research views differ on the sustainability of growth [3]. Monitor demand and input costs.')
 if i==9:
  txt('trade.intent.body','Portfolio manager\nCompany A bonds\nMaturing within two years\nCheck holdings\nCollect offer quotes')
  txt('trade.inquire.body','Trader\nSpecify bonds and buying interest\nRequest offer prices and available size\nReceive quotes')
  for base in ['trade.intent','trade.query','trade.inquire','trade.compare']:
   at(base,y=298,h=308);at(base+'.role',y=311,h=85);at(base+'.body',y=402,h=196)
  for base in ['trade.system','trade.counterparty']:
   at(base,y=665,h=78);at(base+'.role',y=670,h=30);at(base+'.body',y=710,h=30)
  txt('trade.system.role','Market / holdings systems')
  for n,shape in S.items():
   if any(k in n for k in ['trade.query.down','trade.query.up','trade.rfq','trade.quote.return']):
    pass
  at('trade.ask.label',x=1003,y=615,w=120,h=45)
  at('trade.data.label',y=622);at('trade.quote.label',y=622)
  at('story.issuer.request',y=402,h=60) if '!!story.issuer.request' in S else None
 if i==10:
  for n in S:
   if n.startswith('!!trade.case') and n.endswith('.body'):
    xx,yy,ww,hh=geometry(S[n]);position(S[n],h=hh+10)
 if i==14:
  at('tender.llm',h=270);at('tender.answer',h=270)
  at('tender.user',h=65);at('tender.case',h=62)
 if i==15:at('client.input.manager',y=445,h=120)
 if i==16:at('review.questions',h=128)
 if i==17:
  at('comment.risk',y=615,h=131);at('comment.risk.role',y=624);at('comment.risk.body',y=661,h=82)
 if i==18:
  txt('review.llm.body','Add the sales volume driver: channel restocking\nRetain uncertainty over continued restocking\nUse the product’s specific risk wording')
  at('review.llm.body',y=642,h=104)
  at('clientDoc.value.risk',y=694,h=55)
 if i==20:
  at('risk.event.llm.body',h=100);xx,yy,ww,hh=geometry(S['!!risk.event.llm']);at('risk.event.llm',h=hh+30)
 if i==21:
  txt('risk.evidence.mail.text','Company A: credit rating on watch.\nOperating cash flow is under pressure.')
  at('risk.evidence.mail.text',h=116);at('story.issuer.event.mail',h=170)
 if i==25:at('dev.request',h=103)
 if i==27:
  for base in ['dev.samples','dev.generate','dev.test']:
   at(base,y=310,h=200);at(base+'.role',y=323,h=64);at(base+'.body',y=390,h=112)
  for base in ['dev.feedback','dev.revise','dev.deliver']:
   at(base,y=568,h=198);at(base+'.role',y=581,h=62);at(base+'.body',y=645,h=114)
  at('story.client.development.sample',y=390)
  for n in ['dev.samples.body','dev.generate.body','dev.test.body','dev.feedback.body','dev.revise.body','dev.deliver.body']:
   value='\n'.join(S['!!'+n].xpath('./p:txBody//a:t/text()',namespaces=N)).rstrip('.')
   txt(n,value)
 if i==28:
  at('other.0.title',w=650);at('other.0.company',x=950,w=582)
  for j in range(3):
   for k in range(3):at(f'other.{j}.flow.{k}',h=116)
 if i==31:
  at('arch.model.role',h=60);at('arch.model.body',y=580,h=91)
  at('arch.model',h=192);at('arch.tools',h=192);at('arch.tools.body',h=102)
  at('arch.data',y=692);at('arch.models',y=760)
 if i==32:at('phase.0.outputs',h=67)
 if i==9:
  at('trade.system',y=653,h=90);at('trade.system.role',y=657,h=56);at('trade.system.body',y=714,h=27)
  txt('trade.system.role','Market and\nholdings systems')
  at('trade.ask.label',h=50,x=972,w=112)
  at('trade.data.line',y=614,h=31);at('trade.data.tip',y=608)
  at('trade.ask.line',y=614,h=31);at('trade.ask.tip',y=639)
  at('trade.quote.return.line',y=614,h=31);at('trade.quote.return.tip',y=608)
  at('story.issuer.inquiry.subject',y=402,h=58)
 if i==18:at('review.llm.body',h=109)
 if i==27:at('dev.feedback.body',h=119)



 # Repairs found by individual-slide visual inspection.
 if i==3:
  for task,y in [('research',299),('trade',414),('client',529),('review',299),('risk',414),('files',299),('dev',414)]:
   at('task.'+task,y=y,h=48);at('task.'+task+'.outcome',y=y+53,h=55)
 if i==4:
  txt('research.evidence.1.text','Revenue (RMB m): 100 / 110\nSales volume (m units):\n1.0 / 1.1')
  for n,shape in S.items():
   if n.startswith('!!story.issuer.source'):
    xx,yy,ww,hh=geometry(shape);position(shape,h=160)
 if i==10:
  txt('trade.case1.1.body','Interpret the request\nSelect required tools')
  for j in range(4):at(f'trade.case1.{j}',h=163)
  at('trade.case1.scope',y=481)
  for j in range(4):
   at(f'trade.case2.{j}',y=605,h=178);at(f'trade.case2.{j}.role',y=616);at(f'trade.case2.{j}.body',y=658,h=118)
  txt('trade.case2.2.body','Match the quote request\nSend details to the\ntrading system')
 if i==12:
  for j in range(3):at(f'client.material{j}',h=110)
  at('story.client.input.record',h=110) if '!!story.client.input.record' in S else None
 if i==13:
  at('client.views.result',h=149)
  for n,shape in S.items():
   if n.startswith('!!story.client'):
    xx,yy,ww,hh=geometry(shape)
    if yy>550:position(shape,h=149)
 if i==16:
  at('review.reference.label',h=58);at('review.reference.text',y=363,h=126)
 if i==18:at('review.llm',h=182)
 if i==19:at('risk.question.2',h=198)
 if i==20:at('risk.rules.tool',h=172)
 if i==21:
  at('risk.evidence.system',y=434,h=144);at('risk.evidence.system.role',y=449);at('risk.evidence.system.body',y=488,h=86);at('story.issuer.holdings.data',y=491,h=83)
 if i==25:
  at('story.client.development.sample',y=318)
  at('story.client.development.sample.name',y=316) if '!!story.client.development.sample.name' in S else None
 if i==27:
  for n,shape in S.items():
   if n.startswith('!!dev.testFeedback') and not n.endswith('label'):
    xx,yy,ww,hh=geometry(shape)
    if n.endswith('.line'):position(shape,y=518,h=40)
    elif n.endswith('.tip'):position(shape,y=552)

 if i==11:
  at('trade.quote.merge.line',x=1080);at('trade.quote.merge.tip',x=1074)
  at('story.issuer.quote.table',h=126);at('trade.user',y=730,h=57)

 if i==9:at('trade.data.label',x=704,w=127)
 if i==10:
  for j in range(4):at(f'trade.case1.{j}',h=178)

added=[];unfit=[]
for d in M['slides']:
 i=d['page'];part=f'ppt/slides/slide{i}.xml';x=E.fromstring(data[part]);S={s.find('./p:nvSpPr/p:cNvPr',N).get('name'):s for s in x.findall('.//p:sp',N)}
 for e in d['shapes']:replacebody(S[e['name']].find('./p:txBody',N),e['english'])
 layout(i,S,x)
 # Normalize fragment punctuation without touching prose, source URLs or decimal values.
 for name,shape in S.items():
  fragment=name.startswith(('!!client.material','!!ops.row','!!other.')) or name in ['!!cover.kicker','!!driver.revenue.factor','!!arch.tools.body','!!ops.compare.functions'] or name.endswith(('.role','.label','.title','.outputs')) or name in ['!!research.llm.body','!!views.method.body','!!tender.llm.body','!!risk.event.llm.body','!!client.views.llm.body','!!dev.code.body','!!dev.debug.body','!!dev.test.body']
  if fragment:
   for t in shape.findall('./p:txBody//a:t',N):
    if t.text:t.text=t.text.rstrip('.')
 if i==11:
  table=x.find('.//a:tbl',N)
  for rr,row in enumerate(table.findall('./a:tr',N)):
   row.set('h',str((80 if rr==0 else 46)*U))
   for cc,cell in enumerate(row.findall('./a:tc',N)):replacebody(cell.find('./a:txBody',N),d['table'][rr][cc])
 for h in x.findall('.//a:hlinkClick',N):
  m=re.search(r'Slide (\d+)',h.get('tooltip',''))
  if m:h.set('tooltip',f"Slide {m.group(1)}: {M['slides'][int(m.group(1))-1]['title']}")
 for name,s in S.items():
  body=s.find('./p:txBody',N)
  if body is None or not ''.join(s.xpath('./p:txBody//a:t/text()',namespaces=N)):continue
  pr=body.find('.//a:rPr',N)
  if pr is None:continue
  size=float(pr.get('sz','1800'))/75
  need,avail,lines,mw,width=estimate(s,size)
  if need>avail+1 or mw>width+1:unfit.append({'page':i,'name':name,'size':size,'lines':lines,'needed':round(need,1),'available':round(avail,1),'width':round(width,1),'text':' / '.join(s.xpath('./p:txBody//a:t/text()',namespaces=N))})
 data[part]=E.tostring(x,xml_declaration=True,encoding='UTF-8',standalone=True)
 note=E.fromstring(data[f'ppt/notesSlides/notesSlide{i}.xml'])
 for s in note.findall('.//p:sp',N):
  ph=s.find('./p:nvSpPr/p:nvPr/p:ph',N)
  if ph is not None and ph.get('type')=='body':replacebody(s.find('./p:txBody',N),d['notes'])
 data[f'ppt/notesSlides/notesSlide{i}.xml']=E.tostring(note,xml_declaration=True,encoding='UTF-8',standalone=True)
 if i%6==0 or i==33:
  with ZipFile(B/'candidate.pptx','w') as z:
   for e in entries:z.writestr(e,data[e.filename])
  print(f'Saved native package through slide {i:02d}')
(B/'qa/fit-review.json').write_text(json.dumps(unfit,ensure_ascii=False,indent=2))
(B/'qa/added-objects.json').write_text(json.dumps(added,indent=2))
print('Needs review:',len(unfit))
