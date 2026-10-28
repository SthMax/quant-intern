"""Editable static redesign, using native OOXML and the approved package assets.

Every body is composed explicitly in centimeters. Artifact Tool imports/renders
the result; it does not re-export the final native table or diagrams.
"""
from pathlib import Path
from zipfile import ZipFile
from copy import deepcopy
from lxml import etree as E
from PIL import ImageFont
import json,hashlib,math,re

ROOT=Path(__file__).resolve().parent.parent
BUILD=ROOT/'build';QA=BUILD/'qa'
SPEC=json.loads((ROOT.parent/'corporate-template-2026-10-27/layout-spec.json').read_text())
SOURCE=ROOT.parent/'corporate-template-2026-10-27/output/asset-management-llm-corporate-transfer.pptx'
SOURCE_SHA='f7a92ebd1caf4f0257b89065d23b0eccc78456aa0248fdef13e4d7afbf0cf440'
CONTENT=json.loads((ROOT/'src/source-content.json').read_text())
P='http://schemas.openxmlformats.org/presentationml/2006/main'
A='http://schemas.openxmlformats.org/drawingml/2006/main'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS={'p':P,'a':A,'r':R}
CM=SPEC['conversion']['emu_per_cm'];PT=SPEC['conversion']['emu_per_point']
BLUE='005A9C';TEAL='317F7B';PURPLE='7363A6';INK='20262C';GRAY='687782';LIGHT='F3F7FA';RULE='CCD5DA';YELLOW='FFF0BE'
LEFT=SPEC['body']['x'];RIGHT=SPEC['body']['right'];WIDTH=SPEC['body']['width'];TOP=SPEC['body']['y'];BOTTOM=SPEC['body']['bottom']
COL3=[1.27,9.15,17.02];COLW=[7.11,7.10,7.11]
def cm(v):return round(v*CM)
def pt(v):return round(v*PT)
def node(parent,ns,tag,**attrs):return E.SubElement(parent,f'{{{ns}}}{tag}',{k:str(v) for k,v in attrs.items() if v is not None})
def norm(s):return ' '.join(s.split())

