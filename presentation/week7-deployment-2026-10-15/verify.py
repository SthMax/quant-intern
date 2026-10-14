"""Check PDF geometry, embedded fonts, data provenance and approved-note integrity."""
from pathlib import Path
import hashlib
import json
import re
import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
PDF = ROOT / 'output/pdf/week7-long-context-deployment.pdf'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = json.loads((ROOT / 'data/source-manifest.json').read_text())
for file, info in manifest['sources'].items():
    assert sha(REPO / file) == info['sha256'], file
approved = json.loads((REPO / 'knowledge-base/audits/2026-10-14-chinese-prose/validation.json').read_text())
assert sha(ROOT / 'speaker-notes.md') == approved['notes_sha256']
slides = (ROOT / 'slides.tex').read_text()
keys = set(re.findall(r'\\V\{([^}]+)\}', slides))
assert keys <= set(manifest['figures'])
assert slides.count('\\begin{frame}') == 25
reader = PdfReader(PDF)
assert len(reader.pages) == 25
assert reader.metadata.get('/Author') == 'Intern research'
assert reader.metadata.get('/Title') == '本地长上下文Agent部署与推理优化'
checks = []
texts = []
with pdfplumber.open(PDF) as pdf:
    for number, page in enumerate(pdf.pages, 1):
        text = page.extract_text() or ''
        texts.append(re.sub(r'\s+', '', text))
        assert abs(page.width / page.height - 16/9) < 0.001
        chars = [c for c in page.chars if c['text'].strip()]
        outside = [c['text'] for c in chars if c['x0'] < -1 or c['x1'] > page.width+1 or c['top'] < -1 or c['bottom'] > page.height+1]
        overlaps = []
        for i,c in enumerate(chars):
            area = (c['x1']-c['x0'])*(c['bottom']-c['top'])
            if area <= 0:
                continue
            for d in chars[i+1:]:
                iw = min(c['x1'],d['x1'])-max(c['x0'],d['x0'])
                ih = min(c['bottom'],d['bottom'])-max(c['top'],d['top'])
                if iw <= 0 or ih <= 0:
                    continue
                other = (d['x1']-d['x0'])*(d['bottom']-d['top'])
                if other > 0 and iw*ih/min(area,other) > .30:
                    # CJK punctuation uses a full-em PDF box even after TeX kerning.
                    punct = '，、。；：！？（）《》「」『』'
                    kerned_punctuation = (c['text'] in punct or d['text'] in punct) and abs(c['top']-d['top']) < 1
                    if not kerned_punctuation:
                        overlaps.append({'text':c['text']+d['text'], 'x':round(c['x0'],1),'y':round(c['top'],1)})
        assert not outside, (number, outside)
        assert not overlaps, (number, overlaps)
        if number >= 21:
            assert '附录' in texts[-1]
        checks.append({'page':number,'characters':len(text),'outside_page':outside,'possible_character_overlaps':overlaps})
joined = '\n'.join(texts)
for term in ['历史命中','继续研究512K','更长历史来交换','Jev','Qwen3.6','MSIM','MorganStanley','摩根士丹利']:
    assert term not in joined, term
assert not re.search(r'\bMS\b', joined)
critical = {
    3:['Qwen3.8-27B','OpenCode','vLLM'],
    4:['19.7','17.7','14.7','11.2','3.1','8.6','25.8','78.9','估算','外推'],
    5:['新增1K','新增8K','约5秒','约40秒'],
    6:['1.81M','600K','810K','6.8-8.2','7.8-9.9'],
    9:['242K','762K','双TP4','406GB'],
    11:['91-102','285-298','161-283','291-304'],
    14:['50-53','82-93','110-140','1,040-1,379','modifiedvLLM'],
    15:['2,842.48','2,926.08','2,970.50','2.94%','1.52%'],
    16:['510.29GB','202.76GB','307.53GB','286.41GiB','71.60GiB'],
    19:['21项','18项','1.2核','42GiB'],
    21:['20.53','21.01','20.11','17.23','14.82','4,815.8','9.83'],
    22:['1,806,907','6.435M','18.327M','29.498M','BF16'],
    23:['718.48','614.76','922.61','661.15','1,052.18','140K-157K'],
}
for page, terms in critical.items():
    for term in terms:
        assert term in texts[page-1], (page,term)
fonts = {}
for page in reader.pages:
    for font in page['/Resources'].get('/Font', {}).get_object().values():
        f = font.get_object()
        for child in f.get('/DescendantFonts', [f]):
            cf = child.get_object()
            desc = cf.get('/FontDescriptor')
            if desc:
                desc = desc.get_object()
                fonts[str(cf.get('/BaseFont',f.get('/BaseFont')))] = any(k in desc for k in ['/FontFile','/FontFile2','/FontFile3'])
assert fonts and all(fonts.values())
log = (ROOT / 'build/main.log').read_text(errors='replace')
assert not re.search(r'Overfull|Missing character|^! ', log, re.M)
page_map = json.loads((ROOT / 'data/slide-map.json').read_text())
assert [x['page'] for x in page_map['slides']] == list(range(1,26))
for slide in page_map['slides']:
    for file in slide['sources']:
        assert (REPO / file).is_file(), file
result = {'status':'passed; visual review recorded separately','pages':25,'main_pages':20,'appendix_pages':5,
          'pdf_sha256':sha(PDF),'approved_notes_sha256':sha(ROOT/'speaker-notes.md'),
          'approved_notes_unchanged':True,'source_files_hashed':len(manifest['sources']),
          'referenced_display_values':len(keys),'embedded_fonts':fonts,'page_checks':checks,
          'metadata':{str(k):str(v) for k,v in reader.metadata.items()},
          'performance_scope':'Preserved measurements, public results and labelled estimates; no new GPU experiment',
          'price_date':'2026-10-12'}
(ROOT / 'qa/checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':25,'used_values':len(keys),'embedded_fonts':len(fonts),'overlaps':0,'approved_notes_unchanged':True},ensure_ascii=False))
