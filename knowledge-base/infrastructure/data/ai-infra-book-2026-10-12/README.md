# AI Infra Book阅读算例

固定书稿commit `3bdcb4fcab73010eeaccf31cc10a8242a895d82e`，来源TECH-078。此目录保存两个部署相关的**CPU资源复算**；没有GPU测试、模型下载或网络访问。

- `assumptions.json`：长度、输出预留、Qwen结构、朋友实测锚点及三种DeepSeek布局身份。
- `calculate.py`：仅Python标准库；从归档config／结果读取参数并独立算数，写本目录结果。
- `results.json`：4行Spark资源、8行DeepSeek驻留容量、权重组件与Agent资源示例。
- `validation.json`：23项公式／源结果对照，范围为算术和身份核对。

从仓库根目录执行：

```sh
python3 knowledge-base/infrastructure/data/ai-infra-book-2026-10-12/calculate.py
```

文件字节／GiB／GB分开；context是总长度，prefill输入减去8,192输出预留。Qwen表只计全注意力QK／PV矩阵工作，不当完整TTFT。DeepSeek生产890B/token、BF16参考3200B/token与当前Hopper裸1790／逐页对齐1827B/token（hybrid分组及其他池状态另计）分开；当前实现的来源由TECH-080提供。状态载荷不等于完整显存预算，操作数逻辑读取不等于实测HBM流量。朋友1M输出64token容量探针不参与稳定decode拟合。
