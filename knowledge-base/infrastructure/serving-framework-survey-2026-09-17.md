# Serving framework调研：GPU服务、Apple Silicon与异构推理

**核查日期：**2026年9月17日；9月18日补充业务负载、调优和比较方法，沿用原文件路径。

**本轮修改前检查点：**`9e5c2fe`。

**范围：**vLLM、SGLang、TokenSpeed、MLX-LM、MLX-VLM、llama.cpp、KTransformers、ik_llama.cpp；补充TensorRT-LLM。

**输入：**[当前8模型候选](../models/model-survey-2026-09-16.md)、[模型许可](../models/license-review-2026-09-16.md)。

**配套：**[Harness调研](harness-survey-2026-09-17.md)、[参考架构](reference-architecture.md)。

本轮完成官方文档、固定源码快照、许可和版本调查，没有安装引擎、下载模型或跑性能测试。文中的优先级是研究判断，性能描述只说明机制，不宣布某框架在本项目中最快。

### 面向业务读者的概览

Serving framework负责把模型变成可持续使用的服务。对同事而言，它主要影响开始回答前等待多久、阅读长材料是否流畅，以及多人使用时服务是否稳定。

| 项目 | 它做什么 | 主要优点与适用方向 |
|---|---|---|
| vLLM | 在GPU等设备上持续处理多个用户的模型请求 | 模型服务生态与接口较完整，适合集中共享部署 |
| SGLang | 高效组织模型请求、上下文缓存和多卡执行 | 值得重点比较长上下文、多轮Agent与大型MoE服务 |
| TokenSpeed | 针对Agent负载优化调度与计算内核 | 在有准确模型和硬件recipe时，可能提供更好的响应/吞吐组合，需同条件验证 |
| MLX-LM / MLX-VLM | 在Apple Silicon运行文本或多模态模型 | 利用Mac平台特点，适合专业个人机及其本地服务 |
| llama.cpp | 用统一模型格式在多种CPU/GPU平台运行模型 | 部署形态灵活，可全GPU、Metal或CPU/GPU混合运行 |
| KTransformers | 让CPU与GPU协作承担大型模型计算 | 利用大容量主存与CPU专家计算，提供另一种大型模型部署路线 |
| ik_llama.cpp | 为llama.cpp路线增加特定量化和性能优化 | 适合有明确硬件、模型和维护责任的优化对照 |
| TensorRT-LLM | 面向NVIDIA设备进行专用推理优化 | 固定模型和设备时值得比较，需衡量支持范围及维护投入 |

这些是路线优势，不能据此直接排列速度名次。下文保留技术条件，供确定实际组合时使用。

## 1. 结论与建议的验证顺序

- **共享GPU服务：vLLM与SGLang并列基线。** 二者具备成熟服务系统的主要机制，重点工作是核对目标模型、GPU、精度、解析器与负载的组合，并做针对性调优。
- **TokenSpeed作为性能挑战者。** 当前已有Qwen3.8-27B、GLM-5.3/Flash、Kimi K3的具体recipe，值得在匹配硬件上比较；部署、版本和功能覆盖需要单独验收。
- **Mac个人机：MLX-LM/MLX-VLM与llama.cpp Metal两条路线。** 按文本或多模态任务、模型转换、协议要求和维护方式选择，不能只看“能在Mac上运行”。
- **CPU/GPU异构：KTransformers结合SGLang，llama.cpp作通用比较，ik_llama.cpp作特定量化/内核对照。** 重点评估大模型容量、prefill、内存带宽及多用户性能；不因使用CPU就认定仅适合低配场景。
- **TensorRT-LLM补充硬件专用对照。** 在固定NVIDIA设备与模型组合上有评估价值，是否加入实测取决于预期收益及维护投入。

本阶段无需把所有模型与引擎做全排列。先选一个个人或GPU服务组合完成必需PoC，再用相同任务进行少量引擎对照；其他组合完成可追溯的文档与资源研究。

## 2. 分类：平台优化与执行位置是两个维度

