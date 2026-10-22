# 最终汇报三场景配置、容量与性能口径

**核对日期：2026年10月20日｜时区：Asia/Shanghai｜匿名研究稿。** 本文为最终PPT的配置与数字主表；价格冻结为10月12日研究基线。新价格、许可与采购状态由采购研究另行更新，三年TCO使用同一资源边界。本文没有下载权重、运行GPU实验或调用付费API。

结论是：个人采用**DGX Spark＋Qwen3.8-27B**，知识库比较同一套硬件上的**Onyx Enterprise与Milvus＋自建RAG＋Open WebUI**，公司共享Agent以**八卡H200运行DeepSeek-V4.1-Flash**为主要容量候选。131K／262K是基础窗口，512K／1M用于长Agent。Spark在长窗口下仍低于单人20+ token/s目标；八卡H200的20人1M属于有公开缓存池支持的容量方案，其满窗口速度采用明确的服务目标与反推需求。

[主数据与页码映射](data/final-configurations-2026-10-20/slide-data.json) · [机器可读摘要](data/final-configurations-2026-10-20/summary.json) · [复算与验证](data/final-configurations-2026-10-20/validation.json) · [本轮官方原文](../sources/TECH-089/original.md)

## 1. 成稿采用的配置与边界

| 场景 | 配置与分工 | 主稿的性能／容量口径 | 10/12基线预算／万元 |
|---|---|---|---:|
| 个人／三人小组 | 单DGX Spark GB10、128GB统一内存、4TB NVMe；Qwen3.8-27B-FP8；OpenCode与文件工具在员工电脑 | 外测分支为FP8权重＋FP8全注意力KV＋MTP3；完整精度KV保留独立分支；单人生成与三会话驻留分别说明 | 硬件5.8–6.2；个人硬件＋实施6.8–8.2；三人共享硬件＋实施7.8–9.9 |
| NAS权限知识库 | 四张6000D服务器版84GB；三张各运行一个Qwen27回答副本，一张做embedding／reranker；1TB主存；另两台应用／检索CPU节点 | FP8权重、BF16／FP16 KV、关闭MTP；20路8K短问答与131K／262K长会话分开 | 硬件74–141；Onyx首次84.5–158＋授权L；自建首次91.5–168.5 |
| 公司共享Agent | 八张H200 141GB SXM、NVSwitch、双EPYC 9454、1536GB主存；DeepSeek-V4.1-Flash；Hermes＋Skills／MCP；CPU工具执行隔离 | 主情景20个活跃请求；20×1M是容量候选；比较TP8、两独立TP4、同一服务TP4×DP2；A100采用modified vLLM | GPU整机291–304；集中工具CPU节点另加12–26；场景二已有NAS／检索不重复购买 |

金额均为D分析预算，含原表明确的税费、价格、交付与硬件支持准备，尚非本项目供应商报价。场景二为10/12继续采用的9/21–23估算；不把它标作10/20新成交价。企业授权、应用运维、电费、机房改造和专业软件另进入TCO。价格原始入口：[Spark](data/week7-deployment-2026-10-12/spark-price.json)、[知识库](data/scenario-2-rag-2026-09-23/assumptions.json)、[公司整机](data/hardware-prices-2026-10-12.json)。

### 统一的长度与证据图例

| 页面标签 | 总context／tokens | 输入历史预算 | 输出预留 |
|---|---:|---:|---:|
| 131K | 131,072 | 122,880 | 8,192 |
| 262K | 262,144 | 253,952 | 8,192 |
| 512K | 524,288 | 516,096 | 8,192 |
| 1M | 1,000,000 | 991,808 | 8,192 |

Context包括系统提示、工具定义、历史、工具结果、思考与本轮生成；输出预留从总长内扣除。8K短RAG另按**8,192输入＋600输出＝8,792总tokens**。外测的500,000输入＋2,048输出与主稿512K总窗口并非同一条请求；1M容量试验为999,936＋64。

