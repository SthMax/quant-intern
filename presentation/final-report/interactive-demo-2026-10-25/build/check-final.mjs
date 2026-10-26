import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import crypto from 'node:crypto';
import {FileBlob,PresentationFile} from '@oai/artifact-tool';
const B=path.dirname(fileURLToPath(import.meta.url)),R=path.dirname(B);
const finalPath=path.join(R,'output/interactive-company-workflow-demo.pptx');
const hash=async()=>crypto.createHash('sha256').update(await fs.readFile(finalPath)).digest('hex');
const before=await hash();
const P=await PresentationFile.importPptx(await FileBlob.load(finalPath));
await fs.mkdir(path.join(B,'qa/final-render'),{recursive:true});
for(const [i,s] of P.slides.items.entries()){
 const b=await P.export({slide:s,format:'png',scale:1});
 await fs.writeFile(path.join(B,`qa/final-render/state-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await b.arrayBuffer()));
 console.log(`Rendered final state ${i+1}/9`);
}
const after=await hash();
if(before!==after)throw new Error('Final file hash changed during read-only check');
await fs.writeFile(path.join(B,'qa/final-reimport.json'),JSON.stringify({slides:P.slides.items.length,beforeSha256:before,afterSha256:after,fileUnchanged:before===after},null,2));
console.log(`Reimported ${P.slides.items.length} slides; final file unchanged.`);
