# C 修订版：证据与讲述安排

正文：[extended-draft-c-revised.md](extended-draft-c-revised.md)。35 页，含封面和结尾，讲述预算 40 分钟，问答另计。

本轮完整阅读了最新 [initial-draft.md](initial-draft.md)、[阅读体验反馈](c-reading-experience-feedback-for-user.md)、C 原稿及原证据。修订保持既有研究范围，重点重写叙述和表达。原 C、原证据、initial draft、审稿文件与知识库均保留原样。没有读取 A/B 全文或旧 session，也没有重新开展全面研究。

事实和价格沿用截至 2026-10-20 的知识库快照。数据身份直接写在正文对象上：公开评测、外部测量、容量估算、服务目标、三年预算。这里保存详细出处、测量配置、计算过程与本轮未覆盖事项。

## 讲述时间与取舍

以下时间按本页需要解释的实际动作分配。开场和入口页简短，计算、调度和资源布局留出读图时间。讲述重点是解释图中的关系、关键数字和选择，参考参数无需逐项念出。

| 页 | 秒 | 讲述重点 |
|---:|---:|---|
| 01 | 20 | 公司需求与研究主题 |
| 02 | 35 | 公告、财报和代码三个工作动作 |
| 03 | 55 | 三个真实岗位应用，各约十五秒 |
| 04 | 40 | 资料来源怎样带出运行环境 |
| 05 | 60 | 读懂任务，再用重述数字解释比较口径 |
| 06 | 50 | 权重与本次材料怎样进入推理 |
| 07 | 60 | 窗口组成与262K预算算例 |
| 08 | 55 | 能力表现和三种速度感受 |
| 09 | 65 | 固定资源怎样形成取舍 |
| 10 | 60 | 个人和共享两组服务要求 |
| 11 | 90 | 先解释结构和精度，再读主要候选 |
| 12 | 85 | 提取任务、F1和长度分组，主读Qwen两行 |
| 13 | 55 | 长材料问答的任务与分数 |
| 14 | 65 | 工具工作与关键项评分，原版和1017分列 |
| 15 | 60 | 两段选择理由 |
| 16 | 60 | 沿一次请求与工具返回环路读图 |
| 17 | 85 | prefill、decode和合批读取关系 |
| 18 | 80 | KV随长度增长，以及完整内存组成 |
| 19 | 55 | 服务职责怎样对应框架选择 |
| 20 | 90 | 分别读等待和速度，独立交代容量样本 |
| 21 | 65 | 草稿长度故障与修正过程 |
| 22 | 90 | 驻留、共同窗口及分块调度三个层次 |
| 23 | 80 | 首次、继续和恢复的时间顺序 |
| 24 | 90 | 权重树与每卡KV的算式 |
| 25 | 105 | 八卡分组、Engram共享和40份历史的来由 |
| 26 | 85 | 一个公开回放，再读满窗口目标 |
| 27 | 75 | 同机两步增量，各增加了什么 |
| 28 | 85 | 主要硬件预算与支持规模 |
| 29 | 100 | 前三轮输入累计，再交代总工作量假设 |
| 30 | 95 | 公司预算构成、个人金额和建设范围 |
| 31 | 95 | 年度任务增长与第二年的扩容 |
| 32 | 65 | 已有设备和净人工时间 |
| 33 | 55 | 文件、身份、检索和引用的流程 |
| 34 | 45 | 工具循环与最终产物 |
| 35 | 45 | 收回模型、服务与实际采用范围 |
| **合计** | **2,400** | **40 分钟** |

## 逐页来源与采用范围

### 01–04：用途、案例与公司环境

**01**：研究出发点来自 initial draft，机构匿名。

**02**：[公开能力研究][bench] 的任务分类与 [本地研究][local]。文字描述应用方式，没有填入公司效果数据。

**03**：[鹏华原文][penghua] 物理第5–7页和 [永赢原文][maxwealth] 第1–2页。鹏华投研输入对应公告、新闻、研报，产物对应标签、舆情要点、摘要。营销物料审核提供修改建议。永赢的邮件输入和检测链路保持原披露对象。前中后台为本稿按职责归类，机构公开披露的身份随页说明。

