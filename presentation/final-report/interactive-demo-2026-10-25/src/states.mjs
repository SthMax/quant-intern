export const material={
 title:'基金季度客户沟通稿',
 v1:{version:'V1',product:'产品A精选',period:'2026年二季度产品资料V1',view:'甲公司收入增长来自销量提升，后续关注原材料成本',risk:'投资有风险'},
 v2:{version:'V2',product:'产品A精选混合型基金',period:'2026年三季度产品资料V2',view:'甲公司收入增长来自销量提升，后续关注原材料成本',risk:'基金净值随市场波动，投资本金可能亏损'}
};
export const citations={
 front:'天弘基金FinAgent案例，FUND-300，PDF第7–9页。https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf',
 middle:'鹏华基金营销材料审核案例，FUND-308，PDF第6页。https://www.amac.org.cn/xwfb/hydt/202601/P020260202337850951100.pdf\n盈米基金销售内容合规审查发布与客户端流程。https://www.yingmi-inc.com/archives/799',
 back:'工银瑞信基金FundGPT文档比对案例，FUND-312，PDF第7页。https://www.amac.org.cn/xwfb/hydt/202601/P020260202337848496316.pdf'
};
export const states=[
 {page:1,active:'all',title:'公司工作地图',focus:'一份客户材料的工作过程',seconds:20,notes:'公司前台形成研究和客户材料，中台完成审核与风险分析，后台承接运营文件和工具支持。下面沿着一份季度客户沟通稿，连续展示资料进入、内容形成、审核修改和版本更新。',source:['front','middle','back']},
 {page:2,active:'front',title:'公司工作地图',focus:'前台：准备客户沟通资料',seconds:25,notes:'前台同事先明确客户问题与沟通用途，再调取经理观点和产品资料。资料在同一项任务中汇合，减少逐份查找和复制。此处围绕产品A精选，准备一份季度客户沟通稿。',source:['front']},
 {page:3,active:'front',title:'公司工作地图',focus:'LLM 整理资料并撰写',seconds:35,notes:'LLM围绕本期关注问题整理资料，提取观点并组织成客户表达。右侧形成沟通稿V1，包含产品名称、资料期次、本期观点与风险提示。前台同事据此补充内容，再将同一份材料送入审核。',source:['front']},
 {page:4,active:'middle',title:'公司工作地图',focus:'中台：审核同一份沟通稿',seconds:25,notes:'这份沟通稿进入中台后，审核围绕材料内容逐项开展。产品名称需要对应正式文件，引用资料需要使用本期期次，风险提示需要覆盖产品风险。审核意见会直接连接到原文位置。',source:['middle']},
 {page:5,active:'middle',title:'公司工作地图',focus:'问题定位与修改动作',seconds:45,notes:'先看产品名称，按本期文件补充正式全称。再看资料期次，将二季度资料更新为三季度V2。最后看风险提示，将简短提示补充为净值波动和本金亏损的说明。模型把问题位置与修改动作交给作者，审核人继续确认依据和表述。',source:['middle']},
 {page:6,active:'middle',title:'公司工作地图',focus:'修订稿 V2 与变更内容',seconds:30,notes:'修订稿保留原来的研究观点，更新产品正式名称、资料期次和风险提示。再次检查后，材料与修改记录一起进入后续文件维护，前台和中台继续使用同一个版本。',source:['middle']},
 {page:7,active:'back',title:'公司工作地图',focus:'后台：比对 V1 与 V2',seconds:30,notes:'后台同时接收原稿与修订稿，按相同字段对照内容。名称、资料期次和风险提示发生变化，本期观点保持一致。版本比对把逐段寻找差异的工作转为可以直接查看的修改结果。',source:['back']},
 {page:8,active:'back',title:'公司工作地图',focus:'变更清单与更新文件',seconds:30,notes:'比对结果整理为变更清单，并与更新后的客户沟通稿V2一起保存。清单记录修改位置与内容，便于同事复核以及更新相关材料。相同产品的其他沟通文件可以复用本次更新要求。',source:['back']},
 {page:9,active:'all',title:'公司工作地图',focus:'客户材料贯穿前台、中台与后台',seconds:20,notes:'回到公司总图，这份材料依次完成前台生成、中台审核和后台更新。LLM在资料整理、问题定位和文件处理环节参与工作，交付物沿流程连续复用。公司可从客户材料这条流程启动应用，再连接其他日常工作。',source:['front','middle','back']}
];
