import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Presentation,PresentationFile} from '@oai/artifact-tool';
import {slides,sources} from '../src/content.mjs';
const B=path.dirname(fileURLToPath(import.meta.url)),R=path.dirname(B);
const F='PingFang SC';
const C={blue:'#005A9C',ink:'#20262C',muted:'#707C88',line:'#BCC6CF',pale:'#D9EAF7',very:'#F3F7FA',teal:'#317F7B',mint:'#DCEFEA',purple:'#7363A6',lav:'#E8E3F2',gold:'#967335',mark:'#FFF0BE',red:'#AD5247',white:'#FFFFFF'};
const P=Presentation.create({slideSize:{width:1600,height:900}});P.theme.defaultFont=F;
P.theme.colorScheme={name:'Business Blue',themeColors:{accent1:C.blue,accent2:C.teal,accent3:C.purple,accent4:C.gold,accent5:C.red,accent6:C.muted,bg1:C.white,bg2:C.very,tx1:C.ink,tx2:C.muted,dk1:C.ink,dk2:C.blue,lt1:C.white,lt2:C.pale,hlink:C.blue,folHlink:C.purple}};
const tableOwners=[],diagrams=[],manifest=[];
function box(s,x,y,w,h,fill=C.white,line=C.line,lw=1){return s.shapes.add({geometry:'rect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:line,width:line==='none'?0:lw,style:'solid'}});}
function txt(s,v,x,y,w,h=55,size=28,color=C.ink,bold=false,align='left'){
 const q=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});q.text=v;q.text.style={typeface:F,fontSize:size,color,bold,alignment:align,verticalAlignment:'top',autoFit:'none',wrap:'square',insets:0};q.text.insets=0;return q;
}
function line(s,x1,y1,x2,y2,color=C.line,width=1.5){return s.shapes.add({geometry:'line',position:{left:Math.min(x1,x2),top:Math.min(y1,y2),width:Math.abs(x2-x1)||.1,height:Math.abs(y2-y1)||.1,horizontalFlip:x2<x1,verticalFlip:y2<y1},fill:'none',line:{fill:color,width,style:'solid'}});}
function connect(s,a,b,{from='right',to='left',color=C.blue,kind='elbow',arrow=true}={}){const q=s.shapes.connect(a,b,{kind,fromSide:from,toSide:to,line:{fill:color,width:2,style:'solid'},tail:{type:arrow?'triangle':'none',width:'sm',length:'sm'}});q.bringToFront();return q;}
function arrow(s,x,y,w=50,color=C.blue,dir='right'){const q=s.shapes.add({geometry:'rightArrow',position:{left:x,top:y,width:w,height:15,rotation:dir==='down'?90:dir==='left'?180:0},fill:color,line:{fill:'none',width:0}});return q;}
function band(s,label,x,y,w,fill=C.blue){box(s,x,y,w,49,fill,'none');txt(s,label,x+16,y+8,w-32,37,27,C.white,true);}
function node(s,title,x,y,w=240,h=92,{fill=C.pale,color=C.ink,size=28,sub,stroke='none'}={}){const q=box(s,x,y,w,h,fill,stroke);const offset=sub?15:Math.max(13,(h-size*1.25*title.split('\n').length)/2);txt(s,title,x+18,y+offset,w-36,sub?48:h-offset-8,size,color,true,'center');if(sub)txt(s,sub,x+18,y+60,w-36,h-67,24,C.muted,false,'center');return q;}
function caption(s,v,x,y,w=1464,color=C.blue,size=28){txt(s,v,x,y,w,80,size,color,true);}
function example(s,x=1432,y=177){txt(s,'示例',x,y,100,32,20,C.muted,false,'right');}
function footer(s,d){line(s,68,841,1532,841,C.line,1.2);const refs=d.refs.map(([k])=>sources[k]?.short).filter(Boolean);let f=refs.length?'来源：'+[...new Set(refs)].join('；'):'';if(f.length>86)f=f.slice(0,85)+'等';if(f)txt(s,f,68,855,1360,26,14,C.muted);txt(s,String(d.id).padStart(2,'0'),1467,852,65,29,17,C.ink,false,'right');}
function base(d){const s=P.slides.add();s.background.fill=C.white;if(d.section)txt(s,d.section,68,37,1450,30,20,C.blue);if(d.kind!=='cover')txt(s,d.title,68,83,1464,72,44,C.ink,true);footer(s,d);if(d.example)example(s);let refs=d.refs.map(([k,loc])=>`${sources[k].id}，${loc}\n${sources[k].url||''}`).join('\n\n');s.speakerNotes.text=d.notes+(refs?'\n\n来源：\n'+refs:'');return s;}
function table(s,id,cols,rows,x,y,w,h,widths,size=25){const t=s.tables.add({rows:rows.length+1,columns:cols.length,left:x,top:y,width:w,height:h,columnWidths:widths,values:[cols,...rows]});t.cells.block({row:0,column:0,rowCount:rows.length+1,columnCount:cols.length}).assign({fill:C.white,textStyle:{fontSize:size,typeface:F,color:C.ink},margins:{left:15,right:15,top:11,bottom:11},anchor:'center'});t.borders.assign({fill:C.line,width:.7,style:'solid'});t.cells.block({row:0,column:0,rowCount:1,columnCount:cols.length}).assign({fill:C.blue,textStyle:{fontSize:size,typeface:F,color:C.white,bold:true}});for(let r=2;r<=rows.length;r+=2)t.cells.block({row:r,column:0,rowCount:1,columnCount:cols.length}).assign({fill:C.very});tableOwners.push(id);return t;}
function doc(s,title,x,y,w,h,rows,{version='',highlight=[],size=25}={}){const q=box(s,x,y,w,h,C.white,C.line,1.4);txt(s,title,x+24,y+20,w-48,46,28,C.ink,true);if(version)txt(s,version,x+24,y+69,w-48,32,21,C.muted);line(s,x+24,y+112,x+w-24,y+112,C.line,1);const rh=(h-141)/rows.length;rows.forEach((r,i)=>{let ry=y+127+i*rh;if(highlight.includes(i))box(s,x+20,ry-3,w-40,rh-7,C.mark,'none');txt(s,r[0],x+28,ry,w-56,34,22,C.blue,true);txt(s,r[1],x+28,ry+38,w-56,rh-42,size,C.ink);});return q;}
function steps(s,items,x,y,w,h=112,{gap=44,size=28,fill=C.pale}={}){const nw=(w-gap*(items.length-1))/items.length;let prev;const out=[];items.forEach((v,i)=>{const a=node(s,v,x+i*(nw+gap),y,nw,h,{fill,size});if(prev)connect(s,prev,a);prev=a;out.push(a);});return out;}
function lane(s,label,y,h=135,{color=C.blue}={}){box(s,68,y,1464,h,C.white,'none');box(s,68,y,200,h,C.very,'none');txt(s,label,86,y+Math.max(26,(h-38)/2),164,54,27,color,true);line(s,68,y+h,1532,y+h,C.line,1);}
function tag(s,v,x,y,w=280,color=C.muted,size=23){txt(s,v,x,y,w,64,size,color);}

function buildSlide(d){const s=base(d);if(d.id>1)diagrams.push(d.id);
switch(d.kind){
case 'cover':{
 txt(s,'同行实践与公司方案',96,205,1408,65,31,C.blue,true);
 txt(s,'资管公司工作流程中的\nLLM 应用',96,301,1408,188,68,C.ink,true);
 line(s,99,567,1499,567,C.blue,4);
 txt(s,'2026年10月',99,616,1200,50,30,C.muted);break;}
case 'scope':{
 band(s,'日常输入',68,226,315);band(s,'同事完成工作的过程',475,226,650);band(s,'工作成果',1217,226,315);
 ['文档','数据','消息','业务需求'].forEach((v,i)=>tag(s,v,105,317+i*90,240,C.ink,30));
 ['资料处理','分析解释','业务操作','协作交付'].forEach((v,i)=>{let y=305+i*92;box(s,475,y,650,65,i%2?C.very:C.pale,'none');txt(s,v,503,y+13,594,44,30,C.ink,true);});
 ['分析','操作','材料','工具'].forEach((v,i)=>tag(s,v,1254,317+i*90,240,C.ink,30));arrow(s,402,480,52);arrow(s,1146,480,52);
 caption(s,'沿业务流程建设应用，让同事在日常任务中使用 LLM',68,749,1464,C.blue,31);break;}
case 'map':{
 const cols=[['前台',['研究分析','交易支持','客户材料'],C.pale],['中台',['材料审核','风险分析'],C.mint],['后台',['运营文件','工具开发'],C.lav]];
 cols.forEach((a,i)=>{let x=68+i*500;band(s,a[0],x,229,464);a[1].forEach((v,j)=>{box(s,x,309+j*106,464,76,a[2],'none');txt(s,`${[1,4,6][i]+j}  ${v}`,x+25,329+j*106,414,50,30,C.ink,true);});});
 line(s,68,664,1532,664,C.line,1);txt(s,'两条贯穿任务',68,696,275,43,27,C.ink,true);
 line(s,370,720,452,720,C.teal,5);txt(s,'甲公司：研究、交易、风险与运营',481,696,1000,50,28,C.teal);
 line(s,370,783,452,783,C.purple,5);txt(s,'客户沟通稿：生成、审核、版本更新',481,758,1000,50,28,C.purple);break;}
case 'research_flow':{
 caption(s,'甲公司本季度发生了什么变化，原因是什么，各方怎么看',68,201,1370,C.blue,31);
 lane(s,'资料来源',294,145);lane(s,'研究员',439,179);lane(s,'研究成果',618,154);
 const xs=[300,550,800,1050,1300],ws=[204,204,204,204,204];
 ['财报','券商研报','会议资料'].forEach((v,i)=>node(s,v,xs[i],324,ws[i],74,{fill:C.very,size:27}));
 let a=steps(s,['收集资料','提取数据','计算变化','比较观点','形成分析'],300,480,1204,88,{gap:46,size:27});
 ['检索','摘录','核对','整理'].forEach((v,i)=>tag(s,v,xs[i],582,204,C.muted,23));
 const b=node(s,'变化与经营原因',424,660,430,70,{fill:C.pale,size:28});const c=node(s,'观点比较与研究要素',934,660,570,70,{fill:C.pale,size:28});
 break;}
case 'driver_tree':{
 txt(s,'盈利变化按经营因素逐层展开',68,203,1200,54,31,C.blue,true);
 const root=node(s,'净利润变化',68,412,235,106,{fill:C.blue,color:C.white,size:31});
 const mids=[['收入',300],['成本',443],['费用',586]].map(([v,y])=>node(s,v,413,y,238,82,{size:30}));
 const drivers=[['销量、单价',300],['原材料、生产成本',443],['渠道、销售费用',586]].map(([v,y])=>node(s,v,775,y,335,82,{fill:C.very,size:28}));
 mids.forEach((m,i)=>{connect(s,root,m,{kind:'elbow'});connect(s,m,drivers[i]);});
 band(s,'取数与计算',1217,278,315);['调用财务数据','计算变化与贡献','关联行业信息'].forEach((v,i)=>txt(s,v,1235,362+i*95,279,62,27,C.ink));
 line(s,1217,658,1532,658,C.line,1);txt(s,'结构化归因结果',1217,687,315,55,30,C.blue,true);
 caption(s,'研究员据此继续判断增长质量与可持续性',68,767,1464,C.ink,28);break;}
case 'views':{
 steps(s,['多份研报','相关性筛选','按问题形成小结','比较并汇总'],68,232,1464,92,{gap:70,size:28});
 band(s,'甲公司  市场观点对照',68,387,1464);
 const xs=[68,562,1056],w=476;const titles=['研报A','研报B','观点汇总'];
 const vals=[['销量增长带动收入','关注渠道补库持续性'],['价格改善支持利润','关注原材料成本变化'],['共识：经营表现改善','差异：增长驱动与持续性']];
 titles.forEach((t,i)=>{txt(s,t,xs[i]+19,471,w-38,46,30,i===2?C.blue:C.ink,true);vals[i].forEach((v,j)=>{line(s,xs[i]+19,532+j*99,xs[i]+w-19,532+j*99,C.line,1);txt(s,v,xs[i]+19,553+j*99,w-38,78,27,C.ink);});});
 caption(s,'按同一研究问题比较观点，汇总共识与分歧',68,759,1464,C.blue,29);break;}
case 'elements':{
 band(s,'资料中的信息',68,229,478);band(s,'研究要素表示例',640,229,892);
 doc(s,'甲公司研究资料',68,309,478,423,[['财报','产品销售与经营指标'],['会议纪要','渠道变化与经营解释'],['研报','增长判断与关注事项']],{size:25});
 table(s,d.id,['研究要素','填报内容','资料出处'],[['经营变化','销量增长','财报'],['驱动因素','渠道补库','会议纪要'],['关注事项','成本变动','研报']],640,309,892,423,[235,340,317],25);arrow(s,568,512,50);
 txt(s,'中欧披露，截至2026年5月，整体编制效率提升约50%',68,765,1464,56,28,C.blue,true);break;}
case 'research_proposal':{
 const a=node(s,'研究员提交\n甲公司与研究问题',68,270,320,123,{fill:C.very,size:29});
 const b=node(s,'检索资料',478,270,300,123,{size:30});const c=node(s,'提取与计算',478,457,300,108,{size:30});const e=node(s,'比较与解释',478,631,300,108,{size:30});connect(s,a,b);connect(s,b,c,{from:'bottom',to:'top'});connect(s,c,e,{from:'bottom',to:'top'});
 const f=doc(s,'甲公司季度分析',944,228,588,511,[['财务变化','本季度变化与计算口径'],['经营原因','经营因素及对应证据'],['观点与要素','观点分歧、研究要素与出处']],{version:'研究结果',size:26});connect(s,e,f,{kind:'elbow'});
 txt(s,'继续追问与更新资料',68,477,318,82,28,C.blue,true);line(s,228,578,228,704,C.blue,2);line(s,228,704,431,704,C.blue,2);arrow(s,420,697,40);
 txt(s,'固收应用：评级报告、募集说明书形成基本面更新材料',68,779,1464,46,26,C.muted);break;}
case 'trade_lanes':{
 ['投资经理','交易员','业务系统'].forEach((v,i)=>lane(s,v,252+i*166,166));
 const a=node(s,'甲公司相关债券\n筛选条件',312,289,290,93,{size:27});const b=node(s,'报价比较',788,457,280,91,{size:28});const c=node(s,'成交要素核对',1195,457,309,91,{size:28});
 const q=node(s,'行情与持仓查询',529,621,320,89,{fill:C.very,size:28});const t=node(s,'交易指令准备',1195,621,309,89,{fill:C.very,size:28});connect(s,a,q,{from:'bottom',to:'top',kind:'elbow'});connect(s,q,b,{from:'top',to:'bottom',kind:'elbow'});connect(s,b,c);connect(s,c,t,{from:'bottom',to:'top'});
 txt(s,'券名、方向',313,386,278,32,23,C.muted);txt(s,'券名、价格、数量',789,420,376,32,23,C.muted);txt(s,'券名、方向、价格、数量',1080,746,450,42,23,C.blue,true);break;}
case 'trade_cases':{
 band(s,'南方基金  小喃同学',68,222,1464);steps(s,['自然语言请求','条件解析与筛券','行情、持仓查询','接入业务接口'],68,311,1464,103,{gap:62,size:28});
 txt(s,'收益率、评级、期限等条件直接进入查询',68,440,1464,54,27,C.muted);
 band(s,'兴证全球基金  千询',68,526,1464);steps(s,['经理询价意向','报价与对手匹配','聊天转成交要素','推送交易系统'],68,615,1464,103,{gap:62,size:28});
 txt(s,'经理在交易系统完成指令下达',68,749,1464,54,27,C.muted);break;}
case 'trade_proposal':{
 const a=node(s,'同一任务入口',68,234,290,110,{fill:C.blue,color:C.white,size:30});txt(s,'查询甲公司债券\n比较报价\n整理交易要素',68,383,290,140,28,C.ink);
 band(s,'候选与报价',478,222,1054);table(s,d.id,['券名','方向','价格','数量'],[['甲公司债A','买入','按实时报价','按投资意图'],['甲公司债B','买入','按实时报价','按投资意图']],478,299,1054,235,[317,200,270,267],26);
 const n=node(s,'结构化交易要素',478,613,400,95,{size:29});const k=node(s,'已有交易系统',1132,613,400,95,{fill:C.very,size:29});connect(s,n,k);connect(s,a,n,{kind:'elbow'});
 txt(s,'券名、方向、价格、数量沿流程复用',478,758,1054,50,29,C.blue,true);break;}
case 'materials_flow':{
 band(s,'已有资料',68,236,388);['经理观点','产品资料','研究报告','客户问题'].forEach((v,i)=>node(s,v,68,319+i*104,388,72,{fill:C.very,size:28}));
 const a=node(s,'按问题检索',612,359,370,101,{size:30});const b=node(s,'按用途重新组织',612,575,370,101,{size:30});connect(s,a,b,{from:'bottom',to:'top'});line(s,491,355,491,667,C.line,2);line(s,456,355,491,355,C.line,2);line(s,456,667,491,667,C.line,2);line(s,491,409,575,409,C.blue,2);arrow(s,565,402,35);
 ['路演材料','产品问答','机构标书'].forEach((v,i)=>{const n=node(s,v,1160,320+i*161,372,85,{fill:C.pale,size:29});connect(s,b,n,{kind:'elbow'});});
 caption(s,'一份研究与产品资料，支持多种客户沟通用途',68,775,1464,C.blue,29);break;}
case 'manager_views':{
 steps(s,['路演纪要、评论与定期报告','按经理或产品整理','销售摘要、早评与收评'],68,230,1464,113,{gap:75,size:29});
 band(s,'观点原材料',68,419,674);band(s,'客户表达',858,419,674);
 txt(s,'经理关注企业经营改善，\n持续跟踪订单与成本变化。',95,518,620,155,33,C.ink);
 txt(s,'本期关注点是经营变化。\n后续跟踪订单与成本，\n解释观点更新的依据。',885,518,620,174,31,C.ink);
 arrow(s,775,566,50);txt(s,'销售按客户问题调取既有观点，再组织为可沟通的材料',68,769,1464,53,28,C.blue,true);break;}
case 'tender':{
 const xs=[68,594,1120],w=412;['机构客户问题','公司知识资料','标书章节'].forEach((v,i)=>band(s,v,xs[i],234,w));
 const rows=[['投研流程如何组织','投研流程说明','投研能力章节'],['产品信息如何表述','产品文件与定期报告','产品介绍章节'],['运营如何支持服务','业务制度与操作说明','运营服务章节']];
 rows.forEach((r,i)=>{const y=344+i*143;let a=node(s,r[0],68,y,w,88,{fill:C.very,size:26});let b=node(s,r[1],594,y,w,88,{fill:C.pale,size:26});let c=node(s,r[2],1120,y,w,88,{fill:C.very,size:26});connect(s,a,b);connect(s,b,c);});
 caption(s,'问题、回答与资料出处逐项对应，复用已有业务知识',68,779,1464,C.blue,29);break;}
case 'client_proposal':{
 band(s,'材料任务',68,235,465);txt(s,'客户问题：本期关注什么\n产品：产品A精选\n用途：季度沟通',91,332,420,181,29,C.ink);
 node(s,'经理观点摘要',68,573,465,76,{size:29});node(s,'产品问答',68,681,465,76,{fill:C.very,size:29});arrow(s,558,449,53);
 doc(s,'基金季度客户沟通稿',654,222,878,570,[['产品信息','产品A精选'],['资料版本','2026年二季度产品资料V1'],['本期观点','甲公司收入增长来自销量提升，后续关注原材料成本'],['风险提示','投资有风险']],{version:'初稿V1',size:26});
 txt(s,'机构标书与咨询工单可复用相同资料',68,785,1464,46,26,C.muted);break;}
case 'review_lanes':{
 txt(s,'基金季度客户沟通稿',68,214,1464,55,31,C.blue,true);
 lane(s,'编写人',298,207);lane(s,'审核人',505,207);
 const a=node(s,'提交初稿V1',300,346,270,101,{size:28});const b=node(s,'按意见修改',869,346,270,101,{size:28});const c=node(s,'提交修订稿',1240,346,264,101,{size:28});
 const r=node(s,'定位问题与依据',478,556,380,103,{fill:C.mint,size:29});const z=node(s,'修订后检查',1128,556,376,103,{fill:C.mint,size:29});connect(s,a,r,{kind:'elbow',from:'bottom',to:'top'});connect(s,r,b,{kind:'elbow',from:'top',to:'bottom'});connect(s,b,c);connect(s,c,z,{from:'bottom',to:'top'});
 txt(s,'检查产品信息、业绩表述、风险提示和文件内容',300,756,1204,55,28,C.ink);break;}
case 'annotated':{
 const q=doc(s,'基金季度客户沟通稿',68,229,760,536,[['产品信息','产品A精选'],['资料版本','2026年二季度产品资料V1'],['本期观点','甲公司收入增长来自销量提升，后续关注原材料成本'],['风险提示','投资有风险']],{version:'初稿V1',highlight:[0,1,3],size:24});
 const cs=[['产品名称','按本期产品文件核对正式名称'],['资料期次','将二季度资料更新为三季度V2'],['风险提示','补齐本期文件中的风险提示']];
 const sy=[405,504,701];
 cs.forEach((v,i)=>{let y=252+i*150;box(s,944,y,588,124,C.very,'none');txt(s,v[0],968,y+15,540,42,25,C.blue,true);txt(s,v[1],968,y+61,540,49,27,C.ink);line(s,828,sy[i],901,sy[i],C.blue,1.8);line(s,901,sy[i],901,y+61,C.blue,1.8);line(s,901,y+61,944,y+61,C.blue,1.8);});
 txt(s,'鹏华：7类71项规则，修改建议采纳率91%',68,791,890,40,25,C.blue,true);txt(s,'盈米：初稿预审、修改、复查',964,791,568,40,25,C.ink);break;}
case 'revision':{
 const w=432,xs=[68,584,1100];
 doc(s,'基金季度客户沟通稿',xs[0],237,w,553,[['产品信息','产品A精选'],['资料版本','2026年二季度产品资料V1'],['本期观点','甲公司收入增长来自销量提升，后续关注原材料成本'],['风险提示','投资有风险']],{version:'初稿V1',highlight:[0,1,3],size:23});
 band(s,'问题清单',xs[1],237,w);['产品名称改为正式全称','资料更新为三季度V2','补充净值波动及本金亏损提示'].forEach((v,i)=>{line(s,xs[1],333+i*136,xs[1]+w,333+i*136,C.line,1);txt(s,v,xs[1]+18,360+i*136,w-36,88,27,C.ink);});
 doc(s,'基金季度客户沟通稿',xs[2],237,w,553,[['产品信息','产品A精选混合型基金'],['资料版本','2026年三季度产品资料V2'],['本期观点','甲公司收入增长来自销量提升，后续关注原材料成本'],['风险提示','基金净值随市场波动，投资本金可能亏损']],{version:'修订稿V2',highlight:[0,1,3],size:23});
 arrow(s,520,458,40);arrow(s,1038,458,40);
 txt(s,'提交即检查',68,803,432,33,24,C.blue,true);txt(s,'意见定位到内容',584,803,432,33,24,C.blue,true);txt(s,'再次检查并保留变更',1100,803,432,33,24,C.blue,true);break;}
case 'risk_flow':{
 const left=['托管邮件','事件消息','系统提示'];const ln=left.map((v,i)=>node(s,v,68,282+i*145,313,88,{fill:C.very,size:28}));
 const a=node(s,'解析风险信息',499,425,328,106,{size:30});const b=node(s,'关联产品与持仓',922,287,610,97,{fill:C.mint,size:30});const c=node(s,'查询规则与资料',922,457,610,97,{fill:C.mint,size:30});const e=node(s,'影响解释与跟进事项',922,627,610,97,{fill:C.pale,size:30});
 ln.forEach(v=>connect(s,v,a,{kind:'elbow'}));connect(s,a,b,{kind:'elbow'});connect(s,b,c,{from:'bottom',to:'top'});connect(s,c,e,{from:'bottom',to:'top'});
 txt(s,'持续跟踪对象：甲公司',68,768,1464,54,29,C.teal,true);break;}
case 'risk_cases':{
 band(s,'汇添富基金  风控工作台与条款问答',68,229,703);band(s,'天弘基金  热门事件助手',829,229,703);
 const a=node(s,'托管行邮件',68,324,703,74,{fill:C.very,size:28});const b=node(s,'风险信息提取',68,457,703,74,{fill:C.pale,size:28});connect(s,a,b,{from:'bottom',to:'top'});
 steps(s,['风控结果','绑定条款','解释依据'],68,625,703,87,{gap:28,size:25,fill:C.mint});
 const r=steps(s,['事件详情','历史事件','产业关系'],829,324,703,87,{gap:28,size:25,fill:C.very});const z=node(s,'综合分析与事件解读',829,625,703,87,{fill:C.pale,size:30});r.forEach(v=>connect(s,v,z,{from:'bottom',to:'top',kind:'elbow'}));
 txt(s,'风险内容与规则原文',68,764,703,54,28,C.blue,true);txt(s,'事件影响的共同讨论材料',829,764,703,54,28,C.blue,true);break;}
case 'risk_proposal':{
 ['原始邮件','持仓数据','规则条款'].forEach((v,i)=>node(s,v,68,286+i*145,285,87,{fill:C.very,size:28}));
 const d1=doc(s,'甲公司  影响分析',493,223,1039,540,[['事件与相关持仓','甲公司被列入评级观察，产品A持有其相关债券'],['规则依据','信用事件跟踪要求及对应条款入口'],['跟进事项','更新发行人分析，汇总相关持仓，向投资经理发送事件说明']],{version:'风险提示处理结果',size:29});
 [329,474,619].forEach(y=>{line(s,353,y,415,y,C.blue,2);line(s,415,y,415,486,C.blue,2);});line(s,415,486,493,486,C.blue,2);
 txt(s,'风险同事直接查出处、核对影响并分派任务',68,787,1464,43,28,C.blue,true);break;}
case 'operations_flow':{
 band(s,'文件输入',68,231,338);band(s,'文件处理',500,231,628);band(s,'交付结果',1222,231,310);
 ['传真与扫描件','客户材料版本','同类电子文件'].forEach((v,i)=>node(s,v,68,326+i*145,338,85,{fill:C.very,size:28}));
 ['字段识别与录入','版本比对','批量修订与保存'].forEach((v,i)=>{node(s,v,500,326+i*145,628,85,{fill:C.pale,size:29});arrow(s,429,361+i*145,50);});
 ['业务记录','差异清单','修订文件'].forEach((v,i)=>{node(s,v,1222,326+i*145,310,85,{fill:C.very,size:28});arrow(s,1151,361+i*145,50);});
 txt(s,'甲公司交易要素与客户沟通稿继续进入后台处理',68,786,1464,45,28,C.blue,true);break;}
case 'operations_cases':{
 band(s,'华安基金  单据智能录入',68,228,703);band(s,'工银瑞信基金  文档比对',829,228,703);
 doc(s,'业务单据',68,310,310,366,[['券名','甲公司债A'],['交易方向','买入'],['业务字段','价格与数量']],{size:23});arrow(s,405,487,40);doc(s,'录入记录',471,310,300,366,[['证券','甲公司债A'],['方向','买入'],['字段','结构化保存']],{size:23});
 doc(s,'基金季度客户沟通稿',829,310,703,446,[['产品名称','V1 产品A精选\nV2 产品A精选混合型基金'],['资料期次','V1 2026年二季度产品资料\nV2 2026年三季度产品资料'],['风险提示','V1 投资有风险\nV2 基金净值随市场波动，投资本金可能亏损']],{version:'初稿V1与修订稿V2的差异',highlight:[0,1,2],size:23});
 txt(s,'华安披露：超80%的柜面传真采用智能录入',68,776,703,48,26,C.blue,true);txt(s,'PDF、Word与扫描件形成可视化差异',829,776,703,48,26,C.ink);break;}
case 'operations_proposal':{
 ['沟通稿V1','修订稿V2','统一更新要求'].forEach((v,i)=>node(s,v,68,276+i*147,310,87,{fill:C.very,size:28}));
 const a=node(s,'识别与字段提取',487,276,415,87,{size:29});const b=node(s,'版本核对与批量修订',487,486,415,107,{size:28});connect(s,a,b,{from:'bottom',to:'top'});
 const o=doc(s,'文件处理交付',1048,232,484,505,[['修订文件','基金季度客户沟通稿V2'],['变更清单','产品名称、资料期次、风险提示'],['处理记录','文件版本、修改位置与核对状态']],{size:25});connect(s,b,o,{kind:'elbow'});line(s,378,320,431,320,C.blue,2);line(s,431,320,487,320,C.blue,2);line(s,431,320,431,614,C.blue,2);line(s,378,466,431,466,C.blue,2);line(s,378,614,431,614,C.blue,2);line(s,431,540,487,540,C.blue,2);
 txt(s,'博时BSBox的批量文件修订，为同类任务集中处理提供参照',68,779,1464,50,27,C.muted);break;}
case 'development_flow':{
 lane(s,'业务同事',262,202);lane(s,'开发同事',464,249);
 const a=node(s,'描述比对需求\n提供两版报告',300,311,320,106,{size:28});const b=node(s,'试用并反馈',1128,311,376,106,{fill:C.mint,size:28});
 const r=steps(s,['整理要求','编写程序','测试与修改','工具与说明'],300,541,1204,99,{gap:52,size:27});connect(s,a,r[0],{from:'bottom',to:'top',kind:'elbow'});connect(s,r[3],b,{from:'top',to:'bottom'});
 connect(s,b,r[1],{from:'bottom',to:'top',color:C.teal,kind:'elbow'});
 txt(s,'报告比对需求形成可以重复使用的工具',300,763,1204,54,30,C.blue,true);break;}
case 'development_cases':{
 band(s,'易方达基金',68,232,703);band(s,'景顺长城基金',829,232,703);
 txt(s,'研发管理流程引入大模型',68,324,703,68,32,C.ink,true);txt(s,'量化团队使用本地模型辅助编程',829,324,703,68,32,C.ink,true);
 steps(s,['需求','开发','测试','交付'],68,466,1464,100,{gap:55,size:30});
 txt(s,'LLM辅助编写程序',435,610,460,55,28,C.blue,true);txt(s,'LLM辅助生成与修订测试',935,610,597,55,28,C.blue,true);
 box(s,68,709,1464,102,C.very,'none');txt(s,'报告比对工具',92,739,285,55,28,C.blue,true);txt(s,'两版文件进入处理程序，输出差异结果与操作说明',393,739,1093,55,28,C.ink);break;}
case 'development_proposal':{
 band(s,'业务侧',68,229,490);band(s,'开发侧',716,229,816);
 const a=node(s,'两版报告与比较要求',68,329,490,104,{fill:C.mint,size:29});const b=node(s,'整理需求与测试样例',716,329,816,104,{size:29});connect(s,a,b);
 const c=node(s,'LLM辅助编程、测试与修改',716,513,816,104,{size:29});connect(s,b,c,{from:'bottom',to:'top'});
 const e=node(s,'差异结果与使用反馈',68,668,490,104,{fill:C.mint,size:29});const f=node(s,'程序、测试样例、操作说明',716,668,816,104,{fill:C.very,size:28});connect(s,c,f,{from:'bottom',to:'top'});connect(s,f,e,{from:'left',to:'right'});
 line(s,313,668,313,480,C.teal,2);line(s,313,480,1000,480,C.teal,2);line(s,1000,480,1000,461,C.teal,2);s.shapes.add({geometry:'upArrow',position:{left:993,top:433,width:14,height:30},fill:C.teal,line:{fill:'none',width:0}});break;}
case 'other':{
 const data=[['内部办事','招商、平安','运营说明与内部政策','按问题检索解释','操作与办事指引'],['邮件安全','永赢','邮件、附件与链接','理解意图并调度检测','风险分级与处置线索'],['经营分析','汇添富\n公开专利提出','产品、渠道与期间问题','取数、计算与归因','原因与行动要点报告']];
 data.forEach((r,i)=>{let y=238+i*184;txt(s,r[0],68,y+7,230,50,31,C.blue,true);txt(s,r[1],68,y+68,230,65,24,C.muted);const a=node(s,r[2],349,y,351,119,{fill:C.very,size:26});const b=node(s,r[3],768,y,351,119,{fill:C.pale,size:26});const c=node(s,r[4],1187,y,345,119,{fill:C.very,size:26});connect(s,a,b);connect(s,b,c);if(i<2)line(s,68,y+151,1532,y+151,C.line,1);});break;}
case 'recommendations':{
 table(s,d.id,['应用','使用者','主要产物','改善的工作'],[['投研分析','研究员、投资经理','公司分析与研究要素','检索、计算与观点比较'],['交易支持','投资经理、交易员','候选券、报价、交易要素','查询、询价与指令准备'],['客户材料','销售、机构业务同事','观点摘要、问答、标书','资料检索与内容组织'],['材料审核','编写人、审核人','问题位置、依据、修改意见','逐项检查与反复修改'],['风险分析','风险、投资同事','影响说明与跟进事项','邮件处理与影响分析'],['运营文件','运营、业务同事','业务记录、差异、修订文件','抄录、核对与批量修改'],['工具开发','业务、开发同事','程序、测试、操作说明','需求整理到工具交付']],68,225,1464,573,[250,300,450,464],25);break;}
case 'cross_lanes':{
 ['前台','中台','后台'].forEach((v,i)=>lane(s,v,262+i*174,174));
 txt(s,'投资研究与业务支持',298,207,570,45,28,C.teal,true);txt(s,'客户材料生成、审核与更新',932,207,600,45,28,C.purple,true);
 const a=node(s,'甲公司研究与交易准备',300,305,540,89,{fill:C.mint,size:28});const b=node(s,'甲公司影响分析',300,479,540,89,{fill:C.mint,size:28});const c=node(s,'交易记录与运营文件',300,653,540,89,{fill:C.mint,size:28});connect(s,a,b,{from:'bottom',to:'top',color:C.teal});connect(s,b,c,{from:'bottom',to:'top',color:C.teal});
 const e=node(s,'基金季度客户沟通稿',932,305,572,89,{fill:C.lav,size:28});const f=node(s,'审核、修改与复查',932,479,572,89,{fill:C.lav,size:28});const g=node(s,'版本比对与材料更新',932,653,572,89,{fill:C.lav,size:28});connect(s,e,f,{from:'bottom',to:'top',color:C.purple});connect(s,f,g,{from:'bottom',to:'top',color:C.purple});
 txt(s,'建议从投研分析与客户材料流程启动',300,790,1204,40,28,C.blue,true);break;}
case 'architecture':{
 const a=node(s,'员工使用入口',455,217,690,74,{fill:C.blue,color:C.white,size:31});const b=node(s,'研究、交易、材料、审核、风险、运营与开发流程',215,357,1170,96,{fill:C.pale,size:31});connect(s,a,b,{from:'bottom',to:'top'});
 const c=node(s,'模型服务\n候选：Qwen、DeepSeek',68,549,420,144,{fill:C.very,size:28});const e=node(s,'资料\n文档、知识库、业务数据',590,549,420,144,{fill:C.very,size:28});const f=node(s,'业务工具\n检索、计算\n查询、文件处理',1112,549,420,144,{fill:C.very,size:27});[c,e,f].forEach(n=>connect(s,b,n,{from:'bottom',to:'top',kind:'elbow'}));
 txt(s,'资料权限、来源与变更记录随工作流程保留',68,768,1464,56,29,C.blue,true);break;}
case 'roadmap':{
 const xs=[68,568,1068],ww=464;const data=[['第一阶段','研究与客户材料应用','投研、销售、合规、IT','任务样例、资料目录、应用初版','形成两条工作流程'],['第二阶段','交易与运营系统接入','交易、运营、IT','查询接口、字段规范、文件流程','复用资料与业务工具'],['第三阶段','工具开发与内部服务','业务部门、开发、支持团队','工具、测试、操作说明、维护机制','扩展更多部门工作']];
 data.forEach((r,i)=>{let x=xs[i];txt(s,r[0],x,220,ww,46,28,C.blue,true);line(s,x,286,x+ww,286,C.blue,5);txt(s,r[1],x,323,ww,96,34,C.ink,true);txt(s,'负责人角色',x,456,ww,40,23,C.muted);txt(s,r[2],x,502,ww,83,27,C.ink);txt(s,'交付物',x,603,ww,40,23,C.muted);txt(s,r[3],x,649,ww,94,27,C.ink);txt(s,r[4],x,779,ww,44,26,C.blue,true);});break;}
case 'evaluation':{
 steps(s,['原工作任务','使用应用','记录结果','调整流程'],68,242,1464,109,{gap:67,size:31});
 const values=[['任务完成时间','完成同一任务的实际用时'],['交付采用情况','输出直接使用与修改情况'],['返工次数','提交后补充与重新处理次数'],['使用频次','同事持续使用的任务与次数']];
 values.forEach((r,i)=>{let x=68+(i%2)*758,y=450+Math.floor(i/2)*133;line(s,x,y,x+706,y,C.line,1.3);txt(s,r[0],x,y+24,285,56,29,C.blue,true);txt(s,r[1],x+299,y+24,407,80,26,C.ink);});
 caption(s,'从投研分析与客户材料两条流程启动，逐步接入更多部门工作',68,761,1464,C.blue,32);break;}
default:throw new Error(d.kind);
}
manifest.push({slide:d.id,title:d.title,kind:d.kind,diagram:d.id>1,shapes:s.shapes.items.length,nativeTables:tableOwners.includes(d.id)});return s;}

const selected=process.env.ONLY_SLIDES?.split(',').map(Number);for(const d of slides){if(selected&&!selected.includes(d.id))continue;buildSlide(d);}
await fs.mkdir(path.join(B,'qa/render'),{recursive:true});
await fs.writeFile(path.join(B,'presentation.json'),JSON.stringify(P.toProto()));
await fs.writeFile(path.join(B,'manifest.json'),JSON.stringify({slides:manifest,tableOwners,diagramSlides:diagrams},null,2));
const render=process.env.RENDER_SLIDES?.split(',').map(Number);
for(const [i,s] of P.slides.items.entries()){
 const id=selected?selected[i]:i+1;if(render&&!render.includes(id))continue;
 const png=await P.export({slide:s,format:'png',scale:1});await fs.writeFile(path.join(B,`qa/render/slide-${String(id).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
 console.log(`Rendered slide ${id}`);
}
await(await PresentationFile.exportPptx(P)).save(path.join(B,selected?'sample.pptx':'candidate.pptx'));
console.log(`Built ${P.slides.items.length} editable slides.`);