**04**：initial draft 与 [参考架构][architecture]、[来源核查][refresh] 第6节。使用环境是研究要求，本轮没有对公司既有系统完成上线审查。

### 05–10：任务、概念与要求

**05**：任务参考 [公开能力研究][bench] 第4节。新增120／90／100亿元完全为教学数字，采用反馈给出的重述示例。比较分母100亿元，增长20%。原披露90保留用于说明重述背景。该页没有引用真实公司的财务结果。

**06**：[模型研究][models] 与 [Serving调研][serving]。权重来自训练，当前财报与问题作为输入，图中推理产生输出。删除原来的重复定义表。

**07**：[最终配置][config] 第1节。四档总窗口为131072／262144／524288／1000000。输出预留8192，对应输入历史122880／253952／516096／991808。正文展开262K一档，其余预算保留这里。模型官方1,048,576上限在候选页按原值列出。

**08**：[Spark原始汇总][sparkraw] 与 [Serving调研][serving]。TTFT计入网络、校验、排队、prefill和首步生成。decode采用首token之后的生成阶段，吞吐另按测量窗口解释。

**09**：取舍依据 [模型研究][models]、[最终配置][config]。比喻限定在本轮候选与运行资源内。架构和优化可以改善资源使用；本页没有建立参数量与能力的单调关系。

**10**：[最终配置][config] 第1、2、5、6节。两组为分析配置和服务目标，单人20、共享每路10／20均为目标。H200、NVSwitch与1536GB主存保持对应关系。设备采购和公司服务验收在本轮范围之外。

### 11–15：模型比较与选择

**11**：[模型研究][models] 第3节、[Qwen模型卡][qwencard]、[DeepSeek模型卡][dscard]。B为十亿参数；稠密与MoE的解释先于候选表。BF16／FP8是数字存储格式，模型制品常含多种张量格式。表格字节来自归档索引，Qwen主方案FP8与表内BF16基础体量明确标注。MiMo主索引之外还有DFlash／音频制品。GB为10^9字节。

**12**：[ExtractBench作者CSV][extractcsv]、[README][extractreadme]、[公开能力研究][bench]第2.2节。370文档中252／98／20分别为短／中／长，全集按文档等权。指标为value F1×100。正文保留端点、输入方式与思考设置。详细条件：Qwen27／35自托管vLLM、FP8，150dpi逐页图像，最大输出32768；DeepSeek API同分辨率图像、关闭思考、最大输出65536；GLM API原文件、开启思考、最大输出131072。各配置temperature=0、JSON object、一次提取。Qwen思考采用端点默认，GLM effort未单列。这组证据评价英文企业文档完整流程。

**13**：[AA归档][aaoriginal]、[条件记录][conditions]、[公开能力研究][bench]第2.3节。AA-LCR v1.1为100题约100K多文档问答，每题3次；保留各模型公开思考档位。当前资料未完整披露每个历史运行权重SHA。这里只使用该任务范围内的分数。

**14**：[Vals方法原文][valsmethod]、[原HTML][valshtml]和[CSV][financecsv]。主指标dealbreaker-gated severity-weighted Partial Credit，关键项失败整题零分。同一默认harness六工具，2小时限时，页面更新10月18日。逐模型thinking、精度、权重SHA披露存在缺项。正文给描述性数值，未开展统计显著性判断。Gemma旧v1.1数值保持在该页之外。

**15**：综合 [公开能力研究][bench]、[最终配置][config]、[刷新核查][refresh]形成研究选择。Qwen以提取与长文能力、个人设备速度为依据，DeepSeek结合能力与已经研究的资源/运行路线。GLM Flash和MiMo Flash保留为金融任务对照。

1017升级候选的开放权重和MIT许可见[制品对照][artifacts]及刷新核查。原版和1017该次config、索引和LICENSE相同，权重值未下载比较。性能数据继续以原版身份出现，Spark约100K速度来自外部随机输入。公司同题质量评测是后续阶段工作。

### 16–19：运行机制与框架

