"""Check the generated PDF and the provenance of its presentation values."""
import hashlib
import json
import re
from pathlib import Path
import pdfplumber
from pypdf import PdfReader
ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
PDF = ROOT / 'output/week4-deployment-options.pdf'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads((ROOT / 'data/source-manifest.json').read_text())
for file, info in manifest['sources'].items():
    assert sha(REPO / file) == info['sha256'], file
slides = (ROOT / 'slides.tex').read_text()
keys = set(re.findall(r'\\V\{([^}]+)\}', slides))
assert keys <= set(manifest['figures'])
reader = PdfReader(PDF)
assert len(reader.pages) == 16
assert '本地大模型部署方案' in str(reader.metadata.get('/Title', ''))
assert reader.metadata.get('/Author') == 'Intern research'
checks = []
all_text = []
with pdfplumber.open(PDF) as pdf:
    for number, page in enumerate(pdf.pages, 1):
        text = page.extract_text() or ''
        all_text.append(text)
        compact = re.sub(r'\s+', '', text)
        if number in [3,4,5]: assert '场景1' in compact
        if number in [6,7,8]: assert '场景2' in compact
        if number in [9,10,11]: assert '场景3' in compact
        if number >= 13: assert '附录' in compact
        assert abs(page.width / page.height - 16/9) < 0.001
        chars = [c for c in page.chars if c['text'].strip()]
        outside = [c['text'] for c in chars if c['x0'] < -1 or c['x1'] > page.width + 1 or c['top'] < -1 or c['bottom'] > page.height + 1]
        overlaps = []
        for i,c in enumerate(chars):
            area = (c['x1']-c['x0'])*(c['bottom']-c['top'])
            if area <= 0: continue
            for d in chars[i+1:]:
                iw = min(c['x1'],d['x1']) - max(c['x0'],d['x0'])
                ih = min(c['bottom'],d['bottom']) - max(c['top'],d['top'])
                if iw <= 0 or ih <= 0: continue
                other = (d['x1']-d['x0'])*(d['bottom']-d['top'])
                if other > 0 and iw*ih/min(area,other) > 0.30:
                    overlaps.append({'text':c['text']+d['text'], 'x':round(c['x0'],1),'y':round(c['top'],1)})
        assert not outside, (number, outside)
        checks.append({'page':number,'characters':len(text),'outside_page':outside,'possible_character_overlaps':overlaps})
joined = '\n'.join(all_text)
assert 'Qwen3.6' not in joined and 'Qwen35' not in joined and '35B' not in joined and '4-bit' not in joined
assert 'FP8' in joined and 'BF16' in joined
assert 'M5 Max' not in joined
for term in ['DGX Spark', '22.6', '17.3', '38.6', '108.2', '164.6', '56.6']:
    assert term.replace(' ', '') in re.sub(r'\s+', '', joined), term
assert '566,016' in re.sub(r'\s+','',joined) and '322,816' in re.sub(r'\s+','',joined)
assert not re.search(r'\bMSIM\b|\bMS\b|Morgan\s+Stanley|摩根士丹利', joined, re.I)
assert '74-141' in re.sub(r'\s+','',joined)
assert '255-512' in re.sub(r'\s+','',joined)
log = (ROOT/'build/main.log').read_text(errors='replace')
assert not re.search(r'Overfull|Missing character|^! ', log, re.M)
fonts = {}
for page in reader.pages:
    for font in page['/Resources'].get('/Font', {}).get_object().values():
        f=font.get_object()
        children=f.get('/DescendantFonts', [f])
        for child in children:
            cf=child.get_object(); desc=cf.get('/FontDescriptor')
            if desc:
                desc=desc.get_object(); name=str(cf.get('/BaseFont',f.get('/BaseFont')))
                fonts[name]=any(k in desc for k in ['/FontFile','/FontFile2','/FontFile3'])
assert fonts and all(fonts.values())
result={'status':'automated checks passed; visual review recorded separately','pages':16,'main_pages':12,'appendix_pages':4,'order':[1,2,3],
 'pdf_sha256':sha(PDF),'referenced_display_values':len(keys),'source_files_hashed':len(manifest['sources']),
 'embedded_fonts':fonts,'page_checks':checks,'metadata':{str(k):str(v) for k,v in reader.metadata.items()},
 'performance_status':'Engineering estimates; no new device benchmarks','price_date':'Dated observations and estimates: 2026-09-21 / 2026-09-24'}
(ROOT/'qa/checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':16,'used_values':len(keys),'embedded_fonts':len(fonts),'possible_overlap_counts':{x['page']:len(x['possible_character_overlaps']) for x in checks if x['possible_character_overlaps']}},ensure_ascii=False))