用户提出的“硬件优化、通用框架、CPU/GPU混合”覆盖了实际选择，但不是互斥分类。vLLM/SGLang支持多种后端，同时使用硬件专用内核；llama.cpp既能全GPU运行，也能CPU/GPU混合；KTransformers现在还能与SGLang组合。

| 维度 | 需要回答的问题 | 例子 |
|---|---|---|
| 服务目标 | 单人交互、离线批处理，还是多用户持续服务 | MLX个人服务；vLLM/SGLang共享服务 |
| 平台与内核 | 具体GPU架构、精度、注意力/MoE内核是否匹配 | CUDA/ROCm后端；Apple Metal；CPU AMX/AVX |
| 权重与计算位置 | 全部驻留加速器，还是分层/专家异构执行 | llama.cpp offload；kt-kernel专家放置 |
| API及调度 | 客户端需要什么协议，服务如何批处理、缓存和恢复 | Chat Completions、Responses、Messages；连续批处理 |

以下按实际部署路径组织，同时记录跨路径能力。

## 3. 框架概览与许可

版本列是核查时取得的GitHub latest-release或包索引快照，**不代表本轮所有HEAD功能都已包含在该版本**。每项源码按完整commit保存；不能混用main文档、旧wheel和新模型recipe后宣称已经验证。

