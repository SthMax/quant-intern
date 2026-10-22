# TECH-092 来源目录：最终成稿时效核验

**本文件是作者编写的来源目录，不是原文翻译。** 原语言正文、原始字节与机械提取分别保存在下列文件；精确URL、获取时间、最终URL、字节数和SHA见[retrieval-manifest.json](retrieval-manifest.json)、[补充获取记录](retrieval-extra.json)及[file-manifest.json](file-manifest.json)。核验本地日期2026-10-20；获取UTC时间可为10月19日17–18时，对应上海次日凌晨。

| 类别 | 原文入口 |
|---|---|
| 模型制品／许可 | [12项模型与修订](model-revisions.json)；[Qwen27 FP8许可](models/qwen27fp8/LICENSE)；[DeepSeek原版](models/deepseek/README.md)、[1017](models/deepseek1017/README.md)；[GLM主模型许可](models/glm/LICENSE)、[Flash](models/glmflash/LICENSE)；[Kimi许可](models/kimi/LICENSE)；[MiMo Flash](models/mimoflash/README.md)、[Pro](models/mimopro/README.md)；[Gemma4本版许可](models/gemma-apache2.md) |
| 引擎及缓存 | [vLLM0.32 release API](engines/vllm-v032.json)、[许可](engines/vllm-v032-LICENSE)；[LMCache DeepSeek recipe](engines/lmcache-deepseek.md)、[Qwen recipe](engines/lmcache-qwen.md)、[许可](engines/lmcache-LICENSE) |
| API版本及条款 | [DeepSeek1017公告](api/deepseek-1017-news.md)、[定价](api/deepseek-pricing.md)、[开放平台协议](api/deepseek-open-platform-terms.md)、[隐私](api/deepseek-privacy.md)；[Anthropic2025限制公告](api/anthropic-sales-2025.md)、[现行商业条款](api/anthropic-commercial.md)、[11/12未来地区政策](api/anthropic-regions-future.md) |
| 商业软件 | [Onyx价格](software/onyx-pricing.md)、[核心许可](software/onyx-LICENSE)、[企业许可](software/onyx-ee-LICENSE)、[OpenWebUI许可](software/open-webui-LICENSE) |
| 硬件价格 | [Spark官方可读正文](hardware/spark-store.md)、[规格](hardware/spark-spec.md)；[A100原HTML](hardware/a100-serverstore.html)；[H100](hardware/h100-exxact.md)、[H200](hardware/h200-exxact.md)；[H200NVL原HTML](hardware/h200-nvl-vipera.html) |
| 出口及供货 | [正式BIS规则PDF](hardware/bis-2026-00789.pdf)、[机械提取](hardware/bis-2026-00789.md)；[eCFR742.6](hardware/ecfr-742-6.md)；[NVIDIA10-Q PDF](hardware/nvidia-2027-q2-10q.pdf)、[机械提取](hardware/nvidia-2027-q2-10q.md) |
| 监管原文 | [证监会IT办法](regulation/csrc-it-management.md)、[218令PDF](regulation/csrc-cyber-218.pdf)、[条文提取](regulation/csrc-cyber-218.md)；[个保法](regulation/pipl.md)、[2025修正网络安全法](regulation/cybersecurity-2025.md)、[网络数据条例](regulation/network-data-security.md)、[跨境规定](regulation/cross-border.md)、[生成式AI暂行办法](regulation/genai-measures.md) |
| 行业团体标准 | [AMAC发布公告](regulation/amac-announcement.md)、[标准PDF](regulation/amac-t0004-2026.pdf)、[条文提取](regulation/amac-t0004-2026.md) |

HTML优先由Defuddle从已保存原HTML机械提取；PDF由pypdf提取并保留物理页标记。提取可能遗漏布局、隐藏选项、发布日期或动态内容，原HTML／PDF优先。A100隐藏价格选项读取原HTML，不能只用简化正文。Spark原HTML超时，可读正文由官方URL的Exa提取并与web.run打开的页面核对，明确不声称取得其原HTML。

补充的完整原语言文本保留了简化提取遗漏的日期和复杂编号：[eCFR742.6全文](hardware/ecfr-742-6-fulltext.txt)、[Anthropic未来政策日期](api/anthropic-regions-future-fulltext.txt)、[商业条款及日期](api/anthropic-commercial-fulltext.txt)、[A100可见文字](hardware/a100-serverstore-fulltext.txt)、[H200NVL可见文字](hardware/h200-nvl-vipera-fulltext.txt)。这些文件由HTMLParser机械提取，原HTML仍保留完整属性与选项。

[证据与边界说明](evidence-note.md) · [研究分析](../../infrastructure/final-source-refresh-2026-10-20.md)
