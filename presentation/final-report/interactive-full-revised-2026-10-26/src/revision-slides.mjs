export function revisedContent(s,d,H){
 const {rect,txt,node,line,arrow,elbow,heading,strip,steps,table,clientDoc,material,C}=H;
 function task(n,role,body,x,y,w,h=150,kind='human',size=25){const fill=kind==='llm'?C.pale:kind==='tool'?C.mint:C.very,color=kind==='llm'?C.blue:kind==='tool'?C.teal:C.ink;rect(s,n,x,y,w,h,fill);txt(s,n+'.role',role,x+20,y+15,w-40,34,24,color,true);txt(s,n+'.body',body,x+20,y+61,w-40,h-68,size,C.ink);}
 function evidence(n,title,body,x,y,w,h,size=23){line(s,n+'.rule',x,y,x+w,y,C.line);txt(s,n+'.label',title,x,y+10,w,31,22,C.blue,true);txt(s,n+'.text',body,x,y+46,w,h-46,size);}
 function take(n,v,y=741,size=26){txt(s,n,v,426,y,1106,43,size,C.ink);}
 switch(d.page){
 case 8:{
 node(s,'research.question','研究员：本季度收入为何增长，增长能否持续？',426,215,1106,68,{fill:C.very,color:C.ink,size:30});
 evidence('research.evidence.1','[1] 财报（上季 / 本季）','收入（百万元）：100 / 110\n销量（万件）：100 / 110',426,310,310,100,22);
 evidence('research.evidence.2','[2] 会议纪要','渠道补库带动发货',426,426,310,70,23);
 evidence('research.evidence.3','[3] 两份研报','A：需求恢复可持续\nB：补库持续性待观察',426,512,310,92,23);
 task('research.llm','LLM读材料、组织分析','选取收入与销量比较\n联系会议中的经营解释\n对照研报的不同判断',783,310,339,294,'llm',25);
 task('research.tool','计算工具：收入与销量增幅','收入增长10%\n销量增长10%\n平均单价不变',1174,310,358,294,'tool',27);
 line(s,'research.material.bus',758,368,758,558,C.blue,1.8);[368,459,558].forEach((y,i)=>line(s,'research.material.in'+i,736,y,758,y,C.blue,1.8));arrow(s,'research.evidence.in',758,458,773,458);arrow(s,'research.call',1132,408,1164,408);arrow(s,'research.return',1164,537,1132,537);

 arrow(s,'research.toResult',952,611,952,625);rect(s,'research.result',426,633,1106,93,C.white,C.line);heading(s,'research.result.title','LLM形成分析',446,652,203,26);
 txt(s,'research.result.text','收入增长来自销量提升[1]，渠道补库带动发货[2]。\n研报对持续性看法不同[3]，继续跟踪需求与成本。',677,649,830,69,25);
 take('research.user','研究员核对出处，追问补库持续性，形成研究判断',747,26);break;}
 case 9:{
 heading(s,'trade.task','任务：准备甲公司两年内到期债券的买入询价资料',426,215,1106,32);
 const xs=[426,710,994,1278],w=254;
 task('trade.intent','1  投资经理','拟买入甲公司债券\n两年内到期\n列出现有持仓\n汇总卖方报价',xs[0],310,w,205,'human',24);
 task('trade.query','2  交易员查数据','查候选券与持仓\n记录数据时间',xs[1],310,w,205,'human',24);
 task('trade.inquire','3  交易员询价','报出候选券名\n说明买入需求\n询问价格与可出量\n接收对手报价',xs[2],310,w,205,'human',24);
 task('trade.compare','4  交易员汇总','整理候选券与报价\n供经理讨论\n后续交易安排',xs[3],310,w,205,'human',24);
 ['经理需求','候选券','报价资料'].forEach((v,i)=>{arrow(s,'trade.sequence'+i,xs[i]+w+5,408,xs[i+1]-9,408);txt(s,'trade.sequence'+i+'.label',v,xs[i]+w-35,269,100,31,21,C.muted,false,'center');});
 task('trade.system','行情与持仓系统','返回查询数据',710,582,254,113,'tool',24);arrow(s,'trade.data',837,572,837,524);txt(s,'trade.data.label','查询结果',849,538,128,31,21,C.teal);
 task('trade.counterparty','交易对手','返回债券报价',994,582,254,113,'human',24);arrow(s,'trade.ask',1053,524,1053,572);arrow(s,'trade.quote.return',1183,572,1183,524);txt(s,'trade.ask.label','询价',1004,538,57,29,20,C.muted);txt(s,'trade.quote.label','报价',1195,538,57,29,20,C.muted);
 take('trade.repetition','重复操作：填查询条件、切换系统、从聊天中抄录报价',744,27);break;}
 case 11:{
 node(s,'trade.intent','经理：拟买入甲公司两年内到期债券，查持仓并汇总卖方报价',426,215,1106,68,{fill:C.very,color:C.ink,size:29});
 task('trade.llm.query','LLM理解查询要求','主体：甲公司\n意向：买入\n期限：两年内到期\n查询：候选券与持仓',426,326,338,207,'llm',25);
 task('trade.system','业务系统执行查询','返回甲公司债 A\n期限1.2年\n持仓面额2000万元',810,326,338,207,'tool',25);
 task('trade.llm.quote','LLM读取对手聊天','“甲A卖方净价100.20，\n面额2000万元可出”\n提取券名、净价与面额',1194,326,338,207,'llm',24);
 arrow(s,'trade.query.call',773,421,801,421);arrow(s,'trade.quote.merge',979,542,979,581);arrow(s,'trade.chat.merge',1363,542,1363,581);
 heading(s,'trade.result.title','LLM归并查询结果和报价',426,552,520,28);
 table(s,d,'trade.result',['候选券 / 到期','持仓面额（万元）','净价（元/百元面值）','可出面额（万元）'],[['甲A / 1.2年','2000','100.20','2000']],426,598,1106,126,[285,255,296,270],23);
 take('trade.user','交易员核对原话与报价时间，经理据此讨论后续安排',746,26);break;}
 case 27:{
 node(s,'dev.request','业务要求：比较两版报告，忽略重复页眉，标出正文改写',426,215,1106,68,{fill:C.very,color:C.ink,size:29});
 task('dev.samples','1  开发同事提供样例','两版客户沟通稿\n标出预期差异位置',426,335,338,150,'human',25);
 task('dev.generate','2  LLM整理要求并写代码','按段落比较正文\n生成程序和测试样例',810,335,338,150,'llm',25);
 task('dev.test','3  测试工具执行程序','正文改写已识别\n页眉变化被误报',1194,335,338,150,'tool',25);
 task('dev.deliver','6  开发同事复测并提供','检查代码、运行测试\n提供工具与操作说明',426,580,338,150,'human',25);
 task('dev.revise','5  LLM按反馈修改','修改页眉过滤代码\n补充页眉变化测试',810,580,338,150,'llm',25);
 task('dev.feedback','4  开发同事说明问题','页眉差异无需报告\n正文差异必须保留',1194,580,338,150,'human',25);
 arrow(s,'dev.toLLM',774,409,800,409);arrow(s,'dev.toTest',1158,409,1184,409);arrow(s,'dev.testFeedback',1363,495,1363,570);txt(s,'dev.testFeedback.label','运行结果',1380,518,152,37,22,C.teal);arrow(s,'dev.toRevise',1184,654,1158,654);arrow(s,'dev.toDelivery',800,654,774,654);
 break;}
 case 4:{
 node(s,'research.question','研究员要回答：收入为何增长，增长能否持续？',426,215,1106,68,{fill:C.very,color:C.ink,size:30});
 evidence('research.evidence.1','[1] 财报（上季 / 本季）','收入（百万元）：100 / 110\n销量（万件）：100 / 110',426,333,338,133,24);
 evidence('research.evidence.2','[2] 会议纪要','渠道补库带动发货，\n补库持续性仍需跟踪。',810,333,338,133,24);
 evidence('research.evidence.3','[3] 两份研报','A判断需求恢复可持续，\nB关注补库持续性。',1194,333,338,133,24);

 heading(s,'research.manual.title','研究员的准备工作',426,538,1106,28);
 steps(s,'research.manual',['找出相关材料','抄录并计算变化','重读和比较观点','写出分析依据'],426,593,1106,83,25,C.very);
 take('research.repetition','反复检索、抄录和核对之后，才能集中判断经营变化',737,27);break;}
 case 5:{
 heading(s,'driver.llm.title','LLM拆解研究问题，计算工具完成取数与计算',426,215,1106,31);
 node(s,'driver.root','净利润\n变化',426,421,180,110,{fill:C.blue,color:C.white,size:30});
 [['revenue','收入','销量、单价',315],['cost','成本','原材料、生产成本',460],['expense','费用','渠道、销售费用',605]].forEach(([k,a,b,y])=>{node(s,'driver.'+k+'.node',a,723,y,178,77,{size:29});node(s,'driver.'+k+'.factor',b,1015,y,359,77,{fill:C.very,size:27});elbow(s,'driver.'+k+'.branch',606,476,723,y+38,661);arrow(s,'driver.'+k+'.link',908,y+38,1005,y+38);});
 node(s,'driver.tools','数据接口\n计算工具',1402,315,130,367,{fill:C.mint,color:C.teal,size:25});
 take('driver.result','LLM联系经营资料解释变化，研究员据此判断增长质量',736,27);break;}
 case 6:{
 heading(s,'views.llm.title','LLM按同一研究问题，逐篇阅读并对照观点',426,215,1106,31);
 evidence('views.reportA','研报 A','销量增长带动收入。\n需求恢复支持持续增长。',426,330,338,197,28);
 evidence('views.reportB','研报 B','渠道补库带动发货。\n补库持续性仍待观察。',810,330,338,197,28);
 task('views.method','富国的LLM处理','筛选相关研报\n按研究方向整理小结\n汇总并检查表述',1194,330,338,197,'llm',25);
 rect(s,'views.result',426,592,1106,126,C.white,C.line);
 heading(s,'views.consensus.title','LLM汇总共识',448,613,450,27);txt(s,'views.consensus.body','销量增长支持本期收入',448,661,450,43,26);
 heading(s,'views.difference.title','LLM保留分歧',1010,613,500,27);txt(s,'views.difference.body','持续需求恢复，还是阶段性补库？',1010,661,500,43,26);
 take('views.user','研究员从分歧继续查证，分析中保留对应研报出处',745,26);break;}
 case 7:{
 heading(s,'elements.head','LLM把资料中的判断填入研究分析表',426,215,1106,32);
 strip(s,'elements.left','资料接口提供材料',426,291,307);strip(s,'elements.right','LLM填写研究要素表示例',790,291,742);
 [['财报与计算结果','销量增长10%','经营变化'],['会议纪要','渠道补库带动发货','驱动因素'],['两份研报','补库持续性仍有分歧','关注事项']].forEach(([a,b,c],i)=>{const y=375+i*103;node(s,'element.'+i+'.source',a,426,y,307,72,{fill:C.very,size:25});arrow(s,'element.'+i+'.arrow',743,y+36,777,y+36);txt(s,'element.'+i+'.label',c,813,y+17,196,45,25,C.blue,true);txt(s,'element.'+i+'.value',b,1035,y+17,472,45,26);line(s,'element.'+i+'.rule',790,y+82,1532,y+82);});
 txt(s,'elements.stat','中欧披露：整体编制效率提升约50%（截至2026年5月）',426,707,1106,41,26,C.blue,true);
 take('elements.user','研究员核对填报内容与出处，补充自己的判断',751,25);break;}
 case 12:{
 heading(s,'client.task','客户经理准备一份季度沟通稿',426,215,1106,32);
 evidence('client.question','客户的问题','本期公司经营发生了什么变化？\n后续需要关注什么？',426,313,1106,118,30);
 ['经理观点','产品文件','以往沟通材料'].forEach((v,i)=>node(s,'client.material'+i,v,426+i*384,474,338,68,{fill:C.very,color:C.ink,size:28}));
 heading(s,'client.manual.title','客户经理反复完成',426,584,1106,28);steps(s,'client.manual',['找对应观点','核对产品与期次','按客户问题改写'],426,636,1106,79,26,C.very);
 take('client.repetition','同一观点在沟通稿、问答和标书中需要多次整理',749,27);break;}
 case 13:{
 heading(s,'client.views.head','天弘让LLM汇集同一经理或产品的近期观点',426,215,1106,31);
 evidence('client.views.source','路演纪要、评论与定期报告','“甲公司收入增长来自销量提升，\n后续关注原材料成本。”',426,330,470,195,28);
 task('client.views.llm','LLM按客户问题整理','寻找相关观点\n合并重复内容\n写成便于沟通的解释',978,330,554,195,'llm',27);arrow(s,'client.views.input',908,427,966,427);
 rect(s,'client.views.result',426,584,1106,126,C.white,C.line);heading(s,'client.views.result.title','销售可直接使用的观点摘要',448,605,1062,28);txt(s,'client.views.result.text','本期收入改善主要来自销量提升，后续继续跟踪原材料成本。',448,657,1062,43,27);
 take('client.views.user','天弘还将市场资料整理成行业周评、每日早评和收评',748,26);break;}
 case 14:{
 node(s,'tender.question','机构客户问：公司的投研流程怎样组织？',426,215,1106,68,{fill:C.very,color:C.ink,size:30});
 evidence('tender.source','公司知识资料','研究流程说明\n研究员形成公司分析，\n投资经理讨论投资判断。',426,337,338,220,26);
 task('tender.llm','LLM识别问题并组织回答','找到“投研流程”资料\n提取研究与决策的分工\n按标书章节写成回答',810,337,338,220,'llm',25);
 task('tender.answer','标书中的回答','研究员整理公司分析，\n投资经理讨论投资判断。\n出处：投研流程说明',1194,337,338,220,'human',25);
 arrow(s,'tender.input',774,447,800,447);arrow(s,'tender.output',1158,447,1184,447);
 take('tender.user','业务同事核对回答与资料，补充本次客户要求后使用',649,27);
 txt(s,'tender.case','工银瑞信FundGPT串联知识维护、问答识别、审核与标书生成',426,723,1106,50,25,C.blue,true);break;}
 case 15:{
 node(s,'client.input.customer','客户问题\n本期关注什么？',426,297,230,100,{fill:C.very,color:C.ink,size:24});
 node(s,'client.input.manager','现有观点\n销量与原料成本',426,458,230,100,{fill:C.very,color:C.ink,size:24});
 node(s,'client.input.product','现有产品资料\n二季度 V1',426,619,230,100,{fill:C.very,color:C.ink,size:24});
 [347,508,669].forEach((y,i)=>elbow(s,'client.input.link'+i,656,y,745,508,697));
 task('client.llm','LLM撰写材料','提取相关观点\n按季度沟通\n组织文字',745,403,210,207,'llm',24);arrow(s,'client.generate',962,508,998,508);
 clientDoc(s,material.v1,1008,245,524,510,{compact:true});
 txt(s,'client.user','客户经理核对观点，再将同一份沟通稿提交审核',426,753,550,40,23,C.ink);break;}
 case 16:{
 clientDoc(s,material.v1,426,289,690,435,{mark:['view']});
 evidence('review.reference','审核同事查阅的本期路演','“渠道补库带动销量，\n补库持续性仍需跟踪。”',1174,289,358,165,25);
 heading(s,'review.questions.title','审核时需要判断',1174,497,358,28);txt(s,'review.questions','稿件是否讲清增长原因？\n是否保留后续观察事项？',1174,554,358,116,26);
 take('review.manual','逐段对照原文，还要核对产品名称、资料期次与风险提示',749,26);break;}
 case 17:{
 clientDoc(s,material.v1,426,289,690,435,{mark:['product','period','view','risk']});
 const cs=[['meta','LLM对照本期资料','名称与期次沿用旧版\n建议按本期资料更新',420,285],['view','LLM比较观点含义','原文：补库推动、持续性待观察\n建议补充原因与观察事项',562,443],['risk','LLM补全风险表述','资料：净值波动、本金亏损\n建议写明两项风险',649,601]];
 cs.forEach(([k,a,b,sy,y])=>{task('comment.'+k,a,b,1174,y,358,139,'llm',22);elbow(s,'comment.'+k+'.lead',1116,sy,1174,y+69,1144);});
 take('review.case','鹏华按规则给修改建议；盈米把预审、修改与复查接到写作过程',753,24);break;}
 case 18:{
 task('review.inputs','同事提供稿件和本期资料','V1沟通稿、产品资料V2\n完整路演：补库推动，持续性待观察',426,245,524,125,'human',24);
 task('review.tool','文件工具定位差异','匹配产品名称、资料期次及原文位置',426,394,524,115,'tool',24);
 task('review.llm','LLM解释并修改表述','补充“渠道补库”这一经营原因\n加入“补库持续性”的跟踪事项\n按产品资料补充具体风险',426,533,524,176,'llm',25);
 clientDoc(s,material.v2,1008,245,524,510,{compact:true,mark:['product','period','view','risk'],revised:true});
 arrow(s,'review.toRevision',962,621,997,621);
 take('review.user','作者确认改写，审核人查看原文、修改理由与修订稿',755,25);break;}
 case 19:{
 evidence('risk.mail','风险同事收到邮件','甲公司被列入评级观察，\n原因是经营现金流承压。',426,255,1106,144,31);
 heading(s,'risk.manual.title','风险同事接着查三件事',426,453,1106,29);
 task('risk.question.0','哪些产品相关？','查持仓系统，\n核对产品和数量',426,515,338,155,'human',27);
 task('risk.question.1','按什么要求跟踪？','查合同、内控制度，\n找对应条款',810,515,338,155,'human',27);
 task('risk.question.2','影响怎样解释？','重读公司研究，\n整理事件说明',1194,515,338,155,'human',27);
 take('risk.repetition','逐封读邮件，再跨系统和文件查找同一发行人的信息',745,27);break;}
 case 20:{
 strip(s,'risk.htf','汇添富基金',426,230,521);strip(s,'risk.th','天弘基金',1011,230,521);
 task('risk.mail.extract','LLM读托管行风控邮件','提取涉及的风险内容，\n送到风险人员工作台',426,319,521,139,'llm',26);
 task('risk.rules.tool','系统保存规则与原文的对应','风控规则关联法规、\n内控制度和合同条款',426,489,521,139,'tool',26);
 txt(s,'risk.rules.explain','LLM据原文解释触发规则的依据',426,661,521,77,27,C.blue,true);
 evidence('risk.event.input','事件材料','事件详情、历史相似事件、\n产业链关联和市场情绪',1011,319,521,139,27);
 task('risk.event.llm','LLM组织事件解释','比较历史事件与当前情况，\n梳理影响方向和相关事项',1011,489,521,139,'llm',26);
 txt(s,'risk.event.user','投资与风险同事据此讨论事件影响',1011,661,521,77,27,C.ink);break;}
 case 21:{
 evidence('risk.evidence.mail','邮件原文','甲公司评级观察，\n经营现金流承压。',426,252,338,122,26);
 task('risk.evidence.system','持仓查询返回','产品A持有甲公司债券\n持仓面额2000万元',426,410,338,139,'tool',25);
 evidence('risk.evidence.rule','跟踪要求','信用事件发生后，\n更新发行人研究。',426,585,338,123,25);
 task('risk.llm','LLM连接事件与资料','识别邮件中的发行人\n把持仓对应到产品A\n对照条款和既有研究\n组织影响说明',810,299,338,301,'llm',26);
 task('risk.result','影响说明与后续事项','现金流承压涉及偿债能力\n需要更新信用判断。\n\n相关产品：产品A\n补充研究：现金流变化',1194,299,338,371,'human',25);
 line(s,'risk.material.bus',786,330,786,646,C.blue,1.8);[330,479,646].forEach((y,i)=>line(s,'risk.material.in'+i,764,y,786,y,C.blue,1.8));arrow(s,'risk.toLLM',786,452,800,452);arrow(s,'risk.toResult',1158,452,1184,452);
 take('risk.user','风险同事复核持仓与条款，研究员补充分析，投资经理讨论应对',748,25);break;}
 case 22:{
 ['接收的材料','运营同事完成','保存的结果'].forEach((v,i)=>strip(s,'ops.head'+i,v,426+i*378,231,350));
 [['传真与扫描件','抄录字段后逐项核对','业务记录'],['客户材料 V1 / V2','逐段找改动、解释含义','差异清单'],['同类电子文件','逐份修改同一内容','更新文件']].forEach((r,i)=>{const y=345+i*137;r.forEach((v,j)=>node(s,'ops.row'+i+'.'+j,v,426+j*378,y,350,87,{fill:C.very,color:C.ink,size:25}));arrow(s,'ops.a'+i,782,y+43,796,y+43);arrow(s,'ops.b'+i,1160,y+43,1174,y+43);});
 take('ops.repetition','费时之处：从文件搬运信息，阅读上下文解释修改含义',754,26);break;}
 case 23:{
 strip(s,'ops.huaan','华安  单据智能录入',426,228,352);task('ops.form','识别传真与单据','读取单据内容\n提取业务字段\n用于柜面录入',426,318,352,236,'tool',28);txt(s,'ops.stat','华安披露：超过80%\n柜面传真采用智能录入',426,609,352,109,26,C.blue,true);
 strip(s,'ops.icbc','工银瑞信  多格式文档比对',822,228,710);txt(s,'ops.formats','PDF、Word、扫描件',822,310,710,37,26,C.muted);
 node(s,'ops.compare.read','模型识别文档内容，比较两个版本',822,364,710,69,{fill:C.pale,color:C.blue,size:27});
 heading(s,'ops.compare.old.label','V1观点',822,470,710,24);txt(s,'ops.compare.old.text','甲公司收入增长来自销量提升，\n后续关注原材料成本。',822,513,710,68,26);
 heading(s,'ops.compare.new.label','V2观点：新增文字已标出',822,599,710,24);
 rect(s,'ops.compare.mark.driver',1030,641,104,34,C.mark);rect(s,'ops.compare.mark.watch',926,682,130,34,C.mark);
 txt(s,'ops.compare.new.line1','甲公司销量提升与渠道补库有关，',822,641,710,39,26);txt(s,'ops.compare.new.line2','后续关注补库持续性及原材料成本。',822,682,710,39,26);
 txt(s,'ops.compare.functions','差异呈现、错别字识别、结果导出',822,748,710,35,24,C.blue,true);break;}
 case 24:{
 task('ops.inputs','运营同事提供两版客户稿','基金季度客户沟通稿 V1 / V2',426,245,524,111,'human',25);
 task('ops.tool','文件工具对齐段落','定位名称、期次和观点的文字改动',426,381,524,112,'tool',25);
 task('ops.llm','LLM解释变化的业务含义','对照前后文，区分新增与保留内容\n说明观点怎样变化\n列出需要同步修改的材料',426,518,524,183,'llm',25);
 rect(s,'changeLog',1008,245,524,510,C.white,C.line);heading(s,'changeLog.title','客户沟通稿变更说明',1033,266,474,29);txt(s,'changeLog.object','基金季度客户沟通稿 V1 / V2',1033,315,474,37,22,C.muted);line(s,'changeLog.rule',1033,367,1507,367);
 [['driver','新增经营原因','销量提升与渠道补库有关'],['watch','观察事项的变化','增加补库持续性，保留原材料成本跟踪'],['sync','需要同步更新','其他沟通稿与产品问答中的相关观点']].forEach(([k,a,b],i)=>{const y=391+i*115;heading(s,'changeLog.'+k+'.label',a,1033,y,474,25);txt(s,'changeLog.'+k+'.body',b,1033,y+43,474,66,25);});
 arrow(s,'ops.explain.toLog',961,609,998,609);
 take('ops.user','运营同事核对变更说明，随V2保存，并更新相关材料',754,25);break;}
 case 25:{
 node(s,'dev.request','业务同事：两版报告改了哪里？页眉日期变化不算正文差异',426,215,1106,68,{fill:C.very,color:C.ink,size:28});
 task('dev.requirements','开发同事整理要求','标出新增、删除、改写\n忽略重复页眉',426,348,338,220,'human',25);
 task('dev.code','开发同事编写程序','读取文件，匹配正文段落\n计算文字差异，输出位置',810,348,338,220,'human',25);
 task('dev.debug','开发同事反复测试','换行和跨页会打乱匹配\n页眉变化可能被误报',1194,348,338,220,'human',25);
 arrow(s,'dev.req.code',774,458,800,458);arrow(s,'dev.code.debug',1158,458,1184,458);
 take('dev.workload','从一句业务要求到可用工具，要写程序、准备样例并反复定位问题',678,27);
 break;}
 case 26:{
 heading(s,'dev.case1','易方达：大模型进入开发与测试环节',426,215,1106,31);txt(s,'dev.case2','景顺长城：量化团队使用本地模型辅助编程',426,268,1106,44,27,C.muted);
 task('dev.requirements','开发同事提出要求','给业务样例和预期结果\n说明程序需要完成的动作',426,370,338,212,'human',26);
 task('dev.code','LLM辅助生成代码与测试','编写文件处理程序\n列出测试场景与预期结果',810,370,338,212,'llm',26);
 task('dev.test','开发同事运行与反馈','运行程序，核对真实结果\n把错误信息交给LLM修改',1194,370,338,212,'human',26);
 arrow(s,'dev.case.in',774,476,800,476);arrow(s,'dev.case.out',1158,476,1184,476);
 node(s,'dev.case.result','开发同事使用模型生成的程序和测试，持续修改到可以使用',426,670,1106,75,{fill:C.mint,color:C.teal,size:27});break;}
 case 28:{
 [['内部办事','招商、平安','政策与流程问题','LLM查资料并解释','办理指引'],['邮件安全','永赢','邮件、附件与链接','LLM判断意图\n调用检测工具','安全处置'],['经营分析','汇添富公开专利提出','产品、期间与指标','LLM识别问题\n算法计算归因','LLM整理分析报告']].forEach(([a,b,c,e,f],i)=>{const y=225+i*178;heading(s,'other.'+i+'.title',a,426,y,235,30);txt(s,'other.'+i+'.company',b,682,y+3,850,38,24,C.muted);steps(s,'other.'+i+'.flow',[c,e,f],426,y+62,1106,78,24,i===2?C.very:C.pale);});break;}
 case 31:{
 node(s,'arch.entry','同事提出业务问题并提供材料',426,229,1106,65,{fill:C.very,color:C.ink,size:30});arrow(s,'arch.a',979,303,979,340);
 node(s,'arch.workflow','研究、询价、客户材料、审核、风险、文件处理、开发',426,352,1106,78,{size:27});line(s,'arch.b.stem',979,440,979,458,C.blue,2);line(s,'arch.b.bus',672,458,1273,458,C.blue,2);arrow(s,'arch.b.model',672,458,672,478);arrow(s,'arch.b.tools',1273,458,1273,478);
 task('arch.model','LLM处理语言与内容','理解问题、阅读材料\n比较解释、生成文字与代码',426,488,491,150,'llm',26);task('arch.tools','工具执行具体操作','查询、计算、文件处理\n程序运行与测试',1013,488,519,150,'tool',26);
 txt(s,'arch.data','共用资料：文档、知识库、业务数据，保留权限、出处与版本',426,680,1106,57,26,C.ink);txt(s,'arch.models','模型服务候选：Qwen、DeepSeek等，按具体任务验证',426,746,1106,35,24,C.muted);break;}

 case 10:{
 strip(s,'trade.southern','南方基金  小喃同学',426,230,1106);
 const xs=[426,710,994,1278],w=254;
 [['自然语言请求','用户说明筛券、\n查询或操作要求','human'],['LLM解析与调度','理解要求和参数，\n调用相应工具','llm'],['数据库与业务接口','实际查询或操作，\n返回处理结果','tool'],['用户使用结果','查看候选与数据，\n确认后继续操作','human']].forEach(([a,b,k],i)=>{task('trade.case1.'+i,a,b,xs[i],310,w,139,k,24);if(i<3)arrow(s,'trade.case1.link'+i,xs[i]+w+5,379,xs[i+1]-9,379);});
 txt(s,'trade.case1.scope','小喃支持查询、筛券、交易指令与消息推送',426,470,1106,40,26,C.blue,true);
 strip(s,'trade.xq','兴证全球基金  千询的成交语料录入',426,538,1106);
 [['Qtrade成交语料','聊天中的券名、\n方向、价格与数量','human'],['AI提取交易信息','把聊天内容转成\n系统所需信息','llm'],['匹配询价并推送','匹配经理询价\n推送交易系统','tool'],['经理下达指令','经理在交易系统\n完成指令下达','human']].forEach(([a,b,k],i)=>{task('trade.case2.'+i,a,b,xs[i],617,w,139,k,24);if(i<3)arrow(s,'trade.case2.link'+i,xs[i]+w+5,686,xs[i+1]-9,686);});break;}

 default:return false;
 }
 return true;
}
