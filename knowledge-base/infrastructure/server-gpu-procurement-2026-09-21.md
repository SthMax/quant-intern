# 中国境内部署的服务器级GPU：采购候选与出口许可路径

**核查日期：2026年9月21日。** 本文服务于第4周的软硬件落地研究，覆盖NVIDIA与AMD服务器加速卡、整机渠道、美国出口规则及已经发生的供货。硬件采购地点为中国境内，应用是机构内部LLM服务。

**阅读顺序：**第1节给出可以继续比较和询价的型号组，第2节列规格，第3–4节解释采购证据，并在第4.3–4.7节给出四卡／八卡BOM和人民币预算；第5节连接到服务架构。并发测算随后按具体任务衔接。配套材料：[参考架构](reference-architecture.md)、[Serving研究](serving-framework-survey-2026-09-17.md)、[模型候选](../models/model-survey-2026-09-16.md)。

## 1. 本轮结论：形成三组采购研究候选

| 研究位置 | 型号 | 已经掌握的事实 | 下一步补齐的采购信息 |
|---|---|---|---|
| **部门服务器主候选** | **NVIDIA L20 48GB；RTX PRO 6000D Blackwell Server Edition 84GB** | HPE有准确地区SKU：L20注明中国／港澳，6000D独立表注明China/HK，并列有兼容服务器；可以从这些OEM配置开始研究 | 按准确SKU取得出口分类及本交易的许可依据、整机报价与交期；核对L20功耗字段冲突 |
| **高带宽共享服务主候选** | **NVIDIA H200 SXM 141GB；H200 NVL 141GB** | 2026年1月规则明确提供附条件的逐案许可路径；NVIDIA最新季度披露已经完成部分许可项下发货 | 确认本买方、地址、数量及用途能纳入何种许可；确定SXM或NVL整机、进口条件和交付时间 |
| **AMD主研究候选** | **Instinct MI308；MI325X／监管披露中的MI325** | MI308已向部分中国客户恢复发货；MI325在2026年2月取得部分中国客户出口许可；MI325X有完整256GB／6TB/s规格和八卡平台 | MI308准确型号、规格和OEM配置；MI325许可所指SKU及其与MI325X的关系；中国进口与本项目交付证据 |
| 补充比较 | L40S、L40、L4、RTX PRO 4500 Blackwell Server Edition、标准RTX PRO 6000 Blackwell Server Edition、MI300X | 均有正式服务器产品与软件生态；原厂/OEM资料同时标明其中的受控属性 | 先取得中国交易许可与渠道材料，再加入具体配置比较 |
| 已有设备／历史参考 | A800、H800、A100、H100、MI210 | 可用于理解既有GPU集群和复用价值；部分OEM部件已经停售 | 现存设备的型号、来源、原授权及转移条件；只有取得这些信息才形成复用方案 |

这组候选覆盖两种重要差异：**L20／6000D用标准PCIe服务器提供部门算力；H200／MI325X用HBM和高速卡间互联承载更大的模型与共享负载。** AMD MI325X的256GB单卡容量值得与H200认真比较，H200并非一个可以概括所有合法交易的“性能上限”。[HPE地区SKU资料][S1]、[6000D独立数据表][S3]、[BIS规则][R1]、[NVIDIA最新披露][D1]、[AMD最新披露][D2]。

本文将证据分为三个层次：**公开销售目录、已经披露的许可／发货、本机构的具体交付条件**。前两层已经能支持本周的型号研究；第三层需要准确买方与供应商文件。全文的“主候选”指下一步研究和询价的优先对象。

## 2. 逐型号规格与比较价值

### 2.1 主候选

容量沿用厂商标称GB；带宽是单GPU显存带宽，卡间链路单独列示。功耗是原厂/OEM的板卡功率或设计点，整机还包括CPU、内存、风扇和网络。PCIe带宽若给数字，采用厂商公布的双向合计口径。

| 准确型号／形态 | 单GPU显存与带宽 | 主机接口、卡间互联 | 板卡功耗口径 | 对LLM部署的价值 | 许可／渠道状态 |
|---|---|---|---|---|---|
| **L20，HPE S4A92C**；Ada，双槽被动散热PCIe | 48GB GDDR6；864GB/s | PCIe 4.0×16；本轮OEM材料未列NVLink连接方案 | HPE独立数据表写最大300W，QuickSpecs V82写350W；待OEM按SKU确认 | 适合27B／35B级量化模型、文档处理及多模型副本；以单卡量化副本作为服务扩展单位 | HPE明确中国／港澳销售；准确ECCN及本次交易许可依据待供应方提供。[S1]、[S2] |
| **RTX PRO 6000D Blackwell Server Edition，HPE S6W21C**；被动散热PCIe服务器版 | 84GB GDDR7 ECC；1398GB/s | PCIe 5.0×16；采用PCIe服务器路线，本轮未取得该SKU的NVLink规格 | QuickSpecs列600W；具体服务器可能配置更低功率上限 | 84GB覆盖当前中型模型约52–72GB的BF16权重体量，并为量化部署提供更大上下文／批处理空间；支持Blackwell低精度功能 | HPE面向中国／香港的服务器SKU、正式兼容整机与NVIDIA驱动条目已核；出口分类和交付条件待取得。[S1]、[S3]、[S4] |
| **H200 SXM5**；Hopper，HGX四／八GPU基板 | 141GB HBM3e；4.8TB/s | PCIe 5.0；NVLink每GPU最高900GB/s，HGX基板组织高速多GPU通信 | 700W | 高显存带宽兼顾大模型生成与多卡分片；八卡总容量1128GB | 附条件逐案许可路径；厂商已披露有限发货。整机及许可需落实到本交易。[R1]、[D1]、[S5] |
| **H200 NVL PCIe**；Hopper，双槽被动散热 | 141GB HBM3e；4.8TB/s | PCIe 5.0×16；NVLink最高900GB/s；OEM列双卡／四卡桥接器 | 600W | 可以比较双卡、四卡及PCIe八卡服务器，容量与HBM带宽较强；适合从部门规模逐步扩展 | 同属H200许可研究；桥接拓扑、OEM部件与SXM分别确认。Lenovo部件4X67A97315；HPE有NVL目录。[S5]、[S6] |
| **AMD Instinct MI325X OAM**；CDNA 3，八GPU UBB 2.0平台 | 256GB HBM3E；6TB/s | PCIe 5.0；7条Infinity Fabric GPU链路，7×128GB/s，即896GB/s双向合计 | 最大1000W／GPU | 单卡容量大，八卡2048GB；可减少部分模型的分片数量，为大模型和缓存留出空间 | BIS举例的许可路径；AMD披露的许可名称是“MI325 products”，本机构配置须与准确SKU对上。[R1]、[D2]、[S7]、[S8] |
| **AMD Instinct MI308** | 本轮未取得与中国交付型号一一对应的官方公开规格表 | 待准确OEM料号／基板资料 | 待准确SKU | 其研究价值首先来自**已经发生的中国客户许可出货**；取得规格后再与MI325X及H200比较 | 2025年4月起需许可；AMD披露已获部分许可并于2025财年末开始发货。保留厂商名称MI308，不把MI300X规格套入。[D2] |

