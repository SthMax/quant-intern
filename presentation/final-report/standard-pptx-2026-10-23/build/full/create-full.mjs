import fs from 'node:fs/promises';
import path from 'node:path';
import {createCanvas} from '@napi-rs/canvas';
const measureContext=createCanvas(10,10).getContext('2d');
function wrapText(value,width,size){measureContext.font=`${size}px Arial Unicode MS`;return value.split('\n').map(part=>{const toks=part.match(/[A-Za-z0-9]+(?:[-.\/][A-Za-z0-9]+)*|[^A-Za-z0-9]/gu)||[];const lines=[];let line='';for(const token of toks){if(!line&&/\s/.test(token))continue;const trial=line+token;if(line&&measureContext.measureText(trial).width>width*.95&&!/[，。！？、：；）]/.test(token)){lines.push(line.trimEnd());line=token.trimStart();}else line=trial;}if(line)lines.push(line.trimEnd());return lines.join('\n');}).join('\n');}
import {Presentation, PresentationFile} from '@oai/artifact-tool';
import {applyPresentationChartFont} from '/Users/sthmax/.codex/plugins/cache/openai-primary-runtime/presentations/26.1020.11348/skills/presentations/container_tools/artifact_tool_utils.mjs';
const root=path.resolve('..'),FONT='Arial Unicode MS';
const pres=Presentation.create({slideSize:{width:1280,height:720}});
pres.theme.defaultFont=FONT;
pres.theme.colorScheme={name:'Office Standard Blue',themeColors:{accent1:'#2F5597',accent2:'#7F7F7F',accent3:'#A5A5A5',accent4:'#4472C4',accent5:'#B4C6E7',accent6:'#D9E2F3',bg1:'#FFFFFF',bg2:'#F2F2F2',tx1:'#202020',tx2:'#595959',dk1:'#202020',dk2:'#595959',lt1:'#FFFFFF',lt2:'#F2F2F2',hlink:'#2F5597',folHlink:'#7F7F7F'}};
const master=pres.masters.add('Office Standard'); master.background.fill='bg1';
function ph(owner,type,index,pos,size,bold=false){const sh=owner.placeholders.add({type,index,geometry:'textbox',position:pos,fill:'none',line:{fill:'none',width:0}});sh.text.style={fontSize:size,bold,color:'tx1',autoFit:'none',insets:0};return sh;}
ph(master,'title',0,{left:64,top:44,width:1152,height:64},42,true);ph(master,'body',1,{left:64,top:150,width:1152,height:500},28);
function layout(name,kind='content'){const l=pres.layouts.add(name);l.setParentLayoutId(master.id);if(kind==='cover'){ph(l,'title',0,{left:88,top:184,width:1104,height:166},56,true);ph(l,'subtitle',1,{left:88,top:392,width:1104,height:200},28);}else if(kind==='section'){ph(l,'title',0,{left:88,top:236,width:1104,height:128},48,true);ph(l,'body',1,{left:88,top:405,width:1050,height:124},28);}else{ph(l,'title',0,{left:64,top:44,width:1152,height:64},42,true);ph(l,'body',1,{left:64,top:132,width:1152,height:62},26);}return l;}
const layouts={cover:layout('Title Slide','cover'),body:layout('Title and Content'),section:layout('Section Header','section'),two:layout('Two Content')};
function slide(type,title,body='',notes=''){const s=pres.slides.add({layoutId:layouts[type].id});s.placeholders.getItem('title').text=title;if(body)s.placeholders.getItem(type==='cover'?'subtitle':'body').text=body;s.speakerNotes.text=notes;return s;}
function compact(t){return t.replace(/([\u3400-\u9fff]) +(?=[A-Za-z0-9])/g,'$1').replace(/([A-Za-z0-9]) +(?=[\u3400-\u9fff])/g,'$1').replace(/(\d) (?=tokens?(?:\/s)?\b)/g,'$1\u00a0');}
function text(s,txt,x,y,w,h,size=26,opts={}){const sh=s.shapes.add({geometry:'textbox',name:txt.slice(0,22),position:{left:x,top:y,width:w,height:h},fill:opts.fill||'none',line:{fill:'none',width:0}});sh.text=wrapText(txt,w,size);sh.text.style={fontSize:size,color:opts.color||'tx1',bold:opts.bold||false,alignment:opts.align||'left',verticalAlignment:'top',autoFit:'none',insets:0};return sh;}
function node(s,txt,x,y,w,h){const sh=s.shapes.add({geometry:'rect',name:txt.split('\n')[0],position:{left:x,top:y,width:w,height:h},fill:'bg1',line:{fill:'accent1',width:1.5}});sh.text=txt;sh.text.style={fontSize:26,color:'tx1',alignment:'center',verticalAlignment:'middle',autoFit:'none',insets:8};return sh;}
function conn(s,a,b,from='right',to='left',arrow=true,kind='straight'){return s.shapes.connect(a,b,{kind,fromSide:from,toSide:to,line:{fill:'accent1',width:2},...(arrow?{tail:{type:'triangle',width:'sm',length:'sm'}}:{})});}
function table(s,values,x,y,w,h,widths,font=25){const t=s.tables.add({rows:values.length,columns:values[0].length,left:x,top:y,width:w,height:h,columnWidths:widths,values});t.styleOptions={headerRow:true,bandedRows:false};t.borders.assign({fill:'bg2',width:1,style:'solid'});for(let r=0;r<values.length;r++){t.rows[r].height=h/values.length;for(let c=0;c<values[0].length;c++){const cell=t.getCell(r,c);cell.fill=r===0?'accent1':(r%2===0?'bg2':'bg1');cell.text.style={fontSize:font,color:r===0?'bg1':'tx1',bold:r===0,autoFit:'none',verticalAlignment:'middle',alignment:c===0?'left':'center'};}}t.cells.block({row:0,column:0,rowCount:values.length,columnCount:values[0].length}).assign({margins:{left:14,right:14,top:10,bottom:10},anchor:'center'});return t;}
const sourceDir='/Users/sthmax/dev/git/ms-intern/presentation/final-report/narrative-drafts-2026-10-22';
const notesBase='内容依据：'+sourceDir+'/extended-draft-d-revised-4.md\n证据核验日期：2026年10月23日。';
const fullDir=path.join(root,'build','full');
const textLayout=pres.layouts.add('Title and Text');textLayout.setParentLayoutId(master.id);ph(textLayout,'title',0,{left:64,top:44,width:1152,height:64},42,true);ph(textLayout,'body',1,{left:64,top:170,width:1152,height:490},30);layouts.prose=textLayout;
const mapping=[];
function sources(i){const e=sourceDir+'/d-revised-4-evidence.md';let out=notesBase+'\n'+e;if(i===5)out+='\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/FUND-113/original.md\nhttps://github.com/yingmi-dev/content-compliance-skill/blob/040df66202f6075cdeadb450e502c7a19c83dabf/README.md\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/FUND-101/original.md';if([19,23].includes(i))out+='\nhttps://artificialanalysis.ai/evaluations/gdpval-aa\nhttps://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-1017-vs-deepseek-v4-1-flash';if([20,33,34].includes(i))out+='\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-076/original.md\n外部随机token测试，FP8权重、FP8缓存、MTP3，关闭前缀缓存。';if(i>=26&&i<=32)out+='\nAI Infra固定修订3bdcb4fcab73010eeaccf31cc10a8242a895d82e\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-078/upstream/manuscripts/03-推理与训练负载.md\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-078/upstream/manuscripts/08-推理优化.md';if(i>=35&&i<=37)out+='\nhttps://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/blob/1bae0e1088993b9b82de08f59de5be5a34e42170/README.md\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-020/original.md';if(i>=39&&i<=44)out+='\n'+sourceDir+'/d-revised-4-data.json\n预算口径：业务任务为完整工作，每项计划8轮模型调用，另加10%完整轨迹用于修改与重试。三年固定人数，每人每天5项，每年250个工作日。\nDeepSeek本轮复核：https://api-docs.deepseek.com/quick_start/pricing/\nhttps://api-docs.deepseek.com/guides/kv_cache/';if(i===41||i===42)out+='\nhttps://news.smm.cn/news/104118405\nhttps://configurator.exxactcorp.com/configure/TS4-118380266';if(i===43||i===44)out+='\nhttps://docs.bigmodel.cn/cn/guide/start/pricing\nhttps://platform.kimi.com/docs/pricing/chat\nAPI输入累计80%缓存读取为预算假设，按usage更新。DeepSeek按80%高峰、20%低峰、USD/CNY=7.00计价。普通输入、缓存读取与输出分别计费。供应商联网工具费用按实际使用另计。';if(i>=46&&i<=47)out+='\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-072/open-webui.md\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-068/onyx-permissions.md\n/Users/sthmax/dev/git/ms-intern/knowledge-base/infrastructure/scenario-2-enterprise-rag-2026-09-23.md';return out;}
function S(i,type,title,intro=''){if(pres.slides.items.length!==i-1)throw Error('Page order '+i);const s=slide(type,title,intro,sources(i));mapping.push({slide:i,sourcePage:i,title,layout:type});return s;}
function P(i,title,paras){const s=S(i,'prose',title);const b=s.placeholders.getItem('body');b.text=paras.map(x=>({runs:[wrapText(x,1152,30)],spaceAfter:2000}));return s;}
function T(i,title,intro,values,widths,tail='',opts={}){const s=S(i,'body',title,wrapText(intro,1152,26));if(opts.introH)s.placeholders.getItem('body').position={left:64,top:132,width:1152,height:opts.introH};const y=opts.y||228,h=opts.h||300;table(s,values,64,y,1152,h,widths,opts.font||27);if(tail)text(s,tail,64,opts.tailY||(y+h+36),1152,opts.tailH||110,opts.tailFont||27);return s;}
function chain(s,labels,x=64,y=280,w=1152,h=80){const gap=36,bw=(w-gap*(labels.length-1))/labels.length;const nodes=labels.map((v,j)=>node(s,v,x+j*(bw+gap),y,bw,h));for(let j=1;j<nodes.length;j++)conn(s,nodes[j-1],nodes[j]);return nodes;}
function section(i,title,body){return S(i,'section',title,body);}
// 1–7: business needs
S(1,'cover','公司本地部署 LLM\n模型、运行环境与成本','实习研究汇报\n\n金融工作需求与部署选择依据\n2026 年 10 月 23 日');
T(2,'汇报内容','围绕金融工作需求，说明模型选型、运行安排与投入预算。',[
 ['章节','主要内容'],['一、金融工作与本地部署需求','应用场景与使用环境'],['二、分析任务对模型的要求','上下文、模型能力与速度'],['三、模型选型','个人设备与公司服务器的选择依据'],['四、运行环境与使用体验','请求处理、多轮任务与共享使用'],['五、资源需求与成本','单台设备与 API 的三年投入'],['六、日常应用与验证','使用入口、资料接入与验证工作']],[560,592],'',{y:224,h:410,font:27});
