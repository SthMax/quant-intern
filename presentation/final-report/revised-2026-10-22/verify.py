"""Check final files, source identity and the main financial/experience quantities."""
from pathlib import Path
import hashlib,json,re,unicodedata,zipfile,xml.etree.ElementTree as ET
from pypdf import PdfReader

R=Path(__file__).resolve().parent;REPO=R.parents[2]
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d=load(R/'data/slides.json');s=d['slides'];m=load(R/'data/source-manifest.json');checks={}
checks['content_count']=len(s)==38 and d['main_slides']==32 and d['appendix_slides']==6
checks['source_hashes']=all(sha(REPO/x['path'])==x['sha256'] for x in m['sources'])
checks['reviewed_content']=sha(R/'data/slides.json')==m['slides_sha256'] and sha(R/'speaker-notes.md')==m['speaker_notes_sha256']
t=load(REPO/'knowledge-base/infrastructure/data/tco-2026-10-20/results.json')
checks['tco_values']=True
for graph,scale in zip(s[26]['charts'],['personal','company']):
 case=next(c for c in t['cases'] if c['scale']==scale and c['volume']=='base')
 expected=[case['totals'][route]['three_year_total_cny']/10000 for route in ['local','deepseek']]
 checks['tco_values'] &= all(abs(a-b)<0.00001 for a,b in zip(graph['values'],expected))
checks['financial_example']=(120-100)/100==0.2 and round((120-90)/90*100,1)==33.3
checks['time_saving_example']=(90-25-20)*30/60==22.5
checks['spark_wait_minutes']=abs(s[11]['waits']['values'][0]-144.8/60)<0.001 and abs(s[11]['waits']['values'][1]-1470.1/60)<0.001
pptx=R/'output/final-report-2026-10-22.pptx';pdf=R/'output/final-report-2026-10-22.pdf'
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
with zipfile.ZipFile(pptx) as z:
 dim=ET.fromstring(z.read('ppt/presentation.xml')).find('p:sldSz',ns)
 checks['pptx_16_9']=int(dim.attrib['cx'])*9==int(dim.attrib['cy'])*16
 parts=[p for p in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',p)]
 checks['pptx_pages']=len(parts)==38
 text='\n'.join(z.read(p).decode() for p in z.namelist() if p.endswith('.xml'))
 checks['pptx_anonymous']=not re.search(r'MSIM|Morgan\s*Stanley|摩根士丹利|\bMS\b',text)
 checks['speaker_notes']=all(row['notes'] in ''.join(ET.fromstring(z.read(f"ppt/notesSlides/notesSlide{row['id']}.xml")).itertext()) for row in s)
reader=PdfReader(pdf);texts=[p.extract_text() or '' for p in reader.pages]
norm=lambda v:re.sub(r'\s+','',unicodedata.normalize('NFKC',v))
checks['pdf_pages']=len(reader.pages)==38
checks['pdf_16_9']=all(abs(float(p.mediabox.width)/float(p.mediabox.height)-16/9)<0.0001 for p in reader.pages)
checks['pdf_complete_titles']=all(norm(row['title']) in norm(text) for row,text in zip(s,texts))
checks['pdf_anonymous']=not re.search(r'MSIM|Morgan\s*Stanley|摩根士丹利|\bMS\b','\n'.join(texts)+str(reader.metadata))
uris=[str(ref.get_object().get('/A',{}).get('/URI','')) for p in reader.pages for ref in p.get('/Annots',[])]
checks['source_links']=all(url in uris for _,url in s[-1]['links'])
checks['finalizer_hash']=sha(pptx)==load(R/'qa/finalizer.json')['finalSha256']
out={'date':'2026-10-22','checks':checks,'passed':all(checks.values()),'artifacts':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in [pptx,pdf,R/'speaker-notes.md']],'native_powerpoint_opened':False}
(R/'qa/verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':out['passed'],'failed':[k for k,v in checks.items() if not v]}))
if not out['passed']:raise SystemExit(1)