**原厂资料也需要按版本交叉核对。** L20独立数据表与更新的QuickSpecs V82分别写300W与350W，电源配置应以供应方最终物料清单为准。6000D的84GB／1398GB/s由2026年9月独立数据表确认，V82第10页同时列600W、PCIe 5.0×16及兼容整机。QuickSpecs部分MIG／精度字段存在可疑内容；容量与带宽按独立数据表交叉核对，接口和功耗据对应OEM规格记录，冲突单独保留。[S1]、[S2]、[S3]

### 2.2 补充型号：有部署价值，但中国采购证据弱于主候选

| 型号／形态 | 显存；显存带宽 | 互联；板卡功耗 | 研究位置和中国采购证据 |
|---|---|---|---|
| **H20 SXM5**，Hopper | Dell XE9680文档确认96GB；本轮未取得该准确变体带宽表 | 八GPU NVLink；Dell该配置列500W | 仍是评估境内既有推理设备的重要对象。NVIDIA披露2025年8月开始获得部分H20许可，随后中国方面限制销售，库存未能售出；本轮没有形成可用于机构采购的现行交付承诺。[D1]、[S9] |
| **L40S PCIe**，Ada | 48GB GDDR6；864GB/s | PCIe 4.0×16，无NVLink；350W | 较成熟的企业推理与图形路线。NVIDIA受许可产品清单及Lenovo受控表均覆盖L40S；HPE中文目录有产品，采购研究需继续核具体许可。[D1]、[S1]、[S6]、[S10] |
| **L40 PCIe**，Ada | 48GB GDDR6；864GB/s | PCIe 4.0×16，无NVLink；300W | 可作已有图形／推理服务器参考。Lenovo该部件于2025年12月停售且标记受控，HPE仍保留目录，需按厂商分别判断供应。[S6]、[S11] |
| **L4 PCIe**，Ada，半高单槽 | 24GB GDDR6；300GB/s | PCIe 4.0×16，无NVLink；72W | 可独立承载embedding、reranker或资料解析等辅助服务。NVIDIA最新披露及Lenovo均列受控，24GB并不构成免许可依据。[D1]、[S10]、[S12] |
| **RTX PRO 4500 Blackwell Server Edition**，PCIe单槽被动散热 | 32GB GDDR7；800GB/s | PCIe 5.0×16；165W | 量化中型模型或辅助服务的密度／能耗对照。HPE S6W30C、Lenovo 4X67B12675为准确服务器SKU；Lenovo标记Controlled，中国现行交付待核。[S1]、[S10] |
| **RTX PRO 6000 Blackwell Server Edition**，标准96GB版 | 96GB GDDR7；1597GB/s | PCIe 5.0×16，无NVLink；600W，部分整机可限至450W | 相比6000D有更大容量和带宽。Lenovo明确列受控；其八卡PCIe整机可作技术对照，当前中国主询价对象优先用地区明确的84GB 6000D。[S13] |
| **AMD MI300X OAM**，CDNA 3 | 192GB HBM3；5.3TB/s | Infinity Fabric 896GB/s；750W | 可比较MI325X的内存升级收益。Dell XE9680、HPE XD685等有正式八卡配置，Lenovo列受控；未取得与MI308／MI325同等级的最新中国许可出货披露。[S7]、[S9]、[S10]、[S14] |

### 2.3 历史设备与更高性能产品

**A800／H800继续作为既有设备调查对象。** A800 80GB PCIe版为1935GB/s、SXM版为2039GB/s，两者NVLink为400GB/s；Lenovo指南已标记停售。Dell仍保留H800 80GB SXM5、700W八卡配置的服务资料。NVIDIA最新监管披露列出A100、A800、H100、H800等受许可产品。若机构已有设备，应按序列号、原购买方、安装地址及用途研究复用；对于新购，H200有更直接的当前许可与厂商供货证据。[S15]、[S9]、[D1]

**AMD MI210是64GB PCIe存量路线。** 官方规格为CDNA 2、64GB HBM2e、约1.6TB/s、300W，可通过Infinity Fabric桥连接多卡。Lenovo将其列为Controlled，并于2026年5月15日停止营销对应部件。若已有设备，适合比较BF16与量化任务；新采购阶段优先把调查资源放在MI308／MI325系列。[S16]、[S10]

**B200／B300、MI350X／MI355X等用于观察更高性能档位。** 例如MI350X／MI355X显存带宽为8TB/s，已经超过2026年1月特定逐案路径的6500GB/s条件。NVIDIA新一代高端产品也不能凭H200的政策类推中国交付。本轮没有取得这些型号供本项目中国部署的许可／供货证据，保留技术参考即可。[R1]、[S17]、[D1]

DGX Spark属于个人AI系统，本篇按服务器级GPU的边界另留到个人机研究。

## 3. 美国出口规则怎样作用于采购

### 3.1 关键规则是“准确货物＋交易＋最终用户／用途”

