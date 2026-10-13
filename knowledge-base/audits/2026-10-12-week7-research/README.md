# 第7周研究整合检查｜2026年10月12日

本记录覆盖三条并行研究与主agent的价格／来源整合。研究报告、计算和原件分别归入`infrastructure/`、`infrastructure/data/`、`sources/TECH-xxx/`；完整上游克隆仅在忽略跟踪的`.research-workspace/repos/`。

## 交叉核对结果

- [来源索引](../../reading-index.json)：211个唯一ID，192主阅读、15辅助、4来源链；TECH-086预留未使用。
- TECH-076–085及087共171项登记文件SHA-256与原件一致；原始代码、章节和日志保持来源语言。
- [部署计算](../../infrastructure/data/week7-deployment-2026-10-12/validation.json)：280行公司容量、24行Spark状态／精度情景；131K／262K／512K／1M均含8K输出预留。
- [A100审查](../../infrastructure/data/deepseek-a100-project-2026-10-12/audit-results.json)：43个来源文件、30组缓存、11条prefill主张、8条并发主张、4条Jev公式复算。
- [Book复算](../../infrastructure/data/ai-infra-book-2026-10-12/validation.json)：23项算术与来源一致性检查，四行Spark及八行DeepSeek资源情景。
- [整机费用](../../infrastructure/data/hardware-prices-2026-10-12.json)：四组预算公式与逐项金额一致，汇率／税／支持准备为明确的分析输入。
- 作者研究稿的本地链接有效；新增候选文件的常见凭据模式检查无命中，研究稿无机构关联名称。
- 四份已发布PDF与当前HEAD逐字节相同；其来源hash保留为9月24日快照，新Markdown的变化单独记录。

## 复核中形成的修订

1. CED bounded replay是模型设计中的有意近似。A100专项区分这一机制、README对decoder结构的错误描述，以及定制边界／权重质量待验证事项。
2. 三条研究统一DeepSeek的890 B/token逻辑布局与当前Hopper 1,827 B/token/rank页载荷；容量主表使用真实启动池，保留post-graph预算敏感性。
3. 10%余量指token工作集准入；预分配池没有因此释放物理内存。等待工具的会话继续计入驻留工作集。
4. A100价格对应八卡SXM翻新整机，作者性能主要来自四卡PCIe，分别保留形态与拓扑。
5. Spark的原BF16 KV要求与FP8 KV＋MTP3实测分开；冷曲线差分标为热prefill分析，p95留待实测。
6. Jev默认计时公式与实测路径分别记录；公开InferenceX回放的合成DSpark接受率、缓存输入和输出吞吐分别呈现。

主agent完成来源／代码和计算交叉核对。人工复核仍为pending；本轮没有新增GPU运行、真实任务质量评测或交易报价。检查明细见[validation.json](validation.json)。新的Beamer及逐页检查列于[周计划](../../../weekly/week-07-plan.md)。
