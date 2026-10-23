# D第三轮修订：选型依据、版本与讲述时间

正文：[extended-draft-d-revised-3.md](extended-draft-d-revised-3.md)。先行工作稿：[d-chapter-3-selection-logic.md](d-chapter-3-selection-logic.md)。用户说明：[d-revised-3-response-for-user.md](d-revised-3-response-for-user.md)。

本轮核验日期为2026-10-23。全文47页，其中正文39页，封面1页、目录1页、章节页6页；讲述预算40分钟。第三章使用用户直接提供的实际决策过程组织，第四、第五章保持上一轮形成的请求与费用路线，顺延一页。

## 1. 决策过程与外部事实各自承担什么

本轮用户直接确认的研究目标和判断包括：个人端优先成熟整机、降低部署维护负担；Spark在本次用途中的框架支持、综合性价比和NVIDIA技术栈复用价值；128GB容量范围内模型能力优先；Qwen27的模型能力和稳定使用表现优先于本轮个人候选，FP8速度可接受；服务器从单台八卡条件选原Flash，再在1017发布后更新。

这些内容在正文中作为演讲者的实际选择与判断呈现。公开资料用于核对产品、型号、文件体量、框架路径、GDPval-AA分数及设备运行结果。Qwen“稳定使用表现”保留为用户提供的定性调研判断；本轮没有新增业务质量、长期运行或候选稳定性测试。正文没有为这一判断虚构通过率或SLA。

## 2. 个人整机：正式名称、规格与预算

### 第17–18页

