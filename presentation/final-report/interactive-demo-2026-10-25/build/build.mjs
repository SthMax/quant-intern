import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Presentation,PresentationFile} from '@oai/artifact-tool';
import {states,material,citations} from '../src/states.mjs';
const B=path.dirname(fileURLToPath(import.meta.url)),R=path.dirname(B);
const F='PingFang SC',C={blue:'#005A9C',ink:'#20262C',muted:'#707C88',line:'#BCC6CF',pale:'#D9EAF7',very:'#F3F7FA',white:'#FFFFFF',mark:'#FFF0BE',teal:'#317F7B',mint:'#DCEFEA',purple:'#7363A6'};
const P=Presentation.create({slideSize:{width:1600,height:900}});P.theme.defaultFont=F;
P.theme.colorScheme={name:'Business workflow',themeColors:{accent1:C.blue,accent2:C.teal,accent3:C.purple,accent4:'#967335',accent5:'#AD5247',accent6:C.muted,bg1:C.white,bg2:C.very,tx1:C.ink,tx2:C.muted,dk1:C.ink,dk2:C.blue,lt1:C.white,lt2:C.pale,hlink:C.blue,folHlink:C.purple}};
const manifest=[];
function rect(s,name,x,y,w,h,fill=C.white,stroke='none',lw=1){return s.shapes.add({name,geometry:'rect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:stroke,width:stroke==='none'?0:lw,style:'solid'}});}
function txt(s,name,value,x,y,w,h=50,size=28,color=C.ink,bold=false,align='left'){
 const q=s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});q.text=value;q.text.style={typeface:F,fontSize:size,color,bold,alignment:align,verticalAlignment:'top',autoFit:'none',wrap:'square',insets:0};q.text.insets=0;return q;
}
function button(s,name,value,x,y,w,h,{fill=C.very,color=C.blue,size=25,stroke='none'}={}){const q=rect(s,name,x,y,w,h,fill,stroke);q.text=value;q.text.style={typeface:F,fontSize:size,color,bold:true,alignment:'center',verticalAlignment:'middle',autoFit:'none',wrap:'square',insets:0};q.text.insets=0;return q;}
function line(s,name,x1,y1,x2,y2,color=C.line,width=1.5){return s.shapes.add({name,geometry:'line',position:{left:Math.min(x1,x2),top:Math.min(y1,y2),width:Math.abs(x2-x1)||.1,height:Math.abs(y2-y1)||.1,horizontalFlip:x2<x1,verticalFlip:y2<y1},fill:'none',line:{fill:color,width,style:'solid'}});}
function arrow(s,name,x1,y1,x2,y2,color=C.blue){return s.shapes.add({name,geometry:'connector',kind:'straight',position:{left:x1,top:y1,width:x2-x1,height:y2-y1},line:{fill:color,width:2,style:'solid'},tail:{type:'triangle',width:'sm',length:'sm'}});}
const offices=[{key:'front',title:'前台',tasks:[['research','研究分析'],['trade','交易支持'],['client','客户材料']],route:'client'},{key:'middle',title:'中台',tasks:[['review','材料审核'],['risk','风险分析']],route:'review'},{key:'back',title:'后台',tasks:[['files','运营文件'],['dev','工具开发']],route:'files'}];
function map(s,d){const full=d.page===1||d.page===9;
 offices.forEach((o,i)=>{
  const x=full?68+i*500:68,y=full?238:216+i*173,w=full?464:280,h=full?410:158,headH=full?58:43;
  const active=d.active==='all'||d.active===o.key;
  rect(s,`!!map.${o.key}`,x,y,w,h,C.very,C.line,1);
  button(s,`nav.${o.key}`,o.title,x,y,w,headH,{fill:active?C.blue:C.pale,color:active?C.white:C.blue,size:full?33:27});
  const taskY=full?y+103:y+56,step=full?91:32,ts=full?31:22;
  o.tasks.forEach(([k,v],j)=>{
   const selected=k===o.route&&(active||full),ty=taskY+j*step;
   if(selected)rect(s,`!!task.${k}.highlight`,x+(full?20:12),ty-(full?11:3),w-(full?40:24),full?65:32,active?C.pale:'#E9EDF0');
   txt(s,`!!task.${k}`,v,x+(full?42:25),ty,w-(full?84:50),full?47:31,ts,selected?C.blue:C.muted,selected);
  });
  if(full&&d.page===9){
   const captions=['沟通稿 V1','修订稿 V2','更新稿与变更清单'];
   txt(s,`!!map.${o.key}.outcome`,captions[i],x+24,y+334,w-48,52,27,C.teal,true,'center');
  }
 });
 if(full){
  arrow(s,'!!route.front-middle',532,470,568,470,d.page===9?C.teal:C.line);
  arrow(s,'!!route.middle-back',1032,470,1068,470,d.page===9?C.teal:C.line);
  txt(s,'!!map.route.caption',d.page===9?'生成材料、审核修改、比对更新，交付物沿流程复用':'本次演示：客户材料生成、审核与更新',68,700,1464,62,32,C.blue,true);
 }else line(s,'!!map.separator',384,216,384,741,C.line,1);
}
function common(s,d){s.background.fill=C.white;txt(s,'!!heading',d.title,68,44,1464,70,44,C.ink,true);txt(s,'!!subtitle','一份客户材料的工作过程',68,125,1464,40,27,C.muted);line(s,'!!heading.rule',68,186,1532,186,C.line,1.2);map(s,d);
 if(d.page!==1&&d.page!==9){txt(s,'!!focus',d.focus,434,213,1038,55,35,C.blue,true);txt(s,'!!example','示例',1472,218,60,32,20,C.muted,false,'right');}
 button(s,'nav.home','公司总图',68,784,280,49,{fill:C.white,color:C.blue,stroke:C.line,size:24});
 txt(s,'!!state.number',`${d.page} / 9`,1174,795,93,36,22,C.muted,false,'right');
 button(s,'nav.prev','上一步',1290,784,110,49,{fill:C.very,color:C.blue,size:23});
 button(s,'nav.next',d.page===9?'重新演示':'下一步',1418,784,114,49,{fill:C.blue,color:C.white,size:23});
 line(s,'!!footer.rule',68,853,1532,853,C.line,1);
 const refs=d.source.map(k=>({front:'天弘基金',middle:'鹏华基金、盈米基金销售',back:'工银瑞信基金'}[k]));
 txt(s,'!!footer.source','方案参考：'+refs.join('；'),68,866,1350,24,14,C.muted);
 s.speakerNotes.text=d.notes+'\n\n来源：\n'+d.source.map(k=>citations[k]).join('\n\n');
}
function input(s,key,title,body,x,y,w,h,size=26){return button(s,`!!input.${key}`,title+'\n'+body,x,y,w,h,{fill:C.very,color:C.ink,size,stroke:C.line});}
function doc(s,v,x,y,w,h,{suffix='',mark=[],revised=false,compact=false}={}){
 const prefix='!!clientDoc'+suffix;
 rect(s,prefix,x,y,w,h,C.white,C.line,1.4);txt(s,prefix+'.title',material.title,x+24,y+20,w-104,45,compact?27:29,C.ink,true);txt(s,prefix+'.version',v.version,x+w-71,y+23,47,34,22,C.blue,true,'right');line(s,prefix+'.rule',x+24,y+78,x+w-24,y+78,C.line,1);
 const data=[['product','产品名称',v.product],['period','资料期次',v.period],['view','本期观点',v.view],['risk','风险提示',v.risk]];
 if(compact){
  const ys=[y+101,y+181,y+268,y+378],hs=[70,78,103,96];
  data.forEach(([k,l,val],i)=>{const yy=ys[i];rect(s,prefix+'.highlight.'+k,x+17,yy-6,w-34,hs[i],mark.includes(k)?(revised?C.mint:C.mark):'none');txt(s,prefix+'.label.'+k,l,x+26,yy,w-52,32,21,C.blue,true);txt(s,prefix+'.value.'+k,val,x+26,yy+33,w-52,hs[i]-32,22,C.ink);});
 }else{
  const ys=[y+103,y+165,y+227,y+334],hs=[49,49,91,77];
  data.forEach(([k,l,val],i)=>{const yy=ys[i];rect(s,prefix+'.highlight.'+k,x+169,yy-5,w-193,hs[i],mark.includes(k)?(revised?C.mint:C.mark):'none');txt(s,prefix+'.label.'+k,l,x+24,yy,132,36,22,C.blue,true);txt(s,prefix+'.value.'+k,val,x+178,yy,w-202,hs[i],24,C.ink);});
 }
}
function content(s,d){switch(d.page){
 case 1:break;
 case 2:{
  input(s,'customer','客户问题','本期关注什么？',434,307,482,105,27);
  input(s,'manager','经理观点','甲公司收入与成本变化',434,448,482,105,27);
  input(s,'product','产品资料','产品A精选、二季度 V1',434,589,482,105,27);
  line(s,'!!input.join1',916,360,968,360,C.blue,2);line(s,'!!input.join2',916,501,968,501,C.blue,2);line(s,'!!input.join3',916,642,968,642,C.blue,2);line(s,'!!input.bus',968,360,968,642,C.blue,2);arrow(s,'!!input.toTask',968,501,1044,501);
  button(s,'!!task.brief','季度客户沟通稿\n产品A精选',1044,410,488,182,{fill:C.pale,color:C.blue,size:32});
  txt(s,'!!task.use','用途：季度客户沟通',1044,632,488,48,27,C.muted);break;}
 case 3:{
  input(s,'customer','客户问题','本期关注什么？',434,306,230,100,22);
  input(s,'manager','经理观点','收入与成本',434,465,230,100,22);
  input(s,'product','产品资料','产品A精选\n二季度 V1',434,624,230,110,22);
  line(s,'!!input.join1',664,356,700,356,C.blue,2);line(s,'!!input.join2',664,515,700,515,C.blue,2);line(s,'!!input.join3',664,679,700,679,C.blue,2);line(s,'!!input.bus',700,356,700,679,C.blue,2);arrow(s,'!!input.toLLM',700,515,750,515);
  button(s,'!!llm','LLM\n整理与撰写',750,441,202,148,{fill:C.pale,color:C.blue,size:29});arrow(s,'!!llm.toDoc',952,515,1008,515);
  doc(s,material.v1,1008,279,524,491,{compact:true});break;}
 case 4:{
  doc(s,material.v1,434,292,720,430);
  txt(s,'!!review.heading','逐项检查',1212,324,320,49,31,C.blue,true);
  ['产品名称','资料期次','风险提示'].forEach((v,i)=>{line(s,'!!review.check.rule.'+i,1212,395+i*105,1532,395+i*105,C.line,1);txt(s,'!!review.check.'+i,v,1212,421+i*105,320,54,28,C.ink);});
  arrow(s,'!!doc.toReview',1154,506,1195,506);break;}
 case 5:{
  doc(s,material.v1,434,292,720,430,{mark:['product','period','risk']});
  const comments=[['product','正式产品名称','补充“混合型基金”',395,326],['period','本期资料','改用三季度产品资料 V2',457,475],['risk','产品风险说明','补充净值波动与本金亏损',654,624]];
  comments.forEach(([k,a,b,sy,cy])=>{rect(s,'!!comment.'+k,1212,cy,320,112,C.very);txt(s,'!!comment.'+k+'.title',a,1230,cy+13,284,35,23,C.blue,true);txt(s,'!!comment.'+k+'.body',b,1230,cy+53,284,57,23,C.ink);line(s,'!!comment.'+k+'.lead1',1154,sy,1180,sy,C.blue,1.6);line(s,'!!comment.'+k+'.lead2',1180,sy,1180,cy+56,C.blue,1.6);line(s,'!!comment.'+k+'.lead3',1180,cy+56,1212,cy+56,C.blue,1.6);});break;}
 case 6:{
  doc(s,material.v2,434,292,720,430,{mark:['product','period','risk'],revised:true});
  button(s,'!!review.result','修订后检查',1212,326,320,69,{fill:C.mint,color:C.teal,size:27});
  ['名称与资料对应','使用三季度资料','风险提示已更新'].forEach((v,i)=>txt(s,'!!review.result.'+i,v,1212,443+i*91,320,66,25,C.ink));
  txt(s,'!!review.version','客户沟通稿 V2',1212,706,320,43,26,C.teal,true);break;}
 case 7:{
  doc(s,material.v1,434,279,524,491,{suffix:'.v1',mark:['product','period','risk'],compact:true});
  doc(s,material.v2,1008,279,524,491,{mark:['product','period','risk'],revised:true,compact:true});
  arrow(s,'!!compare',963,514,1000,514);break;}
 case 8:{
  rect(s,'!!changeLog',434,279,524,491,C.very,C.line,1);
  txt(s,'!!changeLog.title','变更清单',458,299,476,49,29,C.blue,true);line(s,'!!changeLog.rule',458,357,934,357,C.line,1);
  const changes=[['product','产品名称','补充正式产品全称',389],['period','资料期次','二季度 V1 更新为三季度 V2',498],['risk','风险提示','补充净值波动与本金亏损',607]];
  changes.forEach(([k,a,b,y])=>{txt(s,'!!changeLog.'+k+'.label',a,458,y,476,35,23,C.blue,true);txt(s,'!!changeLog.'+k+'.body',b,458,y+40,476,64,25,C.ink);});
  doc(s,material.v2,1008,279,524,491,{revised:true,compact:true});break;}
 case 9:break;
}}
for(const d of states){const s=P.slides.add();common(s,d);content(s,d);manifest.push({page:d.page,title:d.focus,seconds:d.seconds,nativeShapeCount:s.shapes.items.length,shapeNames:s.shapes.items.map(q=>q.name)});}
await fs.mkdir(path.join(B,'qa/render'),{recursive:true});
await fs.writeFile(path.join(B,'presentation.json'),JSON.stringify(P.toProto()));
await fs.writeFile(path.join(B,'manifest.json'),JSON.stringify({slideCount:9,estimatedSeconds:states.reduce((a,b)=>a+b.seconds,0),slides:manifest},null,2));
const navigation={slideCount:9,objectMatching:'Stable shape names prefixed with !! for persistent business objects. Navigation is one native shape with internal text.',slides:states.map(d=>({page:d.page,buttons:{'nav.front':2,'nav.middle':4,'nav.back':7,'nav.home':1,'nav.prev':Math.max(1,d.page-1),'nav.next':d.page===9?1:d.page+1}}))};
await fs.writeFile(path.join(R,'src/navigation-map.json'),JSON.stringify(navigation,null,2));
const selected=process.env.RENDER_PAGES?.split(',').map(Number);
for(const [i,s] of P.slides.items.entries()){if(selected&&!selected.includes(i+1))continue;const b=await P.export({slide:s,format:'png',scale:1});await fs.writeFile(path.join(B,`qa/render/state-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await b.arrayBuffer()));console.log(`Rendered ${i+1}/9`);}
await(await PresentationFile.exportPptx(P)).save(path.join(B,'base.pptx'));
console.log('Built base.pptx with nine states.');