GPU通常涉及集成电路的ECCN，例如3A090；装入服务器后还要核对4A090或相关“.z”条目等整机分类。采购材料应同时列**GPU料号、服务器整机料号、出口／再出口地点、最终安装地址、最终用户和用途**。L20、6000D的原厂地区专用目录为供应研究提供了具体起点，出口分类应由供应方针对交付物说明。

美国总部或国际集团身份属于许可证审查的事实输入。设备最终安装在中国时，仍然需要处理中国目的地要求；总部所在地还影响某些全球范围最终用户管制。BIS在2026年5月31日再次明确：对D:5／澳门总部或最终母公司主体的既有先进计算许可要求继续执行，即使收货实体在其他国家。本文不对本机构的具体集团主体和许可证资格作个案认定。[R2]、[R3]

### 3.2 H200／MI325X路径：可逐案申请，条件具体且可核查

2026年1月15日生效的规则，将以下交易纳入逐案审查：**从美国出口、目的地为中国或澳门最终用户、TPP小于21,000且总DRAM带宽小于6500GB/s的相关先进计算货物**，并满足Part 748 Supplement No.2(dd)资料与证明要求。BIS在规则说明中直接举H200和MI325X为例。[R1]、[R2]、[R4]

主要条件如下：

1. 货物在规则发布时已经在美国商业销售，申请中披露TPP、DRAM带宽、互联、封装内存及峰值功率等准确规格。
2. 出口商证明美国供应充足，对华供货不会延误美国客户订单或挤占为美国市场服务的相同／更先进节点产能。
3. 同一先进计算货物对中国／澳门出口的**累计TPP**，不超过该货物此前向美国境内最终用途客户供货累计TPP的50%。这是出口商供货证明口径，而非某个中国买方“可以买美国采购量的一半”。
4. 提供最终收货方KYC、物理安全和相关远程IaaS用户信息；排除条款列明的军事、军事情报、核导弹／生化武器用途及受限交易方，并控制其远程访问。
5. 每次从美国出口前由符合条件的美国独立第三方实验室核对实际性能，向BIS提交证明。IaaS服务场景还包括特定模型权重转移与远程访问承诺。[R4]

对机构内部LLM服务，落地材料可明确人员范围、数据中心地址、身份与权限管理、是否提供外部算力服务以及运维访问方式。这些是描述实际用途与接收条件的材料，也直接帮助后续系统设计。

**许可证与费用的实际进展。** NVIDIA最新10-Q已经披露H200完成部分许可项下发货；AMD最新10-Q则分别披露MI308已发货、MI325获许可但进口状态仍未明。两家公司对H200／MI325都描述了美国先行检测及进入美国检测时25%关税的影响。报价应让供应方明确这部分费用的承担方式及计价基础，不能把25%简单加在所有GPU或整机报价之上。[D1]、[D2]

### 3.3 再出口、境内转移、继续使用的区别

| 交易／使用情形 | 需要核对的事项 |
|---|---|
| 从美国按许可出口到中国指定用户 | 适用上述逐案路径时，按批准型号、数量、收货主体、用途和检测条件交付 |
| 从第三国库存调入中国 | 属于再出口方向；2026年1月规则说明明确，相关货物再出口和境内转移的申请仍保留推定拒绝政策，不能直接套用“从美国出口”的新路径 |
| 中国境内二手购买或从另一法人调拨 | EAR §734.16把同一外国境内最终用户或最终用途改变定义为境内转移。应核原许可是否涵盖新用户／用途，及现行要求是否需要新的授权 |
| 同一主体、原地址和原授权用途继续使用合法取得的设备 | 先核原授权条件与持续义务；普通继续使用与新发生的跨境交易／最终用户变更分别处理 |
| 原许可证已列明的收货方及最终用户之间移动 | §750.7(c)(1)(ix)允许一定范围内按原许可进行，但须满足姓名／地址及许可附加条件；具体许可可能进一步限制 |

货物的来源证明因此有实际价值：序列号、原采购和进口记录、许可证相关范围、转售链条及原厂服务资格。EAR一般禁令10还覆盖明知与违法出口／再出口／转移相关的购买、使用等行为，境内发票需要与这些来源材料一起判断。[R1]、[R5]、[R6]、[R7]

### 3.4 本轮怎样处理现行文本与旧政策

本轮读取的eCFR页面显示Title 15资料更新至2026年9月17日，最后修订为8月28日；另以2026年1月Federal Register最终规则及5月31日BIS指导交叉核查。

eCFR仍可见2025年AI Diffusion框架条文，而BIS另有不执行该框架新增要求的政策。2026年5月31日官方指导强调，**旧有的中国相关管制继续执行**。因此本文没有把页面上的全球国家配额机械视为当前全部执行安排，也没有把“AI Diffusion不执行”理解为中国高级GPU放开。[R3]、[R8]

## 4. 中国供货与整机证据

### 4.1 当前能拿去对接的原厂/OEM入口

| 产品线 | 证据、地区与日期 | 可以支持的判断 | 仍需供应方提供 |
|---|---|---|---|
| **HPE L20，S4A92C** | HPE中国产品目录；QuickSpecs V82（2026-07-20）第14–15页；本轮2026-09-21读取。兼容DL380a Gen11／Gen12、DL320／DL340 Gen12及DL385 Gen11等 | 准确中国地区SKU和受支持整机路径已经存在 | 出口分类、功率配置、带卡数量的完整BOM、含税报价、原厂保修及交期。[S1]、[S2] |
| **HPE RTX PRO 6000D，S6W21C** | QuickSpecs V82第10页；独立数据表落款2026年9月，第1页标注China/HK，第3页列DL380a Gen12、DL380 Gen12、DL385 Gen11 | 正式服务器版84GB方案已进入OEM资料，可用于部门服务器配置比较 | 对华许可依据、单卡功率上限、准确支持数量、价格和交期。[S1]、[S3] |
| **H200 SXM／NVL** | NVIDIA 2026-08-26披露许可发货；Lenovo H200产品指南，最后更新2025-11-07；HPE中国目录有H200 NVL；Dell XE9680支持八SXM H200 | 能从正规的NVL服务器和HGX整机路线研究，厂商层面已有许可发货事实 | 具体买方是否被许可覆盖、中国进口条件和实际可交付整机；本轮未取得公开面向本机构的报价。[D1]、[S5]、[S6]、[S9] |
| **AMD MI308** | AMD 2026-08-05披露，部分中国客户许可下于2025财年末开始发货 | 有实际中国供应证据，值得向AMD/OEM核准确配置 | 交付名称和规格、OEM整机、许可用户和新订单条件。[D2] |
| **AMD MI325／MI325X** | AMD同份披露给出许可进展；AMD官方八卡平台；HPE XD685发布资料（2024-10-10）及Supermicro AMD服务器目录 | 许可路径和成熟八卡整机分别有证据 | 将许可中的MI325名称对应到交付SKU，并取得中国进口／交付条件；全球或中文版产品目录只用于证明产品与整机存在。[D2]、[S8]、[S14]、[S18] |

