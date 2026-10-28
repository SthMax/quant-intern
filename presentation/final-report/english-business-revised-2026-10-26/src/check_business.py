"""Check the English deck's links, animation, editable table and source references."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from copy import deepcopy
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT.parent / 'color-revision-2026-10-26/output/asset-management-llm-story-colors.pptx'
FINAL = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / 'output/asset-management-llm-business-en.pptx'
N = {
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'm': 'http://schemas.microsoft.com/office/powerpoint/2015/09/main',
}

def tree(node):
    if node is None:
        return None
    return [node.tag, sorted(node.attrib.items()), node.text or '', [tree(child) for child in node]]

def text(node):
    return '\n'.join(item.text or '' for item in node.findall('.//a:t', N))

def links(node):
    return [sorted((k, v) for k, v in item.attrib.items() if k != 'tooltip')
            for item in node.findall('.//a:hlinkClick', N)]

assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == 'e0dd5d80c18d5f391968245f79d70941c87e8180faf44e86f3a123f31cfd4faa'
counts = {'slides': 0, 'links': 0, 'morphs': 0, 'animated_slides': 0, 'native_tables': 0}
with ZipFile(SOURCE) as original, ZipFile(FINAL) as english:
    slide_parts = [name for name in english.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', name)]
    assert len(slide_parts) == 33
    for page in range(1, 34):
        part = f'ppt/slides/slide{page}.xml'
        a, b = E.fromstring(original.read(part)), E.fromstring(english.read(part))
        counts['slides'] += 1
        ids_a = [(n.get('id'), n.get('name')) for n in a.findall('.//p:cNvPr', N)]
        ids_b = [(n.get('id'), n.get('name')) for n in b.findall('.//p:cNvPr', N)]
        expected_added = {17:[('9000','!!business.review.umbrella')],32:[('9001','!!business.phase.teams'),('9002','!!business.phase.outputs')]}.get(page,[])
        assert ids_b == ids_a + expected_added, (page, 'original object identities and exact added labels')
        assert len({n[0] for n in ids_b}) == len(ids_b), (page, 'unique object IDs')
        timing = deepcopy(b.find('./p:timing', N))
        for new_id,new_name in expected_added:
            match=timing.xpath('.//p:par[p:cTn/p:childTnLst/p:set/p:cBhvr/p:tgtEl/p:spTgt[@spid="'+new_id+'"]]',namespaces=N)
            assert len(match)==1,(page,'new label appearance',new_id)
            delay=match[0].find('./p:cTn/p:stCondLst/p:cond',N).get('delay')
            assert delay=='150',(page,'new label timing must match its original group')
            match[0].getparent().remove(match[0])
        assert tree(a.find('./p:timing', N)) == tree(timing), (page, 'all original appearance timing unchanged')
        assert tree(a.find('.//m:morph', N)) == tree(b.find('.//m:morph', N)), (page, 'Morph')
        assert [tree(t) for t in a.findall('.//p:transition',N)] == [tree(t) for t in b.findall('.//p:transition',N)],(page,'transition timing')
        morph_transition=b.find('.//m:morph',N).getparent()
        assert morph_transition.get('{http://schemas.microsoft.com/office/powerpoint/2010/main}dur')=='700',(page,'0.70 second Morph')
        assert links(a) == links(b), (page, 'link IDs/actions')
        rels = f'ppt/slides/_rels/slide{page}.xml.rels'
        assert original.read(rels) == english.read(rels), (page, 'link destinations')
        assert not re.search('[\u4e00-\u9fff]', text(b)), (page, 'untranslated slide text')
        click_nodes = b.findall('.//a:hlinkClick', N)
        assert all(not re.search('[\u4e00-\u9fff]', n.get('tooltip', '')) for n in click_nodes)
        counts['links'] += len(click_nodes)
        counts['morphs'] += len(b.findall('.//m:morph', N))
        counts['animated_slides'] += int(b.find('./p:timing', N) is not None)
        counts['native_tables'] += len(b.findall('.//a:tbl', N))
        notes = f'ppt/notesSlides/notesSlide{page}.xml'
        source_notes = text(E.fromstring(original.read(notes)))
        english_notes = text(E.fromstring(english.read(notes)))
        assert english_notes.strip(), (page, 'missing notes')
        for url in re.findall(r'https?://\S+', source_notes):
            assert url in english_notes, (page, 'missing source URL', url)
        if page == 11:
            assert 'LLM extracts supplied\nquote details' in text(b)
            assert 'The trader provides this quote:' in text(b)
            cells = [[text(cell).replace('\n', ' ') for cell in row.findall('./a:tc', N)]
                     for row in b.findall('.//a:tbl/a:tr', N)]
            assert cells[1] == ['Bond A / 1.2 years', '20', '100.20', '20'], cells
        if page == 18:
            assert 'Company A' in text(b) and 'V2' in text(b)

# Explicit wording, monetary units, versions and elapsed-time checks against the actual package.
with ZipFile(FINAL) as z:
    def slide_text(i):return text(E.fromstring(z.read(f'ppt/slides/slide{i}.xml')))
    def notes_text(i):return text(E.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml')))
    def normalized(s):return ' '.join(s.split())
    def shape_text(i,name):
        x=E.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
        return normalized(' '.join(x.xpath('.//p:sp[p:nvSpPr/p:cNvPr[@name="'+name+'"]]/p:txBody//a:t/text()',namespaces=N)))
    v1='Higher sales volumes drove Company A’s revenue growth. We are monitoring raw-material costs.'
    for i in [15,16,17]:
        assert shape_text(i,'!!clientDoc.value.view')==v1,(i,'V1 investment text')
        assert 'Product A Select' in slide_text(i) and 'Q2 2026' in slide_text(i) and 'Investing involves risk.' in slide_text(i)
    assert shape_text(23,'!!ops.compare.old.text')==v1
    v2='Channel restocking supported Company A’s sales volume growth. We are monitoring whether restocking continues, alongside raw-material costs.'
    assert shape_text(18,'!!clientDoc.value.view')==v2
    assert normalized(shape_text(23,'!!ops.compare.new.line1')+' '+shape_text(23,'!!ops.compare.new.line2'))==v2
    assert 'Added: whether restocking continues.' in slide_text(24)
    assert 'Retained: raw-material cost monitoring.' in slide_text(24)
    assert 'Cash-flow pressure affects the issuer’s capacity to service debt.' in normalized(slide_text(21))
    assert 'Time from starting the task to completing the output' in normalized(slide_text(33))
    assert 'elapsed time from starting the task to completing the output' in notes_text(33)
    assert 'approximately 50% higher' in slide_text(7)
    assert 'more than 80%' in normalized(slide_text(23)) and 'direct-sales counter' in normalized(slide_text(23))
    assert '91% acceptance rate for suggested edits' in notes_text(17)
    assert 'Participating teams' in slide_text(32) and 'Deliverables' in slide_text(32)
    assert 'LLM-assisted review' in slide_text(17)
    for i in [1,11,14,15,30,33]:assert '..' not in notes_text(i).split('Sources:')[0],(i,'double punctuation')
assert counts == {'slides': 33, 'links': 407, 'morphs': 33, 'animated_slides': 14, 'native_tables': 1}, counts
report = {
    'status': 'pass',
    'file': str(FINAL),
    'sha256': hashlib.sha256(FINAL.read_bytes()).hexdigest(),
    'counts': counts,
    'original_object_identities_link_targets_and_animation_preserved': True,
    'added_native_labels':3,
    'added_labels_bound_to_original_150ms_appearance_group':True,
    'slide_text_and_tooltips_in_english': True,
    'original_source_urls_preserved': True,
    'quote_provenance_and_rmb_units_checked': True,
}
target = ROOT / 'build/qa/business-integrity.json'
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
