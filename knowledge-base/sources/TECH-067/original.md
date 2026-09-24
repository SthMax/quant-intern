# MiMo-V2.6部署证据阅读入口

本文件是研究者编写的来源索引。链接文本保持原语言；各自URL与SHA-256见[metadata](metadata.json)。

- [vLLM Flash V2.6 recipe](vllm-flash.md)：4×H200、专用镜像、DFlash、工具解析。
- [vLLM Pro V2.6 recipe](vllm-pro.md)：8×H200及对应运行参数。
- [SGLang V2.5 cookbook](sglang-v25.md)：当前MiMo模型卡链接的旧版资料；其性能表对应V2.5。
- [vLLM最新发布](vllm-latest-release.json)：v0.30.0，2026-09-22。
- [SGLang最新发布](sglang-latest-release.json)：v0.5.20，2026-09-18。
- [PR #57784](vllm-pr-57784.json)、[改动文件](vllm-pr-57784-files.json)：2026-09-20合并。
- [v0.30.0 MiMo主干](v030-mimo_v2.py)、[Omni](v030-mimo_v2_omni.py)、[注册表](v030-registry.py)、[FP8／MXFP4入口](v030-fp8.py)：正式tag逐文件核对。
- [NVIDIA GLM-5.3资料](glm53-nvidia.md)：用于参数与架构对照；接口与托管配置按该来源自己的范围。

核验说明：9月22日recipe仍写stable≤0.29.0；本轮读取的v0.30.0 MiMo源码保留旧router和Omni类定义。部署研究采用包含PR关键改动的专用构建。上游commit比较API触发公开访问频率限制，原响应状态在metadata记录；源码对照独立完成。
