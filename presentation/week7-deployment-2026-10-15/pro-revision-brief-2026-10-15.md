# 第七周演示稿补充说明

**交给Pro的修改任务｜2026年10月15日**

请在现有Pro版演示稿上修改，保留其视觉风格、四部分结构和讲者备注。本次主要补齐六处信息，并增加两页关于分层KV缓存的介绍。本文给出了可用于slide的文案、算例和原始链接，可以独立作为修改依据。

基稿为`week7-long-context-redesign.pptx`及同名PDF，现有**25页正文、7页附录，共32页**。下文页码全部指修改前的32页版本；插入新页后，请同步更新页码、交叉引用和讲者备注。基稿位置：[PPTX](output/gpt-pro/week7-long-context-redesign.pptx)、[PDF](output/gpt-pro/week7-long-context-redesign.pdf)。

## 一 修改目标和讲述方式

听众是mentor和组员。介绍重点是方案如何运行、需要什么资源、用户获得什么，以及预算多少。研究结论保持：个人采用DGX Spark和暂定Qwen3.8-27B；公司采用暂定DeepSeek-V4.1-Flash，以八卡H200为主要候选；公司若采用A100，使用固定版本的modified vLLM。

正文用完整、直接的中文解释技术。使用“上下文”“缓存命中”“把缓存从CPU内存复制回GPU”等具体说法。性能数字在表头或旁注标明“实测”“估算”及负载；必要条件写在对应数字旁，不在每段末尾重复“不能代表”“尚未证明”等提醒。技术细节放附录和讲者备注。

新增缓存内容的中心结论是：**GPU优先服务正在运行的任务，CPU内存和SSD保存暂时不用的会话状态；下一轮取回已有缓存，可以减少重复prefill。** 公司服务器和Spark的内存结构不同，应分别说明。

本文的缓存指KV及继续推理所需的其他模型状态。若“request caching”指保存并直接返回完整答案，那属于另一层应用缓存；这里的Agent仍会处理每轮新增的工具结果，并生成新的回答。

## 二 现有页面需要补充的信息

| 原页码 | 修改内容 | 放置方式 |
|---|---|---|
| **7** | 右侧17.5／12.5 token/s对应**三路、每路100K输入**。目前条件只在脚注，容易与左侧600K／1M容量图连在一起理解。 | 将速度框标题改为“三路实测，每路输入100K”；保留两种计时窗口。 |
| **14和29** | 补上完整服务器报价对应的CPU、主机内存和互联。 | 第14页保留价格图；第29页增加紧凑配置表，见下文。 |
| **15** | 补回作者宣传的“33→673 token/s，超过官方API”，交代研究这个项目的缘起。 | 在项目介绍中加一行背景；讲者备注解释这是作者自身实现的迭代宣传。 |
| **18** | 明确消融实验属于**Tokha233的modified vLLM，8×A800**。 | 标题或副标题直接写明归属，避免将约4.5%的增量算到shi3z项目上。 |
| **26** | 补Spark长上下文启动配置，尤其是YaRN和MTP草稿上限。 | 表格旁补一行配置；详细参数放讲者备注。 |
| **32** | 将原始链接放进PDF可见页面。当前链接只在PPT讲者备注中。 | 末页保留4至6个核心链接，更多链接放技术附录或备注；检查PDF导出后的链接可点击。 |

### A100案例的背景和实验归属

第15页可以加入：

> 作者以“A100从33提升到673 token/s，超过官方API”为标题，记录自研引擎的优化过程。最初目标是批量生成，后来转向Coding Agent的长输入和多轮缓存。

讲者备注保留一次必要说明：该headline描述作者自身实现的演进；我们已有材料没有给出673对应的完整测试条件，因此性能对照继续采用第17页已经列明硬件和负载的数据。

