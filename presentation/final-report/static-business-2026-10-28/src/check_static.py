"""Independent mechanical and content-coverage checks for the static draft."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from PIL import ImageFont
import hashlib,json,re,sys
from build_static import ROOT,SOURCE,SOURCE_SHA,SPEC,NS,CM,PT,norm

FILE=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'build/candidate.pptx'
QA=ROOT/'build/qa';QA.mkdir(exist_ok=True,parents=True)
manifest=json.loads((QA/'layout-manifest.json').read_text())
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SOURCE_SHA
P=NS['p'];A=NS['a']
def local(q):return E.QName(q).localname
def geometry(q):
    f=q.find('./p:spPr/a:xfrm',NS)
    if f is None:f=q.find('./p:xfrm',NS)
    if f is None:return None
    o=f.find('./a:off',NS);e=f.find('./a:ext',NS)
    return [int(v.get(k))/CM for v,k in [(o,'x'),(o,'y'),(e,'cx'),(e,'cy')]]
def text(q):return norm(' '.join(q.xpath('.//a:t/text()',namespaces=NS)))
def url_list(b):return sorted(re.findall(r'https?://[^\s<>]+',b.decode()))
def paragraph_fit(q):
    b=q.find('./p:txBody',NS);g=geometry(q)
    if b is None or not text(b):return None
    bp=b.find('./a:bodyPr',NS);w=g[2]-sum(int(bp.get(k,'0'))/CM for k in ['lIns','rIns']);h=g[3]-sum(int(bp.get(k,'0'))/CM for k in ['tIns','bIns'])
    needed=0;count=0;maxword=0
    for p in b.findall('./a:p',NS):
        rp=p.find('.//a:rPr',NS)
        if rp is None:continue
        size=int(rp.get('sz'))/100;bold=rp.get('b')=='1'
        f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',round(size*96/72*4))
        line='';lines=1
        for word in ''.join(p.xpath('.//a:t/text()',namespaces=NS)).split():
            maxword=max(maxword,f.getlength(word)/4*2.54/96)
            test=(line+' '+word).strip()
            if line and f.getlength(test)/4*2.54/96>w:lines+=1;line=word
            else:line=test
        needed+=lines*size*2.54/72*1.20;count+=lines
    return {'estimated_lines':count,'needed_cm':round(needed,3),'available_cm':round(h,3),'height_flag_cm':round(needed-h,3),'max_word_cm':round(maxword,3),'inner_width_cm':round(w,3)}

coverage=[];errors=[];fit=[];tables=[];counts=[];caption_removals={9:{'!!trade.sequence0.label','!!trade.sequence1.label','!!trade.sequence2.label','!!trade.data.label','!!trade.ask.label','!!trade.quote.label'}}
with ZipFile(SOURCE) as zs,ZipFile(FILE) as z:
    p=E.fromstring(z.read('ppt/presentation.xml'));sz=p.find('./p:sldSz',NS)
    assert (int(sz.get('cx')),int(sz.get('cy')))==(SPEC['slide']['width_emu'],SPEC['slide']['height_emu'])
    assert len(p.findall('./p:sldIdLst/p:sldId',NS))==33
    for i in range(1,34):
        x=E.fromstring(z.read(f'ppt/slides/slide{i}.xml'));s=E.fromstring(zs.read(f'ppt/slides/slide{i}.xml'))
        assert not x.xpath('.//*[local-name()="timing" or local-name()="transition" or local-name()="morph" or local-name()="anim" or local-name()="animEffect" or local-name()="animMotion"]'),i
        assert not x.xpath('.//*[local-name()="hlinkClick" or local-name()="hlinkHover"]'),i
        assert not x.xpath('.//*[@action]'),i
        assert not x.xpath('.//p:cNvPr[@hidden="1"]',namespaces=NS),i
        rels=E.fromstring(z.read(f'ppt/slides/_rels/slide{i}.xml.rels'))
        assert not any(r.get('Type','').endswith('/slide') for r in rels),i
        whole=text(x);names=x.xpath('.//p:cNvPr/@name',namespaces=NS)
        assert not any(n.startswith(('!!nav.','!!story.header.')) or n in ['!!page','!!example'] for n in names),i
        assert not re.search(r'\b\d+\s*/\s*33\b',whole),i
        assert all(t not in ['Overview','Home','Back','Next','Start','Example'] for t in x.xpath('.//a:t/text()',namespaces=NS)),i
        title='!!cover.title' if i==1 else '!!heading';subtitle='!!cover.kicker' if i==1 else '!!subtitle'
        for q in x.find('./p:cSld/p:spTree',NS):
            g=geometry(q)
            if g is None:continue
            n=q.find('.//p:cNvPr',NS).get('name');xx,yy,w,h=g
            if n==title:zone=(SPEC['title']['x'],SPEC['title']['y'],SPEC['title']['x']+SPEC['title']['width'],SPEC['title']['bottom_limit']);assert round(yy*CM)==round(SPEC['title']['y']*CM)
            elif n==subtitle or n=='header.rule':zone=(SPEC['subtitle']['x'],SPEC['subtitle']['y'],SPEC['subtitle']['x']+SPEC['subtitle']['width'],SPEC['subtitle']['bottom_limit']);assert n=='header.rule' or round(yy*CM)==round(SPEC['subtitle']['y']*CM)
            else:zone=(SPEC['body']['x'],SPEC['body']['y'],SPEC['body']['right'],SPEC['body']['bottom'])
            if xx<zone[0]-.001 or yy<zone[1]-.001 or xx+w>zone[2]+.001 or yy+h>zone[3]+.001:errors.append({'slide':i,'name':n,'cm':g,'zone':zone})
            pf=paragraph_fit(q)
            if pf and (pf['height_flag_cm']>.12 or pf['max_word_cm']>pf['inner_width_cm']+.02):fit.append({'slide':i,'name':n,'text':text(q),**pf})
        a=s.find('.//a:tbl',NS);b=x.find('.//a:tbl',NS)
        if a is not None:
            assert b is not None and a.xpath('.//a:t/text()',namespaces=NS)==b.xpath('.//a:t/text()',namespaces=NS)
            tables.append({'slide':i,'rows':len(b.findall('./a:tr',NS)),'columns':len(b.findall('./a:tblGrid/a:gridCol',NS)),'text_and_values_preserved':True})
        note=f'ppt/notesSlides/notesSlide{i}.xml';assert url_list(zs.read(note))==url_list(z.read(note)),f'Note URLs changed on {i}'
        if i!=3:assert zs.read(note)==z.read(note),f'Notes changed on {i}'
        else:assert 'provide direct navigation' not in z.read(note).decode()
        rec={'slide':i,'reused':[],'removed_interface':[],'replaced_legacy_locator':[],'removed_redundant_connector_captions':[],'rewritten_or_omitted_business_text':[]}
        m=manifest[i-1]
        assert m['family']!='Pending redesign'
        for key,value in m['unused_text'].items():
            if key.startswith('!!story.header.') or key in ['!!page','!!example'] or key.startswith('!!nav.') and key not in ['!!nav.front','!!nav.middle','!!nav.back']:rec['removed_interface'].append({'key':key,'text':value})
            elif key.startswith(('!!nav.','!!map.','!!task.')):rec['replaced_legacy_locator'].append({'key':key,'text':value})
            elif key in caption_removals.get(i,set()):rec['removed_redundant_connector_captions'].append({'key':key,'text':value,'reason':'Action remains explicit in workflow text; duplicate connector caption removed.'})
            else:rec['rewritten_or_omitted_business_text'].append({'key':key,'text':value})
        assert not rec['rewritten_or_omitted_business_text'],rec
        for key in m['source_keys_used']:
            val=next(q for q in json.loads((ROOT/'src/source-content.json').read_text()) if q['slide']==i)['text'][key]
            assert norm(val) in whole,f'Missing reused text {i} {key}'
            rec['reused'].append({'key':key,'text':val,'method':'Verbatim words; line breaks may change.'})
        coverage.append(rec)
        counts.append({'slide':i,'editable_shapes':len(x.findall('.//p:sp',NS)),'native_connectors':len(x.findall('.//p:cxnSp',NS)),'native_tables':len(x.findall('.//a:tbl',NS)),'pictures':len(x.findall('.//p:pic',NS))})
    assert sum(q['pictures'] for q in counts)==1,'Only the original cover image should be raster'
    assert tables and tables[0]['slide']==11
assert not errors,errors
sha=hashlib.sha256(FILE.read_bytes()).hexdigest()
report={'status':'PASS','file':str(FILE),'sha256':sha,'source_sha256':SOURCE_SHA,'slide_count':33,'canvas_cm':[SPEC['slide']['width'],SPEC['slide']['height']],'canvas_emu':[SPEC['slide']['width_emu'],SPEC['slide']['height_emu']],'timing_trees':0,'transitions':0,'morph':0,'interaction_actions':0,'internal_slide_jump_relationships':0,'removed_controls_counters_and_header_tags':True,'all_objects_in_required_zones':True,'zone_violations':errors,'native_tables':tables,'research_citation_urls_preserved':True,'all_other_notes_byte_identical':True,'source_note3_change':'Obsolete direct-navigation instruction replaced with a static topic-location description.','all33_have_explicit_new_compositions':True,'copy_coverage':'src/copy-coverage.json','editability_counts':counts}
(QA/'mechanical-check.json').write_text(json.dumps(report,indent=2))
(QA/'fit-diagnostics.json').write_text(json.dumps(fit,indent=2))
(ROOT/'src/copy-coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False))
print(json.dumps({'status':report['status'],'sha256':sha,'fit_items_for_visual_review':len(fit),'geometry_violations':len(errors)},indent=2))
for f in fit:print(f['slide'],f['name'],f['height_flag_cm'])
