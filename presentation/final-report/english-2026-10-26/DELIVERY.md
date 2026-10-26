# English edition

Final PowerPoint: `output/asset-management-llm-interactive-en.pptx`

SHA256: `86822d1bb55cf9ac3d5a0b4894705be6b68966d44c6851ca7d16501a6bae146d`

The 33-slide English edition adapts the slide copy, speaker notes, navigation labels and tooltips. Arial typography, shorter wording, column widths and document fields accommodate English text. Company A remains teal and the client update remains purple. Business diagrams and the quotation table remain editable.

All 407 internal links, 33 Morph transitions and the 14 slides with staged appearances retain their original targets and timing. The quotation example uses trader-supplied quote records, RMB 20m face values and a clean price of 100.20 per RMB 100 face value. Original source URLs remain in the speaker notes.

All 33 slides received visual review. Native PowerPoint checks covered pages 3, 9, 11, 17, 18, 21, 24, 30 and 31, including navigation and the V1-to-V2 transition. Package, layout, font, import and interaction checks passed. Private review records and rendered pages are under `build/qa/`.

## Sources and reproduction

The input is the Chinese color revision at `../color-revision-2026-10-26/output/asset-management-llm-story-colors.pptx`. Its SHA256 is `e0dd5d80c18d5f391968245f79d70941c87e8180faf44e86f3a123f31cfd4faa`.

English text lives in `src/english_copy.py`; `ENGLISH-COPY.md` provides a readable export. Run `src/export_copy.py`, then `src/build_english.py`, followed by `src/finalize.mjs` and `src/check_english.py`. Use the bundled Python runtime for layout preparation and the bundled Node runtime for rendering/finalization. `src/render-one.mjs` renders one slide in a fresh process. Preserve an existing final file and validation receipt before rebuilding to the same output path.
