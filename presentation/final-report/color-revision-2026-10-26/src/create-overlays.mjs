import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const {Presentation,PresentationFile}=await import('/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs');
const R=path.dirname(path.dirname(fileURLToPath(import.meta.url))),B=path.join(R,'build'),F='PingFang SC';
const plan=JSON.parse(await fs.readFile(path.join(R,'src/color-map.json'),'utf8'));
const p=Presentation.create({slideSize:{width:1600,height:900}});p.theme.defaultFont=F;
function rect(s,name,x,y,w,h,color){s.shapes.add({name,geometry:'rect',position:{left:x,top:y,width:w,height:h},fill:'#'+color,line:{fill:'none',width:0}});}
function text(s,name,value,x,y,w,h,size,color,bold=false){const q=s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});q.text=value;q.text.style={typeface:F,fontSize:size,color:'#'+color,bold,alignment:'left',verticalAlignment:'top',autoFit:'none',wrap:'square',insets:0};q.text.insets=0;}
for(const d of plan.slides){const s=p.slides.add();
 if(d.header.length===2){for(const [j,h] of d.header.entries()){const x=j===0?1204:1312,c=plan.colors[h.kind];rect(s,`!!story.header.${h.kind}.bar`,x,131,5,25,c);text(s,`!!story.header.${h.kind}.name`,h.name,x+14,125,j===0?80:134,35,22,c,true);}}
 else if(d.header.length===1){const h=d.header[0],c=h.kind==='neutral'?plan.colors.muted:plan.colors[h.kind],w=h.kind==='issuer'?110:140,qx=h.kind==='issuer'?1330:1366;rect(s,`!!story.header.${h.kind}.bar`,1204,132,5,25,c);text(s,`!!story.header.${h.kind}.name`,h.name,1218,125,w,36,24,c,true);if(h.qualifier)text(s,`!!story.header.${h.kind}.qualifier`,h.qualifier,qx,130,1460-qx,31,20,plan.colors.muted);}
 for(const o of d.overlays){if(o.type==='bar')rect(s,o.name,o.x,o.y,o.w,o.h,o.color);else text(s,o.name,o.text,o.x,o.y,o.w,o.h,o.size,o.color,true);}
}
await(await PresentationFile.exportPptx(p)).save(path.join(B,'overlays.pptx'));
console.log('Created native overlay objects for 33 pages');
