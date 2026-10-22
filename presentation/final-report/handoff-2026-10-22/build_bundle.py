"""Archive the current research workspace, retaining original paths and byte hashes."""
from pathlib import Path
import collections,hashlib,json,posixpath,re,subprocess,zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PREFIX='quant-llm-pro-handoff-2026-10-22'
ARCHIVE=HERE/(PREFIX+'.zip')
ROOTS=['knowledge-base','presentation','reports','weekly','scripts','PROJECT_PLAN.md','README.md','RESEARCH_TOOLS.md']
raw=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z','--',*ROOTS],cwd=ROOT)
names=sorted(set(x for x in raw.decode().split('\0') if x))
files=[]
for name in names:
    p=ROOT/name
    if p.is_symlink() or not p.is_file() or p.is_relative_to(HERE):continue
    if any(part in {'.git','node_modules','__pycache__','.DS_Store'} for part in p.parts):continue
    if p.name.startswith('.env') or p.name.endswith(('.pyc','.swp','.zip.part')):continue
    files.append((name,p))

core=[
 'PROJECT_PLAN.md',
 'knowledge-base/companies/llm-report-scope-2026-09-09.md',
 'knowledge-base/companies/focused-research-2026-09-09.md',
 'knowledge-base/companies/case-diversity-2026-09-09.md',
 'knowledge-base/companies/quant-research-2026-09-09.md',
 'knowledge-base/companies/efund-llm-deep-dive.md',
 'knowledge-base/regulation/synthesis-2026-09-06.md',
 'knowledge-base/regulation/review-results-2026-09-09.md',
 'knowledge-base/models/model-survey-2026-09-16.md',
 'knowledge-base/models/license-review-2026-09-16.md',
 'knowledge-base/models/mimo-v2.6-research-2026-09-22.md',
 'knowledge-base/infrastructure/serving-framework-survey-2026-09-17.md',
 'knowledge-base/infrastructure/harness-survey-2026-09-17.md',
 'knowledge-base/infrastructure/final-configurations-2026-10-20.md',
 'knowledge-base/infrastructure/scenario-1-personal-agent-2026-09-24.md',
 'knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md',
 'knowledge-base/infrastructure/scenario-3-company-agent-2026-09-23.md',
 'knowledge-base/infrastructure/dgx-spark-qwen27-external-benchmark-2026-10-12.md',
 'knowledge-base/infrastructure/scenario-1-speed-target-review-2026-09-24.md',
 'knowledge-base/infrastructure/workstation-configurations-2026-09-21.md',
 'knowledge-base/infrastructure/server-gpu-procurement-2026-09-21.md',
 'knowledge-base/infrastructure/server-gpu-procurement-2026-10-12.md',
 'knowledge-base/infrastructure/deepseek-a100-project-review-2026-10-12.md',
 'knowledge-base/infrastructure/ai-infra-book-reading-2026-10-12.md',
 'knowledge-base/infrastructure/tco-analysis-2026-10-20.md',
 'knowledge-base/models/public-benchmark-review-2026-10-20.md',
 'knowledge-base/pilots/final-pilot-roadmap-2026-10-20.md',
 'knowledge-base/pilots/data/final-pilot-roadmap-2026-10-20/evaluation-protocol.md',
 'knowledge-base/infrastructure/final-source-refresh-2026-10-20.md',
]
assert all((ROOT/p).is_file() for p in core)
def rebased_links(text,name):
    def replace(m):
        target=m.group(2)
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:|^#|^/',target):return m.group(0)
        if '\n' in target:return m.group(0)
        target=posixpath.normpath(posixpath.join('repo',posixpath.dirname(name),target))
        return m.group(1)+target+m.group(3)
    return re.sub(r'(!?\[[^\]\n]*\]\()([^\n)]+)(\))',replace,text)

