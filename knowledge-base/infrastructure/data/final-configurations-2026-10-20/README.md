# 最终三场景数据 — 2026-10-20

匿名研究数据，CPU本地复算；没有GPU执行、权重下载或付费API调用。

运行：`python3 knowledge-base/infrastructure/data/final-configurations-2026-10-20/recalculate.py`

主入口为`summary.json`（配置与预算）、`slide-data.json`（PPT页码映射）、`validation.json`（17项检查与输入hash）。CSV分别保存Spark精确测量与经验曲线、共享池份额、RAG容量与条件性能、公司严格预算容量、旧版本AgentX回放、服务目标反推、主存分区、传输条件算例及工具CPU教学数据。

数据身份不可互换：外部设备测量仍是原机器、精度、负载与引擎；拟合不是测量，传输与工程效率不是测量，服务目标不是设备预测。1M的64输出探针单独保留。`strict_uniform_memory_context_tokens`为纯内存均分结果，`admitted_context_cap_tokens`进一步取本项目1M应用上限。公司strict pool由公开已分配池按post-graph建议线性缩放，不是新启动实测；两TP4一律采用相同C32 profile。

10/12价格作为固定基线，场景二延用9月G3估算；新价格与交易可交付性另由采购研究维护。640GiB CPU缓存为使用既有1536GB主存的规划额度，不是额外购买640GiB内存。

来源原文在TECH-089及复用的TECH-070/076/079/080/084/085/087/088；研究解释在`../../final-configurations-2026-10-20.md`。原文、抓取失败响应和作者分析分开存放。
