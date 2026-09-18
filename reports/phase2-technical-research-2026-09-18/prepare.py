"""Build source labels and preserve evidence identities for the Phase 2 report."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

def expand(path):
    text = path.read_text()
    return re.sub(r"\\input\{([^}]+)\}",
                  lambda m: expand(HERE / (m[1] + '.tex'))
                  if m[1] not in {'preamble', 'reference-labels', 'references'} else '', text)

def esc(value):
    replacements = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%',
                    '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}'}
    return ''.join(replacements.get(c, c) for c in str(value))

titles = {
4: 'Qwen3.8-27B：模型卡、配置与许可', 6: 'Gemma 4 26B A4B：模型卡与配置',
8: 'DeepSeek-V4.1-Flash：模型卡、配置与许可',
9: 'vLLM v0.29.0：固定正式版架构注册表',
10: 'Qwen3.8-27B：vLLM官方部署配置与上游测试构建',
11: 'DeepSeek-V4.1-Flash：vLLM初始支持合并记录', 12: 'Gemma 4：Apache 2.0许可',
13: 'Qwen3.6-35B-A3B：模型卡、配置与许可', 14: 'Gemma 4 31B：模型卡与配置',
15: 'GLM-5.3：模型卡与自定义许可', 16: 'GLM-5.3-Flash：模型卡与MIT许可',
17: 'Kimi K3：模型卡与自定义许可', 18: 'Muse Spark 1.2：多模态能力与开放权重计划',
19: 'Apache License 2.0', 20: 'vLLM：项目与模型服务文档',
21: 'SGLang：项目与服务接口文档', 22: 'TokenSpeed：调度、模型与服务文档',
23: 'MLX-LM：项目与服务实现', 24: 'MLX-VLM：多模态与服务文档',
25: 'llama.cpp：项目与HTTP服务文档', 26: 'KTransformers：异构推理与GLM Flash教程',
27: 'ik_llama.cpp：量化与工具调用文档', 28: 'LangChain：框架概览',
29: 'LangGraph：状态流程、持久运行与人工中断', 30: 'Dify：产品、部署与许可',
31: 'LlamaIndex：项目与文档处理方向', 32: 'Haystack：检索与Agent流程',
33: 'Flowise：产品及分层许可', 34: 'n8n：自动化平台与许可',
35: 'OpenCode：模型连接与权限', 36: 'pi：Agent、模型与执行环境',
37: 'DeepSeek Harness：架构、模型与预览状态', 38: 'Codex CLI：项目许可与官方配置文档',
39: 'Claude Code：许可、网关与企业部署文档', 40: 'TensorRT-LLM：项目与许可',
41: 'Deep Agents：Agent能力与本地模型连接', 42: 'Apple WWDC26：在Mac上运行本地Agent',
43: 'Open WebUI：产品功能与许可', 44: 'LibreChat：Agents与代码执行服务',
45: 'Onyx：研究平台与产品版本', 46: 'RAGFlow：文档与Agent能力',
47: 'Goose：通用任务助手、Recipes与模型连接', 48: 'OpenClaw：个人助手、模型与信任边界',
49: 'Microsoft Agent Framework：项目与BUILD 2026更新', 50: 'AutoGen：维护状态说明',
51: 'Agno：SDK、AgentOS与管理产品', 52: 'CrewAI：Crews、Flows与模型连接',
53: 'AnythingLLM：个人与团队资料应用', 54: 'vLLM v0.29.0：发布记录与服务benchmark参数',
55: 'SGLang：吞吐与内存调优指南',
56: 'Hermes Agent：桌面、记忆与Skills',
57: 'LobeHub：Agent工作空间、自托管与Coding Agent整合',
58: 'Cherry Studio：桌面、Agent运行时与企业版',
59: 'Codex：Skills、MCP、非交互执行与SDK',
60: 'Claude Code与Agent SDK：通用任务、Skills与MCP',
61: 'OpenClaw：团队、记忆与Codex Harness整合',
62: 'Agent Skills：业务方法、脚本与资源格式',
63: 'Model Context Protocol：资料、工具与系统连接',
}

body = expand(HERE / 'main.tex')
ids = list(dict.fromkeys(re.findall(r'\\src\{(TECH-\d+)\}', body)))
labels, entries, manifest = [], [], []
for number, sid in enumerate(ids, 1):
    directory = ROOT / 'knowledge-base/sources' / sid
    meta_path = directory / 'metadata.json'
    meta = json.loads(meta_path.read_text())
    files = []
    for name, spec in meta['files'].items():
        path = directory / name
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != spec['sha256']:
            raise ValueError(f'Source hash mismatch: {path}')
        files.append({'path': str(path.relative_to(ROOT)), 'sha256': digest})
    files.append({'path': str(meta_path.relative_to(ROOT)),
                  'sha256': hashlib.sha256(meta_path.read_bytes()).hexdigest()})
    title = titles[int(sid.split('-')[1])]
    access_date = datetime.fromisoformat(meta['retrieved_at']).astimezone(ZoneInfo('Asia/Shanghai')).date().isoformat()
    snapshot = '资料快照 ' + access_date
    if meta.get('revision'):
        snapshot += '，repo修订 ' + meta['revision'][:12]
    labels.append(r'\expandafter\def\csname refnum@' + sid + r'\endcsname{' + str(number) + '}')
    entries.append(r'\referenceentry{' + sid + '}{' + esc(title) + '}{' + esc(meta['issuer']) + '}{' + esc(snapshot) + '}{' + meta['official_url'] + '}')
    manifest.append({'id': sid, 'number': number, 'title': title, 'url': meta['official_url'],
                     'revision': meta.get('revision'), 'retrieved_at': meta['retrieved_at'],
                     'files': files})

(HERE / 'reference-labels.tex').write_text('\n'.join(labels) + '\n')
(HERE / 'references.tex').write_text('\n'.join(entries) + '\n')
(HERE / 'data/source-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
models = []
for n in [4, 13, 14, 6, 8, 16, 15, 17]:
    d = ROOT / f'knowledge-base/sources/TECH-{n:03d}'
    m = json.loads((d / 'metadata.json').read_text())
    size = json.loads((d / 'model.safetensors.index.json').read_text())['metadata']['total_size']
    models.append({'id': m['source_id'], 'model': m['model_id'], 'tensor_bytes': size,
                   'decimal_gb': round(size / 1e9, 2), 'revision': m['revision']})
(HERE / 'data/model-artifacts.json').write_text(json.dumps(models, ensure_ascii=False, indent=2) + '\n')
print(f'Prepared {len(ids)} references and eight model artifact records.')