parts=['# 核心研究合并文本\n\n29份现有研究正文的阅读副本。各文件保留自己的截止日、原文及计算条件；仅将相对链接展开到本包位置。完整原文件在`repo/`，历史内容与现行结论以文件顶部更新说明区分。\n\n## 目录\n']
for i,name in enumerate(core,1):parts.append(f'{i}. [{name}](repo/{name})\n')
for i,name in enumerate(core,1):
    parts.append(f'\n\n---\n\n# 文档{i:02d}：{name}\n\n原文件：[打开](repo/{name})\n\n')
    parts.append(rebased_links((ROOT/name).read_text(),name))
merged=''.join(parts)

groups=[
 ('先读：当前配置、经济性与任务',['knowledge-base/infrastructure/final-configurations-2026-10-20.md','knowledge-base/infrastructure/tco-analysis-2026-10-20.md','knowledge-base/models/public-benchmark-review-2026-10-20.md','knowledge-base/pilots/final-pilot-roadmap-2026-10-20.md','knowledge-base/infrastructure/final-source-refresh-2026-10-20.md']),
 ('行业用途与监管',['knowledge-base/companies/index.md','knowledge-base/companies/focused-research-2026-09-09.md','knowledge-base/companies/quant-research-2026-09-09.md','knowledge-base/regulation/index.md','knowledge-base/regulation/review-results-2026-09-09.md']),
 ('模型、serving与harness',['knowledge-base/models/model-survey-2026-09-16.md','knowledge-base/models/license-review-2026-09-16.md','knowledge-base/models/mimo-v2.6-research-2026-09-22.md','knowledge-base/infrastructure/serving-framework-survey-2026-09-17.md','knowledge-base/infrastructure/harness-survey-2026-09-17.md']),
 ('三套方案与硬件',['knowledge-base/infrastructure/scenario-1-personal-agent-2026-09-24.md','knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md','knowledge-base/infrastructure/scenario-3-company-agent-2026-09-23.md','knowledge-base/infrastructure/dgx-spark-qwen27-external-benchmark-2026-10-12.md','knowledge-base/infrastructure/server-gpu-procurement-2026-10-12.md','knowledge-base/infrastructure/workstation-configurations-2026-09-21.md']),
 ('推理与缓存专项',['knowledge-base/infrastructure/deepseek-a100-project-review-2026-10-12.md','knowledge-base/infrastructure/ai-infra-book-reading-2026-10-12.md','presentation/week7-deployment-2026-10-15/speaker-notes.md']),
 ('数据与复算',['knowledge-base/infrastructure/data/final-configurations-2026-10-20/README.md','knowledge-base/infrastructure/data/tco-2026-10-20/README.md','knowledge-base/models/data/public-benchmarks-2026-10-20/README.md','knowledge-base/pilots/data/final-pilot-roadmap-2026-10-20/seed-cases.jsonl','knowledge-base/pilots/data/final-pilot-roadmap-2026-10-20/evaluation-protocol.md','knowledge-base/infrastructure/data/final-source-refresh-2026-10-20/README.md']),
 ('总计划与当前尝试',['PROJECT_PLAN.md','weekly/final-presentation-plan-2026-10-19.md','presentation/final-report/speaker-notes.md','presentation/final-report/revised-2026-10-22/speaker-notes.md','presentation/final-report/editorial/professional-presenter-review-2026-10-22.md']),
]
index=['# 阅读地图\n\n先看用户反馈，再按具体问题选择研究正文；来源与计算文件可按原文链接继续追溯。\n']
for title,paths in groups:
    index.append(f'\n## {title}\n\n')
    for name in paths:
        assert (ROOT/name).is_file(),name
        index.append(f'- [{Path(name).name}](repo/{name})\n')
index.append('\n## 已有PDF与PPTX\n\n以下为当前仓库中的成品与草稿，未重新下载历史Release，也未改写其中内容。10月15日Pro版属于曾使用的汇报；两版final report仍未获用户认可。\n\n')
for name,p in files:
    if name.startswith(('presentation/','reports/')) and p.suffix.lower() in {'.pdf','.pptx'}:
        index.append(f'- [{name}](repo/{name})\n')
