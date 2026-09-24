# Research Tooling Audit

Checked by Codex on **6 September 2026**, Asia/Shanghai, against the current
session's callable tools, local MCP configuration, installed dependencies, and
the [confirmed project plan](PROJECT_PLAN.md).

The core workflow for public-source research is operational: search, open
original sources, inspect Chinese webpages, analyze tables, record evidence,
and prepare reports. The setup has gaps in citation-library access, batch
Chinese OCR, and the standalone Playwright browser. These do not prevent the
current Phase 1 work, but this is not an assertion of unrestricted database
access or a fully tested end-to-end production research environment.

## MCP and connector status

“Passed” means the specific live check below succeeded. “Available” means the
tool schema or dependency is present; it does not mean every operation was
tested. Availability and authentication can change between sessions.

| MCP / connector | Research purpose | Check and status |
|---|---|---|
| `exa_search` | General search; advanced domain/date/category filters; webpage extraction; code context | **Passed:** searched for a Chinese regulatory source and extracted the original CAC page. Advanced filters and code-context tools are available but were not separately tested. |
| `exa-search-http` (tool prefix `exa_search_http`) | Same Exa tools | **Passed:** search succeeded. Local configuration confirms the exact same endpoint as `exa_search`; this is not an independent search provider. |
| `fetch` | Retrieve a known URL as Markdown or raw HTML | **Passed:** retrieved official OpenAI MCP documentation. |
| `context7` | Current library and framework documentation | **Passed:** resolved vLLM and retrieved documentation with official source links. |
| `node_repl` | Persistent JavaScript for analysis and transformations | **Passed:** executed a simple calculation. |
| `microsoft-playwright` | Standalone automated browser with page inspection, screenshots, and downloads | **Failed:** required Chrome for Testing / Chromium revision 1243 is absent. The suggested installer attempted the download, but it timed out repeatedly. Use the verified in-app browser for research. |
| GitHub through `codex_apps` | Repositories, code, issues, model implementations, and benchmark provenance | **Passed:** authenticated account lookup. Repository-specific access remains subject to the connected account's permissions. |
| Zotero MCP | Reference-library integration | **Disabled** in local configuration and absent from callable tools. Its configured authentication was not tested. |
| Legacy `computer-use` server | Separate local computer-control integration | **Disabled** in local configuration. The in-app CUA browser is a separate, working capability. |

Additional callable MCP groups include Codex app/task management, plugin
permission management, Sites, document-session control, and the artifact
template picker. These are supporting tools; their presence does not provide
additional research databases. They were not exhaustively exercised.

Exa also exposes legacy `deep_search_exa` and `deep_researcher_start/check`
tools. Their schemas explicitly mark them **deprecated**. Prefer normal or
advanced Exa search and direct source inspection; legacy research execution was
not tested.

## Other research tools

| Capability | Available tools | Verification / limitation |
|---|---|---|
| Independent web discovery | Built-in web search, domain/recency filters, page opening, link navigation, text finding | **Passed:** live search and page retrieval. Also exposes PDF screenshots, image search, and finance lookups; those were not tested. |
| Interactive websites | CUA / Codex in-app browser | **Passed:** opened the original CAC page and read its Chinese article text. This provides a working alternative to standalone Playwright. |
| Clean local webpage extraction | Defuddle CLI | Executable and skill present; network extraction was not tested. Fetch and Exa extraction already passed. |
| Local files and evidence | Shell, `rg`, file editing, Git, Python, JavaScript | File reads and local configuration checks passed. Existing Markdown source register and evidence templates remain the project's citation workflow. |
| Tabular analysis | Bundled Python with pandas, NumPy, openpyxl | Packages detected. Use the bundled interpreter rather than assuming system Python has them. |
| PDFs | pypdf, pdfplumber, ReportLab, `pdftoppm`, image inspection | Libraries/executable detected; no representative PDF extraction/rendering test in this audit. |
| Scanned documents | Tesseract and image inspection | Tesseract runs, but installed languages are `eng`, `osd`, and `snum`. Simplified/traditional Chinese OCR models are absent. |
| Reports and presentations | Word, spreadsheet, PDF, presentation, LaTeX, and visualization skills | Skills are available; python-docx and python-pptx detected. Artifact creation/rendering was not tested. |
| Structured research workflows | Deep Research skill; Obsidian and policy-research skills | Skills are available, not additional database subscriptions. Invoke the Deep Research workflow when explicitly requested. Vault access and specialized workflows were not tested. |

