# Harness有效窗口核查

- 来源ID：TECH-083
- 检查日期：2026-10-12
- 检查人：Codex部署研究agent；静态资料／数据／代码检查
- 人工复核：pending，未宣称完成
- 证据身份：发行者原文或原始公开结果；本项目推导另标分析

## 已检查

Pi固定441f5767c4fe4eebbec6ebe9bb4a57f430871eba，OpenCode固定bcf23b6775c79a429b1511b255d6d88ab0248d4a。已读custom provider、context/output metadata、compaction与MCP配置文档。Pi默认reserve16384，contextWindow-reserve后压缩；OpenCode新旧文档schema有不同key，运行时按安装版schema固定。

## 适用边界

Hermes本轮尝试的原始路径返回404/429，未拿到新文档；沿用TECH072既有Hermes证据而不声称已重核其10月实现。文件中仅归档实际成功获取的Pi/OpenCode资料。

原URL、固定revision和SHA-256见[metadata.json](metadata.json)。