**16**：[Serving调研][serving]、[A100专项][a100]第1.3节。图中框架职责由引导句表达，计算顺序为prefill再decode。应用执行工具后将新结果返回队列。推理引擎没有被画成一个独立于prefill/decode的中间计算阶段。

**17**：同源机制解释。新增公式是同一稠密模型、各请求历史独立、以权重及历史读取作主项的简化模型。它解释合批中的权重复用，实际吞吐还受算子、临时空间、通信、调度及带宽利用率影响。MoE和推测解码的完整成本分别由具体实现决定。

**18**：[最终配置][config]第3节、[载荷数据][restorecsv]。全注意力KV为65536／32768 B/token，两列由长度直接相乘得到。正文资源树把其他状态、草稿、分页、计算与调度空间列为组成项。FP16同为16位，已在列名写明。FP8 KV的实际业务质量保留在后续验证范围。

**19**：[Serving调研][serving]、[vLLM0.32发布][vllmrelease]和[A100专项][a100]。研究选择vLLM主线、SGLang对照、modified vLLM用于旧架构，个人设备另有MLX／llama.cpp路径。没有进行框架同机速度排名。版本注采用10月20日冻结状态。

### 20–23：Spark、调度与状态续用

**20**：[TECH-076原始汇总][sparkraw]。数据来自用户10月12日提供的朋友设备测试，主测试日期未知，环境文件、完整引擎版本和逐请求原始日志尚未导入知识库。本项目没有复跑。

单GB10、TP1、FP8权重、默认尺度FP8 KV、MTP3、FlashInfer、YaRN4，主模型和修正后草稿均1M。max_num_seqs=8、max_num_batched_tokens=16384、内存预算0.80、prefix cache关闭、temperature=0、ignore_eos。随机普通token ID按usage核长度，KV未做质量校准或回答质量评价。

50K／100K输入各2次，300K／500K各1次，每次输出2048。TTFT63.1／144.8／658.9／1470.1秒，decode21.01／20.11／17.23／14.82。等待图按分钟显示、条格取近似整数，精确秒数伴随数值。1M容量样本独立为999936＋64，TTFT4815.8秒，短段decode9.83，完成1次。正文80.26分钟为秒数换算。

**21**：同来源“MTP长度门限诊断”。300K输入、草稿262144上限时，5.80token/s、接受率0、平均长度1；修正上限1M后17.23、99.4%、3.98。正文采用提供方“平均每步接受长度”字段，故障修正身份写在开头。来源没有提供正常关闭MTP的配对实验。

**22**：[TECH-076][sparkraw]和[共享CSV][sharingcsv]。共享池1806907，三份512K总窗口1572864，10%池余量后余53352.3。该驻留为容量计算。

三路100000＋4096测试：共同窗口总52.41、每路17.47，完整decode均值12.45。共同窗口从最晚首token到最早结束，由累计token序列插值；完整decode含其他请求prefill干扰。原50K对应59.08／19.69／16.85，修订正文仅主讲100K。调度图是顺序机制示意，没有赋予示意块测量时长。

**23**：[最终配置][config]第3.3、7节，[Qwen缓存recipe][qwenrecipe]和[DeepSeek recipe][dsrecipe]。正文用“拟采用”标明状态保存路线，前缀复用和闲置状态恢复分步解释。Qwen状态包含全注意力KV、GDN递推和卷积，匹配前缀、位置、版本和布局。Spark统一内存下的CPU副本占用同一物理内存。

LMCache的Qwen文本路径要求align、prefix caching及分组块，align属实验性；准确FP8＋MTP3＋GB10＋SSD组合仍待运行验证。DeepSeek多组缓存需要index、SWA及scratch重建，recipe的MTP尚未验证。恢复算例移入本文件：Spark1M FP8全注意力KV32.768GB，有效SSD6GB/s时纯载荷读5.46秒；DeepSeek TP8 global14.616GB，合计24GB/s时纯CPU至GPU载荷0.609秒。完整恢复另计状态、调度、重放和新增输入处理。

### 24–27：共享资源、服务与适配

