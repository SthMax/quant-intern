import json,re
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as ET
from effects_lib import add_morph,add_reveal
ROOT=Path(__file__).resolve().parent.parent
P='http://schemas.openxmlformats.org/presentationml/2006/main'
A='http://schemas.openxmlformats.org/drawingml/2006/main'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG='http://schemas.openxmlformats.org/package/2006/relationships'
NS={'p':P,'a':A,'r':R}
m=json.loads((ROOT/'src/state-manifest.json').read_text())
with ZipFile(ROOT/'build/base.pptx') as z:
    entries=z.infolist(); content={e.filename:z.read(e.filename) for e in entries}
paths=[p for p in content if re.fullmatch(r'ppt/slides/slide\d+\.xml',p)]
assert len(paths)==m['slideCount']==33
nav_audit=[]; effects=[]
for d in m['slides']:
    page=d['page']; sp=f'ppt/slides/slide{page}.xml'; rp=f'ppt/slides/_rels/slide{page}.xml.rels'
    slide=ET.fromstring(content[sp]);rels=ET.fromstring(content[rp]);props=slide.xpath('.//p:cNvPr',namespaces=NS)
    by_name={p.get('name'):p for p in props}; names=[p.get('name') for p in props if p.get('name','').startswith('!!')]
    assert len(names)==len(set(names)),f'Duplicate object on {page}'
    links=[]
    for key,target in d['navigation'].items():
        obj=by_name.get('!!'+key)
        if obj is None:
            assert page<=2 and key not in (['nav.next'] if page==1 else ['nav.home','nav.prev','nav.next']),(page,key)
            continue
        rid=f'rIdNavSlide{target}'; rel=rels.find(f'{{{PKG}}}Relationship[@Id="{rid}"]')
        if rel is None:rel=ET.SubElement(rels,f'{{{PKG}}}Relationship',Id=rid)
        rel.set('Type',R+'/slide');rel.set('Target',f'slide{target}.xml')
        for old in obj.findall(f'{{{A}}}hlinkClick'):obj.remove(old)
        action=ET.Element(f'{{{A}}}hlinkClick');action.set(f'{{{R}}}id',rid);action.set('action','ppaction://hlinksldjump');action.set('tooltip',f'第{target}页  '+m['slides'][target-1]['title']);obj.insert(0,action)
        links.append({'shape':key,'target':target})
    groups=[]
    for prefix in d['reveals']:
        objects=[{'id':p.get('id'),'name':p.get('name')} for p in props if p.get('name','')=='!!'+prefix or p.get('name','').startswith('!!'+prefix+'.')]
        assert objects,(page,prefix)
        if page==17:
            h=by_name.get('!!clientDoc.highlight.'+prefix.split('.')[-1])
            if h is not None:objects.append({'id':h.get('id'),'name':h.get('name')})
        groups.append({'prefix':prefix,'objects':objects})
    add_morph(slide)
    targets=add_reveal(slide,groups) if groups else []
    content[sp]=ET.tostring(slide,xml_declaration=True,encoding='UTF-8',standalone=True)
    content[rp]=ET.tostring(rels,xml_declaration=True,encoding='UTF-8',standalone=True)
    nav_audit.append({'page':page,'links':links})
    effects.append({'page':page,'morph_ms':700,'groups':groups,'delays_ms':[150+550*i for i in range(len(groups))],'targets':targets})
with ZipFile(ROOT/'build/animated-candidate.pptx','w') as z:
    for entry in entries:z.writestr(entry,content[entry.filename])
(ROOT/'build/qa/navigation.json').write_text(json.dumps(nav_audit,ensure_ascii=False,indent=2))
(ROOT/'build/qa/effects.json').write_text(json.dumps(effects,ensure_ascii=False,indent=2))
print(json.dumps({'slides':33,'links':sum(len(r['links']) for r in nav_audit),'morph':33,'animated_pages':[r['page'] for r in effects if r['groups']]}))
