# C 版证据、时间预算与核查记录

正文：[extended-draft-c.md](extended-draft-c.md)。共 35 页，含封面和结尾，预计讲述 40 分 15 秒。

作者依据 2026-10-22 更新的 [initial-draft.md](initial-draft.md) 与 [c-authoring-brief.md](c-authoring-brief.md) 独立写作。只读取这两份任务材料、本地知识库索引、研究笔记及对应原始归档，没有读取 A／B 稿、旧 review、旧 session、旧 PPT 或旧 plan。本轮未运行模型、连接 GPU、执行付费 API 或取得新的报价。

资料采用知识库截至 2026-10-20 的冻结状态。正文中的当前选择指该研究快照，不声称已搜索核验 10 月 21–22 日的一切新增发布。外部测试、公开基准、条件计算和公司实测严格区分。适用上级路径未发现 AGENTS.md。已阅读 Presentations 技能，仅采用与本次 Markdown 交付相符的文字质量、受众与事实核验要求，没有生成幻灯片文件。

## 阅读顺序与时间预算

前半段以财报任务逐步解释参数、上下文、能力和速度。模型比较产生实施起点，推理流程进一步解释运行性能，再把设备与工作量变成成本变量。工具与入口最后用两页接回工作。正文没有要求读者跳回指定页拼接论证。

| 页 | 秒 | 页 | 秒 | 页 | 秒 |
|---:|---:|---:|---:|---:|---:|
| 01 | 30 | 13 | 75 | 25 | 90 |
| 02 | 45 | 14 | 75 | 26 | 90 |
| 03 | 60 | 15 | 60 | 27 | 75 |
| 04 | 45 | 16 | 60 | 28 | 75 |
| 05 | 60 | 17 | 75 | 29 | 75 |
| 06 | 60 | 18 | 75 | 30 | 90 |
| 07 | 60 | 19 | 60 | 31 | 75 |
| 08 | 60 | 20 | 90 | 32 | 60 |
| 09 | 75 | 21 | 75 | 33 | 60 |
| 10 | 60 | 22 | 75 | 34 | 60 |
| 11 | 75 | 23 | 90 | 35 | 60 |
| 12 | 75 | 24 | 90 | 合计 | 2,415 |

页内限定语属于上屏内容，但讲述不必逐字重复。时间预算包含读图与过渡，不包含独立问答。35 页已达到允许上限，后续补入材料应伴随替换或压缩。

## 逐页证据与边界

### 01，30 秒

研究主题与目的来自 initial draft。封面不作技术能力或已部署成果声明。机构与实习单位匿名，保留日期到月份。

### 02，45 秒

语言模型的工作描述采用一般机制说明，具体用途与 [公开能力研究][bench] 的任务分组、[本地 LLM 研究][local] 相符。表中“可以得到”描述产物形态，不是任何模型在公司任务上的保证。没有将文本生成等同事实正确，也没有使用未经测量的节省比例。

### 03，60 秒

直接检查 [FUND-308 原文][penghua] PDF 物理第 5–7 页和 [FUND-352 原文][maxwealth] PDF 第 1–2 页。

鹏华投研助手的输入是 A 股公告、新闻舆情、券商研报，对应标签、个股舆情要点与摘要。营销审核的输入是宣传物料，对应修改建议。永赢邮件安全输入覆盖文本、附件、链接、二维码和 HTML，不改写为交易对话或会议录音。前中后台标签是本稿按工作职责归类。均为机构自述，通过协会发布，一手披露不代表独立效果评测。为保持开头简洁，没有使用采纳率、节省成本或检出率。

### 04，45 秒

公司的本地部署出发点来自 initial draft。架构为研究解释图，参考 [参考架构][architecture] 与 [最终来源核查][refresh] 第 6 节。只讲资料授权和运行条件，没有把本地部署写成自动合规，也不进行具体法律适用判断。图中各系统不代表公司已经建成。

### 05，60 秒