- **正式产品名：NVIDIA DGX Spark。** 实际打开[NVIDIA产品页](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)和[官方硬件说明](https://docs.nvidia.com/dgx/dgx-spark/hardware.html)。采用的设备为GB10、128GB统一系统内存、4TB NVMe，与[外部测量记录](../../../knowledge-base/sources/TECH-076/original.md)中的主机A一致。
- **Mac Studio搭载M5 Ultra。** 实际打开[Apple技术规格](https://www.apple.com/mac-studio/specs/)与[中国商店](https://www.apple.com.cn/shop/buy-mac/mac-studio)。256GB配置对应36核CPU／80核GPU，采用2TB SSD；统一内存与硬件名称已经核对。
- **框架路径：**实际打开[NVIDIA单设备vLLM部署指南](https://build.nvidia.com/spark/vllm)，其官方playbook目录也列SGLang；[MLX-LM](../../../knowledge-base/sources/TECH-023/original.md)和[llama.cpp](../../../knowledge-base/sources/TECH-025/original.md)支持Mac端运行路径。正文“共用技术栈”指服务框架、接口、配置与维护经验的复用。
- **价格：**Spark采用10月12日[价格输入](../../../knowledge-base/infrastructure/data/week7-deployment-2026-10-12/spark-price.json)，58,407–61,840元，正文约5.8–6.2万元。Mac采用9月21日已归档的[整机价格台账](../../../knowledge-base/infrastructure/data/hardware-prices-2026-09-21.json)W6，90,499元；其配置为M5 Ultra36／80、256GB、2TB，原记录对应Apple配置器官价。正文称“调研价格”，本轮当前商店用于确认产品和配置，未把旧价改标成新的成交报价。相关[配置研究](../../../knowledge-base/infrastructure/workstation-configurations-2026-09-21.md)保留逐项升级价。

“综合性价比”是用户对本次任务的选择判断，正文把它展开为购机投入、所需框架适配及后续维护的综合考虑。两台设备采用各自实际研究过的配置。

## 3. 个人模型：先模型能力，后速度

### 第19页的GDPval-AA

本轮实际打开[Qwen27／Qwen35官方对照](https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-qwen3-6-35b-a3b)，GDPval-AA v2.1行分别为1417／889。Gemma31B的620分采用同日已核对的[Qwen27／Gemma31B](https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-gemma-4-31b)。

| 正文名称与推理标签 | 官方模型仓库 | GDPval-AA v2.1 |
| --- | --- | ---: |
| Qwen3.8-27B／Xhigh | [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | 1417 |
| Qwen3.6-35B-A3B／Reasoning | [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | 889 |
| Gemma 4 31B／Reasoning | [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) | 620 |

GDPval-AA仍使用[既定官方方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)：模型在工具环境中交付专业任务文件，同题产物匿名配对形成Elo。新第19页仅保留理解比较需要的方法说明，完整方法与[原任务示例](https://artificialanalysis.ai/evaluations/gdpval-aa#example-tasks)已在本轮此前实际阅读。

### 第20页的架构与设备表现

本轮实际打开两份Qwen官方模型卡：27B被定义为稠密模型；35B-A3B卡片明确35B总参数、3B激活参数。正文据此解释生成过程的计算取舍，速度结果采用实际Spark记录。

[TECH-076原提供方总结](../../../knowledge-base/sources/TECH-076/original.md)：单DGX Spark、TP1、Qwen3.8-27B-FP8、FP8 KV、MTP3、FlashInfer、随机普通token输入、关闭前缀缓存。每请求输出2048：

| 输入 | 次数 | TTFT秒 | decode token/s |
| ---: | ---: | ---: | ---: |
| 50,000 | 2 | 63.1 | 21.01 |
| 100,000 | 2 | 144.8 | 20.11 |
| 500,000 | 1 | 1470.1 | 14.82 |

单次50K的decode范围20.95–21.07，100K范围20.10–20.11，保留在原记录；正文采用均值。原始环境文件与逐请求日志的取得状态继续沿原档案，不新增复现声明。用户认为这组FP8速度可以接受，正文用它说明模型能力优先之后所接受的实际速度取舍。

## 4. 服务器：原Flash到1017的连续两阶段

### 第21页候选及制品版本

读取[9月22日候选制品数据](../../../knowledge-base/models/data/model-artifacts-2026-09-22.json)后，本轮逐一访问对应官方仓库的**固定修订权重索引**，核对metadata.total_size，五项均与归档一致。

| 调研候选／官方仓库 | 固定修订 | 权重tensor字节 | 正文约GB |
| --- | --- | ---: | ---: |
| [deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/dba1be0a40aa45a94ad051997016db3960a90277/model.safetensors.index.json) | `dba1be0a40aa45a94ad051997016db3960a90277` | 510,286,023,000 | 510 |
| [XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/model.safetensors.index.json) | `73875d00b30a89ef8cc353a0b60b0e9f9561952d` | 566,027,990,784 | 566 |
| [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash/blob/eb9eb208eb0d988989d07a6a12d0fdeb5f52574a/model.safetensors.index.json) | `eb9eb208eb0d988989d07a6a12d0fdeb5f52574a` | 328,326,771,576 | 328 |
| [zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3/blob/aca966e4e02791568aa6a4ced368624b3d897f42/model.safetensors.index.json) | `aca966e4e02791568aa6a4ced368624b3d897f42` | 755,617,140,416 | 756 |
| [moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/model.safetensors.index.json) | `f831ab66814297da540d832a5235f8e904f29d06` | 1,560,860,324,864 | 1,561 |

MiMo的研究产品名为MiMo-V2.6-Pro，对应开放制品仓库为MiMo-V2.6-Pro-RL；正文在权重文件比较表采用仓库的准确名称。所有体量按各自发布格式计量。此表服务于放置空间的初步认识，运行布局在后续章节展开。

### 第22页：初始选择理由

原Flash的选择理由来自用户本轮对实际调研过程的确认。对应技术依据为[原Flash官方模型卡归档](../../../knowledge-base/sources/TECH-092/models/deepseek/README.md)、[模型及框架研究](../../../knowledge-base/infrastructure/serving-framework-survey-2026-09-17.md)及[公开多卡运行原件](../../../knowledge-base/sources/TECH-084/benchmarks.json)。

原版的约510GB制品、Engram主机放置、压缩共享历史，为单台八卡提供资源安排路径；vLLM与SGLang提供服务框架。原版公开八H200回放行442758，平均输入156,951tokens、系统输出1052.17744token/s、缓存命中95.711%、合成DSpark平均接受长度3.51。它在本轮作为初始选择中速度参照的来源，正文采用用户给出的综合调研判断，没有增加跨模型同机测速排名。

原Flash“模型能力足以承担目标工作”，是用户对初始选择的判断。第23页再进入1017发布后的更新，时间位置清楚分开。

### 第23页：版本更新与评价

实际打开[原Flash／1017官方AA对照页](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-1017-vs-deepseek-v4-1-flash)：截至10月23日，GDPval-AA v2.1分别为1600和1746，标签均为Max。表格明确写成当日对两个版本的评价，没有将该快照回填为9月当时获得的分数。

[10月17日官方发布](https://api-docs.deepseek.com/news/news261017/)与[1017官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)支持发布时间、开放权重和升级关系。同日已核的GDPval-AA候选结果中，MiMo Pro为1683、GLM Flash1642、Kimi K31533；正文以当日数据支持1017领先的判断。

最终主力版本仍固定为`deepseek-ai/DeepSeek-V4.1-Flash-1017`，修订`1bae0e1088993b9b82de08f59de5be5a34e42170`。本轮此前已直接核对该修订的配置、完整索引、参考实现：索引510,286,023,000 B，Engram表及尺度202,758,032,400 B。原Flash的历史性能保留其历史身份，第四章的现行部署继续使用1017的制品结构与明确服务目标。

## 5. 顺延页面的依据与预算

第四章现为25–36页，第五章37–42页，使用上一轮已核对的技术与成本输入，主要变化是页码与衔接。

| 本轮页码 | 主要来源与数值 |
| --- | --- |
| 5 | [MENTOR](../../../knowledge-base/sources/FUND-113/original.md)、[盈米客户端](https://github.com/yingmi-dev/content-compliance-skill/blob/040df66202f6075cdeadb450e502c7a19c83dabf/README.md)、[易方达开发测试](../../../knowledge-base/sources/FUND-101/original.md) |
| 26–33 | [AI Infra第3章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/03-推理与训练负载.md)、[第8章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/08-推理优化.md)、[Spark外测](../../../knowledge-base/sources/TECH-076/original.md)；8192÷20＝409.6秒；长度与三路并发均沿原记录 |
| 34–36 | 1017固定官方制品；[vLLM](../../../knowledge-base/sources/TECH-020/original.md)、[SGLang](../../../knowledge-base/sources/TECH-021/original.md)；20路×20token/s＝400总输出目标 |
| 38–42 | [硬件台账](../../../knowledge-base/infrastructure/data/hardware-prices-2026-10-12.json)、[TCO输入](../../../knowledge-base/infrastructure/data/tco-2026-10-20/inputs.json)、[原分项](../../../knowledge-base/infrastructure/data/tco-2026-10-20/presentation-bars.csv)，按当前一台服务器范围计算 |
| 44–45 | [入口与工具执行](../../../knowledge-base/sources/TECH-072/open-webui.md)、[权限](../../../knowledge-base/sources/TECH-068/onyx-permissions.md)、[知识库研究](../../../knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md) |
| 46–47 | 任务验证和选择总结，按本轮用户明确的实际过程组织 |

### 当前单台设备预算汇总

个人三年计划2482.5项，公司中等95312.5项，较低30000项。公司一台八H200、工具同机运行，现有NAS、身份和员工终端作为复用资源。公司预算已去除原外置工具CPU购置180,000元及三年电费8,830.08元。

| 公司中等量本地组成 | 人民币元 |
| --- | ---: |
| 八H200整机 | 2,973,646.64 |
| 机房接入 | 30,000.00 |
| 实施 | 112,500.00 |
| 三年技术运维 | 450,000.00 |
| GPU整机设施电费 | 56,433.22 |
| 机位 | 54,000.00 |
| 软件支持 | 60,000.00 |
| 合计 | 3,736,579.86 |

公司API为75,000实施＋300,000运维＋60,000平台支持＋59,601.2364调用＝494,601.2364元。个人本地90,465.64365元、API16,552.36794元。第42页低量本地3,728,163.1073元／30000＝124.27元，中量3,736,579.8581／95312.5＝39.20元。

工作轨迹8轮、首轮100K、以后每轮新增8K、每轮输出2K，累计输入1.08M、输出16K，额外轨迹10%。本地复用按90%、API95%，公司服务预算按8000未缓存输入tokens/s与400输出tokens/s、每年2000h和70%时间安排。价格及功耗假设、舍入与单机调整的完整计算保留在[上一轮测算记录第4节](d-revised-2-evidence.md)。这些计算与当前模型制品的部署规划相接，第四、第五章不再新增设备路线。

## 6. 时间分配

增加的一页用于完整讲清两段选型。第三章8:30；基础概念中已明确的步骤和结尾适当缩短。全场40:00，正文37:45、封面与目录0:45、六张章节页合计1:30。

| 分块 | 页码 | 时间 |
| --- | --- | ---: |
| 开场与目录 | 1–2 | 0:45 |
| 第一章 | 3–7 | 3:00 |
| 第二章 | 8–15 | 5:30 |
| 第三章 | 16–24 | 8:30 |
| 第四章 | 25–36 | 12:15 |
| 第五章 | 37–42 | 6:15 |
| 第六章 | 43–47 | 3:45 |
| 合计 | 1–47 | 40:00 |

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
| 9 | 正文 | 0:30 | 4:30 |
| 10 | 正文 | 0:30 | 5:00 |
| 11 | 正文 | 0:45 | 5:45 |
| 12 | 正文 | 1:15 | 7:00 |
| 13 | 正文 | 0:45 | 7:45 |
| 14 | 正文 | 0:30 | 8:15 |
| 15 | 正文 | 1:00 | 9:15 |
| 16 | 章节页 | 0:15 | 9:30 |
| 17 | 正文 | 1:00 | 10:30 |
| 18 | 正文 | 1:00 | 11:30 |
| 19 | 正文 | 1:15 | 12:45 |
| 20 | 正文 | 1:15 | 14:00 |
| 21 | 正文 | 1:00 | 15:00 |
| 22 | 正文 | 1:00 | 16:00 |
| 23 | 正文 | 1:00 | 17:00 |
| 24 | 正文 | 0:45 | 17:45 |
| 25 | 章节页 | 0:15 | 18:00 |
| 26 | 正文 | 1:00 | 19:00 |
| 27 | 正文 | 1:00 | 20:00 |
| 28 | 正文 | 1:00 | 21:00 |
| 29 | 正文 | 1:00 | 22:00 |
| 30 | 正文 | 1:15 | 23:15 |
| 31 | 正文 | 1:15 | 24:30 |
| 32 | 正文 | 1:15 | 25:45 |
| 33 | 正文 | 1:00 | 26:45 |
| 34 | 正文 | 1:00 | 27:45 |
| 35 | 正文 | 1:15 | 29:00 |
| 36 | 正文 | 1:00 | 30:00 |
| 37 | 章节页 | 0:15 | 30:15 |
| 38 | 正文 | 1:00 | 31:15 |
| 39 | 正文 | 1:15 | 32:30 |
| 40 | 正文 | 1:30 | 34:00 |
| 41 | 正文 | 1:15 | 35:15 |
| 42 | 正文 | 1:00 | 36:15 |
| 43 | 章节页 | 0:15 | 36:30 |
| 44 | 正文 | 0:45 | 37:15 |
| 45 | 正文 | 1:00 | 38:15 |
| 46 | 正文 | 1:00 | 39:15 |
| 47 | 正文·结尾 | 0:45 | 40:00 |

## 7. 本轮完成核对

已按1–47页通读，重点核对个人整机→Spark→128GB→模型能力→速度取舍，以及单机八卡→原Flash→1017两条决策链。原17页窗口档位研究安排已删除；相邻页面与后面的任务验证页同类长度计划也已清理，实际长度性能数据继续用于解释。

检查了各页末句、图表与标题，保留有用的连接和事实条件；正文没有脚注或防御性尾句。旧Flash仅出现在第三章初始选型的历史位置，第四章后的服务器主力为精确1017；单台设备范围保持。目录、页码、时间和本地来源链接已核对，旧稿保持原状。
