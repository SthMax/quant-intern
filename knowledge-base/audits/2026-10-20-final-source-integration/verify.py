import hashlib,json,re,subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT=Path.cwd(); KB=ROOT/'knowledge-base'; OUT=KB/'audits/2026-10-20-final-source-integration'
hash_checks=[];hash_failures=[];known_hashes={}
def digest(p):
 if p not in known_hashes:known_hashes[p]=hashlib.sha256(p.read_bytes()).hexdigest()
 return known_hashes[p]
def check_hash(base,path,declared,where,expected_bytes=None):
 p=(base/path).resolve();r={'manifest':str(where.relative_to(ROOT)),'path':str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p),'declared_sha256':declared}
 if not p.exists():r['status']='missing';hash_failures.append(r)
 else:
  r['actual_sha256']=digest(p);r['status']='passed' if r['actual_sha256']==declared else 'mismatch'
  if expected_bytes is not None and p.stat().st_size!=expected_bytes:r['status']='byte_count_mismatch'
  if r['status']!='passed':hash_failures.append(r)
 hash_checks.append(r)
def walk(obj,base,where):
 if isinstance(obj,list):
  for x in obj:walk(x,base,where)
 elif isinstance(obj,dict):
  if isinstance(obj.get('path'),str) and re.fullmatch(r'[0-9a-f]{64}',str(obj.get('sha256',''))):check_hash(base,obj['path'],obj['sha256'],where,obj.get('bytes'))
  for k,v in obj.items():
   if k=='files' and isinstance(v,dict):
    for n,row in v.items():
     if isinstance(row,dict) and re.fullmatch(r'[0-9a-f]{64}',str(row.get('sha256',''))) and 'path' not in row:check_hash(base,n,row['sha256'],where,row.get('bytes'))
   walk(v,base,where)
for n in range(89,93):
 base=KB/'sources'/f'TECH-{n:03}'
 for p in base.glob('*.json'):
  if any(x in p.name for x in ['manifest','metadata','retrieval']):walk(json.loads(p.read_text()),base,p)

changed=subprocess.check_output(['git','diff','--name-only'],text=True).splitlines()
untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],text=True).splitlines()
md=[]
for name in dict.fromkeys(changed+untracked):
 p=ROOT/name
 if p.suffix!='.md' or not p.exists() or 'audits/2026-10-20-final-source-integration/' in name:continue
 if '/sources/TECH-' in name and p.name not in ['original.md','evidence-note.md']:continue
 if '/sources/TECH-' in name and p.parent.name not in [f'TECH-{n:03}' for n in range(89,93)]:continue
 md.append(p)
link_checks=[];broken=[];preexisting=[]
pattern=re.compile(r'!?\[[^\]\n]*\]\(([^\n]+?)\)')
for p in md:
 text=p.read_text();name=str(p.relative_to(ROOT))
 prev=subprocess.run(['git','show','HEAD:'+name],capture_output=True,text=True).stdout if name in changed else ''
 for match in pattern.finditer(text):
  raw=match.group(1).strip()
  if raw.startswith('<'):raw=raw[1:raw.find('>')]
  else:raw=re.split(r'\s+["\']',raw,maxsplit=1)[0]
  if not raw or raw.startswith('#') or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',raw):continue
  target=unquote(raw.split('#',1)[0].split('?',1)[0]);q=(p.parent/target).resolve()
  r={'document':name,'target':target,'line':text[:match.start()].count('\n')+1,'exists':q.exists()}
  link_checks.append(r)
  if not q.exists():
   if match.group(0) in prev:preexisting.append(r)
   else:broken.append(r)
