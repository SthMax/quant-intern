import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const B=path.dirname(fileURLToPath(import.meta.url)),R=path.dirname(B);
const S='/Users/sthmax/.codex/plugins/cache/openai-primary-runtime/presentations/26.1020.11348/skills/presentations';
process.env.RUNTIME_NODE_MODULES='/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const {finalizePresentation}=await import(pathToFileURL(path.join(S,'container_tools/artifact_tool_utils.mjs')).href);
const spec=JSON.parse(await fs.readFile(path.join(B,'manifest.json'),'utf8'));
const result=await finalizePresentation({
 workspaceDir:R,candidatePath:path.join(B,'candidate.pptx'),finalPath:path.join(R,'output/asset-management-llm-workflows.pptx'),
 pythonExecutable:'/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',
 integrityValidatorPath:path.join(S,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(S,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','15240000,8572500','--validate-bullet-geometry','--validate-heading-fit',...spec.tableOwners.flatMap(n=>['--require-native-table-slide',String(n)])],
 explicitTotalSlideCount:33,requiredNativeTableOwnerSlides:spec.tableOwners,requiredNativeChartOwnerSlides:[],
 fontPolicy:{basis:'design',families:['PingFang SC']},verifyArtifactToolImport:true,
 receiptPath:path.join(B,'qa/finalizer.json')
});
console.log(JSON.stringify({path:result.finalPath,sha256:result.finalSha256,layoutWarnings:result.presentationLayout?.warnings},null,2));
