# 最终汇报

**当前版本：[10月28日前中后台 LLM 应用视觉流程版（英文）](visual-workflows-2026-10-28/DELIVERY.md)**，33页，25.40 × 14.28 cm，可编辑静态 PPTX。页面用角色、资料、处理、产出和人工判断组织图形，详细解释与完整依据放入讲者备注。

- [下载 PPTX](visual-workflows-2026-10-28/output/asset-management-llm-visual-en.pptx)
- [逐页讨论与上屏／讲述安排](visual-workflows-2026-10-28/PAGE-DISCUSSION.md)
- [最终审阅记录](visual-workflows-2026-10-28/FINAL-REVIEW.md)

历史版本：[10月22日面向业务同事的修订稿](revised-2026-10-22/README.md)，32页正文＋6页备查，围绕三套技术方案展开。

下文保留10月20日版本的文件与制作记录。该版本的受众定位和内容编排已被新版重写，原排版检查不构成对演讲适用性的确认。

2026年10月20日。**34页正文＋8页附录**，配套逐页讲稿。

## 成品

- [可编辑PPTX](output/final-report-2026-10-20.pptx)
- [演示PDF](output/final-report-2026-10-20.pdf)
- [逐页讲稿](speaker-notes.md)
- [研究与逐页计划](../../weekly/final-presentation-plan-2026-10-19.md)

正文从公募基金的前中后台工作出发，依次介绍个人Spark、权限知识库和公司共享Agent。各方案在本节讲完使用方式、硬件、上下文与性能、缓存和费用，随后比较三年本地／API成本并安排试点。

| 页码 | 内容 |
|---|---|
| 01–08 | 工作需求、行业案例、贯穿任务、系统分工与模型依据 |
| 09–15 | Spark＋Qwen27，长上下文、缓存、三人共享与费用 |
| 16–18 | NAS权限、Onyx／Milvus自建、统一资源与预算 |
| 19–26 | DeepSeek共享服务、H200／H100／A100、缓存与整机投入 |
| 27–31 | 方案组合、数据处理范围、多轮计费、三年TCO与扩容 |
| 32–34 | 五项试点、业务验收与实施顺序 |
| 35–42 | 模型软件、实测、容量、A100、计费及原始来源 |

## 本轮研究

| 工作包 | 结果 |
|---|---|
| W1 | [统一配置与可复算数字](../../knowledge-base/infrastructure/final-configurations-2026-10-20.md) |
| W2 | [三年TCO与API对照](../../knowledge-base/infrastructure/tco-analysis-2026-10-20.md) |
| W3 | [公开评测](../../knowledge-base/models/public-benchmark-review-2026-10-20.md)、[试点与评价包](../../knowledge-base/pilots/final-pilot-roadmap-2026-10-20.md) |
| W4 | [版本、许可、采购与数据条款核对](../../knowledge-base/infrastructure/final-source-refresh-2026-10-20.md) |

研究代理按用户要求使用GPT-6.1-sol、xhigh。W2完成独立反算；W3采用作者公开榜单并保留模型、任务、指标及运行条件，另准备12个虚构任务及标准答案／验收清单。没有新增GPU或模型任务实测。

## 行文与文件检查

- [中文老师初审](editorial/chinese-teacher-review.md)：逐页审读与正文连读，应用214处文字修订。
- [中文老师视觉复查](editorial/chinese-teacher-final-review.md)：查看全部42页，并复查最后11张变更页。
- [成品检查记录](qa/verification.json)：页码、来源哈希、关键数字、匿名化及PDF文本／链接。
- [PPTX结构检查](qa/finalizer.json)：42页，25个原生表格、5个原生图表，图表含可编辑数据工作簿。

PPTX使用PingFang SC；PDF嵌入字体。性能数字区分用户提供的外部实测、公开回放、工程估算和目标。成本按注明的工作量、计费、汇率和人工假设计算，实际报价、任务质量和使用量可以替换输入后重算。

## 文件与重建

- `data/slides.json`保存最终页序与内容，`data/source-manifest.json`记录输入和讲稿哈希。
- `prepare_content.py`生成初稿，`apply_editorial.py`应用审稿与排版措辞。
- `build.mjs`生成原生PPT对象和预览；`finalize.mjs`检查并包装PPTX。
- `build.sh`重建成品，`verify.py`核对可机器检查的内容。
- `output/`仅放成品；`build/`和渲染图片不入库。

重建使用本机Codex工作区运行时及其Artifact Tool、LibreOffice和Poppler。运行`bash presentation/final-report/build.sh`前应按相应技能标记本次文件创建／编辑；脚本不重复执行技能标记。旧生成文件保存在忽略的`build/previous-*`目录，原有已发布材料保持原样。

本轮未创建新的GitHub Release。
