"""Reflow the approved native package into the measured corporate transfer canvas.

No presentation importer writes the deliverable. IDs, relationships, timing,
transitions and all approved words remain in their original OOXML package.
"""
from pathlib import Path
from zipfile import ZipFile
from copy import deepcopy
from lxml import etree as E
from PIL import ImageFont
import hashlib, json, math, re

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / 'build'
SPEC=json.loads((ROOT/'layout-spec.json').read_text())
SOURCE = (ROOT/SPEC['source_deck']).resolve()
SOURCE_SHA = SPEC['source_sha256']
NS = {'p':'http://schemas.openxmlformats.org/presentationml/2006/main', 'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
A, P = NS['a'], NS['p']
CM, PT, SOURCE_UNIT = SPEC['conversion']['emu_per_cm'], SPEC['conversion']['emu_per_point'], 9525
SLIDE = (SPEC['slide']['width'], SPEC['slide']['height'])
TITLE, SUBTITLE = SPEC['title'], SPEC['subtitle']
BODY = (SPEC['body']['x'], SPEC['body']['y'], SPEC['body']['right'], SPEC['body']['bottom'])
MAIN_LEFT, MAIN_TOP, MAIN_RIGHT, MAIN_BOTTOM = 6.88, 4.45, BODY[2], 12.00
SX = (MAIN_RIGHT-MAIN_LEFT)/1106  # cm per source coordinate
SY = (MAIN_BOTTOM-MAIN_TOP)/593

def emu_cm(v): return round(v*CM)
def emu_pt(v): return round(v*PT)
def half(v): return math.floor(v*2+0.5)/2
def local(x): return E.QName(x).localname
def nv(s): return s.find('.//p:cNvPr', NS)
def name(s): return nv(s).get('name','')
def xf(s):
    r=s.find('./p:spPr/a:xfrm', NS)
    return r if r is not None else s.find('./p:xfrm', NS)
def geom(s, unit=CM):
    f=xf(s); o=f.find('./a:off',NS); e=f.find('./a:ext',NS)
    return [int(v.get(k))/unit for v,k in [(o,'x'),(o,'y'),(e,'cx'),(e,'cy')]]
def pos(s,x=None,y=None,w=None,h=None):
    f=xf(s); o=f.find('./a:off',NS); e=f.find('./a:ext',NS)
    for k,v in [('x',x),('y',y)]:
        if v is not None: o.set(k,str(emu_cm(v)))
    for k,v in [('cx',w),('cy',h)]:
        if v is not None: e.set(k,str(max(1,emu_cm(v))))
def text(s): return '\n'.join(s.xpath('./p:txBody/a:p//a:t/text()',namespaces=NS))
def body_text(s,value):
    b=s.find('./p:txBody',NS)
    if b is None: return
    ps=b.findall('./a:p',NS); templates=[deepcopy(p) for p in ps]
    if not templates: return
    start=b.index(ps[0])
    for p in ps:b.remove(p)
    for j,line in enumerate(value.split('\n')):
        p=deepcopy(templates[min(j,len(templates)-1)])
        runs=p.findall('./a:r',NS); r=deepcopy(runs[0]) if runs else E.Element(f'{{{A}}}r')
        for q in list(p):
            if local(q) not in ['pPr','endParaRPr']:p.remove(q)
        for q in r.findall('./a:t',NS):r.remove(q)
        E.SubElement(r,f'{{{A}}}t').text=line
        end=p.find('./a:endParaRPr',NS)
        p.insert(p.index(end) if end is not None else len(p),r)
        b.insert(start+j,p)
def font(s,points):
    for q in s.iter():
        if local(q) in ['rPr','defRPr','endParaRPr']:q.set('sz',str(round(points*100)))
def scale_style(s,scale=0.55):
    for q in s.iter():
        tag=local(q)
        if tag in ['rPr','defRPr','endParaRPr'] and q.get('sz'):
            q.set('sz',str(round(max(9.5,half(float(q.get('sz'))/100*scale))*100)))
        if tag in ['latin','ea','cs'] and q.get('typeface'):q.set('typeface','Arial')
        if tag in ['bodyPr','tcPr']:
            for k in ['lIns','rIns','tIns','bIns','marL','marR','marT','marB']:
                if q.get(k): q.set(k,str(emu_cm(round(int(q.get(k))/CM*scale,3))))
        if tag in ['ln','lnL','lnR','lnT','lnB','lnTlToBr','lnBlToTr'] and q.get('w') and int(q.get('w'))>0:
            q.set('w',str(emu_pt(max(.5,half(int(q.get('w'))/PT*scale)))))
        if tag=='pPr':
            for k in ['marL','marR','indent']:
                if q.get(k):q.set(k,str(round(int(q.get(k))*scale)))
        if tag in ['spcPts'] and q.get('val'):q.set('val',str(round(int(q.get('val'))*scale)))

def transformed(s,origin=(426,209),dest=(MAIN_LEFT,MAIN_TOP),sx=SX,sy=SY):
    x,y,w,h=geom(s,SOURCE_UNIT)
    pos(s,round(dest[0]+(x-origin[0])*sx,3),round(dest[1]+(y-origin[1])*sy,3),round(w*sx,3),max(.003,round(h*sy,3)))

SIDEBAR={'!!map.front','!!nav.front','!!task.research','!!task.trade','!!task.client','!!map.middle','!!nav.middle','!!task.review','!!task.risk','!!map.back','!!nav.back','!!task.files','!!task.dev'}
def shared(i,S):
    for n,s in S.items():
        if n=='!!heading':pos(s,TITLE['x'],TITLE['y'],TITLE['width'],.85);font(s,20)
        elif n=='!!subtitle':pos(s,SUBTITLE['x'],SUBTITLE['y'],SUBTITLE['width'],.6);font(s,11.5)
        elif n=='!!heading.rule':pos(s,SUBTITLE['x'],SPEC['body']['y']-.20,SUBTITLE['width'],.003)
        elif n=='!!footer.rule':pos(s,BODY[0],BODY[3]-.34,SPEC['body']['width'],.003)
        elif n=='!!source':pos(s,BODY[0],BODY[3]-.30,SPEC['body']['width'],.30);font(s,7)
        elif n=='!!nav.home':pos(s,BODY[0],12.10,4.96,.50);font(s,10.5)
        elif n=='!!nav.prev':pos(s,20.35,12.10,1.75,.50);font(s,10)
        elif n=='!!nav.next':pos(s,22.38,12.10,1.75,.50);font(s,10)
        elif n=='!!page':pos(s,18.80,12.16,1.2,.35);font(s,9)
        elif n=='!!map.separator':pos(s,6.56,BODY[1],.003,8.03)
        elif n=='!!example':pos(s,22.68,BODY[1]+.02,1.45,.36);font(s,8)
        elif n.startswith('!!story.header.'):
            # A fixed body-row cue replaces the old subtitle-row position.
            dual=i in [3,29,30]
            if '.issuer.' in n: base=15.53 if dual else 17.20
            elif '.client.' in n:base=19.50 if dual else 17.20
            else:base=17.20
            if n.endswith('.bar'):pos(s,base,BODY[1]+.05,.07,.29)
            elif n.endswith('.name'):pos(s,base+.20,BODY[1],3.0,.40);font(s,10)
            elif n.endswith('.qualifier'):pos(s,20.55,BODY[1],2.1,.70);font(s,8.5)
        elif i not in [3,29] and n in SIDEBAR:
            transformed(s,(68,209),(BODY[0],BODY[1]),4.96/274,7.78/510)
            font(s,12 if n.startswith('!!nav.') else 10.5)
            if n=='!!task.files':font(s,10)

def overrides(i,S):
    def at(n,**kw):pos(S['!!'+n],**kw)
    def sz(n,p):font(S['!!'+n],p)
    def delta(n,dy=0,dh=0):
        x,y,w,h=geom(S['!!'+n]);at(n,y=y+dy,h=h+dh)
    if i==1:
        at('cover.title',x=TITLE['x'],y=TITLE['y'],w=TITLE['width'],h=.85);body_text(S['!!cover.title'],'LLMs in Asset Management');sz('cover.title',22)
        at('cover.kicker',x=SUBTITLE['x'],y=SUBTITLE['y'],w=SUBTITLE['width'],h=.60);sz('cover.kicker',12)
        at('cover.white',x=1.27,y=3.92,w=14.57,h=8.30)
        at('cover.line',x=1.27,y=6.15,w=13.60,h=.003)
        at('cover.date',x=1.27,y=5.1,w=13.60,h=.65);sz('cover.date',14)
        at('nav.next',x=1.27,y=10.80,w=3.6,h=.85);sz('nav.next',14)
        pic=next(s for s in S.values() if local(s)=='pic')
        pos(pic,16.84,3.92,7.289,8.30)
    if i in [3,29]:
        for office in ['front','middle','back']:delta('map.'+office,dh=.20)
        for task in ['trade','risk','dev']:delta('task.'+task,dy=.10);delta('task.'+task+'.outcome',dy=.10)
        delta('task.client',dy=.20);delta('task.client.outcome',dy=.20)
        for n in S:
            if n.endswith('.outcome'):delta(n[2:],dh=.12)
    if i==4:
        for n in ['story.issuer.source.1','story.issuer.source.2','story.issuer.source.3']:delta(n,dh=.28)
    if i==6:delta('views.method',dh=.18)
    if i==8:
        # Preserve every evidence sentence while reserving distinct rule/summary gaps.
        at('research.question',h=.72) if '!!research.question' in S else None
        for j,(rule,label,body,height) in enumerate([(5.60,5.67,6.14,1.16),(7.38,7.45,7.88,.43),(8.39,8.46,8.88,1.53)],1):
            at(f'research.evidence.{j}.rule',y=rule)
            at(f'research.evidence.{j}.label',y=label)
            at(f'research.evidence.{j}.text',y=body,h=height)
        for n in ['research.llm','research.tool']:at(n,y=5.60,h=4.53)
        for n in ['research.llm.role','research.tool.role']:delta(n,dy=-.136)
        for n in ['research.llm.body','research.tool.body']:delta(n,dy=-.136)
        at('research.material.in0',y=6.72);at('research.material.in1',y=8.05);at('research.material.in2',y=9.65)
        at('research.material.bus',y=6.72,h=2.93)
        at('research.result',y=10.47,h=1.18);at('story.issuer.analysis',y=10.47,h=1.18)
        at('research.result.title',y=10.57,h=.98)
        at('research.result.text',y=10.53,h=1.14);sz('research.result.text',9.5)
        at('research.toResult.line',y=10.20,h=.12);at('research.toResult.tip',y=10.26)
        at('research.user',y=11.73,h=.37);sz('research.user',9.5)
        at('story.issuer.source.group',y=5.60,h=4.81)
    if i==9:
        # Use the generous inter-panel gap for labels, with no forced word breaks.
        at('trade.data.label',x=11.25,y=9.64,w=2.02,h=.75);sz('trade.data.label',8.5)
        at('trade.ask.label',x=15.40,y=9.58,w=1.20,h=.75);sz('trade.ask.label',8.5)
        at('trade.quote.label',x=18.97,y=9.65,w=1.40,h=.38);sz('trade.quote.label',8.5)
        at('trade.system',y=10.36,h=1.10)
        at('trade.system.role',y=10.39,h=.74);sz('trade.system.role',9.5)
        at('trade.system.body',y=11.11,h=.38);sz('trade.system.body',9)
        at('trade.counterparty',y=10.36,h=1.10)
        at('trade.counterparty.role',y=10.42,h=.38)
        at('trade.counterparty.body',y=10.98,h=.40)
        at('trade.repetition',y=11.65,h=.42);sz('trade.repetition',10)
    if i==10:
        for j in range(4):delta(f'trade.case2.{j}',dh=.24)
    if i==13:
        delta('client.views.result',dh=.12)
        for n in S:
            if n.startswith('!!story.client') and not n.startswith('!!story.header'):
                x,y,w,h=geom(S[n])
                if y>9:delta(n[2:],dh=.12)
    if i==14:
        delta('tender.answer',dh=.43);delta('tender.answer.body',dh=.28)
    if i==15:
        delta('client.input.manager',dh=.17);delta('client.input.product',dh=.12)
    if i in [16,17]:
        at('clientDoc.highlight.view',h=1.33)
    if i==16:
        at('review.questions.title',y=8.35)
        at('review.questions',y=9.06,h=1.72)
    if i==17:
        at('comment.risk.body',h=1.15)
        at('comment.risk',h=1.90)
        at('review.case',h=.78)
    if i==18:
        at('review.inputs',h=2.25)
        at('review.inputs.body',y=5.55,h=1.52)
        at('review.tool.body',h=.78)
        at('review.tool',h=1.77)
        at('review.llm.body',h=1.50)
        at('clientDoc',h=6.65);at('story.client.document',h=6.65)
        at('clientDoc.highlight.view',h=2.07)
        at('clientDoc.highlight.risk',y=10.15,h=1.27)
        at('clientDoc.label.risk',y=10.20)
        at('clientDoc.value.risk',y=10.61,h=.76)
        at('review.user',y=11.72,h=.38)
    if i==21:
        at('risk.evidence.mail.text',h=1.72)
        at('story.issuer.event.mail',h=2.45)
        at('risk.evidence.system',y=7.48,h=2.02)
        at('risk.evidence.system.role',y=7.60)
        at('risk.evidence.system.body',y=8.10,h=1.30)
        at('story.issuer.holdings.data',y=8.10,h=1.30)
        for n in ['risk.evidence.rule.rule','risk.evidence.rule.label','risk.evidence.rule.text']:delta(n,dy=.43)
        delta('story.issuer.event.rule',dy=.43)
        delta('risk.result',dh=.23)
        delta('story.issuer.impact.report',dh=.23)
    if i==23:
        delta('ops.form',dh=.20)
        at('ops.compare.new.line2',y=10.53)
        delta('story.client.version.v2',dh=.24)
        # Phrase highlights follow the final text font rather than the old pixel canvas.
        def width(value,shape):
            r=shape.find('.//a:rPr',NS);p=float(r.get('sz'))/100
            f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',round(p*96/72*4))
            return f.getlength(value)/4*2.54/96
        for mark,body,prefix,phrase in [('ops.compare.mark.driver','ops.compare.new.line1','','Channel restocking'),('ops.compare.mark.watch','ops.compare.new.line2','We are monitoring ','whether restocking continues')]:
            x,y,w,h=geom(S['!!'+body]);at(mark,x=x+width(prefix,S['!!'+body]),y=y,w=width(phrase,S['!!'+body]),h=.39)
    if i==24:delta('ops.tool.body',dy=-.10)
    if i==25:
        at('dev.request',h=1.44)
        for n in S:
            if n.startswith('!!dev.') and n not in ['!!dev.request','!!dev.workload']:delta(n[2:],dy=.22)
        delta('story.client.development.sample',dy=.22)
        delta('story.client.development.sample.name',dy=.22)
    if i==27:
        for n in ['dev.feedback','dev.revise','dev.deliver']:delta(n,dh=.32)
    if i==28:delta('other.2.flow.1',dy=-.03,dh=.24)
    if i==31:
        at('arch.model',h=2.65);at('arch.tools',h=2.65)
        at('arch.model.body',h=1.33)
        at('arch.data',y=10.78,h=.86)
        at('arch.models',y=11.68,h=.37);sz('arch.models',9.5)
    if i==32:
        at('phase.0.roles',h=.86)
        at('phase.0.rule',y=6.90)

    # Give the final text boxes their measured line height. Background changes
    # above are explicit, and this pass never changes wording or point size.
    fit_names={4:['research.evidence.1.text','research.evidence.3.text'],5:['driver.llm.title'],10:['trade.case2.2.body'],11:['trade.user'],12:['client.question.text'],14:['tender.llm.body'],16:['review.reference.text'],23:['ops.compare.new.line1','ops.compare.new.line2'],27:['dev.request','dev.feedback.body']}
    for n in fit_names.get(i,[]):
        e=estimate(S['!!'+n])
        if e and e['overflow_cm']>0:delta(n,dh=e['overflow_cm']+.07)

def estimate(s):
    b=s.find('./p:txBody',NS)
    if b is None or not text(s):return None
    bp=b.find('./a:bodyPr',NS); x,y,w,h=geom(s)
    w-=sum(int(bp.get(k,'0'))/CM for k in ['lIns','rIns']);h-=sum(int(bp.get(k,'0'))/CM for k in ['tIns','bIns'])
    width=w*96/2.54; lines=0;needed=0
    for p in b.findall('./a:p',NS):
        value=''.join(p.xpath('.//a:t/text()',namespaces=NS));r=p.find('.//a:rPr',NS)
        size=float(r.get('sz','950'))/100 if r is not None else 9.5
        bold=r is not None and r.get('b')=='1'
        f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',round(size*96/72*4))
        count=1;line=''
        for word in value.split():
            test=(line+' '+word).strip()
            if line and f.getlength(test)/4>width:count+=1;line=word
            else:line=test
        lines+=count;needed+=count*size*96/72*1.12
    return {'lines':lines,'needed_cm':round(needed*2.54/96,3),'available_cm':round(h,3),'overflow_cm':round(needed*2.54/96-h,3)}

def main():
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SOURCE_SHA
    BUILD.mkdir(exist_ok=True);(BUILD/'qa').mkdir(exist_ok=True)
    with ZipFile(SOURCE) as z:entries=z.infolist();data={e.filename:z.read(e.filename) for e in entries}
    p=E.fromstring(data['ppt/presentation.xml']);size=p.find('./p:sldSz',NS);size.set('cx',str(SPEC['slide']['width_emu']));size.set('cy',str(SPEC['slide']['height_emu']))
    data['ppt/presentation.xml']=E.tostring(p,xml_declaration=True,encoding='UTF-8',standalone=True)
    fit=[];inventory=[]
    for i in range(1,34):
        part=f'ppt/slides/slide{i}.xml';root=E.fromstring(data[part]);ss=[s for s in root.find('./p:cSld/p:spTree',NS) if xf(s) is not None]
        S={name(s):s for s in ss}
        for s in ss:
            scale_style(s)
            if i in [2,3,29]:transformed(s,(68,209),(BODY[0],MAIN_TOP),SPEC['body']['width']/1464,SY)
            else:transformed(s)
            if local(s)=='graphicFrame':
                table=s.find('.//a:tbl',NS)
                for q in table.findall('./a:tblGrid/a:gridCol',NS):q.set('w',str(emu_cm(int(q.get('w'))/SOURCE_UNIT*SX)))
                for q in table.findall('./a:tr',NS):q.set('h',str(emu_cm(int(q.get('h'))/SOURCE_UNIT*SY)))
                font(s,9.5)
        # Sidebar positions use source coordinates, independent of body transforms.
        if i not in [1,2,3,29]:
            original=E.fromstring(data[part]);orig={name(s):s for s in original.find('./p:cSld/p:spTree',NS) if xf(s) is not None}
            for n in SIDEBAR:
                if n in S:pos(S[n],*(geom(orig[n],CM)))
        shared(i,S);overrides(i,S)
        for s in ss:
            e=estimate(s)
            if e and e['overflow_cm']>.04:fit.append({'slide':i,'name':name(s),'text':text(s),**e})
            inventory.append({'slide':i,'id':nv(s).get('id'),'name':name(s),'kind':local(s),'cm':[round(q,3) for q in geom(s)],'text':text(s)})
        data[part]=E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
    with ZipFile(BUILD/'candidate.pptx','w') as z:
        for e in entries:z.writestr(e,data[e.filename])
    (BUILD/'qa/fit-review.json').write_text(json.dumps(fit,indent=2))
    (BUILD/'qa/object-inventory.json').write_text(json.dumps(inventory,indent=2))
    print('Native candidate written. Potential text-fit items:',len(fit))
    for q in fit:print(q['slide'],q['name'],q['overflow_cm'])
if __name__=='__main__':main()
