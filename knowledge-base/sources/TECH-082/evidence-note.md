# Qwen长上下文与前缀缓存核查

- 来源ID：TECH-082
- 检查日期：2026-10-12
- 检查人：Codex部署研究agent；静态资料／数据／代码检查
- 人工复核：pending，未宣称完成
- 证据身份：发行者原文或原始公开结果；本项目推导另标分析

## 已检查

固定vLLM a281ad32f0368caa2c6ebe38a0e59a75b3f22392及recipes 21302fdc7506d180d2e4f37beeabc6836bd6d50d。APC文档、cache_config、Qwen recipe已读。align只在合适边界留线性层状态，shared-prefix checkpoint有MTP与prefix-match-unit条件；chunked prefill的吞吐与decode延迟存在权衡。

## 适用边界

朋友测试的安装revision仍待environment.json；当前主线功能说明不等同其安装版本。固定模型权重FP8与KV精度分别记录，不能拿FP8 KV结果证明BF16 KV速度。

原URL、固定revision和SHA-256见[metadata.json](metadata.json)。
