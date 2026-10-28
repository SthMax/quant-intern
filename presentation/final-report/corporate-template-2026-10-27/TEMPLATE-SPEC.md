# Corporate PowerPoint layout specification

This is the authoritative layout specification for the 33-slide corporate-template adaptation. The user supplied the measurements on 27 October 2026. Implementation: GPT-6.1 Sol, xhigh. Independent review: the previous Astra PPT editor.

## Retained user intent for follow-up work

On 27 October 2026 root reread the user messages throughout the current thread, `01a167a1-425f-7363-b6c5-ae1379d1b1a9`, and the relevant closing turns of predecessor thread `01a1615c-bbad-79a2-9ef6-89d61eeaf8fa`. This section preserves the user's decisions through context compaction. Later user instructions govern any subsequent changes.

- The report recommends LLM applications for a mainland asset manager that had not adopted LLMs when the user described it. The user is an intern with limited cross-department access. Research the work and peer examples, then give concrete company recommendations. Do not make the user supply an internal interview study or decompose all departments before helping.
- The mentor requires a linear front-office, middle-office, back-office narrative. Seven task themes are established: research, trading support, client materials, content review, risk analysis, document processing and tool development. Keep the approved 33-slide structure during optimization.
- Each topic explains the work, relevant industry examples and the proposed company application. A proposal must visibly show what employees supply, what the LLM does, what tools/systems do, what output results, and how colleagues use it. Pages 8, 11, 15, 18, 21, 24 and 27 carry these proposals. The user specifically rejected pages that showed only generic business steps with no visible LLM contribution.
- The two recurring examples are Company A and the quarterly client update. Preserve their identities, facts and versions across departments. The approved color system makes Company A teal, client-update documents purple, navigation blue, tools/people neutral and changed passages yellow.
- Preserve the corrected trading input: the trader supplies received quote records and the LLM extracts their details. The wording must not revert to the LLM independently reading counterparty chats. Tool-development pages explain LLM assistance with requirements, code, testing and revision, as well as the resulting business tool.
- The user's preferred expression is direct, specific, formal business language. Avoid defensive stock phrases, unsolicited scope contraction and language such as “typical,” “does not mean,” “avoid pretending” or “hope to make recommendations.” State the workflow, action and recommendation. The user and mentor steer the substantive argument. Preserve source facts and units accurately.
- Slides should be visual and easy to present, with little text and substantial use of diagrams, document examples and comparisons. The mentor's webpage-like experience means a persistent company map, clear current location, local expansion/highlighting and sequential disclosure. Images and image generation are authorized when they explain the material. Preserve native editable business diagrams and text for company-template transfer.
- The previous technology-led organization around personal Qwen/Spark and company DeepSeek/server deployment was superseded by this workflow narrative. Model choices are implementation means. Do not restore the old technical chapters when consulting historical files.
- The current English wording has already undergone the user's requested professional business-English review and implementation. Give the writer and PPT agents English prompts and have them read review comments line by line. Preserve the approved wording while optimizing layout; explain any substantive proposed change separately.
- The current stage is refinement. The user said the content was broadly satisfactory before requesting clearer navigation, color semantics, professional English and template fit. Carry those accepted decisions forward rather than reopening the narrative.

### Proposed versus implemented navigation

The October 26 navigation/color discussion proposed a numbered three-step progress strip and a per-topic page counter. The subsequent color-only implementation explicitly retained the existing navigation. The delivered deck uses department/task highlighting, subtitle breadcrumbs and the overall page counter; the richer numbered strip and per-topic counter are a prior proposal, not an implemented feature. Keep that distinction in future status reports.

### Current artifact and continuation point

The completed corporate transfer edition is `output/asset-management-llm-corporate-transfer.pptx`, SHA256 `f7a92ebd1caf4f0257b89065d23b0eccc78456aa0248fdef13e4d7afbf0cf440`. Sol completed the adaptation, Astra accepted it, and root completed native PowerPoint checks. Use this edition as the visual baseline for follow-up work. The reproduction scripts intentionally start from the approved English source identified below and apply the recorded adaptation. The source dependency is not a direction to resume editing an earlier visual draft.

The user requested a standard, editable PPTX for manual integration into the company master, with no extra PDF. Corporate slide geometry is now measured and authoritative. The photographs provide placement context; the company template remains on the work computer. The latest staffing preference is Sol 6.1 xhigh for implementation, with the earlier Astra PPT agent reviewing. Git commit/push and GitHub release requests are separate completed actions for earlier revisions and do not automatically publish later modifications.

## Exact user requirements

All dimensions are in centimeters. All absolute coordinates are measured from the slide's top-left. Do not infer coordinates from a centered PowerPoint ruler without converting them.

| Property | Value |
| --- | ---: |
| Slide width | 25.40 |
| Slide height | 14.28 |
| Left margin | 1.27 |
| Right margin | 1.27 |
| Main-title top | 2.00 |
| Subtitle top | 3.00 |
| Body top | 3.92 |
| Bottom margin | 1.27 |
| Body left / right | 1.27 / 24.13 |
| Body bottom | 13.01 |
| Body width / height | 22.86 / 9.09 |

Keep the exact 14.28 cm height. Do not silently substitute a mathematically exact 16:9 height. The title and subtitle values specify the top of their text boxes. A single-line title should fit above the subtitle, and a subtitle should fit above the body. Horizontal placement below the body boundary is otherwise flexible and should support clear, attractive layouts.