class Page:
    def __init__(self,i,source):
        self.i=i;self.source=source;self.root=deepcopy(source);self.tree=self.root.find('./p:cSld/p:spTree',NS);self.used=set();self.id=100;self.items=[];self.family='';self.principle=''
        self.copy=CONTENT[i-1]['text']
        for q in list(self.tree):
            if E.QName(q).localname not in ['nvGrpSpPr','grpSpPr']:self.tree.remove(q)
        for q in list(self.root):
            if E.QName(q).localname=='timing' or q.xpath('.//*[local-name()="transition"]'):self.root.remove(q)
        self.header()
    def take(self,key,flat=False):
        k=key if key.startswith('!!') else '!!'+key
        self.used.add(k);v=self.copy[k]
        return norm(v) if flat else v
    def box(self,name,x,y,w,h,fill=None,line=None,lw=.5):
        self.id+=1;s=node(self.tree,P,'sp');nv=node(s,P,'nvSpPr');node(nv,P,'cNvPr',id=self.id,name=name);node(nv,P,'cNvSpPr');node(nv,P,'nvPr')
        pr=node(s,P,'spPr');f=node(pr,A,'xfrm');node(f,A,'off',x=cm(x),y=cm(y));node(f,A,'ext',cx=cm(w),cy=cm(h))
        g=node(pr,A,'prstGeom',prst='rect');node(g,A,'avLst')
        if fill:node(node(pr,A,'solidFill'),A,'srgbClr',val=fill)
        else:node(pr,A,'noFill')
        ln=node(pr,A,'ln',w=pt(lw) if line else 0)
        if line:node(node(ln,A,'solidFill'),A,'srgbClr',val=line)
        else:node(ln,A,'noFill')
        self.items.append({'name':name,'kind':'shape','cm':[x,y,w,h]})
        return s
    def txt(self,name,value,x,y,w,h,size=12,bold=False,color=INK,align='l',anchor='t',fill=None,pad=0,line=None):
        s=self.box(name,x,y,w,h,fill,line);b=node(s,P,'txBody');bp=node(b,A,'bodyPr',wrap='square',lIns=cm(pad),rIns=cm(pad),tIns=cm(pad),bIns=cm(pad),anchor=anchor);node(bp,A,'noAutofit');node(b,A,'lstStyle')
        for t in str(value).split('\n'):
            p=node(b,A,'p');pp=node(p,A,'pPr',algn=align);node(node(pp,A,'lnSpc'),A,'spcPct',val=108000)
            rp=node(pp,A,'defRPr',sz=round(size*100),b=int(bold));node(node(rp,A,'solidFill'),A,'srgbClr',val=color);node(rp,A,'latin',typeface='Arial');node(rp,A,'ea',typeface='Arial');node(rp,A,'cs',typeface='Arial')
            r=node(p,A,'r');rpr=deepcopy(rp);rpr.tag=f'{{{A}}}rPr';r.append(rpr);node(r,A,'t').text=t
        self.items[-1].update(kind='text',text=value,font_pt=size,bold=bold,padding_cm=pad)
        return s
    def source_text(self,key,x,y,w,h,**kw):return self.txt('!!'+key,self.take(key),x,y,w,h,**kw)
    def line(self,name,x1,y1,x2,y2,color=RULE,width=.5,arrow=False):
        self.id+=1;s=node(self.tree,P,'cxnSp');nv=node(s,P,'nvCxnSpPr');node(nv,P,'cNvPr',id=self.id,name=name);node(nv,P,'cNvCxnSpPr');node(nv,P,'nvPr');pr=node(s,P,'spPr')
        f=node(pr,A,'xfrm',flipH='1' if x2<x1 else None,flipV='1' if y2<y1 else None);node(f,A,'off',x=cm(min(x1,x2)),y=cm(min(y1,y2)));node(f,A,'ext',cx=max(1,cm(abs(x2-x1))),cy=max(1,cm(abs(y2-y1))));g=node(pr,A,'prstGeom',prst='line');node(g,A,'avLst')
        ln=node(pr,A,'ln',w=pt(width));node(node(ln,A,'solidFill'),A,'srgbClr',val=color)
        if arrow:node(ln,A,'tailEnd',type='triangle',w='sm',len='sm')
        self.items.append({'name':name,'kind':'connector','cm':[min(x1,x2),min(y1,y2),abs(x2-x1),abs(y2-y1)]})
    def header(self):
        title='cover.title' if self.i==1 else 'heading';sub='cover.kicker' if self.i==1 else 'subtitle'
        self.source_text(title,LEFT,SPEC['title']['y'],WIDTH,.94 if self.i==1 else .80,size=22 if self.i==1 else 20.5,bold=True)
        self.txt('!!'+sub,norm(self.take(sub)),LEFT,SPEC['subtitle']['y'],WIDTH,.52,size=10.5,color=GRAY)
        self.line('header.rule',LEFT,3.72,RIGHT,3.72,width=.5)
        if self.i!=1:self.source_text('source',LEFT,12.77,WIDTH,.24,size=6.5,color=GRAY) if self.copy.get('!!source') else None
        if self.i not in [1,2,3,29,30]:
            office=0 if 4<=self.i<=15 else 1 if 16<=self.i<=21 else 2 if 22<=self.i<=28 else -1
            for j,label in enumerate(['Front office','Middle office','Back office']):
                self.txt('locator.'+str(j),label,COL3[j],12.35,COLW[j],.28,size=8,bold=(j==office),color=BLUE if j==office else GRAY)
    def heading(self,text,x,y,w,color=BLUE,size=13):return self.txt('section.'+str(self.id+1),text,x,y,w,.65,size=size,bold=True,color=color)
    def rulehead(self,key,x,y,w,color=BLUE,size=13,h=.62):
        self.txt('!!'+key,norm(self.take(key)),x,y,w,h,size=size,bold=True,color=color);self.line(key+'.rule',x,y+h+.10,x+w,y+h+.10,color=color,width=1)
    def note(self,key,y=11.75,size=11):self.txt('!!'+key,norm(self.take(key)),LEFT,min(y,11.84),WIDTH,.52,size=size)
    def module(self,base,x,y,w,h,color=BLUE,fill=None,size=11.5):
        if fill:self.box(base+'.background',x,y,w,h,fill)
        self.source_text(base+'.role',x+.16,y+.12,w-.32,.88,size=12,bold=True,color=color)
        self.source_text(base+'.body',x+.16,y+1.15,w-.32,h-1.27,size=size)
    def document(self,x,y,w,h,version=1,highlight=False):
        self.box('client.document',x,y,w,h,'FFFFFF',PURPLE,.75);self.line('client.document.accent',x,y,x,y+h,PURPLE,2)
        self.source_text('clientDoc.title',x+.28,y+.22,w-1.3,.60,size=14,bold=True,color=PURPLE)
        self.source_text('clientDoc.version',x+w-.8,y+.24,.5,.4,size=11,bold=True,color=PURPLE,align='r')
        self.line('client.document.rule',x+.28,y+.94,x+w-.28,y+.94,PURPLE,.5)
        if version==1:
            fields=[('product',1.25,.70),('period',2.13,.70),('view',3.04,2.05),('risk',5.42,.90)]
        else:fields=[('product',1.25,.70),('period',2.13,.70),('view',3.04,2.10),('risk',5.50,1.58)]
        for f,dy,fh in fields:
            if f=='risk' and version==1:fh=1.24
            if highlight is True or (isinstance(highlight,set) and f in highlight):self.box('client.highlight.'+f,x+.22,y+dy-.08,w-.44,fh+.08,YELLOW)
            if f in ['product','period']:
                self.txt('!!clientDoc.label.'+f,norm(self.take('clientDoc.label.'+f)),x+.36,y+dy,2.90,.58,size=10.5,bold=True,color=GRAY)
                self.source_text('clientDoc.value.'+f,x+3.45,y+dy,w-3.83,fh,size=11.5)
            else:
                self.txt('!!clientDoc.label.'+f,norm(self.take('clientDoc.label.'+f)),x+.36,y+dy,w-.72,.45,size=10.5,bold=True,color=INK)
                self.source_text('clientDoc.value.'+f,x+.36,y+dy+.50,w-.72,fh-.45,size=11.5)
    def table(self,x,y,w):
        q=deepcopy(self.source.find('.//p:graphicFrame',NS));self.id+=1
        nv=q.find('./p:nvGraphicFramePr/p:cNvPr',NS);nv.set('id',str(self.id));nv.set('name','table.bond.summary')
        for old in nv.findall('./a:hlinkClick',NS):nv.remove(old)
        f=q.find('./p:xfrm',NS);o=f.find('./a:off',NS);e=f.find('./a:ext',NS)
        o.set('x',str(cm(x)));o.set('y',str(cm(y)));e.set('cx',str(cm(w)));e.set('cy',str(cm(1.8)))
        tab=q.find('.//a:tbl',NS)
        for el,ww in zip(tab.findall('./a:tblGrid/a:gridCol',NS),[5,5.55,6.0,w-16.55]):el.set('w',str(cm(ww)))
        for rr,row in enumerate(tab.findall('./a:tr',NS)):
            row.set('h',str(cm(1.12 if rr==0 else .68)))
            for cell in row.findall('./a:tc',NS):
                cp=cell.find('./a:tcPr',NS)
                for k in ['marL','marR']:cp.set(k,str(cm(.14)))
                for k in ['marT','marB']:cp.set(k,str(cm(.08)))
                for r in cell.iter():
                    if E.QName(r).localname in ['rPr','defRPr','endParaRPr']:r.set('sz','1100' if rr==0 else '1150')
                    if E.QName(r).localname in ['lnL','lnR','lnT','lnB']:r.set('w',str(pt(.5)))
        self.tree.append(q);self.items.append({'name':'table.bond.summary','kind':'table','cm':[x,y,w,1.8]})

