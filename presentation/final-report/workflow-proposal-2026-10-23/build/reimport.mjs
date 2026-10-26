import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {FileBlob,PresentationFile} from '@oai/artifact-tool';
const B=path.dirname(fileURLToPath(import.meta.url)),R=path.dirname(B);
const P=await PresentationFile.importPptx(await FileBlob.load(path.join(R,'output/asset-management-llm-workflows.pptx')));
await fs.mkdir(path.join(B,'qa/final-render'),{recursive:true});
for(const [i,s] of P.slides.items.entries()){
 const blob=await P.export({slide:s,format:'png',scale:1});
 await fs.writeFile(path.join(B,`qa/final-render/slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
}
const inspect=await P.inspect({kind:'slide,textbox,shape,table,chart,notes',maxChars:1000000});
await fs.writeFile(path.join(B,'qa/reimport.ndjson'),inspect.ndjson);
await fs.writeFile(path.join(B,'qa/reimport.json'),JSON.stringify({slides:P.slides.items.length},null,2));
console.log(`Reimported and rendered ${P.slides.items.length} slides.`);
