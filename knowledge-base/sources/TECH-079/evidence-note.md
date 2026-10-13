# DeepSeek官方制品容量核查

- 来源ID：TECH-079
- 检查日期：2026-10-12
- 检查人：Codex部署研究agent；静态资料／数据／代码检查
- 人工复核：pending，未宣称完成
- 证据身份：发行者原文或原始公开结果；本项目推导另标分析

## 已检查

HF revision 5254448103b6254fc646dacbca1cbbf20e9216c1。config.json的text_config和量化字段、index metadata.total_size已逐项读出。总制品510286023000B；Engram按两层rows×(256+8)为202758032400B；非Engram307527990600B。原生官方制品是FP4专家＋FP8 dense，不重标为全FP8。552B仅backbone；Engram与DSpark另计。

## 适用边界

只下载README、config、index与参考代码，没有下载权重，没有执行参考kernel。磁盘tensor大小不直接等于GPU常驻量。

原URL、固定revision和SHA-256见[metadata.json](metadata.json)。
