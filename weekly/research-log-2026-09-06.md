# Week 2 Research Start — 6 September 2026

The user authorized starting the Week 2 plan. Read `RESEARCH_TOOLS.md`; used
built-in web and Exa discovery, original-source retrieval, and the PDF skill for
selected-page extraction/rendering. The two Exa aliases are one provider.
No internal systems or paid financial databases were accessed.

## Completed first batch

| Work | Result |
|---|---|
| Company disclosures | 6 managers / 7 primary-source initiatives |
| Scale observations | 6 sourced broader/group-AUM figures; 2 separate public-fund AUM observations |
| Additional candidates | 10, not counted as verified |
| Official governance corpus | 12 publications, with law/rule/guidance/standard/research categories distinguished |
| Master register | 30 sources: 25 primary, 5 candidate secondary/discovery sources |
| Synthesis | Company and three-theme regulatory summaries |
| Presentation input | First Phase 1 research brief |
| Human verification | Pending; no human sign-off asserted |

## Material findings and qualifications

- REG-007/008: SR 26-2 replaces SR 11-7; the April 2026 guidance excludes
  generative and agentic AI. Internal firm MRM coverage is not established.
- REG-009/010: AMAC's April 2026 LLM application standard is directly relevant.
  Standard recommendations, statutory duties, and adoption requirements need
  separate treatment.
- REG-001: service audience matters to the generative-AI interim measures;
  non-public organizational use is a distinct scope question.
- Procurement, service terms, and reported operational platform cases provide
  different kinds of adoption evidence.
- Reposts remain secondary reporting; proprietary model origin and a contractual
  technology partner are different facts.
- AUM dates/scopes differ. Lower bounds were not converted into exact values
  or invented upper bounds.

## Retrieval and verification details

- Exa is useful for discovery, but a returned page may include several documents
  or substantial navigation. Legal passages were located within the named
  original document; PIPL was fetched separately to avoid cross-document mixing.
- Some Exa/web requests to AMAC, CSRC and XQ pages failed or timed out. Original
  HTML/PDF retrieval succeeded where used as evidence.
- `pdftotext` was absent from PATH. The bundled Poppler executable and bundled
  Python/pypdf worked; no dependency installation was needed.
- PDF visual checks covered the ChinaAMC award row, AMAC interpretability clause,
  Fullgoal RAG page, Dacheng Qwen page, and GF service-definition page.
- Critical PDF hashes identify the inspected versions. Primary PDFs/rendered
  images are temporary retrieval artifacts; reusable repository records are
  Markdown notes and official source links.
- Missing PDF publication dates were left unverified rather than inferred from
  URLs. The GF document repeats a printed page number, so notes use physical PDF
  page indices.

## Repository boundary

At session start `README.md` had an existing tools-navigation edit and
`RESEARCH_TOOLS.md` was untracked. These user-side changes are preserved and
excluded from the research-only commit. The final `PROJECT_PLAN.md` is unchanged.

## Next actions

1. Verify the ten additional company candidates, prioritizing original company
   or association project disclosures.
2. Capture comparable public-fund AUM and current licence-register checks.
3. Resolve source publication dates and complete amendment/repeal/status searches.
4. Extend the legal corpus to current cybersecurity/data-security law, audit,
   labelling and relevant referenced standards.
5. Obtain internal MRM/AMAC-adoption/COD inputs through the user.
6. Complete human source review and build the final presentation.

## Integrity checks

- Checked 153 local Markdown links across 40 Markdown files; all targets resolve.
- Checked table-column consistency and registered source IDs; no issues found.
- Reconciled 30 source rows (25 primary / 5 candidate), 6 company rows, and
  7 initiative rows with summaries.
- Verified three recorded PDF SHA-256 hashes against retrieved files.
- Git diff whitespace check passed; the final project plan remains unchanged.
- These are repository/content-integrity checks, not human legal approval or
  independent validation of company performance claims.