**24**：[DeepSeek索引][dsindex]、[最终配置][config]第5.1节和[Hopper实现源码][attention]。权重总510286023000B，Engram202758032400B，其余307527990600B。树中的GPU分配描述索引字节去向，实际加载副本、反量化及临时空间列入完整预算。

global KV采用Hopper1827B/token/TP rank。正文用“每张参与推理的卡”解释本方案一个rank/GPU的放置。20×1M×1827＝36.54GB/卡；TP8合计292.32GB。模型论文其他硬件格式的890B/token未用于此计算。

**25**：[最终配置][config]第5.2–5.3节、[容量CSV][capacitycsv]、[server日志][serverlog]和[Engram共享文档][engram]。单TP8严格池28.250M、两个TP4各16.935M为公开池按图捕获后建议GiB线性缩放，准入再保留10%。采用C32 profile。这是预算敏感性，未在本项目设备重新启动测量。

20份1M在两种布置下均满足该预算。40份历史时，TP8约635584/份，双TP4各20份约762048/份，正文取636K／762K。20生成＋20等待工具是具体任务状态例。

公开池镜像为nightly-cd10ed6f9f6b37a8ace9cf380007e66fe12ec0c3，Engram CPU offload、FP8 MLA/index、DSpark5。TP4×DP2是新增方案，Engram共享要求同节点、CPU offload、DP>1、共享IPC和足够/dev/shm；正文明确两个副本各自管理会话缓存。两独立服务默认两份主存表。

**26**：[AgentX原数据][agentx]和[回放CSV][replaycsv]。正文主讲原版DeepSeek、H200TP8/C32、平均输入156951、95.7%命中、端到端output1052.18、p95TTFT2.63。镜像身份同25，合成DSpark接受长度3.51。活跃会话在生成和工具等待间交替。原稿H100TP8/C20为718.48、p956.98，H200TP4/C32为922.61、p955.12，移到这里供查。

服务目标独立为20路各1M总窗口、每路10或20，系统200或400token/s。8192输出分别13.65／6.83分钟；目标仅计算持续生成。原稿冷启动15分钟门槛移证据：20×991808÷900＝22040.18未缓存输入token/s。当前没有20路真实满1M的速度记录。

**27**：[Tokha消融原文][ablation]、[作者README][tokhareadme]、[A100专项][a100]。准确设备八A800 80GB SXM，C128、78–90coding输入、1024输出、effort100、180秒，TP4×DP2＋EP8，DSpark5。基础已有Marlin、NCCL、CUDA Graph、FP8 KV、EPLB。新增dense BF16和custom EP8，两次均值2842.48／2926.08／2970.50，逐档2.94%／1.52%，合计4.50%。两次均值保持描述统计身份。

shi3z四A100 PCIe项目移出正文，其拓扑、项目贡献与其他测试已保存在原证据和A100专项。本次只展开一个同机增量案例。

### 28–32：硬件、工作量与成本

**28**：[整机采购研究][hardware]、[价格JSON][prices]和[刷新核查][refresh]第4节。人民币预算基线10/12，挂牌10/20复核。包含汇率7.00、税费/价格/交付/支持准备。A100原卖方为翻新、90天保修身份，国内交付及本地支持按预算情景处理。正式采购的交易、交付和保修需按供应商报价落实。

四H200 NVL为单卡价格加整机BOM，161–283万元。该行删除原稿对应另一四卡H200配置的762K容量，两个配置保持分开。H100242240采用严格池＋10%余量。八H20020×1M为容量估算。GPU整机已有CPU/RAM，另列12–26万对应工具节点。

**29**：[TCO研究][tco]第1、3、4节与[逐轮账][ledger]。输入100K至170K合计1.08M，输出16K，最后总长172K。每项增加10%轨迹为重跑修改预算。可复用历史命中本地90%、API95%，API计费另处理缓存边界。个人750／825／907.5，公司25000／31250／39062.5，非整数表示预算期望量。

**30**：[TCO结果][tcoresults]、[分项CSV][bars]、[价格原文][dsprice]。公司本地392.5410万、API68.3431万，个人9.0466／1.6552万，按两位显示。GPU采购占比75.75%，正文约76%。本地设施等20.9263含接入3、电费6.5263、机位5.4、软件6；API6.883含平台6、CPU电0.883。

