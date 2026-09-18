"""Check compiled PDF, numeric source records, references and evidence hashes."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote
import pdfplumber
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
pdf = HERE / 'report.pdf'
reader = PdfReader(pdf)
manifest = json.loads((HERE / 'data/source-manifest.json').read_text())
count = 0
for source in manifest:
    for entry in source['files']:
        path = ROOT / entry['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256'], path
        count += 1
urls = []
for page in reader.pages:
    for annotation in page.get('/Annots', []):
        action = annotation.get_object().get('/A', {})
        if action.get('/S') == '/URI':
            urls.append(str(action.get('/URI')))
expected = {unquote(s['url']) for s in manifest}
assert expected == {unquote(u) for u in urls}
text = '\n'.join(p.extract_text() or '' for p in reader.pages)
for marker in ['TECH-', '用户要求', 'mentor', '检查点', '9e5c2fe', '\ufffd']:
    assert marker not in text, marker
for term in ['Qwen3.8', 'Gemma', 'Kimi', 'Open WebUI', 'LibreChat', 'RAGFlow', 'Hermes', 'LobeHub', 'Cherry Studio', 'OpenClaw', 'TokenSpeed']:
    assert term in text, term
model_source = (HERE / 'models.tex').read_text()
for model in json.loads((HERE / 'data/model-artifacts.json').read_text()):
    value = f"{model['decimal_gb']:,.2f}"
    assert value in model_source, value
log = (HERE / 'build/main.log').read_text()
for marker in ['Overfull', 'Missing character', 'undefined references', 'undefined on input']:
    assert marker not in log, marker
pages = []
with pdfplumber.open(pdf) as doc:
    for i, page in enumerate(doc.pages, 1):
        assert page.chars, i
        outside = [c for c in page.chars if c['x0'] < 0 or c['x1'] > page.width + .5 or c['top'] < 0 or c['bottom'] > page.height + .5]
        assert not outside, (i, outside[:3])
        pages.append({'physical_page': i, 'characters': len(page.chars)})
out = {'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'physical_pages': len(reader.pages),
       'reference_count': len(manifest), 'source_hashes_verified': count,
       'external_urls_verified': len(expected), 'model_values_verified': 8,
       'latex_critical_warnings_absent': True, 'pages': pages,
       'visual_review': 'Recorded separately in qa/review.md; machine checks do not prove layout quality.'}
(HERE / 'qa/checks.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:v for k,v in out.items() if k != 'pages'}, ensure_ascii=False, indent=2))