来源：[shi3z 9月12日文章公开部分](https://note.com/shi3zblog/n/nd5fc5341b342)、[9月17日续文公开部分](https://note.com/shi3zblog/n/n93b0161463b4)、[本次阅读的固定源码](https://github.com/shi3z/deepseekv4.1-A100-custom/tree/580568edd6f84537ff042ded4ee842b892bf3ff4)。付费续文未作为已读取材料使用。

第18页建议标题：**modified vLLM同机消融 每项改动带来多少收益**。

副标题：**Tokha233，8×A800，128并发；实际输入78–90 token、输出1,024 token，每档两次。**

| 配置 | 两次平均总输出 token/s | 相对上一档 |
|---|---:|---:|
| Marlin dense＋NCCL EP8基线 | 2,842.48 | — |
| 大batch稠密层改走BF16算子 | 2,926.08 | +2.94% |
| 再加入定制EP8通信 | 2,970.50 | +1.52% |

两项合计约4.5%。这里的BF16指部分稠密层的执行算子，官方原生checkpoint仍是FP4／FP8制品。该实验的服务上限虽设为1M，实际输入仍是78–90 token，表内保留实际负载即可。

直接来源：[消融明细](https://github.com/Tokha233/deepseek-v4.1-flash-a100-turbo/blob/main/docs/concurrency-and-short-requests.zh-CN.md)、[测试方法](https://github.com/Tokha233/deepseek-v4.1-flash-a100-turbo/blob/main/benchmarks/README.md)、[项目README](https://github.com/Tokha233/deepseek-v4.1-flash-a100-turbo)。第17页另一个modified vLLM来源为[keplerzip性能记录](https://github.com/keplerzip/deepseek-v4.1-flash-a100/blob/main/docs/performance.md)。以上数字来自10月14日归档；上游更新时注意区分新旧测试。

### Spark配置和三路测试

第26页可直接使用以下配置行：

> 单GB10、TP1；FP8权重＋FP8 KV、MTP3、FlashInfer；YaRN factor=4；主模型和MTP草稿上限均为1,000,000；本次实测关闭前缀缓存。

讲者备注补充：原生上限为262,144；`max_num_seqs=8`、`max_num_batched_tokens=16,384`、GPU内存预算0.80。主模型扩展到1M时，也要显式设置草稿上限。朋友的300K诊断中，草稿仍受262K门限限制时测得5.80 token/s；修正后重测为17.23 token/s。该诊断解释配置问题，主结果继续使用修正后的样本。

第7页保留：三路均为100,000输入、各4,096输出。共同decode窗口每路平均17.47 token/s，约写17.5；从各自首token到输出结束的全段平均12.45，约写12.5。左侧1.81M缓存池是容量信息。

来源：[官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B-FP8/blob/main/README.md)、[vLLM草稿长度问题58080](https://github.com/vllm-project/vllm/issues/58080)、[vLLM benchmark CLI](https://docs.vllm.ai/en/latest/cli/bench/serve/)。外部测试数字来自用户提供的汇总，本文已列出所需参数；完整记录见本仓库[外部测试分析](../../knowledge-base/infrastructure/dgx-spark-qwen27-external-benchmark-2026-10-12.md)。

### 报价对应的完整服务器

以下延续**2026年10月12日预算**，汇率假设为USD/CNY=7.00；人民币为含所列税费、运输和支持准备的预算估算。

| GPU服务器 | CPU及主机内存 | 机内互联 | 原交付预算 万元 |
|---|---|---|---:|
| 8×A100 80GB SXM4，翻新 | 双EPYC 7V12；1TB DDR4 | HGX／NVLink | 91–102 |
| 8×H100 80GB SXM5 | 双EPYC 9454；1.5TB DDR5 | NVSwitch | 285–298 |
| 4×H200 NVL 141GB | 双Xeon 6710E等级；1TB主存 | 四卡桥接、PCIe服务器 | 161–283 |
| 8×H200 SXM 141GB | 双EPYC 9454；1.5TB DDR5 | NVSwitch | 291–304 |

四卡H200为组件估算，CPU是预算等级；其余三项有完整服务器挂牌作为输入。新增工具CPU节点另计12–26万元。主机RAM还要容纳Engram、系统和工具等开销，剩余空间才可分配给CPU KV池。

原始价格入口：[A100服务器](https://www.theserverstore.com/nvidia-hgx-8x-a100-80gb-sxm4-nvlink-gpu-server-zt-systems)、[H100服务器](https://configurator.exxactcorp.com/configure/TS4-193475697)、[H200服务器](https://configurator.exxactcorp.com/configure/TS4-118380266)、[H200 NVL单卡](https://viperatech.com/product/nvidia-h200-nvl-graphic-card-141-gb-passive-pcie-900-21010-0040-000)、[Spark官方页面](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)。旧预算与重新查询的价格分别标日期；新增报价仍需核对具体SKU和交付条件。

## 三 新增两页正文

### 新页一 放在原第12页之后

**标题：GPU运行当前任务 内存和SSD保留其他会话**

页面用三层图表示：

- **GPU显存**：正在生成的会话。
- **CPU内存**：近期会继续使用的会话缓存。
- **NVMe SSD**：较久未使用、仍值得保留的缓存。

箭头分别标明“保存缓存”和“读取缓存”。旁边用一次Agent轮次说明：

1. 模型返回工具调用，本轮模型请求结束。
2. 工具执行期间，缓存保存在CPU内存或SSD；GPU空间可供其他请求使用。
3. 工具结果返回，服务查找前缀并载入已有状态。
4. 模型处理新增输入，再继续生成。

页面结论：**同时运行的任务数由GPU资源决定；可保留的会话数由整套缓存系统决定。**

底部给出两条实现路线即可：**vLLM原生KV卸载；vLLM＋LMCache MP**。具体配置放备注。

### 新页二 放在原第23页之后

**标题：取回已有缓存 可以省去长前缀的重复计算**

用下表展示一个DeepSeek TP4、1M会话的缓存读取算例。标题旁标“传输估算”，带宽写进表格。

| 路径 | 假设条件 | 载荷传输时间 |
|---|---|---:|
| CPU内存→GPU | 7.31GB，四卡合计有效24GB/s | 约0.30秒 |
| SSD→内存→GPU | SSD有效6GB/s，随后按24GB/s载入GPU；串行相加 | 约1.52秒 |
| 20个会话同时从内存载回 | 共146.16GB，合计有效24GB/s | 约6.1秒 |

正文用一句话连接实际体验：**再次调用时读取已有缓存，只为本轮新增内容做prefill。排队期间还可以提前加载缓存。**

脚注一次写清：本表仅计算当前Hopper TP4布局的全局KV载荷；实际首token等待还包括其他所需状态、排队、新增输入prefill和第一步生成。表内带宽是假设值。

如果版面需要图形，可把“CPU读取→新增prefill→生成”和“完整输入prefill→生成”画成流程；时间轴按示意绘制，避免给尚无数据的DeepSeek完整1M重算时间编造柱高。

## 四 分层缓存的研究依据

### AI Infra Book已经覆盖原理和实验

| 位置 | 内容 | 可用于讲述的结论 |
|---|---|---|
| 8.3.3 | 对话与Agent的前缀复用、混合注意力状态 | 同一会话追加内容，可以复用已有前缀；递推模型还要保存对应状态。 |
| 8.3.4 | 准入、淘汰、换出与重算 | 缓存价值取决于重算成本、读取成本和再次使用概率。 |
| 9.5.2 | HBM、DRAM、SSD与远端存储 | 逐层加载和排队期间预取，可以减少读取造成的额外等待。 |
| 9.5.3 | 持久化与部分重算 | 保存数据和索引，才能在重启或重新调度后找回可用状态。 |
| 9.5.4 | 缓存亲和性与路由 | 选择请求目的地时，同时考虑排队时间和缓存位置。 |

原书固定版本：`3bdcb4fcab73010eeaccf31cc10a8242a895d82e`。直接阅读[第8章](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/manuscripts/08-推理优化.md)、[第9章](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/manuscripts/09-分布式推理.md)。

书中还附有[两个独立引擎共享CPU KV池的实验](https://github.com/bojieli/ai-infra-book/blob/3bdcb4fcab73010eeaccf31cc10a8242a895d82e/experiments/ch09/09-07/shared-kv/README.md)：同一RTX PRO 6000 Blackwell上的两个Qwen3-8B引擎，通过LMCache共享CPU缓存。12次复用机会中，4GiB池完整命中5次，8GiB池完整命中12次。它适合说明缓存容量影响复用；实验使用约2K／8K输入，与本报告的百万token目标分开标注。

核心公式可放讲者备注：

> 保存一次的时间＋k次读取时间 < k次重新prefill时间。

长期写入SSD时，使用缓存准入和淘汰策略，优先保留仍在进行的多轮任务及高复用前缀。书中也讨论了SSD写入寿命与异步写入，正文可概括为“优先保存值得复用的状态”。

### vLLM原生路径

[vLLM KV Offloading Usage Guide](https://docs.vllm.ai/en/stable/features/kv_offloading_usage/)给出完整配置和数据路径：

- `OffloadingConnector`与`CPUOffloadingSpec`：把完成的KV块异步保存到主机内存，命中时载入GPU。
- `TieringOffloadingSpec`：CPU主层加一个或多个次级存储层。
- 文件系统层`type: fs`：把KV写入指定目录，可使用本地NVMe。
- 当前这条多级路径通过CPU主层中转，读取顺序为SSD→CPU→GPU。

简单CPU卸载的顶层参数为`--kv-offloading-size`和`--kv-offloading-backend native`；多级存储通过`--kv-transfer-config`配置。内存预算参数的统计范围要按所用版本核对，官方接口按跨worker总量记录，不能直接当成每张卡的额外容量。`--cpu-offload-gb`是权重卸载参数，勿将其用作KV缓存配置。

已有GPU前缀缓存和CPU／SSD缓存需要区分。仅开启`--enable-prefix-caching`不等于启用了磁盘持久化。原生卸载还区分prompt块与decode产生的块；涉及保存Agent上一轮输出时，应按所选版本核对`offload_prompt_only`及其默认值。

### vLLM与LMCache MP

[LMCache MP的L2存储文档](https://docs.lmcache.ai/mp/l2_storage.html)描述了CPU内存层、持久化存储、异步写入与缺失时预取。普通文件系统、NIXL存储等有各自的adapter。

当前[旧本地存储教程](https://docs.lmcache.ai/kv_cache/storage_backends/local_storage.html)已将进程内模式标为弃用，进一步research和配置应优先参考MP文档。若采用双TP4或增加模型实例，需统一可共享对象的标识，并让实例连接相应缓存服务；相同模型名本身还不足以保证缓存格式兼容。

两条路线可以这样介绍：**单实例先比较vLLM原生卸载；需要独立缓存服务或多个实例复用时，再比较LMCache MP。** 这是本报告的实现选择思路，具体性能按模型、缓存布局与存储测量。

### Qwen和DeepSeek的现成支持

| 模型 | 已找到的官方说明 | 实施时核对的组合 |
|---|---|---|
| Qwen3.8-27B | LMCache列入单GPU验证模型；按混合注意力组保存状态 | `align`模式、分组对象、与引擎一致的chunk大小；本项目还使用FP8制品、FP8 KV、MTP3。 |
| DeepSeek-V4.1-Flash | LMCache列有八GPU验证recipe；分别处理多种缓存组 | 所选GPU对应的KV格式、缓存组和DSpark／MTP。该recipe明确标注MTP组合尚未验证。 |

直接链接：[Qwen3.5／3.6／3.8 recipe](https://docs.lmcache.ai/recipes/qwen3_5.html)、[DeepSeek-V4.1-Flash recipe](https://docs.lmcache.ai/recipes/deepseek_v41_flash.html)。Qwen的`align`前缀缓存仍标注为实验性；正文介绍其工作原理，部署备注保留具体版本和组合。

版本核对时有一处过时提示：DeepSeek的LMCache recipe仍写“vLLM尚无包含V4.1的正式release”，但[vLLM 0.30.0发布记录](https://github.com/vllm-project/vllm/releases/tag/v0.30.0)已列入该模型，10月5日又发布了[0.31.0](https://github.com/vllm-project/vllm/releases/tag/v0.31.0)。不要沿用旧提示得出“只能用nightly”的结论；模型已进入release与某个缓存／MTP组合完成验证是两个具体事项。

## 五 应用于两套部署方案

### 公司服务器

独立GPU显存与主机DRAM是两类物理资源。把可复用缓存保存在主机内存后，GPU可腾出逻辑缓存块给其他请求；等待工具的用户回来时，再读取所需状态。最近使用的会话优先留在DRAM，更久未使用的会话保存到SSD。

据此，方案分别预算：

- 同时生成请求：GPU计算、显存和单路生成速度。
- 等待工具或用户的会话：DRAM／SSD容量、读取带宽和缓存命中。
- 大批会话同时继续：合计读取量、排队和新增输入prefill。

原第12页“20个生成＋20个等待＝40份上下文”仍成立，新增页解释如何将这40份状态分配到不同存储层。原第10页的20×1M是GPU缓存容量估算，不因增加SSD就改写成更高的同时生成能力。

### Spark

[NVIDIA Spark内存架构](https://docs.nvidia.com/dgx/dgx-spark-porting-guide/overview.html)明确说明CPU和GPU共用128GB LPDDR5x。CPU缓存和GPU缓存仍消耗同一份物理内存；单纯增加CPU缓存副本不会扩大总容量。

Spark适合优先考虑：**在统一内存中保留近期会话，用本地NVMe保存闲置长会话。** 这样能减少重新打开长任务时的完整prefill。512K持续生成的约15 token/s仍沿用原有估算；分层缓存主要改善下一轮开始前的等待和可保存的会话数量。

原第25页总结可以补一行：**公司采用GPU＋DRAM＋SSD分层；Spark重点研究内存＋SSD。**

### Engram主存预算的版本变化

原第11页按两个独立实例各存一份Engram计算，主存约203GB／406GB。[vLLM 0.31.0发布记录](https://github.com/vllm-project/vllm/releases/tag/v0.31.0)新增了同机DP副本默认共享Engram host tables的能力，对应[PR 57651](https://github.com/vllm-project/vllm/pull/57651)。

请进一步核对最终双TP4采用的是两个独立服务进程，还是支持这项共享机制的同机DP部署，再决定Engram保留一份还是两份。当前旧预算保留“两份副本”的条件；若采用共享实现，则更新主存分配，同时注明新版本。Engram是模型的查找表，和本文讨论的会话KV缓存分别计账。

## 六 算例输入和计算方法

新增页二沿用已有Hopper实现的全局KV布局：**1,827 bytes／token／TP rank**。这个数包含该布局的页对齐，来自已归档的源代码复算；没有把TP副本除以卡数。

| 输入 | 数值或假设 |
|---|---|
| 会话总长度 | 1,000,000 tokens |
| 单rank全局KV | 1.827GB |
| TP4四份载荷之和 | 7.308GB |
| CPU到四GPU的合计有效带宽 | **假设24GB/s** |
| SSD读取有效带宽 | **假设6GB/s** |
| SSD路径计算 | 先读到CPU，再载入GPU，按串行相加 |

复算：

- 内存载入：`7.308 / 24 = 0.3045秒`。
- SSD载入：`7.308 / 6 + 7.308 / 24 = 1.5225秒`。
- 20会话的内存载入：`20 × 7.308 / 24 = 6.09秒`。

这些是已有缓存的读取时间，不含首次保存。跨多个TP rank去重、广播、预取或流水化会改变实际传输路径；算例固定为当前四份载荷的串行预算。最终首token时间还需要该次请求的新输入prefill等阶段，页面标注一次即可。

原计算入口：[公司方案](../../knowledge-base/infrastructure/scenario-3-company-agent-2026-09-23.md)、[结构化结果](../../knowledge-base/infrastructure/data/week7-deployment-2026-10-12/results.json)。Pro若只能读取上传附件，可直接用本节已列全的输入；不要将假设带宽标成设备实测。

## 七 PDF可见的参考链接和交付检查

末页至少保留以下入口，并使导出的PDF可点击：

1. [AI Infra Book](https://github.com/bojieli/ai-infra-book)，讲解主要对应第8、9、11章。
2. [vLLM KV卸载指南](https://docs.vllm.ai/en/stable/features/kv_offloading_usage/)。
3. [LMCache多级存储](https://docs.lmcache.ai/mp/l2_storage.html)。
4. [shi3z A100项目](https://github.com/shi3z/deepseekv4.1-A100-custom)。
5. [modified vLLM的A800消融与测试](https://github.com/Tokha233/deepseek-v4.1-flash-a100-turbo/blob/main/docs/concurrency-and-short-requests.zh-CN.md)。
6. [Qwen模型卡](https://huggingface.co/Qwen/Qwen3.8-27B-FP8/blob/main/README.md)与[DeepSeek模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)，可合并为同一项。

其余链接随对应页讲者备注保留。当前说明中的内嵌链接用于进一步研究；不要只引用“原版PDF第几页”。

修改后交付可编辑PPTX和PDF，并完成以下检查：

- 六处补充全部落实；两页新内容插入后，页码和交叉引用一致。
- 继续保留四部分结构，公司知识库保持简版。
- 17.5／12.5 token/s旁明确100K输入；消融图明确modified vLLM／8×A800。
- 缓存取回图明确流向，所有时间旁保留其计算范围和带宽假设。
- 公司DRAM与Spark统一内存分别说明；模型权重、Engram和会话KV分别计账。
- PDF来源链接可点击；图表无遮挡、错位和文字溢出。
- 使用匿名的实习项目署名，封面、正文、备注和文件属性均保持一致。

完整解释沿用[已认可讲稿](speaker-notes.md)。修改以Pro稿为基底，输出修订版PPTX及PDF。
