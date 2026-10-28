"""Static/geometry/evidence/notes checks; visual mechanism review is separate."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from PIL import ImageFont
import json,hashlib,re,sys
from native import *
from build_visual import SOURCE,SHA,APPROVED,notes_body

FILE=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'build/candidate.pptx'
QA=ROOT/'build/qa';QA.mkdir(exist_ok=True,parents=True)
MNF=json.loads((QA/'layout-manifest.json').read_text())
NOTES=json.loads((ROOT/'src/speaker-notes.json').read_text())
def local(q):return E.QName(q).localname
def txt(q):return norm(' '.join(q.xpath('.//a:t/text()',namespaces=NS)))
def geom(q):
    f=q.find('./p:spPr/a:xfrm',NS)
    if f is None:f=q.find('./p:xfrm',NS)
    if f is None:return None
    o=f.find('./a:off',NS);e=f.find('./a:ext',NS)
    return [int(v.get(k))/CM for v,k in [(o,'x'),(o,'y'),(e,'cx'),(e,'cy')]]
def urlset(s):return sorted(set(re.findall(r'https?://[^\s]+',s)))
def fitted(q):
    b=q.find('./p:txBody',NS);g=geom(q)
    if b is None or not txt(b):return None
    bp=b.find('./a:bodyPr',NS);ww=g[2]-sum(int(bp.get(k,'0'))/CM for k in ['lIns','rIns']);hh=g[3]-sum(int(bp.get(k,'0'))/CM for k in ['tIns','bIns'])
    need=0;lines=0;mw=0
    for p in b.findall('./a:p',NS):
        r=p.find('.//a:rPr',NS)
        if r is None:continue
        size=int(r.get('sz','1200'))/100;bold=r.get('b')=='1';f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',round(size*96/72*4))
        line='';nn=1
        for word in ''.join(p.xpath('.//a:t/text()',namespaces=NS)).split():
            mw=max(mw,f.getlength(word)/4*2.54/96);s=(line+' '+word).strip()
            if line and f.getlength(s)/4*2.54/96>ww:nn+=1;line=word
            else:line=s
        need+=nn*size*2.54/72*1.16;lines+=nn
    return {'lines':lines,'estimated_cm':round(need,3),'available_cm':round(hh,3),'overflow_cm':round(need-hh,3),'max_word_cm':round(mw,3),'inner_width_cm':round(ww,3)}

assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SHA
assert all(p['family']!='Pending' for p in MNF)
assert all(n['narration'].strip() for n in NOTES)
for n in NOTES:
    for bad in ['rather than organizing','the lines do not imply','The smaller map','The plain branch','there is no LLM actor','The two lanes keep','The diagram keeps','The neutral edge markers','The highlighted investment','The sample labels']:
        assert bad not in n['narration'],(n['slide'],bad)

zones=[];fit=[];counts=[];coverage=[];tables=[];page_text={};maps=[]
with ZipFile(SOURCE) as old,ZipFile(FILE) as z:
    root=E.fromstring(z.read('ppt/presentation.xml'));sz=root.find('./p:sldSz',NS)
    assert (int(sz.get('cx')),int(sz.get('cy')))==(SPEC['slide']['width_emu'],SPEC['slide']['height_emu'])
    assert len(root.findall('./p:sldIdLst/p:sldId',NS))==33
    for part in z.namelist():
        if part.startswith('ppt/') and part.endswith('.xml'):
            q=E.fromstring(z.read(part))
            assert not q.xpath('.//*[local-name()="timing" or local-name()="transition" or local-name()="morph" or local-name()="hlinkClick" or local-name()="hlinkMouseOver" or local-name()="hlinkHover"]'),part
            assert not q.xpath('.//*[@action]'),part
    for i in range(1,34):
        part=f'ppt/slides/slide{i}.xml';x=E.fromstring(z.read(part));source=E.fromstring(old.read(part));page_text[i]=whole=txt(x)
        names=x.xpath('.//p:cNvPr/@name',namespaces=NS)
        assert not any(n.startswith(('!!nav.','!!story.header.')) or n in ['!!page','!!example'] for n in names)
        assert not re.search(r'\b\d+\s*/\s*33\b',whole)
        assert not any(t in ['Overview','Home','Back','Next','Start','Example'] for t in x.xpath('.//a:t/text()',namespaces=NS))
        assert not x.xpath('.//p:cNvPr[@hidden="1"]',namespaces=NS)
        rels=E.fromstring(z.read(f'ppt/slides/_rels/slide{i}.xml.rels'));assert not any(r.get('Type','').endswith('/slide') for r in rels)
        ids=x.xpath('.//p:cNvPr/@id',namespaces=NS);assert len(ids)==len(set(ids)),i
        for s in x.find('./p:cSld/p:spTree',NS):
            g=geom(s)
            if g is None:continue
            name=s.find('.//p:cNvPr',NS).get('name');xx,yy,ww,hh=g
            if name=='title':
                zone=(1.27,2.0,24.13,3.0);assert round(yy*CM)==cm(2.0) and round(hh*CM)==cm(.95)
                assert set(s.xpath('./p:txBody//a:rPr/@sz',namespaces=NS))=={'2400'}
            elif name=='subtitle':
                zone=(1.27,3.0,24.13,3.92);assert round(yy*CM)==cm(3.0) and round(hh*CM)==cm(.75)
                assert set(s.xpath('./p:txBody//a:rPr/@sz',namespaces=NS))=={'1600'}
                assert set(s.xpath('./p:txBody//a:rPr/a:solidFill/a:srgbClr/@val',namespaces=NS))=={BLUE}
            else:zone=(1.27,3.92,24.13,13.01)
            if xx<zone[0]-.001 or yy<zone[1]-.001 or xx+ww>zone[2]+.001 or yy+hh>zone[3]+.001:zones.append({'slide':i,'name':name,'cm':g,'allowed':zone})
            f=fitted(s)
            if f and (f['overflow_cm']>.15 or f['max_word_cm']>f['inner_width_cm']+.02):fit.append({'slide':i,'name':name,'text':txt(s),**f})
        if i not in [1,3,29]:
            tasknames=[n for n in names if n.startswith('map.task.') and not n.startswith('map.task.focus.')]
            assert len(tasknames)==7,(i,tasknames)
            assert len([n for n in names if n.startswith('map.office.') and not n.startswith('map.office.rule.')])==3
            maps.append({'slide':i,'offices':3,'tasks':7,'current_context_visible':True})
        source_table=source.find('.//a:tbl',NS);table=x.find('.//a:tbl',NS)
        if source_table is not None:
            assert table is not None
            assert source_table.xpath('.//a:t/text()',namespaces=NS)==table.xpath('.//a:t/text()',namespaces=NS)
            frame=x.find('.//p:graphicFrame',NS);gg=geom(frame)
            cols=[int(c.get('w'))/CM for c in table.findall('./a:tblGrid/a:gridCol',NS)];rows=[int(r.get('h'))/CM for r in table.findall('./a:tr',NS)]
            assert abs(sum(cols)-gg[2])<.001 and abs(sum(rows)-gg[3])<.001
            tables.append({'slide':i,'rows':len(rows),'columns':len(cols),'editable':True,'text_values_units_preserved':True,'column_widths_cm':cols,'row_heights_cm':rows})
        np=f'ppt/notesSlides/notesSlide{i}.xml';original_note='\n'.join(''.join(q.xpath('.//a:t/text()',namespaces=NS)) for q in notes_body(E.fromstring(old.read(np))).findall('./a:p',NS))
        body=notes_body(E.fromstring(z.read(np)));actual='\n'.join(''.join(q.xpath('.//a:t/text()',namespaces=NS)) for q in body.findall('./a:p',NS))
        assert actual==NOTES[i-1]['full_notes'],i
        assert urlset(original_note)==urlset(actual),(i,urlset(original_note),urlset(actual))
        assert NOTES[i-1]['narration'].strip(),(i,'Missing spoken explanation')
        account=[]
        for key,value in APPROVED[i-1]['text'].items():
            nv=norm(value)
            if key.startswith('!!nav.') and key not in ['!!nav.front','!!nav.middle','!!nav.back'] or key.startswith('!!story.header.') or key in ['!!page','!!example']:mode='requested_interface_removal'
            elif key.startswith(('!!nav.','!!task.','!!map.')):mode='architecture_or_recurring_object_reexpressed'
            elif nv in whole:mode='on_screen_verbatim'
            elif nv in norm(actual):mode='speaker_notes_verbatim'
            else:mode='condensed_visual_or_spoken_explanation; full_approved_record_retained'
            account.append({'source_key':key,'disposition':mode,'complete_record':'src/approved-content.json#slide-'+str(i)})
        coverage.append({'slide':i,'discussion_page':i,'mechanism':MNF[i-1]['family'],'source_keys':account,'narration_words':len(NOTES[i-1]['narration'].split()),'supporting_passages':len(NOTES[i-1]['supporting_wording']),'source_urls':NOTES[i-1]['source_urls']})
        counts.append({'slide':i,'text_shapes':len(x.findall('.//p:sp',NS)),'native_connectors':len(x.findall('.//p:cxnSp',NS)),'native_tables':len(x.findall('.//a:tbl',NS)),'pictures':len(x.findall('.//p:pic',NS))})
    assert sum(q['pictures'] for q in counts)==1 and tables[0]['slide']==11

assert not zones,zones
def need(i,*values):
    s=page_text[i].casefold()
    for v in values:assert norm(v).casefold() in s,(i,'Missing visible evidence',v)
for i in [4,8]:need(i,'Prior / current quarter','Revenue','RMB m','Sales volume','m units','100 / 110','1.0 / 1.1')
need(8,'[1]','[2]','[3]','Revenue +10%','Sales volume +10%','Average price unchanged','uncertain')
need(9,'Portfolio manager','Trader','Market / holdings systems','Counterparty','Query','Bonds + holdings','Request offers','Offer quotes','Bond / quote summary','within two years')
need(11,'Quote from trader','100.20','RMB 20m face','Current holding','Available size','per RMB 100 face value','Bond A / 1.2 years')
v1='Higher sales volumes drove Company A’s revenue growth. We are monitoring raw-material costs.'
v2='Channel restocking supported Company A’s sales volume growth. We are monitoring whether restocking continues, alongside raw-material costs.'
for i in [15,16,23]:need(i,v1)
for i in [18,23]:need(i,v2)
need(7,'Approximately 50% higher','Research-preparation efficiency','May 2026')
need(23,'Direct-sales counter: more than 80% of faxes entered automatically','Comparison result','Existing V1','Existing V2')
need(28,'patent proposal','Algorithms','Quantify contributions')
for phrase in ['Product A Select','Q2 2026 product information, V1','Investing involves risk.']:assert phrase in NOTES[14]['full_notes']
for phrase in ['Product A Select Mixed-Asset Fund','Q3 2026 product information, V2','The fund’s NAV fluctuates with market conditions. Capital is at risk.']:assert phrase in norm(NOTES[17]['full_notes'])

sha=hashlib.sha256(FILE.read_bytes()).hexdigest()
report={'status':'PASS','file':str(FILE),'sha256':sha,'source_sha256':SHA,'slides':33,'canvas_cm':[25.40,14.28],'canvas_emu':[9144000,5140800],'title_pt':24,'subtitle_pt':16,'title_top_cm':2.0,'subtitle_top_cm':3.0,'title_height_cm':.95,'subtitle_height_cm':.75,'timing':0,'transitions':0,'morph':0,'click_hover_actions':0,'internal_slide_jumps':0,'controls_counters_detached_tags':0,'geometry_violations':zones,'native_tables':tables,'company_maps':maps,'speaker_notes_match_source_json':True,'all_original_source_urls_preserved':True,'visible_critical_evidence_checks':True,'source_key_coverage':'src/content-coverage.json','complete_approved_records':'src/approved-content.json','complete_original_notes_archive':'src/source-notes.json','editability':counts,'text_fit_diagnostic_count':len(fit),'visual_semantics_review':'PAGE-DISCUSSION.md and FINAL-REVIEW.md; not certified by mechanical checks'}
(QA/'mechanical-check.json').write_text(json.dumps(report,indent=2))
(QA/'fit-diagnostics.json').write_text(json.dumps(fit,indent=2,ensure_ascii=False))
(ROOT/'src/content-coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False))
mapping=[]
for i,p in enumerate(MNF,1):
    mapping.append({'slide':i,'discussion_reference':f'PAGE-DISCUSSION.md page{i}',
        'visible_mechanism':p['family'],
        'see':[{'name':q['name'],'text':q.get('text',''),'kind':q['kind']} for q in p['items'] if not q['name'].startswith(('map.','source.note','title','subtitle'))],
        'say':NOTES[i-1]['narration'],'supporting_passages':NOTES[i-1]['supporting_wording'],
        'source_urls':NOTES[i-1]['source_urls'],'custom_spans':p['custom_spans'],
        'source_key_dispositions':coverage[i-1]['source_keys']})
(ROOT/'src/implementation-mapping.json').write_text(json.dumps(mapping,indent=2,ensure_ascii=False))
print(json.dumps({'status':report['status'],'sha256':sha,'fit_diagnostics':len(fit),'geometry_violations':len(zones)},indent=2))
for q in fit:print(q['slide'],q['name'],q['overflow_cm'])