人工按2500元/技术人日，本地公司实施45人天、年运维60，API实施30、年运维40。两路线均含18万元工具CPU。已有NAS/身份/检索/终端复用，额外RAG GPU、全库解析和企业授权另立项目。

DeepSeek1017低峰未缓存/缓存/输出每百万USD0.15/0.003/0.60，高峰双倍。80%高峰、汇率7、token税费准备6%；三年固定费率是假设。平台条款要求资料范围先获准。本地Qwen/DeepSeek与API的同题质量、轮数、复核尚未统一实测，表内为相同任务轨迹预算。

**31**：[TCO研究][tco]第7、9节、[逐轮账][ledger]。本地273240 fresh input＋17600output已含1.1轨迹，机时273240/8000＋17600/400＝78.155秒。1400h×3600/78.155＝64487项/年。吞吐为容量规划输入，来源公开高命中AgentX没有被移作该任务实测。

高情景50K/75K/112.5K，节点1/2/2，TCO712.78／77.23万。平均容量安排还需要真实混合负载核定。原稿全冷敏感性留此：本地缓存全失时，中等情景第2年扩容，三年712.75万。1M长期日常产能另外评估。

**32**：[TCO研究][tco]第8、11节。已有八A100情景134.42万元为新增改造及后续运行预算，改造10万、年硬件支持3万，实施65人天、年运维80人天，平均2kW独立功耗假设。原资产历史购置成本和其他用途的机会成本需要资产决策单独考虑。新购翻新八A100情景212.13万。A100长窗口容量及任务吞吐保持待测状态。

原稿357.42万元移入证据，完整假设为95312.5项×净省15分钟×150元/小时。它是业务工时价值敏感性，实际净时间要扣准备、主动交互、复核、返工和占用人的等待。现金兑现由外包、加班、招聘等付款变化确定。

### 33–35：使用与收束

**33**：[场景二研究][rag]与[最终配置][config]第4节。解析时保留来源位置，员工身份与有效权限过滤检索，引用访问再次鉴权。Onyx企业本地部署需询价，自建路线负责具体集成。正文保持方案描述。

原独立RAG硬件容量移此：4×84GB卡，其中3个Qwen27回答副本，1卡检索辅助，FP8权重、完整KV。单回答卡池38.6GB，每会话(C×65536＋153944064)×1.15。131K三卡9份，262K三卡3份，20路8192＋600短问答可驻留。[原容量数据][ragcsv]。此建设在推理TCO之外单列。

**34**：[Harness调研][harness]与[最终配置][config]。个人OpenCode、本机工具，共享Hermes和独立CPU环境是原研究入口备选，正文简化品牌名而保留Skills和MCP职责。图表示提出调用、工具执行、返回结果、形成工作文件的循环。详细任务起步顺序保留为研究后续安排。

**35**：总结模型与运行路线，后续以公司任务记录质量、等待和人工净时间。当前研究成果包括公开能力整理、框架研究、资源及成本计算，公司GPU实测与业务验收尚未完成。

## 自查记录

完成按页序的正文通读和单独的事实条件检查。页号连续01–35，图表数据与单位完整；上屏末句逐页检查，删除重复总结、自评和针对假想误读的反驳。来源文件与研究数据保持原样。

本轮定点复核了新增教学算例、KV载荷、等待单位换算、MTP前后字段、共享池余量、并行容量、消融增幅、TCO分项与年度扩容。页内资料身份、费用范围及版本对应关系在改写后保持明确。完整读图与讲解时间合计2400秒。

## 来源入口