def representative(p):
    i=p.i
    if i==8:
        p.family='Evidence / LLM analysis / calculation, with full-width output'
        p.source_text('research.question',LEFT,4.04,WIDTH,.66,size=14,bold=True,color=BLUE)
        for j,(ly,by,bh) in enumerate([(5.15,5.70,1.03),(6.98,7.50,.60),(8.30,8.83,1.36)],1):
            p.source_text(f'research.evidence.{j}.label',1.27,ly,7.11,.46,size=11.5,bold=True,color=TEAL)
            val=p.take(f'research.evidence.{j}.text')
            if j==1:val=val.replace('Sales volume (m units):\n','Sales volume (m units): ')
            p.txt(f'!!research.evidence.{j}.text',val,1.27,by,7.11,bh,size=11)
            if j<3:p.line(f'evidence.{j}.rule',1.27,by+bh+.14,8.38,by+bh+.14)
        p.rulehead('research.llm.role',9.15,5.15,7.10)
        p.source_text('research.llm.body',9.15,6.17,7.10,3.40,size=12)
        p.box('calculation.background',17.02,5.06,7.11,4.72,LIGHT)
        p.source_text('research.tool.role',17.32,5.24,6.51,.7,size=12.5,bold=True)
        p.source_text('research.tool.body',17.32,6.40,6.51,2.95,size=13,color=TEAL)
        p.line('analysis.calculation',16.40,7.18,16.90,7.18,BLUE,1,True)
        p.line('calculation.analysis',16.90,8.40,16.40,8.40,BLUE,1,True)
        p.line('evidence.analysis',8.50,7.18,9.03,7.18,TEAL,1,True)
        p.line('analysis.summary',12.70,9.75,12.70,10.27,BLUE,1,True)
        p.box('research.output',LEFT,10.45,WIDTH,1.30,'EFF6F4')
        p.source_text('research.result.title',1.55,10.62,4.70,1.05,size=12,bold=True,color=TEAL)
        p.source_text('research.result.text',6.65,10.63,17.15,1.02,size=11)
        p.note('research.user',11.88,10.5)
    elif i==11:
        p.family='Query criteria and supplied quote into a native result table'
        p.source_text('trade.intent',LEFT,4.05,WIDTH,.84,size=13,bold=True,color=BLUE)
        for j,base in enumerate(['trade.llm.query','trade.system','trade.llm.quote']):
            p.rulehead(base+'.role',COL3[j],5.25,COLW[j],BLUE,12.5,1.1)
            p.source_text(base+'.body',COL3[j],6.55,COLW[j],2.10,size=11.5,color=TEAL if j==1 else INK)
        p.line('query.execution',8.50,7.1,9.03,7.1,BLUE,1,True)
        for x in [12.70,20.575]:p.line('data.summary.'+str(x),x,8.80,x,9.03,BLUE,1,True)
        p.source_text('trade.result.title',LEFT,8.96,WIDTH,.58,size=14,bold=True,color=BLUE)
        p.table(LEFT,9.66,WIDTH)
        p.note('trade.user',11.69,10.5)
    elif i==17:
        p.family='Reviewed client document with three aligned LLM comments'
        p.document(1.27,4.12,13.30,7.20,1,True)
        p.source_text('business.review.umbrella',15.55,4.12,8.58,.6,size=14,bold=True,color=BLUE)
        for n,dy,h in [('meta',5.10,1.55),('view',7.07,1.90),('risk',9.45,1.87)]:
            p.source_text('comment.'+n+'.role',15.85,dy,7.98,.45,size=12,bold=True)
            p.source_text('comment.'+n+'.body',15.85,dy+.58,7.98,h-.45,size=11.5)
            p.line('comment.'+n+'.rule',15.55,dy-.10,24.13,dy-.10,color=RULE)
            p.line('document.comment.'+n,14.70,dy+.6,15.40,dy+.6,BLUE,.75,True)
        p.note('review.case',11.70,10.5)
    elif i==18:
        p.family='Three-stage review method beside the complete revised client document'
        p.document(11.45,4.12,12.68,7.66,2,True)
        for base,y,h in [('review.inputs',4.20,2.46),('review.tool',7.02,1.80),('review.llm',9.08,2.62)]:
            p.txt('!!'+base+'.role',norm(p.take(base+'.role')),1.27,y,9.05,.68,size=12,bold=True,color=BLUE if base.endswith('llm') else INK)
            p.source_text(base+'.body',1.27,y+.82,9.05,1.90 if base.endswith('inputs') else h-.82,size=10.5 if base.endswith('inputs') else 11.5)
            if base!='review.llm':p.line(base+'.rule',1.27,7.00 if base.endswith('inputs') else y+h+.18,10.32,7.00 if base.endswith('inputs') else y+h+.18)
        p.line('review.document',10.47,10.13,11.25,10.13,BLUE,1,True)
        p.note('review.user',11.91,10)
    elif i==22:
        p.family='Open three-column operations matrix with one highlighted recurring example'
        for j in range(3):p.rulehead(f'ops.head{j}',COL3[j],4.25,COLW[j],BLUE,14)
        for r,y in enumerate([5.72,7.68,9.64]):
            if r==1:p.box('operations.client.version.row',LEFT,y-.15,WIDTH,1.35,'F3F0F8')
            for c in range(3):p.source_text(f'ops.row{r}.{c}',COL3[c]+.16,y,COLW[c]-.32,1.05,size=13,bold=(c==2),color=PURPLE if r==1 else INK)
            for xx in [8.49,16.37]:p.line(f'operations.flow.{r}.{xx}',xx,y+.44,xx+.49,y+.44,BLUE,1,True)
            if r<2:p.line(f'operations.row.{r}',LEFT,y+1.38,RIGHT,y+1.38)
        p.note('ops.repetition',11.75,11.5)
    elif i==32:
        p.family='Three-stage implementation timeline with aligned teams and deliverables'
        p.line('implementation.timeline',1.75,4.72,23.80,4.72,BLUE,1.5,True)
        for j in range(3):
            x=COL3[j];w=COLW[j]
            p.source_text(f'phase.{j}.number',x,5.02,w,.95,size=25,bold=True,color=BLUE)
            p.source_text(f'phase.{j}.title',x,6.12,w,1.42,size=14,bold=True,color=BLUE)
            p.txt(f'phase.{j}.teams.label',p.take('business.phase.teams'),x,7.98,w,.45,size=9.5,bold=True,color=GRAY)
            p.source_text(f'phase.{j}.roles',x,8.57,w,1.0,size=11.5)
            p.txt(f'phase.{j}.deliverables.label',p.take('business.phase.outputs'),x,10.02,w,.45,size=9.5,bold=True,color=GRAY)
            p.source_text(f'phase.{j}.outputs',x,10.62,w,1.55,size=12)
    else:return False
    return True

