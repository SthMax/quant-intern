# TECH-091 原语言来源导航：公开模型评测

**本文件是作者编写的来源导航，不是原文摘录或翻译。** 以下文件保留发布方模型卡、基准作者原文、HTML、CSV及源码；可比较范围与研究判断单独见[证据说明](evidence-note.md)和[公开评测研究](../../models/public-benchmark-review-2026-10-20.md)。访问日期为2026-10-20，Asia/Shanghai；人工复核尚未进行。

## 模型发布方原文

[Qwen27](modelcards/qwen27/original.md) · [Qwen35](modelcards/qwen35/original.md) · [DeepSeek原版](modelcards/deepseek/original.md) · [Gemma31B](modelcards/gemma31/original.md) · [Gemma26B](modelcards/gemma26/original.md) · [GLM](modelcards/glm/original.md) · [GLM Flash](modelcards/glmflash/original.md) · [Kimi](modelcards/kimi/original.md) · [MiMo Flash](modelcards/mimoflash/original.md) · [MiMo Pro](modelcards/mimopro/original.md)。各目录的`api.json`及[获取清单](retrieval-manifest.json)保留仓库、修订和精确URL；当前模型卡SHA不代表历史评测运行SHA。1017新增制品核对见[TECH-092](../TECH-092/original.md)。

## 基准作者原文与数据

| 来源 | 本地原文入口 | 原始发布入口 |
|---|---|---|
| Finance Agent v2 | [原语言提取](benchmarks/vals-fabv2/original.md)、[原HTML](benchmarks/vals-fabv2/source.html) | [Vals AI](https://www.vals.ai/benchmarks/fabv2) |
| CorpFin v2 | [原语言提取](benchmarks/vals-corpfinv2/original.md) | [Vals AI](https://www.vals.ai/benchmarks/corp_fin_v2) |
| ExtractBench | [作者README](benchmarks/extractbench/readme.md)、[榜单CSV](benchmarks/extractbench/leaderboard.csv)、[配置源码清单](code-manifest.json) | [固定仓库修订](https://github.com/run-llama/ExtractBench/tree/56b8fdd91b2cf3648caf75c717c68441ecf4d43f) |
| Artificial Analysis | [模型对照原语言提取](benchmarks/aa-deepseek-qwen/original.md)、[方法原HTML](benchmarks/aa-methodology/source.html) | [Intelligence Benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) |
| BizBench v1 | [论文原语言提取](benchmarks/bizbench-paper/original.md)、[原HTML](benchmarks/bizbench-paper/source.html)、[实现README](benchmarks/bizbench/readme.md)、[配置模板](benchmarks/bizbench/config-template.json) | [arXiv v1](https://arxiv.org/html/2610.20424v1)、[作者仓库](https://github.com/ant-intl/BizAgentBench) |
| ReLE | [作者README](benchmarks/rele/readme.md) | [中文金融知识榜](https://github.com/jeinlee1991/chinese-llm-benchmark/blob/main/leaderboard/金融基础知识.md) |
| DeepSWE | [原HTML](benchmarks/deepswe/source.html) | [作者榜](https://deepswe.datacurve.ai/) |

原HTML／作者CSV优先于可能遗漏动态表格的简化提取。作者配置模板与实际历史运行参数分别处理；缺少逐模型thinking、工具或权重修订的来源据实保留缺口。

[元数据](metadata.json) · [主获取记录](retrieval-manifest.json) · [补充记录](additional-retrievals.json) · [第二组补充](supplement-retrievals.json) · [AA获取记录](aa-retrievals.json) · [文件哈希清单](file-manifest.json)。
