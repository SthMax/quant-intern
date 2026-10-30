"""Package, measured geometry, static, evidence and provenance checks."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import hashlib,json,re,posixpath,sys
from native import *
from build_streamlined import SOURCE,SHA,PLAN,BASE,INPUTS,OLD_NOTES,APPROVED,notes_body

FILE=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'build/candidate.pptx'
QA=ROOT/'build/qa';QA.mkdir(exist_ok=True,parents=True)
NOTES=json.loads((ROOT/'src/speaker-notes.json').read_text())
def txt(x):return norm(' '.join(x.xpath('.//a:t/text()',namespaces=NS)))
def geometry(s):
    x=s.find('./p:spPr/a:xfrm',NS)
    if x is None:x=s.find('./p:xfrm',NS)
    if x is None:return None
    o=x.find('./a:off',NS);e=x.find('./a:ext',NS)
    return [int(v.get(k))/CM for v,k in [(o,'x'),(o,'y'),(e,'cx'),(e,'cy')]]
def shape_name(s):
    x=s.find('.//p:cNvPr',NS);return x.get('name','') if x is not None else ''

assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SHA
violations=[];counts=[];footnotes=[];texts={};coverage=[]
with ZipFile(FILE) as z,ZipFile(SOURCE) as old:
    names=set(z.namelist());pr=E.fromstring(z.read('ppt/presentation.xml'));sz=pr.find('./p:sldSz',NS)
    assert [int(sz.get(a)) for a in ['cx','cy']]==[SPEC['slide']['width_emu'],SPEC['slide']['height_emu']]
    assert len(pr.findall('./p:sldIdLst/p:sldId',NS))==28
    assert len([v for v in names if re.match(r'ppt/slides/slide\d+\.xml$',v)])==28
    for name in sorted(names):
        if not name.endswith(('.xml','.rels')):continue
        x=E.fromstring(z.read(name))
        if name.startswith('ppt/'):
            assert not x.xpath('.//*[local-name()="timing" or local-name()="transition" or local-name()="morph" or local-name()="hlinkClick" or local-name()="hlinkMouseOver" or local-name()="hlinkHover"]'),name
            assert not x.xpath('.//*[@action]'),name
        if name.endswith('.rels'):
            owner='' if name=='_rels/.rels' else name.replace('/_rels/','/').removesuffix('.rels')
            for r in x:
                if r.get('TargetMode')=='External':continue
                target=r.get('Target','');dest=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(owner),target))
                assert dest in names,(name,target,dest)
    for i in range(1,29):
        x=E.fromstring(z.read(f'ppt/slides/slide{i}.xml'));whole=texts[i]=txt(x)
        ids=x.xpath('.//p:cNvPr/@id',namespaces=NS);assert len(ids)==len(set(ids)),i
        assert 'Company workflow' not in whole
        assert not any(t in ['Overview','Home','Back','Next','Start','Example'] for t in x.xpath('.//a:t/text()',namespaces=NS))
        assert not re.search(r'\b\d+\s*/\s*(28|33)\b',whole)
        ss=x.find('./p:cSld/p:spTree',NS)
        nn=[shape_name(s) for s in ss]
        for s in ss:
            name=shape_name(s);g=geometry(s)
            if g is None:continue
            xx,yy,ww,hh=g
            if name=='title':
                zone=[1.27,2.00,24.13,3.00]
                assert txt(s)==PLAN[i-1]['title'] and abs(yy-2.0)<.00001 and abs(hh-.95)<.00001
                assert set(s.xpath('.//a:rPr/@sz',namespaces=NS))=={'2400'}
                assert set(s.xpath('.//a:rPr/@b',namespaces=NS))=={'1'}
            elif name=='subtitle':
                zone=[1.27,3.00,24.13,3.92]
                assert txt(s)==PLAN[i-1]['subtitle'] and abs(yy-3.0)<.00001 and abs(hh-.75)<.00001
                assert set(s.xpath('.//a:rPr/@sz',namespaces=NS))=={'1600'}
                assert set(s.xpath('.//a:rPr/a:solidFill/a:srgbClr/@val',namespaces=NS))=={BLUE}
            elif name=='source.note':
                zone=[1.27,13.01,24.13,13.55]
                assert set(s.xpath('.//a:rPr/@sz',namespaces=NS))=={'800'}
                assert len(s.findall('./p:txBody/a:p',NS))==1
                assert width(txt(s),8)<=ww+.01,(i,'footnote width')
                footnotes.append({'slide':i,'text':txt(s),'cm':g,'pt':8,'single_line':True})
            else:zone=[1.27,3.92,24.13,13.01]
            if xx<zone[0]-.001 or yy<zone[1]-.001 or xx+ww>zone[2]+.001 or yy+hh>zone[3]+.001:violations.append({'slide':i,'name':name,'cm':g,'zone':zone})
            for f in s.xpath('.//a:latin/@typeface | .//a:ea/@typeface | .//a:cs/@typeface',namespaces=NS):assert f=='Arial',(i,name,f)
        if i not in [1,3,22]:
            tasks=[v for v in nn if v.startswith('map.task.') and not v.startswith('map.task.focus.')]
            assert len(tasks)==6,(i,tasks)
            assert not any('.review' in v for v in tasks)
            focus={v.removeprefix('map.task.focus.') for v in nn if v.startswith('map.task.focus.')}
            if i in [2,24]:assert focus=={'research','trade','client','risk','records','dev'},(i,focus)
            if i==25:assert focus=={'research','client'},(i,focus)
        if i in [3,22]:assert len([v for v in nn if v.startswith('firm.task.')])==6
        tab=x.find('.//a:tbl',NS)
        if i==10:
            assert tab is not None
            src=E.fromstring(old.read('ppt/slides/slide11.xml')).find('.//a:tbl',NS)
            assert tab.xpath('.//a:t/text()',namespaces=NS)==src.xpath('.//a:t/text()',namespaces=NS)
        else:assert tab is None
        body=notes_body(E.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml')))
        actual='\n'.join(''.join(p.xpath('.//a:t/text()',namespaces=NS)) for p in body.findall('./a:p',NS))
        assert actual==NOTES[i-1]['full_notes'] and NOTES[i-1]['narration'].strip(),i
        assert actual.startswith('Suggested spoken explanation\n')
        counts.append({'slide':i,'text_shapes':len(x.findall('.//p:sp',NS)),'native_connectors':len(x.findall('.//p:cxnSp',NS)),'native_tables':len(x.findall('.//a:tbl',NS)),'pictures':len(x.findall('.//p:pic',NS))})
        records=[]
        for orig in INPUTS[i-1]:
            keys=[]
            for key,val in APPROVED[orig-1]['text'].items():
                if key.startswith(('!!nav.','!!story.header.')) or key in ['!!page','!!example']:where='requested interface removal or six-section map reexpression'
                elif norm(val) in whole:where='visible verbatim'
                elif norm(val) in norm(actual):where='notes verbatim'
                else:where='condensed/merged; complete approved source record retained'
                keys.append({'source_key':key,'disposition':where})
            records.append({'original_page':orig,'source_keys':keys})
        coverage.append({'slide':i,'original_pages':INPUTS[i-1],'sources':records})
assert not violations,violations
assert sum(x['pictures'] for x in counts)==1
assert sum(x['native_tables'] for x in counts)==1
def need(i,*vv):
    for v in vv:assert norm(v).casefold() in texts[i].casefold(),(i,v)
for i in [4,7]:need(i,'Prior / current quarter','Revenue','RMB m','Sales volume','m units','100 / 110','1.0 / 1.1')
need(7,'Revenue +10%','Sales volume +10%','Average price unchanged','uncertain')
need(10,'Quote from trader','100.20','RMB 20m face','Current holding','Available size','per RMB 100 face value','Bond A / 1.2 years')
need(13,'Higher sales volumes drove Company A’s revenue growth. We are monitoring raw-material costs.','Channel restocking supported Company A’s sales volume growth. We are monitoring whether restocking continues, alongside raw-material costs.','Q2 product source','Q3 product source','Document tools','Match passages','LLM revises','Middle office checks')
assert 'Company A' not in texts[12] and 'V1' not in texts[12] and 'V2' not in texts[12]
need(18,'HuaAn','Direct-sales counter: more than 80% of faxes entered automatically','Proposed application','Operations','Business record')
need(26,'Approximately 50% higher','Research-preparation efficiency','May 2026')
need(28,'patent proposal','Algorithms','Quantify contributions')
for v in ['Product A Select','Q2 2026 product information, V1','Investing involves risk.','Product A Select Mixed-Asset Fund','Q3 2026 product information, V2','The fund’s NAV fluctuates with market conditions. Capital is at risk.']:assert v in norm(NOTES[12]['full_notes']),v
all_old_urls=set(v for r in OLD_NOTES for v in r['source_urls']);all_new_urls=set(v for r in NOTES for v in r['source_urls'])
assert all_old_urls==all_new_urls,(all_old_urls-all_new_urls,all_new_urls-all_old_urls)
assert 'Yingmi' in NOTES[11]['full_notes'] and 'repeat review' in NOTES[11]['full_notes']
assert 'Qwen' in NOTES[23]['full_notes'] and 'DeepSeek' in NOTES[23]['full_notes'] and 'candidates' in NOTES[23]['full_notes']
assert set(v for ss in INPUTS for v in ss)==set(range(1,34))
sha=hashlib.sha256(FILE.read_bytes()).hexdigest()
report={'status':'PASS','file':str(FILE),'sha256':sha,'source_sha256':SHA,'slides':28,'main_slides':25,'appendix_slides':3,'canvas_emu':[9144000,5140800],'title_pt':24,'subtitle_pt':16,'source_footnote_pt':8,'source_footnote_above_rule_cm':13.55,'geometry_violations':violations,'static_actions_transitions_timing':0,'section_maps':6,'native_table_slide':10,'native_table_text_units_preserved':True,'notes_match_json':True,'source_url_coverage':'all original URLs retained','complete_source_pages_accounted_for':33,'footnotes':footnotes,'editability':counts,'native_powerpoint_verification':'not performed'}
(QA/'mechanical-check.json').write_text(json.dumps(report,indent=2)+'\n')
(ROOT/'src/content-coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:report[k] for k in ['status','sha256','slides','main_slides','appendix_slides','geometry_violations']},indent=2))
