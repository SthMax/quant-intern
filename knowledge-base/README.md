# Knowledge Base

> 2026-09-24更新[场景一四配置比较](infrastructure/scenario-1-speed-target-review-2026-09-24.md)：单6000D、双6000D、M5 Ultra 256GB、DGX Spark；统一Qwen3.8-27B FP8权重及完整精度KV，以单人20+为目标，列出人民币整机预算、131K／262K／524K速度及缓存容量。含36组主情景和单卡95%显存分支；[Beamer演示稿](../presentation/week4-deployment-2026-09-24/README.md)及[三份详细方案PDF](../reports/week4-deployment-2026-09-24/README.md)已同步。

> 2026-09-24按反馈统一现行编号：**1个人／小组、2公司知识库、3公司通用Agent**。个人与知识库主用Qwen3.8-27B，权重至少8-bit；个人按131K／262K／524K满窗口计算，公司通用Agent以每任务262K、20并发为主口径，并提供5／20／30／50任务的context上限。见[Beamer演示稿](../presentation/week4-deployment-2026-09-24/README.md)及下列方案。模型／价格原始来源保留，当前200个来源ID。

> 2026-09-23更新[场景二计算](infrastructure/scenario-2-enterprise-rag-2026-09-23.md)：补齐prefill、decode、每路速度与KV总context，统一90%显存和15%缓存开销；120组性能情景中105组满足预算，15组H1／35B另标边界，95%紧配单列；另有40组context容量。正文以8K问答、32K长资料和20并发为主，平台与价格沿用原方案。

> 2026-09-23完成[场景三：公司共享模型＋通用Agent](infrastructure/scenario-3-company-agent-2026-09-23.md)，以Hermes、Skills／MCP和隔离执行为主线，比较集中与桌面执行。文档列六个资源档、三类完整任务、增量／合并预算；[432组任务模拟](infrastructure/data/scenario-3-agent-2026-09-23/)计入工具排队、上下文增长、缓存回收及子任务敏感性。新增TECH-072–074，当前199项：180主阅读、15辅助、4来源链。性能为未校准分析模拟。

> 2026-09-23完成[场景二：Onyx Enterprise与Milvus自建RAG两条方案](infrastructure/scenario-2-enterprise-rag-2026-09-23.md)。涵盖NAS权限、Office／PDF入库、模型、四档硬件、项目预算，以及1／5／20／30／50并发下的响应与吞吐分析计算；[参数与复算脚本](infrastructure/data/scenario-2-rag-2026-09-23/)保留120组情景，均未作GPU实测校准。新增TECH-068–071，当前196项：177主阅读、15辅助、4来源链。下一步讨论场景三。

> 2026-09-22完成[MiMo-V2.6 Pro／Flash详细研究](models/mimo-v2.6-research-2026-09-22.md)，加入[当前10模型候选池](models/model-survey-2026-09-16.md)。比较非coding Agent能力、GLM参数与权重、MXFP4、KV、DFlash及四／八卡部署；[许可专项](models/license-review-2026-09-16.md)同步。新增TECH-064–067，当前192项：173主阅读、15辅助、4来源链。原第三周报告保留其发布时快照。

> 2026-09-21新增[中国境内部署的服务器GPU采购研究](infrastructure/server-gpu-procurement-2026-09-21.md)，覆盖NVIDIA／AMD型号、地区SKU、出口许可及原厂供货披露。现已补充七套四／八卡整机预算，并完成[个人／三人工作站配置与价格](infrastructure/workstation-configurations-2026-09-21.md)。公开价、境外换算与分析估算分别标识，逐项计算保存在[硬件价格JSON](infrastructure/data/hardware-prices-2026-09-21.json)，接入[参考架构](infrastructure/reference-architecture.md)和[TCO输入](infrastructure/tco-model.md)。本轮为第四周工作资料，原TECH索引数量保持不变。

> 2026-09-18新增[Harness比较与Coding Agent工作流研究](infrastructure/harness-survey-2026-09-17.md)：Open WebUI/LobeHub/Cherry Studio、Hermes/OpenClaw，以及Skills/MCP与通用执行环境。新增TECH-056–063；当前188项：169主阅读、15辅助、4来源链。修改前检查点为`d3057af`。

