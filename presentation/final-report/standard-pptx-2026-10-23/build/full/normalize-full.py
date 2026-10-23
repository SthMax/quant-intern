from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
from copy import deepcopy
from pathlib import Path
NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
def q(p,t):return '{'+NS[p]+'}'+t
src=ZipFile('full/artifact-full-draft.pptx');parts={n:src.read(n) for n in src.namelist()}
for n,blob in list(parts.items()):
 if not n.endswith('.xml'):continue
 r=E.fromstring(blob)
 if r.tag == q('a','theme'):
  r.set('name','Office Standard')
  for fs in r.findall('.//a:fontScheme',NS):
   fs.set('name','Office Standard Chinese')
   for f in list(fs):
    f.find('a:ea',NS).set('typeface','Arial Unicode MS')
    for script in ['Hans','Hant','Jpan','Hang']:
     E.SubElement(f,q('a','font'),script=script,typeface='Arial Unicode MS')
 if n.startswith('ppt/slides/slide'):
  for sp in r.findall('.//p:sp',NS):
   ph=sp.find('p:nvSpPr/p:nvPr/p:ph',NS)
   if ph is not None:
    # Let slide text styles inherit from its standard layout.
    ls=sp.find('p:txBody/a:lstStyle',NS)
    if ls is not None:ls.clear()
    for pp in sp.findall('p:txBody/a:p/a:pPr',NS):
     for child in list(pp):
      if child.tag==q('a','defRPr'):pp.remove(child)
     if pp.find('a:buNone',NS) is None:pp.insert(0,E.Element(q('a','buNone')))
  for rp in r.findall('.//a:rPr',NS)+r.findall('.//a:endParaRPr',NS):rp.set('lang','zh-CN')
 if n=='ppt/slideMasters/slideMaster2.xml':
  styles=r.find('p:txStyles',NS)
  if styles is None:styles=E.SubElement(r,q('p','txStyles'))
  for role,size,bold in [('titleStyle','3150','1'),('bodyStyle','2100','0'),('otherStyle','1800','0')]:
   st=E.SubElement(styles,q('p',role))
   for i in range(1,10):
    pp=E.SubElement(st,q('a',f'lvl{i}pPr'),marL='0',indent='0');E.SubElement(pp,q('a','buNone'));rp=E.SubElement(pp,q('a','defRPr'),sz=size,b=bold,lang='zh-CN')
    prefix='+mj' if role=='titleStyle' else '+mn'
    E.SubElement(rp,q('a','latin'),typeface=prefix+'-lt');E.SubElement(rp,q('a','ea'),typeface=prefix+'-ea')
 if '/charts/' in n:
  for el in r.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/chart}valAx/{http://schemas.openxmlformats.org/drawingml/2006/chart}numFmt'):
   el.set('sourceLinked','0');el.set('formatCode','0')
  for el in r.findall('.//a:latin',NS):el.set('typeface','+mn-lt')
  for el in r.findall('.//a:ea',NS):el.set('typeface','+mn-ea')
 if n.startswith('ppt/slideLayouts/slideLayout'):
  number=int(Path(n).stem.replace('slideLayout',''))
  types={1:'title',2:'titleOnly',3:'obj',4:'twoObj',5:'secHead',6:'blank',7:'title',8:'obj',9:'secHead',10:'twoObj',11:'obj'}
  r.set('type',types[number]);r.set('preserve','1')
  for pp in (r.findall('.//a:pPr',NS)+r.findall('.//a:defPPr',NS)+[el for el in r.iter() if E.QName(el).localname.startswith('lvl') and E.QName(el).localname.endswith('pPr')]) if number>=7 else []:
   if pp.find('a:buNone',NS) is None:pp.insert(0,E.Element(q('a','buNone')))
  if number in [8,10]:
   tree=r.find('p:cSld/p:spTree',NS)
   template=r.find('.//p:sp[p:nvSpPr/p:nvPr/p:ph[@type="body"]]',NS) if False else [s for s in tree.findall('p:sp',NS) if s.find('.//p:ph',NS).get('type')=='body'][0]
   for idx,geo in ([(2,(64,205,1152,470))] if number==8 else [(2,(64,235,552,300)),(3,(664,235,552,300))]):
    s=deepcopy(template);s.find('p:nvSpPr/p:cNvPr',NS).set('id',str(100+idx));s.find('p:nvSpPr/p:cNvPr',NS).set('name','Content '+str(idx))
    ph=s.find('.//p:ph',NS);ph.set('type','obj');ph.set('idx',str(idx));sp=s.find('p:spPr',NS);xf=sp.find('a:xfrm',NS)
    if xf is None:xf=E.SubElement(sp,q('a','xfrm'))
    xf.clear();E.SubElement(xf,q('a','off'),x=str(geo[0]*9525),y=str(geo[1]*9525));E.SubElement(xf,q('a','ext'),cx=str(geo[2]*9525),cy=str(geo[3]*9525))
    tree.append(s)
 if n.startswith('ppt/slides/slide'):
  for i,gf in enumerate(r.findall('.//p:graphicFrame',NS)):
   nv=gf.find('p:nvGraphicFramePr/p:nvPr',NS)
   E.SubElement(nv,q('p','ph'),type='obj',idx=str(2+i))
 parts[n]=E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile('full/standard-full-candidate.pptx','w',ZIP_DEFLATED) as out:
 for n,b in parts.items():out.writestr(n,b)
print('Normalized standard layouts, theme fonts, placeholders and native content links.')
