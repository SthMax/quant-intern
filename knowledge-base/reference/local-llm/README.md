# 外部本地LLM实现与评价参考

> 用户已排除以旧模型为中心的选型路线：此目录的AlphaFin/FinGPT资料仅作历史存档，不再推荐ChatGLM2方案。2026参考见[新目录](../2026-llm-quant/README.md)。AlphaQT-Bench是2026评价参考，仍可单独使用。

本目录提供可复用技术参考，不计为公募公司部署案例或公司4/5分数量。论文中的成绩为作者实验，不是实习机构本地测量。[研究结论与具体PoC候选](../../models/local-llm-poc-evidence-2026-09-09.md)。

| 材料 | 原件／代码 | 本地与证据边界 |
|---|---|---|
| AlphaQT-Bench，ACL 2026 | [论文PDF](alphaqt-bench/source.pdf) · [提取](alphaqt-bench/original.md) · [元数据](alphaqt-bench/metadata.json) | 金融因子代码生成评价；有完整Prompt，原实验通过云平台调用，未找到完整公开基准代码包 |
| AlphaFin，LREC-COLING 2024 | [论文PDF](alphafin/source.pdf) · [提取](alphafin/original.md) · [元数据](alphafin/metadata.json) | ChatGLM2-6B＋LoRA本地加载与BGE/FAISS；训练配置不等同推理最低配置 |
| AlphaFin官方代码，`068d93e` | [README](alphafin-code/files/README.md) · [文件清单](alphafin-code/archive.json) · [本地QA实现](alphafin-code/files/src/stage2_financial_qa/webui/run.py) | 选取10份源码/文档/许可；不含模型权重、完整数据或预建索引，没有执行 |
| FinGPT指令微调基准 | [论文PDF](fingpt-paper/source.pdf) · [提取](fingpt-paper/original.md) · [元数据](fingpt-paper/metadata.json) | 外部金融NLP任务与历史模型基线 |
| FinGPT官方代码，`781a7c0` | [README](fingpt-code/files/README.md) · [SETUP](fingpt-code/files/SETUP.md) · [文件清单](fingpt-code/archive.json) | 选取8份文件，包括3个notebook；`notebook-code/`仅为代码阅读导出，非执行结果；发现基座/adapter不匹配示例，见研究结论 |

仓库源码与notebook字节按commit归档，阅读导出单独存储。代码许可、底座模型许可、adapter与数据许可分别看其原始来源；本轮未下载模型/完整数据、安装环境或调用推理API。