本页是教学任务设定，没有虚构公司的财报数字或把它包装成已经完成的测试。验收对象参考 [公开能力研究][bench] 第 4 节与 [TCO 研究][tco] 第 1 节。任务使用一份包含比较数字的当期财报即可成立，后续 TCO 则单独规定完整多轮轨迹，二者没有冒充同一测量样本。

### 06，60 秒

参数、上下文和推理是机制解释，参考 [模型研究][models] 与 [Serving 调研][serving]。用“通常不会更新权重”保留训练与在线输入的区别，没有暗示所有部署都无需数据处理或模型微调。本页只引入理解下一步所需概念。

### 07，60 秒

四档预算直接来自 [最终配置][config] 第 1 节。8,192 输出从总窗口扣除，覆盖思考与生成内容。1M 采用本研究的 1,000,000，不混写成模型配置的 1,048,576。token 与文档页数没有固定比例。

### 08，60 秒

指标定义参照 [Spark 外部原始汇总][sparkraw]、[Serving 调研][serving]。TTFT 包含 HTTP／校验、排队、prefill 和首生成步骤，不能直接视为纯 prefill。decode 不含首 token 等待。吞吐是否端到端、哪些请求进入共同窗口，留给对应数据页说明。能力采用任务分项，没有把“智力”视为一个直接可测的单值。

### 09，75 秒

取舍属于工程解释，依据 [模型研究][models] 第 3–5 节、[最终配置][config] 的缓存／并发结果及 [Serving 调研][serving]。条件明确限定在给定模型、硬件和运行方式。“不可能三角”只保留为直觉，不作定理，也不以参数数目推出能力排序。

### 10，60 秒

硬件与目标引用 [最终配置][config] 第 1、2、5、6 节。Spark 单人 20+、共享每路 10／20 token/s 是目标。131K／262K 为基础研究档位，512K／1M 为长任务档位，未声称已经证明是业务最低需求。八 H200 是分析资源情景，不是公司采购或已部署设备。

### 11，75 秒

模型类型、窗口与体量依据 [模型研究][models] 第 3 节及其各模型固定索引。补核 [Qwen27 模型卡][qwencard]、[DeepSeek 模型卡][dscard] 和 [制品对照][artifacts]。表格是模型候选的资源描述，不做运行内存排名。

Qwen27／35 和 Gemma 用归档 BF16 体量，不能以它们与 MiMo 的 MXFP4 混合制品直接比较参数效率。MiMo 172.92GB 为主索引，不包含独立 DFlash／音频制品。DeepSeek 的主干与 Engram 参数计数不同，本页不压缩成易混淆的单个参数量。主方案 FP8 Qwen 与基表 BF16 明确分开。GLM 主版、MiMo Pro、Kimi 保留在能力比较中，没有为覆盖全部候选再扩一页。

### 12，75 秒

直接核对 [ExtractBench 原始榜单 CSV][extractcsv] 的四行及 [作者 README][extractreadme]，配置解释对照 [公开能力研究][bench] 第 2.2 节。全集分数是 370 份文档等权，不是按字段总量或页数加权。252 短、98 中、20 长，全集不能当作长文表现。

模型端点、图像／文件输入、thinking 和输出预算并不一致，所以正文称完整提取流程。所有配置 temperature＝0、单次提取、JSON object；Qwen 最大输出 32,768，DeepSeek 65,536，GLM 131,072。Qwen thinking 未显式设置，GLM effort 未显式披露。该指标是 value F1×100，不是引用 F1、中文实体边界 F1或业务成功率。页上保留影响横向比较的关键差异。

### 13，75 秒

AA 分项来自 [公开能力研究][bench] 第 2.3 节、[评测条件记录][conditions] 与 [AA 对照归档][aaoriginal]。AA-LCR v1.1 是 100 题、约 100K 多文档、每题 3 次。正文保留各模型原标签，未给未披露模型补写统一思考强度。两项测试衡量不同任务，不能将本页 82% 和提取 F1 加权形成总分。Kimi 的 89% 不推出最适合当前硬件。

### 14，75 秒

直接核对 [Vals 原始 HTML][valshtml] 的模型表与 [方法提取][valsmethod]，数值与 [Finance Agent v2 CSV][financecsv] 一致。主指标为 dealbreaker-gated severity-weighted Partial Credit，关键项失败导致整题归零，仍不等于整题全对率。