section(3,'第一章\n金融工作与本地部署需求','金融工作的应用场景\n本地服务的使用环境');
{
 const s=S(4,'body','LLM 在资料处理中的作用','大语言模型依据问题和资料，参与阅读、归纳、分析与文字形成。');
 text(s,'资料与任务要求',64,231,1152,42,30,{bold:true});const ns=chain(s,['寻找相关信息','组织关系与解释','形成文字或\n结构化结果'],64,310,1152,95);const check=node(s,'同事核对依据，决定如何使用',390,470,500,70);conn(s,ns[2],check,'bottom','right',true,'elbow');
 text(s,'例如，从公告整理日期、主体与金额，或比较多份材料中的不同表述。\n明确任务范围和交付要求，便于检查结果。',64,593,1152,85,28);
}
P(5,'金融工作的公开应用案例',[
 '投研：易方达参与的 MENTOR 研究使用中文文章和英文财经新闻，依次识别热点事件、推演后续事件并形成行业排序。该公开研究原型展示了文本信息进入投研分析的路径。',
 '合规：盈米的内容合规审查 Skill 接收文本或文档，提供风险位置、理由和修改建议。内容作者据此修改，再由合规人员终审。',
 '技术支持：易方达在协会发布的云平台案例中披露，将大模型接入开发与测试环节。研发人员获得代码和测试辅助，产物继续进入既有交付流程。']);