图中固定四种身份：**实测**（外部设备或公开回放，保留负载与版本）、**经验计算**（用已有Spark数据拟合）、**条件计算**（显存／传输／工程效率假设）、**服务目标**（按目标速度反推需求）。前三者也不能替代业务质量验收。账号数、正在生成请求数和仍保留状态的会话数单独计量。

## 2. Spark：首次等待、单人生成与目标差距

### 2.1 外部设备取得的结果

| 精确输入＋输出 | 单请求decode／token/s | 冷TTFT | 身份 |
|---|---:|---:|---|
| 50,000＋2,048 | 21.01 | 63.1秒 | 两次稳定请求均值 |
| 100,000＋2,048 | 20.11 | 144.8秒 | 两次稳定请求均值 |
| 300,000＋2,048 | 17.23 | 658.9秒 | 一次稳定请求 |
| 500,000＋2,048 | 14.82 | 1,470.1秒 | 一次稳定请求 |
| 999,936＋64 | 9.83 | 4,815.8秒 | 1M容量完成附带的短输出速率 |

同一主机、FP8权重＋FP8 KV＋MTP3、FlashInfer、YaRN4、关闭前缀缓存、随机普通token输入。300K故障样本5.80来自draft长度仍停在262,144，修正到1,000,000后17.23；它不是正常关闭MTP的对照。模型revision、完整引擎版本与逐请求原始文件尚未取得，保留“用户提供的外部测量汇总”身份。[外部测试及方法](dgx-spark-qwen27-external-benchmark-2026-10-12.md) · [TECH-076](../sources/TECH-076/original.md)

### 2.2 主稿四档经验计算

| 总context | 单人decode | 冷prefill | 精确命中后追加1,024输入的prefill | 追加8,192输入的prefill | 生成8,192输出所需时间 |
|---|---:|---:|---:|---:|---:|
| 131K | 19.7 token/s | 188.5秒／3.1分钟 | 2.0秒 | 16.1秒 | 415.6秒 |
| 262K | 17.7 | 513.6秒／8.6分钟 | 3.0秒 | 24.1秒 | 463.3秒 |
| 512K | 14.7 | 1,547.6秒／25.8分钟 | 5.0秒 | 40.1秒 | 558.6秒 |
| 1M | 11.2，外推 | 4,731.5秒／78.9分钟，外推 | 8.7秒，外推 | 69.1秒，外推 | 731.5秒，外推 |

冷prefill沿用四个设备数据点的`aN+bN²`经验曲线；生成速率拟合100K／300K／500K的秒/token。512K档也略超500,000输入锚点；1M为较远外推。1M的64输出9.83单独画作容量样本，不能强制与长输出拟合11.2合为一个“实测速度”。[计算数据](data/final-configurations-2026-10-20/spark-windows.csv)

追加时间是`T(N)−T(N−Δ)`的条件估算，假设旧KV和线性注意力状态均可恢复，且有效执行效率不变。它不是实测热TTFT；排队、SSD／内存恢复、状态重放和第一步decode还需加入。前缀复用减少重复输入计算，持续生成仍要访问长历史。单人20+是体验目标，四档接近满窗口的拟合值均没有确认达到该目标；512K约15、1M约11应直接讲清。

## 3. Spark：三人驻留、同时生成和SSD

### 3.1 共享缓存池的份额

外测启动记录为模型与drafter28.47GiB、KV预分配池59.73GiB、共享token池1,806,907，最多8个活动序列。下面留10% token工作集余量；token余量不会释放已经分配的物理内存。

| 配置与会话 | 占用tokens | 占共享池 | 留10%后剩余tokens | 结论 |
|---|---:|---:|---:|---|
| FP8，三人各131K | 393,216 | 21.8% | 1,233,000 | 可驻留 |
| FP8，三人各262K | 786,432 | 43.5% | 839,784 | 可驻留 |
| FP8，三人各512K | 1,572,864 | 87.0% | 53,352 | 可驻留，增长空间小 |
| FP8，一人1M | 1,000,000 | 55.3% | 626,216 | 其余两人共享约626K，而非忽略余量后的约807K |
| BF16，三人各262K | 786,432 | 87.0% | 26,676 | 半池近似下可驻留 |
| BF16，一人512K | 524,288 | 58.0% | 288,820 | 半池近似下可驻留 |
| BF16，一人1M | 1,000,000 | 110.7% | −186,892 | 原池预算不足 |