def first_half(p):
    i=p.i
    if i==1:
        p.family='Minimal cover with full original landscape artwork'
        q=deepcopy(p.source.find('.//p:pic',NS));p.id+=1
        n=q.find('./p:nvPicPr/p:cNvPr',NS);n.set('id',str(p.id));n.set('name','cover.artwork')
        for n in q.findall('./p:blipFill/a:srcRect',NS):n.getparent().remove(n)
        f=q.find('./p:spPr/a:xfrm',NS);o=f.find('./a:off',NS);e=f.find('./a:ext',NS)
        for k,v in [('x',12.70),('y',4.10)]:o.set(k,str(cm(v)))
        e.set('cx',str(cm(11.43)));e.set('cy',str(cm(7.62)));p.tree.append(q);p.items.append({'name':'cover.artwork','kind':'image','cm':[12.70,4.10,11.43,7.62]})
        p.txt('cover.scope','Mainland asset management',LEFT,4.45,10.40,.8,size=16,color=BLUE)
        p.line('cover.rule',LEFT,10.28,10.80,10.28,BLUE,1)
        p.source_text('cover.date',LEFT,10.78,10.40,.6,size=12.5,color=GRAY)
    elif i==2:
        p.family='Input / LLM work / output overview with a dominant center column'
        for j,(x,w) in enumerate([(1.27,4.96),(7.06,10.17),(18.28,5.85)]):p.rulehead(f'scope.head{j}',x,4.30,w,BLUE,13.5)
        for j,y in enumerate([5.73,7.02,8.31,9.60]):
            p.source_text(f'scope.input{j}',1.27,y,4.96,.94,size=12.5)
            p.txt(f'!!scope.work{j}',norm(p.take(f'scope.work{j}')),7.06,y-.09,10.17,1.02,size=13,bold=True,color=BLUE,fill=LIGHT,pad=.16)
            p.txt(f'!!scope.output{j}',norm(p.take(f'scope.output{j}')),18.28,y,5.85,1.02,size=12.5)
        p.line('scope.input.work',6.36,8.15,6.93,8.15,BLUE,1,True);p.line('scope.work.output',17.38,8.15,18.13,8.15,BLUE,1,True)
        p.source_text('scope.result',LEFT,11.40,WIDTH,.7,size=14,bold=True,color=BLUE)
    elif i in [3,29]:
        p.family='Seven-task editorial map in three open office columns'
        groups=[('front',['research','trade','client']),('middle',['review','risk']),('back',['files','dev'])]
        for j,(off,tasks) in enumerate(groups):
            p.txt('map.office.'+off,p.take('nav.'+off),COL3[j],4.27,COLW[j],.75,size=16,bold=True,color=BLUE)
            p.line('map.office.rule.'+off,COL3[j],5.20,COL3[j]+COLW[j],5.20,BLUE,1)
            for k,t in enumerate(tasks):
                y=5.58+k*1.78
                p.source_text('task.'+t,COL3[j],y,COLW[j],.67,size=12.5,bold=True,color=BLUE)
                p.txt('!!task.'+t+'.outcome',norm(p.take('task.'+t+'.outcome')),COL3[j],y+.75,COLW[j],.94,size=11)
        if i==3:
            p.source_text('map.route.title',LEFT,11.30,3.6,.92,size=10.5,bold=True,color=GRAY)
            p.source_text('map.route1.text',5.10,11.30,19.03,.55,size=10.5,color=TEAL)
            p.source_text('map.route2.text',5.10,11.88,19.03,.55,size=10.5,color=PURPLE)
        else:p.note('recommend.body',11.70,12)
    elif i==4:
        p.family='Three research evidence columns above the analyst preparation sequence'
        p.source_text('research.question',LEFT,4.05,WIDTH,.76,size=14,bold=True,color=BLUE)
        for j in range(1,4):
            p.source_text(f'research.evidence.{j}.label',COL3[j-1],5.30,COLW[j-1],.60,size=11.5,bold=True,color=TEAL)
            t=p.take(f'research.evidence.{j}.text').replace('Sales volume (m units):\n','Sales volume (m units): ')
            p.txt(f'!!research.evidence.{j}.text',t,COL3[j-1],6.04,COLW[j-1],2.00,size=12)
        p.source_text('research.manual.title',LEFT,8.53,WIDTH,.60,size=13,bold=True,color=BLUE)
        xs=[1.27,7.15,13.03,18.91]
        for k,x in enumerate(xs):
            p.txt(f'!!research.manual.{k}',norm(p.take(f'research.manual.{k}')),x,9.54,5.22,1.15,size=12.5,bold=True)
            if k<3:p.line(f'research.preparation.{k}',x+5.35,10.00,x+5.73,10.00,BLUE,1,True)
        p.note('research.repetition',11.67,11.5)
    elif i==5:
        p.family='Earnings-driver tree with a separate execution-tools lane'
        p.source_text('driver.llm.title',LEFT,4.05,WIDTH,1.10,size=13,bold=True,color=BLUE)
        p.txt('!!driver.root',norm(p.take('driver.root')),1.27,6.90,4.25,1.70,size=15,bold=True,color='FFFFFF',fill=BLUE,pad=.22,anchor='ctr')
        p.line('driver.branch',6.20,5.80,6.20,10.30,BLUE,1);p.line('driver.root.branch',5.55,7.75,6.20,7.75,BLUE,1)
        for k,(base,y) in enumerate([('revenue',5.32),('cost',7.36),('expense',9.40)]):
            p.line('driver.branch.'+base,6.20,y+.55,6.86,y+.55,BLUE,1,True)
            p.txt('!!driver.'+base+'.node',norm(p.take('driver.'+base+'.node')),7.02,y,3.48,1.10,size=13,bold=True,color=BLUE)
            p.line('driver.factor.'+base,10.57,y+.55,11.21,y+.55,BLUE,1,True)
            p.txt('!!driver.'+base+'.factor',norm(p.take('driver.'+base+'.factor')),11.43,y,8.00,1.10,size=12.5)
        p.txt('!!driver.tools',norm(p.take('driver.tools')),20.50,5.30,3.63,5.21,size=12,bold=True,fill=LIGHT,pad=.25,anchor='ctr')
        p.note('driver.result',11.65,11)
    elif i==6:
        p.family='Paired research hypotheses with a separated synthesis'
        p.source_text('views.llm.title',LEFT,4.05,WIDTH,.80,size=13.5,bold=True,color=BLUE)
        for j,base in enumerate(['views.reportA','views.reportB','views.method']):
            key=base+'.role' if j==2 else base+'.label';p.rulehead(key,COL3[j],5.30,COLW[j],TEAL if j<2 else BLUE,12.5)
            p.source_text(base+('.body' if j==2 else '.text'),COL3[j],6.35,COLW[j],2.35,size=11.5 if j==2 else 12.5)
        for x,base in [(1.27,'views.consensus'),(13.20,'views.difference')]:
            p.source_text(base+'.title',x,9.35,10.93,.56,size=13,bold=True,color=TEAL if x<2 else BLUE)
            p.source_text(base+'.body',x,10.12,10.93,.98,size=13)
        p.line('synthesis.rule',LEFT,8.98,RIGHT,8.98,TEAL,.75)
        p.note('views.user',11.75,11)
    elif i==7:
        p.family='Source-to-template mapping with one attributed performance callout'
        p.source_text('elements.head',LEFT,4.05,WIDTH,.72,size=13.5,bold=True,color=BLUE)
        p.rulehead('elements.left',1.27,5.22,6.40,BLUE,12.5);p.rulehead('elements.right',9.15,5.22,14.98,BLUE,12.5)
        for j,y in enumerate([6.50,7.87,9.24]):
            p.txt(f'!!element.{j}.source',norm(p.take(f'element.{j}.source')),1.27,y,6.40,1.02,size=12)
            p.line(f'template.map.{j}',7.91,y+.40,8.89,y+.40,BLUE,1,True)
            p.source_text(f'element.{j}.label',9.15,y,4.60,1.02,size=11.5,bold=True,color=BLUE)
            p.source_text(f'element.{j}.value',14.12,y,10.01,1.02,size=12.5)
            p.line(f'template.row.{j}',9.15,y+1.09,24.13,y+1.09)
        p.source_text('elements.stat',LEFT,10.85,WIDTH,1.0,size=11.5,bold=True,color=BLUE)
        p.note('elements.user',12.00,10.5)
    elif i==9:
        p.family='Four open trading stages with a separate systems/counterparty support lane'
        p.source_text('trade.task',LEFT,4.05,WIDTH,.76,size=13.5,bold=True,color=BLUE)
        for k,base in enumerate(['trade.intent','trade.query','trade.inquire','trade.compare']):
            x=1.27+k*5.88;p.rulehead(base+'.role',x,5.25,5.22,BLUE,12,1.03)
            p.source_text(base+'.body',x,6.66,5.22,3.13,size=11)
            if k<3:p.line('trade.stage.'+str(k),x+5.35,7.82,x+5.73,7.82,BLUE,1,True)
        p.line('trade.support.rule',LEFT,10.13,RIGHT,10.13)
        p.txt('trade.system.support',norm(p.take('trade.system.role'))+': '+p.take('trade.system.body'),1.27,10.55,10.93,.88,size=11.5,color=GRAY)
        p.txt('trade.counterparty.support',p.take('trade.counterparty.role')+': '+p.take('trade.counterparty.body'),13.20,10.55,10.93,.88,size=11.5,color=GRAY)
        p.note('trade.repetition',11.75,10.5)
    elif i==10:
        p.family='Two separate peer workflows with aligned four-stage lanes'
        for row,(head,y) in enumerate([('trade.southern',4.07),('trade.xq',8.52)],1):
            p.source_text(head,LEFT,y,WIDTH,.67,size=13,bold=True,color=BLUE)
            for k in range(4):
                x=1.27+k*5.88;base=f'trade.case{row}.{k}'
                p.txt('!!'+base+'.role',norm(p.take(base+'.role')),x,y+1.05,5.22,.80,size=11.5,bold=True,color=BLUE)
                p.source_text(base+'.body',x,y+1.97,5.22,1.67,size=11)
                if k<3:p.line(f'peer.{row}.flow.{k}',x+5.33,y+2.45,x+5.73,y+2.45,BLUE,.75,True)
        p.source_text('trade.case1.scope',LEFT,7.68,WIDTH,.56,size=10.5,bold=True,color=BLUE)
    elif i==12:
        p.family='Client questions and source material above a three-step preparation sequence'
        p.source_text('client.task',LEFT,4.05,WIDTH,.76,size=13.5,bold=True,color=BLUE)
        p.source_text('client.question.label',1.27,5.35,10.93,.52,size=11,bold=True,color=GRAY)
        p.source_text('client.question.text',1.27,6.07,10.93,2.15,size=14)
        for j,y in enumerate([5.35,6.65,7.95]):
            p.txt(f'!!client.material{j}',norm(p.take(f'client.material{j}')),13.20,y,10.93,.98,size=12.5,color=PURPLE)
            p.line(f'client.material.rule.{j}',13.20,y+1.02,24.13,y+1.02)
        p.source_text('client.manual.title',LEFT,9.28,WIDTH,.60,size=12.5,bold=True,color=BLUE)
        for k in range(3):
            p.txt(f'!!client.manual.{k}',norm(p.take(f'client.manual.{k}')),COL3[k],10.25,COLW[k],1.05,size=12,bold=True)
            if k<2:p.line(f'client.manual.flow.{k}',COL3[k]+COLW[k]+.12,10.69,COL3[k+1]-.12,10.69,BLUE,.75,True)
        p.note('client.repetition',11.75,10.5)
    elif i==13:
        p.family='Source quotation and LLM method with an emphasized client-facing summary'
        p.source_text('client.views.head',LEFT,4.05,WIDTH,1.05,size=13,bold=True,color=BLUE)
        p.source_text('client.views.source.label',1.27,5.65,10.93,.85,size=11,bold=True,color=GRAY)
        p.source_text('client.views.source.text',1.27,6.65,10.93,1.95,size=12.5)
        p.rulehead('client.views.llm.role',13.20,5.65,10.93,BLUE,13)
        p.source_text('client.views.llm.body',13.20,6.76,10.93,1.85,size=12)
        p.box('client.summary.output',LEFT,9.50,WIDTH,1.78,'F3F0F8')
        p.source_text('client.views.result.title',1.56,9.77,6.72,1.12,size=12.5,bold=True,color=PURPLE)
        p.source_text('client.views.result.text',8.84,9.79,14.93,1.16,size=12)
        p.note('client.views.user',11.70,11)
    elif i==14:
        p.family='Reference material to LLM method to a traceable RFP response'
        p.source_text('tender.question',LEFT,4.05,WIDTH,.85,size=13,bold=True,color=BLUE)
        for j,(role,body) in enumerate([('tender.source.label','tender.source.text'),('tender.llm.role','tender.llm.body'),('tender.answer.role','tender.answer.body')]):
            if j==2:p.box('rfp.document',16.80,5.21,7.33,5.52,'FFFFFF',PURPLE,.75)
            p.rulehead(role,COL3[j],5.45,COLW[j]-.22,BLUE if j<2 else PURPLE,12,1.02)
            p.source_text(body,COL3[j],6.83,COLW[j]-.22,3.56,size=11.5)
            if j<2:p.line('rfp.flow.'+str(j),COL3[j]+COLW[j]+.10,8.0,(COL3[j+1]-.12) if j==0 else 16.68,8.0,BLUE,.75,True)
        p.note('tender.user',11.14,10.5)
        p.txt('!!tender.case',norm(p.take('tender.case')),LEFT,11.80,WIDTH,.50,size=10.5,bold=True,color=BLUE)
    elif i==15:
        p.family='Client inputs and explicit LLM drafting beside the complete V1 document'
        p.document(11.45,4.12,12.68,7.20,1,False)
        for key,y in [('client.input.customer',4.25),('client.input.manager',5.93),('client.input.product',7.61)]:
            t=p.take(key).split('\n');p.txt(key+'.label',t[0],1.27,y,9.05,.45,size=10.5,bold=True,color=GRAY);p.txt(key+'.value',norm(' '.join(t[1:])),1.27,y+.60,9.05,.85,size=13)
            p.line(key+'.rule',1.27,y+1.45,10.32,y+1.45)
        p.rulehead('client.llm.role',1.27,9.47,9.05,BLUE,13)
        p.source_text('client.llm.body',1.27,10.48,9.05,1.12,size=11.5)
        p.line('draft.client.document',10.49,10.70,11.25,10.70,BLUE,1,True)
        p.note('client.user',11.91,10.5)
    elif i==16:
        p.family='V1 document contrasted with current-source uncertainty and review criteria'
        p.document(1.27,4.12,13.30,7.20,1,{'view'})
        p.source_text('review.reference.label',15.55,4.22,8.58,.96,size=12,bold=True,color=BLUE)
        p.source_text('review.reference.text',15.55,5.43,8.58,2.10,size=12)
        p.rulehead('review.questions.title',15.55,8.0,8.58,BLUE,13)
        p.source_text('review.questions',15.55,9.12,8.58,2.18,size=12)
        p.note('review.manual',11.75,10.5)
    else:return False
    return True

