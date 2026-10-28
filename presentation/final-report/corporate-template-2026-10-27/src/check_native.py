"""Strict source-to-candidate preservation and measured-zone checks."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import hashlib,json,re,sys
from adapt_native import NS,CM,PT,ROOT,SOURCE,SOURCE_SHA,SPEC,TITLE,SUBTITLE,BODY,geom,xf,nv,name,text,estimate,local

CANDIDATE=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'build/candidate.pptx'
QA=ROOT/'build/qa';QA.mkdir(exist_ok=True)
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SOURCE_SHA,'Approved source baseline changed'
def canon(x):return E.tostring(x,method='c14n') if x is not None else None
def norm(t):return ' '.join(t.split())
def items(root):return [s for s in root.find('./p:cSld/p:spTree',NS) if xf(s) is not None]
def sig(root):return [(nv(s).get('id'),name(s),local(s)) for s in items(root)]
def links(root):return [canon(x) for x in root.findall('.//a:hlinkClick',NS)]
def palette(root):return sorted(set(root.xpath('.//a:srgbClr/@val',namespaces=NS)))
checks=[];zones=[];fonts=set();line_widths=set();table_info=[];slides=[];textdiff=[];links_total=0;morph=0;timing=0;added=[];pictures=[];selection=[]
with ZipFile(SOURCE) as zs,ZipFile(CANDIDATE) as zc:
    assert set(zs.namelist())==set(zc.namelist()),'Package parts differ'
    changed=[n for n in zs.namelist() if zs.read(n)!=zc.read(n)]
    assert all(re.fullmatch(r'ppt/slides/slide\d+\.xml',n) or n=='ppt/presentation.xml' for n in changed)
    presentation=E.fromstring(zc.read('ppt/presentation.xml'))
    sz=presentation.find('./p:sldSz',NS)
    assert (int(sz.get('cx')),int(sz.get('cy')))==(SPEC['slide']['width_emu'],SPEC['slide']['height_emu'])
    assert len(presentation.findall('./p:sldIdLst/p:sldId',NS))==33
    for i in range(1,34):
        part=f'ppt/slides/slide{i}.xml';s=E.fromstring(zs.read(part));c=E.fromstring(zc.read(part))
        assert sig(s)==sig(c),f'Slide {i} IDs/names/types changed'
        assert links(s)==links(c),f'Slide {i} hyperlink XML changed'
        assert palette(s)==palette(c),f'Slide {i} color semantics changed'
        for tag in ['transition','timing']:
            assert [canon(q) for q in s.findall('.//p:'+tag,NS)]==[canon(q) for q in c.findall('.//p:'+tag,NS)],f'Slide {i} {tag} changed'
        transitions=c.findall('.//p:transition',NS)
        assert any(q.get('{http://schemas.microsoft.com/office/powerpoint/2010/main}dur')=='700' and q.xpath('./*[local-name()="morph"]') for q in transitions)
        links_total+=len(links(c));morph+=bool(c.xpath('.//*[local-name()="morph"]'));timing+=c.find('./p:timing',NS) is not None
        originals={nv(q).get('id'):q for q in items(s)}
        selected={'slide':i,'title':[],'subtitle':[],'body':[],'exclude_from_body_transfer':[]}
        for q in items(c):
            ident=nv(q).get('id');n=name(q);source=originals[ident]
            ts=norm(' '.join(source.xpath('.//a:t/text()',namespaces=NS)));tc=norm(' '.join(q.xpath('.//a:t/text()',namespaces=NS)))
            if ts!=tc:textdiff.append({'slide':i,'id':ident,'name':n,'source':ts,'candidate':tc})
            assert palette(source)==palette(q),f'Slide {i} {n} color changed'
            x,y,w,h=geom(q)
            if n in ['!!heading','!!cover.title']:
                zone=(TITLE['x'],TITLE['y'],TITLE['x']+TITLE['width'],TITLE['bottom_limit']);kind='title'
                assert round(y*CM)==round(TITLE['y']*CM)
            elif n in ['!!subtitle','!!cover.kicker','!!heading.rule']:
                zone=(SUBTITLE['x'],SUBTITLE['y'],SUBTITLE['x']+SUBTITLE['width'],SUBTITLE['bottom_limit']);kind='subtitle'
                if n!='!!heading.rule':assert round(y*CM)==round(SUBTITLE['y']*CM)
            else:zone=BODY;kind='body'
            selection_key='exclude_from_body_transfer' if n in ['!!cover.white','!!heading.rule'] else kind
            selected[selection_key].append({'id':ident,'name':n,'kind':local(q)})
            if x<zone[0]-.001 or y<zone[1]-.001 or x+w>zone[2]+.001 or y+h>zone[3]+.001:
                zones.append({'slide':i,'id':ident,'name':n,'zone':kind,'cm':[round(v,4) for v in [x,y,w,h]],'allowed':zone})
            for v in q.xpath('.//a:rPr/@sz',namespaces=NS):
                v=int(v)/100;fonts.add(v);assert v*2==round(v*2),f'Fractional font on {i} {n}: {v}'
            for line in q.iter():
                if local(line) in ['ln','lnL','lnR','lnT','lnB','lnTlToBr','lnBlToTr'] and line.get('w') and int(line.get('w'))>0:
                    points=int(line.get('w'))/PT;line_widths.add(points)
                    assert points*2==round(points*2),f'Line width outside 0.5 pt grid on {i} {n}: {points}'
            for bp in q.findall('./p:txBody/a:bodyPr',NS):
                assert sum(int(bp.get(k,'0')) for k in ['lIns','rIns'])<round(w*CM)
                assert sum(int(bp.get(k,'0')) for k in ['tIns','bIns'])<round(h*CM)
            if int(ident)>=9000:added.append({'slide':i,'id':ident,'name':n})
            if local(q)=='pic':
                sx,sy,sw,sh=geom(source);ratio=(w/h)/(sw/sh)
                pictures.append({'slide':i,'id':ident,'aspect_ratio_change':ratio-1})
                assert abs(ratio-1)<.001,'Image aspect changed'
            table=q.find('.//a:tbl',NS)
            if table is not None:
                columns=[int(t.get('w'))/CM for t in table.findall('./a:tblGrid/a:gridCol',NS)]
                rows=[int(t.get('h'))/CM for t in table.findall('./a:tr',NS)]
                assert abs(sum(columns)-w)<.002
                assert abs(sum(rows)-h)<.002
                for rr,row in enumerate(table.findall('./a:tr',NS)):
                    for cc,cell in enumerate(row.findall('./a:tc',NS)):
                        cp=cell.find('./a:tcPr',NS)
                        if cp is not None:
                            assert sum(int(cp.get(k,'0'))/CM for k in ['marL','marR'])<columns[cc]
                            assert sum(int(cp.get(k,'0'))/CM for k in ['marT','marB'])<rows[rr]
                table_info.append({'slide':i,'rows':len(rows),'columns':len(columns),'editable':True,'column_widths_cm':columns,'row_heights_cm':rows})
        slides.append({'slide':i,'objects':len(items(c)),'internal_links':len(links(c)),'timing_unchanged':True,'transition_unchanged':True,'identities_unchanged':True,'approved_text_unchanged':not any(d['slide']==i for d in textdiff)})
        selection.append(selected)
assert not textdiff,textdiff
assert links_total==407,links_total
assert morph==33,morph
assert timing==14,timing
assert not zones,zones
assert [t['slide'] for t in table_info]==[11]
report={'status':'PASS','source':str(SOURCE),'source_sha256':SOURCE_SHA,'candidate':str(CANDIDATE),'candidate_sha256':hashlib.sha256(CANDIDATE.read_bytes()).hexdigest(),'canvas_cm':[SPEC['slide']['width'],SPEC['slide']['height']],'canvas_emu':[SPEC['slide']['width_emu'],SPEC['slide']['height_emu']],'slides':33,'shape_id_name_type_preservation':True,'internal_links':407,'exact_link_xml_and_destinations_preserved':True,'morph_transitions':33,'morph_ms':700,'appearance_slides':14,'timing_xml_preserved':True,'unchanged_notes_and_relationship_parts':True,'approved_text_normalized_equal':True,'wording_changes':[],'font_points':sorted(fonts),'native_tables':table_info,'added_business_labels_preserved':added,'images':pictures,'slide_details':slides,'changed_package_parts':changed}
(QA/'interaction-content-report.json').write_text(json.dumps(report,indent=2))
(QA/'geometry-report.json').write_text(json.dumps({'status':'PASS','canvas_cm':report['canvas_cm'],'canvas_emu':report['canvas_emu'],'specification':str(ROOT/'layout-spec.json'),'exact_title_and_subtitle_tops':True,'all_objects_within_required_zones':True,'violations':zones,'table_dimensions_consistent':True,'text_insets_within_shape':True,'font_size_grid':'0.5 pt','font_points':sorted(fonts),'image_aspect_ratio_preserved':True,'line_width_grid':'0.5 pt','actual_positive_line_widths_pt':sorted(line_widths),'declared_exceptions':[]},indent=2))
(QA/'transfer-selection-manifest.json').write_text(json.dumps(selection,indent=2))
(ROOT/'src/transfer-selection-manifest.json').write_text(json.dumps(selection,indent=2))
print(json.dumps({k:report[k] for k in ['status','candidate_sha256','slides','internal_links','morph_transitions','appearance_slides','font_points']},indent=2))