BF16使用“FP8 token池减半、其他开销不变”的工程近似，尚非新启动实测。完整KV原始载荷65,536 B/token，FP8为32,768；1M BF16仅全注意力KV已65.536GB，超过59.73GiB池约64.134GB。开启前缀checkpoint、调整并发或MTP会改变池，正式准入采用重新加载后的日志。[份额图数据](data/final-configurations-2026-10-20/spark-sharing.csv)

### 3.2 三人同时生成的现有证据

| 每路精确输入＋输出 | 三路共同decode窗口总输出 | 共同窗口每路平均 | 每请求完整decode阶段平均 |
|---|---:|---:|---:|
| 50,000＋4,096 | 59.08 token/s | 19.69 token/s | 16.85 token/s |
| 100,000＋4,096 | 52.41 | 17.47 | 12.45 |

完整阶段包含其他请求prefill造成的干扰；共同窗口是三路都已开始且尚未结束的时段。三人各512K目前只有容量分析，不能把单人的14.7直接写成三人各14.7。运行上先采用一路交互优先、冷长prefill排队、空闲时准备批处理，再用混合负载核定调度参数。

CLI的131,072输入＋8,192输出总长139,264：4路／8路端到端总输出23.70／26.99 token/s，共同decode引擎窗口58.66／83.91。图中如果保留这些数据，应标明它们与131K总窗口不同。[精确输入与统计分母](data/final-configurations-2026-10-20/spark-measured.csv)

### 3.3 为什么Spark主要用SSD扩大闲置缓存

Spark的CPU与GPU共用128GB LPDDR5x，CPU缓存副本仍消耗同一物理内存。适用的分层是“统一内存中的活动状态→本地NVMe中的闲置状态”；员工电脑承担工具，减少统一内存竞争。只保存聊天记录保证内容可重建；保存与引擎兼容的KV及线性状态，才有机会减少重新prefill。

以**假设有效SSD读取6GB/s**算，512K FP8全注意力KV原始载荷17.180GB需2.86秒，1M的32.768GB需5.46秒。这些只算载荷读取，未计递归checkpoint、序列化、文件系统、重放与排队；Spark没有再额外增加一跳独立显卡PCIe拷贝。当前59.73GiB池来自关闭前缀缓存的外测，不能直接当作启用SSD缓存后的新池。[SSD与恢复算例](data/final-configurations-2026-10-20/restoration-budgets.csv)

## 4. 知识库：主稿只采用一套完整硬件

两条路线共用Qwen3.8-27B-FP8回答服务。A由Onyx Enterprise承担企业知识平台；B由Milvus、应用权限／RAG服务与Open WebUI组合。NAS仍是文件和有效权限来源：已验证身份决定检索范围，候选内容进入重排与模型之前做授权过滤，打开引用时再次核验。Onyx连接器能力与具体NAS适配分别验收。[原场景与交付分工](scenario-2-enterprise-rag-2026-09-23.md)

| 资源 | 数量与目标配置 | 预算归属 |
|---|---|---|
| GPU节点 | 4×RTX PRO 6000D服务器版84GB；双Xeon6710E各64核；1TB ECC主存；2×1.92TB系统＋2×3.84TB企业NVMe；双口25GbE、BMC、5×2400W电源与对应风冷／供电组件 | 原G3整机62–115万元 |
| 回答服务 | 三张卡各一个TP1 Qwen27副本；FP8混合权重31GB预算／卡；BF16／FP16 KV；关闭MTP与thinking；单卡缓存38.6GB | 已在GPU节点内 |
| 辅助模型 | 第四张GPU用于Qwen3-Embedding-0.6B、Qwen3-Reranker-0.6B及受限速入库；Onyx本地模型组合按其固定版本支持核验 | 已在GPU节点内 |
| 应用与检索 | 两台各16–32核x86、128GB ECC、2×3.84TB镜像NVMe、10／25GbE、冗余电源与基础支持 | 12–26万元 |
| 原文件／身份 | 复用NAS、身份目录与备份；索引／ACL增量同步 | NAS新增容量与完整HA另列 |
| 软件实施 | Onyx42–68人天；自建70–110人天；2,500元／人天 | 10.5–17／17.5–27.5万元，D工时 |