T(6,'公司应用的使用条件','公开新闻、财报与内部研究文件，对资料范围和使用环境提出不同要求。',[
 ['使用问题','需要明确的安排'],['使用人员','身份、用户范围与使用入口'],['可读取的资料','文件权限、资料来源与可访问范围'],['后续工作衔接','引用、复核和交付流程'],['模型运行位置','运行位置、服务连接与维护责任']],[370,782],'安全与合规要求落实在身份、资料权限和工作流程等具体条件中。',{h:330});
P(7,'本地部署的运行环境控制',[
 '公司的需求是在自身管理的环境中使用 LLM。模型部署在公司设备上，便于统一安排运行位置、服务连接和资源使用。',
 '身份与权限系统限定资料访问范围，应用流程组织结果复核与交付，使本地能力能够进入日常工作。',
 '本次研究聚焦相互关联的部署选择：模型选型、运行环境及资源投入。分析从一项财报任务展开。']);
// 8–15: task requirements
section(8,'第二章\n分析任务对模型的要求','以财报分析为例\n说明材料、模型能力与等待时间的关系');
T(9,'财报分析的任务与交付要求','任务：解释本期收入和利润变化的主要原因，并指出各项判断的依据。',[
 ['交付内容','核对方式'],['收入、利润及变化','回到对应报表，检查数字、期间和单位'],['变化原因及相关业务','核对管理层解释、分部信息和必要附注'],['判断依据','打开引用位置，检查解释与原文的关系']],[390,762],'分析需要读准数字与单位，区分本期、上期和可比口径，再以正文与附注支撑原因解释。',{h:296,tailFont:28});
{
 const s=S(10,'body','上下文与推理','上下文包括本次材料、问题以及需要保留的对话历史。模型据此生成回答的运行过程称为推理。');
 const a=node(s,'系统要求、财报内容、用户问题、已有对话',240,251,800,70),b=node(s,'已训练好的模型',420,371,440,70),c=node(s,'收入与利润变化、原因解释、原文依据',240,491,800,70);conn(s,a,b,'bottom','top');conn(s,b,c,'bottom','top');
 text(s,'财报与附注的容量、分析完成程度和结果等待时间，分别对应上下文、模型能力与速度。',64,617,1152,70,28);
}
{
 const s=S(11,'body','固定资源下的上下文、模型能力与速度','给定硬件、并发规模和运行方式，三项要求共享内存与计算预算。');
 const a=node(s,'模型能力\n理解材料、完成分析',275,222,270,88),b=node(s,'上下文\n带入材料与历史',70,490,270,88),c=node(s,'速度\n缩短等待、持续生成',485,490,270,88);conn(s,a,b,'left','top',false);conn(s,a,c,'right','top',false);conn(s,b,c,'right','left',false);
 text(s,'更多信息需要\n更多分析',83,345,210,66,24,{fill:'bg1',align:'center'});text(s,'更充分的推理\n需要计算时间',526,345,230,66,24,{fill:'bg1',align:'center'});text(s,'更长输入增加\n处理与状态负担',296,592,232,68,24,{align:'center'});
 text(s,'材料增加，设备需要处理并保留更多信息。',844,242,360,100,28);text(s,'更多思考步骤或计算量更大的模型，会提高单项任务的资源占用。',844,365,360,134,28);text(s,'选型需明确材料规模、分析要求与可接受的等待时间。',844,525,360,112,28);
}
{
 const s=S(12,'body','上下文窗口与任务信息','上下文窗口容纳材料和工作过程，包括问题、报表、附注，以及后续资料和讨论。');
 text(s,'上下文窗口',64,240,1152,40,30,{bold:true});const labels=['系统要求','材料与附注','历史与工具结果','本轮生成'];labels.forEach((v,i)=>node(s,v,64+i*288,306,288,100));
 text(s,'输入与输出通常按 token 计量。Token 是模型处理文本的片段，可以对应字、词或部分字符。',64,466,1152,90,30);
 text(s,'较长窗口有助于保留相关材料与工作过程。使用时还需为后续生成预留空间。',64,591,1152,80,30);
}
T(13,'模型能力与分析任务的深度','同一份财报可以对应不同程度的工作要求。',[
 ['工作要求','模型需要完成的处理'],['整理收入与利润','定位表格，识别数字、单位与期间'],['解释本期变化','联系业务、费用和附注，组织有依据的原因'],['比较不同公司','对齐口径，识别差异并说明其意义'],['形成可交付分析','组织比较表、计算结果、文字与引用']],[390,762],'任务越深入，越需要衔接多个步骤。模型评价应关注最终交付物的完成程度。',{h:330});
{
 const s=S(14,'body','首次输出、生成速度与完整任务时间','首次输出时间影响提交材料后的等待，生成速度影响内容出现的速度。');
 chain(s,['提交材料','等待首次输出','持续生成','本轮完成'],64,270,1152,80);
 text(s,'生成速度通常以 token/s 表示。输出长度与生成速度共同决定生成阶段的持续时间。',64,421,1152,85,30);
 text(s,'完整任务还包括工具计算、补充资料和多轮修改。短问答适合即时跟进，较长分析可以提前提交，再在其他工作间隙查看结果。',64,548,1152,118,30);
}
T(15,'使用场景与选型顺序','上下文、模型能力与速度，需要结合使用方式和设备条件判断。',[
 ['使用场景','选择起点','后续判断'],['个人日常工作','容易部署和维护的整机','硬件确定后优先模型能力，再判断速度是否可接受'],['公司共享服务','单台八卡服务器的部署条件','综合能力、速度与框架支持']],[280,390,482],'以下分别说明个人设备和公司服务器的选择过程。',{h:290,font:28,tailY:578});
