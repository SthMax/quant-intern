import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const spec=JSON.parse(await fs.readFile(path.resolve(root,'../corporate-template-2026-10-27/layout-spec.json'),'utf8'));
const skill='/Users/sthmax/.codex/plugins/cache/openai-primary-runtime/presentations/26.1020.11348/skills/presentations';
const runtime='/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies';
process.env.RUNTIME_NODE_MODULES=path.join(runtime,'node/node_modules');
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const finalPath=path.resolve(root,process.argv[2]||'output/asset-management-llm-streamlined-en.pptx');
await fs.mkdir(path.dirname(finalPath),{recursive:true});
const receiptPath=path.join(root,'build/qa',path.basename(finalPath)+'.validation.json');
const r=await finalizePresentation({workspaceDir:root,candidatePath:path.join(root,'build/candidate.pptx'),finalPath,
 pythonExecutable:path.join(runtime,'python/bin/python3'),
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu',`${spec.slide.width_emu},${spec.slide.height_emu}`,'--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide','10'],
 explicitTotalSlideCount:28,requiredNativeTableOwnerSlides:[10],requiredNativeChartOwnerSlides:[],fontPolicy:{basis:'reference',families:['Arial'],referencePath:path.resolve(root,'../visual-workflows-2026-10-28/output/asset-management-llm-visual-en.pptx'),referenceSha256:'1dae3a54c474190f1ca41ddbbd1a923d61929df714f861828547a59ddd39a2e4'},verifyArtifactToolImport:true,
 receiptPath});
await fs.copyFile(receiptPath,path.join(root,'build/qa/finalizer.json'));
console.log(JSON.stringify({path:r.finalPath,sha256:r.finalSha256,integrity:r.packageIntegrity.status,warnings:r.presentationLayout.warnings},null,2));
