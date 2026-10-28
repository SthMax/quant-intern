from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,sys,json,hashlib
r=Path(__file__).resolve().parent.parent
s=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else r/'build/candidate.pptx'
t=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else r/'build/qa/render'
pages=[int(i) for i in sys.argv[3:]] or range(1,34)
sha=hashlib.sha256(s.read_bytes()).hexdigest()
def run(i):
    p=subprocess.run(['/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node',str(r/'src/render-one.mjs'),str(i),str(s),str(t)],capture_output=True,text=True)
    print(i,p.returncode,p.stderr[-700:] if p.returncode else 'rendered',flush=True)
    if p.returncode:raise RuntimeError(i)
with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(run,pages))
assert hashlib.sha256(s.read_bytes()).hexdigest()==sha
rec=[json.loads((t/f'slide-{i:02d}.json').read_text()) for i in pages]
assert all(q['inputSha256']==sha for q in rec)
(t/'render-manifest.json').write_text(json.dumps({'input':str(s),'inputSha256':sha,'slides':rec},indent=2))
