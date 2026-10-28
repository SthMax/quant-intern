# Delivery

Final editable PowerPoint: `output/asset-management-llm-visual-en.pptx`.

SHA256: `1dae3a54c474190f1ca41ddbbd1a923d61929df714f861828547a59ddd39a2e4`.

The 33-slide English edition uses native diagrams, text, connectors and the native bond table on page 11. Its short on-screen evidence and labels support the spoken explanation in the embedded notes. The notes retain relevant full passages, factual context, source URLs and the cover-image credit. The three-office/seven-task map provides static task orientation. All prior editions remain intact.

The exact canvas is 25.40 × 14.28 cm. Main titles use 24 pt bold at y2.00 cm and subtitles use 16 pt blue at y3.00 cm. These point sizes are agreed design choices. The measured body limits and company brand/footer clearance remain authoritative. The deck contains no animations, transitions, slide-jump actions, navigation controls, page counters or detached example tags. Meaningful object names support later manual animation.

## Review and validation

The author inspected all 33 pages. The independent reviewer inspected all 33 pages and their embedded spoken notes, discussed page mechanisms in `PAGE-DISCUSSION.md`, and passed the targeted repairs. `FINAL-REVIEW.md` records no remaining reviewer findings against the exact final hash. The final fresh-process renders are in `build/qa/final-render/`, with input and PNG hashes in `render-manifest.json`; `build/qa/render-reconciliation.json` verifies all 33 images against the immutable file.

`build/qa/mechanical-check.json` passes the static-removal, exact geometry, native-table, notes, critical-evidence and original-source-URL checks. The Artifact Tool import and structural finalization checks pass, recorded in `build/qa/finalizer.json` and the filename-specific validation receipt.

The finalizer retains one conservative page-11 native-table height warning (estimated overflow 0.1461 in). Root resolved it visually in Microsoft PowerPoint for Mac: the complete table, maturity, values/units and human-check steps are visible and separated. The bounded native check covered pages 3, 4, 8, 9, 11, 17, 18, 23, 25, 31 and 32. These pages opened without a repair prompt, showed content immediately and had no material clipping or unintended overlap. `build/qa/native-check.json` and `build/qa/native/` record this result. Root closed the checked copy without saving, and the final hash remained unchanged. Conservative text-fit estimates remain in `build/qa/fit-diagnostics.json`; they are estimates, not a claim of observed clipping.

## Reproduction and content records

`src/README.md` contains the bundled-runtime build, check, finalize and fresh-process render commands. `IMPLEMENTATION.md` records the geometry, SEE/SAY approach and per-page mechanisms. `src/implementation-mapping.json` and `src/content-coverage.json` connect the final page objects and notes to the approved source material. `src/approved-content.json` and `src/source-notes.json` preserve the complete source records; `src/speaker-notes.json` matches the embedded notes.

Private candidates, renders, third-party references and QA caches stay under ignored `build/`. Only the frozen final deck belongs in `output/`. Root owns the authorized local Git commit. No push or release is requested.