// 16–24: choices
section(16,'第三章\n模型选型与部署条件','结合设备使用方式、任务能力与运行体验\n说明个人端和服务器端的选择依据');
T(17,'个人设备的整机方案','个人工具需要方便部署，并能在日常使用中持续维护。',[
 ['整机','比较配置','使用路径'],['NVIDIA DGX Spark','128GB 统一内存\n4TB SSD','NVIDIA 软件栈\n连接员工电脑使用'],['Mac Studio，M5 Ultra','256GB 统一内存\n2TB SSD','macOS\nMLX 或 Metal 本地推理']],[410,330,412],'成熟整机集成计算、内存、散热和系统，安装、升级与维护可沿厂商提供的路径进行。',{h:310,font:27});
P(18,'DGX Spark 的选择依据',[
 '框架适配：Spark 支持 NVIDIA 软件与容器环境，厂商提供 vLLM、SGLang 等部署指南，具备本次研究所需的推理框架运行路径。',
 '维护衔接：个人设备与公司服务器采用 NVIDIA 路线，模型服务接口、框架配置、监控和维护经验可以延续。',
 '投入匹配：Spark 研究预算约 5.8–6.2 万元，M5 Ultra 256GB／2TB 配置的调研价格约 9.05 万元。综合购机、框架适配与维护，选择 Spark，并在 128GB 统一内存范围内确定模型。']);
T(19,'个人模型优先满足任务能力','GDPval-AA v2.1 比较模型使用文件、代码和网页工具完成专业工作后的交付物。',[
 ['个人候选模型／AA 推理标签','Elo'],['Qwen3.8-27B／Xhigh','1,417'],['Qwen3.6-35B-A3B／Reasoning','889'],['Gemma 4 31B／Reasoning','620']],[850,302],'2026 年 10 月 23 日读取，Elo 越高，工作交付表现越强。\nQwen3.8-27B 在本组候选中表现最强。结合稳定使用表现的调研判断，选择其作为个人主力，随后评估生成速度。',{h:280,tailFont:27});
T(20,'Qwen3.8-27B 的生成速度取舍','模型参数是训练形成并保存的数值。Qwen27 采用稠密架构，每步使用主体参数。Qwen3.6-35B-A3B 从总计35B中每步约激活3B，计算负担不同。',[
 ['输入 tokens','输出 tokens','首次输出等待','后续生成速度'],['50,000','2,048','63.1 秒','21.01 token/s'],['100,000','2,048','144.8 秒','20.11 token/s'],['500,000','2,048','1,470.1 秒','14.82 token/s']],[285,250,300,317],'外部测试采用 FP8 权重与缓存、MTP3、随机输入，关闭前缀缓存。前两档各两次，500K 一次。\n接受 50K–100K 输入下约 20 token/s 的体验，保留 Qwen27 的任务能力。长材料可提前提交。',{y:260,h:260,font:26,tailFont:25,tailY:555,tailH:140,introH:100});
T(21,'服务器模型与单机八卡条件','共享服务需综合考虑模型能力、推理速度、框架支持，以及模型与会话的资源占用。',[
 ['调研候选','当时采用的官方权重制品体量，约 GB'],['DeepSeek-V4.1-Flash','510'],['MiMo-V2.6-Pro-RL','566'],['GLM-5.3-Flash','328'],['GLM-5.3','756'],['Kimi K3','1,561']],[620,532],'权重文件体量用于判断部署容量。服务器还需为会话历史和持续计算保留资源。',{h:342,font:26,tailFont:27});