这里的电源是冗余配置能力，不是墙插功耗。GPU整机62–115与CPU12–26合计74–141；Onyx首次84.5–158＋L，自建91.5–168.5。L为私有化企业授权／支持的待报价变量，不用云订阅价或随意设定的年费替代。[完整G3硬件与预算](server-gpu-procurement-2026-09-21.md) · [原人工与费用输入](data/scenario-2-rag-2026-09-23/assumptions.json)

### 8K与长会话必须分成两行

每张回答卡按`84×90%−31−6＝38.6GB`缓存；三副本各有独立池，不能跨卡直接合并。单会话预算为`(context×65,536＋153,944,064)×1.15 bytes`，包括完整精度全注意力KV、递归／卷积状态和15%页准备。

| 负载 | 每会话预算 | 三副本同时准入 | 20份会话预算 | 主稿用途 |
|---|---:|---:|---:|---|
| 8,192输入＋600输出 | 0.840GB | 20路能放入；配置批次上限另约束 | 16.79GB | 日常RAG短问答性能情景 |
| 131,072总context，含8K输出 | 10.055GB | 3份／卡，合计**9份** | 201.11GB | 长会话容量与队列 |
| 262,144总context，含8K输出 | 19.934GB | 1份／卡，合计**3份** | 398.68GB | 长会话容量与队列 |

[容量计算](data/final-configurations-2026-10-20/rag-capacity.csv)。不计15%准备会得到12／6份的不同速算；它不是本主稿口径。20路长会话需要换出／恢复、排队或扩容，不能继承20路8K速度。

20路同时到达、8,192输入＋600输出、模型已加载、冷缓存的原工程模型：基准每路21.5–22.0 token/s，最后一路TTFT37.4秒，整批65.3秒，端到端总输出183.8 token/s。低／高效率条件对应整批100.8／47.6秒、119.1／252.1总输出。三条均为**假设效率下的条件计算**，不是GPU测量或Onyx／Milvus之间的性能排名。[性能与效率身份](data/final-configurations-2026-10-20/rag-performance.csv)

## 5. 公司：20活跃请求与20×1M的容量候选

### 5.1 权重、Engram、KV分别计量

| 项目 | 统一数值与来源 | 不能直接推出什么 |
|---|---|---|
| 原生checkpoint tensor总量 | **510,286,023,000 B＝510.286GB** | 不是同样大小的GPU常驻内存 |
| 两张Engram host表 | **202,758,032,400 B＝202.758GB＝188.833GiB** | 不是用户KV；不会随会话长度线性增加 |
| 非Engram tensor总量 | **307,527,990,600 B＝307.528GB** | 不能忽略rank复制、反量化、草稿与workspace后简单除卡数 |
| Hopper global KV | **1,827 B/token/TP rank**；1M为1.827GB／rank | 不能再除TP；不能拿论文890 B/token替代 |
| 20×1M global KV | **36.54GB／rank**；TP8全rank292.32GB | 未含SWA、草稿、scratch、allocator与图内存 |

Engram表计算为`(384006168＋384016682)×(256＋8)`。模型原生为FP8 dense＋FP4 experts、BF16 embedding/head及scale的混合格式；模型名／单个量化标签不能把全模型概括成纯FP8。[官方制品与固定config](../sources/TECH-079/original.md)

Hopper的main584B与index132B，按压缩比2／2／2／1和block64、576B页对齐，合计116,928B／64＝1,827。vLLM **v0.32.0固定attention.py与TECH-080已审源码逐字节相同**，该布局解释仍有效。0.32一般NVFP4 KV能力扩展不能据此将DeepSeek V4.1 Hopper改算成SM100的记录；其`nvfp4_ds_mla`路径仍要求相应架构。静态格式用于解释，准入仍采用具体启动池。[0.32固定源码](../sources/TECH-089/vllm-0.32-attention.py) · [原逐页推导](scenario-3-company-agent-2026-09-23.md)