默认提供 EDGAR、网络搜索、HTML 读取、资料查询、计算器和价格历史工具，每题限时 2 小时。正文不使用 API 耗时推本地速度。原版和 1017 单列。Gemma 历史 v1.1 分数没有混入 v2。方法说明多次运行与误差汇总，但未用数据缺项强行做统计检验，正文只解释描述性差异。

### 15，60 秒

这页是研究判断，综合 [公开能力研究][bench] 第 1 节、[最终配置][config]、[来源刷新][refresh] 第 2–3 节。个人选择同时考虑提取、长文能力、实际设备上的速度证据。共享选择保留 DeepSeek 的可追溯资源与运行路线，不声称它在金融榜第一，也不把尚无同机数据的 GLM/MiMo 写成较慢。

Spark 的约 20 token/s 保留随机输入外测身份。DeepSeek 1017 的配置、完整权重索引和 LICENSE 与该次原版快照逐字节相同，见 [制品对照][artifacts]。这只支持静态资源预算，不能证明权重值、质量与速度相同。原版测试不改标 1017。

### 16，60 秒

机制图依据 [Serving 调研][serving] 和 [A100 专项][a100] 第 1.3 节。模型权重预先加载，输入进入队列后做 prefill，decode 产生结果或工具调用，工具结果追加回新请求。图简化了多个状态与调度过程，不表示任何请求一定调用工具，也不表示权重每轮重复下载。

### 17，75 秒

prefill／decode 瓶颈为工程解释，依据 [Serving 调研][serving] 与 [A100 专项][a100] 第 2 节。使用“低并发时常常限制”而非声称 decode 一律受带宽限制。高并发、MoE 通信、长历史和专用算子都可能改变瓶颈。先解释资源，再进入缓存量，避免一开始堆叠优化术语。

### 18，75 秒

载荷公式和字节数来自 [最终配置][config] 第 3 节及 [恢复算例 CSV][restorecsv]。本轮重新以 `context×65,536／32,768÷10^9` 校验，显示到两位小数。该表仅 Qwen27 全注意力 KV，明确未含 GDN 递归／卷积、MTP、allocator 与工作区。正文没有将数据当作整机所需总内存。

### 19，60 秒

框架角色依据 [Serving 调研][serving]，版本更新用 [vLLM 0.32 发布原文][vllmrelease] 与 [来源刷新][refresh] 第 3 节，覆盖旧笔记的 0.29／nightly 状态。

vLLM 为本次推荐主线，SGLang 为重要对照，不是同机速度结论。MLX 与 llama.cpp 用作路线描述，不承诺所有候选转换与协议均可直接运行。A100 按 [A100 专项][a100] 使用 modified vLLM。没有把框架通用能力写成本人实现成果。

### 20，90 秒

所有数字直接取 [TECH-076 外部原始汇总][sparkraw]，并对照 [专项分析][sparkstudy]。来源是用户在 10 月 12 日提供的朋友实验总结，主测试日期未知，本研究未拿到 environment.json、launch.sh 和逐请求原始日志，无法自行复跑或重新计算统计量。

完整条件：主机 A、单 GB10、TP1、FP8 权重、默认尺度 FP8 KV、未进行 KV 校准、MTP3、FlashInfer、YaRN4、`max_num_seqs=8`、`max_num_batched_tokens=16384`、内存预算 0.80、关闭 prefix caching、temperature 0、ignore_eos。输入直接使用随机普通 token ID，由 usage 核长度。长度修复后主模型与 draft 均 1M。50K／100K各 2 次，300K／500K各 1 次，1M容量 1 次。1M 是 999,936＋64，不能改成 1M 输入加输出，也不能与长输出稳定速度合并。正文保留必要条件，细项放此处。

### 21，75 秒

直接检查 [TECH-076][sparkraw] 的“MTP 长度门限诊断”。5.80 与 17.23 是同一问题修复前后提供方汇总，99.4% 接受率与平均长度 3.98 保留其原定义。正文明确不能作为正常 on/off 消融，也不将随机输入的高接受率延伸到真实任务。

