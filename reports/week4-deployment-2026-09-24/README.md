# 第四周：三套部署方案PDF

[第四周Release：四份PDF](https://github.com/SthMax/quant-intern/releases/tag/phase2-week4-2026-09-24)

资料整理于2026年9月24日。三份PDF分别对应知识库的现行场景Markdown，保留详细方案、表格、计算口径、历史负载对照及来源；架构图按原有节点和连接关系排版。

| 场景 | PDF | 正文来源 |
|---|---|---|
| 1：个人／小组 | [方案PDF](output/pdf/scenario-1-personal-agent.pdf) | [场景一Markdown](../../knowledge-base/infrastructure/scenario-1-personal-agent-2026-09-24.md) |
| 2：公司知识库与RAG | [方案PDF](output/pdf/scenario-2-enterprise-rag.pdf) | [场景二Markdown](../../knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md) |
| 3：公司通用Agent | [方案PDF](output/pdf/scenario-3-company-agent.pdf) | [场景三Markdown](../../knowledge-base/infrastructure/scenario-3-company-agent-2026-09-23.md) |

场景一已并入单6000D、双6000D、M5 Ultra 256GB与DGX Spark比较，采用Qwen3.8-27B FP8权重和完整精度KV。场景二主用Qwen27 FP8；场景三主口径为20任务、每任务262K，正文另保留短负载对照。

演示版见[16页Beamer](../../presentation/week4-deployment-2026-09-24/README.md)。本目录的三份PDF适合详细阅读，slide用于汇报。

## 文件组织

- `output/pdf/`：三份交付PDF。
- `build.sh`、`build.mjs`、`report.css`、`finalize.py`：Markdown排版、图示、PDF导出和校验。
- `qa/source-manifest.json`：三个正文来源及哈希。
- `qa/checks.json`、`qa/review.md`：内容、字体、页边界和视觉检查。
- `build/`及`qa/render/`：忽略跟踪的临时HTML和逐页预览。

## 重新生成

在本目录运行`./build.sh`，使用Codex自带Node／Python、marked和Playwright，以及本机Chrome。无在线字体或脚本依赖。

PDF外部引用指向原网站；三个方案互相链接到同目录PDF。知识库附件使用相对路径，随仓库保留；单独发送PDF时，计算JSON等附件仍由知识库提供。中文字体以嵌入字形保存，复制与搜索使用标准汉字映射。
