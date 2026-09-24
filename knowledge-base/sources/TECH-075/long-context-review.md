# 长上下文复核：2026年9月24日

本页为研究者核对笔记，原文与推断分别标明。

- [Qwen3.8-27B官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)：262,144为原生输入加输出窗口；超出时说明YaRN配置，明确举例524,288适合factor=2.0。既有完整原文见[TECH-070](../TECH-070/qwen27/original.md)。
- [Qwen3.6-35B-A3B官方模型卡](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)：同样说明原生262,144及524,288/factor=2.0例子；[既有FP8卡原文](../TECH-070/qwen35/original.md)亦含配置。
- [MLX Qwen模型](mlx-qwen.py)将rope_parameters转入rope_scaling；[QwenNext注意力](mlx-next.py)将该配置传给initialize_rope；[RoPE实现](mlx-rope.py)包含YaRN分支。**代码路径核对**支持作为扩展测试路线，本轮未执行524K模型。
- [llama.cpp服务原文](llama-server.md)列有rope-scaling、rope-scale、yarn-orig-ctx、每slot context及checkpoint参数。三路524K必须核对每个slot都得到对应长度。
- [llama.cpp问题27090](https://github.com/ggml-org/llama.cpp/issues/27090)：2026-08-14用户报告Windows CUDA b10430/b10434、Qwen3.8-27B UD-Q8_K_XL、YaRN×4约520K prefill退出；同文记录×2下444K输入完成。9月24日页面仍Open。该报告用作版本回归样本，范围限定到记录的配置，不据此判定所有后端或当前版本。

本场景将131,072／262,144作为原生档，524,288作为独立YaRN×2档。容量满载包含8,192输出tokens；冷装载和精确前缀续跑分开。主内存预算另预留每会话8份额外GPU状态检查点，0和32份单列，属于工程准备假设。