该页说明版本和参数如何影响实际性能，是研究得到的诊断案例，不声称修复操作由本项目在公司设备完成。

### 22，75 秒

token 池和三请求数据来自 [TECH-076][sparkraw]，[最终配置][config] 第 3 节与 [共享 CSV][sharingcsv]。容量重新算：`1,806,907×0.9−3×524,288≈53,352`，表内三人共同窗口总速率 59.08／52.41，按三路平均为 19.69／17.47。每请求完整生成阶段均值为 16.85／12.45，分母不同，不能互换。

3×512K 是驻留条件计算，没有该长度三人同时生成的外测。页内调度安排是工程建议，不是已验证最优参数；“分块 prefill”不承诺消除所有干扰。

### 23，90 秒

架构与传输算例来自 [最终配置][config] 第 3.3、7 节和 [恢复 CSV][restorecsv]。Spark `32.768÷6=5.4613秒`。DeepSeek TP8 `1,827×1M×8=14.616GB`，除八卡合计有效 24GB/s 得 0.609 秒。没有把卡数乘进带宽后再重复计算，也没有给统一内存 Spark 人为加一跳外置 GPU PCIe。

直接核对 [Qwen LMCache recipe][qwenrecipe] 的 `align`、prefix caching、分组缓存和实验性提示，以及 [DeepSeek recipe][dsrecipe] 的 fp8_ds_mla、多组几何、scratch 重建和 MTP 未验证。恢复需要匹配制品、前缀、位置、精度、后端、GPU、块布局和权限。聊天文字可重建任务，但不等于引擎状态缓存。图是普通独立 GPU 分层，Spark 特例随文说明。

### 24，90 秒

权重体量与 Engram 来自 [TECH-079 固定权重索引][dsindex] 和 [最终配置][config] 第 5.1 节。总数 510,286,023,000 B，Engram 202,758,032,400 B，差额 307,527,990,600 B。

Hopper 1,827 B/token/rank 依据该研究对固定 attention 源码的布局复算，源码见 [vLLM 0.32 attention][attention]。不能直接使用模型论文另一硬件格式的 890 B/token。20×1M×1,827＝36.54GB/rank，TP8＝292.32GB。这是 global KV 记录载荷，启动池还受到 SWA、草稿、scratch、图和 allocator 限制。Engram 是权重查表，不是用户记忆或会话缓存。

### 25，90 秒

[最终配置][config] 第 5.2–5.3 节、[容量 CSV][capacitycsv]、[公开 server 日志][serverlog] 支持 token 池数值。[vLLM Engram 原文][engram] 支持同机 DP 共享主存。

28.250M／16.935M 是 post-graph 建议 GiB 线性缩放后的严格预算敏感性，尚未扣 10% token 余量，更不是重新加载后的测量。正文对此明确标注。TP4 使用 C32 profile，避免将 C16 池与 C32 图内存混用。40 份历史严格上限为约 635,584／762,048，正文取 636K／762K，仅作近似。

公开池镜像完整身份：`nightly-cd10ed6f9f6b37a8ace9cf380007e66fe12ec0c3`，Engram CPU offload、FP8 MLA/index、DSpark5。v0.32 的新 DP 布置不能借用旧池标成新实测。共享要求 CPU offload、DP>1、同节点、共享 IPC、足够 `/dev/shm`，两条独立 serve 不自动共享。

### 26，90 秒

公开值来自 [AgentX benchmarks JSON][agentx]，与 [回放 CSV][replaycsv]、[最终配置][config] 第 6 节逐项核对。固定镜像见上一项，模型原版，合成接受长度 3.51。表中是端到端系统 output token/s，不是 total token/s、不含缓存读取冒充输出，也不以吞吐除活跃会话数得到逐请求实测。

目标复算：20×10／20＝200／400；8,192÷10／20÷60＝13.65／6.83 分钟。20×(1,000,000−8,192)÷900＝22,040.18 fresh input token/s。目标排除工具、恢复、排队与失败，不能当业务任务产量。首轮输入处理与高命中回放严格分开。

