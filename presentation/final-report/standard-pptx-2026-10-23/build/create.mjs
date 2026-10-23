import fs from 'node:fs/promises';
import path from 'node:path';
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
function text(s,txt,x,y,w,h,size=26,opts={}){const sh=s.shapes.add({geometry:'textbox',name:txt.slice(0,22),position:{left:x,top:y,width:w,height:h},fill:opts.fill||'none',line:{fill:'none',width:0}});sh.text=txt;sh.text.style={fontSize:size,color:opts.color||'tx1',bold:opts.bold||false,alignment:opts.align||'left',verticalAlignment:'top',autoFit:'none',insets:0};return sh;}
function node(s,txt,x,y,w,h){const sh=s.shapes.add({geometry:'rect',name:txt.split('\n')[0],position:{left:x,top:y,width:w,height:h},fill:'bg1',line:{fill:'accent1',width:1.5}});sh.text=txt;sh.text.style={fontSize:26,color:'tx1',alignment:'center',verticalAlignment:'middle',autoFit:'none',insets:8};return sh;}
function conn(s,a,b,from='right',to='left',arrow=true,kind='straight'){return s.shapes.connect(a,b,{kind,fromSide:from,toSide:to,line:{fill:'accent1',width:2},...(arrow?{tail:{type:'triangle',width:'sm',length:'sm'}}:{})});}
function table(s,values,x,y,w,h,widths,font=25){const t=s.tables.add({rows:values.length,columns:values[0].length,left:x,top:y,width:w,height:h,columnWidths:widths,values});t.styleOptions={headerRow:true,bandedRows:false};t.borders.assign({fill:'bg2',width:1,style:'solid'});for(let r=0;r<values.length;r++){t.rows[r].height=h/values.length;for(let c=0;c<values[0].length;c++){const cell=t.getCell(r,c);cell.fill=r===0?'accent1':(r%2===0?'bg2':'bg1');cell.text.style={fontSize:font,color:r===0?'bg1':'tx1',bold:r===0,autoFit:'none',verticalAlignment:'middle',alignment:c===0?'left':'center'};}}t.cells.block({row:0,column:0,rowCount:values.length,columnCount:values[0].length}).assign({margins:{left:14,right:14,top:10,bottom:10},anchor:'center'});return t;}
const sourceDir='/Users/sthmax/dev/git/ms-intern/presentation/final-report/narrative-drafts-2026-10-22';
const notesBase='内容依据：'+sourceDir+'/extended-draft-d-revised-4.md\n证据核验日期：2026年10月23日。';
slide('cover','公司本地部署 LLM\n模型、运行环境与成本','实习研究汇报\n\n金融工作需求与部署选择依据\n2026 年 10 月 23 日',notesBase);
{
 const s=slide('body','汇报内容','围绕金融工作需求，说明模型选型、运行安排与投入预算。',notesBase);
 table(s,[['章节','主要内容'],['一、金融工作与本地部署需求','应用场景与使用环境'],['二、分析任务对模型的要求','上下文、模型能力与速度'],['三、模型选型','个人设备与公司服务器的选择依据'],['四、运行环境与使用体验','请求处理、多轮任务与共享使用'],['五、资源需求与成本','单台设备与 API 的三年投入'],['六、日常应用与验证','使用入口、资料接入与验证工作']],64,224,1152,410,[560,592],27);
}
{
 const s=slide('body','固定资源下的上下文、模型能力与速度','给定硬件、并发规模和运行方式，三项要求共享内存与计算预算。',notesBase);
 const a=node(s,'模型能力\n理解材料、完成分析',275,222,270,88),b=node(s,'上下文\n带入材料与历史',70,490,270,88),c=node(s,'速度\n缩短等待、持续生成',485,490,270,88);
 conn(s,a,b,'left','top',false);conn(s,a,c,'right','top',false);conn(s,b,c,'right','left',false);
 text(s,'更多信息需要\n更多分析',83,345,210,66,24,{fill:'bg1',align:'center'});text(s,'更充分的推理\n需要计算时间',526,345,230,66,24,{fill:'bg1',align:'center'});text(s,'更长输入增加\n处理与状态负担',296,592,232,68,24,{align:'center'});
 text(s,'材料增加，设备需要处理并保留更多信息。',844,242,360,100,28);text(s,'更多思考步骤或计算量更大的模型，会提高单项任务的资源占用。',844,365,360,134,28);text(s,'选型需明确材料规模、分析要求与可接受的等待时间。',844,525,360,112,28);
}
slide('section','第四章\n运行环境与使用体验','共同运行过程\n个人设备实测与公司服务器安排',notesBase);
{
 const s=slide('body','模型、推理框架与设备的分工','推理框架将模型计算、缓存和调度组织为持续运行的服务。',notesBase+'\n来源：AI Infra第3章与第8章，固定修订3bdcb4fcab73010eeaccf31cc10a8242a895d82e。\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-078/upstream/manuscripts/03-推理与训练负载.md\n/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-078/upstream/manuscripts/08-推理优化.md');
 table(s,[['层次','主要职责'],['模型','理解输入，生成回答或工具请求'],['推理框架','加载模型，组织计算、缓存与请求调度'],['硬件设备','提供计算、内存、存储与连接']],64,206,1152,208,[250,902],25);
 text(s,'服务启动：框架加载模型，准备工作空间',64,443,1120,38,26);
 const a=node(s,'提交材料',64,510,218,62),b=node(s,'处理输入',364,510,218,62),c=node(s,'持续生成',664,510,218,62),d=node(s,'本轮结果',964,510,218,62);conn(s,a,b);conn(s,b,c);conn(s,c,d);const e=node(s,'新问题／工具结果',664,624,280,52);conn(s,d,e,'bottom','right',true,'elbow');conn(s,e,b,'left','bottom',true,'elbow');
}
{
 const s=slide('two','DGX Spark 上 Qwen3.8-27B 的长输入表现','单台 DGX Spark GB10，128GB 统一内存\nQwen3.8-27B-FP8，vLLM 服务路径，FP8 缓存，MTP3',notesBase+'\n来源：/Users/sthmax/dev/git/ms-intern/knowledge-base/sources/TECH-076/original.md\n外部测试。随机token输入，每次输出2,048 tokens，关闭前缀缓存。50K与100K各两次，300K与500K各一次。');
 function chart(x,title,values,max,fmt){const ch=s.charts.add('bar',{position:{left:x,top:235,width:552,height:300},title,titleTextStyle:{fontSize:26,bold:false,fill:'tx1'},titlePlacement:'aboveChart',categories:['50K','100K','300K','500K'],series:[{name:title,values,fill:'accent1',valuesFormatCode:fmt}],barOptions:{direction:'column',grouping:'clustered',gapWidth:125},hasLegend:false,xAxis:{textStyle:{fontSize:22,fill:'tx2'},line:{fill:'tx2',width:1},title:{text:'实际输入 tokens',textStyle:{fontSize:21,fill:'tx2'}}},yAxis:{min:0,max,majorUnit:5,numberFormatCode:'0',textStyle:{fontSize:20,fill:'tx2'},majorGridlines:{fill:'bg2',width:1}},dataLabels:{showValue:true,position:'outEnd',numberFormatCode:fmt,textStyle:{fontSize:23,fill:'tx1'}},chartFill:'bg1',chartLine:{fill:'none',width:0}});applyPresentationChartFont(ch,{fontFamily:FONT});}
 chart(64,'首次输出等待（分钟）',[1.1,2.4,11,24.5],30,'0.0');chart(664,'后续生成速度（token/s）',[21.01,20.11,17.23,14.82],25,'0.00');
 text(s,'外部随机 token 测试，每次输出 2,048 tokens，关闭前缀缓存。\n50K、100K 各测试两次，300K、500K 各测试一次。',64,563,1152,65,23,{color:'tx2'});text(s,'输入增长会延长首次处理时间，并降低后续生成速度。较长材料可提前提交，追问沿已有历史继续。',64,644,1152,45,25);
}
{
 const s=slide('body','固定使用规模下的本地与 API 三年预算','单位：万元。本地按 550 万元购机，API 按 2026 年 10 月 23 日公开费率。',notesBase+'\n预算证据：'+sourceDir+'/d-revised-4-evidence.md，第1至6节。\n计算：'+sourceDir+'/d-revised-4-data.json。\nAPI官方费率：https://api-docs.deepseek.com/quick_start/pricing/\nhttps://docs.bigmodel.cn/cn/guide/start/pricing\nhttps://platform.kimi.com/docs/pricing/chat\n统一情景：每人每天5项任务，每年250个工作日，三年固定规模。每项8轮，累计1.08M输入与16K输出，累计输入80%缓存读取，10%额外轨迹。DeepSeek预算80%高峰、USD/CNY=7.00。Kimi基准1小时缓存。\n预算为研究测算，购机按完整服务器国内采购情景。');
 table(s,[['方案','20 人\n75,000 项任务','50 人\n187,500 项任务'],['单台八 H200，本地 1017','626.03','627.48'],['DeepSeek-V4.1-Flash-1017 API','48.14','55.09'],['GLM-5.3 API','75.71＋缓存存储费','124.02＋缓存存储费'],['Kimi K3 API，1 小时缓存','142.24','290.34']],64,205,1152,315,[550,301,301],25);
 text(s,'API 总额均包含 43.5 万元的接入、技术运维与平台支持。GLM 缓存存储目前限时免费，后续费用按公布的标准计入。',64,548,1152,65,24,{color:'tx2'});text(s,'两种使用规模下，API 支出均较低。\n本地部署的投入同时获得模型与资料处理环境的控制权，应对应持续发生且具有本地使用价值的工作。',64,622,1152,88,24);
}
await fs.mkdir(path.join(root,'build','previews'),{recursive:true});
for(const [i,s] of pres.slides.items.entries()){await fs.writeFile(path.join(root,'build','previews',`slide-${i+1}.png`),new Uint8Array(await (await pres.export({slide:s,format:'png',scale:1})).arrayBuffer()));await fs.writeFile(path.join(root,'build','previews',`slide-${i+1}.layout.json`),await (await s.export({format:'layout',detail:'full'})).text());}
await (await PresentationFile.exportPptx(pres)).save(path.join(root,'build','artifact-draft.pptx'));
await fs.writeFile(path.join(root,'build','content-map.json'),JSON.stringify({source:sourceDir+'/extended-draft-d-revised-4.md',sourcePages:[1,2,11,25,26,33,44],count:7,font:FONT},null,2));console.log('Created 7 editable slides.');
