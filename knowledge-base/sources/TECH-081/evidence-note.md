# SGLang V4.1支持边界核查

- 来源ID：TECH-081
- 检查日期：2026-10-12
- 检查人：Codex部署研究agent；静态资料／数据／代码检查
- 人工复核：pending，未宣称完成
- 证据身份：发行者原文或原始公开结果；本项目推导另标分析

## 已检查

固定279f1fad907dd53044a7b68fcc45bd6a24467c9e。常规NVIDIA cookbook用dev-dsv41；简单硬件列表没有H100，但同日AgentX归档已有H100 TP8+EP8固定镜像/PR，需以具体证据入口和日期说明。AgentX记录注明synthetic-acceptance，goldenAL=3.51；HiCache一些开关从其他硬件配置移植，不能全部标成目标硬件实测。

## 适用边界

未执行preview镜像；不将V4 benchmark误认为V4.1；不把正文中已经过时的支持列表当成当前全部能力，也不把新增recipe当真实1M并发质量证据。

原URL、固定revision和SHA-256见[metadata.json](metadata.json)。
