# Independent business-slide design review

Review the completed static draft after production, using GPT-6.1 Sol with xhigh reasoning. Write the review in English. You are an independent reviewer. The user rejected the previous edition's layout on every page and requested a fresh static draft plus your advice.

Read `HANDOFF.md` for the user requirements. Read the final draft, its extracted text and all 33 rendered pages. Read the latest user's requirements before the older specifications because animations, interactive controls, page counters and detached upper-right example labels must now be absent.

## Reference work

Inspect actual pages from official Morgan Stanley and BlackRock decks listed in HANDOFF.md. Use their readable local PNGs and open the PDFs if additional context helps. Cite the official links and precise one-based PDF page numbers. Explain what the references demonstrate and which principles apply to this deck. Their logos, palette, large document size, legal pages and dense specialist slides do not automatically suit the user's measured company template.

Do not assume a page is effective just because a prominent firm published it. Evaluate hierarchy, composition and readability yourself. Do not treat the author's design notes, prior agent acceptance or a successful geometry check as your conclusion.

## Questions for every slide

- Is the page's purpose clear on first viewing? What should the audience look at first, second and third?
- Does the main evidence, workflow or output dominate the composition? Is section context appropriately subordinate?
- Does the layout suit this particular content, with aligned edges, deliberate spacing and a useful balance of text and visuals?
- Are the typography and line breaks natural, and are labels close to their objects? Is any prose too dense or unnecessarily split?
- Are flows and arrows semantically clear, including who supplies information and where it goes? Does the LLM's contribution remain visible on proposal slides?
- Do Company A and the client document remain recognizable through content and color, without the removed upper-right badges?
- Can colleagues edit the text, diagrams and table and add their own animation? Do objects stay within the measured company regions?

The entire slide should be legible at full-slide display. Check actual rendering in addition to font-point values. Keep the complete client V1/V2 passages, financial units, source facts and the established business argument accurate when suggesting shorter wording or different grouping.

## Requested report

Write `DESIGN-REVIEW.md`, identifying the reviewed draft's path and SHA256 so the advice remains attached to the right version. Include:

1. A concise overall assessment of the new draft, grounded in specific pages.
2. The highest-priority recommendations, each with exact slide numbers and an implementable action.
3. A reference analysis with links/pages and concrete lessons.
4. A page-by-page review of all 33 pages, recording the main visual issue and proposed change, or a specific reason to keep the composition when it works. Use clear priorities such as Required, Recommended and Keep; do not invent criticism to fill a row.
5. Cross-deck recommendations for consistency and presentation rhythm, plus any genuine trade-offs that the user should choose.

Inspect each page individually at readable size. A contact sheet can supplement the review but cannot replace individual inspection. State exact observed defects such as an awkward reading order, weak emphasis, inconsistent gutters, text clipping or a misleading connector. Avoid generic comments such as “make it more professional” or “add whitespace” without placement guidance.

The user requested a draft and independent advice. Do not edit the PPTX or production source, do not approve it on the author's behalf, and do not initiate a redesign loop. Report urgent defects to root promptly, then finish the complete review. Root will deliver the stable draft and your recommendations together.
