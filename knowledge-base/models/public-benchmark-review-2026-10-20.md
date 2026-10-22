# 公开评测与模型选型：最终汇报依据

**资料截止：2026年10月20日。** 本轮采用网上已有评测，不新增模型运行。重点为 Qwen3.8-27B 与 DeepSeek-V4.1-Flash；Gemma、GLM、MiMo、Kimi用于任务能力和资源取舍。公开评测原始来源保存在[TECH-091](../sources/TECH-091/evidence-note.md)，可复算数据在[数据目录](data/public-benchmarks-2026-10-20/README.md)；1017最新制品状态引用[W4／TECH-092核对](../infrastructure/final-source-refresh-2026-10-20.md)。

## 1. 选型结论

**保留Qwen27作为个人工作与知识问答的起点，保留DeepSeek作为共享长任务主线；共享模型的首要对照是GLM-5.3-Flash，其次是MiMo-V2.6-Flash。** 原因来自任务分项：Qwen27的文档字段提取较强；DeepSeek在长材料推理、工具执行与共享资源设计之间形成合适组合；GLM Flash在同榜金融研究任务中更好，值得同题复核。模型规模不决定每类任务的名次。

**DeepSeek-V4.1-Flash-1017已开放权重，采用MIT许可，可作为同资源架构的升级候选。** W4已固定其修订`1bae0e1088993b9b82de08f59de5be5a34e42170`，核对当前原版与1017的配置、完整权重索引及许可逐字节相同，索引体量均为510,286,023,000 B。静态资源架构可沿用作预算；权重值、质量与性能仍按版本分别判断。当前主方案继续保留原版制品和既有测量身份。[官方10月17日公告](https://api-docs.deepseek.com/news/news261017/)、[W4制品核对](../infrastructure/final-source-refresh-2026-10-20.md#2-准确制品与许可)

**先落地公告提取和研究代码辅助，再做财报比较，随后接入NAS权限问答。** 前两项有明确字段或测试可验收；财报比较需增加口径、期间与引用检查；公司知识库还依赖身份、撤权和索引治理。材料预审列第五顺位。完整工作量、测量方法和四项落地方案见[试点路线图](../pilots/final-pilot-roadmap-2026-10-20.md)。

**长窗口需要分两种能力看。** AA-LCR v1.1在约100K token多文档中问一个问题；ExtractBench长文档要求完整输出字段和列表。Qwen27在前者为82%，但后者长文档value F1为38.45%。采购时的512K／1M容量与速度研究继续有意义，业务设计还应分段提取、保存中间结果并核对完整性。

**公开分数已经足以支持本轮选型与试点排序。** 它们评价对应任务和模型系统，未测量本部门的真实节省、NAS权限正确率或内部验收成功率。最终PPT的P31据此改为“公开能力证据＋后续统一任务评价”，本轮交付不等待GPU PoC。

## 2. 四组可并列证据

下表各组拥有自己的任务、评分和运行条件。组内可以比较，组间不相加、不做雷达总分。API模型标识与本地权重修订分开：本轮已固定十项模型卡的当前SHA，公开运行未披露的权重SHA仍记为未披露。

| 证据组 | 谁评、评什么 | 分数含义 | 主要用途 |
|---|---|---|---|
| Finance Agent v2 | Vals AI；财报检索、计算、财务口径与分析 | 关键条件未通过即归零的加权部分得分 | 金融QA、财报比较、工具计算 |
| ExtractBench原版 | LlamaIndex／基准作者；相同370份文档与schema | 每文档value F1的等权均值 | NER邻近能力、字段／列表完整提取 |
| AA分项 | Artificial Analysis；AA-LCR v1.1、AutomationBench-AA、Terminal-Bench 4.0 | 各自协议下得分／pass@1 | 多文档推理、自动化与代码任务 |
| BizBench v1 | 基准作者；50个支付业务长任务，各3次 | 目标、过程、保护条件同时通过的严格成功率 | 说明多步任务还需验过程与授权 |

### 2.1 金融研究：Finance Agent v2

作者页面更新于**2026年10月18日**。相同默认harness提供EDGAR检索、网络检索、HTML读取、资料查询、计算器和价格历史六种工具；每题限时2小时。主指标为**带关键条件门槛的加权部分得分**，不是整题全对率。评分使用三模型评审组。[榜单和方法](https://www.vals.ai/benchmarks/fabv2)

| 模型标签 | 主指标（%） | 对本项目的意义 |
|---|---:|---|
| Qwen 3.8 27B | 48.55 | 可以作为个人金融辅助起点，复杂分析仍需分步校验 |
| DeepSeek V4.1 Flash（原版） | 53.48 | 与共享长任务主线相符，但未领先所有对照 |
| **DeepSeek V4.1 Flash 1017** | **56.96** | 已开放权重／MIT的升级候选；分数单列，保留原版部署和历史评测 |
| GLM 5.3 Flash | 57.85 | 金融任务的优先备选／挑战者 |
| GLM 5.3 | 55.84 | 更大权重在本榜没有稳定转换为更高分 |
| MiMo V2.6 Flash | 56.28 | 同时保留资源效率与金融任务的比较价值 |
| MiMo V2.6 Pro | 57.34 | 较Flash仅高1.06个百分点；先证实内部增益再扩大资源 |
| Kimi K3 | 53.11 | 作为复杂研究与办公能力参照，不因规模直接优先 |

出处：上表均来自同一[Vals作者榜](https://www.vals.ai/benchmarks/fabv2)，原始行见[CSV](data/public-benchmarks-2026-10-20/finance-agent-v2.csv)。该页未逐行公开thinking强度、精度、权重SHA和置信区间；接近的分数不作显著优劣结论。榜中API耗时和费用属于作者的端点与任务，不换算为本地GPU速度或内部TCO。

Gemma 31B在旧**v1.1**页面为50.79%；本轮v2表未列Gemma。两个版本题目及判分不同，旧分数不并入上表。Kimi模型卡引用的历史Finance Agent v2分数也与本次榜单快照不同，主稿统一使用本次作者页面。[旧v1.1](https://www.vals.ai/benchmarks/finance_agent)、[Kimi卡片](https://huggingface.co/moonshotai/Kimi-K3)

### 2.2 字段与实体提取：ExtractBench

**同任务集比较的是完整pipeline。** 370份英文企业文档中145份属于金融域；短文252份（≤10页），中篇98份（11–50页），长篇20份（>50页）。使用统一schema和值评分，包含缺失值、跨页列表与表格。每份文档等权，短文占总分约68.1%，长文约5.4%。[作者README和评分方法](https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/README.md)

| pipeline模型 | 全集value F1 | 短文 | 中篇 | 长篇 |
|---|---:|---:|---:|---:|
| Qwen3.8-27B-FP8 | 89.75 | 94.68 | 87.54 | 38.45 |
| Qwen3.6-35B-A3B-FP8 | 88.11 | 92.86 | 86.37 | 36.90 |
| DeepSeek-V4.1-Flash | 87.11 | 94.44 | 81.49 | 22.23 |
| GLM-5.3-Flash | 80.75 | 96.30 | 51.56 | 27.83 |
| Kimi-K3 | 83.17 | 94.64 | 69.64 | 4.99 |
| Gemma 4 26B A4B | 70.27 | 77.70 | 59.61 | 28.88 |

单位为F1×100，越高越好。来源：[作者CSV固定修订](https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/leaderboard.csv)，[本地提取表](data/public-benchmarks-2026-10-20/extractbench.csv)。MiMo和Gemma31B在本次原版CSV无对应条目。

| 条件 | Qwen27／35 | DeepSeek原版 | GLM Flash | Kimi K3 | Gemma26 |
|---|---|---|---|---|---|
| 端点 | 自托管vLLM，FP8 | DeepSeek API | z.ai API | Fireworks API | 自托管vLLM |
| 输入 | 150dpi逐页图像 | 150dpi逐页图像 | 原文件file_url | 150dpi逐页图像 | 100dpi逐页图像 |
| 最大输出token | 32,768 | 65,536 | 131,072 | 131,072 | 32,768 |
| thinking | 源码未显式设置；取端点默认 | 关闭 | 开启；effort未显式设置 | 取提供商默认 | 源码未显式设置；取端点默认 |

以上配置temperature均为0；一次请求完成提取，使用JSON object模式。配置出自[原始pipeline](https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/src/extract_bench/inference/pipelines/extract.py)及provider源码，完整条件见CSV。因此可说“Qwen27的该提取pipeline表现较好”，不扩张成“同精度、同推理预算的纯模型胜负”。值正确与引用正确分别测；这里展示的是value F1，不能称引用F1。

**业务含义：**公告提取可以从短文、固定schema开始；长列表分段后检查记录数量、重复与遗漏。该基准覆盖公司名、日期、金额等字段提取的邻近能力，但不是中文金融NER的实体边界F1，也不测公告事件归因、交易时点或下游投资收益。

### 2.3 长上下文、工具和终端：AA作者分项

以下使用2026年10月20日同站快照。只并列同名分项；不使用综合Intelligence Index作为金融排名。模型thinking标签直接沿用作者，GLM Flash／MiMo Flash标签未带effort后缀。[DeepSeek/Qwen](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-vs-qwen3-8-27b)、[GLM/Kimi](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-kimi-k3)、[MiMo/Qwen](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-qwen3-8-27b)、[Gemma/Qwen](https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-gemma-4-31b)

| 模型／作者标签 | AA-LCR v1.1 | AutomationBench-AA | Terminal-Bench 4.0 |
|---|---:|---:|---:|
| Qwen3.8-27B xhigh | 82 | 48 | 6 |
| DeepSeek-V4.1-Flash max（原版） | 84 | 69 | 27 |
| GLM-5.3-Flash | 80 | 60 | 33 |
| MiMo-V2.6-Flash | 74 | 64 | 23 |
| Kimi-K3 max | 89 | 58 | 13 |
| Gemma 4 31B reasoning | 70 | 5 | 0 |

单位为%，越高越好。AA-LCR v1.1为100道约100K token多文档问答，重复3次；AutomationBench-AA为657项SaaS任务、50轮上限，违反保护条件则归零，否则按完成目标比例得分；Terminal-Bench4.0采用mini-swe-agent，66项任务、每项重复3次、500步上限。具体判分与harness以[作者方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)为准，工具设置不能从一个分项套给另一个。完整设置保存在[条件记录](data/public-benchmarks-2026-10-20/evaluation-conditions.json)。AA-LCR v1.1修订过答案和评审，不混入v1.0；这组结果也不是接近满1M窗口的质量测试。

**业务含义：**Qwen27可支持个人多文档分析；共享复杂任务应同时考察DeepSeek与GLM Flash。Kimi在这组长文问答较强，仍需结合巨大权重和具体任务收益判断投入。Gemma保留来源不同的备选价值，但本组任务证据支持先验证31B，再考虑26B；不能直接用Google品牌替代中文业务验收。

### 2.4 长任务可靠性：BizBench

作者2026年10月14日论文在相同50个任务、相同资料和工具中比较下列模型，各任务运行3次；用户模拟器均为DeepSeek-V4.1-Flash。目标完成G、过程合规P、保护要求F分别判分，严格成功要求G∧P∧F。判分核对状态和执行记录，不依赖LLM评审。[论文§5、表1](https://arxiv.org/html/2610.20424v1#S5.T1)

| 模型 | 目标完成G | 严格成功 | 中间过程／保护失败 | 三次都成功的任务占比 |
|---|---:|---:|---:|---:|
| Qwen3.8-27B | 42.0 | 32.7 | 28.0 | 10.0 |
| DeepSeek-V4.1-Flash | 46.7 | 43.3 | 9.3 | 26.0 |
| GLM-5.3-Flash | 48.0 | 43.3 | 29.3 | 22.0 |

单位%。最后一列是三次**全部成功**的pass^3，不是至少一次成功的pass@3。论文未完整披露每个模型的推理参数，仓库示例配置不能当作原始运行日志。默认运行还受90分钟墙钟和错误阈值约束，发生上下文溢出时可压缩旧检索结果。[作者实现](https://github.com/ant-intl/BizAgentBench)

**业务含义：**目标答案正确之外，要检查授权顺序、只读边界与过程记录。此测试是支付业务，不映射成基金业务成功率；它为NAS权限问答和材料预审需要的验收方法提供直接启发。

## 3. 中文理解与数学／代码的补充核查

**中文金融理解有直接补充证据，但精确型号覆盖不足。** ReLE作者维护的中文“金融基础知识”榜（v5.12.7，10月15日）列DeepSeek原版82.4%、GLM Flash82.4%、GLM5.3为84.0%、KimiK3为80.8%、MiMo Pro80.0%、Flash76.0%、Gemma31B70.4%、26B68.8%。未列Qwen3.8-27B，不以Qwen Max、3.6-27B代替。该榜未逐行披露thinking、工具、harness、冻结权重及不确定性，本稿仅作为中文能力覆盖的辅助证据。[中文榜原文](https://github.com/jeinlee1991/chinese-llm-benchmark/blob/main/leaderboard/金融基础知识.md)、[已归档数据](data/public-benchmarks-2026-10-20/chinese-finance-supplement.csv)

**数学与代码成绩按原任务保留。** Qwen27官方LiveCodeBench v6为90.3；Gemma31B／26B官方同名v6为80.0／77.1，但两家未给出足够一致的全部运行条件，本稿不据此作严格横向胜负。Gemma的AIME2026无工具为89.2／88.3；DeepSeek原版MathArena Apex在max effort为65.6。它们说明数学／代码覆盖，不代表财务单位、会计口径或研究代码全部正确。[Qwen卡片](https://huggingface.co/Qwen/Qwen3.8-27B)、[Gemma卡片](https://huggingface.co/google/gemma-4-31B-it)、[DeepSeek卡片](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

Gemma两项官方同协议MRCR v2（8 needle、128K平均）分别为66.4%和44.1%，为31B优先于26B进行长资料验证提供依据；该检索任务与AA-LCR、多文档摘要分别保留。[Google卡片原表](https://huggingface.co/google/gemma-4-31B-it#benchmark-results)

代码Agent的headline更依赖完整系统：DeepSeek官方同一模型、最高思考强度下，DeepSWE v1.1使用Claude Code为69.8，mini-SWE为74.2；Qwen27卡片的DeepSWE42.2用Claude Code＋256K，而DeepSeek74.2用mini-SWE＋1M。因此不能把42.2和74.2画成相同harness的模型能力差。AA本次SciCode字段被标为“Under review”，已保留数据，不作为主要选型依据。[DeepSeek跨harness原表](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash#performance-across-agent-scaffolds-deepswe-v11-and-terminal-bench-21-max-reasoning-effort)

## 4. 总计划三项任务能被覆盖多少

| 总计划任务 | 已有公开证据 | 仍须在未来业务验收中测什么 |
|---|---|---|
| 金融NER／公告事件提取 | ExtractBench金融域schema提取；ReLE中文知识补充 | 中文全称／简称、实体边界和类型、金额单位、日期、事件状态；实体F1与完整事件记录准确率分别计 |
| 金融QA | Finance Agent v2检索、财务理解、计算和多步研究；AA-LCR长材料定位 | 内部资料可回答性、原文引用、数值与口径、正确拒答、ACL；不以通用知识答题代替检索链路质量 |
| 多文档摘要 | AA-LCR跨文档推理；Finance Agent披露比较；ExtractBench列表完整性 | 逐项事实覆盖、冲突与期间处理、引用支持、重大遗漏、阅读与返工时间；目前没有可直接套用的中文多文档摘要验收分数 |

后续验收以“字段表、比较表、计算文件、引用清单、测试结果”等实际产物为单位。质量达标后，再把人工活动时间、等待、重试与资源成本接入合格任务成本。配套[任务评价协议和12个虚构种子样例](../pilots/data/final-pilot-roadmap-2026-10-20/evaluation-protocol.md)已备好，未运行模型，不产生本地质量分数。

## 5. P08／P30–32可直接使用的讲述

**P08：**“个人路线先用Qwen27，因为公开文档提取与长材料问答给出了足够的能力依据，资源也能与个人设备配套。共享路线保留DeepSeek，1017已开放权重，可作为同资源架构的升级候选。金融研究同榜中GLM Flash和MiMo同样值得比较。我们按任务选模型，再比较配套资源，公开评测和既有测量各自保留版本。”

**P30：**“第一批选择公告提取和研究代码辅助：一个交付字段与出处，一个交付通过测试的修改。随后把字段和计算方法扩展为财报比较，再接入公司权限资料。每一步都有能被同事检查的产物。”

**P31：**“本轮已经用公开评测回答模型能做哪些工作。下一阶段用同一组中文任务、引用和评分标准核对实际系统，再记录人工节省和合格任务成本。长窗口能装下材料，完整提取、正确引用和连续执行还需要分别验收。”

**P32：**“先把两项可核查任务交付给小组，取得质量与人工基线；再扩展财报比较；NAS身份与撤权链路通过后接入共享知识库。共享GPU规模由任务量、等待和合格任务成本决定。”

## 6. 数据与来源交接

- [ExtractBench分长度SVG](data/public-benchmarks-2026-10-20/extractbench-length.svg)、[金融研究SVG](data/public-benchmarks-2026-10-20/finance-agent-v2.svg)、[BizBench过程评价SVG](data/public-benchmarks-2026-10-20/bizbench-goal-strict.svg)、[AA三项SVG](data/public-benchmarks-2026-10-20/aa-selected.svg)；均有配套CSV输入，适合在PPT重画可编辑图表。
- [TECH-091证据说明](../sources/TECH-091/evidence-note.md)记录网址、抓取日期、SHA、可支持的论断与设置缺项；十项模型卡按当前修订保存。来源作者对自己的基准拥有第一手记录，模型发布方跑分仍为发布方自报。
- 不同榜的费用、速度和成功率未合成总分。Spark外部随机token性能继续沿用[原专项身份](../infrastructure/dgx-spark-qwen27-external-benchmark-2026-10-12.md)，不填入本页质量数据。