Bundled Python at audit time:

```text
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
```

Use `load_workspace_dependencies` to resolve the current path in later sessions.
SciPy, statsmodels, matplotlib, seaborn, Plotly, requests, Beautiful Soup,
PyMuPDF, and DuckDB were not detected in that interpreter. Install only the
dependencies needed for a concrete analysis in an isolated project environment.
Built-in retrieval and JavaScript tools already cover basic collection and
transformation needs.

## Recommended routing for this project

1. **Chinese company landscape:** discover with built-in web search and Exa;
   open fund-company disclosures and original partner announcements; distinguish
   company statements, vendor claims, pilots, and production deployments.
2. **Regulation:** search Chinese originals from the relevant authorities; open
   and inspect the provision; verify publication/effective dates, amendments,
   legal status, and applicability separately. Use the in-app browser for
   interactive pages. A successful extraction is not a legal-status check.
3. **Models and infrastructure:** retrieve original model cards, papers,
   repositories, licenses, and benchmark definitions. Use GitHub for provenance
   and Context7 for current implementation documentation.
4. **Costs and ROI:** use dated vendor pricing and quotations, with explicit
   currencies, taxes, usage assumptions, and sensitivity analysis in a workbook.
5. **Evidence and delivery:** follow the [knowledge-base workflow](knowledge-base/README.md)
   and [source register](knowledge-base/source-register.md). Preserve exact
   article/page/section pointers and distinguish source facts from analysis.

Using two Exa aliases does not corroborate a claim. Corroboration requires
independent supporting sources, even when discovery uses different tools.

## Remaining improvements

| Priority | Improvement | Current position |
|---|---|---|
| Useful for literature work | Enable and test the existing Zotero integration if this project should use that library | Disabled. Zotero supports collection and citation management; the Markdown source register works now. [Zotero documentation](https://www.zotero.org/support/quick_start_guide). |
| Needed for batch Chinese scans | Add official Tesseract `chi_sim` and, if needed, `chi_tra` language data; test on representative scans | Missing. Visual inspection is available for individual pages. [Official language models](https://github.com/tesseract-ocr/tessdata_fast). |
| Optional convenience | Connect one specialist literature service, such as Consensus or SciSpace | Listed as available-to-install plugins, but neither has callable tools in this session. These can improve paper discovery; coverage must still be checked against original papers. [Consensus](https://help.consensus.app/en/articles/9922673-how-consensus-works), [SciSpace](https://scispace.com/help/en/collections/7177367-literature-review). |
| Maintenance | Restore the standalone Playwright browser runtime | Installer download failed; in-app browser passed. |

No callable connectors for Wind, Bloomberg, CNKI, or internal firm
systems were found in this session. This does not establish whether the user
holds subscriptions or can access a particular service through an authorized
browser session. Public tools cannot verify unpublished internal MRM policy.

## Audit method and maintenance

- Inspected the active tool registry and only non-secret MCP configuration
  metadata. No project-scoped `.codex/config.toml` or `.mcp.json` was present.
- The live source-access test used the
  [CAC original](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm).
  This was a tooling check, not a completed regulatory evidence note.
- The browser repair command was
  `bunx -y @playwright/mcp@latest install-browser chrome-for-testing`.
  It failed to download the required browser. MCP enablement, credentials,
  permissions, and server configuration were not changed.
- Current Codex documentation describes shared host MCP configuration in
  `~/.codex/config.toml` and optional trusted project configuration in
  `.codex/config.toml`. [Official MCP documentation](https://developers.openai.com/codex/mcp/).
- Recheck affected tools after account, configuration, runtime, or plugin
  changes. Record failures explicitly instead of equating configuration with
  working access.
