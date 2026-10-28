from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess,sys,hashlib,json
root=Path(__file__).resolve().parent.parent
source=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root/'build/candidate.pptx'
target=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else root/'build/qa/render'
pages=[int(x) for x in sys.argv[3:]] or range(1,34)
source_sha=hashlib.sha256(source.read_bytes()).hexdigest()
def run(i):
    p=subprocess.run(['/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node',str(root/'src/render-one.mjs'),str(i),str(source),str(target)],capture_output=True,text=True)
    print(i,p.returncode,p.stderr[-700:] if p.returncode else 'rendered',flush=True)
    if p.returncode:raise RuntimeError(i)
with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(run,pages))
assert hashlib.sha256(source.read_bytes()).hexdigest()==source_sha,'Source changed during render'
target.mkdir(exist_ok=True,parents=True)
records=[json.loads((target/f'state-{i:02d}.json').read_text()) for i in pages]
assert all(r['inputSha256']==source_sha for r in records)
(target/'render-manifest.json').write_text(json.dumps({'input':str(source),'source_sha256':source_sha,'slides':records},indent=2))
