# vLLM缓存与发布路径核查

- 来源ID：TECH-080
- 检查日期：2026-10-12
- 检查人：Codex部署研究agent；静态资料／数据／代码检查
- 人工复核：pending，未宣称完成
- 证据身份：发行者原文或原始公开结果；本项目推导另标分析

## 已检查

固定vLLM a281ad32f0368caa2c6ebe38a0e59a75b3f22392；recipe 21302fdc7506d180d2e4f37beeabc6836bd6d50d。attention.py:92–101为index布局；124–130、512–522为Hopper packed584与576页对齐；1138–1170及1206–1245为source cache spec（每rank一份latent/index）。sparse_mla.py:125–127支持SM90/100，sparse_indexer.py:117–124的sparse-logits路径仅SM100。Hopper ratio2/ratio1页合计1827B/input-token/rank，为逐页静态载荷；总pool以TECH084日志为准。

## 适用边界

旧recipe内H100约36GiB、H20038.5GiB池为概略描述；具体公开profile日志已显示49.20GiB H100加载、35.16GiB H200TP4池。Engram23.6GiB/rank是每层，两层要相加。V4.1路径需要nightly；主线代码存在不等于在本项目机器运行。

原URL、固定revision和SHA-256见[metadata.json](metadata.json)。
