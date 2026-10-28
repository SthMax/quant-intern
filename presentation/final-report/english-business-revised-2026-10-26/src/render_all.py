from concurrent.futures import ThreadPoolExecutor
import subprocess,sys
from pathlib import Path
r=Path(__file__).resolve().parent.parent
source=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else r/'build/candidate.pptx'
target=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else r/'build/qa/final-render'
pages=[int(x) for x in sys.argv[3:]] or range(1,34)
def run(i):
 p=subprocess.run(['/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node',str(r/'src/render-one.mjs'),str(i),str(source),str(target)],capture_output=True,text=True)
 print(i,p.returncode,p.stderr[-500:] if p.returncode else 'rendered',flush=True)
 if p.returncode:raise RuntimeError(i)
with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(run,pages))