本轮尚未取得中国原厂针对下列完整物料清单的公开报价。按用户允许的估算口径，第4.3–4.7节补充七套四卡／八卡配置与人民币预算，逐项区分国内组件历史挂牌、海外公开整机价和分析假设。

### 4.2 证据怎样进入决策材料

- **L20／6000D：**从准确地区SKU出发做双卡、四卡和整机上限的配置询价。先确认服务器实际支持数量，再计算容量与成本。
- **H200：**并列比较NVL服务器与八卡HGX。采购问询中同时列出许可用户、用途、安装地点、进口安排和交期，使性能方案与交付路径保持一致。
- **AMD：**MI308优先补规格／整机；MI325优先补准确许可SKU和进口／交付；技术比较采用资料完整的MI325X平台。

这些问询项用于准备下一步研究，不表示本轮已经联系厂商或发出询价。

### 4.3 七套四卡／八卡服务器配置与人民币预算

配套的[个人／三人工作站研究](workstation-configurations-2026-09-21.md)覆盖更小的部署规模。两份研究的价格来源、逐项预算与计算式汇总于[硬件价格数据](data/hardware-prices-2026-09-21.json)，便于后续替换正式报价及接入TCO。

**价格标识统一如下：A＝中国公开整机价；B＝国内组件公开价加总；C＝海外公开价换算；D＝分析估算。** 本轮七套目标方案均为D，来源锚点分别标B或C；没有把缺少完整BOM的网页起价归为A或B整机价。

**人民币为主口径，美元采用情景汇率1美元＝7.00元。** 该汇率用于本轮比较，不是2026年9月21日即期汇率。下表是整机及基础部署的**现金预算区间**，范围包含硬件、13%硬件增值税准备、10%硬件价格预留，以及表中列明的交付／三年硬件支持准备。区间来自逐项低／高情景相加，不是统计置信区间或采购承诺；实际采购仍沿用前文的地区SKU与许可路径。

| 编号 | GPU配置／合计显存 | CPU、RAM与NVMe目标配置 | 网络目标配置 | 整机和互联参考 | **人民币预算／类型** |
|---|---|---|---|---|---|
| **G1** | **4×L20 48GB／192GB** | 2×Xeon 6710E，各64核；512GB DDR5 RDIMM（8×64GB）；2×1.92TB系统盘＋2×3.84TB数据盘，均为企业NVMe | 1张双口25GbE；独立BMC管理口 | HPE DL380a Gen12，4U；四张PCIe卡，适合多个单卡模型副本 | **40–74万元，D** |
| **G2** | **8×L20 48GB／384GB** | 同级双6710E；1TB RDIMM（16×64GB）；2×1.92TB＋2×7.68TB企业NVMe | 1张双口100GbE；独立管理口 | 同平台八卡，GPU仍按PCIe拓扑分配 | **66–120万元，D** |
| **G3** | **4×RTX PRO 6000D服务器版84GB／336GB** | 双6710E；1TB RDIMM（16×64GB）；2×1.92TB＋2×3.84TB企业NVMe | 1张双口25GbE；独立管理口 | DL380a Gen12四卡；6000D采用服务器被动散热版本 | **62–115万元，D** |
| **G4** | **8×RTX PRO 6000D服务器版84GB／672GB** | 双6710E；2TB RDIMM（32×64GB，双DIMM／通道，按CPU支持降频）；2×1.92TB＋2×7.68TB企业NVMe | 1张双口100GbE；独立管理口 | DL380a Gen12八卡及前置风扇升级；最多4.8kW的GPU设计功率 | **109–200万元，D** |
| **G5** | **4×H200 NVL 141GB／564GB** | 双6710E；1.5TB RDIMM（16×96GB）；2×1.92TB＋2×7.68TB企业NVMe | 1张双口100GbE；独立管理口 | DL380a Gen12四NVL及对应四向NVLink桥接套件；四卡作为一个高速互联组 | **169–345万元，D** |
| **G6** | **8×HGX H200 SXM／1128GB** | Exxact TS4-118380266：2×EPYC 9454，各48核；1.5TB RDIMM（24×64GB）；目标补至2×1.92TB＋2×7.68TB企业NVMe | 原配置X550双口10GbE；目标增加双口100GbE；独立管理口 | 8U；八H200 SXM与NVSwitch，六组3000W电源，3+3冗余，风冷 | **290–352万元，D**；公开默认配置直接换算为**228.26万元，C** |
| **G7** | **8×MI325X OAM／2048GB** | Supermicro AS-8126GS-TNMR等级：2×EPYC 9005，每颗32–48核；1.5TB RDIMM（24×64GB）；2×1.92TB＋2×7.68TB企业NVMe | 板载双口10GbE；增加双口100GbE；独立管理口 | 8U；完整八OAM UBB与Infinity Fabric；按该eStore配置说明为六组5250W电源、3+3冗余与十只高风量风扇 | **219–336万元，D**；平台公开起价换算为**171.91万元，C** |

**整机参考与价格的关系。** G1–G5的卡数、CPU及风道依据HPE配置规则，但预算由公开标准卡价格和系统集成成本推算，**不是HPE原厂对这些BOM的报价**。原厂GPU料号、整机出厂验证和支持合同会改变价格；例如CDW美国的HPE H200 NVL备件S3U30C挂牌折合约66.29万元／张，显著高于另一经销商的标准NVIDIA料号挂牌23.45万元／张。这两种销售口径应分别保留，原厂CTO询价时用准确料号整体校验预算。[P03]、[P09]

