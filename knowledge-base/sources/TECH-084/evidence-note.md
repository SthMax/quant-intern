# InferenceX测量口径及日志核查

- 来源ID：TECH-084
- 检查日期：2026-10-12
- 检查人：Codex部署研究agent；静态资料／数据／代码检查
- 人工复核：pending，未宣称完成
- 证据身份：发行者原文或原始公开结果；本项目推导另标分析

## 已检查

API返回220行，H100/H200有50行；本项目选5条vLLM回放对照，取3个启动日志前段。原始serverLog明确synthetic DSpark acceptance length3.51，Engram host、FP8 MLA/index、模型加载、KVGiB与pooltokens。H100-C20 pool6435008，H200TP4-C32 pool18326608，H200TP8-C32 pool29497836。

## 适用边界

AgentX并发是活动会话而非固定同时decode数；输入长度分布不同、GPUcache约94–96%命中。total_tput包含缓存输入；仅output_tput才是生成输出。p95是该回放分布，不是每人1M热续跑p95。post-graph内存建议比预分配pool小，10%token余量不能等同物理显存释放。API快照与日志运行时间分别保留。

原URL、固定revision和SHA-256见[metadata.json](metadata.json)。
