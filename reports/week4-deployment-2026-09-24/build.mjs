/** Export canonical scenario Markdown as readable A4 PDFs, preserving content. */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';
const root = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(root, '../..');
const deps = process.env.WORKSPACE_NODE_MODULES || path.join(os.homedir(), '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules');
const { marked } = await import(pathToFileURL(path.join(deps, 'marked/lib/marked.esm.js')));
const { chromium } = await import(pathToFileURL(path.join(deps, 'playwright/index.mjs')));
const out = path.join(root,'output/pdf');
const build = path.join(root,'build');
fs.mkdirSync(out,{recursive:true});fs.mkdirSync(build,{recursive:true});
const css = fs.readFileSync(path.join(root,'report.css'),'utf8');
const specs = [
 ['scenario-1-personal-agent-2026-09-24.md','scenario-1-personal-agent.pdf','个人与小组'],
 ['scenario-2-enterprise-rag-2026-09-23.md','scenario-2-enterprise-rag.pdf','公司知识库与RAG'],
 ['scenario-3-company-agent-2026-09-23.md','scenario-3-company-agent.pdf','公司通用Agent'],
];
const esc = s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const sha = p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const mappings = Object.fromEntries(specs.map(([s,o])=>[path.join(repo,'knowledge-base/infrastructure',s),o]));

