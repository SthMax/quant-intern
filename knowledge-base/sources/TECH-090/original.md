# TECH-090｜三年TCO所用官方API与硬件原文

**获取与核对日期：2026年10月20日。** 本文件是来源索引；以下英文文件为网页原语言文本提取，中文成本分析另存于[三年TCO研究](../../infrastructure/tco-analysis-2026-10-20.md)。原始HTML未取得；提取工具、失败路径、字节数与SHA-256均在[metadata](metadata.json)。

| 原文文件 | 发布方与用途 |
|---|---|
| [DeepSeek Models & Pricing](deepseek-pricing.md) | deepseek-flash对应V4.1-Flash-1017，USD／百万token高低峰、缓存／未缓存输入和输出价格 |
| [DeepSeek Context Caching](deepseek-cache.md) | 精确前缀、输入及输出边界持久化、usage字段与best-effort命中 |
| [DeepSeek First API Call](deepseek-first-call.md) | 官方入口、模型名称与1017版本映射 |
| [DeepSeek Rate Limit & Isolation](deepseek-rate-limit.md) | 并发限额及user_id隔离；不等于延迟SLA |
| [Claude Pricing](claude-pricing.md) | 一方API全球默认、Sonnet5.5、缓存写读、1M标准价、地域附加价 |
| [Claude Prompt Caching](claude-cache.md) | 5分钟／1小时TTL、精确匹配与cache计数口径 |
| [Claude Sonnet 5.5](claude-sonnet55.md) | claude-sonnet-5-5、发布日期、context与分词器条件 |
| [NVIDIA Spark Hardware](spark-hardware.md) | 240W随附电源、140W SoC TDP；不是墙插实测 |
| [Anthropic Supported Regions](anthropic-regions-future.md) | **页面标注2026-11-12生效，晚于本研究截止日，只保留时效核查记录，不用于断言10月20日现行政策。** |

[TECH-092时效核验包](../TECH-092/original.md)补充1017开放权重、当前DeepSeek开放平台协议与2025年Anthropic销售限制；W2正文已读取并采用这些原文，11月12日新政策仍保持未来生效身份。

本包不包含厂商报价单、金融任务质量评测或GPU实测。硬件预算沿TECH-085、TECH-087及10月12日价格台账；Spark外部测试沿TECH-076，公司公开回放沿TECH-084。