def second_half(p):
    i=p.i
    if i==19:
        p.family='Issuer risk alert above three evidence questions'
        p.source_text('risk.mail.label',LEFT,4.18,WIDTH,.52,size=11,bold=True,color=TEAL)
        p.source_text('risk.mail.text',LEFT,4.96,WIDTH,1.34,size=16,color=TEAL)
        p.source_text('risk.manual.title',LEFT,7.03,WIDTH,.65,size=13,bold=True,color=BLUE)
        for j in range(3):
            p.rulehead(f'risk.question.{j}.role',COL3[j],8.13,COLW[j],BLUE,13)
            p.source_text(f'risk.question.{j}.body',COL3[j],9.24,COLW[j],1.78,size=12)
        p.note('risk.repetition',11.75,11)
    elif i==20:
        p.family='Two peer approaches aligned by risk activity'
        p.rulehead('risk.htf',1.27,4.15,10.93,BLUE,15)
        p.rulehead('risk.th',13.20,4.15,10.93,BLUE,15)
        for base,y in [('risk.mail.extract',5.49),('risk.rules.tool',8.18)]:
            p.txt('!!'+base+'.role',norm(p.take(base+'.role')),1.27,y,10.93,.95,size=12.5,bold=True)
            p.source_text(base+'.body',1.27,y+1.16,10.93,1.20,size=12)
        p.source_text('risk.rules.explain',1.27,11.20,10.93,.98,size=10.5,bold=True,color=BLUE)
        p.source_text('risk.event.input.label',13.20,5.49,10.93,.52,size=11,bold=True,color=GRAY)
        p.source_text('risk.event.input.text',13.20,6.28,10.93,1.33,size=12)
        p.source_text('risk.event.llm.role',13.20,8.18,10.93,.95,size=12.5,bold=True,color=BLUE)
        p.source_text('risk.event.llm.body',13.20,9.34,10.93,1.36,size=12)
        p.source_text('risk.event.user',13.20,11.20,10.93,.98,size=10.5)
    elif i==21:
        p.family='Issuer evidence into an explicit LLM assessment and follow-up document'
        for base,y,h in [('risk.evidence.mail',4.25,1.55),('risk.evidence.system',6.80,1.80),('risk.evidence.rule',9.50,1.50)]:
            role=base+('.role' if base.endswith('system') else '.label');body=base+('.body' if base.endswith('system') else '.text')
            p.source_text(role,1.27,y,7.11,.55,size=11.5,bold=True,color=TEAL)
            p.source_text(body,1.27,y+.73,7.11,h,size=11.5)
        p.rulehead('risk.llm.role',9.15,5.18,7.10,BLUE,13)
        p.txt('!!risk.llm.body',p.take('risk.llm.body').replace('Review clauses\nand issuer research','Review clauses and issuer research'),9.15,6.38,7.10,3.70,size=12)
        p.box('risk.assessment.document',17.02,4.12,7.11,7.40,'FFFFFF',TEAL,.75)
        p.source_text('risk.result.role',17.32,4.40,6.51,.95,size=13,bold=True,color=TEAL)
        p.source_text('risk.result.body',17.32,5.72,6.51,5.33,size=11.5)
        p.line('risk.evidence.llm',8.50,7.33,9.03,7.33,TEAL,1,True);p.line('risk.llm.assessment',16.40,7.33,16.90,7.33,BLUE,1,True)
        p.note('risk.user',11.90,10)
    elif i==23:
        p.family='Automated-entry evidence alongside a large V1/V2 document comparison'
        p.rulehead('ops.huaan',1.27,4.13,7.11,BLUE,13)
        p.source_text('ops.form.role',1.27,5.49,7.11,.60,size=12,bold=True)
        p.source_text('ops.form.body',1.27,6.39,7.11,2.29,size=11.5)
        p.source_text('ops.stat',1.27,9.30,7.11,2.40,size=11,bold=True,color=BLUE)
        p.rulehead('ops.icbc',9.15,4.13,14.98,BLUE,13)
        p.source_text('ops.formats',9.15,5.12,14.98,.44,size=10.5,color=GRAY)
        p.source_text('ops.compare.read',9.15,5.77,14.98,.65,size=12.5,bold=True)
        p.source_text('ops.compare.old.label',9.15,6.60,14.98,.50,size=11.5,bold=True,color=PURPLE)
        p.source_text('ops.compare.old.text',9.15,7.23,14.98,1.14,size=11.5)
        p.source_text('ops.compare.new.label',9.15,8.72,14.98,.52,size=11.5,bold=True,color=PURPLE)
        def text_width(t,size):
            f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',round(size*96/72*4));return f.getlength(t)/4*2.54/96
        p.box('version.highlight.driver',9.15,9.50,text_width('Channel restocking',11.5),.48,YELLOW)
        p.box('version.highlight.monitoring',9.15+text_width('We are monitoring ',11.5),10.32,text_width('whether restocking continues',11.5),.48,YELLOW)
        p.txt('!!ops.compare.new.line1',norm(p.take('ops.compare.new.line1')),9.15,9.38,14.98,.77,size=11.5)
        p.txt('!!ops.compare.new.line2',norm(p.take('ops.compare.new.line2')),9.15,10.20,14.98,1.15,size=11.5)
        p.source_text('ops.compare.functions',9.15,11.70,14.98,.5,size=10.5,bold=True,color=BLUE)
    elif i==24:
        p.family='Version-analysis method beside a tangible change-summary document'
        for base,y,h in [('ops.inputs',4.20,1.37),('ops.tool',6.20,1.80),('ops.llm',8.60,2.50)]:
            p.txt('!!'+base+'.role',norm(p.take(base+'.role')),1.27,y,9.05,.68,size=12,bold=True,color=BLUE if base.endswith('llm') else INK)
            p.source_text(base+'.body',1.27,y+.87,9.05,h-.70,size=11.5)
            if base!='ops.llm':p.line(base+'.rule',1.27,y+h+.27,10.32,y+h+.27)
        p.box('change.summary.document',11.45,4.12,12.68,7.66,'FFFFFF',PURPLE,.75)
        p.source_text('changeLog.title',11.79,4.37,11.99,.64,size=14,bold=True,color=PURPLE)
        p.source_text('changeLog.object',11.79,5.16,11.99,.50,size=10.5,color=GRAY)
        p.line('change.summary.rule',11.79,5.78,23.79,5.78,PURPLE,.5)
        for base,y,bh in [('changeLog.driver',6.05,.95),('changeLog.watch',7.90,1.08),('changeLog.sync',9.77,1.00)]:
            p.source_text(base+'.label',11.79,y,11.99,.56,size=12,bold=True,color=BLUE)
            p.source_text(base+'.body',11.79,y+.73,11.99,bh,size=11.5)
        p.line('analysis.change.summary',10.48,10.10,11.24,10.10,BLUE,1,True)
        p.note('ops.user',11.94,10.5)
    elif i in [25,26]:
        p.family='Three open development stages with explicit requirements, code and testing'
        if i==25:
            p.source_text('dev.request',LEFT,4.04,WIDTH,1.24,size=13,bold=True,color=BLUE)
        else:
            p.source_text('dev.case1',LEFT,4.04,WIDTH,.63,size=13.5,bold=True,color=BLUE)
            p.source_text('dev.case2',LEFT,4.91,WIDTH,.92,size=11.5,color=GRAY)
        p.source_text('story.client.development.sample.name',LEFT,5.89,WIDTH,.47,size=10.5,bold=True,color=PURPLE)
        bases=['dev.requirements','dev.code','dev.debug' if i==25 else 'dev.test']
        for j,base in enumerate(bases):
            p.rulehead(base+'.role',COL3[j],6.63,COLW[j],BLUE,12.5,1.00)
            p.source_text(base+'.body',COL3[j],8.03,COLW[j],2.44,size=12)
            if j<2:p.line('development.flow.'+str(j),COL3[j]+COLW[j]+.12,9.0,COL3[j+1]-.12,9.0,BLUE,1,True)
        p.note('dev.workload' if i==25 else 'dev.case.result',11.53,11.5)
    elif i==27:
        p.family='Six-stage code-and-test feedback loop in a restrained serpentine flow'
        p.source_text('dev.request',LEFT,4.04,WIDTH,.90,size=13,bold=True,color=BLUE)
        for j,base in enumerate(['dev.samples','dev.generate','dev.test','dev.deliver','dev.revise','dev.feedback']):
            row=j//3;k=j%3;y=5.40 if row==0 else 9.12;x=COL3[k]
            p.rulehead(base+'.role',x,y,COLW[k],BLUE,11.5,.82)
            p.source_text(base+'.body',x,y+1.16,COLW[k],1.72,size=11,color=PURPLE if base=='dev.samples' else INK)
        for y in [7.35,11.08]:
            for a,b in [(8.50,9.03),(16.40,16.90)]:p.line('development.loop.'+str(y)+'.'+str(a),a if y<9 else b,y,b if y<9 else a,y,BLUE,1,True)
        p.line('development.test.feedback',20.57,8.35,20.57,8.90,BLUE,1,True)
        p.source_text('dev.testFeedback.label',21.00,8.42,3.13,.40,size=8.5,color=GRAY)
    elif i==28:
        p.family='Three compact application lanes separated by subject headings'
        for j,y in enumerate([4.10,6.72,9.34]):
            p.source_text(f'other.{j}.title',1.27,y,10.93,.64,size=12.5,bold=True,color=BLUE)
            p.source_text(f'other.{j}.company',13.20,y+.07,10.93,.50,size=9.5,color=GRAY)
            for k in range(3):
                value=p.take(f'other.{j}.flow.{k}').replace('contributions\nto','contributions to')
                p.txt(f'!!other.{j}.flow.{k}',value,COL3[k],y+.90,COLW[k],1.66,size=11 if k==1 else 11.5,bold=(k==2),color=BLUE if k==1 else INK)
                if k<2:p.line(f'application.flow.{j}.{k}',COL3[k]+COLW[k]+.10,y+1.70,COL3[k+1]-.12,y+1.70,BLUE,.75,True)
    elif i==30:
        p.family='Two colored information lanes across the three offices'
        for j in range(3):p.rulehead(f'cross.head{j}',COL3[j],4.20,COLW[j],BLUE,14)
        for r,(key,y,c,tint) in enumerate([('cross.issuer',5.65,TEAL,'EFF6F4'),('cross.client',8.95,PURPLE,'F3F0F8')]):
            p.source_text(key,LEFT,y,WIDTH,.65,size=14,bold=True,color=c)
            p.box('information.lane.'+str(r),LEFT,y+.98,WIDTH,1.75,tint)
            for k in range(3):
                p.source_text(f'cross.{r}.{k}',COL3[k]+.16,y+1.16,COLW[k]-.32,1.41,size=12,bold=True)
                if k<2:p.line(f'information.lane.{r}.flow.{k}',COL3[k]+COLW[k]+.10,y+1.85,COL3[k+1]-.12,y+1.85,c,1,True)
    elif i==31:
        p.family='Shared-capability hierarchy with distinct LLM and execution responsibilities'
        p.source_text('arch.entry',LEFT,4.08,WIDTH,.76,size=13.5,bold=True,color=BLUE)
        p.line('architecture.entry',12.70,5.00,12.70,5.42,BLUE,1,True)
        p.txt('!!arch.workflow',p.take('arch.workflow'),LEFT,5.58,WIDTH,.83,size=14,bold=True,color='FFFFFF',fill=BLUE,pad=.14)
        p.line('architecture.branch',6.74,6.78,18.67,6.78,BLUE,1);p.line('architecture.trunk',12.70,6.43,12.70,6.78,BLUE,1)
        for x,base in [(1.27,'arch.model'),(13.20,'arch.tools')]:
            p.line(base+'.input',x+5.46,6.78,x+5.46,7.05,BLUE,1,True)
            p.txt('!!'+base+'.role',norm(p.take(base+'.role')),x,7.26,10.93,.88,size=12.5,bold=True,color=BLUE)
            p.source_text(base+'.body',x,8.44,10.93,1.86,size=12)
        p.box('shared.data.band',LEFT,10.61,WIDTH,1.08,LIGHT)
        p.txt('!!arch.data',norm(p.take('arch.data')),1.51,10.77,22.38,.80,size=10.5)
        p.note('arch.models',11.97,10.5)
    elif i==33:
        p.family='Evaluation cycle above four concrete outcome measures'
        p.source_text('evaluation.main',LEFT,4.05,WIDTH,.80,size=13.5,bold=True,color=BLUE)
        for j in range(4):
            x=1.27+j*5.88;p.txt(f'!!evaluation.flow.{j}',norm(p.take(f'evaluation.flow.{j}')),x,5.53,5.22,1.10,size=12.5,bold=True)
            if j<3:p.line('evaluation.cycle.'+str(j),x+5.34,6.04,x+5.73,6.04,BLUE,1,True)
        for j,(x,y) in enumerate([(1.27,8.02),(13.20,8.02),(1.27,10.15),(13.20,10.15)]):
            p.source_text(f'evaluation.{j}.title',x,y,10.93,.60,size=13,bold=True,color=BLUE)
            p.txt(f'!!evaluation.{j}.body',norm(p.take(f'evaluation.{j}.body')),x,y+.84,10.93,1.12,size=11.5)
    else:return False
    return True