function diagram(src) {
 const nodes={};for(const m of src.matchAll(/(\w+)\["([^"]+)"\]/g))nodes[m[1]]=m[2];
 const edges=[];for(const l of src.split('\n')){
  const x=l.replace(/\["[^"]+"\]/g,'');const m=x.match(/(\w+)\s*(<-->|-->)\s*(\w+)/);
  if(m)edges.push({a:m[1],b:m[3],both:m[2]==='<-->'});
 }
 let boxes,routes,w,h;
 if(nodes.ONYX){
  w=550;h=320;boxes={NAS:[10,10,220,52],ADAPTER:[300,10,230,52],USER:[10,97,220,52],ONYX:[300,97,230,62],MODEL:[300,193,230,52],RESULT:[300,276,230,52]};h=342;
  routes={'NAS-ADAPTER':'M230 36H300','ADAPTER-ONYX':'M415 62V97','USER-ONYX':'M230 123H300','ONYX-MODEL':'M415 159V193','MODEL-RESULT':'M415 245V276'};
 }else if(nodes.IDX){
  w=710;h=350;boxes={NAS:[10,10,210,62],INGEST:[250,10,210,62],IDX:[490,10,210,62],AUTH:[10,142,210,62],API:[250,142,210,62],RANK:[490,142,210,62],MODEL:[490,274,210,62],UI:[250,274,210,62]};
  routes={'NAS-INGEST':'M220 41H250','INGEST-IDX':'M460 41H490','NAS-AUTH':'M115 72V142','AUTH-API':'M220 173H250','UI-API':'M355 274V204','API-IDX':'M355 142V106H595V72','API-RANK':'M460 173H490','RANK-MODEL':'M595 204V274','MODEL-UI':'M490 305H460'};
 }else{
  w=800;h=478;boxes={U:[30,10,200,60],G:[300,10,220,60],H:[300,125,220,70],L:[550,125,220,70],K:[30,125,200,70],M:[160,255,220,65],N:[160,370,220,65],X:[470,255,240,65],O:[470,370,240,65]};
  routes={'U-G':'M230 40H300','G-H':'M410 70V125','H-L':'M520 160H550','H-K':'M300 160H230','H-M':'M370 195V226H270V255','M-N':'M270 320V370','H-X':'M450 195V226H590V255','X-O':'M590 320V370','O-U':'M710 403H789V462H10V40H30'};
 }
 const arrow='<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#008b83"/></marker></defs>';
 let body=arrow;
 for(const e of edges){const route=routes[e.a+'-'+e.b];if(!route)throw Error('Missing diagram route '+e.a+'-'+e.b);body+=`<path d="${route}" stroke="#008b83" fill="none" stroke-width="1.8" marker-end="url(#arrow)" ${e.both?'marker-start="url(#arrow)"':''}/>`;}
 for(const [id,label] of Object.entries(nodes)){
  const [x,y,bw,bh]=boxes[id];
  const lines=[];let line='',len=0;const limit=bw>225?23:21;
  for(const c of label){let cw=c.codePointAt(0)>255?2:1;if(len+cw>limit){lines.push(line);line='';len=0;}line+=c;len+=cw;}if(line)lines.push(line);
  const balanced={ONYX:['Onyx Enterprise：','解析、索引、权限检索'],G:['身份、任务队列、','配额与状态'],H:['独立Hermes实例：','计划、工具循环、会话'],L:['共享LLM服务：','模型与请求调度'],X:['隔离工具环境：','文档、计算、文件生成'],O:['产物、检查结果','与任务记录']};
  if(balanced[id] && balanced[id].join('')===label)lines.splice(0,lines.length,...balanced[id]);
  const fontsize=w<600?17:16;
  body+=`<rect x="${x}" y="${y}" width="${bw}" height="${bh}" fill="#f0f6f8" stroke="#c9d8e0"/><text x="${x+bw/2}" y="${y+bh/2-(lines.length-1)*10+5}" text-anchor="middle" font-family="PingFang SC, sans-serif" font-size="${fontsize}" fill="#17334d">`;
  body+=lines.map((l,i)=>`<tspan x="${x+bw/2}" dy="${i?20:0}">${esc(l)}</tspan>`).join('')+'</text>';
 }
 return `<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" role="img">${body}</svg><figcaption>资料、身份、模型与工具之间的数据流；双向箭头表示请求与返回。</figcaption></figure>`;
}

const executable = fs.existsSync(chromium.executablePath())?chromium.executablePath():'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const browser=await chromium.launch({headless:true,executablePath:executable});
const manifest={as_of:'2026-09-24',renderer:'marked / headless Chromium; vector architecture diagrams',documents:[]};
try{
 for(const [i,[filename,output,label]] of specs.entries()){
  const source=path.join(repo,'knowledge-base/infrastructure',filename);
  const md=fs.readFileSync(source,'utf8');
  const title=md.split('\n')[0].replace(/^# /,'');
  const converted=md.replace(/```mermaid\n([\s\S]*?)```/g,(_,code)=>diagram(code));
  // Honor explicitly paired Chinese emphasis even beside punctuation.
  const emphasized=converted.replace(/\*\*([^*\n]+)\*\*/g,(_,inner)=>'<strong>'+marked.parseInline(inner)+'</strong>');
  const content=marked.parse(emphasized,{gfm:true});
  const html=`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>${esc(title)}</title><style>${css}</style></head><body><div class="kicker">第四周部署研究 · SCENARIO ${i+1}</div><main>${content}</main><p class="source-note">文档整理：2026年9月24日。金额、精度与性能口径按正文；来源链接及完整计算数据随项目知识库保存。</p></body></html>`;
  const page=await browser.newPage({viewport:{width:794,height:1123}});
  await page.setContent(html,{waitUntil:'load'});
  await page.evaluate(({source,out,mappings,repo})=>{
   const canonical=u=>u.replace(/\\/g,'/');
   for(const table of document.querySelectorAll('table')){
    const rows=[...table.rows];const n=rows[0].cells.length;if(n>=6)table.classList.add('wide');
    const scores=Array.from({length:n},(_,j)=>{
     const strings=rows.map(r=>r.cells[j]?.textContent.trim()||'');
     const numeric=strings.slice(1).filter(x=>/^[\d\s.,，%％+＋\-–—/／×≈＝:：()（）GBKMT万元秒token/s]*$/.test(x)).length>=(strings.length-1)*.7;
     if(numeric&&j>0)return 4.5;
     const lengths=strings.map(x=>[...x].reduce((a,c)=>a+(c.charCodeAt(0)>255?2:1),0)).sort((a,b)=>a-b);
     return Math.max(j===0?6:5,Math.min(12,Math.sqrt(lengths[Math.floor(lengths.length*.8)]||20)));
    });
    const total=scores.reduce((a,b)=>a+b,0);const cg=document.createElement('colgroup');
    for(const score of scores){const col=document.createElement('col');col.style.width=(score/total*100)+'%';cg.appendChild(col);}table.prepend(cg);
    if(table.getBoundingClientRect().height<280)table.classList.add('keep');
   }
   for(const link of document.querySelectorAll('a[href]')){
    const href=link.getAttribute('href');if(/^(https?:|mailto:|#)/.test(href))continue;
    const resolved=new URL(href,'file://'+source).pathname;
    if(mappings[canonical(resolved)]) link.setAttribute('href','https://pdf-local.invalid/'+mappings[canonical(resolved)]);
    else link.setAttribute('href','https://repo-local.invalid/'+canonical(resolved).slice(canonical(repo).length+1));
   }
  },{source,out,mappings,repo});
  await page.evaluate(()=>document.fonts.ready);
  if(i===2) await page.evaluate(()=>{ const headings=[...document.querySelectorAll('h2')];headings.at(-1).style.breakBefore='page'; });
  const overflow=await page.evaluate(()=>[...document.querySelectorAll('table,pre,figure')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>({tag:e.tagName,width:e.clientWidth,scroll:e.scrollWidth,text:e.textContent.slice(0,80)})));
  if(overflow.length)throw Error(JSON.stringify(overflow));
  const finalhtml=await page.content();fs.writeFileSync(path.join(build,output.replace('.pdf','.html')),finalhtml);
  await page.pdf({path:path.join(out,output),format:'A4',preferCSSPageSize:true,printBackground:true,displayHeaderFooter:true,
   headerTemplate:'<div></div>', footerTemplate:`<div style="width:100%;padding:0 17mm;font:8px Arial;color:#647784;display:flex;justify-content:space-between"><span>WEEK 4 / SCENARIO ${i+1} · 24 SEP 2026</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
   margin:{top:'18mm',bottom:'19mm',left:'17mm',right:'17mm'},tagged:true,outline:true});
  manifest.documents.push({scenario:i+1,title,source:path.relative(repo,source),source_sha256:sha(source),output:path.relative(root,path.join(out,output)),tables:(md.match(/^\|[- :|]+\|$/gm)||[]).length,diagrams:(md.match(/```mermaid/g)||[]).length,html_sha256:sha(path.join(build,output.replace('.pdf','.html')))});
  console.log('Exported',output);await page.close();
 }
}finally{await browser.close();}
fs.writeFileSync(path.join(root,'qa/source-manifest.json'),JSON.stringify(manifest,null,2)+'\n');
