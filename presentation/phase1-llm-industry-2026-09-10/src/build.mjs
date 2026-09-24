import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {Presentation,PresentationFile,FileBlob} from '@oai/artifact-tool';

const WS=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const REPO=path.resolve(WS,'../..');
const SKILL='/Users/sthmax/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations';
const PYTHON='/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
process.env.RUNTIME_NODE_MODULES='/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
process.env.RUNTIME_NODE=process.execPath;
process.env.RUNTIME_PYTHON=PYTHON;
const OUT=path.join(WS,'output',process.env.DECK_FILENAME??'fund-llm-industry-2026-09-10-final.pptx');
const TMP=path.join(WS,'.build');
const {resolvePresentationFont,applyPresentationChartFont,finalizePresentation}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')).href);
const font=resolvePresentationFont({fontFamily:'Heiti SC'});
const colors={navy:'#19374D',teal:'#008C83',ink:'#253C4A',muted:'#566975',gray:'#CBD5DA',pale:'#EFF5F6',white:'#FFFFFF',gold:'#9E6F28'};
const reportDir=path.join(REPO,'reports/phase1-llm-industry-2026-09-09');
const refs=JSON.parse(await fs.readFile(path.join(reportDir,'data/source-manifest.json'),'utf8'));
const refMap=Object.fromEntries(refs.map(x=>[x.id,x]));
const p=Presentation.create({slideSize:{width:1280,height:720}});
const tableOwners=[],chartOwners=[],coverage=[];