index.append('\n## 全部原始证据\n\n- [来源登记表](repo/knowledge-base/source-register.md)\n- [阅读索引](repo/knowledge-base/reading-index.json)\n- [原件说明](repo/knowledge-base/sources/README.md)\n\n`knowledge-base/sources/`和`knowledge-base/reference/`内保留原文、公开PDF、HTML、模型卡、许可、代码证据及元数据。`audits/`保存历史核验与修订记录，适合追溯，不必按时间从头读。\n')

extras={
 '00-START-HERE.md':(HERE/'START-HERE.md').read_bytes(),
 '01-FEEDBACK.md':(HERE/'FEEDBACK.md').read_bytes(),
 '02-READING-MAP.md':''.join(index).encode(),
 '03-CORE-RESEARCH.md':merged.encode(),
}
entries=[];counts=collections.Counter();total=0
temp=ARCHIVE.with_suffix('.zip.part')
print(f'Packaging {len(files)} repository files and {len(extras)} reading files.',flush=True)
with zipfile.ZipFile(temp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
    for name,p in files:
        data=p.read_bytes();archive_path='repo/'+name
        z.writestr(PREFIX+'/'+archive_path,data)
        entries.append({'path':archive_path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'origin':'workspace'})
        counts[name.split('/')[0]]+=1;total+=len(data)
    for name,data in extras.items():
        z.writestr(PREFIX+'/'+name,data)
        entries.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'origin':'handoff reading file'})
        total+=len(data)
    manifest={'date':'2026-10-22','timezone':'Asia/Shanghai','base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'snapshot':'current working tree including uncommitted changes','repository_files':len(files),'knowledge_base_files':counts['knowledge-base'],'registered_source_ids':len(json.loads((ROOT/'knowledge-base/reading-index.json').read_text())['records']),'core_documents':len(core),'counts':dict(counts),'bytes_before_zip':total,'exclusions':['Git database','ignored build/runtime/render caches','symlinks','temporary .research-workspace','this handoff directory (reading files explicitly added above)'],'entries':entries}
    z.writestr(PREFIX+'/MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
temp.replace(ARCHIVE)
print('Verifying every archived byte against the manifest.',flush=True)
with zipfile.ZipFile(ARCHIVE) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(entries)+1
    for e in entries:
        data=z.read(PREFIX+'/'+e['path'])
        assert len(data)==e['bytes'] and hashlib.sha256(data).hexdigest()==e['sha256'],e['path']
    for text_name in ['00-START-HERE.md','01-FEEDBACK.md','02-READING-MAP.md']:
        body=z.read(PREFIX+'/'+text_name).decode()
        for link in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',body):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:|^#',link):continue
            target=PREFIX+'/'+link.split('#')[0]
            assert target in z.namelist(),(text_name,link)
info={k:manifest[k] for k in ['date','base_commit','snapshot','repository_files','knowledge_base_files','registered_source_ids','core_documents','counts']}
info.update(archive=ARCHIVE.name,archive_bytes=ARCHIVE.stat().st_size,archive_sha256=hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),integrity='all entries checked against SHA-256',navigation='all start/feedback/map local links checked')
(HERE/'package-info.json').write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n')
(HERE/'README.md').write_text('# Pro资料包\n\n[下载ZIP]('+ARCHIVE.name+')\n\n包含完整知识库、研究计算、原文、历次汇报、当前两版草稿、用户与mentor反馈及阅读索引。解压后先读`00-START-HERE.md`。\n\n包内保存当前工作区内容，包含未提交修改；不含运行环境和临时构建。两版final report未获用户认可，这一状态已写入交接说明。\n\n[入口说明](START-HERE.md) · [反馈摘要](FEEDBACK.md) · [包信息与校验](package-info.json)\n')
print(json.dumps(info,ensure_ascii=False,indent=2))
