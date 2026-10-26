import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const skill='/Users/sthmax/.codex/plugins/cache/openai-primary-runtime/presentations/26.1020.11348/skills/presentations';
const runtime='/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies';
process.env.RUNTIME_NODE_MODULES=path.join(runtime,'node/node_modules');
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
await fs.mkdir(path.join(root,'output'),{recursive:true});
const result=await finalizePresentation({
 workspaceDir:root,
 candidatePath:path.join(root,'build/candidate.pptx'),
 finalPath:path.join(root,'output/asset-management-llm-interactive-en.pptx'),
 pythonExecutable:path.join(runtime,'python/bin/python3'),
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','15240000,8572500','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide','11'],
 explicitTotalSlideCount:33,
 requiredNativeTableOwnerSlides:[11],
 requiredNativeChartOwnerSlides:[],
 fontPolicy:{basis:'design',families:['Arial']},
 verifyArtifactToolImport:true,
 receiptPath:path.join(root,'build/qa/finalizer-english.json')
});
console.log(JSON.stringify({path:result.finalPath,sha256:result.finalSha256,package:result.packageIntegrity.status,warnings:result.presentationLayout.warnings},null,2));
