# 模型与本地部署研究

本目录服务于Phase 2：开放模型比较、部署资源研究与本地GPU原型。

## 当前研究

- [2026-09-16模型研究](model-survey-2026-09-16.md)：按用户反馈重做8项核心候选，个人机以27B/35B及相近规模Gemma起步，共享服务纳入DeepSeek、GLM与Kimi；未来型号单列。尚无本地性能或金融任务测试。
- [模型许可专项](license-review-2026-09-16.md)：逐项核对Apache、MIT及GLM-5.3/Kimi K3自定义许可，分析集团关联方、商业用途、内部使用与分发边界。
- [第3–5周研究主计划](../../weekly/week-03-05-plan.md)：模型研究为三周主线；行业报告修订按独立fixing plan推进。
- [Serving framework调研](../infrastructure/serving-framework-survey-2026-09-17.md)与[Harness调研](../infrastructure/harness-survey-2026-09-17.md)：2026-09-17补充模型服务、硬件路径、应用运行环境和协议兼容性。

## 技术资料

- [DeepSeek-V4.1-Flash技术报告与中文架构分析](deepseek-v4.1-flash/README.md)：2026-09-11归档，包含两份原始PDF、按页文本与文件校验记录。
- [本地LLM应用证据与原型设计](local-llm-poc-evidence-2026-09-09.md)。

## 工作计划

- [模型比较与金融文本测试](benchmark-plan.md)
- [本地GPU原型](poc-plan.md)
