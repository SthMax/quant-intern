# D 版证据、研究记录与讲述安排

配套正文：[extended-draft-d.md](extended-draft-d.md)。骨架保留：[d-outline.md](d-outline.md)。本文件不属于上屏内容。

编写日期：2026-10-22，Asia/Shanghai。研究事实主要取自知识库截至 2026-10-20 的归档；硬件价格采用 2026-10-12 分析预算。执行者为本轮 D 版作者，采用原始文本、作者 CSV、原始 HTML、公开 API JSON 与既有计算结果核对；没有运行模型、GPU 实验或付费 API，也没有人工业务验收。

叙事和表达依据仅为 [initial-draft.md](initial-draft.md)、[expansion-guide.md](expansion-guide.md) 与本轮先形成的骨架。第二阶段检索 `knowledge-base/` 的研究与原始资料，没有打开其他版本稿件、旧 session 或审查反馈。研究文件中附带的旧页码映射和既有讲述建议未作为本稿的组织依据。

## 一、骨架调整与时间

保留原骨架的六章顺序、目录与全部章节页。实际正文为 **36 页，总计 44 页**：封面 1 页、目录 1 页、章节页 6 页、正文 36 页。结尾计入正文。

相比骨架增加两页，均在 infra 章节：

- 新第 29 页单独解释大模型的放置、多卡分工、Engram 与会话状态。这是理解后续框架与容量比较所必需的一步，避免把新术语藏在数据脚注里。
- 新第 32 页单独解释共享服务的公开回放。它与 Spark 单机测量具有不同的任务、缓存与统计条件，需要独立页面呈现，不能压进一个“速度比较”表。

原骨架第 29–30 页顺延为新 30–31；原第 31–42 页顺延为新 33–44。原第 30 页的“框架／优化对照”实际采用 MTP 配置诊断与机制解释：资料没有本项目同条件的框架横评，因此没有编造框架速度名次。

财报页保留任务示意，没有填入任意公司的数字或虚构运行结果。案例页采用公开研究原型、产品流程和公司披露，逐项说明状态。成本部分围绕本地投入与工作规模，选用 DeepSeek API 作为较简洁的经济参照；未把所有知识库的方案都搬入正文。

### 逐页时间分配

| 页 | 页类 | 时间 | 累计 | 讲述重心／停留安排 |
| ---: | --- | ---: | ---: | --- |
| 1 | 封面 | 0:15 | 0:15 | 直接说明研究任务 |
| 2 | 目录 | 0:30 | 0:45 | 预告六章路径 |
| 3 | 章节页 | 0:15 | 1:00 | 从日常工作进入 |
| 4 | 正文 | 0:30 | 1:30 | 建立能力的共同认识 |
| 5 | 正文 | 1:15 | 2:45 | 三个不同岗位例子，各讲输入、工作与产物 |
| 6 | 正文 | 0:30 | 3:15 | 从资料进入使用条件 |
| 7 | 正文 | 0:45 | 4:00 | 明确本地部署与管理的关系 |
| 8 | 章节页 | 0:15 | 4:15 | 引入财报任务 |
| 9 | 正文 | 0:45 | 5:00 | 先定义有用的交付物 |
| 10 | 正文 | 0:45 | 5:45 | 参数与已有能力 |
| 11 | 正文 | 0:45 | 6:30 | 上下文、推理和 token |
| 12 | 正文 | 0:45 | 7:15 | 容量与能力的关系 |
| 13 | 正文 | 1:00 | 8:15 | 两段等待与完整任务 |
| 14 | 正文 | 1:00 | 9:15 | 汇合选型维度 |
| 15 | 章节页 | 0:15 | 9:30 | 从要求转入比较 |
| 16 | 正文 | 1:00 | 10:30 | 解释规划条件与窗口口径 |
| 17 | 正文 | 1:15 | 11:45 | 三类证据回答不同问题 |
| 18 | 正文 | 1:15 | 13:00 | 读长文问答与提取差异 |
| 19 | 正文 | 1:15 | 14:15 | 金融研究比较及其含义 |
| 20 | 正文 | 1:15 | 15:30 | 将速度转为用户体验 |
| 21 | 正文 | 1:00 | 16:30 | 说明模型选择与备选 |
| 22 | 章节页 | 0:15 | 16:45 | 进入请求运行过程 |
| 23 | 正文 | 1:00 | 17:45 | 读完整流程 |
| 24 | 正文 | 1:00 | 18:45 | 区分内存占用对象 |
| 25 | 正文 | 1:00 | 19:45 | 解释输入处理 |
| 26 | 正文 | 1:00 | 20:45 | 解释逐步生成与完成时间 |
| 27 | 正文 | 1:15 | 22:00 | 读长度变化数据 |
| 28 | 正文 | 1:15 | 23:15 | 读多人计时窗口，解释调度 |
| 29 | 正文 | 1:15 | 24:30 | 多卡放置与参数／状态区别 |
| 30 | 正文 | 1:00 | 25:30 | 框架与硬件匹配 |
| 31 | 正文 | 1:00 | 26:30 | 缓存与 MTP 各改善什么 |
| 32 | 正文 | 1:15 | 27:45 | 公开共享回放及适用范围 |
| 33 | 正文 | 1:15 | 29:00 | 汇合服务方案与验收目标 |
| 34 | 章节页 | 0:15 | 29:15 | 放开硬件投入条件 |
| 35 | 正文 | 1:00 | 30:15 | 读容量配置比较 |
| 36 | 正文 | 1:15 | 31:30 | 统一任务、费用与缓存假设 |
| 37 | 正文 | 1:30 | 33:00 | 读三年总投入和主要差额 |
| 38 | 正文 | 1:30 | 34:30 | 增量投入与扩容台阶 |
| 39 | 正文 | 1:00 | 35:30 | 给出当前规模下的判断 |
| 40 | 章节页 | 0:15 | 35:45 | 回到实际使用 |
| 41 | 正文 | 0:45 | 36:30 | 入口与任务执行位置 |
| 42 | 正文 | 1:00 | 37:30 | 资料与工具接入 |
| 43 | 正文 | 1:15 | 38:45 | 验证产物、质量与体验 |
| 44 | 正文·结尾 | 1:15 | 40:00 | 回到公司需求与已有依据 |

