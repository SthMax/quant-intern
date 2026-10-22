# TECH-089 — 最终汇报版本与缓存支持原文索引

此文件是**作者编写的来源导航**，不是原文摘录或翻译。以下链接文件保留英文原文／官方源码；研究结论单独见[证据说明](evidence-note.md)和[三场景最终核对](../../infrastructure/final-configurations-2026-10-20.md)。

读取日期：2026-10-20，Asia/Shanghai。已执行agent原文与源码检查，未完成独立人工复核；未做GPU执行。

## vLLM官方固定release与源码

| 文件 | 上游与定位 |
|---|---|
| [0.30发布原HTML](vllm-0.30-release.html)／[机械提取正文](vllm-0.30-release-original.txt) | [v0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0)，2026-09-22；Model support：DeepSeek-V4.1-Flash进入release |
| [0.31发布原HTML](vllm-0.31-release.html)／[机械提取正文](vllm-0.31-release-original.txt) | [v0.31.0](https://github.com/vllm-project/vllm/releases/tag/v0.31.0)，2026-10-05；Engram host tables shared across co-located DP replicas |
| [0.32发布原HTML](vllm-0.32-release.html)／[机械提取正文](vllm-0.32-release-original.txt) | [v0.32.0](https://github.com/vllm-project/vllm/releases/tag/v0.32.0)，2026-10-18；latest于10/20指向此版；Breaking changes中的max_tokens和mamba all |
| [0.31 Engram指南](vllm-0.31-engram.md) | [固定tag原文](https://github.com/vllm-project/vllm/blob/v0.31.0/docs/features/engram.md)；Sharing host tables across DP replicas |
| [0.32 Engram指南](vllm-0.32-engram.md)／[配置源码](vllm-0.32-engram-config.py) | [固定tag原文](https://github.com/vllm-project/vllm/blob/v0.32.0/docs/features/engram.md)；dp_shared_memory、cpu_offload、embedding_across_dp及条件 |
| [0.31 attention.py](vllm-0.31-attention.py)／[0.32 attention.py](vllm-0.32-attention.py) | [0.32固定源码](https://github.com/vllm-project/vllm/blob/v0.32.0/vllm/models/deepseek_v41/attention.py)；92–173、506–524等，GPU架构、记录字节与页对齐 |
| [0.32 KV offloading指南](vllm-0.32-kv-offloading.md) | [固定tag原文](https://github.com/vllm-project/vllm/blob/v0.32.0/docs/features/kv_offloading_usage.md)；CPUOffloadingSpec、TieringOffloadingSpec、总worker主存额度、FS／对象存储 |
| [0.32 hybrid cache设计](vllm-0.32-hybrid-cache.md) | [固定tag原文](https://github.com/vllm-project/vllm/blob/v0.32.0/docs/design/hybrid_kv_cache_manager.md)；仅作设计背景，其中Mamba支持描述存在历史性，模型recipe优先核验 |

## LMCache当前dev原文

本轮`git ls-remote`解析`dev`为**64b05b8af88d5fc13b375cdc06b5425cd56dea47**。下列四份rst先下载dev，再请求固定commit验证逐字节相同；因此具备固定版本与SHA-256。它们证明文档所报告的验证范围，不证明任意pip版本或本项目精度／MTP组合已运行。

- [Qwen系列recipe](lmcache-qwen-series.rst)：[固定commit](https://github.com/LMCache/LMCache/blob/64b05b8af88d5fc13b375cdc06b5425cd56dea47/docs/source/recipes/qwen3_5.rst)。Validated models列Qwen3.8-27B单GPU；align、分组、块N与2N−1调度说明；文本验证与实验性限制。
- [DeepSeek V4.1 recipe](lmcache-deepseek-v41.rst)：[固定commit](https://github.com/LMCache/LMCache/blob/64b05b8af88d5fc13b375cdc06b5425cd56dea47/docs/source/recipes/deepseek_v41_flash.rst)。八GPU、多geometry、scratch重算；MTP尚未验证；架构记录不可直接共享；“未有tagged vLLM”提示已被release事实超越。
- [Hybrid models](lmcache-hybrid-models.rst)：[固定commit](https://github.com/LMCache/LMCache/blob/64b05b8af88d5fc13b375cdc06b5425cd56dea47/docs/source/mp/hybrid_models.rst)。GDN递归／卷积状态作为opaque页，object-group分离；正确性以得分而非逐token完全相同为目标。
- [Quickstart](lmcache-mp-quickstart.rst)：[固定commit](https://github.com/LMCache/LMCache/blob/64b05b8af88d5fc13b375cdc06b5425cd56dea47/docs/source/getting_started/quickstart.rst)。MP mode recommended与独立server。
- [L2存储原HTML](lmcache-l2-storage.html)／[机械提取文字](lmcache-l2-storage-original.txt)：[官方网页](https://docs.lmcache.ai/mp/l2_storage.html)，动态文档，按读取字节和hash冻结；异步store、prefetch及文件／块等backend。未由本包将该网页映射到特定源码commit。

## 取得方式与失败响应

[retrieval.json](retrieval.json)保存逐文件请求URL、最终URL、响应、字节、SHA-256与固定commit核验；[metadata.json](metadata.json)给出整体证据状态。`retrieval-response-*`是错误路径取得的404原响应，**不是可引用原文**。GitHub API曾返回速率限制，正式引用采用成功取得的release HTML与固定tag原文。没有绕过付费墙或访问任何私有模型制品。