G6直接从已含八GPU、CPU与1.5TB RAM的完整配置价开始，只增加目标存储／网卡与中国交付的费用情景。G7的美国店起价未显示完整默认CPU／RAM／SSD清单，所以用作整机量级锚点，采用下节的独立部件预算；不能将“171.91万元起”作为表中完整G7配置的实价。[P04]、[P05]

### 4.4 卡数、供电与冷却怎样落实

HPE DL380a Gen12的现行配置表直接列出L20 S4A92C、6000D S6W21C及H200 NVL S3U30C，列有四卡／八卡双宽配置和Xeon 6710E。四卡配置要求五组电源，八卡要求八组；H200 NVL与RTX PRO路线选择2400W或3200W电源。八张RTX PRO还需要前置风扇与前面板组件，不能使用与其冲突的8DW NIC FIO配置。正式BOM应由OEM配置器按所选SKU确认这些关联项。[T01]

| 方案 | 本轮供电／冷却BOM假设 | 卡间拓扑与使用方式 |
|---|---|---|
| G1 | 5×2400W M-CRPS、所需GPU供电线、四卡风冷组件、机架导轨 | 四PCIe卡；优先比较四个单卡副本或两组双卡模型 |
| G2 | 8×2400W M-CRPS、八卡供电／散热组件；按L20 350W较高字段做电源预留 | 八PCIe卡；CPU根端口、交换芯片和GPU分组由OEM拓扑图确认 |
| G3 | 5×2400W M-CRPS、600W卡供电线与风冷组件 | 四PCIe卡；可比较BF16单卡或量化多副本 |
| G4 | 8×3200W M-CRPS；前置风扇P79656-B21、前面板P79660-B21及适配GPU供电线 | 八PCIe卡；8×600W＝4.8kW只含GPU。该机按数据中心风道与双路PDU部署 |
| G5 | 5×3200W M-CRPS及NVL高功率风冷组件；四向桥接套件S4A91C的数量／插槽位置由OEM BOM确定 | 一个四卡NVLink组；四卡GPU设计功率合计2.4kW |
| G6 | 厂商配置器已列6×3000W、3+3，及六根6FT C19-C20电源线；风冷；按现场接口核对已含线缆、PDU连接和上架服务 | HGX八卡NVSwitch；厂家配置器估算6.845kW，作为设施核查输入 |
| G7 | 以AS-8126GS-TNMR当前网页列出的6×5250W、3+3和十风扇为配置研究口径，采购BOM同时确认电源输入条件 | 八OAM完整平台；GPU设计功率约8kW，另计CPU、RAM、风扇和网络 |

HPE八电源机器采用分域冗余：系统域与GPU域分别供电。电源铭牌相加是冗余供电能力，**不是服务器用电量**。G7同系列其他修订的电源和NVMe位数量不同，本表没有把TNMR2旧数据表的3000W电源混入TNMR网页价格。[T01]、[T02]、[P04]、[P05]

MI325X沿用成熟的八OAM平台；本轮没有编造标准四卡MI325X整机。MI308仍等待准确SKU和完整BOM，因此不填价格。跨节点的400GbE／InfiniBand交换机及每GPU独立网络是扩展集群成本，当前七套均以**单节点内部服务**为预算边界。

### 4.5 单项价格锚点及分析假设

所有下列页面均在2026年9月21日读取；未标发布日的销售页按本轮读取快照记录。原始数值、币种、来源日期和税／运／保修信息同时保存在构建目录的`price-sources-2026-09-21.json`。

| 项目 | 可核实的公开价格／来源类别 | 本轮D估算采用的数值和理由 |
|---|---|---|
| L20标准卡 | 成都强川科技，经ZOL刊载，2026-03-03：**2.88万元／张，B组件锚点**；税、保修未列 | **2.4–4.0万元／张，税前分析值**。历史挂牌提供量级，上下沿覆盖成交折扣、原厂料号与供应差异；不是9月现货价。[P01] |
| 6000D标准服务器卡 | 济南信源泰达装机店，2026-05-18：**4.9999万元／张，B组件锚点**；页面促销期限7天已过；税／保修未列 | **5.0–8.5万元／张，税前分析值**。以历史标准卡挂牌为下沿锚点，扩大渠道及原厂集成价格情景；不把它视为HPE S6W21C报价。[P02] |
| H200 NVL标准料号 | ViperaTech：**23.45万元／张，C**（原币USD33,500）；页面标缺货，三年厂家保修，运费和进口税未定 | **23.5–40万元／张，税前分析值**。含渠道、供货条件和原厂适配差异；如果必须按高价OEM备件口径采购，应改用对应实价重新计算。[P03]、[P09] |
| 双Xeon 6710E | Intel RCP：两颗折合**3.4482万元，C建议价锚点**（2×USD2463），每颗64核／205W | **3.5–5.5万元／对**，加入OEM CPU套件、散热器和集成差价假设。[P06] |
| DDR5 RDIMM | memory.net 2026-08-26：64GB DDR5-5600替换条挂牌折合**2.0916万元／条，C**；属于单条替换渠道 | 主预算按**0.8–1.7万元／64GB容量**作OEM整机打包分析假设，约为该替换价的38%–81%；未取得OEM批量报价。96GB按1.5倍容量估算。另保留全额替换价压力情景，见下文。[P07] |
| PCIe平台底座 | 未取得可直接复用的完整裸机实价；Star Networking将P76706-B21自身列为预算估价，折合**11.375万元，D来源** | 四卡主板／BMC／PCIe布局／机箱／导轨**8–14万元**；八卡**10–16万元**。该项不含独立列出的CPU、RAM、GPU、电源和风扇；11.375万元只作量级对照。[P08] |
| 电源、风扇、GPU供电线 | OEM数量规则已核，未取得准确组合公开价 | 四卡按**1.5–5万元**、八卡按**3–7万元**，高功率组取较高端；单独覆盖5/8组M-CRPS、风扇与线缆，避免漏算G4散热升级 |
| NVMe | 没有与所选OEM料号一致的四盘报价；Exxact有存储升级价，但默认选项数量未完整显示 | 四盘含镜像系统与数据盘，按**2–4.5万元**；容量较大的组提高上沿。G6按原配置上增加的存储／NIC合计**2.5–6万元**估算，保留原盘价值 |
| 网卡及短距离连接 | 未取得与最终OEM兼容料号完全一致的报价 | 双口25GbE含短DAC／光模块**0.4–1.0万元**；双口100GbE及连接**1.0–3.0万元**；这是单节点接入，未含集群交换机 |
| 四向NVLink桥接 | HPE确认S4A91C方案，未取得最终套件数量与报价 | G5预留**1–3万元**覆盖桥与安装；OEM若要求多件套件，按最终BOM替换 |
| G7八MI325X／UBB／机箱／电源散热主体 | 美国Supermicro同平台起价**171.91万元，C**，完整默认BOM未披露 | 主体分析分配**145–175万元**，再分别列CPU **4–7万元**、1.5TB RAM **19.2–40.8万元**、四NVMe **3–5万元**及网络 **1–3万元**，得到完整税前硬件 **172.2–230.8万元**。该拆分是分析假设，不是厂商拆项报价。[P05] |

