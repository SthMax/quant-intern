# TECH-091｜最终汇报公开模型评测来源包

**核查日期：2026-10-20，Asia/Shanghai。核查方式：agent读取原始网页、模型卡、作者CSV及配置源码。人工复核：未进行。**

本包支持[公开模型比较](../../models/public-benchmark-review-2026-10-20.md)和[试点路线](../../pilots/final-pilot-roadmap-2026-10-20.md)。来源按原语言归档。模型卡修订及每份原件的URL、抓取时间、字节数和SHA-256在[retrieval-manifest](retrieval-manifest.json)、[additional-retrievals](additional-retrievals.json)、[supplement-retrievals](supplement-retrievals.json)、[AA retrievals](aa-retrievals.json)和[代码清单](code-manifest.json)。总文件哈希见[file-manifest](file-manifest.json)。

## 一手来源与可支持的论断

| 本包位置 | 发布方、标题、日期 | 原始入口与核对位置 | 支持的范围 |
|---|---|---|---|
| `modelcards/qwen27/` | Qwen，Qwen3.8-27B模型卡；本次固定修订 | [卡片](https://huggingface.co/Qwen/Qwen3.8-27B)，Benchmark Results／脚注 | 发布方报告的代码、多模态与工具分数，默认thinking与262K原生窗口 |
| `modelcards/deepseek/` | DeepSeek，DeepSeek-V4.1-Flash模型卡；本次固定修订 | [卡片](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)，Instruct／跨scaffold表 | effort100、各harness及原版模型自报分数；不覆盖1017版本 |
| 其余八项`modelcards/` | Google、Qwen、z.ai、Moonshot、Xiaomi；本次固定修订 | 各API元数据的repo与SHA | Gemma／Qwen35／GLM／Kimi／MiMo对照及当前卡片快照 |
| `benchmarks/extractbench/` | LlamaIndex／基准作者，ExtractBench；当前仓库修订 | [README](https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/README.md)、[CSV](https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/leaderboard.csv) | 相同370文档、分长度value F1；金融域145份；宏平均和证据F1的区别 |
| `benchmarks/extractbench/files/` | 同上，pipeline与provider源码 | [固定源码](https://github.com/run-llama/ExtractBench/blob/56b8fdd91b2cf3648caf75c717c68441ecf4d43f/src/extract_bench/inference/pipelines/extract.py) | 精度标签、图像DPI、端点、输出预算与thinking；是公开实现设置，不是每次历史运行日志 |
| `benchmarks/vals-fabv2/` | Vals AI，Finance Agent v2；页面更新2026-10-18 | [作者榜](https://www.vals.ai/benchmarks/fabv2)，模型表／Methodology | 同默认harness的金融研究得分；927题构成说明、六工具、两小时、partial credit与all-pass定义 |
| `benchmarks/vals-*/` | Vals AI，模型单页、旧v1.1、CorpFin v2及主页 | [v1.1](https://www.vals.ai/benchmarks/finance_agent)、[CorpFin](https://www.vals.ai/benchmarks/corp_fin_v2) | 版本和历史引用核对；旧分数不拼入当前v2表；仅已检查的当前表用于结论 |
| `benchmarks/aa-*/` | Artificial Analysis，模型对照页与Intelligence Benchmarking；2026-10-20快照 | [方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)，AA-LCR v1.1／AutomationBench-AA／Terminal-Bench4 | 同名分项比较；保留推理标签、100K多文档任务、工具分工与重复次数；SciCode标Under review |
| `benchmarks/bizbench-paper/` | 基准作者，BizBench v1，2026-10-14 | [arXiv HTML v1](https://arxiv.org/html/2610.20424v1)，§5表1、§5.2、附录D | Qwen27／DeepSeek／GLM Flash同50任务×3次；目标与严格成功，过程条件与pass^3 |
| `benchmarks/bizbench/` | 基准作者，BizAgentBench；当前HEAD `51e737f...` | [仓库](https://github.com/ant-intl/BizAgentBench)，运行说明与配置模板 | 输出上限、90分钟和错误阈值、评分定义；模板不证明所有模型使用相同参数 |
| `benchmarks/rele/` | NoneLinear ReLE，中文金融知识榜；README标v5.12.7／2026-10-15 | [作者榜](https://github.com/jeinlee1991/chinese-llm-benchmark/blob/main/leaderboard/金融基础知识.md) | 中文金融知识补充；缺少逐行thinking／工具／harness／权重SHA，支持范围低于完整配置证据 |
| `benchmarks/deepswe/` | Datacurve，DeepSWE作者榜；页标2026-09-22 | [作者榜](https://deepswe.datacurve.ai/) | 调查harness与快照差异；当前页面未列DeepSeek4.1/Qwen27，未以其填主稿分数 |

## 模型卡修订与基准运行版本分开

十项模型卡的本次SHA见`retrieval-manifest.json`。这表示研究读取了哪个版本的官方说明，不能据此推断别人跑分使用的权重SHA。ExtractBench代码固定为`56b8fdd91b2cf3648caf75c717c68441ecf4d43f`，包含本次CSV和适配配置。API的`deepseek-flash`可移动，作者旧结果仍按CSV发布的原版标签引用；Finance Agent v2已将1017另列。

## 获取与质量说明

官方卡片、原始CSV、原始配置和所列主比较表均已打开并核对，证据状态为**verified-primary**；发布方自报代表其报告内容，不等同于独立复现。ReLE同样为基准作者一手维护，但设置披露较少，作为补充。

`source.html`保存网页原字节。Defuddle生成部分原语言阅读副本；动态排行榜可能未进入其正文抽取，故跑分以原始HTML表格的机械提取CSV或作者CSV为准。ExtractBench官网只返回应用壳，网页数据未作为跑分原件，实际采用作者仓库CSV。两项GitHub API树请求返回403，记录为获取失败；随后通过公开Git仓库固定修订和已检查源码取得需要的配置，未将失败响应当作原文。

全部处理为公开网页和代码的读取／归档，未运行上游代码，未调用模型、付费API或GPU。报告中的pilot评分、人日、费用和任务量是本项目分析情景，来源包不为其背书。