P(22,'初始服务器主力选择 DeepSeek-V4.1-Flash',[
 '模型规模与运行结构适合单机八卡。相较更大的候选，Flash 的模型体量更便于安排。大型 Engram 参数表可置于主机内存，压缩与共享历史的设计有利于长任务。',
 'vLLM、SGLang 提供部署路径，公开多卡运行记录提供速度参照。调研同时考虑较快推理、主流框架支持与后续维护。',
 '在能够承担目标工作的基础上，Flash 的模型能力、速度和部署条件形成适合当前服务器的组合。调研期间的新版本随后沿此路线更新。']);
T(23,'主力模型更新为 DeepSeek-V4.1-Flash-1017','1017 版本于 10 月 17 日发布，沿用既定架构与部署路线，并提升专业工作表现。',[
 ['版本／AA 推理标签','GDPval-AA v2.1 Elo'],['DeepSeek-V4.1-Flash／Max','1,600'],['DeepSeek-V4.1-Flash-1017／Max','1,746']],[820,332],'2026 年 10 月 23 日核对。1017 在本轮考察的开放模型中领先。\n服务器保留单机八卡部署方向，采用 DeepSeek-V4.1-Flash-1017 作为最终主力。',{h:250,tailFont:28});
{
 const s=S(24,'body','个人端与服务器端的最终选择','两条路径分别对应个人使用与公司共享服务的条件。');
 text(s,'个人端',64,238,520,42,32,{bold:true});text(s,'服务器端',664,238,520,42,32,{bold:true});
 const a=node(s,'成熟整机：DGX Spark\n衔接 NVIDIA 技术栈',64,312,520,90),b=node(s,'128GB 统一内存内优先模型能力\nQwen3.8-27B',64,452,520,90),c=node(s,'单台八卡部署条件\n原 Flash 兼顾能力、速度与框架',664,312,520,90),d=node(s,'1017 发布后沿既定路线更新\nDeepSeek-V4.1-Flash-1017',664,452,520,90);conn(s,a,b,'bottom','top');conn(s,c,d,'bottom','top');text(s,'个人端接受常用输入下约 20 token/s 的生成体验。运行环境进一步将两套配置组织为持续可用的服务。',64,606,1152,90,28);
}
// 25–37: runtime
section(25,'第四章\n运行环境与使用体验','共同运行过程\n个人设备实测与公司服务器安排');
{
 const s=S(26,'body','模型、推理框架与设备的分工','推理框架将模型计算、缓存和调度组织为持续运行的服务。');
 table(s,[['层次','主要职责'],['模型','理解输入，生成回答或工具请求'],['推理框架','加载模型，组织计算、缓存与请求调度'],['硬件设备','提供计算、内存、存储与连接']],64,206,1152,208,[250,902],25);
 text(s,'服务启动：框架加载模型，准备工作空间',64,443,1120,38,26);
 const a=node(s,'提交材料',64,510,218,62),b=node(s,'处理输入',364,510,218,62),c=node(s,'持续生成',664,510,218,62),d=node(s,'本轮结果',964,510,218,62);conn(s,a,b);conn(s,b,c);conn(s,c,d);const e=node(s,'新问题／工具结果',664,624,280,52);conn(s,d,e,'bottom','right',true,'elbow');conn(s,e,b,'left','bottom',true,'elbow');
}
T(27,'服务启动时的模型与工作空间','模型加载后，设备还需保存任务状态，并为实际计算保留空间。',[
 ['保留内容','请求过程中的用途'],['模型参数','供输入处理与生成使用'],['会话状态','保存已处理历史，支持生成与下一轮继续'],['执行空间','容纳临时计算、运行图和推测生成的草稿网络']],[330,822],'KV 缓存保存注意力计算中可重复使用的历史表示。部分模型还需保存其他状态，共同构成任务继续运行所需的计算状态。',{h:288,tailFont:28});
{
 const s=S(28,'body','输入处理与首次输出等待','输入处理称为 prefill。模型将材料转换为后续生成可用的表示，框架同时建立会话状态。');
 chain(s,['提交材料','排队与状态准备','处理输入','首个输出'],64,281,1152,90);
 text(s,'首次输出等待',64,420,1152,42,30,{bold:true});text(s,'等待包括排队、状态准备与输入处理，由本轮输入、已有状态及请求队列共同决定。',64,478,1152,88,30);
 text(s,'材料增加，会提高信息处理量及关系计算量。首个输出出现后，任务进入持续生成。',64,602,1152,88,30);
}
{
 const s=S(29,'body','持续生成与输出时间','后续生成称为 decode。每一步新内容成为下一步条件，模型持续生成直至本轮结束。');
 text(s,'设备反复读取模型参数和历史状态。低并发时，内存带宽经常影响这一阶段的速度。',64,236,1152,88,30);
 text(s,'推测生成先提出多个后续 token，再由目标模型一起验证，使一次计算推进更多内容。',64,363,1152,88,30);
 text(s,'8,192 tokens ÷ 20 token/s ≈ 410 秒 ≈ 6.8 分钟',64,505,1152,58,34,{bold:true,color:'accent1'});
 text(s,'该示例只计算持续生成时间。输入处理时间也需计入本轮主要等待。',64,615,1152,65,28);
}
{
 const s=S(30,'body','多轮任务中的历史复用','后续轮次会继续补充资料、调用工具和修改结果，输入中包含大量已经处理的历史。');
 text(s,'第一轮',64,238,120,42,28,{bold:true});const a=node(s,'材料',230,226,240,74),b=node(s,'处理并保存历史状态',570,226,520,74);conn(s,a,b);
 text(s,'下一轮',64,385,120,42,28,{bold:true});const c=node(s,'匹配的旧前缀\n复用已有计算',230,366,360,100),d=node(s,'新问题／工具结果',690,366,400,100),e=node(s,'处理新增部分，继续生成',390,520,540,74);conn(s,b,c,'bottom','top',true,'elbow');conn(s,c,e,'bottom','left',true,'elbow');conn(s,d,e,'bottom','right',true,'elbow');
 text(s,'前缀缓存查找可复用部分。系统要求和工具定义保持稳定、新内容追加在末尾，有利于延续已有状态。',64,634,1152,70,27);
}
T(31,'工具等待期间的状态保存','模型生成代码后由工具执行，结果返回后再继续。等待期间仍需保留会话状态。',[
 ['任务状态','资源安排'],['正在生成或即将继续','保留在快速工作内存中，直接接续'],['等待工具返回','按等待时间和资源情况安排缓存，恢复后继续'],['较长时间闲置','保存至下一层存储，为其他任务释放工作空间']],[390,762],'恢复时需取回与模型、历史前缀和运行格式相匹配的状态。框架将保存与恢复纳入任务生命周期。',{h:300,tailFont:28});
{
 const s=S(32,'body','共享服务中的请求调度','同一时刻可能同时存在新材料、持续生成和工具等待等不同状态的请求。');
 const a=node(s,'新材料',64,250,280,66),b=node(s,'正在生成',64,366,280,66),c=node(s,'工具结果返回',64,482,280,66),d=node(s,'框架调度',475,366,250,66),e=node(s,'一批计算',850,366,280,66);conn(s,a,d,'right','top',true,'elbow');conn(s,b,d);conn(s,c,d,'right','bottom',true,'elbow');conn(s,d,e);
 text(s,'返回各请求进展，继续安排下一批计算',475,489,655,70,27);
 text(s,'合批使多个请求共享计算机会。长输入分块处理，让框架在块之间继续推进已有请求的生成。',64,612,1152,85,28);
}
{
 const s=S(33,'two','DGX Spark 上 Qwen3.8-27B 的长输入表现','单台 DGX Spark GB10，128GB 统一内存\nQwen3.8-27B-FP8，vLLM 服务路径，FP8 缓存，MTP3');
 function chart(x,title,values,max,fmt){const ch=s.charts.add('bar',{position:{left:x,top:235,width:552,height:300},title,titleTextStyle:{fontSize:26,bold:false,fill:'tx1'},titlePlacement:'aboveChart',categories:['50K','100K','300K','500K'],series:[{name:title,values,fill:'accent1',valuesFormatCode:fmt}],barOptions:{direction:'column',grouping:'clustered',gapWidth:125},hasLegend:false,xAxis:{textStyle:{fontSize:22,fill:'tx2'},line:{fill:'tx2',width:1},title:{text:'实际输入 tokens',textStyle:{fontSize:21,fill:'tx2'}}},yAxis:{min:0,max,majorUnit:5,numberFormatCode:'0',textStyle:{fontSize:20,fill:'tx2'},majorGridlines:{fill:'bg2',width:1}},dataLabels:{showValue:true,position:'outEnd',numberFormatCode:fmt,textStyle:{fontSize:23,fill:'tx1'}},chartFill:'bg1',chartLine:{fill:'none',width:0}});applyPresentationChartFont(ch,{fontFamily:FONT});}
 chart(64,'首次输出等待（分钟）',[1.1,2.4,11,24.5],30,'0.0');chart(664,'后续生成速度（token/s）',[21.01,20.11,17.23,14.82],25,'0.00');
 text(s,'外部随机 token 测试，每次输出 2,048 tokens，关闭前缀缓存。\n50K、100K 各测试两次，300K、500K 各测试一次。',64,563,1152,65,23,{color:'tx2'});text(s,'输入增长会延长首次处理时间，并降低后续生成速度。较长材料可提前提交，追问沿已有历史继续。',64,644,1152,45,25);
}
T(34,'DGX Spark 的三路并发实例','沿用同一组 DGX Spark 与 Qwen3.8-27B-FP8 测试配置，三路请求同时提交，各生成 4,096 tokens。',[
 ['每路输入','共同生成总速度\n（token/s）','共同窗口每路平均\n（token/s）','各请求完整阶段平均\n（token/s）'],['50,000 tokens','59.08','19.69','16.85'],['100,000 tokens','52.41','17.47','12.45']],[270,294,294,294],'共同窗口指三路均在输出的时段。完整阶段还包含其他请求处理输入造成的等待，调度会影响每路体验。\nCPU 与 GPU 共用 128GB 统一内存，闲置会话可进一步考虑 SSD 保存与恢复。',{h:250,font:24,tailY:530,tailFont:27,tailH:150});
{
 const s=S(35,'body','单台八 H200 服务器的运行配置','DeepSeek-V4.1-Flash-1017 与 vLLM，采用单机共享服务。');
 const a=node(s,'同事的任务入口',370,220,540,58),b=node(s,'vLLM：请求、计算、缓存与调度',270,324,740,64),c=node(s,'8 张 H200：共同运行 DeepSeek-V4.1-Flash-1017',170,432,940,64),d=node(s,'CPU、主存与 SSD\n参数表、会话状态与任务文件',64,559,550,88),e=node(s,'同机隔离工具环境\n计算与文件处理',664,559,550,88);conn(s,a,b,'bottom','top');conn(s,b,c,'bottom','top');s.shapes.connect(c,d,{kind:'elbow',fromSide:'bottom',toSide:'top',line:{fill:'accent1',width:2},head:{type:'triangle',width:'sm',length:'sm'},tail:{type:'triangle',width:'sm',length:'sm'}});s.shapes.connect(d,e,{kind:'straight',fromSide:'right',toSide:'left',line:{fill:'accent1',width:2},head:{type:'triangle',width:'sm',length:'sm'},tail:{type:'triangle',width:'sm',length:'sm'}});
}
{
 const s=S(36,'body','1017 的模型与历史状态安排','发布制品约 510GB，其中 Engram 参数表及尺度约 203GB。');
 chain(s,['长输入','编码器处理','压缩、共享\n历史表示','解码器生成'],64,254,1152,90);
 chain(s,['主机内存中的\nEngram 参数表','按需查找','GPU 模型计算'],64,436,1152,90);
 text(s,'输入处理与生成采用不同计算路径。历史表示经过压缩、跨层共享，并由稀疏索引组织读取。\nEngram 大型查找表可置于主机内存，GPU、主存与 SSD 据此为模型、会话和工具分配空间。',64,586,1152,110,27);
}
T(37,'vLLM 对共享请求的组织','单台八 H200 服务器运行 DeepSeek-V4.1-Flash-1017。',[
 ['请求过程','运行安排'],['启动','加载 1017，安排参数表与计算空间'],['长材料进入','分块处理输入，与已有生成交错调度'],['持续生成','合批推进活动请求，检查推测生成的实际收益'],['下一轮继续','复用匹配前缀，恢复所需会话状态'],['工具等待','同机工具处理任务，模型服务接续其他请求']],[300,852],'规划目标为 20 路活动请求、每路约 20 token/s，对应系统总输出 400 token/s。实际承载能力需结合每日工作量与到达分布验证。',{h:342,font:25,tailFont:27});