### 5.2 主稿统一采用post-graph严格预算敏感性

公开日志的已分配池是实测记录；图捕获后建议的较小KV池用于满足0.92内存预算。本表把原token池按建议GiB比例缩放，再保留10% tokens；这是**重新启动前的线性预算敏感性**，还不是新一轮加载测量。

| 部署 | 已分配→严格建议KV／GiB每GPU | 严格token池／实例 | 20份历史各自可用context，上限取1M | 20×131K／262K／512K／1M |
|---|---:|---:|---:|---|
| 8H100 TP8 | 12.36→10.34 | 5.383M | **242,240** | 可／不足／不足／不足 |
| 4H200 TP4 | 35.16→32.49 | 16.935M | **762,048** | 可／可／可／不足 |
| 8H200 TP8 | 62.86→60.20 | 28.250M | **1,000,000** | 可／可／可／可 |
| 8H200双TP4 | 35.16→32.49，每卡 | 两池，各16.935M | **1,000,000**，每组10份 | 可／可／可／可 |

八H200两种布局都覆盖20×1M。双TP4本表固定采用C32 profile，避免把C16更大的池与C32图预算混搭。已分配H100池可算289,536，但严格预算只242,240，最终主表统一用后者。公开池镜像为`nightly-cd10ed6f9f6b37a8ace9cf380007e66fe12ec0c3`，含Engram CPU offload、FP8 MLA/index与DSpark5；其容量与速度不会自动变成0.32升级后的结果。[公开API与日志](../sources/TECH-084/original.md) · [32行主容量表](data/final-configurations-2026-10-20/company-capacity.csv)

若20项正在生成，另20项等待工具，则按40份独立历史计。严格预算下，TP8约**635,584总tokens／份**，双TP4约**762,048／份**；两者均不能把40×1M全部留在GPU。两独立副本与DP2在这里都保留两个KV池，Engram共享不会合并会话池。

### 5.3 同一八卡机器的三种软件布置

| 布置 | GPU权重与KV | Engram主机表 | 使用含义 |
|---|---|---:|---|
| 单TP8 | 一套模型，八rank各自缓存 | 一份202.758GB | 一个队列，单次长prefill使用八卡 |
| 两个独立TP4服务 | 两套GPU模型，各四rank与独立队列 | 默认两份405.516GB | 按用户／项目粘性路由，各组隔离排队 |
| 同一vLLM服务，TP4×DP2，满足共享条件 | 仍为两个GPU副本与两个KV池 | **每节点一份202.758GB** | v0.31起可同机共享Engram host表，保留DP负载均衡 |

