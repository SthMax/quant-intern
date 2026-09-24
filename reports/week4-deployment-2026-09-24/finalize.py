"""Set neutral metadata and portable source links, then check all three PDFs."""
import hashlib
import logging
logging.getLogger("pdfminer.pdffont").setLevel(logging.ERROR)
import json
import os
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote
import pdfplumber
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
manifest=json.loads((ROOT/'qa/source-manifest.json').read_text())
def normalize_cmap(data):
    # CoreText may map an ordinary Han glyph to an identical Kangxi radical.
    # Canonicalize only compatibility Han/radicals for reliable copy and search.
    def destination(h):
        value=bytes.fromhex(h).decode('utf-16-be')
        value=value.translate(str.maketrans('⺠⻅⻆⻓⻔⻚⻛⻬','民见角长门页风齐'))
        value=''.join(unicodedata.normalize('NFKC',c) if 0x2e80 <= ord(c) <= 0x2fff or 0xf900 <= ord(c) <= 0xfaff else c for c in value)
        return value.encode('utf-16-be').hex().upper()
    text=data.decode('ascii')
    def chars(m):
        body=re.sub(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>',lambda q:'<'+q[1]+'> <'+destination(q[2])+'>',m[2])
        return m[1]+' beginbfchar'+body+'endbfchar'
    text=re.sub(r'(\d+) beginbfchar([\s\S]*?)endbfchar',chars,text)
    def ranges(m):
        pairs=[]
        for a,b,value in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*(<[^>]+>|\[[^]]+\])',m[1]):
            start,end=int(a,16),int(b,16)
            values=re.findall(r'<([0-9A-Fa-f]+)>',value)
            for j,code in enumerate(range(start,end+1)):
                dest=values[j] if value.startswith('[') else f'{int(values[0],16)+j:0{len(values[0])}X}'
                pairs.append(f'<{code:0{len(a)}X}> <{destination(dest)}>')
        if not pairs:return m[0]
        return f'{len(pairs)} beginbfchar\n'+'\n'.join(pairs)+'\nendbfchar'
    text=re.sub(r'\d+ beginbfrange([\s\S]*?)endbfrange',ranges,text)
    return text.encode('ascii')

checks=[]
for entry in manifest['documents']:
    p=ROOT/entry['output']; reader=PdfReader(p); writer=PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.add_metadata({'/Title':entry['title'],'/Author':'Intern research',
        '/Subject':'Week 4 local LLM deployment scenario, 24 September 2026',
        '/Keywords':'LLM, deployment, infrastructure, scenario '+str(entry['scenario'])})
    rewritten=0
    seen_fonts=set()
    for page in writer.pages:
        for ref in page['/Resources'].get('/Font',{}).get_object().values():
            key=getattr(ref,'idnum',id(ref))
            if key in seen_fonts:continue
            seen_fonts.add(key);font=ref.get_object()
            if '/ToUnicode' in font:
                cmap=font['/ToUnicode'].get_object()
                cmap.set_data(normalize_cmap(cmap.get_data()))
        for a in page.get('/Annots',[]):
            ann=a.get_object();action=ann.get('/A')
            if not action:continue
            action=action.get_object();uri=str(action.get('/URI',''))
            if uri.startswith('https://pdf-local.invalid/'):
                dest=unquote(uri.split('https://pdf-local.invalid/',1)[1])
            elif uri.startswith('https://repo-local.invalid/'):
                target=REPO/unquote(uri.split('https://repo-local.invalid/',1)[1])
                dest=os.path.relpath(target,p.parent)
            else:continue
            action[NameObject('/URI')]=TextStringObject(dest);rewritten+=1
    temp=p.with_suffix('.tmp.pdf')
    with temp.open('wb') as f:writer.write(f)
    temp.replace(p)
    reader=PdfReader(p);pages=[];joined='';fonts={};links=[];font_refs_seen=set()
    for page in reader.pages:
        for f in page['/Resources'].get('/Font',{}).get_object().values():
            refid=getattr(f,'idnum',id(f))
            if refid in font_refs_seen:continue
            font_refs_seen.add(refid)
            f=f.get_object()
            if f.get('/Subtype') == '/Type3':
                fonts['Type3-embedded-glyphs-'+str(len(fonts))] = bool(f.get('/CharProcs'))
                continue
            for child in f.get('/DescendantFonts',[f]):
                cf=child.get_object();desc=cf.get('/FontDescriptor')
                if desc:
                    desc=desc.get_object();fonts[str(cf.get('/BaseFont',f.get('/BaseFont')))]=any(k in desc for k in ['/FontFile','/FontFile2','/FontFile3'])
        for a in page.get('/Annots',[]):
            action=a.get_object().get('/A')
            if action:
                uri=str(action.get_object().get('/URI',''))
                if uri:links.append(uri)
    with pdfplumber.open(p) as pdf:
        for n,page in enumerate(pdf.pages,1):
            text=page.extract_text() or '';joined+=text+'\n'
            outside=[c['text'] for c in page.chars if c['text'].strip() and (c['x0']<-1 or c['x1']>page.width+1 or c['top']<-1 or c['bottom']>page.height+1)]
            assert not outside,(p.name,n,outside)
            assert len(text)>80,(p.name,'Nearly blank page',n,len(text))
            pages.append({'page':n,'characters':len(text),'first_lines':text.splitlines()[:2]})
    assert all(fonts.values()),fonts
    assert not re.search(r'\bMSIM\b|\bMS\b|Morgan\s+Stanley|摩根士丹利',joined,re.I)
    assert '\ufffd' not in joined
    assert '**' not in joined, 'Unrendered emphasis marker'
    assert not any('invalid/' in x or '/Users/' in x for x in links)
    source=REPO/entry['source']; assert hashlib.sha256(source.read_bytes()).hexdigest()==entry['source_sha256']
    canonical_text='\n'.join(page.extract_text() or '' for page in reader.pages)
    compact=re.sub(r'\s+','',unicodedata.normalize('NFKC',canonical_text))
    headings=re.findall(r'^#{1,4} (.+)$',source.read_text(),re.M)
    for heading in headings:
        clean=re.sub(r'\s+','',unicodedata.normalize('NFKC',heading.replace('**','').replace('`','')))
        assert clean in compact,(p.name,'missing heading',heading)
    if entry['scenario']==1:
        for value in ['22.6','17.3','38.60GB','108.20GB','164.60GB','56.60GB','524,288']:
            assert value in compact,(p.name,value)
    if entry['scenario']==3:
        for value in ['566,016','322,816','34.1','52.0']:
            assert value in compact,(p.name,value)
    checks.append({'pdf':entry['output'],'pages':len(pages),'headings_checked':len(headings),
       'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'embedded_fonts':fonts,
       'links':len(links),'rewritten_links':rewritten,'page_summary':pages})
    print(p.name,len(pages),'pages;',len(headings),'headings;',len(fonts),'embedded fonts;',len(links),'links')
(ROOT/'qa/checks.json').write_text(json.dumps({'status':'Content, metadata, source hashes, links and page bounds checked; visual review separate','documents':checks},ensure_ascii=False,indent=2)+'\n')
