# D 修订版：证据与讲述安排

正文：[extended-draft-d-revised.md](extended-draft-d-revised.md)。本轮原因说明与修改记录：[d-revision-response-for-user.md](d-revision-response-for-user.md)。旧稿与骨架保留。

本轮修订日期为 **2026-10-22**。能力评价统一采用 **GDPval-AA v2.1**，从用户指定页面和 Artificial Analysis 官方方法、模型对照页核对；其他部署与费用数据沿用已核对的知识库来源。正文共 **46 页，其中正文 38 页、封面 1 页、目录 1 页、章节页 6 页**，安排 **40 分钟**。以下记录供复核和制作使用。

## 1. 本轮新增的能力评价依据

实际访问了用户指定的 [GDPval-AA 页面与任务示例](https://artificialanalysis.ai/evaluations/gdpval-aa#example-tasks)，并用 defuddle 读取正文。另打开 [Artificial Analysis 官方方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)，阅读 GDPval-AA v2.1 部分。

采用的评测事实：AA 使用 GDPval 公开 gold 集中的220项任务，覆盖44种职业、9个行业；Stirrup提供代码、文件与网络工具；提交文件后，同题产物匿名配对，由模型评审比较质量并拟合Elo。v2.1将DeepSeek V4.1 Flash（max）固定为1600作为刻度锚点。该页引用的原GDPval论文介绍完整1320任务集；本稿使用AA实际评价的220项与AA的Elo定义。

实际阅读的示例是 **Band Stage Plot**：根据五位成员的演出设备与监听需求，交付一页舞台布置PDF，包含位置、输入输出与编号。新第20页用它说明完整工作产物的要求，表述为任务介绍。

### 分数、模型身份与日期

以下全部于 **2026-10-22** 读取，使用页面明确标注的 **GDPval-AA v2.1**。括号内保留AA推理标签；发布月份来自相应页面的Release Date字段，读取日期与模型发布日期分别记录。

| 正文模型标签 | Elo | 页面标注的模型发布月份 | 直接核对位置 |
| --- | ---: | --- | --- |
| DeepSeek V4.1 Flash 1017（Max） | 1746 | 2026-10 | [GDPval-AA榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)，该行CI为±21 |
| GLM-5.3-Flash | 1642 | 2026-08 | [GLM／Kimi官方对照](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-kimi-k3)，GDPval-AA v2.1行 |
| MiMo-V2.6-Flash | 1607 | 2026-09 | [MiMo／Qwen官方对照](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-qwen3-8-27b)，同名行 |
| DeepSeek V4.1 Flash（Max） | 1600 | 2026-09 | [DeepSeek／Qwen官方对照](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-vs-qwen3-8-27b)，同名行 |
| Kimi K3（Max） | 1533 | 2026-07 | [GLM／Kimi官方对照](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-kimi-k3)，同名行 |
| Qwen3.8 27B（Xhigh） | 1417 | 2026-08 | [DeepSeek／Qwen官方对照](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-vs-qwen3-8-27b)，与其余Qwen对照页一致 |
| Gemma 4 31B（Reasoning） | 620 | 2026-04 | [Qwen／Gemma官方对照](https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-gemma-4-31b)，同名行 |

这七个展示条目均有相应AA结果。Qwen在10月20日归档中的1420已更新为本次页面的1417。DeepSeek原版、1017、非推理版本各有独立标签，本稿选择表中明确列出的条目。GLM Flash和MiMo Flash沿用AA未加effort后缀的标签。公开模型对照页提供的是端点评测标签，权重SHA缺项记录在此。

方法与页面均在本轮实际读取，分数来自可见的GDPval-AA v2.1行；正文模型选择依此重新组织。Finance Agent、ExtractBench、AutomationBench和Terminal-Bench的旧能力分数已从修订稿移除。

## 2. 三角图与概念顺序的依据

新第11页由财报过程提出材料、分析与等待三个要求；第12页用完整Mermaid三角图呈现相互关系，并在同页说明资源机制；第13–15页依次解释上下文、能力与速度。图的三个顶点及三条关系线都已经写入正文。

三角的比较条件写为给定硬件、并发规模与运行方式。机制包括长输入的计算与状态开销、更多推理步骤所需时间，以及计算量较大的候选所需资源。技术依据沿用[AI Infra原书第3章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/03-推理与训练负载.md)与[第8章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/08-推理优化.md)，固定修订`3bdcb4fcab73010eeaccf31cc10a8242a895d82e`。新第22、29页的Spark长度变化数据提供本次运行范围内的实际例子。

## 3. 逐段来源与关键数值

| 修订页码 | 采用内容 | 对应来源与定位 |
| --- | --- | --- |
| 1–4、6–17 | 研究任务、应用条件、概念和规划目标 | initial与guide；[最终配置研究](../../../knowledge-base/infrastructure/final-configurations-2026-10-20.md)的场景、长度与服务目标；第9页是任务要求的呈现 |
| 5 | MENTOR公开研究路径 | [FUND-113原文](../../../knowledge-base/sources/FUND-113/original.md)，PDF pp.1–2；[DOI](https://doi.org/10.1631/FITEE.2500608) |
| 5 | 盈米文档预审与修改流程 | [固定客户端README](https://github.com/yingmi-dev/content-compliance-skill/blob/040df66202f6075cdeadb450e502c7a19c83dabf/README.md)；[公司入口当前指向的发布页](https://www.chnfund.com/article/AR8e4e17e8-252c-d5d6-2eb7-3a20162a0343)，页标2026-03-19 |
| 5 | 易方达开发测试案例 | [FUND-101原文](../../../knowledge-base/sources/FUND-101/original.md)，PDF p.4／印刷p.3；[协会PDF](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337815959196.pdf) |
| 18、20–21、23 | 能力评价与模型选择 | 本文件第1节的GDPval-AA官方页面；模型选择同时结合窗口与设备资源 |
| 19 | Qwen262,144原生、1M扩展；DeepSeek1M | [Qwen卡片归档](../../../knowledge-base/sources/TECH-092/models/qwen27/README.md)，Model Overview／Processing Ultra-Long Texts；[DeepSeek卡片](../../../knowledge-base/sources/TECH-092/models/deepseek/README.md)；253,952＝262,144−8,192 |
| 22、27、29–30、33 | Spark速度、等待、三路并发、MTP配置诊断 | [TECH-076提供方总结](../../../knowledge-base/sources/TECH-076/original.md)，单请求／三请求／长度诊断表 |
| 25–28、30、33 | 请求流程、内存、prefill／decode、调度与缓存 | [AI Infra第3章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/03-推理与训练负载.md)、[第8章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/08-推理优化.md)；410秒由8,192÷20取整 |
| 31 | 制品字节、Engram与多卡缓存 | [TECH-079制品记录](../../../knowledge-base/sources/TECH-079/original.md)；[最终配置研究§5](../../../knowledge-base/infrastructure/final-configurations-2026-10-20.md) |
| 32、35 | 框架、A100路线与同机DP共享 | [vLLM原文](../../../knowledge-base/sources/TECH-020/original.md)、[SGLang原文](../../../knowledge-base/sources/TECH-021/original.md)、[A100专项](../../../knowledge-base/infrastructure/deepseek-a100-project-review-2026-10-12.md)、[vLLM 0.32.0 release](https://github.com/vllm-project/vllm/releases/tag/v0.32.0)、[Engram文档](../../../knowledge-base/sources/TECH-089/vllm-0.32-engram.md) |
| 34 | DeepSeek AgentX回放 | [TECH-084公开API原件](../../../knowledge-base/sources/TECH-084/benchmarks.json)、[整理CSV](../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/company-replay.csv)，行442757／442751／442758 |
| 37 | 20份与40份会话容量 | [容量CSV](../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/company-capacity.csv)，严格post-graph预算与10%余量列 |
| 38–41 | 三年预算、配置增量、扩容与A100复用 | [TCO研究](../../../knowledge-base/infrastructure/tco-analysis-2026-10-20.md)、[输入](../../../knowledge-base/infrastructure/data/tco-2026-10-20/inputs.json)、[总表CSV](../../../knowledge-base/infrastructure/data/tco-2026-10-20/summary.csv)、[硬件台账](../../../knowledge-base/infrastructure/data/hardware-prices-2026-10-12.json) |
| 43–44 | 使用入口、执行位置、RAG、Skills与MCP | [Hermes接入](../../../knowledge-base/sources/TECH-072/open-webui.md)、[权限文档](../../../knowledge-base/sources/TECH-068/onyx-permissions.md)、[知识库方案](../../../knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md)、[Skills](../../../knowledge-base/sources/TECH-072/skills.md)、[MCP](../../../knowledge-base/sources/TECH-072/mcp.md) |
| 45–46 | 任务验证和全场收束 | 本轮依据前文形成的建议；下一步按实际产物、等待与人工时间评价 |

### 数值的实际身份

- Spark：用户于10月12日提供的外部随机token测量汇总；FP8权重、FP8 KV、MTP3、FlashInfer、关闭前缀缓存。50K／100K各两次，300K／500K各一次。原始环境、启动脚本与逐请求日志仍待提供。修订稿保留直接说明运行条件的句子，删除无帮助的末尾辩解，1M短输出容量样本整段退出本稿。
- MTP：300K的5.80→17.23来自草稿长度配置修复，接受率0→99.4%；正文按诊断过程讲述，采用精确值262,144的原始记录，正文以262K简称。
- 共享回放：旧镜像`nightly-cd10ed6f9f6b37a8ace9cf380007e66fe12ec0c3`，高缓存AgentX、合成DSpark接受长度3.51；正文开头直接列运行条件。数据按端到端系统输出与p95 TTFT呈现。
- 制品与容量：510.286GB、202.758GB、307.528GB为十进制制品字节账；global KV按1,827 B/token/rank，20×1M＝36.54GB/rank。容量表使用旧启动池按严格图后预算线性缩放、再留10%token余量，20份为242,240／762,048／1M／1M，TP8下40份为635,584。它们在正文明确作为容量估算进入方案。
- 成本：三年计划任务2482.5与95312.5，显示约2483与95313；个人本地／API为9.05／1.66万元，公司为392.54／68.34万元。公司GPU297.36万元，运维45万元；含实施、工具CPU和持续运行，采用相同计划交付量。模型与路线的真实业务质量、重试和复核时间在下一阶段测量。
- 扩容：每项任务273,240未缓存输入、17,600输出；假设8,000输入tokens/s与400输出tokens/s，机时78.155秒。5,040,000年可用秒÷78.155＝64,487.24项。高工作量第二年扩容，三年712.78万元。H100／H200同口径硬件预算差56,826元；实际交付仍通过供应商报价确定。A100复用三年134.42万元沿用改造与维护预算。

## 4. 页数、调整与时间

相对旧D增加两页：概念部分用五页完成原11–14页的讲述任务；能力比较用独立的任务／方法页和成绩页展开。六章顺序保持，章节页为3、8、16、24、36、42。

| 分块 | 页码 | 时间 |
| --- | --- | ---: |
| 开场与目录 | 1–2 | 0:45 |
| 金融工作与本地需求 | 3–7 | 3:00 |
| 任务与三维取舍 | 8–15 | 6:15 |
| 模型选型 | 16–23 | 7:15 |
| 运行环境与性能 | 24–35 | 12:15 |
| 资源与成本 | 36–41 | 6:15 |
| 使用与收束 | 42–46 | 4:15 |
| 合计 | 1–46 | 40:00 |

### 逐页预算

| 页 | 页类 | 时间 | 累计 |
| ---: | --- | ---: | ---: |
| 1 | 封面 | 0:15 | 0:15 |
| 2 | 目录 | 0:30 | 0:45 |
| 3 | 章节页 | 0:15 | 1:00 |
| 4 | 正文 | 0:30 | 1:30 |
| 5 | 正文 | 1:00 | 2:30 |
| 6 | 正文 | 0:30 | 3:00 |
| 7 | 正文 | 0:45 | 3:45 |
| 8 | 章节页 | 0:15 | 4:00 |
| 9 | 正文 | 0:45 | 4:45 |
| 10 | 正文 | 0:45 | 5:30 |
| 11 | 正文 | 0:45 | 6:15 |
| 12 | 正文 | 1:15 | 7:30 |
| 13 | 正文 | 0:45 | 8:15 |
| 14 | 正文 | 0:45 | 9:00 |
| 15 | 正文 | 1:00 | 10:00 |
| 16 | 章节页 | 0:15 | 10:15 |
| 17 | 正文 | 1:00 | 11:15 |
| 18 | 正文 | 0:45 | 12:00 |
| 19 | 正文 | 0:45 | 12:45 |
| 20 | 正文 | 1:00 | 13:45 |
| 21 | 正文 | 1:15 | 15:00 |
| 22 | 正文 | 1:15 | 16:15 |
| 23 | 正文 | 1:00 | 17:15 |
| 24 | 章节页 | 0:15 | 17:30 |
| 25 | 正文 | 1:00 | 18:30 |
| 26 | 正文 | 1:00 | 19:30 |
| 27 | 正文 | 1:00 | 20:30 |
| 28 | 正文 | 1:00 | 21:30 |
| 29 | 正文 | 1:15 | 22:45 |
| 30 | 正文 | 1:15 | 24:00 |
| 31 | 正文 | 1:15 | 25:15 |
| 32 | 正文 | 1:00 | 26:15 |
| 33 | 正文 | 1:00 | 27:15 |
| 34 | 正文 | 1:15 | 28:30 |
| 35 | 正文 | 1:00 | 29:30 |
| 36 | 章节页 | 0:15 | 29:45 |
| 37 | 正文 | 1:00 | 30:45 |
| 38 | 正文 | 1:15 | 32:00 |
| 39 | 正文 | 1:30 | 33:30 |
| 40 | 正文 | 1:15 | 34:45 |
| 41 | 正文 | 1:00 | 35:45 |
| 42 | 章节页 | 0:15 | 36:00 |
| 43 | 正文 | 0:45 | 36:45 |
| 44 | 正文 | 1:00 | 37:45 |
| 45 | 正文 | 1:15 | 39:00 |
| 46 | 正文·结尾 | 1:00 | 40:00 |

正文预算37:45，封面／目录0:45，章节页合计1:30。这是按阅读、看图与解释步骤分配的演讲预算。

## 5. 本轮完成检查

修订正文完成后，按第1–46页实际通读，随后逐页单独检查末句、表格标签、图示文字与括号。用户本轮三项要求再次独立核对：全稿删除防御性收尾及同类语义；财报任务后立即进入三角图与资源解释，再展开三维；能力比较采用已实际读取和核对的GDPval-AA。正文没有脚注，也没有把删除内容移成小字或括号。

本轮进一步检查了页码连续性、六章与目录对应、时间加总及本文件本地链接。旧初稿、指南、骨架和旧D三份文件保持原状。研究扩充限于GDPval-AA及其官方方法和候选模型数据，其余采用原有已核事实。