**RAM单列的原因。** 2026年单条服务器替换内存的挂牌可能显著高于OEM整机打包采购成本。以memory.net全额单条价做压力情景：512GB、1TB、1.5TB、2TB分别约为**16.73、33.47、50.20、66.93万元，C容量加总**，尚未加入中国VAT。它用于说明扩内存时的现金风险，不替代已含RAM的G6整机价格，也不表示所有OEM都会按这一单条价供货。[P07]

### 4.6 预算计算、税费和服务边界

下表单位均为**人民币万元**。H为完整硬件税前分析小计；各项数值由构建目录`server-price-scenarios-2026-09-21.json`逐项相加，可直接重算。

| 编号 | H：硬件小计，D | 交付／支持包，D、按含税金额预留 | 额外美国检测进口税上沿准备，D | 最终现金区间，D |
|---|---:|---:|---:|---:|
| G1 | 31.4–56.6 | 2–4 | 0 | **40–74** |
| G2 | 52.0–92.7 | 2.5–5 | 0 | **66–120** |
| G3 | 48.7–89.2 | 2.5–5 | 0 | **62–115** |
| G4 | 86.6–157.4 | 3–6 | 0 | **109–200** |
| G5 | 134.7–237.8 | 4–7 | 0–40.0，按GPU高情景160万元×25% | **169–345** |
| G6 | 230.7588–234.2588 | 7–15 | 0–42.7985，按公开整机锚点228.2588万元×假设GPU份额75%×25% | **290–352** |
| G7 | 172.2–230.8 | 8–15 | 0–32.8125，按主体高情景175万元×假设GPU份额75%×25% | **219–336** |

**计算式：现金预算＝H×1.13＋H×10%价格预留＋含税交付／支持包＋尚未体现在来源价格中的美国检测进口税×1.13。** 展示区间向外取整到万元；低／高情景分别代入每项下沿／上沿。

- **中国VAT：**一般货物13%取自2026年已生效的增值税法。本模型把13%用于硬件现金准备，服务包直接用含税金额；进口环节税基、供应商开票拆分及机构进项抵扣在正式报价时按实际处理。[T03]
- **美国检测进口税：**H200／MI325的现行披露说明25%费用，但来源价格有美国本地零售和境内挂牌等不同口径。这里的0表示来源价已含或供应方承担，不表示现行税率为0；上沿只为尚未计入的部分留预算。GPU报关价值未取得时，G6/G7的75%份额明确为分析假设。费用一旦已进入报价，就删除这项，避免重复加税。[D1]、[D2]
- **交付／支持包：**G1–G5预留国内运输、上架、硬件验收、基础Linux／驱动部署及三年硬件支持；目标为工作日下一工作日上门，实际服务覆盖由合同确认。G6/G7另预留高价值运输保险、清关操作、机架电源连接和本地服务衔接。G6原三年零件／人工保修已含在C锚点中，新增包用于交付及本地服务差额。
- **设施和软件边界：**七套均未计机房扩容、UPS、中央空调／液冷改造、跨节点高速交换网络、电费、专职运维，以及模型／Harness集成和商业软件许可。现有机房有这些设施时比较增量成本；若新建，应在下一轮BOM中单独列出。

### 4.7 本轮预算支持的比较

G1/G3适合比较四个独立中型模型副本以及双卡分片的成本；G2/G4体现扩到八张PCIe卡后，GPU之外的RAM、供电和支持支出。G5与G6比较“一个四NVL组”和“八卡HGX高速互联”的硬件投入；G7让AMD大显存八卡平台进入同一张预算表。当前价格跨度首先来自**是否采用原厂整机料号、RAM打包条件、许可交易路径和服务范围**，下一轮取得同口径报价即可大幅缩小区间。

在性能比较中仍使用相同任务质量、输入输出长度和服务目标。这里没有把四卡／八卡直接对应为20／50业务并发，也没有把单节点接入网卡配置写成完整多节点训练网络。

## 5. 与LLM服务的关系

### 5.1 从“可放入模型”扩展到“可持续提供服务”

当前中型候选的BF16权重文件约52–72GB。L20的48GB路线侧重量化或双卡；6000D的84GB路线可比较BF16单卡驻留与量化后更多缓存；H200的141GB和MI325X的256GB进一步支持更大的单卡模型／缓存空间。模型权重、上下文缓存、执行工作空间应一起计入每张卡的资源表。[既有模型数据](../models/model-survey-2026-09-16.md)

对于共享服务，显存带宽影响生成阶段读取权重和缓存的速度；较长材料的输入处理还依赖计算能力和实际低精度内核。比较同一个模型、精度和输入输出分布，才能将864GB/s、1398GB/s、4.8TB/s和6TB/s这些硬件差异转换成用户体验。