`dp_shared_memory`要求CPU offload、DP>1、同节点、共享IPC及足够的`/dev/shm`；容量不足、非同机或不支持的elastic EP会回退／拒绝相应路径，需读启动日志确认。不能把两条独立`vllm serve`命令自动算成DP共享。`embedding_across_dp`则是另一种跨TP×DP分片并交换查表结果的方案；它带每步DP通信，区别于共享host页后各副本只预取自身tokens。[v0.31官方Engram文档](https://github.com/vllm-project/vllm/blob/v0.31.0/docs/features/engram.md) · [v0.32配置源码](../sources/TECH-089/vllm-0.32-engram-config.py)

主存规划可将现有1536GB名义配置分为Engram、**640GiB总CPU缓存候选额度**、256GB系统／加载／元数据准备及剩余余量。TP8／共享DP2尚余约390GB，独立双TP4约187GB。这是分析分区，实际加载峰值、页锁定、NUMA与完整缓存格式要重新验证；不把GPU节点的主存再计成工具服务器采购。[主存分区数据](data/final-configurations-2026-10-20/host-budget.csv)

## 6. 公司：已有速度参照与可执行的1M目标

### 6.1 公开回放保留原负载身份

| 公开配置／活动会话 | 平均输入 | 前缀命中率 | 端到端系统输出 | 平均／p95 TTFT |
|---|---:|---:|---:|---:|
| H100 TP8／20 | 140,896 | 93.8% | 718.48 token/s | 2.05／6.98秒 |
| H200 TP4／16 | 138,189 | 95.1% | 614.76 | 0.83／3.03秒 |
| H200 TP4／32 | 149,855 | 95.2% | 922.61 | 1.47／5.12秒 |
| H200 TP8／16 | 146,517 | 95.5% | 661.15 | 0.65／2.14秒 |
| H200 TP8／32 | 156,951 | 95.7% | 1,052.18 | 0.85／2.63秒 |

这些是AgentX多轮回放、合成DSpark平均接受长度3.51，活动会话不等于所有会话每时刻共同decode。H200 TP4/C32的35,314.95 total token/s/GPU大部分是输入，输出230.65×4＝922.61才是系统端到端输出。不能把总token、缓存读取或每请求交互速率中位数当成20路1M共同decode。[五条可引用记录](data/final-configurations-2026-10-20/company-replay.csv) · [TECH-084原API](../sources/TECH-084/benchmarks.json)

### 6.2 未测满1M时，主稿仍可给出的数字

| 20路、每路8,192输出 | 每路10 token/s目标 | 每路20 token/s目标 |
|---|---:|---:|
| 要求系统持续decode输出 | **200 token/s** | **400 token/s** |
| 纯生成时间／每轮 | **819.2秒／13.65分钟** | **409.6秒／6.83分钟** |
| 纯decode全忙时的调用量上限 | 87.9次／小时 | 175.8次／小时 |

表中调用不是完成的业务任务；它排除了prefill、恢复、工具、排队、失败与人工复核，TCO不能直接把它当作合格任务产量。512K与1M可共用同一目标，但分别测试真实接受率和延迟。

20路各1M、预留8K输出，首次需要处理**19,836,160输入tokens**。若要求整批纯输入处理在5／15／30分钟完成，对应至少**66,120.5／22,040.2／11,020.1 fresh input token/s**。这是反推的性能门槛，未预测设备已经达到；高缓存命中回放的input吞吐不能填进这张表。[四档×四人数×两目标数据](data/final-configurations-2026-10-20/company-targets.csv)

新增1K后p95热TTFT可先比较5／10秒两档，另测追加8K。验收同一8H200整机的TP8与双TP4／DP2：20×512K、20×1M、真实DSpark；记录共同decode200／400目标、逐请求分布、热TTFT、冷1M插入的干扰和工具等待逐出恢复。容量候选因而有明确的速度、首次等待与任务质量门槛。

## 7. KV offload：保存完整可恢复状态

GPU保存正在使用的状态，CPU DRAM保存近期会继续的会话，NVMe延长保留时间。工具返回时恢复兼容状态，再处理新增输入；连续decode仍以活动状态在GPU上的执行为主要路径。聊天日志、Engram表、模型权重和会话缓存是四种不同对象。

| 模型 | 需要恢复／重建的状态 | 本轮支持核对 |
|---|---|---|
| Qwen27混合注意力 | 全注意力KV＋GDN递归与卷积状态；匹配位置与前缀checkpoint；开启MTP时核draft状态和长度 | LMCache列Qwen3.8-27B单GPU文本验证；`align`＋prefix caching＋object-group分离；文档示例统一块784，但FP8 KV／MTP3需读实际启动块尺寸 |
| DeepSeek V4.1 | 多组compressed global KV与index、SWA、必要draft状态；compressor scratch ring按指定路径重算；bounded replay按所选引擎重建有限窗口 | LMCache列八GPU文本验证，按多组geometry存取，跳过非prefix-cacheable scratch；**MTP尚未验证** |

[Qwen当前recipe](https://docs.lmcache.ai/recipes/qwen3_5.html)列的是`Qwen/Qwen3.8-27B`，不能扩大为“FP8制品＋FP8 KV＋MTP3＋GB10＋SSD均已验证”。`align`仍属实验性；外部Spark关闭prefix cache的速度和token池不等于开启状态checkpoint后的配置。`max-num-batched-tokens`取决于实际块N：在[N,2N)较细粒度保留checkpoint，recipe建议2N−1以给decode留共调度空间；直接设N会把混合工作串行化。FP8或MTP会改变布局，784不可生搬。

[DeepSeek当前recipe](https://docs.lmcache.ai/recipes/deepseek_v41_flash.html)使用`fp8_ds_mla`，有各组块尺寸与scratch重算说明。缓存必须匹配模型revision、token前缀、位置规则、KV精度、attention后端、GPU架构、块几何及可访问范围。Hopper／SM100的packed记录不同，不能跨格式直接复用；CacheBlend／CacheGen不适用于这些opaque缓存页。分组存取支持与完整MTP组合完成验证分别判断。[原文与固定LMCache源码](../sources/TECH-089/original.md)

**两条实现路线。** vLLM原生OffloadingConnector将完成的块异步复制到CPU，TieringOffloadingSpec再接文件系统／对象存储；NVMe路径经CPU中转。`cpu_bytes_to_use`为所有worker合计，CPU缓存过小可能只是镜像GPU块。LMCache MP是独立缓存服务，适合管理兼容多实例的共享缓存与次级存储。主稿可介绍两条路线；选定模型、精度与MTP组合仍需验证缓存恢复和任务得分。[vLLM官方指南](https://docs.vllm.ai/en/stable/features/kv_offloading_usage/) · [LMCache多层存储](https://docs.lmcache.ai/mp/l2_storage.html)

### 传输预算与实际等待分开

以1M Hopper global载荷、rank复制、假设四／八卡**合计有效24GB/s**计算：

| 恢复对象 | 传输载荷 | CPU→GPU纯载荷时间 | SSD6GB/s→CPU→GPU串行载荷时间 |
|---|---:|---:|---:|
| 一个TP4会话 | 7.308GB | 0.305秒 | 1.523秒 |
| 一个TP8会话 | 14.616GB | 0.609秒 | 3.045秒 |
| 20个TP4会话同时恢复 | 146.160GB | 6.090秒 | 30.450秒 |
| 20个TP8会话同时恢复 | 292.320GB | 12.180秒 | 60.900秒 |

这些数字只有条件计算身份，未把PCIe／SSD规格当实测；实际还包括其他状态、拷贝调度、NUMA、有限重放、新增prefill和第一步decode。具体引擎若能存一份再广播，载荷账会改变；本表未擅自假定该优化。[12／24／48GB/s敏感性](data/final-configurations-2026-10-20/restoration-budgets.csv)

## 8. 框架版本、A100和CPU工具池

截至10/20，vLLM最新正式版为**v0.32.0，10/18发布**；V4.1从0.30进入正式release，0.31增加同机DP共享Engram，0.32继续完善bounded replay等路径。LMCache V4.1 recipe中的“无任何tagged release”提示已陈旧；其“MTP尚未验证”仍需保留。建议把0.32作为新增验证候选，并冻结镜像digest、驱动／CUDA、模型revision与完整参数；旧AgentX数据保持旧镜像身份。[0.30](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) · [0.31](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) · [0.32](https://github.com/vllm-project/vllm/releases/tag/v0.32.0)

0.32把`max_tokens`视为输出上限而不自动预留context，且移除了`mamba_cache_mode=all`。本项目的8,192输出预算必须在Harness／网关明确实施，模型窗口、草稿窗口与自动压缩阈值同步；不能仅设置输出参数就假定完整窗口始终有8K空间。Qwen的`align`路径与旧变量名按固定版本检查。

**A100公司服务仍采用modified vLLM。** 510.286GB原生制品与Engram offload能力来自模型和通用引擎，项目增量是SM80算子与调度／通信适配。八A100 SXM翻新整机91–102万元是采购基线；shi3z主要四卡PCIe、以及modified vLLM的A100／A800短输入记录，各自保留机器与负载。不能从四卡结果直接倍增为八卡20×1M速度。A100的满窗口池与性能按固定SM80补丁版验证。[A100专项与公开消融](deepseek-a100-project-review-2026-10-12.md) · [TECH-088](../sources/TECH-088/original.md)

工具CPU、环境内存与KV分别计量。每10秒到达一项任务、三轮、每轮模型60秒＋工具墙钟10秒、工具实际4核秒、每环境2GiB且全程保留的教学例：平均21项未完成、18项在模型阶段、工具CPU平均1.2核、环境内存42GiB。模型阶段增至120秒，CPU仍1.2核，环境增至78GiB；到达率翻倍则CPU2.4核、环境84GiB。两台各16–32核／128GB工具节点是既有预算候选，用实测突发与Office／浏览器／OCR峰值确定配额，不能把平均1.2核解释成只采购两核。[六组工具池数据](data/final-configurations-2026-10-20/tool-cpu.csv)

场景二的应用／检索CPU节点与场景三工具执行节点职责不同，默认分别列预算；若计划合并，先核身份、索引写入、工具沙箱与峰值资源。员工电脑执行工具的分支可以复用现有终端，GPU节点已含CPU与主存，不另重复买一遍。

## 9. PPT数据放置与旧资料刷新

| 页面 | 可直接取用的数据 | 需要说清的接续 |
|---|---|---|
| P10–11 | `spark-measured.csv`、`spark-windows.csv` | 首次读材料慢，因此下一页讲保留已有计算 |
| P12–14 | `spark-sharing.csv`、`restoration-budgets.csv`、三路共同窗口 | 统一内存决定SSD扩展；缓存份额与多人计算竞争分开 |
| P15 | `summary.json/scenario1` | 同一硬件配不同实施范围，进入企业资料权限 |
| P18 | `rag-capacity.csv`、`rag-performance.csv`、`summary.json/scenario2` | 用8K问答控制检索输入，长会话按9／3份准入 |
| P20–21 | 原生制品表、`company-capacity.csv` | 权重与Engram固定占用后，再看各rank可保留历史 |
| P22 | `host-budget.csv`、`restoration-budgets.csv` | 等工具仍保存状态，因此引入DRAM／SSD与恢复时间 |
| P23 | `company-replay.csv`、`company-targets.csv` | 先讲已有回放，再给20路满窗口的目标和验证办法 |
| P24–26 | `tool-cpu.csv`、整机预算、A100引擎选择 | GPU与CPU分别核算，随后进入同资源边界TCO |

可交主agent刷新的旧资料清单：

1. **当前三份scenario与reference-architecture：**新增本文冻结配置入口；公司“nightly/preview才支持”更新为正式版本状态；双TP4两份Engram只用于独立服务分支，增加同机DP2共享分支。原9月／10月测试快照与机器标签保留。
2. **scenario2摘要与主表：**固定本稿G3完整BOM＋两CPU节点；只用Qwen27 FP8＋完整精度KV。新增131K九份／262K三份的容量，删除主稿35B／4bit混用；8K速度保留原条件计算身份。
3. **当前讲稿Spark三人页：**默认保留10%token余量后，一人1M留给其余两人约626K；600K／807K属于未扣余量的算术，不能混到准入表。三人512K只确认容量分析，不借用单人速度。
4. **当前讲稿公司容量页与40份状态：**统一post-graph敏感性＋10%token余量；固定C32对照下TP8约636K、双TP4约762K／份。若保留旧664K／876K，必须单列其已分配池／不同profile身份。
5. **缓存续跑与版本页：**SSD聊天记录和引擎兼容状态分开；补全GDN／SWA／index／scratch重建；Qwen FP8 KV＋MTP3与DeepSeek DSpark＋LMCache不能以架构支持代替组合验证。0.32输出预留由应用明确执行。
6. **TCO与采购页：**同一8H200预算用于TP8与双TP4；Engram共享只改变内存分配，不产生另一份机器采购节省。291–304万为10/12整机；CPU工具12–26万与知识库CPU是否新增分别计量。20×1M调用量使用服务目标推导，合格任务产量由真实任务评价决定。

本文未修改全局source-register／reading-index／README，也未修改三份scenario；由整合者更新索引和现行入口。所有公式由[recalculate.py](data/final-configurations-2026-10-20/recalculate.py)本地复算，结果含输入SHA-256及17项语义／算术检查；这确认计算一致性，不宣称完成GPU正确性或业务质量验证。
