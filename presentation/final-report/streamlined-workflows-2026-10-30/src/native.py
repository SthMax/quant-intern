"""Small native OOXML primitives for editable business mechanisms."""
from pathlib import Path
from copy import deepcopy
from lxml import etree as E
from PIL import ImageFont
import json
ROOT=Path(__file__).resolve().parent.parent
SPEC=json.loads((ROOT.parent/'corporate-template-2026-10-27/layout-spec.json').read_text())
P='http://schemas.openxmlformats.org/presentationml/2006/main';A='http://schemas.openxmlformats.org/drawingml/2006/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS={'p':P,'a':A,'r':R};CM=SPEC['conversion']['emu_per_cm'];PT=SPEC['conversion']['emu_per_point']
BLUE='005A9C';TEAL='317F7B';PURPLE='7363A6';INK='20262C';GRAY='65727D';RULE='CBD4DA';LIGHT='F3F7FA';YELLOW='FFF0BE'
L=SPEC['body']['x'];RGT=SPEC['body']['right'];W=SPEC['body']['width'];MAP_R=SPEC['vertical_guides']['absolute_x'][1];M=MAP_R+.50;MW=RGT-M
def cm(v):return round(v*CM)
def pt(v):return round(v*PT)
def n(parent,ns,tag,**attrs):return E.SubElement(parent,f'{{{ns}}}{tag}',{k:str(v) for k,v in attrs.items() if v is not None})
def norm(s):return ' '.join(s.split())
def width(t,size,bold=False):
    f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',round(size*96/72*4));return f.getlength(t)/4*2.54/96