> 2026-09-18在检查点`9e5c2fe`后深化[非coding Harness与应用调研](infrastructure/harness-survey-2026-09-17.md)，正文按产品用途、优点和基金业务用法重写；[Serving调研](infrastructure/serving-framework-survey-2026-09-17.md)增加任务负载和时延达标吞吐比较。该轮索引180项：161主阅读、15辅助、4来源链。

> 2026-09-17新增[Serving framework调研](infrastructure/serving-framework-survey-2026-09-17.md)与[Harness调研](infrastructure/harness-survey-2026-09-17.md)。当日总索引167项：149主阅读、14辅助、4来源链。新增23组官方软件/许可来源，明确框架能力、API兼容和实际运行验证的区别。

> 2026-09-16确定主线：**面向专业个人工作站与共享服务的模型研究**。见[重排后的8模型候选](models/model-survey-2026-09-16.md)、[许可专项](models/license-review-2026-09-16.md)及[第3–5周研究计划](../weekly/week-03-05-plan.md)。当日累计新增19项官方技术/许可来源、总索引144项，首轮5项模型资料转历史辅助；报告修订按[独立计划](../reports/phase1-llm-industry-2026-09-09/editorial/fixing-plan.md)推进。

以下为Phase 1资料积累的历史说明。

> 2026-09-11新增[DeepSeek-V4.1-Flash技术报告与中文分析](models/deepseek-v4.1-flash/README.md)，归入Phase 2模型技术资料。

> Phase 1量化专题范围：**2026年基金公司LLM量化三方向**，API方案可作案例，本地部署加分；部署层与Agent层分开评估。见[案例矩阵](companies/quant-research-2026-09-09.md)。

> 本地LLM目标的研究结果：[任务、代码、部署依赖与评价方案](models/local-llm-poc-evidence-2026-09-09.md)。尚未进入实际GPU部署。

> 当前报告聚焦**LLM及LLM参与的量化流程**，见[范围纠正与入选表](companies/llm-report-scope-2026-09-09.md)。历史广义AI分数不可直接作为LLM排名。

> 新增[非易方达案例与报告平衡建议](companies/case-diversity-2026-09-09.md)：已考虑mentor和量化部门读者，报告正文尚未开始撰写。

> 新增[量化重点研究](companies/quant-research-2026-09-09.md)：标签期限优化、自动因子研发、新闻事件轮动及组合约束。

> 2026-09-09 已整合[重点公司技术研究](companies/focused-research-2026-09-09.md)与[监管／研究复核](regulation/review-results-2026-09-09.md)：[默认阅读索引](reading-index.json)列出112个主阅读记录、9个辅助记录、4个来源链索引。全文检索按reading_path执行；原先清理范围与结果见[清理审查](audits/2026-09-08-relevance-cleanup/README.md)。

> 2026-09-08 微信入库完成：4篇相关研究文章现均已入库，华泰柏瑞由用户保存的5页PDF补齐；3条无关推荐继续排除。见[文章目录](sources/wechat-articles/README.md)及[华泰柏瑞核对报告](audits/2026-09-08-huatai-pdf/README.md)。

提取质量与分析风险：[本次核查、微信Skill测试及更清晰的阅读副本](audits/2026-09-07-extraction-quality/README.md)。

最新来源恢复：[内部浏览器与深搜复核结果](audits/2026-09-07-source-recovery/README.md)。

This folder holds research findings and their evidence. Project scope is
controlled by [the final project plan](../PROJECT_PLAN.md). Current execution is
tracked in [the Weeks 3–5 plan](../weekly/week-03-05-plan.md); the
[Week 2 plan](../weekly/week-02-plan.md) retains the Phase 1 record.

## 原始来源与研究分析 / Original sources and analysis

**来源按原语言保存：中文原文保留中文，英文原文保留英文。英文摘要、翻译和研究者分析均不能代替原始来源。**

The [original-source archive](sources/README.md) holds downloaded source files,
original-language text extractions and per-source retrieval metadata. The
[7 September audit and complete change table](audits/2026-09-07-language-audit/changes.md)
records every baseline file and registered source, including unavailable originals.

- `sources/<source_id>/source.pdf` or `source.html`: downloaded original bytes;
  HTTP compression may be decoded by curl. PDFs preserve figures and page layout.
- `original.md`: mechanically extracted original-language text, never a back-translation.
  It may lose layout, images, footnotes or dynamic content; the source file governs.