// 38–44: workloads and costs
section(38,'第五章\n资源需求与成本','固定每日业务任务量\n比较单台设备与 API 服务的三年投入');
T(39,'20 人与 50 人情景的业务任务量','每人每天 5 项业务任务，每年 250 个工作日，三年保持相同规模。',[
 ['使用规模','每日任务','每年任务','三年任务'],['20 人','100 项','25,000 项','75,000 项'],['50 人','250 项','62,500 项','187,500 项']],[270,260,310,312],'一项业务任务涵盖读取材料、计算、补充、修改与交付，预算安排 8 轮模型调用，并增加 10% 完整轨迹用于修改与重试。\n50 人情景每天基础调用 2,000 次，含额外轨迹的预算约为 2,200 次。',{h:255,tailY:535,tailFont:27,tailH:160});
T(40,'每日 250 项任务的单机安排','相同工作量在不同时段到达，会形成不同的排队和等待。',[
 ['到达方式','运行安排'],['较均匀提交','持续处理输入与生成，保持队列平稳'],['集中提交','交互任务优先，长输入分块，检查排队与完成时间'],['可稍后完成的长任务','提前提交，安排在较空闲时段']],[360,792],'规划速度为 8,000 未缓存输入 tokens/s、400 输出 tokens/s，每日 250 项约需 5.43 小时整机计算。\n8 小时工作窗口按 70% 安排模型工作，提供 5.6 小时。50 人情景需重点验证高峰到达和工具等待。',{h:280,font:26,tailY:548,tailFont:27,tailH:150});
