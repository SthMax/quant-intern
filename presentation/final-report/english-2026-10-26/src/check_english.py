"""Check the English deck's links, animation, editable table and source references."""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as E
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT.parent / 'color-revision-2026-10-26/output/asset-management-llm-story-colors.pptx'
FINAL = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / 'output/asset-management-llm-interactive-en.pptx'
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
        assert ids_a == ids_b, (page, 'object identities')
        assert tree(a.find('./p:timing', N)) == tree(b.find('./p:timing', N)), (page, 'animation')
        assert tree(a.find('.//m:morph', N)) == tree(b.find('.//m:morph', N)), (page, 'Morph')
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
            assert 'LLM parses quote records' in text(b)
            assert 'The trader provides this quote:' in text(b)
            cells = [[text(cell).replace('\n', ' ') for cell in row.findall('./a:tc', N)]
                     for row in b.findall('.//a:tbl/a:tr', N)]
            assert cells[1] == ['Bond A / 1.2 years', '20', '100.20', '20'], cells
        if page == 18:
            assert 'Company A' in text(b) and 'V2' in text(b)

assert counts == {'slides': 33, 'links': 407, 'morphs': 33, 'animated_slides': 14, 'native_tables': 1}, counts
report = {
    'status': 'pass',
    'file': str(FINAL),
    'sha256': hashlib.sha256(FINAL.read_bytes()).hexdigest(),
    'counts': counts,
    'object_identities_link_targets_and_animation_preserved': True,
    'slide_text_and_tooltips_in_english': True,
    'original_source_urls_preserved': True,
    'quote_provenance_and_rmb_units_checked': True,
}
target = ROOT / 'build/qa/english-integrity.json'
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