### 27，75 秒

依据 [A100 专项][a100] 第 2 节，直接核对 [Tokha 消融原文][ablation]。准确设备是八 A800 80GB SXM，不是八 A100；该记录用于 SM80 路线研究。相同 C128、78–90 token coding 输入、固定 1,024 输出、effort100，基础已含 DSpark5、CUDA Graph、FP8 KV、EPLB 等补丁。180 秒计时及 TP4×DP2＋EP8 见 [作者 README][tokhareadme]。

两次均值 2,842.48／2,926.08／2,970.50。逐档约 2.94%／1.52%，合计约 4.5%。两次不构成统计显著性证明。shi3z 主机器四 A100 PCIe、两组 NVLink 卡对，与 SXM/NVSwitch 不同。模型自带低位权重、CED、共享 KV 和 DSpark 不归为自定义引擎原创。固定 modified vLLM 是维护与工程路径判断，不承诺某 fork 已完成公司验收。

### 28，75 秒

预算来自 [整机采购研究][hardware]、[来源刷新][refresh] 第 4 节及 [硬件价格 JSON][prices]。Spark 美国挂牌、A100 翻新整机、H100／H200 整机挂牌和 H200 NVL 单卡 BOM 各自保持身份。四 H200 NVL 是 161–283 万元估算，不能当成与公开四 H200 server 完全相同的已测机器，正文已保留准确配置复验要求。

人民币用 7.00 预算汇率、税费／价格准备、交付和本地支持假设。A100 翻新／90 天原卖方保修身份不能改写新机原厂支持。境内准确 SKU、交易条件、交付和支持仍待具体报价；本稿不作采购许可结论。H100 的 242,240 采用严格 post-graph＋10%口径，不混用旧池可算出的 289,536。工具 CPU 12–26 万元单列，GPU 整机已有 CPU/RAM 不重复采购。

### 29，75 秒

依据 [TCO 研究][tco] 第 1、3、4 节、[逐轮账][ledger]。输入为 100K、110K、……170K，合计 1.08M。每轮 2K 输出，共 16K，最后总长 172K。10% 额外轨迹覆盖追加与重跑，未称为 90.9% 成功率。

个人三年计划交付 750／825／907.5＝2,482.5，公司 25,000／31,250／39,062.5＝95,312.5。非整数是预算期望量，不是真实任务记录。既有 NAS／身份／检索和员工终端复用，未新增全库入库工程或 Onyx 授权。公司两种推理路线均保留 18 万元工具 CPU。人工复核作为业务时间另计，避免和平台运维重复。

### 30，90 秒

数值来自 [TCO 原始结果][tcoresults]、[堆叠分项 CSV][bars] 和 [TCO 研究][tco] 第 5–6 节。公司本地“设施等”20.93＝接入3＋GPU及CPU电费6.5263＋机位5.4＋软件支持6；API 6.8830＝平台6＋CPU电费0.8830。四舍五入后的各项相加和总额一致。

DeepSeek [10月20日价格归档][dsprice]：低峰未缓存／缓存输入／输出为每百万 USD0.15／0.003／0.60，高峰为两倍。80% 高峰等于低峰费率×1.8。缓存按可复用前缀 95% 命中预算，另扣边界，不把首次新内容算命中。API token 费按汇率7.00并预留6%，不是税务确认。三年费率恒定是假设。公司本地功耗、PUE、年运维都是分析输入，未以 PSU 额定功率当耗电。

资料范围依据 [来源刷新][refresh] 第 5 节的已归档服务条款，正文仅保留“符合服务条款的获准资料”，没有开展法律建议。为控制篇幅，本稿不展开全球 Sonnet 对照和相应主体／地域限制，也没有拿它的较高价格证明本地回本。省略不改变 DeepSeek 对照的资源边界。

### 31，75 秒

依据 [TCO 研究][tco] 第 7、9、10 节，[逐轮账][ledger] 和 [敏感性 CSV][sensitivity]。本地复用历史按 90% 命中假设计，首轮冷输入与追加输入分别计算，273,240＝248,400×1.1，17,600＝16,000×1.1。机时 `273240/8000+17600/400=78.155秒`，容量 `1400×3600/78.155≈64,487项/年`。两个吞吐维度没有相加成“总 token 速度”。

