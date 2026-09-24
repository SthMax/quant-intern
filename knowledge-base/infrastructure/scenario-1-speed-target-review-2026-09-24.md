# 场景一选型复核：四配置、FP8权重与完整精度KV

**2026年9月24日更新。** 四配置分析现已合并到[场景一完整方案](scenario-1-personal-agent-2026-09-24.md)，作为Markdown与PDF的统一正文。

当前候选为单RTX PRO 6000D、双6000D TP2、M5 Ultra 256GB和DGX Spark；统一Qwen3.8-27B、FP8权重、BF16／FP16 KV，主要保证单人20+ token/s。完整方案列出整机人民币预算、131K／262K／524K生成速度、KV与状态容量，以及冷prefill与缓存续跑。

## 计算记录

- [现行四配置数据与BOM](data/scenario-1-personal-agent-2026-09-24/four-hardware-comparison.json)
- [现行复算入口](data/scenario-1-personal-agent-2026-09-24/compare_four_hardware.py)
- [一手资料与MLX MXFP8源码记录](../sources/TECH-075/four-hardware-evidence.md)
- [历史混合硬件／8-bit KV筛选](data/scenario-1-personal-agent-2026-09-24/speed-target-review.json)：用户固定完整精度KV后已被现行比较替代。
