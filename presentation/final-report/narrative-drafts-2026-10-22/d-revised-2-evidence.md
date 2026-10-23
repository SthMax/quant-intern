# D第二轮修订：证据、版本、测算与时间

正文：[extended-draft-d-revised-2.md](extended-draft-d-revised-2.md)。先行工作稿：[d-chapters-4-5-reorganization.md](d-chapters-4-5-reorganization.md)。逐项落实说明：[d-revised-2-response-for-user.md](d-revised-2-response-for-user.md)。

本轮核验日期：**2026-10-23**。正文46页，其中正文38页，封面1页、目录1页、章节页6页；讲述预算40分钟。服务器主力版本固定为 **DeepSeek-V4.1-Flash-1017**，公司方案是一台八H200服务器，工具在同机隔离环境运行，个人方案为一台Spark。既有NAS、身份及员工终端按复用资源安排。

## 1. 1017版本核验

实际打开[1017官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)和[10月17日官方发布](https://api-docs.deepseek.com/news/news261017/)。模型卡明确列出1M上下文、MIT许可、1017制品及本地运行入口。本轮进一步通过官方API读取并固定该仓库修订：

`1bae0e1088993b9b82de08f59de5be5a34e42170`

| 官方文件 | 本轮直接读取结果 | 正文用途 |
| --- | --- | --- |
| [config.json](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/blob/1bae0e1088993b9b82de08f59de5be5a34e42170/config.json) | 3311字节；SHA256 `8be45ce0476004a3f529fd896115a4a2e800a129ad2d3ec05b16050f52e21879` | 架构、历史共享、Engram形状、量化与草稿配置 |
| [model.safetensors.index.json](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/blob/1bae0e1088993b9b82de08f59de5be5a34e42170/model.safetensors.index.json) | 7,470,294字节；SHA256 `74b0686a3d2891980d5e303251b075a3bccae2c2ff650747db2620a649b98fa8`；metadata.total_size＝510,286,023,000 B | 第33页约510GB发布制品 |
| [inference/README.md](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/blob/1bae0e1088993b9b82de08f59de5be5a34e42170/inference/README.md) | SHA256 `2834402823199ee24e9a42bdf36a0fc6daf94448f444cb062c042a057a798f1c` | 参考实现的压缩稀疏注意力、Engram及分卡运行入口 |
| [inference/model.py](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/blob/1bae0e1088993b9b82de08f59de5be5a34e42170/inference/model.py) | 实际读取Engram、ParallelEngramEmbedding、历史共享与索引相关代码 | 表按行查找、FP8表与scale、共享历史的解释 |

第33页的编码器／解码器组织，采用1017模型卡直接链接的[官方技术报告](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf)，并结合本次1017固定配置。Engram表的静态载荷为两表行数`384006168＋384016682`，每行256个FP8值及8个尺度字节，合计202,758,032,400 B，正文取约203GB。它描述发布制品中的表与尺度，GPU运行时还由实际后端组织。

本轮采用的服务器数字分为两类：1017官方制品的静态事实，以及明确设定的单机服务目标。正文的20路、每路20 token/s、系统400 token/s是服务目标；公司成本中的输入处理与生成能力也是预算假设。服务器质量与资源的历史测量身份已经从当前方案中清理，正文的设备性能实测保留Qwen27／Spark本来对应的身份。

## 2. GDPval-AA与选型

2026-10-23重新打开[GDPval-AA v2.1榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)，并使用defuddle读取。方法仍采用[AA官方说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking)：220项专业任务、44职业、9行业，Stirrup工具环境提交文件，同题匿名比较，汇总Elo。第20页的舞台布置PDF示例来自用户指定的[任务示例入口](https://artificialanalysis.ai/evaluations/gdpval-aa#example-tasks)。

| 第21页模型／作者标签 | GDPval-AA v2.1 Elo | 本轮读取的直接页面 |
| --- | ---: | --- |
| DeepSeek-V4.1-Flash-1017／Max | 1746 | [1017／Qwen](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-1017-vs-qwen3-8-27b)，与榜单一致 |
| GLM-5.3-Flash | 1642 | [GLM／Kimi](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-kimi-k3) |
| MiMo-V2.6-Flash | 1607 | [MiMo／Qwen](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-qwen3-8-27b) |
| Kimi K3／Max | 1533 | [GLM／Kimi](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-kimi-k3) |
| Qwen3.8-27B／Xhigh | 1417 | [1017／Qwen](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-1017-vs-qwen3-8-27b) |
| Gemma 4 31B／Reasoning | 620 | [Qwen／Gemma](https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-gemma-4-31b) |

正文的横向结论限定在日期、GDPval-AA和展示的开放权重模型组内，1017位于首位。服务器选型按用户本轮确定的1017执行；其他模型在表中承担比较参照，后续部署路线只围绕1017展开。Qwen个人路线保持。

## 3. 第四章的性能与机制材料

- **第22、27、29、32页：**[TECH-076用户提供的外部测量汇总](../../../knowledge-base/sources/TECH-076/original.md)。单Spark GB10、Qwen3.8-27B-FP8、FP8 KV、MTP3、FlashInfer、前缀缓存关闭，随机token负载。50K／100K各两次、300K／500K各一次，输出2048。TTFT为63.1／144.8／658.9／1470.1秒；decode为21.01／20.11／17.23／14.82 token/s。三路各4096输出的共同窗口与完整阶段数值沿用同份总结。原始环境及逐请求文件的取得状态保持原记录。
- **第25–32页：**[AI Infra第3章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/03-推理与训练负载.md)、[第8章](../../../knowledge-base/sources/TECH-078/upstream/manuscripts/08-推理优化.md)，固定修订`3bdcb4fcab73010eeaccf31cc10a8242a895d82e`。使用请求生命周期、prefill／decode、前缀复用、状态恢复与调度机制；第28页409.6秒＝8192÷20。前缀恢复表是运行设计解释。
- **第33页：**本文件第1节的1017官方材料。结构图将Engram指向模型计算，历史共享单独展示。
- **第34页：**[vLLM官方功能归档](../../../knowledge-base/sources/TECH-020/original.md)、[SGLang官方归档](../../../knowledge-base/sources/TECH-021/original.md)及1017模型卡的服务入口。vLLM作为所选服务框架；验证固定模型SHA、引擎、驱动与参数。SGLang是框架职责对照。
- **第35页：**本轮单机服务组织：八H200共同计算一套模型，CPU、主存、SSD及工具环境位于同一服务器。20×20＝400 token/s为目标反推。

## 4. 单机预算的重新计算

### 使用量与任务

个人第一年750项，后两年825／907.5项，三年2482.5项。公司中等使用量25,000／31,250／39,062.5项，三年95,312.5项；较低使用量每年10,000项，三年30,000项。正文采用约数。

每项任务安排8轮，首轮输入100K，此后新增外部资料8K／轮，前轮输出2K进入历史。本轮输入依次100K至170K，累计1.08M；输出共16K；额外轨迹10%。本地可复用前缀命中按90%、API按95%预算。公司年度服务窗口2000小时，保留30%时间用于波动与维护；输入处理8000未缓存tokens/s、输出400 tokens/s是成本规划参数，模型调用的机时预算为78.155秒／项。正文用计划任务量讨论投入。

### 硬件与采购口径

[10月12日硬件台账](../../../knowledge-base/infrastructure/data/hardware-prices-2026-10-12.json)中的一台八H200服务器：双EPYC9454、1536GB主存、8×H200141GB、NVSwitch与SSD等；分析预算2,912,121.64–3,035,171.64元，正文约291–304万元，中值2,973,646.64元。它基于[Exxact原配置](https://configurator.exxactcorp.com/configure/TS4-118380266)及原研究明确的交付、税费与支持准备。对应[归档](../../../knowledge-base/sources/TECH-087/h200-config.md)。Spark按[同日价格输入](../../../knowledge-base/infrastructure/data/week7-deployment-2026-10-12/spark-price.json)，中值60,123.50元。价格是硬件预算，与模型服务版本分开记录。

### 本轮资源范围

公司模型、会话及工具运行放在同一台八H200服务器。既有应用资源、NAS、身份与员工终端作为复用条件。本轮将原TCO中的外置工具CPU购置180,000元及其三年电费8,830.08元从两条公司路线删除；GPU服务器自带CPU和主存已包含在整机预算内。个人路线保持一台Spark与员工终端。

### 三年中等工作量预算，人民币元

| 项目 | 个人本地 | 公司单台八H200 | 公司API |
| --- | ---: | ---: | ---: |
| 推理硬件 | 60,123.50 | 2,973,646.64 | 0 |
| 机房初次接入 | 0 | 30,000.00 | 0 |
| 实施 | 15,000.00 | 112,500.00 | 75,000.00 |
| 三年技术运维 | 15,000.00 | 450,000.00 | 300,000.00 |
| GPU／个人设备设施电费 | 342.14 | 56,433.22 | 0 |
| 三年机位 | 0 | 54,000.00 | 0 |
| 软件／平台支持 | 0 | 60,000.00 | 60,000.00 |
| API模型调用 | 0 | 0 | 59,601.24 |
| **合计** | **90,465.64** | **3,736,579.86** | **494,601.24** |

计算保留原输入精度后汇总。正文第39页四类公司费用为300.364664、11.25、45、17.043321809万元，总额373.657985809万元；个人为6.01235、1.5、1.5、0.034214365万元，总额9.046564365万元。表格以两位小数约数显示，合计从未舍入数计算。

公司较低使用量：原本地低量预算3,916,993.187333元减188,830.08元＝**3,728,163.107333元**，每项计划任务124.2721元；公司中等使用量每项3,736,579.85809÷95,312.5＝**39.2035元**。正文第41页两行均为同一台服务器，费用变化来自工作量对应的运行电费。

个人API保持原三年**16,552.36794元**；公司API＝75,000＋300,000＋60,000＋59,601.236396625＝**494,601.236396625元**。

来源：[TCO输入](../../../knowledge-base/infrastructure/data/tco-2026-10-20/inputs.json)、[三年分项](../../../knowledge-base/infrastructure/data/tco-2026-10-20/presentation-bars.csv)、[总表](../../../knowledge-base/infrastructure/data/tco-2026-10-20/summary.csv)、[原测算研究](../../../knowledge-base/infrastructure/tco-analysis-2026-10-20.md)。本轮读取数据并按当前单机资源范围独立相减、加总和计算单位任务额，原研究文件保持只读。

### API价格与运行参数

2026-10-23实际打开[DeepSeek官方价格](https://api-docs.deepseek.com/quick_start/pricing/)，当前`deepseek-flash`对应1017。低峰每百万token：未缓存输入0.15 USD，命中输入0.003 USD，输出0.60 USD；高峰分别0.30／0.006／1.20。预算80%高峰、汇率7.00，API调用费另预留6%税费，三年保持费率；一项含额外轨迹的调用费用0.62532444744元。供应商联网工具费为0，预算任务以本地文件、代码和工具工作为主。

电费沿原分析参数：Spark运行／空闲0.20／0.04kW，年通电2000h，设施倍率1.10；H200运行／空闲6.80／1.50kW，年通电8760h，PUE1.40，电价0.80元/kWh。忙碌时间按上述规划工作负载计算；同机工具和模型纳入整机功率预算。真实任务、功耗和复核记录在实际部署阶段更新。

## 5. 其他页面的来源

- 第5页：[MENTOR原论文](../../../knowledge-base/sources/FUND-113/original.md)pp.1–2、[盈米固定客户端](https://github.com/yingmi-dev/content-compliance-skill/blob/040df66202f6075cdeadb450e502c7a19c83dabf/README.md)、[易方达开发测试案例](../../../knowledge-base/sources/FUND-101/original.md)PDF p.4。
- 第19页Qwen窗口：[官方模型卡归档](../../../knowledge-base/sources/TECH-092/models/qwen27/README.md)。262144−8192＝253952。
- 第43–44页：[Hermes执行与入口文档](../../../knowledge-base/sources/TECH-072/open-webui.md)、[资料权限文档](../../../knowledge-base/sources/TECH-068/onyx-permissions.md)、[知识库研究](../../../knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md)。本轮图示按单台服务器安排，平台功能作为接入研究。
- 第45–46页：从正文选型与服务安排推导的任务验证与总结，任务评价以产物、时延与人工复核为对象。

## 6. 页码与时间

目录与章节页对应：3–7、8–15、16–23、24–35、36–41、42–46。保留46页、正文38页；正文共37:45，封面与目录0:45，章节页共1:30，合计40:00。

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

## 7. 完成核对

已从头通读正文，并单独连续阅读24–41页，检查每页承接的认识、当前解释和进入下一页的理由。核对标题、图、表与末句；目录区间、精确模型版本、单台设备范围与时间加总一致。正文采用直接事实、运行条件与结果，未添加脚注式辩解。原稿、指南和知识库均保留。
