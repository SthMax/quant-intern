"""Check source provenance, displayed financial values and delivered file contents."""
from pathlib import Path
import csv
import hashlib
import json
import re
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
read = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
slides = read(ROOT / 'data/slides.json')['slides']
manifest = read(ROOT / 'data/source-manifest.json')
checks = []

def check(name, condition, detail=None):
    checks.append({'name': name, 'pass': bool(condition), 'detail': detail})

check('42 slides, 34 main and 8 appendices', len(slides) == 42 and manifest['main_slides'] == 34 and manifest['appendix_slides'] == 8)
for source in manifest['sources']:
    check('source hash: ' + source['path'], sha(REPO / source['path']) == source['sha256'])
check('reviewed slide-content hash', sha(ROOT / 'data/slides.json') == manifest['slides_sha256'])
check('matching speaker-note hash', sha(ROOT / 'speaker-notes.md') == manifest['speaker_notes_sha256'])

tco = read(REPO / 'knowledge-base/infrastructure/data/tco-2026-10-20/results.json')
for chart, scale in zip(slides[29]['charts'], ('personal', 'company')):
    case = next(c for c in tco['cases'] if c['scale'] == scale and c['volume'] == 'base')
    expected = [case['totals'][route]['three_year_total_cny'] / 10000 for route in ('local', 'deepseek', 'claude')]
    check(scale + ' TCO bars agree to displayed 0.01万元', [f'{v:.2f}' for v in chart['values']] == [f'{v:.2f}' for v in expected], expected)
for row, volume in zip(slides[30]['rows'], ('low', 'base', 'high')):
    case = next(c for c in tco['cases'] if c['scale'] == 'company' and c['volume'] == volume)
    expected = [f"{case['totals'][route]['three_year_total_cny']/10000:.2f}" for route in ('local', 'deepseek', 'claude')]
    actual = re.findall(r'\d+\.\d+', row[3])
    check('company ' + volume + ' TCO table', actual == expected, expected)
check('8-round input ledger', sum(r['submitted_input'] for r in tco['round_ledger']) == 1080000)
check('new external input ledger', sum(r['new_external_input'] for r in tco['round_ledger']) == 156000)
check('output ledger', sum(r['output'] for r in tco['round_ledger']) == 16000)

config = read(REPO / 'knowledge-base/infrastructure/data/final-configurations-2026-10-20/summary.json')
pool = int(config['scenario1']['observed_pool_tokens'] * (1 - config['scenario1']['pool_reserve_fraction']))
check('Spark three 512K sessions fit after reserve', 3 * 524288 <= pool, {'pool': pool, 'remaining_after_one_1M': pool - 1000000})
ds = config['scenario3']
check('native checkpoint decomposition', ds['engram_table_bytes'] + ds['non_Engram_checkpoint_bytes'] == ds['native_checkpoint_bytes'])

pptx = ROOT / 'output/final-report-2026-10-20.pptx'
pdf = ROOT / 'output/final-report-2026-10-20.pdf'
namespace = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
with zipfile.ZipFile(pptx) as package:
    slide_parts = [n for n in package.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)]
    note_parts = [n for n in package.namelist() if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml', n)]
    check('42 native PPTX slides and notes', len(slide_parts) == len(note_parts) == 42)
    package_text = '\n'.join(package.read(n).decode() for n in package.namelist() if n.endswith('.xml'))
    check('anonymous PPTX content and properties', not re.search(r'MSIM|Morgan\s*Stanley|摩根士丹利|\bMS\b', package_text))
    for s in slides:
        root = ET.fromstring(package.read(f"ppt/notesSlides/notesSlide{s['id']}.xml"))
        note_text = ''.join(root.itertext())
        check(f"speaker note {s['id']:02d}", s['notes'] in note_text)

reader = PdfReader(pdf)
norm = lambda s: re.sub(r'\s+', '', unicodedata.normalize('NFKC', s))
check('42 PDF pages', len(reader.pages) == 42)
texts = [p.extract_text() or '' for p in reader.pages]
for s, page_text in zip(slides, texts):
    check(f"PDF page {s['id']:02d} has complete Chinese title", norm(s['title']) in norm(page_text))
urls = []
for page in reader.pages:
    for ref in page.get('/Annots', []):
        action = ref.get_object().get('/A', {})
        if action.get('/URI'): urls.append(str(action['/URI']))
check('source page has all eight linked destinations', all(url in urls for _, url in slides[-1]['links']), {'links': len(urls)})
check('anonymous PDF content and metadata', not re.search(r'MSIM|Morgan\s*Stanley|摩根士丹利|\bMS\b', '\n'.join(texts) + str(reader.metadata)))
check('PDF metadata identifies the report', reader.metadata.title == '公募基金本地LLM应用与部署研究' and reader.metadata.author == 'Intern')
receipt = read(ROOT / 'qa/finalizer.json')
check('PPTX matches finalization receipt', sha(pptx) == receipt['finalSha256'])
check('native tables/charts and import passed', receipt['firstPartyImport']['passed'] and receipt['nativeTableArithmetic']['native_table_count'] == 25 and receipt['packageIntegrity']['chart_count'] == 5)

result = {
    'date': '2026-10-20',
    'passed': all(c['pass'] for c in checks),
    'checks': checks,
    'outputs': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p), 'bytes': p.stat().st_size} for p in (pptx, pdf, ROOT/'speaker-notes.md')],
    'visual_review': '42 slide previews reviewed; final 11 changed pages reviewed by the Chinese-teacher agent. PDF renders reviewed separately in editorial/chinese-teacher-final-review.md.',
    'layout_heuristic_warning': 'P36 estimated native table bottom exceeds the callout boundary by 0.0582 inches; the rendered table and last row are visually complete. This is a heuristic warning, not a reported structural finding.',
    'native_powerpoint_opened': False,
}
(ROOT / 'qa/verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
for c in checks:
    if not c['pass']: print('FAILED:', c)
print(f"{sum(c['pass'] for c in checks)}/{len(checks)} checks passed.")
if not result['passed']: raise SystemExit(1)