- `metadata.json`: exact requested/final URLs, retrieval time, SHA-256, extraction
  method, original evidence state, access/quality limits and pending human review.
- `retrieval-response.*`: an error, challenge or wrong-page response, **not** an
  archived original. A failed request does not disprove a prior disclosure.
- Company dossiers, synthesis documents and plans are authored research. Their
  labelled summaries and interpretations are separate from the linked originals.

Source availability and provenance are separate. Archiving a media report or
repost preserves that publication; it does not verify an inaccessible company
original, establish a primary deployment claim, or complete legal-status review.
English originals remain English. Do not manufacture Chinese “originals” by
translating our earlier English notes.

## Phase ownership

| Folder | Phase | Purpose |
|---|---|---|
| companies/ | 1 — Weeks 1–2 | Onshore AI/LLM disclosures, size categories, use cases, partners, and reported outcomes |
| regulation/ | 1 — Weeks 1–2; maintained later | Public regulatory evidence and model risk management questions |
| models/ | 2 — Weeks 3–5 | 5–8-model survey, reusable evaluation framework, one-model GPU proof of concept |
| infrastructure/ | 2 and 3 | Phase 2 reference architecture; Phase 3 three-year on-premise/API TCO |
| pilots/ | 3 — Weeks 6–8 | 3–5 candidates and roadmap with 2–5 concrete proposals |
| templates/ | All | Evidence recording and review |

## Evidence states

- **candidate:** discovered but not checked against the original source.
- **verified-primary:** original primary material was opened and the specific
  claim, identity, date, and location were checked.
- **corroborated:** verified-primary evidence with an additional independent
  supporting source.
- **unresolved:** ambiguous, inaccessible, superseded, or conflicting evidence
  prevents the proposed claim from being verified.

Only verified-primary and corroborated claims may appear as facts in the main
presentation. A primary vendor source supports what the vendor reported; it does
not automatically establish independently measured customer outcomes.

Record who checked the source. Agent inspection and user/manual verification are
separate: use a human-check status and date without implying human review
occurred merely because a link is available.

## Required citation fields

Each source in [source-register.md](source-register.md) needs:

- Stable source ID, exact title, issuer, and source/instrument type.
- Publication date; for rules, effective date and amendment/current status.
- Direct primary URL and access date.
- Relevant article, section, page, or timestamp.
- Narrow supported claim and limitations.
- Evidence state and a link to the detailed evidence note.
- In that note, reviewer/method and human-check status.

Use “not stated” or “not yet verified” for absent or unresolved dates. Never infer
an effective date or legal force from the publication date or document title.

## Workflow

1. Log a candidate and its discovery source.
2. Open the original source and check the exact claim and its context.
3. Save the source file and original-language extraction under `sources/<source_id>/`;
   record retrieval metadata and check that the cited passage survives extraction.
   Save an evidence note using [the template](templates/evidence-note.md), then
   update the source register and relevant index.
4. Record findings as research proceeds, so slides never become the only record.
5. Keep source wording, interpretation, and open applicability questions explicit.
6. Before presentation release, follow every material claim's links to the
   original passage; record reviewer and result.
7. Update counts and report unresolved/manual-review items honestly.

The overview supplied in the final project plan is project context, not a
verified industry research finding. Source its claims before reusing them as
evidence.

## Citation discipline

- Prefer authoritative Chinese originals; translations are aids.
- Search snippets and reposts may support discovery, not legal conclusions.
- Distinguish law/rules, regulator guidance, drafts, industry material, vendor
  claims, and internal requirements.
- Verify instrument status and applicability separately.
- Preserve exact source wording and section/page pointers. Use selected original
  passages in evidence notes and link the full archived original; summaries and
  translations must be labelled as authored research.
- Record AUM unit, metric, entity scope, date, and source. Compare compatible
  measurements and label gaps.
- Distinguish announcement, pilot, and production use.
- Absence of a disclosure does not establish absence of adoption.

## Data handling

Use public information in this repository. Do not place confidential internal,
client, personal, portfolio/position, or licensed research data here without the
user's explicit direction and an authorized storage basis. Track internal-policy
questions without copying restricted text. COD is the host organization's infrastructure; MRM
means model risk management. Those clarifications do not supply architecture
specifications or internal policy content.
