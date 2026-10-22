# 三年TCO可复算资料

**2026年10月20日。** 正文见[完整分析](../../tco-analysis-2026-10-20.md)。只执行CPU标准库计算，不调用付费API或GPU。

复算命令：

```bash
python3 knowledge-base/infrastructure/data/tco-2026-10-20/calculate.py
python3 knowledge-base/infrastructure/data/tco-2026-10-20/independent_audit.py
```

| 文件 | 内容 |
|---|---|
| [inputs.json](inputs.json) | 日期、官方费率、工作量、人工、功耗、电价、PUE、税费准备和服务包络 |
| [calculate.py](calculate.py) | 逐轮输入账、三年成本、容量限载、扩容、敏感性及代数回本点 |
| [results.json](results.json) | 完整机器可读结果与来源SHA-256；未测质量／SLA保留null |
| [round-ledger.csv](round-ledger.csv) | 8轮实际提交、新增、输出、各路线缓存与重新prefill |
| [summary.csv](summary.csv) | 2规模×3用量×3路线三年总表 |
| [annual-costs.csv](annual-costs.csv) | 54行年度分项、人工与外部采购运行支出 |
| [sensitivity.csv](sensitivity.csv) | 28项单因素、2个规模，共56行 |
| [volume-curve.csv](volume-curve.csv) | 301行首年用量／增长／扩容后的三年成本，供曲线制作 |
| [presentation-bars.csv](presentation-bars.csv) | P29中量分面板堆叠柱，各类别金额及万元值 |
| [time-value.csv](time-value.csv) | 释放工时、时间价值、0／25／100%现金兑现分别计算 |
| [validation.json](validation.json) | 已执行的算术、容量与计费守恒检查 |
| [independent_audit.py](independent_audit.py) | 独立Decimal等差数列、固定＋变动成本反算；不导入主脚本 |
| [independent-audit.json](independent-audit.json) | 6情景增长、全部年度分项、301曲线点、4个临界值、链接和来源hash复核 |
| [annual-token-volumes.csv](annual-token-volumes.csv) | 18行年度输入、缓存写读、输出与扩容节点 |
| [three-year-token-volumes.csv](three-year-token-volumes.csv) | 6情景三年token全账，含额外轨迹 |

金额包含表内人工资源成本；`nonlabor_outlay`剔除内部人工，只表示可识别的外部采购和运行支出。是否发生新增现金由实施方式和合同决定。`cny_per_target_accepted_task_conditional`用计划合格任务量作分母，不是已测任务成本。`capacity_envelope_pass`只核对预算机时，不是GPU实测SLA。

A100的性能及合格任务成本均为null。500K起步长任务的本地成本在敏感性CSV主列留空，仅在`unvalidated_algebraic_local_cny`保存未经验证的演算值，不能作为已达标部署报价。

公司包络为400输出token/s与8,000重新prefill token/s，分别计机时再相加，按每年2,000h、70%上限规划。全context驻留能力、峰值等待和金融任务质量须另外验证。技术人日按2,500元、分析师业务工时价值按150元／小时分别计算。DeepSeek API只对应符合平台条款且获准的材料；Sonnet是适用主体／地域成立时的全球经济对照。本地Python与文件工具不触发供应商Search／Fetch费；新增联网工具计数参数基准为0，启用后单列。

源快照为[TECH-090](../../../sources/TECH-090/original.md)及[TECH-092当前版本与条款](../../../sources/TECH-092/original.md)，硬件沿10月12日台账，Spark曲线沿外部测量拟合。