T(41,'八卡 H200 的国内采购预算','目标配置：8×H200 SXM/HGX，机内 NVSwitch 互联，主存与 SSD 支持参数表、缓存和工具工作。',[
 ['单台整机采购情景','预算'],['较低','500 万元'],['中间','550 万元'],['较高','600 万元']],[750,402],'9 月 16 日国内公开采价：H200 HGX 整机 566 万元，超微 H200 现货 575 万元含税。预算采用 550 万元，并观察上下 50 万元变化。\n实际采购按完整配置、交付与保修询价。个人 Spark（128GB／4TB）的研究预算约 5.8–6.2 万元。',{h:255,tailY:530,tailFont:26,tailH:165});
T(42,'本地部署的三年投入','50 人使用、单台八 H200，整机采购按 550 万元测算。单位：万元。',[
 ['费用组成','三年预算'],['整机与机房初次接入','553.00'],['初次实施','11.25'],['持续技术运维','45.00'],['电力、机位与软件支持','18.23'],['合计','627.48']],[820,332],'实施 45 人天、年运维 60 人天，技术人力 2,500 元／人天。采购价 500–600 万元时，三年投入约 577.48–677.48 万元。\n个人 Spark 按每天 3 项、三年固定使用，总投入约 9.05 万元。',{h:330,font:25,tailY:590,tailFont:25,tailH:115});
T(43,'API 的任务负载与计费口径','每项 8 轮：首轮输入 100K，后续每轮新增 8K 资料，并带入前轮 2K 输出。累计输入 1.08M、输出 16K。',[
 ['API／计价币种','普通输入','缓存读取','输出'],['DeepSeek-V4.1-Flash-1017\n高峰美元价','$0.30','$0.006','$1.20'],['GLM-5.3／境内人民币','¥8','¥2','¥28'],['Kimi K3／境内人民币','¥20','¥2','¥100']],[540,204,204,204],'2026 年 10 月 23 日官方费率，单位为每百万 tokens。输出含思考、工具参数与正文。\nDeepSeek 低峰减半，按 80% 高峰和 USD/CNY＝7.00 测算。Kimi 写入价为 5 分钟 ¥20、1 小时 ¥40，基准取 1 小时。\nAPI 统一假设累计输入 80% 命中缓存，另增 10% 轨迹。输入按互斥类别计费，输出另计。',{h:280,font:25,tailY:535,tailFont:24,tailH:170});