### 5.2 八卡服务器有不同的执行方式

- **多个模型副本：**每张卡或每组卡运行独立副本，请求按负载分配。适合能够在单卡／少量卡驻留的27B／35B模型，PCIe卡可以从这一路线发挥作用。
- **一个模型跨卡分片：**多卡共同完成一次推理，对GPU间通信更敏感。H200 HGX及MI325X八卡平台的高速互联是此路线的重要比较因素。
- **辅助任务分开：**embedding、reranker、OCR／多模态解析、LLM生成可以用不同资源池。部分低功耗卡即使不承担主模型，也可能降低整套服务成本。

H200 NVL的双／四卡桥接组、HGX八卡全互联、PCIe八卡，以及AMD八OAM平台应各自画拓扑图。多卡显存总和提供容量起点，实际模型分片与缓存分配决定每张卡能用多少。[S5]、[S8]、[S13]

### 5.3 软件比较与容量定义

NVIDIA路线衔接CUDA上的vLLM／SGLang；AMD路线衔接ROCm上的相同服务框架，逐模型核所用精度与内核。Serving与GPU应一起固定版本，使用已经定义的知识问答、长材料和多步Agent任务比较。现阶段的5／20／30／50仍是讨论档位，GPU采购表不填无依据的并发承诺。

## 6. 下一步所需的真实输入

本轮可以继续推进规格和软件组合研究。要把候选转为可交付配置，缺口集中在三类：

1. **准确SKU与整机：**本机构已有服务器／可调拨卡的部件号；新购意向的服务器品牌、GPU形态及数量。MI308和许可名称MI325尤其需要对应的官方物料资料。
2. **具体许可事实：**采购法人、最终使用法人、最终母公司注册地、安装地址、内部使用范围与远程访问安排；供应方针对该交易的出口分类、许可证或其他授权依据。
3. **可交付供应：**机构现有合格供应商、是否只接受原厂新机与本地保修、目标交付窗口；随后取得同口径的BOM、含税报价与交期。

上述信息不需要写入公开研究稿的机构名称字段；可由实际采购及合规负责人在内部流程中维护。

## 7. 关键证据目录

全部来源于2026年9月21日获取。价格新增来源P01–P09及配置／税制来源T01–T03的日期、数值和性质详见第4.5节与构建目录价格来源清单。发布日期与网页读取日分别记录；持续更新网页采用“本轮读取”口径。法规和监管披露优先于商品标题，准确SKU数据优先于同系列推测。

| 编号 | 资料与日期 | 本文使用位置 |
|---|---|---|
| R1 | Federal Register，91 FR 1684，2026-01-15生效，文件2026-00789；[官方PDF][R1] | H200／MI325X逐案路径、美国出口与再出口／转移区别 |
| R2 | eCFR §742.6；本轮页面显示法规更新至2026-09-17；[现行条文][R2] | 产品／地区与许可证审查政策 |
| R3 | BIS，2026-05-31；[官方一页指导][R3] | AI Diffusion不执行政策与原有中国总部／母公司管制 |
| R4 | Part 748 Supplement No.2(dd)；[现行条文][R4] | 供应、累计TPP、用户／用途、KYC和检测条件 |
| R5–R7 | eCFR §§734.16、750.7、736.2；[境内转移][R5]、[许可范围][R6]、[一般禁令][R7] | 现存、二手及调拨 |
| R8 | GAO B-337935，2026-05-12；[官方决定][R8] | AI Diffusion条文与不执行政策状态说明 |
| D1 | NVIDIA 10-Q，2026-08-26，季度截至2026-07-26；[SEC原文][D1] | H200/H20供货、许可、检测关税及受控型号 |
| D2 | AMD 10-Q，2026-08-05，季度截至2026-06-27；[公司原文][D2] | MI308发货与MI325许可、进口和检测费用 |
| S1 | HPE NVIDIA Accelerators QuickSpecs，页脚V82，2026-07-20（下载URL参数为ver=83）；[PDF][S1] | 第10页6000D；第14页L20；第15页地区脚注；旧V78仅用于版本比较 |
| S2 | HPE L20，S4A92C；[中国产品页][S2]及[独立数据表][S2a] | 48GB／864GB/s、地区、整机与300W字段 |
| S3 | HPE 6000D，S6W21C，独立表落款2026年9月；[PDF][S3] | 第1页China/HK；第3页84GB／1398GB/s、整机；第5页日期 |
| S4 | NVIDIA数据中心驱动580.159.04；[官方发布说明][S4] | RTX 6000D准确驱动名称存在；不据此推断采购许可 |
| S5 | Lenovo H200，2025-11-07更新；[产品指南][S5] | Table 1料号、Table 2规格、NVL桥接与HGX区别 |
| S6 | HPE中国NVIDIA加速卡目录；[产品目录][S6] | NVL、L系列的OEM入口 |
| S7–S8 | AMD MI300系列与MI325X平台，平台发布2024-10-10；[系列资料][S7]、[平台页][S8]、[平台数据表][S8a] | 容量、带宽、功率及八OAM互联 |
| S9 | Dell XE9680安装及服务手册，持续更新；[GPU规格][S9] | H20/H800/H200/MI300X准确服务器配置 |
| S10 | Lenovo GPU Summary，2026-09-12更新；[产品及受控表][S10] | Controlled标记、准确料号、MI210等停售日期 |
| S11–S12 | Lenovo L40及NVIDIA L4；[L40指南][S11]、[L4资料][S12] | 48GB／24GB、带宽、功率及产品状态 |
| S13 | Lenovo RTX PRO 6000 Blackwell Server Edition，2026-07-28更新；[指南][S13] | 96GB标准服务器版规格、无NVLink、受控标记 |
| S14 | HPE XD685，2024-10-10；[原厂发布][S14] | MI325X/MI300X八卡整机、风冷／液冷 |
| S15–S16 | Lenovo A800停售产品指南；AMD MI210资料持续更新；[A800][S15]、[MI210][S16] | 既有设备参考 |
| S17–S18 | AMD MI350X产品资料；Supermicro AMD整机目录；[MI350X][S17]、[Supermicro][S18] | 更高性能档与OEM平台存在 |