高情景年度 50K／75K／112.5K，后两年超过一台规划产能，因此节点 1／2／2。容量仅为平均负载规划，未证明突发 SLA，也没有预测并行节点线性加速。缓存全部失效的 712.75 万元来自独立敏感性分支，API仍维持基准。本文未引用 TCO 笔记中旧的 26.55M 缓存余量数，容量统一采用最新最终配置。

### 32，60 秒

A100 134.42／212.13 万元来自 [TCO 研究][tco] 第 8 节：复用分支假设改造 10 万元、年硬件支持 3 万元，实施65人天、年运维80人天，平均墙插2kW独立预算。没有对 A100 填入已合格单位任务成本。

工时价值来自第 11 节：95,312.5×0.25小时×150元＝3,574,218.75元。15分钟净节省是敏感性假设，不是实测；150元业务小时与2,500元技术人日不同。现金兑现需真实付款变化。结论只适用于给定工作量、材料可进入对应路线和任务质量可比的条件。

### 33，60 秒

两条产品路线来自 [场景二研究][rag]，[最终配置][config] 第 4 节。容量直接核对 [RAG 容量 CSV][ragcsv]：每张回答卡池 `84×0.9−31−6=38.6GB`；每会话 `(C×65536+153944064)×1.15` 字节。131K每卡3份、三卡9份，262K每卡1份、三卡3份。20路短问答精确是8192输入＋600输出，正文已写明。20路能驻留不是速度保证。

Onyx 企业本地部署需询价，不能以公开云席位价格代替，本文不额外承诺某 NAS 连接器。自建路线的权限同步、撤权、引用再次鉴权仍需完成。图是建议流程，不称现有系统实现。

### 34，60 秒

入口与分工参考 [Harness 调研][harness]、[最终配置][config] 第 1、8 节。OpenCode、Hermes、Skills/MCP 为研究选项，具体版本、工具解析和文件权限没有被表述为已集成完成。CPU执行与GPU推理分开，员工终端可复用，不把工具调用都算成GPU负载。产物形式沿用公开能力研究的验收建议，没有铺开工具清单或项目周计划。

### 35，60 秒

总结对应本次研究已有资料，不声称完成公司设备部署、GPU PoC、业务质量验收或真实节省测量。研究完成与运行待验收并列说明。选型、服务、容量和成本结论均有前面的顺序解释，不依赖跨页跳转。

## 最终自查

- 页号连续 01–35，共 35 页，标题、文字和图表完整，包含封面、结尾。
- 总时间 2,415 秒，即 40 分 15 秒。模型比较与技术解释占主体，独立成本 5 页，工具层 2 页。
- 历史案例保持输入／应用／产物对应，没有使用国泰 BERT 实体识别当作生成式 LLM 案例，也未混入传统量化收益。
- 长窗口区分模型配置 1,048,576、本研究1,000,000、外测999,936＋64和512K总窗口；公开100K质量分数不扩大到1M。
- Spark 外测不称公司实测。未披露模型 revision／完整引擎版本不以10月20日新取得SHA补写。
- 共同decode、完整decode和端到端输出采用原分母；高命中回放不替代满窗口冷启动。
- 权重、Engram、global KV、启动池与系统内存分别计量。TP rank复制不漏算，也不重复除以TP。
- 成本采用同一任务轨迹与规模。已核对token加总、容量、恢复算例、消融百分比、TCO分项及扩容条件。
- 数据与软件时间冻结在归档时点。完整组合支持与通用框架能力分开，没有虚构已完成集成。
- 证据链接使用本地原件与数据，引用信息不混入最终上屏稿。所做自查确认材料与算术一致，不替代独立审稿或设备验证。

## 来源入口

以下相对路径均从本文件所在目录解析。原始页面 URL、获取日期、SHA 和人工复核缺口可沿各来源目录 metadata 追溯。知识库研究文档是解释层，原件和数据另列。

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