| 框架 | 主要定位 | 版本快照 | 仓库许可 | 本项目角色 |
|---|---|---|---|---|
| [vLLM](https://github.com/vllm-project/vllm) [TECH-020](../sources/TECH-020/original.md) | 多用户模型服务、多硬件后端 | v0.29.0，9月9日 | Apache 2.0 | GPU共享基线之一 |
| [SGLang](https://github.com/sgl-project/sglang) [TECH-021](../sources/TECH-021/original.md) | 高吞吐服务、缓存、MoE与分布式 | v0.5.19，9月5日 | Apache 2.0 | GPU共享基线之一；异构集成前端 |
| [TokenSpeed](https://github.com/lightseekorg/tokenspeed) [TECH-022](../sources/TECH-022/original.md) | 面向agent负载的高性能服务 | v0.1.0，7月24日；源码/recipe更新更晚 | MIT | 硬件与模型匹配时加入比较 |
| [MLX-LM](https://github.com/ml-explore/mlx-lm) [TECH-023](../sources/TECH-023/original.md) | Apple Silicon文本推理、量化、微调及服务 | GitHub/PyPI为0.31.3；核查源码更新至9月 | MIT，Apple版权声明 | Mac文本基线 |
| [MLX-VLM](https://github.com/Blaizzy/mlx-vlm) [TECH-024](../sources/TECH-024/original.md) | MLX多模态及HTTP服务 | v0.7.1，9月14日 | MIT；社区项目 | Mac多模态与Responses候选 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) [TECH-025](../sources/TECH-025/original.md) | GGUF、多平台CPU/GPU及HTTP服务 | v0.4.1，9月14日 | MIT | 通用个人机、Metal及offload基线 |
| [KTransformers](https://github.com/kvcache-ai/ktransformers) [TECH-026](../sources/TECH-026/original.md) | CPU/GPU异构MoE、kt-kernel与SGLang集成 | v0.7.1，9月15日 | Apache 2.0 | 大内存异构路线 |
| [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) [TECH-027](../sources/TECH-027/original.md) | llama.cpp分支，扩展量化和优化实现 | 固定commit；latest-release API返回404 | MIT | 工作负载明确时的优化对照 |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) [TECH-040](../sources/TECH-040/original.md) | NVIDIA专用推理栈 | latest-release快照v1.2.1；源码更新更晚 | Apache 2.0及第三方部分 | 固定设备/模型组合的补充评估 |

许可证列指本次仓库文件，模型权重、CUDA等运行组件、容器及企业支持合同另行核对。ik的API返回404只表示本轮未取得标准latest-release记录，不代表没有tag或其他构建渠道。包索引与GitHub发布记录差异也不直接说明项目停止维护。

## 4. GPU共享服务

### 4.1 vLLM

官方项目包含PagedAttention内存管理、连续批处理、前缀缓存、结构化输出、推理/工具解析器以及多种并行方式。这些机制使其适合作为几十人共享服务的基线。[README](../sources/TECH-020/original.md)、[服务API](../sources/TECH-020/openai-server.md)。

本项目的主要工程问题是：所选模型和精度使用哪个内核；长输入如何与交互decode共存；显存应在权重、缓存及调度余量之间如何分配；框架提供的Responses能力是否覆盖harness实际发送的请求。

**研究判断：**优先选择有目标模型官方recipe、可固定构建和正常维护路径的配置。先验证普通推理及任务质量，再逐项加入MTP/推测解码、缓存或并行优化。一个版本支持某架构，不等于所有工具解析器、量化与GPU组合同时可用。

共享入口还要核对HTTP面的实际鉴权范围：本轮官方服务文档明确`--api-key`并不保护同进程的所有端点，例如其列出的`/invocations`。因此参考架构应检查并限制实际暴露的端点，不能仅因配置了一个key就认为整个服务面受保护。

### 4.2 SGLang

当前SGLang的核心是推理服务系统，不能仅按早期编排DSL理解。官方列出RadixAttention前缀缓存、连续批处理、分块prefill、结构化输出、量化，以及TP/PP/EP/DP等并行能力；还有PD分离和分层缓存等扩展。[TECH-021](../sources/TECH-021/original.md)。

对本项目，长材料、多轮agent调用和大型MoE是重点验证负载。缓存价值取决于真实前缀复用；多用户重试、工具输出及上下文压缩会改变缓存命中。KTransformers的当前异构路线可使用SGLang服务层，因此两者可能是组合关系。

**研究判断：**与vLLM使用同一模型、材料、精度和服务目标比较。共享服务只有几十人时，是否需要PD分离或跨节点EP由测量决定，先保留简单可维护配置。公开“生产采用”说明框架成熟度，不能替代特定组合的运行验收。

### 4.3 TokenSpeed

官方把C++调度控制面与Python执行面分开，采用有限状态机管理请求/KV生命周期，并提供可插拔内核与SMG集成入口。[README](../sources/TECH-022/original.md)。它面向agent型负载，值得关注反复prefill、低批量交互及模型专用优化。

本轮[recipe](../sources/TECH-022/models.md)直接列出Qwen3.8-27B、GLM-5.3、GLM-5.3-Flash与Kimi K3，以及部分NVIDIA/AMD配置。**不能根据旧参数页一句“currently serves CUDA”忽略同一快照的新AMD/NPU示例。** 反过来也不能把某个AMD recipe扩展为所有模型和设备的完整支持。

需要单独核对：

- 7月release与9月模型支持的构建差异；固定runner镜像、scheduler、kernel、SMG和模型版本。
- `--max-num-batched-tokens`等参数的语义不能机械照搬。官方[参数对照](../sources/TECH-022/compatible-parameters.md)将每步调度预算与全局token池区分。
- [入门文档](../sources/TECH-022/getting-started.md)目前是开发环境路径，使用源码可编辑安装和较宽容器权限。企业运行时应将确有需要的权限与普通开发便利配置区分，形成标准镜像。
- 本轮recipe没有确认DeepSeek-V4.1-Flash的准确条目，不能用V4-Flash/Pro的条目替代；Gemma与Qwen3.6-35B的准确组合也待补核。

**研究判断：**它是有明确技术与模型支持证据的新候选，值得实测，但“性能挑战者”到共享服务默认引擎之间还需要版本、功能和稳定性证据。作者吞吐图只在其硬件、模型和输入输出条件内解释。

### 4.4 TensorRT-LLM的补充位置

NVIDIA官方推理项目适合加入特定硬件优化路线的对照。[TECH-040](../sources/TECH-040/original.md)。本阶段先关注候选模型的实际支持方式、精度/硬件限制、服务API及与现有运维栈的连接；不因它属于厂商栈就假定必然更快，也不把所有当前路径都概括成必须手工构建静态engine。

只有在准确模型和设备存在可复用路径，且预期收益足以覆盖额外维护时，才加入首轮benchmark。

## 5. Apple Silicon：不只有mlx-lm

### 5.1 MLX-LM

MLX提供Apple Silicon数组计算和Metal基础；MLX-LM负责文本模型装载、量化、生成和微调，并提供`mlx_lm.server`。本轮核对的[server源码](../sources/TECH-023/server.py)有工具解析、请求队列和BatchGenerator，但POST路由为Completions/Chat Completions，未列Responses。

[Apple WWDC26](https://developer.apple.com/videos/play/wwdc2026/232/)明确演示MLX-LM Server接OpenCode、连续批处理和多Mac分布式推理。[转录归档](../sources/TECH-042/original.md)。这是Apple生态与实现路径证据，不是本项目的速度结果。统一内存需同时容纳模型、缓存、系统和其他进程，物理内存容量不等于全部可交给推理。

**项目用途：**四个专业个人机候选的文本工作路线；确定模型转换及文本模型类、chat template和工具解析。若harness只提供Responses调用，原生MLX-LM接口不能仅改base URL就对接。

### 5.2 MLX-VLM

这是基于MLX的社区多模态项目，不能写成Apple官方MLX-LM的同名组件。当前[README](../sources/TECH-024/original.md)包含连续批处理、结构化输出、缓存与服务指标，列出Chat Completions和Responses端点；有Qwen3.8示例和[Gemma 4专门说明](../sources/TECH-024/gemma4.md)。

**项目用途：**财报图表、扫描材料等多模态实验，以及需要Responses的Mac组合候选。文本、图像、量化、缓存和工具功能逐项验证；源码HEAD能力不能自动归入已安装wheel。模型能读图也不等于复杂金融表格提取已经达标。

### 5.3 llama.cpp Metal、应用封装与其他方向

llama.cpp原生支持Apple Metal和GGUF，可与MLX路线在同一Mac上比较。[TECH-025](../sources/TECH-025/original.md)。它还提供自己的HTTP server，适合希望跨Windows/Linux/Mac复用模型格式与服务配置的场景。

Ollama、LM Studio属于更高层的本地模型管理/应用入口，不能只按产品名判断底层引擎、协议或许可；具体版本可能使用不同运行后端。Apple官方也列出这些生态工具。若需要原生Mac应用开发，Apple另提供MLX Swift方向，但本阶段不为现有PoC另写一套客户端。

多Mac分布式是可研究路径；是否比一台专业工作站或集中GPU服务划算，需要把互联、吞吐、故障和维护一起比较。Mac也可以只承载harness、连接集中GPU服务，客户端平台不决定模型必须在该Mac上推理。

## 6. CPU/GPU混合与通用运行

### 6.1 llama.cpp

其范围包括CPU、全GPU、多后端及CPU/GPU混合，不仅是offload工具。当前[server文档](../sources/TECH-025/server.md)包含多用户并行解码、连续批处理、API key和多种HTTP协议。

**优势与取舍：**GGUF与多种量化提供较灵活的装载方式，适合个人设备和跨平台部署。部分层或专家放到CPU后，需测主存带宽、CPU向量指令、线程/NUMA放置以及CPU-GPU传输对prefill与decode的影响。模型能装载只是容量条件，不能据此推定几十人共享的响应目标。

### 6.2 KTransformers

当前仓库以kt-kernel为CPU优化和异构专家执行核心，强调AMX/AVX、NUMA、INT4/INT8及CPU/GPU专家放置，并可集成SGLang服务。[README](../sources/TECH-026/original.md)、[kt-kernel](../sources/TECH-026/kt-kernel.md)。

与本项目直接相关的是[GLM-5.3-Flash教程](../sources/TECH-026/glm53-flash.md)：它列出FP8模型约306 GiB、至少350 GB可用系统内存、特定GPU/CPU内核条件，并使用`ktransformers[sglang]`的兼容组合。这里的内存与设备是该文档路径的要求，不是所有KT模型的最低配置。

**研究判断：**把KT/SGLang作为大型模型异构路线认真比较，尤其是在大容量主存与GPU能够提供合适质量/延迟时。验证CPU专家执行、GPU热专家、prefill策略、线程与NUMA，再测并发。当前有GLM Flash证据，不能据旧DeepSeek-V4教程直接宣布V4.1支持完成。

### 6.3 ik_llama.cpp

它是独立维护的llama.cpp分支，提供额外量化、内核和并行优化，当前README列出多个新架构与后端进展。[TECH-027](../sources/TECH-027/original.md)。本轮[function-calling文档](../sources/TECH-027/function-calling.md)已有原生/通用工具调用路径，因此不能沿用旧讨论中的“没有tool calling”概括。

**研究判断：**若某个目标模型和设备在其量化/内核上有可重复收益，可进入对照。代价包括特定量化制品兼容、与上游的差异、版本固定和缺陷回归。对共享平台，需证明收益与维护安排；对专家个人工作站，可保留更大的评估空间。通用parser存在也不保证所有新模型工具格式可靠。

## 7. 与当前8模型的对应关系

“已找到路径”表示本轮官方模型卡、框架代码或recipe中有对应证据，均未本地实测。以下为下一步验证路由，不是全平台支持承诺。

| 模型 | 首先验证的路径 | 已取得的具体证据或缺口 |
|---|---|---|
| Qwen3.8-27B | vLLM / SGLang；Mac比较MLX-VLM与llama.cpp | 原模型卡列GPU引擎；TokenSpeed有精确27B FP8 recipe，MLX-VLM有27B示例；llama量化与chat template还需固定 |
| Qwen3.6-35B-A3B | vLLM / SGLang；个人平台补MLX/GGUF | 卡片给出引擎版本建议；同架构的Qwen3.5支持只能提供线索，实际3.6制品与解析器另核 |
| Gemma 4 31B | vLLM / SGLang；MLX-VLM / llama.cpp Metal | vLLM架构记录、MLX-VLM具体31B示例；其他引擎准确构建与格式待固定 |
| Gemma 4 26B A4B | vLLM / SGLang；MLX/GGUF路径 | 有Gemma 4架构记录，26B MoE不能直接套31B内存、量化和速度 |
| DeepSeek-V4.1-Flash | 更新的vLLM / SGLang发布方构建 | vLLM支持合入记录已取得；本轮主分支有架构入口。TokenSpeed/KT的V4条目不能替代V4.1 |
| GLM-5.3-Flash | vLLM / SGLang、TokenSpeed；KT异构 | 精确模型卡、TokenSpeed recipe及KT教程已取得；全部路径需区别HEAD与release |
| GLM-5.3 | vLLM / SGLang、TokenSpeed | 模型卡和TokenSpeed精确recipe；先结合模型自定义许可及实际多卡资源 |
| Kimi K3 | vLLM / SGLang、TokenSpeed | 卡片列服务引擎，TokenSpeed有K3及具体硬件recipe；完整实测取决于资源，研究继续保留 |

## 8. Serving与harness的接口合同

| 引擎/路径 | 本轮确认的接口证据 | 接入含义 |
|---|---|---|
| vLLM | 文档列Chat与Responses等API | Codex候选路径仍需验证事件、工具循环及状态相关字段 |
| SGLang | 已归档Chat Completions和Anthropic兼容文档 | OpenCode/pi可先测Chat；Responses的准确版本/前端覆盖单列验证 |
| TokenSpeed | `serve`与SMG前端，文档Chat示例 | 不由“OpenAI-compatible”直接推定Responses全部行为 |
| MLX-LM固定源码 | Completions / Chat Completions POST路由 | 优先接Chat兼容harness；Codex需要其他适配路线 |
| MLX-VLM当前文档 | Chat Completions、Responses、JSON schema | Responses候选；harness实际所需子集还需联调 |
| llama.cpp当前server文档 | Chat Completions、Responses、Anthropic Messages | 有更广协议表面，但各模型的工具与推理格式仍分别核对 |
| KT/SGLang | 使用对应SGLang-KT服务层及parser | 按安装组合验证，不继承任意上游版本全部能力 |
| ik_llama.cpp | Chat/function-calling路径 | 额外协议未在本轮确认，按需求补核 |

最低联调应覆盖：流式事件、tool call ID与参数、并行工具结果、reasoning分离、JSON schema、上下文超限、取消、超时、重试和使用量计数。协议转换gateway可以研究，但其字段丢失、状态保存和额外数据处理也是实际成本。

## 9. 面向本项目的benchmark设计

分别比较引擎与模型，避免同时换模型、精度、harness后无法判断差异来源。

| 测试组 | 固定条件 | 测什么 |
|---|---|---|
| 同模型同设备的GPU引擎对照 | 相同权重、精度、任务、上下文与生成设置 | TTFT、每token延迟、p50/p95完整任务时间、合格吞吐、显存、错误 |
| 单机平台对照 | 同一业务样本与质量要求，明确格式/量化差异 | Mac/专业GPU工作站的体验、资源、功耗与维护；不把不同精度当纯引擎差异 |
| 异构对照 | 同模型和可比质量，记录CPU/RAM/NUMA/GPU/互联 | prefill、decode、长上下文、并发退化、CPU及带宽占用 |
| agent负载回放 | 固定工具轨迹和输入输出，再与真实agent结果对照 | 多轮prefill、缓存命中、短生成和长工具返回的混合影响 |

样本覆盖短问答、长材料、批量事件提取，沿用1/4/8/16/32/50并发档位；无法达到的档位如实记录。冷启动、预热、无缓存和有缓存分开测。加入请求到达速率和用户思考/工具执行间隔，不能把50个账号直接当成50路持续decode。

调优顺序建议为：基础正确性与精度 → 上下文/缓存与显存 → 调度及prefill → 并行布局 → 推测解码等附加优化。每步复测质量与失败样本。GPU/内核和解析器变化可能改变输出，吞吐优化不自动等于业务收益。

交付记录包含确切commit/tag、镜像digest、依赖、驱动、模型制品、启动参数、测试输入、原始日志和故障恢复结果。持续运行及恢复验证按[三周计划](../../weekly/week-03-05-plan.md)执行。本轮只完成研究设计，尚未产生benchmark数字。

## 10. 9月18日深化：如何判断哪条路线真正适合本项目

### 10.1 区分三种工作负载

| 实际工作 | 负载特征 | 优先观察什么 |
|---|---|---|
| 员工交互问答 | 用户会阅读答案和继续提问，到达时间不均匀 | 首次响应、尾部延迟、取消和排队；短问题不能长期被大任务挡住 |
| 一批公告或报告处理 | 可事先准备任务，部分可以等待 | 固定时间内完成多少合格任务、资源利用率、失败重试和批任务截止时间 |
| 多步骤研究Agent | 一项用户任务产生多次模型调用，中间夹着检索、计算和文件操作 | 多轮prefill、共享前缀、工具结果增长、完整任务时间及总调用量 |

这里有一个会影响硬件估算的区别：用户人数不是模型请求数。一位研究员的一项任务可能产生多次调用，但调用之间又可能在等待工具。容量研究需要记录任务到达、模型调用和工具耗时，而不是简单按员工数量乘单次回答速度。

**本项目分析：**以同一组真实业务材料构造上述三类负载。先测引擎纯推理，再测应用完整任务。这样可以判断慢在模型、排队、检索还是文件工具，不把所有等待都归因于GPU。

### 10.2 从峰值吞吐转向“在等待要求内完成的工作”

[vLLM v0.29.0 benchmark文档](https://docs.vllm.ai/en/v0.29.0/cli/bench/serve/)支持请求速率、分位数及`goodput`指标，可按首次token时间、每token时间和端到端时延设目标。[TECH-054](../sources/TECH-054/original.md)。

对本项目，应同时报告：

- 引擎吞吐：单位时间生成多少token或完成多少请求。
- 时延达标吞吐：有多少请求在规定等待时间内完成。
- 合格业务任务吞吐：有多少完整任务同时达到质量与时间要求。

后一个指标还需要金融任务评分，不能由框架的goodput直接给出。一个能产生更多token但需要更多纠错、重试和人工核查的组合，未必更有经济性。质量和时延目标在实验前写明，原始失败请求也计入结果。

### 10.3 调优指南必须对应同一种使用方式

本轮核对的[SGLang调优指南](https://docs.sglang.io/docs/advanced_features/hyperparameter_tuning)明确以**offline batch inference**为其中一节的前提。[TECH-055](../sources/TECH-055/original.md)。它围绕批大小、队列、缓存池、prefill、并行方式讨论吞吐；这些机制可以借鉴，具体队列目标不能直接搬到几十人的交互服务。

| 观察到的现象 | 下一步核查方向 | 需要一起复查的结果 |
|---|---|---|
| 长材料开始回答很慢 | 输入长度、prefill批预算、复用前缀、解析/检索耗时 | TTFT与其他用户等待，不能只看最终decode速度 |
| 单人速度可以，多人明显排队 | 实际到达率、调度预算、缓存容量、模型副本 | p95时延、错误率、资源成本 |
| 增加并发后内存耗尽 | 权重、KV/状态缓存、图执行缓冲与临时激活 | 同精度质量、可支持的上下文和运行余量 |
| 多轮Agent比单问答慢很多 | 工具历史膨胀、重复prefill、缓存命中、工具延迟 | 完整任务成功率与总时间 |
| 多卡没有预期收益 | 并行布局、互联、通信开销及各阶段负载 | 同服务目标下是否模型副本更适合；需实测判断 |
| CPU/GPU混合能加载但体验差 | CPU指令、NUMA、主存带宽、专家放置与传输 | 长输入、持续生成和并发分别测量 |

表中是诊断路线，不是已找到本项目瓶颈。先改变一个因素并留足记录，避免把大量参数同时打开后无法解释收益来源。

### 10.4 框架比较需要补齐的证据

| 路线 | 已有比较价值 | 深入研究应取得的下一份证据 |
|---|---|---|
| vLLM / SGLang | 共享GPU成熟服务路线 | 同一模型/精度/设备/任务的实际时延与质量，再比较可维护配置 |
| TokenSpeed | 特定模型、硬件及Agent负载的优化路线 | 当前recipe使用的构建与基线同条件测试；不能跨模型/跨硬件借用峰值图 |
| MLX / llama.cpp Metal | 专业Mac部署路径 | 同业务材料下的模型转换、量化质量、内存和用户任务体验 |
| KT / llama.cpp / ik异构 | 可利用主存承担大模型容量 | 固定CPU、内存拓扑、GPU和精度，比较实际任务及多人退化 |

经济性要计入管理员调优和升级时间。只有在任务成功率和响应目标可接受时，才比较设备、能耗与维护成本。本阶段不需要为追求全框架榜单同时采购或部署多种硬件。

### 10.5 与非coding应用选型的连接

员工工作台、资料研究平台和长任务助手会产生不同负载。最新[harness调研](harness-survey-2026-09-17.md)加入Open WebUI、LibreChat、Onyx、RAGFlow、Goose等路线。先选择希望交付的员工能力，再给serving准备相应负载；同一套GPU服务也可以支持多种前端。

9月18日再次读取GitHub latest-release，vLLM仍为v0.29.0，SGLang仍为v0.5.19，快照保存在TECH-054/055。没有新tag不意味着模型适配停止，已经归档的main、特定发布方构建和正式release继续分别记录。

## 11. 来源与完成边界

TECH-020–027、040为引擎repo快照，TECH-042为Apple官方转录；TECH-009–019及模型卡补充准确模型条件。额外文档的固定路径、抓取时间及SHA-256见各metadata。已核对的API/源码是“有该接口/入口”的证据，本机正确运行与生产服务承诺都需要后续验证。

9月18日增加TECH-054–055的benchmark与调优资料，扩展到实际任务负载和业务验收。未生成任何本地性能排名或部署结果。

下一步优先形成一个GPU服务组合和一个个人机组合的可执行配置，随实际设备确定。Harness的结构、协议和许可结论见[独立调研](harness-survey-2026-09-17.md)。