### 原件保存说明

本轮成功下载的公开原件集中于报告既有、被忽略的构建目录`reports/phase2-technical-research-2026-09-18/build/server-gpu-procurement/`，清单为`source-files.json`。HPE PDF已通过网页阅读工具核查，直接下载连接本轮超时；目录清单明确区分“已保存原件”与“在线读取、未保存原件”。没有改动原来源档案或全局TECH编号。

[R1]: https://www.govinfo.gov/content/pkg/FR-2026-01-15/pdf/2026-00789.pdf
[R2]: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-742/section-742.6
[R3]: https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf
[R4]: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-748/appendix-Supplement%20No.%202%20to%20Part%20748
[R5]: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.16
[R6]: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-750/section-750.7
[R7]: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-736/section-736.2
[R8]: https://www.gao.gov/products/b-337935
[D1]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[D2]: https://ir.amd.com/financial-information/sec-filings/content/0000002488-26-000123/amd-20260627.htm
[S1]: https://www.hpe.com/psnow/downloadDoc/NVIDIA%20Accelerators%20for%20HPE%20QuickSpecs-c04123180.pdf?contentDisposition=attachment&deepLink=&form=false&hf=regular&id=c04123180.pdf&isFutureVersion=true&isLinearized=false&originalObjectName=&prelaunchSection=&preview=false&print=&r=&section=&softrollSection=&utm_campaign=&utm_content=&utm_medium=&utm_source=&utm_term=&ver=83
[S2]: https://www.hpe.com/cn/zh/product-catalog/compute/accelerators/pip.nvidia-accelerators.1014837498.html
[S2a]: https://www.hpe.com/psnow/generateDDS/NVIDIA%20L20%2048GB%20PCIe%20GPU%20Accelerator%20for%20HPE%20data%20sheet-PSN1014837498WWEN.pdf?cc=WW&contentDisposition=attachment&deepLink=&isLinearized=false&lc=EN&oid=1014837498&prelaunch=false&prelaunchSection=&print=&section=&softroll=0&softrollSection=
[S3]: https://www.hpe.com/psnow/generateDDS/NVIDIA%20RTX%20PRO%206000D%2084GB%20PCIe%20Accelerator%20for%20HPE%20data%20sheet-PSN1014927525HKEN.pdf?cc=HK&deepLink=&lc=EN&oid=1014927525&prelaunch=false&prelaunchSection=&print=&section=&softroll=0&softrollSection=
[S4]: https://docs.nvidia.com/datacenter/tesla/pdf/NVIDIA_Data_Center_GPU_Driver_Release_Notes_580_v9.0.pdf
[S5]: https://lenovopress.lenovo.com/lp1944-nvidia-h200-141gb-gpu
[S6]: https://www.hpe.com/cn/zh/product-catalog/compute/accelerators/pip.models.nvidia-accelerators.4206249.html
[S7]: https://www.amd.com/en/products/accelerators/instinct/mi300.html
[S8]: https://www.amd.com/en/products/accelerators/instinct/mi300/mi325x/platform.html
[S8a]: https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/instinct-mi325x-platform-datasheet.pdf
[S9]: https://www.dell.com/support/manuals/en-au/poweredge-xe9680/xe9680_ism_pub/gpu-specifications?guid=guid-1f91b9fb-b8fd-492e-863f-45febc9355c6&lang=en-us
[S10]: https://lenovopress.lenovo.com/lp0768-thinksystem-thinkagile-gpu-summary
[S11]: https://lenovopress.lenovo.com/lp1718-nvidia-l40-48gb-pcie-gen4-passive-gpu
[S12]: https://www.nvidia.com/zh-tw/data-center/l4/
[S13]: https://lenovopress.lenovo.com/lp2263-thinksystem-nvidia-rtx-pro-6000-blackwell-server-edition-pcie-gen5-gpu
[S14]: https://www.hpe.com/us/en/newsroom/press-release/2024/10/hpe-launches-new-purpose-built-solutions-powered-by-amd-to-accelerate-training-for-large-complex-ai-models.html
[S15]: https://lenovopress.lenovo.com/lp1813-thinksystem-nvidia-a800-pcie-gpu
[S16]: https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi210.html
[S17]: https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi350x-gpu-brochure.pdf
[S18]: https://www.supermicro.com/zh_cn/accelerators/amd


**主agent整合复核（2026-09-21）：**抽查NVIDIA与AMD最新季度披露、HPE QuickSpecs V82及6000D独立数据表、1月Federal Register规则。6000D地区口径按独立表记为China/HK，L20按QuickSpecs记为中国／香港／澳门；保留其功耗冲突。


[P01]: https://m.zol.com.cn/article/11420528.html
[P02]: https://vga.zol.com.cn/1183/11838132.html
[P03]: https://viperatech.com/product/nvidia-h200-nvl-graphic-card-141-gb-passive-pcie-900-21010-0040-000
[P04]: https://configurator.exxactcorp.com/configure/TS4-118380266
[P05]: https://store.supermicro.com/us_en/8u-gpu-superserver-as-8126gs-tnmr.html
[P06]: https://www.intel.com/content/www/us/en/products/sku/240363/intel-xeon-6710e-processor-96m-cache-2-40-ghz/specifications.html
[P07]: https://memory.net/product/mem-dr564mc-er56-supermicro-1x-64gb-ddr5-5600-rdimm-pc5-44800r-dual-rank-x4-replacement/
[P08]: https://www.star-networking.com/products/hpe-p76706-b21.html
[P09]: https://www.cdw.com/product/nvidia-h200-nvl-accelerator-gpu-computing-processor-h200-tensor-core/8299396
[T01]: https://www.hpe.com/us/en/collaterals/collateral.a00047453enw.html
[T02]: https://support.hpe.com/hpesc/public/docDisplay?docId=sd00005071en_us&docLocale=en_US&page=GUID-78D09FA3-09AA-42EA-838F-D55402AEE195.html
[T03]: https://www.npc.gov.cn/npc/c2/c30834/202412/t20241225_442038.html
