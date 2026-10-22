# 公开评测数据与PPT图表

**2026-10-20快照。** 来源原件在[TECH-091](../../../sources/TECH-091/evidence-note.md)，结论在[模型评测研究](../../public-benchmark-review-2026-10-20.md)。本目录没有模型调用结果；全部分数来自公开来源。

| 文件 | 用途与口径 |
|---|---|
| `finance-agent-v2.csv` | 8项模型标签；Finance Agent v2关键条件门槛后的加权部分得分；1017更新单列 |
| `finance-agent-full-snapshot.csv` | 作者页面完整表格的机械提取；费用与耗时不是本地TCO／GPU性能 |
| `extractbench.csv` | 六个pipeline的全集／短／中／长F1、长列表precision/recall、原始配置与精确代码修订 |
| `artificial-analysis.csv` | 同站同名分项；SciCode保留“Under review”标签，不作为主要推荐依据 |
| `bizbench.csv` | 同50任务×3次；目标／过程／保护与严格成功，pass^3独立列 |
| `chinese-finance-supplement.csv` | ReLE中文金融知识补充；未披露每行完整设置，Qwen27缺项不补值 |
| `official-supplement.csv` | 官方数学／代码／长检索与DeepSeek跨harness分数；不同协议不排序 |
| `checks.json` | 从分组数量复算ExtractBench全集均值；只验证转录和加权口径 |
| `build_tables.py` | 从来源原件重建CSV、保存被检查的原始配置；需Python+lxml，不访问模型 |
| `draw_figures.py` | 按CSV生成四张可编辑SVG；横轴均为0–100，不合成总分 |

## 图表及建议页位

- `finance-agent-v2.svg`：P08或A03金融任务对照。页面需保留“加权部分得分”和更新日期。
- `extractbench-length.svg`：P31/A11。长文档分数与全集分数的差别应随图说明；输入、thinking和输出上限不同。
- `aa-selected.svg`：P08/A03。三项分组显示，AA-LCR约100K，与部署容量图分开。
- `bizbench-goal-strict.svg`：P31/A11。说明评价目标与过程；不称为本部门任务成功率。

SVG为原生向量文字及矩形，CSV可以直接供PPT重画。图中文字与图注已包含来源、日期与最主要条件；详细条件随配套表交接。

每幅图附同名PNG，已逐图视觉核查，无裁切和重叠；SVG保留可编辑文本。

## 复算

先用带lxml的Python执行`build_tables.py`，再执行`draw_figures.py`。`build_tables.py`的可选代码原件保存步骤使用研究工作区的ExtractBench固定修订；正式来源包已含对应文件，无需重新clone即可阅读。试点评分、工作量和虚构题目另在[pilot数据目录](../../../pilots/data/final-pilot-roadmap-2026-10-20/evaluation-protocol.md)。

## 比较限制

同榜只是比较起点：保留模型标签、工具、harness和thinking条件。本轮不能把API端点对应到运行时完整权重SHA；当前下载的模型卡SHA是资料快照，不是证明基准运行使用该SHA。公开分数不填入内部ROI或验收结果。