章节时间为 3:15、5:15、7:15、12:30、6:30、4:30，加开场与目录 0:45，总计 **40:00**；正文共 **37:45**。模型、infra 与成本合计 **26:15**。这是按解释步骤进行的桌面节奏预算，尚未完成真人计时试讲；正文只放上屏内容，讲述时可展开图中的关系，不逐字朗读所有限定。

## 二、来源目录与采用范围

以下编号仅用于本文件复核，不要求上屏。原始发布内容与本项目的研究计算分别列示；来源当前可访问并不意味着已经独立复现作者的结果。

### E01｜金融应用案例

- **MENTOR**：Chen 等，2025，易方达与高校共同署名论文。[原始论文文本，PDF pp.1–2](../../../knowledge-base/sources/FUND-113/original.md)；[出版方 DOI](https://doi.org/10.1631/FITEE.2500608)。明确输入为中文 KOL 文章与英文金融新闻，任务依次为事件发现／排序、事件预测与行业排序。第 5 页仅介绍研究路径与产物，不采用回测收益或预测率，不认定已在公司实盘运行。
- **盈米内容审查**：[公司固定客户端 README](https://github.com/yingmi-dev/content-compliance-skill/blob/040df66202f6075cdeadb450e502c7a19c83dabf/README.md)；[知识库技术研究](../../../knowledge-base/reference/yingmi-compliance-workflow-2026-09-09.md)。2026-10-22 重新打开公司发布入口 `https://www.yingmi-inc.com/archives/799`，实际重定向至 [中国基金报发布页](https://www.chnfund.com/article/AR8e4e17e8-252c-d5d6-2eb7-3a20162a0343)，页标 2026-03-19。现网页支持初稿预审、修改与终审衔接；客户端支持文本或文档输入和结果返回。第 5 页不使用“风险为 0”、规则数、案例数或效率百分比。公司网址当前重定向到媒体，不能仅凭域名将现页面称为公司自写原文。
- **易方达云平台**：[FUND-101 原文 PDF p.4／印刷 p.3](../../../knowledge-base/sources/FUND-101/original.md)；[协会托管原始 PDF](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337815959196.pdf)。直接披露在开发与测试环节引入大模型。正文把它放在后台技术支持位置，未把综合云平台的效率数字当作 LLM 单独贡献。PDF未明确出版日期，不从路径推定。

### E02｜模型概念、窗口与原生制品

- [Qwen27 官方模型卡归档](../../../knowledge-base/sources/TECH-092/models/qwen27/README.md)，Model Overview 与 Processing Ultra-Long Texts；[官方卡片](https://huggingface.co/Qwen/Qwen3.8-27B)。27B 参数、262,144 原生窗口及 1,000,000 扩展配置有直接依据；1M 上限不代表所有任务达标。
- [Qwen27 FP8 官方仓库](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)，2026-10-22 打开核对，仍列 FP8 制品及 vLLM／SGLang 使用路径。运行记录的具体 revision 尚缺时不以当前卡片修订反填。
- [DeepSeek 原版官方卡片归档](../../../knowledge-base/sources/TECH-092/models/deepseek/README.md)，Introduction／Architecture／Additional architectural components；[官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)。支持 1M、CED、Engram、共享压缩 KV 和推测生成的结构解释。
- [TECH-079 原始制品记录](../../../knowledge-base/sources/TECH-079/original.md)与[最终制品核验](../../../knowledge-base/infrastructure/final-source-refresh-2026-10-20.md)，支持 510,286,023,000 B、Engram 表 202,758,032,400 B、余量 307,527,990,600 B。正文 GB 一律十进制；三者是文件／参数字节账，不能当实际加载显存。
- [1017 官方公告](https://api-docs.deepseek.com/news/news261017/)与[1017 固定官方卡片](../../../knowledge-base/sources/TECH-092/models/deepseek1017/README.md)。采用开放权重升级候选的事实；未将原版速度、缓存池或任务得分改标为 1017 实测。

第 10–14 页的基础概念为本轮解释性写作，以模型卡和 E05 的请求机制作技术支撑，不设定虚构训练过程或公司数据进入训练的事实。

### E03｜公开任务能力

研究入口：[2026-10-20 公开评测研究](../../../knowledge-base/models/public-benchmark-review-2026-10-20.md)。本稿独立选择与页面任务对应的分项，不采用该研究附带的旧演讲页码或讲述段落。

**Finance Agent v2**：[作者页面](https://www.vals.ai/benchmarks/fabv2)；[归档说明](../../../knowledge-base/sources/TECH-091/benchmarks/vals-fabv2/original.md)；[原始 HTML](../../../knowledge-base/sources/TECH-091/benchmarks/vals-fabv2/source.html)；[整理 CSV](../../../knowledge-base/models/data/public-benchmarks-2026-10-20/finance-agent-v2.csv)。作者页更新 2026-10-18。第 19 页五个分数在原始 HTML 的模型记录或表行逐项找到：Qwen 48.553→48.55，DeepSeek 原版 53.481→53.48，1017 56.96，GLM Flash 57.85，MiMo Flash 56.28。主指标为关键条件门槛下的 severity-weighted partial credit；不是 all-pass。同默认六工具环境，逐模型 thinking、精度、权重 SHA 和置信区间未披露，不能给接近分数显著性结论。

**ExtractBench**：[固定作者 README](https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/README.md)；[作者原始 CSV 归档](../../../knowledge-base/sources/TECH-091/benchmarks/extractbench/leaderboard.csv)；[pipeline 条件](../../../knowledge-base/sources/TECH-091/benchmarks/extractbench/pipelines.md)。固定修订 `56b8fdd91b2cf3648caf75c717c68441ecf4d43f`。第 18、19 页使用 Qwen3.8 27B：Overall 89.75、Short 94.68、Long 38.45；DeepSeek Overall 87.11，均已回读作者 CSV 原行。短文≤10页，长文>50页；370份文档中长文20份，逐文档等权平均。Qwen 为自托管 vLLM FP8、150dpi逐页图像、32,768最大输出，thinking 取端点默认；DeepSeek 为 API、150dpi图像、65,536最大输出、thinking关闭。可评价完整 pipeline，不能当作同推理预算纯模型比较；value F1与引用F1不同，也不是中文金融NER或下游投资收益。

**Artificial Analysis 分项**：[作者对照页](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-vs-qwen3-8-27b)；[归档原文](../../../knowledge-base/sources/TECH-091/benchmarks/aa-deepseek-qwen/original.md)。第 18 页 Qwen xhigh 的 AA-LCR v1.1＝82%；第 21 页 DeepSeek max／Qwen xhigh 的 AutomationBench-AA＝69／48、Terminal-Bench4.0＝27／6。AA-LCR v1.1 为约100K多文档问答，不证明1M能力；另外两个分项各自使用对应工具环境，不能跨榜相加。正文保留作者推理标签，不用综合榜单充当金融排名。

### E04｜Spark 外部测量

唯一设备测量原始入口为[TECH-076 用户提供总结](../../../knowledge-base/sources/TECH-076/original.md)，辅助理解见[专项分析](../../../knowledge-base/infrastructure/dgx-spark-qwen27-external-benchmark-2026-10-12.md)。收到日期2026-10-12，主实验日期未提供；未取得 environment.json、启动脚本、逐请求JSON或完整日志。

- 硬件：单DGX Spark GB10，TP1，128GB统一内存。软件设置：Qwen3.8-27B-FP8，FP8 KV默认尺度未校准，MTP3，FlashInfer，YaRN4，关闭前缀缓存，随机普通token精确长度输入。不得称为本轮独立实测、自然语言业务负载或质量验证。
- 第20／27页输入50,000／100,000／300,000／500,000，输出均2,048；TTFT秒63.1／144.8／658.9／1470.1；decode 21.01／20.11／17.23／14.82 token/s。前两档各2次，后两档各1次。
- 1M样本为999,936＋64＝1,000,000，TTFT4815.8秒＝80.2633分钟。仅作为容量完成；未采用其9.83 token/s短输出值去预测长期任务产能。
- 第28页三路各4096输出，共同窗口总吞吐59.08／52.41、每路19.69／17.47；完整阶段均值16.85／12.45。共同窗口采用SSE累计token序列插值，其平均值不能与完整阶段直接互换。
- 第31页300K故障／修正样本5.80／17.23，接受率0／99.4%。原草稿门限262,144，后同步1,000,000。故障路径仍有验证开销，不作正常MTP关闭对照，也不称固定加速倍数。

正文分钟数按TTFT÷60四舍五入。单页指标名、单位、输入输出、样本数与证据限制已保留。

### E05｜请求机制与性能解释

- 李博杰《深入理解 AI Infra：量化分析与系统设计》，固定修订 `3bdcb4fcab73010eeaccf31cc10a8242a895d82e`。[原始第3章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/03-推理与训练负载.md)，§3.1.1–3.1.2、§3.2；[原始第8章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/08-推理优化.md)，输入调度、缓存、推测生成相关章节；[固定上游仓库](https://github.com/bojieli/ai-infra-book/tree/3bdcb4fcab73010eeaccf31cc10a8242a895d82e)；[本项目阅读研究](../../../knowledge-base/infrastructure/ai-infra-book-reading-2026-10-12.md)。
- 第23–28页请求生命周期、prefill／decode区别、低并发读取压力、合批和chunked prefill的解释，依据上述机制。未将书中其他模型、RTX实验或理想资源算例移植为本项目性能。
- 第26页8,192÷20＝409.6秒＝6.8267分钟，是假设保持20 token/s的算术示例，明确没有包含TTFT、工具和人工；只取约410秒／6.8分钟。
- 第24、31页Qwen需要KV之外的递推状态，见E02模型结构与[LMCache当前归档](../../../knowledge-base/sources/TECH-092/engines/lmcache-qwen.md)。未宣称FP8 KV＋MTP3＋GB10＋SSD全部组合已验证。

### E06｜框架与多卡运行

- [vLLM官方README归档](../../../knowledge-base/sources/TECH-020/original.md)、[SGLang官方README归档](../../../knowledge-base/sources/TECH-021/original.md)，支持分页、连续批处理、分块输入、前缀缓存和多卡能力。研究路线说明见[Serving调研](../../../knowledge-base/infrastructure/serving-framework-survey-2026-09-17.md)。第30页把vLLM设为当前可追溯数据主线，SGLang为对照，是本轮在现有证据上的研究判断，未作速度排名。
- [vLLM v0.32.0 release](https://github.com/vllm-project/vllm/releases/tag/v0.32.0)，2026-10-22实时打开，页面确认10月18日发布；采用“固定版本候选”而非将所有历史数字归给新版。版本更新与缓存事实见[TECH-089](../../../knowledge-base/sources/TECH-089/original.md)。
- [v0.31 Engram官方文档](https://github.com/vllm-project/vllm/blob/v0.31.0/docs/features/engram.md)、[归档v0.32 Engram文档](../../../knowledge-base/sources/TECH-089/vllm-0.32-engram.md)。TP4×DP2同机共享要求CPU offload、DP>1、共享IPC与足够共享内存；不能从两条独立serve命令自动推定共享。第33页保留这一区别，未据此再减GPU整机采购额。
- [A100专项](../../../knowledge-base/infrastructure/deepseek-a100-project-review-2026-10-12.md)、[TECH-088原始来源入口](../../../knowledge-base/sources/TECH-088/original.md)。采用modified vLLM作为公司A100验证路线，区分模型原生能力与SM80适配；未采用不同项目的跨机器加速比，也未将四卡短输入结果倍增为八卡1M性能。

### E07｜DeepSeek容量与共享回放

研究主表：[最终配置研究](../../../knowledge-base/infrastructure/final-configurations-2026-10-20.md)。原始启动日志：[TECH-084](../../../knowledge-base/sources/TECH-084/original.md)；[原始公开API JSON](../../../knowledge-base/sources/TECH-084/benchmarks.json)；[来源与URL元数据](../../../knowledge-base/sources/TECH-084/metadata.json)。

**第29页：**原生制品字节数采用E02。Hopper格式按[TECH-080实现](../../../knowledge-base/sources/TECH-080/original.md)和[后续固定版本核验](../../../knowledge-base/sources/TECH-089/original.md)，为1,827 B/token/TP rank；20×1,000,000×1,827＝36.54GB/rank。不能用论文890 B/token替代，也不能再除TP。主表只写global KV，其他状态仍需另计。

**第32页：**[整理回放CSV](../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/company-replay.csv)保留原始API行ID：

| 行ID | 部署 | 平均输入 | 输出token/s | p95 TTFT秒 | GPU缓存命中 |
| ---: | --- | ---: | ---: | ---: | ---: |
| 442757 | H200 TP4，16活动会话 | 138189.09055 | 614.75775 | 3.02859 | 0.9508978493 |
| 442751 | H200 TP4，32活动会话 | 149854.78422 | 922.60949 | 5.11831 | 0.9523468149 |
| 442758 | H200 TP8，32活动会话 | 156951.17321 | 1052.17744 | 2.63289 | 0.9571115953 |

公开2026-09月AgentX回放，镜像 `vllm/vllm-openai:nightly-cd10ed6f9f6b37a8ace9cf380007e66fe12ec0c3`，DSpark5、synthetic acceptance length 3.51。并发数指活动会话，并非全部时刻共同decode。各行的输入分布亦不完全一致；正文只描述记录中的组合，不宣称纯粹增加卡数带来某个固定倍数。

**第35页：**[32行容量CSV](../../../knowledge-base/infrastructure/data/final-configurations-2026-10-20/company-capacity.csv)。公式为：公开token池×图运行后严格KV建议GiB／原分配GiB，再保留10% token余量，按驻留会话分配，受1M请求上限约束。20份历史的242,240／762,048／1M／1M来自对应TP8、TP4与双TP4记录；八H200 TP8的40份历史＝635,584，正文约636K。该线性缩放是敏感性分析，没有新启动实测。两独立TP4均用C32 profile，不混入C16较大的池。

**第33页：**20×20＝400输出token/s，是服务目标反推。没有用高缓存合成DSpark回放去证明20×1M已经达到400。

### E08｜成本、投入与配置比较

主要研究：[三年TCO](../../../knowledge-base/infrastructure/tco-analysis-2026-10-20.md)；[输入参数](../../../knowledge-base/infrastructure/data/tco-2026-10-20/inputs.json)；[三年结果CSV](../../../knowledge-base/infrastructure/data/tco-2026-10-20/summary.csv)；[结果JSON](../../../knowledge-base/infrastructure/data/tco-2026-10-20/results.json)。本稿采用研究的计算数据与条件，不采用其旧讲稿内容。

**硬件预算来源**：[10月12日价格台账](../../../knowledge-base/infrastructure/data/hardware-prices-2026-10-12.json)。H100、H200分别基于[Exxact H100配置](https://configurator.exxactcorp.com/configure/TS4-193475697)、[Exxact H200配置](https://configurator.exxactcorp.com/configure/TS4-118380266)，再加储存／网络、税费和支持准备；境外公开价不能当中国含税交付报价。原始页面归档在[TECH-087](../../../knowledge-base/sources/TECH-087/original.md)，10月20日时效核验在[TECH-092硬件](../../../knowledge-base/sources/TECH-092/hardware/h200-exxact.md)。

| 第38页数字 | 原始预算（人民币元） | 采用方式 |
| --- | ---: | --- |
| 八H100 | 2,855,295.64–2,978,345.64 | 正文采用原研究向外取整285–298万元 |
| 八H200 | 2,912,121.64–3,035,171.64 | 正文采用291–304万元 |
| 同口径增量 | 两端差均为56,826.00 | 约5.68万元，来自原预算逐项相减 |

H200增加价值与第35页的容量计算联系，是有条件的研究判断；未声称完成现实采购，也不保证增量价格长期不变。

**第36页任务与成本条件：**首轮100K；八轮输入100K、110K……170K之和1.08M；外部新输入156K已包括在上述总和；八轮输出16K，最后172K。额外0.10份完整轨迹是重试准备，并非90%通过率。个人750／825／907.5项，三年2482.5；公司25000／31250／39062.5项，三年95312.5。小数是规划期望量，正文取整数约数。

DeepSeek API 费率为10月20日快照：低峰输入未命中0.15、命中0.003、输出0.60 USD／百万tokens；高峰翻倍，假设80%高峰。2026-10-22重开[官方价格](https://api-docs.deepseek.com/quick_start/pricing/)核对一致。汇率7.00及API token费6%税费准备均为分析参数；硬件已含原预算准备，不再加6%。本地可复用前缀90%命中，API95%；整体提交输入命中率另取决于首轮新输入，不能把95%直接乘所有输入。官方API对照模型是1017，而本地既有测量为原版；质量未统一实测，正文标作预算对照。

**第37页成本：**个人本地90465.64365元、API16552.36794元；公司本地3925410元左右、API683431元左右，分别按万元两位小数显示9.05／1.66、392.54／68.34。GPU整机2973646.64元÷公司TCO约75.8%；公司年运维60人天×2500×3＝450000元。公司双方均计18万元工具CPU，不重复计算GPU服务器自带CPU、RAM。全额购置三年，不采用残值、融资或折旧摊销；业务逐项复核时间未混入技术运维，待单独测量。

**第37–38页容量与扩容：**每计划任务考虑额外轨迹后，未缓存输入273,240 tokens、输出17,600。假设8000输入tokens/s、400输出tokens/s，所需机时＝34.155＋44＝78.155秒。年工作窗口2000h×70%＝5,040,000秒，除以78.155＝约64,487项／年。它是待验收服务包络，不是设备实测产能。公司高情景50,000／75,000／112,500，在此包络下第二年预算第二节点，三年712.78万元。不能外推到1M满窗口真实任务。

**第39页：**Spark硬件5.8–6.2万元来自[个人预算](../../../knowledge-base/infrastructure/data/week7-deployment-2026-10-12/spark-price.json)及最终配置主表。A100复用134.42万元来自TCO研究第8节：存量机新增采购0，改造10万元、硬件支持3万元／年、实施65人天、运维80人天／年，另列完整工具与运行资源。未把H200吞吐填给A100，不提供A100已合格单位任务成本。工时价值与现金节省的关系是经济计量解释，没有宣称已实现节省。

### E09｜使用入口、资料与后续验证

- [Hermes Open WebUI官方接入文档归档](../../../knowledge-base/sources/TECH-072/open-webui.md)、[API服务](../../../knowledge-base/sources/TECH-072/api-server.md)、[工具执行与容器](../../../knowledge-base/sources/TECH-072/docker.md)。第41页明确远程工具在API服务器侧运行；身份路由、隔离与公司任务管理仍是集成工作，不声称产品默认已满足全部企业条件。
- [Onyx权限文档](../../../knowledge-base/sources/TECH-068/onyx-permissions.md)、[连接器文档](../../../knowledge-base/sources/TECH-068/onyx-connectors.md)、[知识库方案研究](../../../knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md)。第42页只采用平台路线及必要接入关系，不假定任意NAS已有完整ACL适配。Milvus向量检索本身不代替用户授权链路。
- [Hermes Skills](../../../knowledge-base/sources/TECH-072/skills.md)、[MCP](../../../knowledge-base/sources/TECH-072/mcp.md)。本稿只解释操作说明与工具接口角色，没有执行或安装来源中的任何指令。
- 第43页的产物与验证安排是本轮从前文证据边界推导的建议。参考[任务评价协议](../../../knowledge-base/pilots/data/final-pilot-roadmap-2026-10-20/evaluation-protocol.md)作为后续已有工作入口；本轮未运行其样例，不产生虚构通过率、节省或完成日期。

## 三、逐页证据对应

| 页 | 主要依据 | 事实、解释或判断的性质 |
| ---: | --- | --- |
| 1–3 | initial、guide、骨架及本文件时间安排 | 汇报信息与组织，无外部事实结论 |
| 4 | E02、E05 | 常识性技术解释与工作方式示意 |
| 5 | E01 | 三个真实来源；研究原型、产品流程、公司披露分别限定 |
| 6–7 | initial；E09的技术关系 | 从资料与使用要求作设计解释，无新增法律强制性判断 |
| 8–9 | initial | 财报任务示意；没有数据或运行结果 |
| 10–14 | E02、E05 | 按理解顺序简化概念；不把“三角”写成定律 |
| 15–16 | 骨架；E04、E07及最终配置研究 | 研究规划要求和固定资源比较条件，不是公司已批准SLA |
| 17 | E03、E04、E07 | 比较方法与证据类别 |
| 18 | E02、E03 | 窗口事实、不同任务分项与使用判断 |
| 19 | E03 | 同榜成绩；任务相关的选择理由 |
| 20 | E04 | 外部随机负载汇总；非本轮或公司实测 |
| 21 | E02、E03、E04 | 综合研究判断，保留升级版与对照模型 |
| 22–23 | E05、E06 | 请求流程及服务角色 |
| 24 | E02、E05 | 内存对象、精度与状态解释 |
| 25–26 | E04、E05 | 输入／生成机制；条件算例单列 |
| 27–28 | E04、E05 | 外测表与调度解释 |
| 29 | E02、E06、E07 | 制品字节与缓存格式；机制解释 |
| 30 | E06 | 框架能力与路线判断，没有速度排名 |
| 31 | E04、E05、E06 | 优化机制及配置诊断，不伪造开关消融 |
| 32 | E07 | 原始公开回放；合成推测与高缓存条件保留 |
| 33 | E04、E06、E07 | 运行判断和服务目标，未承诺达标 |
| 34–35 | E07 | 章节过渡与资源敏感性计算 |
| 36–39 | E08 | 固定假设下预算与增量分析，未发生采购或兑现收益 |
| 40–42 | E09 | 接入方案，未认定公司已上线 |
| 43 | E03、E04、E07、E08、E09 | 本轮提出的验证安排 |
| 44 | 前文依据的收束 | 不引入新的分数、模型或预算结论 |

## 四、核对记录与仍有的实际限制

已完成以下文本层核对：

1. 按第1–44页顺序全文自读：金融工作→本地环境→任务与概念→比较与选择→请求机制→性能和框架→硬件与成本→日常使用。目录与六张章节页一致；没有依赖旧稿或跨页跳读才能理解的结论。
2. 参数、上下文、token先于窗口和速度；KV、prefill、decode先于容量与优化；TP和副本先于H100／H200容量对照。新增两页用于补足理解步骤。
3. 数值回查原始作者CSV、Finance Agent HTML、Spark提供方总结、AgentX API记录与成本CSV。所有预算、目标和条件计算在正文保留身份；没有把一次1M容量样本改成1M服务性能。
4. 表格均有比较对象、指标与单位；文本图均有输入、过程与结果。第18页的两种能力指标没有合成总分，第28页不同计时窗口没有混用，第32页没有用活动会话数平均出每人速度。
5. 第35页采用严格post-graph敏感性与10%余量；成本仅采用相应日常轨迹的服务包络。没有使用TCO研究中旧的较宽松启动池数字替代本稿严格容量。
6. 全场页类计数与时间加总为44页、36正文、40:00；这是桌面预算，正式演讲仍需真人试讲。证据记录不计入上屏文字与演讲时间。

尚未取得的资料包括：Spark原始运行环境与逐请求日志、公司真实任务质量与时间基线、目标GPU上的满窗口与混合并发测量、供应商交付报价。它们限制的是实际验收与采购结论，不阻碍本轮完成基于现有资料的演讲稿。

**本轮交付固定：正文与证据文件均已完成。** 原初稿、指南和骨架未修改；未提交、推送或运行外部业务操作。
