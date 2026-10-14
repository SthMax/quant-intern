# A100原生权重与modified vLLM对照来源

**读取日期：2026年10月14日。** 本页是研究者编写的来源索引；下面链接的文件保存原语言正文、代码或公开页面提取。分析见[A100专项](../../infrastructure/deepseek-a100-project-review-2026-10-12.md)。

| 来源 | 本地原文 | 支持的内容 |
|---|---|---|
| shi3z，9月12日文章 | [公开部分](shi3z-0912-public.md) | 33→673的标题、正文单路／并行数字、早期开发过程；付费续篇未读取 |
| shi3z，9月17日续文 | [公开部分](shi3z-0917-public.md) | 原目标为同prompt大量生成，随后接入Coding Agent，处理长输入和状态问题；付费续篇未读取 |
| shi3z固定仓库 | [bench_vllm.sh](shi3z-bench-vllm.sh) | 这个脚本实际测试Qwen27，不能补足DeepSeek同机引擎比较 |
| Tokha233 vLLM适配项目 | [README](tokha-readme.md)、[测试方法](tokha-benchmark-method.md)、[逐次消融](tokha-ablation.md)、[补丁清单](tokha-patch-manifest.json) | 单机8×A800，78–90输入／1,024输出，C1–C256；同机dense与EP8两项增量优化 |
| keplerzip A100部署 | [性能报告](kepler-performance.md)、[实现版本](kepler-architecture.md) | 历史TP8、DSpark5的八卡A100短请求操作者回传结果；当前新版本与历史数据分开 |
| wtdcode vLLM backport | [README](backport-readme.md) | Ampere适配、FULL Graph、并行与低位执行；该分支仍将V4.1列为WIP，具体可运行组合来自特定补丁配置 |
| vLLM官方实现 | [CUDA Graph设计](vllm-cuda-graphs.md)、[MXFP8 Marlin源码](vllm-marlin-mxfp8.py) | 成熟框架已有的图捕获与SM80 W8A16能力 |

原URL、文件哈希、提取方式见[metadata](metadata.json)。本组用于解释技术归属和公开性能范围；没有同一台四卡机器上的shi3z与modified vLLM成对测速。公司选择modified vLLM属于结合维护和运行需求的方案决定。人工复核pending。