## Vertical alignment guides

The slide center is x = 12.70 cm. The user's symmetric offsets convert as follows:

| Offset from center | Left absolute x | Right absolute x |
| --- | ---: | ---: |
| ±0.50 | 12.20 | 13.20 |
| ±3.55 | 9.15 | 16.25 |
| ±4.32 | 8.38 | 17.02 |
| ±6.47 | 6.23 | 19.17 |
| ±11.43 | 1.27 | 24.13 |

Sorted guide coordinates: 1.27, 6.23, 8.38, 9.15, 12.20, 13.20, 16.25, 17.02, 19.17, 24.13 cm.

Use these as alignment and component-width recommendations. Do not snap every small object or every text-box edge to a guide. Useful derived arrangements include two columns (1.27–12.20 and 13.20–24.13) and three columns (1.27–8.38, 9.15–16.25, 17.02–24.13). Individual slide composition may use other widths within the permitted area.

## Production decisions

These decisions implement the supplied geometry. They are not additional company requirements.

- Adapt the latest approved business-English deck, preserving its 33-slide sequence and approved copy. Keep the original deliverable untouched.
- Keep the brand area above y=2.00 free for the company's master. The company template supplies its logo and footer. Do not recreate its logo from the photographs.
- Use distinct, named title, subtitle, office-navigation, body, navigation-control and source-note objects. Keep title/subtitle text separate from the body so it can be placed in the company placeholders without duplicate sample text.
- Put body graphics, office navigation, controls, example labels and any source notes inside the body rectangle. Keep the lower 1.27 cm free for the company footer. A background may cover the canvas but must not obscure a destination master when copied.
- Use a consistent office-navigation position on workflow slides. A proposed sidebar spans x=1.27–6.23; choose and record a consistent main-content gutter after inspecting the content. Keep the office map and current position visible.
- Preserve Company A in teal (#317F7B, tint #EFF6F4), the quarterly client update in purple (#7363A6, tint #F3F0F8), structure/navigation in blue (#005A9C, tint #D9EAF7), neutral tools/people in #F3F7FA with #20262C text, and revised text in yellow (#FFF0BE).
- Use native editable diagrams and the native slide-11 table. Never flatten complete slides to pictures. Existing source artwork can be retained in the allowed area without distortion.
- Preserve stable object IDs/names, 407 internal links and their destinations, 33 Morph transitions at 0.70 seconds, and the existing appearance groups on 14 slides. Reflow shapes and text without replacing the underlying interaction system.
- Copy approved English exactly where possible. Rewrap and reorganize before reducing fonts. Necessary wording changes require a small explicit change log and review for business meaning. Fonts remain Arial unless the user supplies a corporate font requirement. The user has not yet specified corporate font sizes.
- Work in centimeters and explicit points, with one central conversion layer. 1 cm = 360000 EMU; 1 point = 12700 EMU. The exact canvas is 9144000 × 5140800 EMU. Do not pass pixel canvas dimensions to an exporter without an explicit physical-size conversion.
- Automated geometry inspection should flag material objects outside their allowed zones. Check native tables, groups, text insets, font sizes, line widths, connector endpoints and image aspect ratios in addition to shape bounding boxes. Any declared exception must be limited to an actual background or other documented design need.

## Source and reproduction

Source: `../english-business-revised-2026-10-26/output/asset-management-llm-business-en.pptx`

Source SHA256: `4fd31b6f18748ccdfc202619ea97d499d2d2ec6e815008df35e8fe695b1df7a2`

The existing source uses 15240000 × 8572500 EMU (42.333333 × 23.8125 cm). It came from a 1600 × 900 coordinate canvas at 9525 EMU per coordinate unit. Physical dimensions and corporate reserved zones must both be adapted. Changing only the slide-size element does not reflow its objects.

Related references: `../english-business-review-2026-10-26/BUSINESS-ENGLISH-REVIEW.md`, `../english-business-revised-2026-10-26/EDITORIAL-CHECK.md`, and that revision's `src/` and `DELIVERY.md`. The approved review has already been implemented and should not be reapplied to an earlier draft.

Photographs for visual context: `/Users/sthmax/Downloads/IMG_6791.jpg` (manual company layout) and `/Users/sthmax/Downloads/IMG_6792.jpg` (failed object paste). Measurements in this specification supersede visual estimates from those photographs. Sample words such as “test” in the photographs are not requested slide copy. Do not ask the user to export corporate files or bypass workplace security restrictions.

## Delivery and review

Create the revised PPTX under this directory's `output/`, reproducible code under `src/`, and private renders/diagnostics under `build/`. Keep this specification and `layout-spec.json` together. Add a short transfer guide with the exact geometry and steps for separating title/subtitle from body content. Be accurate that slide-level Morph and internal destinations need verification after transfer into another presentation.

Render and inspect every adapted slide. The Astra reviewer should compare all 33 renders with the specification and approved content, examine dense pages 8, 11, 17, 18, 23, 24 and 32, and check the geometry and interaction reports. Repair findings and recheck affected pages. Native PowerPoint checks should cover representative dense pages and linked/progressive sequences, without modifying the source file. Deliver the complete adapted deck after review. Commit, push and release are separate actions and are not part of this request.
