# 四配置复核资料：FP8权重、完整精度KV

**读取日期：2026-09-24。** 本页为研究记录，保留原文链接和证据范围。

| 来源 | 观察与用途 |
|---|---|
| [MLX quantize官方API](https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.quantize.html) | MXFP8采用E4M3数值、32值共享E8M0尺度；与affine整数格式分别定义。 |
| [MLX-LM utils固定修订](https://github.com/ml-explore/mlx-lm/blob/15bcf8b929e5da67aa7f8fe6feda7fb9eda00050/mlx_lm/utils.py) | 原样保存为[mlx-utils-fp8.py](mlx-utils-fp8.py)，MXFP8默认8bits／group32，loader识别mxfp8。官方Qwen制品quant_method=fp8另属一种格式，本轮采用从BF16转换路径。 |
| [MLX-LM convert固定修订](https://github.com/ml-explore/mlx-lm/blob/15bcf8b929e5da67aa7f8fe6feda7fb9eda00050/mlx_lm/convert.py) | 原样保存为[mlx-convert-fp8.py](mlx-convert-fp8.py)，标准--q-mode mxfp8入口；非量化层可保持BF16。未执行模型下载／转换，31GB为分析预算。 |
| [Apple中国技术规格](https://www.apple.com.cn/mac-studio/specs/) | M5 Ultra为1.2TB/s，256GB选项关联36核CPU／80核GPU。9月21日90,499元／2TB价格继续引用原台账。 |
| [Spark官方硬件说明](https://docs.nvidia.com/dgx/dgx-spark/hardware.html) | 128GB统一内存、273GB/s、20核Arm、1TB／4TB；240W电源随整机。 |
| [NVIDIA美国商城](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/) | 128GB／4TB，USD4,699，9月24日显示Out of Stock。人民币32,893元为7.00情景汇率换算；4–5万元是另列中国交付D预算。 |
| [NVIDIA调价公告](https://forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713) | 2026年2月公告从USD3,999调至4,699，OEM品牌另行定价。 |
| [HPE采购研究入口](../../infrastructure/server-gpu-procurement-2026-09-21.md) | 沿用已核84GB／1398GB/s、China/HK、被动散热和兼容服务器。单／双卡整机价格属新集成方案分析。 |
| [vLLM Qwen recipe](https://recipes.vllm.ai/Qwen/Qwen3.8-27B) | 官方FP8部署及原生MTP接入；5090为SM120路线，其他设备和短负载速度分开记录。 |
| [NVIDIA NIM支持矩阵](https://docs.nvidia.com/nim/vision-language-models/2.1.1-variant/support-matrix.html) | Qwen3.8-27B有RTX6000D／FP8／单GPU条目。表中GPU Memory为85GB；本项目按HPE84GB标称、十进制预算，最终以设备字节复算。 |
| [Spark测试作者原帖](https://forums.developer.nvidia.com/t/comprehensive-qwen3-8-27b-study-on-dgx-sparks-quantization-speculative-decoding-and-tp-dp-scaling/381102) | 作者2026-08-24发布；128输入／128输出、10轮，FP8权重＋FP8 KV，单流7.9token/s、MTP17.1。仅作短输入量级及提速路径参考。 |

本轮长context计算保留45%／60%／75%带宽敏感性。短输入约90%的权重读取效率不作为长context注意力的校准值。MTP在数值表关闭；后续实测启用时记录draft／验证额外内存与有效接受率。