T(44,'固定使用规模下的本地与 API 三年预算','单位：万元。本地按 550 万元购机，API 按 2026 年 10 月 23 日公开费率。',[
 ['方案','20 人\n75,000 项业务任务','50 人\n187,500 项业务任务'],['单台八 H200，本地 1017','626.03','627.48'],['DeepSeek-V4.1-Flash-1017 API','48.14','55.09'],['GLM-5.3 API','75.71＋缓存存储费','124.02＋缓存存储费'],['Kimi K3 API，1 小时缓存','142.24','290.34']],[550,301,301],'API 总额均含 43.5 万元接入、技术运维与平台支持。GLM 缓存存储目前限时免费，后续按公布标准计入。\n两种规模下，API 支出均较低。本地投入同时获得模型与资料处理环境的控制权，应对应持续发生且具有本地使用价值的工作。',{y:205,h:315,font:25,tailY:548,tailFont:25,tailH:158});
// 45–49: applications and validation
section(45,'第六章\n日常应用与验证','使用入口与资料接入\n通过实际任务检验部署选择');
{
 const s=S(46,'body','本地服务的使用路径','使用入口与任务执行位置，按个人工作和公司共享任务分别安排。');
 text(s,'个人文件与代码工作',64,226,1152,40,30,{bold:true});chain(s,['员工电脑上的\nOpenCode／文件工具','Spark 模型服务','结果回到工作目录'],64,289,1152,84);
 text(s,'公司共享任务',64,426,1152,40,30,{bold:true});const n=chain(s,['浏览器入口','身份与任务管理','服务器任务执行层'],64,482,1152,72);text(s,'任务执行层衔接主力模型与同机隔离工具环境。模型提出操作，工具返回结果后，模型继续处理。',64,590,1152,70,27);text(s,'个人工具使用员工电脑上的文件，共享任务在服务器授权目录中执行。',64,665,1152,42,27);
}
{
 const s=S(47,'body','公司资料与工具的接入','检索增强生成（RAG）先检索用户获准读取的相关资料，再交给模型回答并提供引用。');
 chain(s,['身份与问题','获准范围内检索','授权过滤与重排','依据片段回答\n核验引用'],64,250,1152,90);
 text(s,'平台可比较 Onyx Enterprise 与 Milvus＋自建 RAG 服务＋Open WebUI。前者集中提供企业知识平台能力，后者由团队组合并维护检索、权限与应用。两条路线均需衔接 NAS 身份、访问范围和撤权更新。',64,406,1152,150,28);
 text(s,'文件读取、计算和代码执行可通过工具提供。Skills 保存可复用的操作说明，MCP 等接口连接外部工具，由同一任务入口组织使用。',64,593,1152,100,28);
}
T(48,'部署方案的任务验证','从具有明确交付物的工作开始，积累公司自身的使用依据。',[
 ['验证工作','交付与检查方式','支持的决策'],['公告字段整理','字段表与出处，检查主体、日期、金额和覆盖','首批文档工作的范围'],['研究代码辅助','可复跑的修改、测试与结果文件','模型与工具的配合方式'],['财报比较','数字、期间、口径、计算文件与引用','共享模型的质量收益'],['权限知识问答','按身份检查检索和引用，测试撤权更新','公司资料接入范围']],[260,560,332],'记录首次等待、生成停顿、完整任务时间、重试与人工复核。观察材料增长、工具返回及多人使用对体验的影响，为后续配置提供依据。',{h:330,font:24,tailFont:27});
P(49,'公司本地部署的选择与后续验证',[
 '选型：个人端选择 DGX Spark，并在 128GB 统一内存范围内优先模型能力，采用 Qwen3.8-27B。服务器从单机八卡条件选出 Flash，随后更新为 DeepSeek-V4.1-Flash-1017。',
 '运行：沿共同的请求过程安排模型、缓存与调度，结合 Spark 实例和八 H200 服务器配置，形成各自的运行路径。',
 '投入与验证：按 20 人、50 人的固定业务任务量比较本地与 API 的完整三年预算。下一步以任务产物检查能力与体验，记录等待、复核和净节省时间，为本地服务建立实际依据。']);
await fs.mkdir(path.join(fullDir,'previews'),{recursive:true});
for(const [i,s]of pres.slides.items.entries()){await fs.writeFile(path.join(fullDir,'previews',`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await(await pres.export({slide:s,format:'png',scale:1})).arrayBuffer()));await fs.writeFile(path.join(fullDir,'previews',`slide-${String(i+1).padStart(2,'0')}.json`),await(await s.export({format:'layout',detail:'full'})).text());}
await(await PresentationFile.exportPptx(pres)).save(path.join(fullDir,'artifact-full-draft.pptx'));
await fs.writeFile(path.join(fullDir,'content-map.json'),JSON.stringify({count:49,bodyCount:41,timeBudgetMinutes:40,source:sourceDir+'/extended-draft-d-revised-4.md',slides:mapping},null,2));
console.log('Created complete 49-slide editable deck.');