function txt(s,text,x,y,w,h,size=28,color=colors.ink,bold=false,align='left'){
 const t=s.shapes.add({geometry:'textbox',name:`text-${s.id??''}-${text.slice(0,16)}`,position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 t.text=text;t.text.style={typeface:font,fontSize:size,color,bold,alignment:align,verticalAlignment:'top',autoFit:'none',wrap:'square',insets:{top:0,bottom:0,left:0,right:0}};
 return t;
}
function slide(title,{sub='',dark=false,foot='',footY=645}={}){
 const s=p.slides.add();s.background.fill=dark?colors.navy:colors.white;
 const i=p.slides.items?.length??coverage.length+1;
 txt(s,title,64,43,1152,78,44,dark?colors.white:colors.navy,true);
 if(sub)txt(s,sub,66,132,1148,56,26,dark?'#C9DFE3':colors.muted);
 if(foot)txt(s,foot,66,footY,1090,43,20,dark?'#C9DFE3':colors.muted);
 txt(s,String(coverage.length+1).padStart(2,'0'),1190,672,34,28,17,dark?'#C9DFE3':colors.muted,false,'right');
 coverage.push({slide:coverage.length+1,title,sourceIds:[]});return s;
}
function note(s,text,ids=[]){
 const n=coverage.at(-1);n.sourceIds=ids;
 const cite=ids.map(id=>{const r=refMap[id];if(!r)throw new Error('Missing source '+id);return `${r.title}\n${r.date_label}\n${r.locator}\n${r.url}`;}).join('\n\n');
 s.speakerNotes.textFrame.setText(text+(cite?'\n\n资料来源\n'+cite:''));
}
function table(s,values,{x=64,y=210,w=1152,h=370,widths=null,fontSize=26,header=colors.navy,rowHeights=null,firstColBold=false,pad=10}={}){
 const rows=values.length,cols=values[0].length;
 const t=s.tables.add({rows,columns:cols,left:x,top:y,width:w,height:h,columnWidths:widths??Array(cols).fill(w/cols),values:values.map(row=>row.map(cell=>typeof cell==='string'?cell.replace(/。$/,''):cell))});
 t.styleOptions={headerRow:true,bandedRows:false};
 t.cells.block({row:0,column:0,rowCount:rows,columnCount:cols}).assign({fill:colors.white,textStyle:{typeface:font,fontSize,color:colors.ink,lineSpacing:1.05},margins:{left:14,right:14,top:pad,bottom:pad},anchor:'center'});
 t.borders.assign({style:'solid',fill:colors.gray,color:colors.gray,width:0.6});
 t.cells.block({row:0,column:0,rowCount:1,columnCount:cols}).assign({fill:header,textStyle:{typeface:font,fontSize,bold:true,color:colors.white}});
 if(firstColBold&&rows>1)t.cells.block({row:1,column:0,rowCount:rows-1,columnCount:1}).assign({textStyle:{typeface:font,fontSize,bold:true,color:colors.navy}});
 if(rowHeights)rowHeights.forEach((v,i)=>t.rows[i].height=v);
 tableOwners.push(coverage.length);return t;
}
function chart(s,categories,series,{x=64,y=205,w=780,h=385,max=1.2,major=.2,format='0.00',legend=true}={}){
 const c=s.charts.add('bar',{position:{left:x,top:y,width:w,height:h},categories,series:series.map(a=>({...a,valuesFormatCode:format})),barOptions:{direction:'column',grouping:'clustered',gapWidth:110},hasLegend:legend,legend:{position:'bottom',overlay:false,textStyle:{typeface:font,fontSize:23,fill:colors.ink}},xAxis:{visible:true,line:{fill:colors.gray,width:1},majorGridlines:null,textStyle:{typeface:font,fontSize:23,fill:colors.ink}},yAxis:{visible:true,min:0,max,majorUnit:major,numberFormatCode:format,majorGridlines:{fill:'#E7ECEF',width:1},line:{fill:'none',width:0},textStyle:{typeface:font,fontSize:21,fill:colors.muted}},dataLabels:{showValue:true,position:'outEnd',textStyle:{typeface:font,fontSize:24,bold:true,fill:colors.ink}},chartFill:colors.white,plotAreaFill:colors.white,chartLine:{fill:'none',width:0},plotAreaLine:{fill:'none',width:0}});
 applyPresentationChartFont(c,{fontFamily:font});chartOwners.push(coverage.length);return c;
}

// 1 Cover
{
 const s=p.slides.add();s.background.fill=colors.navy;
 coverage.push({slide:1,title:'基金公司LLM应用调研',sourceIds:[]});
 txt(s,'基金公司LLM应用调研',76,212,1130,110,64,colors.white,true);
 txt(s,'行业案例与本地部署探索',80,350,1050,60,34,'#B7DDDA');
 txt(s,'Intern 实习项目',80,536,1000,40,25,colors.white);
 txt(s,'2026年9月    资料截至2026年9月9日',80,589,1080,38,22,'#C7D5DD');
 note(s,'这次调研想了解，基金公司目前怎样使用LLM，以及哪些经验可以用于我们的本地部署项目。我会先介绍同业的整体情况，再展开四个应用方向，最后讨论合规要求和后续选择。材料以中国公募基金2026年的公开披露为主，海外机构与研究框架作为方法补充。');
}
// 2 Thesis
{
 const s=slide('为什么值得开展本地实践');
 txt(s,'同业已经把LLM接入具体工作',66,190,1115,60,38,colors.teal,true);
 txt(s,'富国和天弘用于投研准备，南方用于数据查询，\n鹏华用于知识和材料审核。量化研究也已有相关案例。',66,270,1120,118,32);
 txt(s,'我的判断是，我们有必要开始积累实际应用经验。\n长期不开展实践，可能逐渐形成效率和工具使用经验的差距。',66,440,1120,128,32);
 note(s,'这里的判断来自同业已经披露的具体应用。它们并不都具有同样的成熟度，也不能据公开资料比较各家公司真实投资收益，但已经足以说明这是一项值得实际尝试的能力。我们需要通过自己的任务了解模型、数据和工具怎样配合，单纯阅读模型介绍很难形成这部分经验。\n\n接下来先说明调研覆盖哪些公司，以及这些材料集中在哪些应用上。',['FUND-007','FUND-300','FUND-200','FUND-308','FUND-251']);
}
// 3 Overview
{
 const s=slide('调研范围与行业概览',{foot:'规模口径为2026年二季度末非货公募规模，剔除ETF联接基金。完整公司表见附录。'});
 txt(s,'20家主要样本，加大成补充案例',66,181,1115,55,35,colors.teal,true);
 txt(s,'样本规模约为3,448亿元至1.70万亿元。\n易方达、华夏和广发超过1万亿元。',66,255,1115,100,31);
 txt(s,'公开应用覆盖多个研究与业务环节，披露深度差异较大。\n技术名称较容易找到，实施和运维分工通常介绍得较少。',66,393,1115,106,31);
 txt(s,'规模用于确定调研对象。案例能说明公开进展，不能代表全行业采用率。',66,544,1115,68,26,colors.muted);
 note(s,'调研以同一季度末的非货公募规模前20家公司为核心，另保留大成的补充案例。财联社提供了可比规模口径。我们没有用规模给技术能力排序。\n\n材料同时包含公司案例、媒体采访、历史采购和联合研究，不能将它们都当作生产系统。整体看，应用已经从一般问答延伸到资料整理、数据查询、审核和量化研究。接下来用几个有具体内容的案例说明。',['FUND-400','FUND-007','FUND-200','FUND-308','FUND-316']);
}
// 4 Main directions
{
 const s=slide('四个应用方向与代表案例',{foot:'国内公司实践、海外资管方法与公开研究框架分别注明。'});
 table(s,[['方向','代表材料','研究员可以用它做什么'],['投研分析','富国、天弘','筛选研报，整理观点，拆解财务问题。'],['数据查询','南方、易方达','理解查询需求，调用数据接口或生成受限SQL。'],['知识与合规','鹏华、汇添富','检索依据，提取风险信息，辅助材料审核。'],['LLM辅助量化','国内文本案例、Man、QuantaAlpha','提取事件变量，生成和检验因子，调用研究工具。']],{y:188,h:421,widths:[190,305,657],fontSize:26,firstColBold:true});
 note(s,'报告保留这四个方向。它们都利用模型理解和生成语言，但交给研究员的结果不同。前两个方向重点是研究准备和查数，知识与合规需要找到适用依据，量化则要继续检验信息是否形成有用信号。\n\n先看披露相对具体的富国和天弘。',['FUND-007','FUND-300','FUND-200','FUND-115','FUND-308','FUND-220','FUND-323','EXT-QA']);
}
// 5 research
{
 const s=slide('富国与天弘的投研准备工作',{foot:'时间为公司自报的整体流程效果，原文未给出统一任务对照与人工复核工时。'});
 table(s,[['公司','具体处理','公司报告的时间变化'],['富国','筛选相关研报，分项归纳后形成市场观点。','一周以上缩短至3小时以内'],['天弘','拆解消费企业利润增长，\n分析销量、价格和原材料等因素。','数日缩短至分钟级']],{y:191,h:285,widths:[165,595,392],fontSize:28});
 txt(s,'两家公司都把模型放进了研究准备的具体步骤。\n整理后的结果仍需核对数字、来源和关键假设。',66,531,1115,92,29);
 note(s,'富国把本地模型接入研究系统。针对投资标的，先判断研报相关性，筛选后形成小结，再综合输出。公司研究系统积累约30万份研报，所报告的时间变化来自相关整体流程，不能理解为模型一次读取所有研报的速度。\n\n天弘的例子围绕消费企业净利润展开，从收入、成本、费用进一步拆到销量、单价、原材料和渠道。我认为可借鉴的是先把资料和分析结构准备出来，研究员再进入增长质量和可持续性的判断。',['FUND-007','FUND-300']);
}
// 6 Southern
{
 const s=slide('南方怎样处理自然语言查询',{sub:'说明性问题：截至6月末，按行业汇总指定评级和期限信用债的存续余额',foot:'小喃整套交易助理自报日均操作耗时降低约40%，查询子流程的单独效果未披露。'});
 table(s,[['环节','需要完成的工作'],['理解问题','识别统计日、评级口径、剩余期限和汇总方式。'],['形成查询','选择获准的数据表，按模板生成SQL查询语句。'],['程序检查','核对权限、语法和执行计划，再由数据库返回结果。'],['研究员复核','检查统计口径、缺失和重复记录，与人工答案比较。']],{y:221,h:370,widths:[226,926],fontSize:27});
 note(s,'这个债券问题用于解释南方公开机制，并非南方展示过的真实查询。模型要先理解业务需求，然后才能选表和形成查询。比如截至6月末的内部评级，不能用当前评级或外部评级直接替代。\n\n南方公开了选表、SQL生成、权限与执行检查的衔接，也介绍了角色、终端和网络条件限制。公司报告整合5个以上系统、20个以上流程，日均操作时间减少40%，但没有给出单独自然语言查询的准确率和耗时。我们验证时要把答案正确和整体效率分开记录。',['FUND-200']);
}
// 7 Query choices
{
 const s=slide('数据查询的两种实现',{foot:'Index-Hub公开的是客户端。内部模型、数据服务端和生产配置没有完整公开。'});
 table(s,[['','南方的受限SQL','易方达Index-Hub接口'],['模型的工作','选表并生成关联、筛选和汇总语句。','选择已有接口并填写参数。'],['适合的问题','需要灵活组合字段与统计口径。','少量固定接口能覆盖的高频问题。'],['主要准备','数据字典、只读权限和标准答案。','接口说明、访问授权、字段单位和错误处理。']],{y:185,h:340,widths:[200,476,476],fontSize:27});
 txt(s,'已有稳定接口时，可以先验证少量高频问题。\n确需灵活统计时，再考虑受限SQL。',66,557,1100,70,29);
 note(s,'两种方式都让模型理解研究员的表达，区别在于允许模型自由决定多少数据操作。固定接口把一部分操作提前定义好，容易限定范围。受限SQL更灵活，也更依赖清晰的数据字典与权限。\n\nIndex-Hub的固定版本有部分子包缺少配置，服务授权和端到端质量仍需确认。对我们的实习项目，我倾向根据现有数据基础选择实现方式，而不是先决定必须采用哪一种Agent框架。',['FUND-200','FUND-115','FUND-116']);
}
// 8 Penghua results
{
 const s=slide('鹏华的营销材料审核',{foot:'91%衡量修改建议的采纳。原文未披露完整违规标注集和漏检统计。'});
 txt(s,'7类、71项规则与大模型共同检查材料',66,180,1100,61,34,colors.teal,true);
 table(s,[['公司披露的使用记录','数量'],['累计审核文件','1,266篇'],['执行信息审核','近6万项'],['提出有效修改建议','989条'],['最新建议采纳率','91%']],{x:64,y:263,w:710,h:327,widths:[475,235],fontSize:28});
 txt(s,'检查风险提示、产品事实、\n业绩宣传和禁止性表达。\n\n合规人员复核疑点，\n并作出发布决定。',839,292,374,280,29);
 note(s,'鹏华的材料说明系统已在实际审核中使用。它把7类、71项规则与大模型结合，覆盖风险提示、基金信息、业绩真实性和禁止性宣传等问题。\n\n这些使用数量和建议采纳能够说明应用已经产生结果，但审核质量还需要漏检和误报数据。尤其不能把91%的采纳率直接解读成准确率。对合规应用，我们要同时观察覆盖到什么问题、哪些问题漏掉，以及复核总耗时。',['FUND-308']);
}
// 9 knowledge and compliance
{
 const s=slide('知识问答和审核需要不同的检验',{sub:'汇添富将风险邮件提取、投资条款问答接入已有风险管理平台'});
 table(s,[['','知识问答','材料审核'],['需要的输出','答案与适用原文，保留资料版本。','疑点位置、相关规则和修改建议。'],['常见问题','遗漏例外、使用旧资料，或回答超出原文。','漏过隐含承诺，也可能误报正常表达。'],['怎样看效果','引用支持情况与获得答案的耗时。','漏检、误报、复核与返工耗时。']],{y:224,h:330,widths:[195,478,479],fontSize:27});
 txt(s,'模型处理文字，已有数据与规则系统继续承担计算和控制。',66,593,1120,54,29,colors.teal);
 note(s,'鹏华的知识问答先处理、切分和检索资料，再让模型据此回答。汇添富则把托管风险邮件和投资条款查询与风险管理平台连接起来。两家公司说明模型可以参与非结构化内容处理，但整个规则平台的效果不能全部归到LLM。\n\n知识问答和审核共用部分资料基础，验收方式却不同。问答主要核对答案与依据，审核还需要一套违规样本来确认漏检。内部制度查询和对外营销审核的责任也需要分别安排。',['FUND-308','FUND-220']);
}
// 10 domestic quant
{
 const s=slide('国内基金的LLM量化披露',{foot:'这些资料定位了LLM参与的环节，尚不足以恢复完整策略或比较实盘业绩。'});
 table(s,[['公司','已经介绍的工作','尚缺的关键细节'],['富国','从舆情提取政策敏感度因子，辅助评价既有因子。','因子定义、时间对齐和独立贡献。'],['广发','从非结构化数据中挖掘另类因子。','文本处理规则、模型与完整回测。'],['华泰柏瑞','结构化公告、纪要与舆情，结合量化信号做组合诊断。','模型与具体因子。自主回测Agent仍是展望。']],{y:192,h:382,widths:[170,520,462],fontSize:27});
 note(s,'国内基金的相关披露以文本处理和辅助研究比较明确。富国提到政策敏感度因子，但相邻的神经网络因子生成和整体轮动业绩不能都算作LLM贡献。广发和华泰柏瑞则来自有明确公司归属的媒体材料。\n\n量化部分我会沿三个问题展开：怎样把文本转成变量，怎样生成和修改因子，怎样让研究工具检验模型输出。完整方法还需要参考海外资管与公开研究。',['FUND-007','FUND-251','FUND-359']);
}
// 11 event extraction
{
 const s=slide('公告事件怎样形成研究变量',{sub:'说明性例子：T日收盘后发布扩产计划，年产能拟由10万吨增至15万吨'});
 table(s,[['从原文保留的信息','如何进入研究'],['事件与状态','记录为“拟扩产、待审批”，与实际投产分开。'],['产能与单位','保留10万吨和15万吨，程序计算计划增幅50%。'],['原文与发布时间','匹配证券并去重，记录首次可得时间。'],['后续检验','比较未来收益、风险或盈利预期变化，控制已有暴露。']],{y:218,h:349,widths:[330,822],fontSize:27});
 txt(s,'T日收盘后的消息不能用于当天收盘前的决策。',66,603,1120,43,29,colors.teal);
 note(s,'这是报告中的说明性例子，没有运行模型或回测。模型先提取实体、事件、数字、单位、时间和状态，程序再计算、匹配和去重。关键是保留“计划”和“待审批”，避免把未来安排变成已经实现的产量变化。\n\n我们可以先检验这些字段是否正确，再研究它是否带来新增信息。即使最终没有选股增量，准确的事件信息也可能用于风险监控。易方达参与的NLPCC 2026任务提供了新闻与行情加载、决策和回测基线，但它是有数据条件的学术任务。',['FUND-007','FUND-119']);
}
// 12 Man chart
{
 const s=slide('AlphaTrend的三类研究实验',{sub:'Man AHL用预期有效、较差和不确定的想法检验同一个研究流程',foot:'Sharpe为原文所述约值。作者模拟展示，基准经过有意简化。'});
 chart(s,['恢复反应机制','局部峰谷信号','开放探索'],[{name:'方案集中或中心位置',values:[1.05,.80,.85],fill:colors.teal},{name:'简化后的基准',values:[.95,.95,.95],fill:'#B3C0C8'}],{x:64,y:210,w:820,h:390,max:1.2,major:.2});
 txt(s,'恢复机制改善表现。\n峰谷方案落后。',924,263,286,145,30,colors.navy,true);
 txt(s,'开放探索约为\n0.70至1.00，\n表现随时期变化。',924,445,286,135,27);
 note(s,'Man故意从既有突破信号中移除提高反应速度的机制，再看AlphaTrend能否重新发现改进。该组方案的Sharpe集中在约1.05，简化基准约0.95。局部峰谷方案中心约0.80，几乎都落后，说明系统能够输出负面结果。开放想法分布约0.70至1.00，中心约0.85。\n\n柱形展示的是原文描述的约略中心或集中位置，不是精确均值，也没有展示全部分布。原文图注截至2015年，但正文提及2012至2016年的部分表现，时间口径未完全一致。这里借鉴的是研究检验方法，不能解释为2026实盘收益。原作者还指出多重试验和人类判断的重要性。',['FUND-323']);
}
// 13 QA case
{
 const s=slide('QuantaAlpha的因子修改案例',{sub:'原作者附录C：价量因子的相关性改善，组合风险却上升',foot:'案例未报告下一次修改完成后的结果。它与总体实验的轮次、换手和成本口径也有差异。'});
 txt(s,'系统提出两类动量互补的假设，实际生成价量因子，\n再根据回测反馈提出修改。',66,212,1135,83,30);
 table(s,[['指标','案例基准','子因子结果'],['信息比率','0.973','0.963'],['超额收益最大回撤','约7.30%','11.37%']],{y:337,h:201,widths:[510,321,321],fontSize:29});
 txt(s,'反馈拒绝直接采用，并建议补入波动状态后重新检验。',66,578,1120,45,29,colors.teal);
 note(s,'QuantaAlpha保存从假设、表达式和代码到回测结果的研究记录，后续可以修改或组合研究步骤。附录C生成的子因子计算20日价量变动相关性，乘以5日日内收益均值，再作横截面排名。原式的变动分母使用当日价格和成交量，复现时需要照原文核对。\n\n子因子Rank IC为0.0311，高于父记录的0.0216和0.0246，但信息比率略降、最大回撤扩大，系统给出拒绝直接采用及修改建议。表达式没有机构持仓、社交热度或基本面数据，也未实现假设中提出的波动权重。我认为这里最有启发的是检查经济解释与实际实现能否对应。\n\n附录的轮次、换手及成本记录与总体设置并不完全一致，因此将该例用于解释研究动作，不把它的收益与总体表格合并。',['EXT-QA','EXT-QC']);
}
// 14 QA experiment
{
 const s=slide('QuantaAlpha的总体实验',{sub:'同用GPT-5.2，比较三个LLM因子框架的IC',foot:'原作者结果，尚未独立复现。沪深300，2022年至2025年12月26日。\n约150个因子由同一LightGBM模型评价。'});
 chart(s,['RD-Agent','AlphaAgent','QuantaAlpha'],[{name:'IC',values:[.0286,.0347,.0472],fill:colors.teal}],{x:64,y:205,w:752,h:397,max:.055,major:.01,format:'0.0000',legend:false});
 table(s,[['框架','年化\n超额收益'],['RD-Agent','3.58%'],['AlphaAgent','1.11%'],['QuantaAlpha','4.68%']],{x:858,y:248,w:354,h:316,widths:[205,149],fontSize:24});
 note(s,'这里取论文表1中同一基础模型下的框架比较。IC衡量预测值与后续收益的相关性，QuantaAlpha在这组对照中为0.0472。其收益和回撤来自约150个因子与相同下游LightGBM组成的评价流程，不是单个生成因子的独立收益。\n\n训练期2016至2020年，验证期2021年，测试期2022年初至2025年12月26日。组合每日选50只等权股票，每次替换5只，次日开盘成交，买入费率0.05%、卖出0.15%。三种框架的超额收益最大回撤分别为16.76%、13.89%、11.80%。\n\n论文的部分传统或深度学习方法在某些组合指标上更好，不能从此表推论LLM全面优于现有量化方法。消融实验使用DeepSeek-V3.2，移除修改环节后IC从0.0461降到0.0382，也为迭代作用提供了作者实验依据。',['EXT-QA']);
}
// 15 decoupling
{
 const s=slide('模型服务与研究框架可以分别验证');
 table(s,[['比较对象','保持一致的部分','需要观察的差异'],['本地与API模型','相同资料、任务、提示词和工具。','答案质量、工具调用、响应时间与资源。'],['研究工作流','固定的数据读取、代码检查和回测规则。','失败步骤和人工修正工作量。'],['持续使用','明确版本与结果记录。','更新后标签、代码和结论是否改变。']],{y:184,h:362,widths:[255,449,448],fontSize:27});
 txt(s,'API案例中的任务设计可以借鉴，本地替换后的效果需要实测。',66,590,1120,59,29,colors.teal);
 note(s,'QuantaAlpha报告一次主要运行约20小时、180万tokens，采用托管模型API与CPU回测。这个例子说明框架怎样连接任务和工具，与本地模型需要多少GPU是不同的问题。\n\n我们可以先研究接口与评价方式，再测试本地模型能否完成相同工作。模型服务留在内部，也不自动意味着全部数据处理都在内部，文字识别、检索向量、日志和远程运维还需要一起确认。接下来讨论这些合规条件。',['EXT-QA','EXT-QC','REG-004','REG-006']);
}
// 16 Governance themes
{
 const s=slide('合规要求对应用设计的影响',{foot:'公开文件提供研究依据。实习机构内部制度、COD条件和具体用例分类仍需确认。'});
 table(s,[['关注的问题','相关依据','对实施的影响'],['哪些资料可以使用','个人信息保护法、数据安全法','确认使用依据、资料权限、保存与外部处理。'],['输出将用于什么','内部MRM制度\n行业评测参考','记录用途、负责人、检验方法和版本变化。'],['谁承担运行责任','证券基金信息技术管理办法','核对系统重要性、供应商职责和替换安排。']],{y:200,h:367,widths:[290,390,472],fontSize:27});
 note(s,'考虑到我们对合规的要求，我同时梳理了数据保护、生成式AI服务和证券基金信息技术管理文件。需要把法律、监管规定、团体标准和内部政策分开理解。\n\n个人信息保护法涉及合法基础、委托处理和特定影响评估。数据安全法覆盖个人信息以外的数据。证券基金信息技术管理办法要求机构保留自身责任，并对重要系统外部独立运维设限，包含法定例外。\n\nAMAC 2026大模型应用规范为团体标准，提供场景评测和权限参考，具体采用依据仍需确认。美国SR26-2是银行监督指引，配套定义排除生成式和Agentic AI，不能代替实习机构内部政策。',['REG-002','REG-014','REG-003','REG-009','REG-010','REG-012','REG-007','REG-008']);
}
// 17 applicability
{
 const s=slide('数据和服务范围需要在原型阶段明确');
 table(s,[['准备开展的工作','实施前需要确认'],['仅供内部研究的资料处理','服务对象、数据使用权与内部制度。'],['接入内部研报和数据库','员工权限、有效版本、缓存与结果导出的范围。'],['使用外部模型或辅助服务','处理地点、保存删除、供应商角色及可能的数据出境。'],['面向客户或对外发布','重新判断服务与内容责任，并落实审核与发布安排。']],{y:185,h:421,widths:[431,721],fontSize:27});
 note(s,'生成式人工智能服务管理暂行办法第2条以向境内公众提供服务为适用条件，并排除未向公众提供此类服务的组织研发和应用。内部工具仍需要遵守相应的数据、安全和金融机构管理要求。\n\n本地模型可能调用外部识别、向量或日志服务，API也不必然代表出境，需要核查实际位置和数据流。原型只要涉及外部处理或运维，就应确认相应条件，不能等到生产接入才考虑。重要系统和外包职责按照证券基金信息技术管理办法第43至45条等核查，对外发布还需考虑生成内容标识和金融业务要求。',['REG-001','REG-002','REG-003','REG-004','REG-005','REG-006','REG-010','REG-016']);
}
// 18 close
{
 const s=slide('后续本地验证的初步选择');
 table(s,[['候选任务','适合启动的条件','先检验什么'],['公告事件提取','可以使用的公告样本与人工标注。','字段、状态、时间和原文依据是否准确。'],['只读数据查询','已有数据字典、稳定接口和访问权限。','答案与统计口径是否正确，是否减少总查数时间。']],{y:191,h:270,widths:[276,430,446],fontSize:28});
 txt(s,'我倾向先选一个具体任务，取得可以自己复核的结果。',66,513,1120,60,32,colors.teal,true);
 txt(s,'按项目计划比较模型并完成本地部署，再决定下一步投入。',66,592,1110,49,27);
 note(s,'这次行业调研提供了可以借鉴的方向。结合实习范围，我倾向从公告事件提取或只读查询中选择一个，具体选择取决于数据和系统条件。\n\n按项目计划，下一阶段比较5至8个开放模型，在本地GPU部署一个模型完成金融文本任务。使用一致的资料、任务和检验方式，记录质量、时延、资源和人工复核时间。以后再根据实际使用量和运行要求比较三年TCO。\n\n这里希望讨论的是，部门是否已有适合的小型数据任务，以及哪些数据、系统和内部管理条件可以先确认。',[]);
}
// 19-21 Company appendix
const cohort=JSON.parse(await fs.readFile(path.join(reportDir,'data/cohort.json'),'utf8'));
const detail=[
 ['易方达','指数研究和基金查询','指数平台、公开查询客户端','有高校联合研究',['FUND-004','FUND-115']],
 ['华夏','模型接入安全','2025年安全网关采购','北京世纪东凌中标',['FUND-001']],
 ['广发','智能理财与文本因子','协议提及DeepSeek、Qwen','实施分工未详述',['FUND-009','FUND-251']],
 ['富国','市场观点、知识与文本因子','本地模型、检索与计算平台','公司介绍为自研',['FUND-007']],
 ['南方','交易助理与数据查询','选表、SQL及权限检查','模型和实施方未详述',['FUND-200']],
 ['汇添富','风险邮件和条款问答','LLM与已有规则平台配合','外部分工未详述',['FUND-220']],
 ['景顺长城','本地文档处理与检索','报道提到模型和检索组件','媒体未披露实施方',['FUND-251']],
 ['嘉实','ESG数据与研究','报告披露AI和文本处理','LLM具体范围待核',['FUND-304']],
 ['博时','数据和研究工具协作','内部模型、隔离运行与审计','报道未详述外部分工',['FUND-215']],
 ['鹏华','知识问答与营销审核','私有模型、提示词和规则','未说明外部实施方',['FUND-308']],
 ['招商','个股分析与财报点评','多个工作流及信息提取','媒体未披露实施方',['FUND-251']],
 ['国泰','组合平台检索问答','昇腾与DeepSeek\n另有传统文本处理','外部分工未详述',['FUND-403']],
 ['永赢','邮件反钓鱼','安全GPT邮件处理','未说明外部实施方',['FUND-352']],
 ['工银瑞信','养老金运营\nFundGPT研究服务','大模型平台及历史合作','恒生聚源\n工银科技、智谱AI',['FUND-312','FUND-316']],
 ['天弘','财务分析与工具调用','模型服务、检索及金融数据','Wind与同花顺工具',['FUND-300']],
 ['中欧','取数、建模与写作','报道提到100余项Skills','公众号转载媒体报道',['FUND-356','FUND-251']],
 ['华安','灵思知识与研究平台','2025案例，本地与API配合','外部分工未详述',['FUND-150']],
 ['华泰柏瑞','文本与量化信号结合','结构化处理和组合诊断','中国证券报采访材料',['FUND-359']],
 ['兴证全球','固收交易信息处理','文本提取与交易工具衔接','LLM具体范围待核',['FUND-011']],
 ['平安','AI青蚨研究资料整理','报道介绍检索与溯源','实施分工未详述',['FUND-160']],
 ['大成','固收交易要素提取','Qwen2.5与交易系统衔接','未说明外部实施方',['FUND-013']]
];
for(let part=0;part<3;part++){
 const group=detail.slice(part*7,(part+1)*7);
 const s=slide(`附录A  公司调研汇总（${part+1}/3）`,{foot:'规模单位：亿元。2026年二季度末非货公募规模，剔除ETF联接基金。大成为补充案例。',footY:657});
 const values=[['公司','非货规模','主要应用','公开技术信息','合作或来源说明'],...group.map(d=>{const a=cohort.find(x=>x.company===d[0]);return [d[0],a?a.aum_cny_100m.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2}):'补充案例',d[1],d[2],d[3]];})];
 table(s,values,{y:139,h:492,widths:[155,153,250,350,244],fontSize:23,pad:5});
 note(s,'本表保留报告表A中的全部21家公司，分三页查阅。规模用于确定样本，不作为技术能力排名。技术组件的品牌名称不能用来推断整个系统的合同分工。历史采购、广义AI、媒体陈述和具体LLM应用按对应来源理解。\n\n'+group.map(d=>d[0]+'：'+d.slice(1,4).join('。')+'。').join('\n'),['FUND-400',...new Set(group.flatMap(d=>d[4]))]);
}
// 22 MENTOR
{
 const s=slide('附录B  MENTOR的行业排序实验',{sub:'易方达与高校共同作者的2025年研究，作为方法补充',foot:'Spearman衡量排序一致程度。原作者结果，完整版权数据与样本映射仍有复现条件。'});
 table(s,[['方法','美股11行业\nSpearman','A股9行业\nSpearman','A股前3\n命中率'],['动量基线','0.159','0.100','0.444'],['SEP + DeepSeek','0.078','0.118','0.472'],['MENTOR + DeepSeek','0.220','0.141','0.488'],['MENTOR + O1','0.221','0.173','0.439']],{y:211,h:336,widths:[425,245,245,237],fontSize:26,pad:7});
 txt(s,'排序相关性提高，并不保证最领先行业的命中率同步提高。',66,586,1120,48,29,colors.teal);
 note(s,'MENTOR先预测下周热点，再进行行业排序。实际结果出现后，教师角色分析偏差，系统修改下一周使用的文字策略，未在每周重新训练模型权重。\n\n文本样本覆盖2023至2024年，包括160,190篇中文KOL帖子和72,108篇英文财经新闻，行情来自Wind和Bloomberg。表3显示O1在A股排序相关性上更高，但前3命中率低于DeepSeek版本和动量。这说明需要先确定评价目标，也应与简单金融基线比较。\n\n这是2025年联合论文，非2026年新增生产项目。完整版权数据未公开，正文与补充材料部分数据描述对应不清，不能直接把结果解释为基金实盘收益。',['FUND-113','FUND-114']);
}
// 23 Original process figure
{
 const s=slide('附录C  AlphaTrend原文研究流程',{foot:'来源：Man AHL，2026年2月11日。原始流程图按原比例展示。'});
 const img=await fs.readFile(path.join(REPO,'knowledge-base/sources/FUND-323/workflow.png'));
 s.images.add({blob:new Uint8Array(img),contentType:'image/png',alt:'Man AHL AlphaTrend原始研究流程，包含想法、实现、回测、分析与结论。',fit:'contain',position:{left:130,top:140,width:1020,height:478}});
 note(s,'原图显示从研究想法、方案生成、实现、回测、基准分析到综合结论的连续过程。市场数据和基准分析由工具提供，LLM参与研究方案与解释。图中是Man原文公开流程，并不意味着各节点的完整提示词、专有工具和数据已公开。\n\n图像出处与原始文章一致。',['FUND-323']);
}
// 24 Code verification
{
 const s=slide('附录D  量化代码的验证',{foot:'AlphaQT-Bench为ACL 2026论文。比例仅对应论文中的270项任务和12个模型。'});
 table(s,[['检查','回答的问题'],['能否执行','代码能否运行，并返回要求的结果。'],['是否存在前视','截断未来数据后，历史因子值是否变化。'],['功能是否正确','结果是否符合任务定义和专家代码。'],['计算结构是否符合要求','是否满足批量数组计算等约束。']],{y:178,h:359,widths:[390,762],fontSize:27});
 txt(s,'四项同时通过的平均正确率：93.7%（Gemini-2.5-Pro）\n开放权重模型中最高为81.9%（DeepSeek-V3）。',66,566,1120,75,27);
 note(s,'这里的指标是Verified Accuracy，要求运行、时序因果、功能和结构四类检查全部通过。它不是只看向量化，也不是交易策略成功率。93.7%和81.9%是论文所测模型中的结果，不作为当前模型市场排名。\n\n前视检查先用完整样本计算，再选一个较早时点截断重算，比较相同历史时点的结果。通过这一检查仍不能保证原始资料发布时间正确，或经济解释与实现相符。',['EXT-AB']);
}

