import fs from 'node:fs/promises';
import {sources,slides} from './content.mjs';
await fs.writeFile(new URL('./content.mjs',import.meta.url),'export const sources='+JSON.stringify(sources,null,2)+';\nexport const slides='+JSON.stringify(slides,null,2)+';\n');
await fs.writeFile(new URL('./speaker-notes.md',import.meta.url),'# 逐页讲述与来源\n\n'+slides.map(d=>'## '+String(d.id).padStart(2,'0')+' '+d.title+'\n\n'+d.notes+'\n\n'+d.refs.map(([k,loc])=>sources[k].short+'，'+loc+'\n'+sources[k].url).join('\n\n')).join('\n\n'));
