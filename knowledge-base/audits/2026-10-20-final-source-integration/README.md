# 最终研究来源与入口整合检查

**核对日期：2026-10-20，Asia/Shanghai｜检查方式：agent本地文件、索引与SHA-256核对。** 未提交或发布。

TECH-089–092已正式登记到[source-register](../../source-register.md)与[reading-index](../../reading-index.json)。实际为216个唯一来源ID：197主阅读、15辅助、4来源链；两个全局文件的ID集合一致，无重复。原212条阅读记录逐条内容与顺序相对HEAD均未改变。仓库没有reading-index.md，本次没有额外生成另一份索引。

[知识库README](../../README.md)加入10/20配置、TCO、公开评测、试点及核验入口。reference-architecture及三份现行scenario只增加最新W1／W2／W4顶部入口；移除该新增行后，与HEAD原正文逐字节相同，旧数字与历史发布快照保持原文。

TECH-091原语言文件分散在模型卡、评测与源码目录。本次补充[original.md来源导航](../../sources/TECH-091/original.md)，明确标注为作者编写的目录；metadata补充主阅读与原文／证据说明入口，file-manifest同步这两份文件的当前哈希。发布方原文、作者CSV及配置源码均未改动。

| 检查 | 结果 |
|---|---:|
| 新增或修改的作者Markdown | 34份 |
| 本地Markdown目标链接 | 1,250次，0断链 |
| 来源包声明哈希 | 431次，覆盖215个不同文件，0不匹配 |
| 可解析的分析输入哈希映射 | 22次，0不匹配 |
| 四包原文目录／metadata／evidence-note入口 | 全部存在 |
| source-register与reading-index来源集合 | 216项一致 |
| 旧阅读记录及三场景／架构正文 | 内容与顺序检查通过 |

完整结果：[validation.json](validation.json)、[来源哈希逐项记录](source-hash-checks.json)、[分析输入哈希逐项记录](analysis-input-hash-checks.json)。可从仓库根目录执行`python3 knowledge-base/audits/2026-10-20-final-source-integration/verify.py`重新核对。

范围说明：本次检查新增／修改的作者Markdown及四个来源包显式声明的本地文件哈希；发布方原始Markdown中的远端相对链接不改写成仓库链接。外部URL能否长期访问、来源内容是否真实、人工审查、模型任务质量与交易准入，不由文件完整性检查代替。