[bench]: ../../../knowledge-base/models/public-benchmark-review-2026-10-20.md
[models]: ../../../knowledge-base/models/model-survey-2026-09-16.md
[local]: ../../../knowledge-base/models/local-llm-poc-evidence-2026-09-09.md
[architecture]: ../../../knowledge-base/infrastructure/reference-architecture.md
[penghua]: ../../../knowledge-base/sources/FUND-308/original.md
[maxwealth]: ../../../knowledge-base/sources/FUND-352/original.md
[refresh]: ../../../knowledge-base/infrastructure/final-source-refresh-2026-10-20.md
[config]: ../../../knowledge-base/infrastructure/final-configurations-2026-10-20.md
[serving]: ../../../knowledge-base/infrastructure/serving-framework-survey-2026-09-17.md
[qwencard]: ../../../knowledge-base/sources/TECH-091/modelcards/qwen27/original.md
[dscard]: ../../../knowledge-base/sources/TECH-091/modelcards/deepseek/original.md
[artifacts]: ../../../knowledge-base/infrastructure/data/final-source-refresh-2026-10-20/model-artifact-comparison.json
[extractcsv]: ../../../knowledge-base/sources/TECH-091/benchmarks/extractbench/leaderboard.csv
[extractreadme]: ../../../knowledge-base/sources/TECH-091/benchmarks/extractbench/readme.md
[conditions]: ../../../knowledge-base/models/data/public-benchmarks-2026-10-20/evaluation-conditions.json
[aaoriginal]: ../../../knowledge-base/sources/TECH-091/benchmarks/aa-deepseek-qwen/original.md
[valshtml]: ../../../knowledge-base/sources/TECH-091/benchmarks/vals-fabv2/source.html
[valsmethod]: ../../../knowledge-base/sources/TECH-091/benchmarks/vals-fabv2/original.md
[financecsv]: ../../../knowledge-base/models/data/public-benchmarks-2026-10-20/finance-agent-v2.csv
[sparkraw]: ../../../knowledge-base/sources/TECH-076/original.md
[sparkstudy]: ../../../knowledge-base/infrastructure/dgx-spark-qwen27-external-benchmark-2026-10-12.md
[vllmrelease]: ../../../knowledge-base/sources/TECH-089/vllm-0.32-release-original.txt
[sharingcsv]: ../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/spark-sharing.csv
[restorecsv]: ../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/restoration-budgets.csv
[qwenrecipe]: ../../../knowledge-base/sources/TECH-089/lmcache-qwen-series.rst
[dsrecipe]: ../../../knowledge-base/sources/TECH-089/lmcache-deepseek-v41.rst
[dsindex]: ../../../knowledge-base/sources/TECH-079/model.safetensors.index.json
[attention]: ../../../knowledge-base/sources/TECH-089/vllm-0.32-attention.py
[capacitycsv]: ../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/company-capacity.csv
[serverlog]: ../../../knowledge-base/sources/TECH-084/server-h200-tp8-c32.txt
[engram]: ../../../knowledge-base/sources/TECH-089/vllm-0.32-engram.md
[agentx]: ../../../knowledge-base/sources/TECH-084/benchmarks.json
[replaycsv]: ../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/company-replay.csv
[a100]: ../../../knowledge-base/infrastructure/deepseek-a100-project-review-2026-10-12.md
[ablation]: ../../../knowledge-base/sources/TECH-088/tokha-ablation.md
[tokhareadme]: ../../../knowledge-base/sources/TECH-088/tokha-readme.md
[hardware]: ../../../knowledge-base/infrastructure/server-gpu-procurement-2026-10-12.md
[prices]: ../../../knowledge-base/infrastructure/data/hardware-prices-2026-10-12.json
[tco]: ../../../knowledge-base/infrastructure/tco-analysis-2026-10-20.md
[tcoresults]: ../../../knowledge-base/infrastructure/data/tco-2026-10-20/results.json
[ledger]: ../../../knowledge-base/infrastructure/data/tco-2026-10-20/round-ledger.csv
[bars]: ../../../knowledge-base/infrastructure/data/tco-2026-10-20/presentation-bars.csv
[dsprice]: ../../../knowledge-base/sources/TECH-090/deepseek-pricing.md
[sensitivity]: ../../../knowledge-base/infrastructure/data/tco-2026-10-20/sensitivity.csv
[rag]: ../../../knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md
[ragcsv]: ../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/rag-capacity.csv
[harness]: ../../../knowledge-base/infrastructure/harness-survey-2026-09-17.md
