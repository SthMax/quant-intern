# TECH-075：个人／三人模型与Coding Agent部署依据

**读取日期：2026年9月24日。** 官方文档与源码快照按原语言保存；量化制品采用发行者页面观察，精确tensor与完整制品hash尚未取得。价格继续引用9月21日硬件台账。

| 资料 | 本地入口 | 用途 |
|---|---|---|
| Codex配置参考 | [原文](codex-config.md) | 自定义provider、Responses接口及本地模型配置 |
| pi模型接入 | [原文](pi-models.md) | 本地模型与兼容端点 |
| MLX服务说明／源码 | [说明](mlx-server.md)、[源码](mlx-server.py) | 批处理条件、KV量化与串行退回、共享入口 |
| llama.cpp服务 | [原文](llama-server.md) | 多用户批处理、接口、上下文与检查点 |
| 苹果工作站规格 | [原页](apple-specs.html) | M5 Max／Ultra带宽与统一内存 |
| AMD统一内存推理 | [原页](amd-uma.html) | UMA分配及Qwen3.5相关实测对照 |
| NVIDIA工作站／GB10规格 | [RTX5000](rtx5000.html)、[Spark](spark.html) | 显存、带宽及平台结构 |
| 量化模型与OpenCode接入页面 | [观察记录](quantization-observations.json) | 发布者显示的体积、短修订号及接入能力；记录中保留直接URL |

OpenCode页面通过网页工具读取；本地原页请求返回403，未将观察笔记标作原文。量化页面同样区分显示值与向上取整的运行权重预算。模型结构和官方FP8制品沿用[TECH-070](../TECH-070/original.md)。

## 满上下文更新

[131K／262K／524K模型与引擎核对](long-context-review.md)补充官方YaRN×2路线、MLX代码路径及限定配置的回归样本。

## Qwen精度更新

当前个人与知识库方案统一主用Qwen3.8-27B，权重至少8-bit。[制品观察](quantization-observations.json)新增MLX8与GGUF Q8_0，先前4-bit观察放入已替代记录。MiMo精度另按官方制品和用户指定范围处理。

## 四配置与FP8格式复核

[单6000D、双6000D、M5 Ultra 256GB及DGX Spark的证据](four-hardware-evidence.md)补充MLX MXFP8主线源码与Spark准确品牌价格。当前选择保持BF16／FP16 KV，原8-bit KV速度筛选退为历史记录。