class Page:
    def __init__(self,i,source,content):
        self.i=i;self.source=source;self.root=deepcopy(source);self.tree=self.root.find('./p:cSld/p:spTree',NS);self.copy=content;self.id=100;self.items=[];self.family='Pending';self.narration='';self.discussion='';self.custom=[]
        for q in list(self.tree):
            if E.QName(q).localname not in ['nvGrpSpPr','grpSpPr']:self.tree.remove(q)
        for q in list(self.root):
            if E.QName(q).localname=='timing' or q.xpath('.//*[local-name()="transition"]'):self.root.remove(q)
        self.text('title',norm(content['!!cover.title' if i==1 else '!!heading']),L,SPEC['title']['y'],W,.95,24,True)
        self.text('subtitle',norm(content['!!cover.kicker' if i==1 else '!!subtitle']),L,SPEC['subtitle']['y'],W,.75,16,False,BLUE)
        if content.get('!!source'):self.text('source.note',content['!!source'],L,13.17,W,.33,8,False,GRAY)
        if i not in [1,3,22]:self.map()
    def original(self,key):return self.copy[key if key.startswith('!!') else '!!'+key]
    def shape(self,name,x,y,w,h,fill=None,line=None,lw=.75,geometry='rect'):
        self.id+=1;s=n(self.tree,P,'sp');nv=n(s,P,'nvSpPr');n(nv,P,'cNvPr',id=self.id,name=name);n(nv,P,'cNvSpPr');n(nv,P,'nvPr');pr=n(s,P,'spPr');f=n(pr,A,'xfrm');n(f,A,'off',x=cm(x),y=cm(y));n(f,A,'ext',cx=cm(w),cy=cm(h));g=n(pr,A,'prstGeom',prst=geometry);n(g,A,'avLst')
        if fill:n(n(pr,A,'solidFill'),A,'srgbClr',val=fill)
        else:n(pr,A,'noFill')
        ln=n(pr,A,'ln',w=pt(lw) if line else 0)
        if line:n(n(ln,A,'solidFill'),A,'srgbClr',val=line)
        else:n(ln,A,'noFill')
        self.items.append({'name':name,'kind':'shape','cm':[x,y,w,h],'geometry':geometry});return s
    def text(self,name,value,x,y,w,h,size=12,bold=False,color=INK,align='l',anchor='t',fill=None,line=None,pad=0,geometry='rect',linepct=105000):
        s=self.shape(name,x,y,w,h,fill,line,geometry=geometry);b=n(s,P,'txBody');bp=n(b,A,'bodyPr',wrap='square',lIns=cm(pad),rIns=cm(pad),tIns=cm(pad),bIns=cm(pad),anchor=anchor);n(bp,A,'noAutofit');n(b,A,'lstStyle')
        vals=value if isinstance(value,list) else [{'text':t,'size':size,'bold':bold,'color':color} for t in str(value).split('\n')]
        for v in vals:
            pp=n(b,A,'p');pr=n(pp,A,'pPr',algn=align);n(n(pr,A,'lnSpc'),A,'spcPct',val=linepct)
            rp=n(pr,A,'defRPr',sz=round(v.get('size',size)*100),b=int(v.get('bold',bold)));n(n(rp,A,'solidFill'),A,'srgbClr',val=v.get('color',color));n(rp,A,'latin',typeface='Arial');n(rp,A,'ea',typeface='Arial');n(rp,A,'cs',typeface='Arial')
            run=n(pp,A,'r');rpr=deepcopy(rp);rpr.tag=f'{{{A}}}rPr';run.append(rpr);n(run,A,'t').text=v['text']
        self.items[-1].update(kind='text',text='\n'.join(v['text'] for v in vals),font_sizes=[v.get('size',size) for v in vals],padding_cm=pad);return s
    def node(self,name,title,body,x,y,w,h,kind='role',color=None,size=12):
        c=color or (BLUE if kind=='llm' else TEAL if kind=='issuer' else PURPLE if kind=='client' else GRAY)
        fill='EAF3FA' if kind=='llm' else 'EFF6F4' if kind=='issuer' else 'F7F4FB' if kind=='client' else LIGHT
        vals=[{'text':title,'size':13,'bold':True,'color':c}]
        if body:
            vals += [{'text':t,'size':size,'bold':False,'color':INK} for t in body.split('\n')]
        return self.text(name,vals,x,y,w,h,fill=fill,line=c,pad=.17,geometry='roundRect' if kind in ['role','llm','human','tool'] else 'rect',anchor='ctr')
    def document(self,name,title,body,x,y,w,h,color=TEAL,size=12):
        self.shape(name+'.paper',x,y,w,h,'FFFFFF',color,.75,'foldedCorner')
        lines=[];line=''
        for word in title.split():
            trial=(line+' '+word).strip()
            if line and width(trial,12.5,True)>w-.55:lines.append(line);line=word
            else:line=trial
        if line:lines.append(line)
        lines=lines or [''];offset=.72+.55*(len(lines)-1)
        self.text(name+'.title','\n'.join(lines),x+.18,y+.12,w-.55,.55*len(lines),12.5,True,color)
        self.text(name+'.content',body,x+.18,y+offset,w-.36,max(.15,h-offset-.14),size,linepct=100000)
    def line(self,name,x1,y1,x2,y2,color=BLUE,lw=.9,arrow=True):
        self.id+=1;s=n(self.tree,P,'cxnSp');nv=n(s,P,'nvCxnSpPr');n(nv,P,'cNvPr',id=self.id,name=name);n(nv,P,'cNvCxnSpPr');n(nv,P,'nvPr');pr=n(s,P,'spPr');f=n(pr,A,'xfrm',flipH='1' if x2<x1 else None,flipV='1' if y2<y1 else None);n(f,A,'off',x=cm(min(x1,x2)),y=cm(min(y1,y2)));n(f,A,'ext',cx=max(1,cm(abs(x2-x1))),cy=max(1,cm(abs(y2-y1))));g=n(pr,A,'prstGeom',prst='line');n(g,A,'avLst');ln=n(pr,A,'ln',w=pt(lw));n(n(ln,A,'solidFill'),A,'srgbClr',val=color)
        if arrow:n(ln,A,'tailEnd',type='triangle',w='sm',len='sm')
        self.items.append({'name':name,'kind':'connector','cm':[min(x1,x2),min(y1,y2),abs(x2-x1),abs(y2-y1)]})
    def route(self,name,points,color=BLUE,lw=.9,arrow=True):
        for j,(a,b) in enumerate(zip(points,points[1:])):self.line(name+'.'+str(j),*a,*b,color,lw,arrow and j==len(points)-2)
    def caption(self,name,value,x,y,w,size=10,color=GRAY,h=.45):self.text(name,value,x,y,w,h,size,False,color)
    def merge(self,name,edges,busx,target,color=BLUE):
        ys=[a[1] for a in edges]+[target[1]]
        for j,(xx,yy) in enumerate(edges):self.line(name+'.source.'+str(j),xx,yy,busx,yy,color,.75,False)
        self.line(name+'.bus',busx,min(ys),busx,max(ys),color,.75,False);self.line(name+'.target',busx,target[1],target[0],target[1],color,.9,True)
    def finance(self,name,x,y,w=4.50,h=3.00):
        self.shape(name+'.paper',x,y,w,h,'FFFFFF',TEAL,.75,'foldedCorner');self.text(name+'.title','[1] Company A',x+.15,y+.12,w-.50,.45,12.5,True,TEAL)
        self.caption(name+'.period','Prior / current quarter',x+.15,y+.64,w-.30,9.5,GRAY)
        self.text(name+'.revenue.label','Revenue\n(RMB m)',x+.15,y+1.08,2.35,.95,10.5)
        self.text(name+'.revenue.values','100 / 110',x+2.50,y+1.16,w-2.65,.55,12,True,TEAL)
        self.text(name+'.volume.label','Sales volume\n(m units)',x+.15,y+1.91,2.35,.95,10.5)
        self.text(name+'.volume.values','1.0 / 1.1',x+2.50,y+1.99,w-2.65,.55,12,True,TEAL)
    def excerpt(self,name,paragraphs,x,y,w,size=12,lineh=.58,changes=()):
        import re
        yy=y
        for pi,para in enumerate(paragraphs):
            spans=[]
            for phrase in changes:
                start=para.find(phrase)
                if start>=0:spans.append((start,start+len(phrase)))
            words=list(re.finditer(r'\S+',para));groups=[];start=0;line=[]
            for word in words:
                trial=para[start:word.end()] if line else word.group()
                if line and width(trial,size)>w-.04:
                    groups.append((start,line[-1].end()));start=word.start();line=[word]
                else:
                    if not line:start=word.start()
                    line.append(word)
            if line:groups.append((start,line[-1].end()))
            for li,(a,b) in enumerate(groups):
                val=para[a:b]
                for hi,(c,d) in enumerate(spans):
                    lo=max(a,c);hiend=min(b,d)
                    if lo<hiend:self.shape(name+f'.highlight.{pi}.{li}.{hi}',x+width(para[a:lo],size),yy+.07,width(para[lo:hiend],size),.47,YELLOW)
                self.text(name+f'.line.{pi}.{li}',val,x,yy,w,.58,size,linepct=100000)
                yy+=lineh
            yy+=.10
        return yy-y
    def client_evidence(self,name,x,y,w,h,version=1,metadata=True,risk=True,highlight=False,size=12):
        self.shape(name+'.paper',x,y,w,h,'FFFFFF',PURPLE,.8)
        self.text(name+'.title','Quarterly client update '+('V1' if version==1 else 'V2'),x+.20,y+.14,w-.40,.62,13,True,PURPLE)
        yy=y+.97
        if metadata:
            fund='Product A Select' if version==1 else 'Product A Select Mixed-Asset Fund'
            period='Q2 2026, V1' if version==1 else 'Q3 2026, V2'
            self.text(name+'.fund',fund,x+.20,yy,w-.40,.55,10.5);yy+=.66
            self.text(name+'.source','Product source: '+period,x+.20,yy,w-.40,.55,10.5,False,GRAY);yy+=.77
        self.text(name+'.view.label','Investment view',x+.20,yy,w-.40,.45,10.5,True);yy+=.57
        para=['Higher sales volumes drove Company A’s revenue growth.','We are monitoring raw-material costs.'] if version==1 else ['Channel restocking supported Company A’s sales volume growth.','We are monitoring whether restocking continues, alongside raw-material costs.']
        spans=['Channel restocking supported','sales volume','whether restocking continues, alongside'] if highlight and version==2 else []
        yy+=self.excerpt(name+'.view',para,x+.20,yy,w-.40,size,.58,spans)
        if risk:
            yy+=.22;self.text(name+'.risk.label','Risk disclosure',x+.20,yy,w-.40,.45,10.5,True);yy+=.55
            risktext='Investing involves risk.' if version==1 else 'The fund’s NAV fluctuates with market conditions. Capital is at risk.'
            self.excerpt(name+'.risk',[risktext],x+.20,yy,w-.40,10.5,.50)
    def map(self):
        current='research' if 4<=self.i<=7 or self.i==26 else 'trade' if 8<=self.i<=10 else 'client' if 11<=self.i<=13 or self.i==27 else 'risk' if 14<=self.i<=16 else 'records' if 17<=self.i<=18 else 'dev' if 19<=self.i<=21 else None
        whole=self.i in [2,24];cross=self.i==23;front=self.i==25
        groups=[('Front office',[('research','Research'),('trade','Trading support'),('client','Client communications')],4.18),('Middle office',[('risk','Risk analysis')],7.08),('Back office',[('records','Record entry'),('dev','Tool development')],9.42)]
        for j,(office,tasks,y) in enumerate(groups):
            active=whole or cross or any(k==current for k,v in tasks) or front and j==0 or self.i==28 and j==2
            self.text('map.office.'+str(j),office,L+.08,y,4.70,.50,11,True,BLUE if active else GRAY)
            self.line('map.office.rule.'+str(j),L,y+.61,MAP_R-.12,y+.61,BLUE if active else RULE,.6,False)
            for k,(key,label) in enumerate(tasks):
                ty=y+.83+k*.55;on=key==current or whole or cross and key!='dev' or front and key in ['research','client']
                if on:self.shape('map.task.focus.'+key,L+.08,ty-.01,4.66,.49,'D9EAF7')
                self.text('map.task.'+key,label,L+.27,ty,4.34,.46,10.5,on,BLUE if on else GRAY)
    def table(self,x,y,w=MW):
        q=deepcopy(self.source.find('.//p:graphicFrame',NS));self.id+=1;nv=q.find('./p:nvGraphicFramePr/p:cNvPr',NS);nv.set('id',str(self.id));nv.set('name','output.bond.quote.table')
        f=q.find('./p:xfrm',NS);o=f.find('./a:off',NS);e=f.find('./a:ext',NS);o.set('x',str(cm(x)));o.set('y',str(cm(y)));e.set('cx',str(cm(w)));e.set('cy',str(cm(2.65)))
        tab=q.find('.//a:tbl',NS)
        for col,ww in zip(tab.findall('./a:tblGrid/a:gridCol',NS),[3.4,4.3,5.4,w-13.1]):col.set('w',str(cm(ww)))
        for rr,row in enumerate(tab.findall('./a:tr',NS)):
            row.set('h',str(cm(1.40 if rr==0 else 1.25)))
            for cell in row.findall('./a:tc',NS):
                pr=cell.find('./a:tcPr',NS)
                for k in ['marL','marR']:pr.set(k,str(cm(.12)))
                for k in ['marT','marB']:pr.set(k,str(cm(.08)))
                for el in cell.iter():
                    if E.QName(el).localname in ['rPr','defRPr','endParaRPr']:el.set('sz','1200')
                    if E.QName(el).localname in ['lnL','lnR','lnT','lnB']:el.set('w',str(pt(.5)))
        self.tree.append(q);self.items.append({'name':'output.bond.quote.table','kind':'table','cm':[x,y,w,2.65]})