def fallback(p):
    # Only used during early composition calibration; all pages receive a final
    # explicit layout before the stable draft is produced.
    p.family='Pending redesign'
    exclude=lambda n:n.startswith(('!!nav.','!!map.','!!task.','!!story.header.')) or n in ['!!heading','!!subtitle','!!example','!!page','!!source']
    vals=[(n,v) for n,v in p.copy.items() if not exclude(n)]
    y=4.1
    for n,v in vals[:8]:
        p.txt(n,v,1.27,y,22.86,.75,size=10.5);y+=.9

def main():
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SOURCE_SHA
    QA.mkdir(exist_ok=True,parents=True)
    with ZipFile(SOURCE) as z:entries=z.infolist();data={e.filename:z.read(e.filename) for e in entries}
    pages=[]
    for i in range(1,34):
        part=f'ppt/slides/slide{i}.xml';p=Page(i,E.fromstring(data[part]))
        if not representative(p) and not first_half(p) and not second_half(p):fallback(p)
        data[part]=E.tostring(p.root,xml_declaration=True,encoding='UTF-8',standalone=True)
        rel=f'ppt/slides/_rels/slide{i}.xml.rels';rels=E.fromstring(data[rel])
        for q in list(rels):
            if q.get('Type','').endswith('/slide'):rels.remove(q)
        data[rel]=E.tostring(rels,xml_declaration=True,encoding='UTF-8',standalone=True)
        if i==3:
            note=f'ppt/notesSlides/notesSlide{i}.xml';s=data[note].decode();s=s.replace('The task names provide direct navigation to each topic.','The task names locate the seven application areas across the firm.');data[note]=s.encode()
        pages.append({'slide':i,'family':p.family,'items':p.items,'source_keys_used':sorted(p.used),'unused_text':{n:v for n,v in p.copy.items() if n not in p.used}})
    with ZipFile(BUILD/'candidate.pptx','w') as z:
        for e in entries:z.writestr(e,data[e.filename])
    (QA/'layout-manifest.json').write_text(json.dumps(pages,indent=2,ensure_ascii=False))
    print('Native static draft written; explicit compositions:',sum(p['family']!='Pending redesign' for p in pages))
if __name__=='__main__':main()