idx=json.loads((KB/'reading-index.json').read_text());counts=Counter(r['collection_role'] for r in idx['records'])
reg_ids=re.findall(r'^\|\s*([A-Z]+-\d+)\s*\|',(KB/'source-register.md').read_text(),re.M)
regset=set(reg_ids);idxset={r['source_id'] for r in idx['records']}
baseline=json.loads(subprocess.check_output(['git','show','HEAD:knowledge-base/reading-index.json'],text=True))
checks={'registered_ids':len(idxset),'record_count':len(idx['records']),'counts':dict(counts),'register_unique_ids':len(regset),'register_rows':len(reg_ids),'register_matches_reading_index':regset==idxset,'old_reading_records_unchanged':idx['records'][:len(baseline['records'])]==baseline['records'],'old_reading_order_unchanged':idx['records'][:len(baseline['records'])]==baseline['records'],'reading_index_md_present':(KB/'reading-index.md').exists()}
assert checks['registered_ids']==216 and counts=={'main':197,'supporting':15,'redirect':4}
assert checks['register_matches_reading_index'] and checks['old_reading_records_unchanged']
body_checks={}
for name in ['reference-architecture.md','scenario-1-personal-agent-2026-09-24.md','scenario-2-enterprise-rag-2026-09-23.md','scenario-3-company-agent-2026-09-23.md']:
 p=KB/'infrastructure'/name
 old_text=subprocess.check_output(['git','show','HEAD:'+str(p.relative_to(ROOT))],text=True)
 new_text=re.sub(r'> \*\*2026-10-20最新研究入口：\*\*[^\n]*\n\n','',p.read_text(),count=1)
 body_checks[name]=new_text==old_text
assert all(body_checks.values())
checks['scenario_and_architecture_old_bodies_unchanged']=body_checks
for n in range(89,93):
 row=next(r for r in idx['records'] if r['source_id']==f'TECH-{n:03}')
 assert (KB/row['reading_path']).exists() and (KB/row['metadata_path']).exists() and (KB/'sources'/row['source_id']/'evidence-note.md').exists()
# Data declarations that explicitly map input paths to SHA-256.
data_hashes=[]
for base in [KB/'infrastructure/data/final-configurations-2026-10-20',KB/'infrastructure/data/tco-2026-10-20',KB/'models/data/public-benchmarks-2026-10-20',KB/'infrastructure/data/final-source-refresh-2026-10-20',KB/'pilots/data/final-pilot-roadmap-2026-10-20']:
 for p in base.glob('*.json'):
  d=json.loads(p.read_text())
  def w(o):
   if isinstance(o,list):
    for x in o:w(x)
   elif isinstance(o,dict):
    for k,v in o.items():
     if isinstance(v,dict) and ('sha256' in k.lower() or 'hash' in k.lower()):
      for path,sha in v.items():
       if isinstance(sha,str) and re.fullmatch('[0-9a-f]{64}',sha):
        possibilities=[ROOT/path,KB/path,p.parent/path]
        q=next((x for x in possibilities if x.is_file()),None)
        if q:data_hashes.append({'manifest':str(p.relative_to(ROOT)),'path':str(q.resolve().relative_to(ROOT)),'status':'passed' if digest(q)==sha else 'mismatch'})
     w(v)
  w(d)
fail_data=[r for r in data_hashes if r['status']!='passed']
result={'as_of':'2026-10-20','scope':'New authored agent Markdown, four new source-packet declared hashes, and resolvable analysis input-hash maps. Raw publisher Markdown is preserved and is not reinterpreted as local authored links.','status':'passed' if not(hash_failures or broken or fail_data) else 'requires_fix','index':checks,'authored_markdown_documents':len(md),'local_link_checks':len(link_checks),'broken_new_local_links':broken,'preexisting_broken_local_links':preexisting,'source_hash_assertions':len(hash_checks),'unique_source_files_hashed':len({x['path'] for x in hash_checks}),'source_hash_failures':hash_failures,'analysis_input_hash_checks':len(data_hashes),'analysis_input_hash_failures':fail_data,'documents':[str(p.relative_to(ROOT)) for p in md]}
(OUT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'source-hash-checks.json').write_text(json.dumps(hash_checks,ensure_ascii=False,indent=2)+'\n')
(OUT/'analysis-input-hash-checks.json').write_text(json.dumps(data_hashes,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['documents','scope']},ensure_ascii=False,indent=2))