await fs.mkdir(TMP,{recursive:true});await fs.mkdir(path.dirname(OUT),{recursive:true});await fs.mkdir(path.join(WS,'.codex-finalizer'),{recursive:true});
const stem=path.basename(OUT,'.pptx');
const candidatePath=path.join(TMP,`${stem}.candidate.pptx`);
await (await PresentationFile.exportPptx(p)).save(candidatePath);
await fs.writeFile(path.join(WS,'src/slide-manifest.json'),JSON.stringify({reportCommit:'98bab07',reportPdf:'reports/phase1-llm-industry-2026-09-09/report.pdf',researchCutoff:'2026-09-09',preparedDate:'2026-09-10',mainSlides:18,appendixSlides:6,slides:coverage},null,2));
const renders=path.join(TMP,`draft-render-${stem}`);await fs.mkdir(renders,{recursive:true});
for(let i=0;i<p.slides.items.length;i++){
 const s=p.slides.items[i];const blob=await p.export({slide:s,format:'png',scale:1});
 await fs.writeFile(path.join(renders,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
 const layout=await s.export({format:'layout'});await fs.writeFile(path.join(renders,`slide-${String(i+1).padStart(2,'0')}.layout.json`),await layout.text());
}
const result=await finalizePresentation({workspaceDir:WS,candidatePath,finalPath:OUT,pythonExecutable:PYTHON,integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...[...new Set(tableOwners)].flatMap(n=>['--require-native-table-slide',String(n)])],requiredNativeTableOwnerSlides:[...new Set(tableOwners)],requiredNativeChartOwnerSlides:[...new Set(chartOwners)],materializeLiteralChartWorkbooks:true,fontPolicy:{basis:'design',families:[font]},verifyArtifactToolImport:true,receiptPath:path.join(WS,'.codex-finalizer',path.basename(OUT)+'.validation.json')});
console.log(JSON.stringify({output:OUT,slides:coverage.length,tableOwners,chartOwners,result},null,2));
// Render the final package, not only the authoring object.
const checked=await PresentationFile.importPptx(await FileBlob.load(OUT));
const finalRender=path.join(TMP,`final-render-${stem}`);await fs.mkdir(finalRender,{recursive:true});
for(let i=0;i<checked.slides.items.length;i++){
 const blob=await checked.export({slide:checked.slides.items[i],format:'png',scale:1});
 await fs.writeFile(path.join(finalRender,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
}
console.log('Final deck rendered.');
