# English copy: LLMs in Asset Management

33 slides. Office labels: Front office / Middle office / Back office. Stages: Workflow / Peer practices / Proposed approach. Running examples: Company A / Client update.

All economic values follow the Chinese source. Financial comparisons use prior/current quarter, not year-on-year.

## 01. LLMs in Asset Management



### Slide copy

- Peer practices and proposed applications
- LLMs in / Asset Management
- October 2026

### Speaker notes

This presentation examines how LLMs can support the day-to-day work of an asset manager. It starts with peer practices, then develops proposed applications for the firm. The discussion follows front-, middle- and back-office work, using Company A and a quarterly client update as recurring examples. Cover image: an AI-generated research workspace.


## 02. Research scope and application goals

Research scope

### Slide copy

- Daily inputs
- Work supported by LLMs
- Work products
- Documents
- Retrieve and organize
- Company analysis
- Data
- Calculate and explain
- Trade details
- Messages
- Query and act
- Client materials
- Business requests
- Draft and collaborate
- Business tools
- Build applications around the work people need to complete

### Speaker notes

The inputs are documents, data, messages and business requests. LLMs interpret questions, read and compare material, organize explanations, and draft text or code. Connected tools perform queries, calculations and other operations. Employees check the results and use them to complete research, trading preparation, client communications, review and development tasks.


## 03. Seven workflows across the firm

Firm overview

### Slide copy


### Speaker notes

The map covers seven workflows. Each topic begins with the work employees do and the repetitive preparation it involves, then looks at peer practices and a proposed approach for the firm. Company A links research, bond inquiries and risk monitoring. The quarterly client update links drafting, review and document maintenance. The task names provide direct navigation to each topic.


## 04. Preparing a company research assessment

Front office  /  Research  /  Workflow

### Slide copy

- Analyst: Why did revenue grow, and can the growth continue?
- [1] Prior / current quarter
- Revenue (RMB m): 100 / 110 / Volume (m units): 1.0 / 1.1
- [2] Meeting notes
- Restocking lifted shipments. / Monitor its persistence.
- [3] Two research reports
- A: demand recovery can last. / B: will restocking last?
- The analyst’s preparation work
- Find relevant sources
- Extract data and / calculate changes
- Reread and / compare views
- Document the / reasoning
- Repeated searching, extraction and checking take time away from analysis

### Speaker notes

The analyst needs to explain why Company A’s revenue grew and whether that growth can continue. The preparation involves locating comparable revenue and volume data, reading the explanation in meeting notes and comparing two research reports. In this illustrative scenario, prior-quarter and current-quarter revenue are RMB 100m and RMB 110m, while sales volume is 1.0m and 1.1m units. Repeated searches, extraction, calculations and rereading are the work required before the analyst can assess the business. The next three slides show peer approaches to earnings analysis, research synthesis and template preparation.


## 05. Tianhong: analyzing earnings drivers

Front office  /  Research  /  Peer practices

### Slide copy

- The LLM breaks down the question. Tools retrieve data and calculate.
- Change in / net profit
- Revenue
- Volume and selling price
- Cost of sales
- Materials and production costs
- Expenses
- Distribution and selling expenses
- Data / feeds / and / calculation / tools
- The LLM links operating evidence to the numbers. Analysts assess the quality of growth.

### Speaker notes

Tianhong’s FinAgent breaks a net-profit question into revenue, cost of sales and expenses, then explores drivers such as volume, selling price, raw materials and distribution. The LLM organizes the questions and calls data and calculation tools. Those tools return the figures and calculations. The model connects them to operating and industry information, while the analyst assesses the quality and persistence of growth. Tianhong reported that the associated manual data preparation and calculations fell from days to minutes.

Sources:
FUND-300, pp. 5–6
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf


## 06. Fullgoal: comparing research views

Front office  /  Research  /  Peer practices

### Slide copy

- The LLM reads each report against the same research question
- Report A
- Higher volumes lifted revenue. / Demand recovery can sustain growth.
- Report B
- Channel restocking lifted shipments. / Its persistence remains uncertain.
- Fullgoal’s LLM workflow
- Screen relevant reports / Summarize by topic / Combine and check the wording
- Identify common ground
- Higher volumes supported revenue
- Preserve the disagreement
- Demand recovery or restocking?
- Analysts investigate the disagreement, with links back to the underlying reports

### Speaker notes

Fullgoal first uses the model to assess each report’s relevance to the investment target. It then summarizes the reports against the analyst’s research interests, synthesizes the summaries, adjusts the wording and checks the result. In the Company A example, Report A links higher volumes to a lasting demand recovery. Report B emphasizes channel restocking and questions whether it will persist. The LLM makes the common ground and competing explanations easy to compare. The analyst can investigate the disagreement with the original reports at hand.

Sources:
FUND-007, pp. 8–9
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808067241.pdf


## 07. Zhong Ou: populating research templates

Front office  /  Research  /  Peer practices

### Slide copy

- The LLM turns source material into a populated research template
- Source materials
- Illustrative research template
- Financials and calculations
- Operating change
- Sales volume up 10%
- Meeting notes
- Business driver
- Restocking lifted shipments
- Research reports
- Open question
- Will the restocking cycle persist?
- Reported ~50% improvement in research preparation efficiency (May 2026)
- Analysts check the entries and sources, then add their own assessment

### Speaker notes

Zhong Ou’s assistant connects internal research information and external sources, separates collection, analysis and synthesis, and populates a research template. The example maps financials and calculations to operating changes, meeting notes to business drivers, and research reports to open questions. These example fields illustrate the method. Analysts check the entries and sources and add their own assessment. Zhong Ou reported an approximately 50% improvement in overall preparation efficiency, with data as of May 2026.

Sources:
FUND-354, Application design and implementation
https://static.nfnews.com/content/202511/27/c11946239.html
FUND-356, Research template; data as of May 2026
https://mp.weixin.qq.com/s/rgMRw8HbZUhiu9PkUBM7vA


## 08. Proposed research workflow

Front office  /  Research  /  Proposed approach

### Slide copy

- Analyst: Why did revenue grow this quarter, and can it continue?
- [1] Prior / current quarter
- Revenue (RMB m): 100 / 110 / Volume (m units): 1.0 / 1.1
- [2] Meeting notes
- Restocking lifted shipments
- [3] Research reports
- A: lasting demand recovery / B: restocking duration unclear
- LLM analyzes the sources
- Compare revenue and volume / Link the operating explanation / Compare the research views
- Calculation tools return
- Revenue: +10% / Volume: +10% / Average selling price: unchanged
- LLM analysis
- Volume drove revenue growth [1], supported by channel restocking [2]. / Views differ on persistence [3]. Track demand and input costs.
- The analyst checks the sources, tests the restocking thesis and forms a view

### Speaker notes

The proposed workflow brings together Tianhong’s earnings-driver analysis, Fullgoal’s comparison of research views and Zhong Ou’s research-template preparation. The analyst provides a question and the relevant financials, meeting notes and research reports. Prior-quarter and current-quarter revenue are RMB 100m and RMB 110m; volume is 1.0m and 1.1m units. The LLM requests the revenue and volume growth calculations. The tools return 10% growth in each and an unchanged average selling price. The LLM then links channel restocking in the meeting notes to the reported numbers and preserves the disagreement over persistence. The analyst checks the references, tests the restocking thesis and forms a view. The figures and source excerpts are illustrative.

Sources:
FUND-300, pp. 5–6
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf
FUND-007, pp. 8–9
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808067241.pdf
FUND-354, Application design and implementation
https://static.nfnews.com/content/202511/27/c11946239.html
FUND-011, pp. 5–7
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337841539992.pdf


## 09. Preparing a bond quote request

Front office  /  Trading support  /  Workflow

### Slide copy

- Task: request offers for Company A bonds maturing within two years
- 1  Portfolio manager
- Company A bonds / Due within 2 years / Check current holdings / Collect offer quotes
- 2  Trader: query
- Find bonds and holdings / Record the data timestamp
- 3  Trader: quotes
- Name the bonds / State buying interest / Ask for price and size / Receive quotes
- 4  Trader summary
- Summarize bonds and quotes / Discuss next steps / with the portfolio manager
- Request
- Bonds
- Quotes
- Market / holdings
- Query results
- Query results
- Counterparty
- Returns quotes
- RFQ
- Quote
- Repeated work: entering filters, switching systems and copying quote messages

### Speaker notes

The task is to prepare candidate bonds, current holdings and offer quotes for a potential purchase of Company A bonds maturing within two years. The portfolio manager sets the request. The trader queries market and holdings systems and records the data timestamp, then contacts counterparties with the bond names and buying interest, asks for price and available size, and receives quotes. The trader brings the information together for discussion with the portfolio manager. Systems supply data and counterparties supply quotes. Repeated filters, system switching and copying messages are the preparation steps the proposed application can improve.


## 10. Trading applications at Southern and Aegon-Industrial

Front office  /  Trading support  /  Peer practices

### Slide copy

- Southern Asset Management: Xiaonan trading assistant
- User request
- Specify a screen, / query or action
- LLM interprets
- Read the request / Call the right tools
- Systems execute
- Run the task / Return the result
- User follows up
- Review the data / Confirm next steps
- Xiaonan supports queries, bond screening, order instructions and notifications
- Aegon-Industrial: capturing trade details from Qtrade records
- Qtrade records
- Bond, side, / price and size
- AI extracts details
- Extract the details / for the system
- Match and route
- Match the request / Route to trading
- Portfolio manager
- Submits the / instruction

### Speaker notes

Southern’s Xiaonan assistant interprets a natural-language request, identifies parameters, breaks the work into tasks and calls database or business-system interfaces. Its applications include bond screening, market queries, trading instructions and notifications. Users review the results and confirm relevant actions. Aegon-Industrial’s Qianxun platform also captures trade information from Qtrade records, extracting bond, direction, price and size. It matches that information with the portfolio manager’s quote request and routes it to the trading system, where the portfolio manager submits the instruction. These are two distinct peer applications: connecting language to system queries and reducing repeated entry of trade information.

Sources:
FUND-200, pp. 4–8
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337849876845.pdf
FUND-011, pp. 3–6
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337841539992.pdf


## 11. Proposed bond quote workflow

Front office  /  Trading support  /  Proposed approach

### Slide copy

- Portfolio manager: check holdings and collect offers for Company A bonds maturing within two years
- LLM parses the request
- Issuer: Company A / Side: buy / Maturity: within two years / Query: bonds and holdings
- Systems run the query
- Bond A (Company A) / Maturity: 1.2 years / Held face value: RMB 20m
- LLM parses quote records
- The trader provides this quote: / “Bond A: clean price 100.20, / RMB 20m face value available.” / Extract bond, price, face value
- LLM combines query results and quotes
- The trader checks the source and quote time. The portfolio manager discusses next steps.

| Bond / maturity | Held face value (RMB m) | Clean price per RMB100 face value | Available face value (RMB m) |
|---|---:|---:|---:|
| Bond A / 1.2 years | 20 | 100.20 | 20 |

### Speaker notes

The portfolio manager wants to buy Company A bonds maturing within two years, check current holdings and collect offer quotes. The LLM extracts the issuer, maturity condition and requested data, then calls the business query. Systems return the candidates, maturities and holdings. The trader first requests quotes from counterparties, then provides the received quote messages or quote request records. The LLM parses those supplied records, extracts the bond, clean price and available face value, and combines them with the system results. In the example, the Company A bond has 1.2 years to maturity, held face value is RMB 20m, the offer clean price is RMB 100.20 per RMB 100 face value, and RMB 20m face value is available. The trader checks the record’s source, time and amounts. The portfolio manager uses the summary to discuss next steps. The approach draws on Southern’s natural-language queries and Aegon-Industrial’s parsing of trading records.

Sources:
FUND-200, pp. 4–8
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337849876845.pdf
FUND-011, pp. 3–6
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337841539992.pdf


## 12. Preparing a quarterly client update

Front office  /  Client materials  /  Workflow

### Slide copy

- A client relationship manager prepares a quarterly update
- The client’s questions
- What changed in the company’s business this quarter? / What should we watch next?
- Portfolio manager views
- Product documents
- Previous client materials
- Work repeated for each update
- Find the relevant views
- Check the fund / and source period
- Adapt the content / to the client’s questions
- The same source material is repeatedly adapted for updates, Q&A and RFP responses

### Speaker notes

A client relationship manager first establishes what the client wants to understand. Preparing a quarterly update then means finding the relevant portfolio manager views, checking product documents and the reporting period, and adapting the wording for the client’s questions. The same material is repeatedly reused in updates, product Q&A and institutional RFP responses. The next slides show Tianhong’s view summaries, ICBCUBS’s RFP support and a proposed quarterly-update workflow.


## 13. Tianhong: portfolio manager views and market commentary

Front office  /  Client materials  /  Peer practices

### Slide copy

- Tianhong uses LLMs to bring together recent manager and product views
- Presentations, commentary and reports
- “Company A’s revenue grew with volumes. / We are watching raw-material costs.”
- LLM organizes the response
- Find the relevant views / Combine overlapping content / Write a clear client explanation
- Summary for client teams
- Revenue improved as volumes rose. Continue monitoring raw-material costs.
- Tianhong also produces weekly sector views and daily market commentary

### Speaker notes

Tianhong brings together recent manager presentations, market comments and periodic reports for a named portfolio manager or product. The LLM finds the relevant views, removes duplication and writes a concise explanation for client-facing teams. The example turns a view on Company A’s volume growth and raw-material costs into a client summary. Employees check and use that summary in their communication. Tianhong also turns market information into weekly sector views and daily commentary.

Sources:
FUND-300, pp. 7–9
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf


## 14. ICBCUBS: institutional RFP responses

Front office  /  Client materials  /  Peer practices

### Slide copy

- Institutional client: how is your investment research process organized?
- Internal reference material
- Research process description: / Analysts prepare company research. / Portfolio managers discuss the view.
- LLM finds and drafts
- Find the research process / Identify who does what / Draft the RFP response
- Draft RFP response
- Analysts prepare research. / Portfolio managers discuss / the investment view. / Source: research process
- The business team checks the answer and source, then addresses the client’s specific requirements
- ICBCUBS FundGPT connects knowledge maintenance, question analysis, review and RFP drafting

### Speaker notes

ICBCUBS FundGPT links knowledge maintenance, question analysis and review with RFP response generation. The example client asks how the research process is organized. The model finds the internal process description, identifies the responsibilities of analysts and portfolio managers, and drafts the relevant answer with a source reference. The business team checks the answer against the source and addresses the client’s specific requirements. The question and answer on the slide are illustrative.

Sources:
FUND-312, pp. 7, 9
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337848496316.pdf


## 15. Proposed client update workflow

Front office  /  Client materials  /  Proposed approach

### Slide copy

- Client question / What matters this quarter?
- Existing view / Volume and input costs
- Product information / Q2, V1
- LLM drafts
- Extract relevant views / Organize the update / for quarterly discussion
- Quarterly client update
- V1
- Fund name
- Product A Select
- Source version
- Q2 2026 product information, V1
- Current view
- Volume growth drove Company A's revenue. / Monitor raw-material costs.
- Risk disclosure
- Investing involves risk.
- The client team checks the view and submits the same update for review

### Speaker notes

The client team supplies a question, existing portfolio manager views and product information. The LLM selects the relevant content and organizes a quarterly client update. In the example, the existing view says volume growth drove Company A’s revenue and that raw-material costs should be monitored. The product material supplied is the Q2 version, so the resulting document is V1. The client team checks the view and submits the same update for review. The following section compares it with the fuller current presentation and Q3 product documents.

Sources:
FUND-300, pp. 7–9
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf
FUND-312, pp. 7, 9
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337848496316.pdf
FUND-351, Digital finance applications
https://fund.10jqka.com.cn/20251111/c672391490.shtml


## 16. Reviewing client communications

Middle office  /  Content review  /  Workflow

### Slide copy

- Quarterly client update
- V1
- Fund name
- Product A Select
- Source version
- Q2 2026 product information, V1
- Current view
- Volume growth drove Company A's revenue. / Monitor raw-material costs.
- Risk disclosure
- Investing involves risk.
- Current manager presentation
- “Channel restocking lifted volumes. / Its persistence needs monitoring.”
- What the reviewer checks
- Does the draft explain the driver? / Does it retain the watch points?
- Compare the source wording, fund name, reporting period and risk disclosure

### Speaker notes

The reviewer compares V1 with the current portfolio manager presentation. V1 links revenue growth to volumes; the fuller source explains that channel restocking supported volumes and that its persistence needs monitoring. The reviewer must assess whether the update explains the driver and preserves the watch points, alongside checks on the fund name, source period and risk disclosure. Finding the relevant passages, comparing their meaning and explaining proposed edits are tasks an LLM can support.


## 17. Penghua and Yingmi: content review

Middle office  /  Content review  /  Peer practices

### Slide copy

- Quarterly client update
- V1
- Fund name
- Product A Select
- Source version
- Q2 2026 product information, V1
- Current view
- Volume growth drove Company A's revenue. / Monitor raw-material costs.
- Risk disclosure
- Investing involves risk.
- LLM checks current sources
- Name and period are outdated. / Use current documents.
- LLM compares meaning
- Source: restocking drove growth. / Add the restocking driver and / uncertainty over its duration.
- LLM clarifies risk wording
- Source: NAV volatility and capital risk. / State both risks explicitly.
- Penghua suggests rule-based edits. Yingmi supports pre-review, revision and rechecking.

### Speaker notes

Penghua’s marketing-material review system applies 71 rules across seven categories and produces suggested edits. The rules cover risk disclosures, fund information, performance claims and prohibited marketing statements. Penghua reported a 91% acceptance rate for suggested edits. Yingmi, a fund distributor, accepts text or files, identifies issues and reasons, suggests changes and supports rechecking after revision. The illustrative client update shows the model checking outdated product details, recognizing the missing restocking explanation and persistence watch point, and making the risk wording more specific.

Sources:
FUND-308, pp. 6
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337850951100.pdf
Yingmi official release and API client
https://www.yingmi-inc.com/archives/799


## 18. Proposed drafting and review workflow

Middle office  /  Content review  /  Proposed approach

### Slide copy

- Author supplies current sources
- V1 update and V2 product documents / Presentation: restocking drove growth. / How long it will last remains uncertain.
- File tools locate changes
- Match fund name, source period and passages
- LLM explains and revises
- Add channel restocking as the driver / Retain the question of persistence / Use the product’s specific risk wording
- Quarterly client update
- V2
- Fund name
- Product A Select Mixed-Asset Fund
- Source version
- Q3 2026 product information, V2
- Current view
- Company A’s volume growth reflects channel restocking. / Monitor whether restocking continues and track raw-material costs.
- Risk disclosure
- The fund's NAV fluctuates with markets. / Capital is at risk.
- The author approves the edits. The reviewer checks the sources, rationale and revised update.

### Speaker notes

The proposed approach brings V1, current product information and the full portfolio manager presentation into the same review task. File tools match names, reporting periods and source passages. The LLM reads the wording in context, explains the missing business driver and watch point, and suggests a concrete revision. V2 adds channel restocking and its persistence, updates the formal fund name and source version, and uses the product’s specific risk wording. The author approves the edits. The reviewer checks the source, rationale and revised document.

Sources:
FUND-308, pp. 6
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337850951100.pdf
Yingmi official release and API client
https://www.yingmi-inc.com/archives/799


## 19. Investigating a risk alert

Middle office  /  Risk analysis  /  Workflow

### Slide copy

- A risk analyst receives an alert
- Company A is on ratings watch. / Operating cash flow is under pressure.
- The risk team needs to establish
- Which funds are exposed?
- Query holdings / Check funds and amounts
- Which rules apply?
- Read contracts and controls / Find the relevant clauses
- What is the impact?
- Review issuer research / Prepare an event assessment
- Read each alert, then search several systems and documents for the same issuer

### Speaker notes

The risk analyst receives an alert: Company A is on ratings watch. Operating cash flow is under pressure. The next questions are which funds hold the issuer’s bonds, which monitoring requirements apply, and what existing research needs updating. Answering them means querying holdings, locating contract or internal-policy clauses and reviewing issuer research. The alert and scenario are illustrative. Peer practices on the next slide show how models can help with alert extraction, rule explanations and event assessments.


## 20. China Universal and Tianhong: risk support

Middle office  /  Risk analysis  /  Peer practices

### Slide copy

- China Universal
- Tianhong
- LLM reads custodian risk alerts
- Extract the relevant risk information / Route it to the risk team’s workspace
- System links rules to sources
- Map risk rules to regulations, / internal controls and contract terms
- The LLM explains the rule using its source text
- Event information
- Event details, historical parallels, / industry links and market sentiment
- LLM develops an explanation
- Compare the event with past cases / Outline implications and follow-up
- Investment and risk teams discuss the implications

### Speaker notes

China Universal’s platform uses an LLM to extract risk information from custodian alerts and route it to the risk team’s workspace. It also links system rules to regulations, internal controls and contract wording so that a model can explain the basis for a rule trigger. Tianhong’s event assistant brings together event details, historical parallels, industry relationships and market sentiment to develop an impact explanation. Investment and risk teams use the material to discuss the event and determine their response.

Sources:
FUND-220, pp. 5
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337837900594.pdf
FUND-300, pp. 10
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf


## 21. Proposed risk assessment and follow-up

Middle office  /  Risk analysis  /  Proposed approach

### Slide copy

- Original alert
- Company A: ratings watch. / Operating cash flow / is under pressure.
- Holdings query returns
- Product A holds / Company A bonds / Face value: RMB 20m
- Monitoring requirement
- Refresh issuer research / when a credit event occurs.
- LLM links the evidence
- Identify the issuer / Map fund exposures / Review clauses / and issuer research / Draft the assessment
- Assessment and follow-up
- Cash-flow pressure affects debt-servicing capacity. / Reassess the credit view. /  / Affected fund: Product A / Research follow-up: cash-flow trends
- Risk checks exposure and rules. Analysts update research. Portfolio managers discuss the response.

### Speaker notes

The risk team provides the alert. A holdings query returns that Product A holds Company A bonds with RMB 20m face value. The applicable example monitoring requirement calls for an issuer-research update following a credit event. The LLM identifies the issuer, maps the exposure to Product A and brings the requirement and existing research into an assessment. Cash-flow pressure is relevant to debt-servicing capacity, so the credit view needs refreshing and cash-flow trends require further research. Risk staff check holdings and clauses, analysts update their assessment, and portfolio managers discuss the response. The event, requirement, fund and amounts are illustrative.

Sources:
FUND-220, pp. 5, 10
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337837900594.pdf
FUND-300, pp. 10
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf


## 22. Processing operational documents

Back office  /  Document processing  /  Workflow

### Slide copy

- Documents received
- Operations work
- Results retained
- Faxes and scans
- Enter and check fields
- Business records
- Client update V1 / V2
- Find and interpret changes
- Change list
- Related electronic files
- Repeat the edit in each file
- Updated files
- Time goes into rekeying information and reading the context behind each change

### Speaker notes

Operations teams transcribe and check fields from faxes and scans, compare client-update versions paragraph by paragraph, and repeat common edits across related files. These tasks require both moving information between formats and reading enough context to understand each change. The peer examples cover automated data entry and document comparison. The proposed application then shows how a model can explain what a change means for the client material.


## 23. HuaAn and ICBCUBS: document processing

Back office  /  Document processing  /  Peer practices

### Slide copy

- HuaAn: automated data entry
- Read faxes and forms
- Recognize document content / Extract business fields / Support counter-service entry
- HuaAn reports that over 80% / of counter-service faxes use / automated data entry
- ICBCUBS: document comparison
- PDF, Word and scanned documents
- The model reads the content and compares versions
- V1 view
- Volume growth drove Company A's revenue. / Monitor raw-material costs.
- V2 view: new wording highlighted
- Company A’s volume growth reflects channel restocking.
- Monitor whether restocking continues and track raw-material costs.
- Visual differences, typo detection and export

### Speaker notes

HuaAn’s platform recognizes information in counter-service faxes and forms and uses it for business entry. HuaAn reported that more than 80% of these faxes used automated data entry. ICBCUBS FundGPT supports content recognition and comparison across PDF, Word and scanned documents, with visual differences, typo detection and export. The client-update example highlights the added wording on channel restocking and its persistence. The next slide builds on the identified text changes by explaining their business meaning.

Sources:
FUND-150, pp. 26–28
https://edc-book.ccf.org.cn/%E3%80%8A2025CCF%E4%BC%81%E4%B8%9A%E6%95%B0%E5%AD%97%E5%8C%96%E5%8F%91%E5%B1%95%E6%8E%A8%E8%8D%90%E6%A1%88%E4%BE%8B%E9%9B%86%E3%80%8B.pdf
FUND-312, pp. 7
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337848496316.pdf


## 24. Proposed document change analysis

Back office  /  Document processing  /  Proposed approach

### Slide copy

- Operations supplies both versions
- Quarterly client update V1 / V2
- File tools align passages
- Locate name, period and wording changes
- LLM explains what changed
- Separate new and retained information / Explain the change in meaning / Identify related materials to update
- Client update change log
- Quarterly client update V1 / V2
- Added business driver
- Channel restocking supported volume growth
- Updated monitoring priorities
- Track how long restocking lasts. / Keep monitoring raw-material costs.
- Related content to update
- The same view in other client updates / and product Q&A
- Operations checks the change log, retains it with V2 and updates related materials

### Speaker notes

Operations supplies V1 and V2 of the same quarterly client update. File tools align the passages and locate wording changes. The LLM reads them in context, distinguishes additions from retained information and explains the implications: channel restocking has been added as a driver, and its persistence has been added to the watch points while raw-material cost monitoring remains. The change log also identifies related client updates and product Q&A that need the same revision. Operations checks the explanation, retains it with V2 and updates the related material. Bosera’s bulk document-revision work provides a reference for extending the approach.

Sources:
FUND-150, pp. 26–28
https://edc-book.ccf.org.cn/%E3%80%8A2025CCF%E4%BC%81%E4%B8%9A%E6%95%B0%E5%AD%97%E5%8C%96%E5%8F%91%E5%B1%95%E6%8E%A8%E8%8D%90%E6%A1%88%E4%BE%8B%E9%9B%86%E3%80%8B.pdf
FUND-312, pp. 7
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337848496316.pdf
FUND-215, Bulk document revision
https://finance.sina.com.cn/money/fund/jjh/2026-04-30/doc-inhwfyep1330822.shtml


## 25. Turning a business request into a working tool

Back office  /  Tool development  /  Workflow

### Slide copy

- Business request: what changed between the reports? Ignore changes to repeated page headers.
- Developer: requirements
- Flag additions, deletions and edits / Ignore repeated page headers
- Developer writes code
- Read files and match paragraphs / Calculate differences and locations
- Developer: testing
- Line and page breaks disrupt matching / Header changes can cause false alerts
- A working tool requires code, test cases and repeated investigation of errors
- Client update V1 / V2

### Speaker notes

The business team wants to know what changed between two reports, excluding changes to repeated page headers. Developers turn the request into testable requirements, write code to read the files, match paragraphs and report changes, then investigate issues caused by line breaks, page breaks and repeated headers. The work moves repeatedly between the requirement, code and actual execution results. The next slides show how an LLM can support that development process.


## 26. E Fund and Invesco Great Wall: development support

Back office  /  Tool development  /  Peer practices

### Slide copy

- E Fund uses LLMs in development and testing
- Invesco Great Wall’s quant team uses local models for coding support
- Developer defines the task
- Supply examples and expected results / Specify the required behavior
- LLM drafts code and tests
- Write code to process files / List test cases and expected results
- Developer tests the result
- Run the code and check the output / Give errors back to the LLM
- Developers use generated code and tests, then iterate until the tool works
- Client update V1 / V2

### Speaker notes

E Fund has introduced LLMs into development and testing within its integrated development platform. Invesco Great Wall’s quantitative team uses local models for coding support. The report-comparison example illustrates the collaboration: the developer supplies examples and expected results, the LLM drafts processing code and test cases, and the developer runs the code, checks the result and provides errors for revision. Generated code and tests are working material for the developer to use and improve.

Sources:
FUND-101, pp. 4
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337815959196.pdf
FUND-103, Intelligent service platform
https://gifts.szu.edu.cn/info/1023/1364.htm
FUND-254, Quantitative team coding support
https://www.cls.cn/detail/2237261


## 27. Proposed software development workflow

Back office  /  Tool development  /  Proposed approach

### Slide copy

- Requirement: compare two reports, ignore repeated headers and flag changes to the body text
- 1  Developer: examples
- Client update V1 and V2 / Expected differences marked
- 2  LLM: code and tests
- Match body-text paragraphs / Generate code and tests
- 3  Test runner executes
- Body changes found / Header changes falsely flagged
- 6  Developer retests
- Review code and rerun tests / Provide the tool and guide
- 5  LLM revises the code
- Fix the repeated-header filter / Add a header-change test
- 4  Developer: feedback
- Ignore repeated headers / Keep body-text changes
- Test results

### Speaker notes

The requirement is to compare reports, ignore repeated page headers and identify changes in the body text. The developer supplies two client-update versions and expected differences. The LLM drafts the code and tests. Execution finds the body-text changes but incorrectly flags header changes. The developer explains that headers should be ignored while genuine content changes must remain. The LLM revises the header filter and adds a regression test. The developer reviews the code, reruns the tests and supplies the tool with a user guide. The test result is illustrative and shows how specific execution feedback helps the model support development.

Sources:
FUND-101, pp. 4
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337815959196.pdf
FUND-254, Quantitative team coding support
https://www.cls.cn/detail/2237261


## 28. Other back-office applications

Back office  /  Other applications

### Slide copy

- Internal services
- China Merchants Fund, Ping An Fund
- Policy and process questions
- LLM retrieves and explains
- Guidance for employees
- Email security
- Maxwealth Fund
- Email, attachments and links
- LLM assesses intent / and calls detection tools
- Security response
- Business analytics
- Method proposed in a China Universal patent
- Fund, period and metric
- LLM interprets the question / Algorithms calculate drivers
- LLM writes the analysis

### Speaker notes

China Merchants Fund and Ping An Fund use internal knowledge to answer policy, process and operational questions. LLMs retrieve and explain the relevant material. Maxwealth uses models to assess email context and intent and call detection tools for security response. A published China Universal patent proposes using an LLM to identify the fund, period and metric in a business question, with systems retrieving data and algorithms calculating drivers; the model then writes the analysis. In each case, the model interprets content while tools perform specific operations.

Sources:
FUND-351, Digital finance applications
https://fund.10jqka.com.cn/20251111/c672391490.shtml
FUND-160, Internal knowledge services
https://www.cs.com.cn/ssgs/gsxl/202602/t20260206_6537131.html
FUND-352, pp. 1–2
https://www.amac.org.cn/xwfb/hydt/202607/P020260701319545695145.pdf
FUND-227 / CN121958380A, Example 1, steps S1–S4 and report generation
https://patents.google.com/patent/CN121958380A/zh


## 29. Seven proposed applications

Proposed applications

### Slide copy

- Seven applications, with a clear result for each user
- LLMs assist with reading, comparison and drafting. People check the results and exercise judgment.

### Speaker notes

The seven proposals give each user a concrete result: sourced company analysis, a query and quote summary, a client update, review comments with reasons, a risk assessment and follow-up, a document change log, or code and tests. Research and client communications provide an initial focus. Queries and document workflows can then connect the applications to additional teams and tasks.

Sources:
FUND-300, Source text
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf
FUND-200, Source text
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337849876845.pdf
FUND-308, Source text
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337850951100.pdf
FUND-220, Source text
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337837900594.pdf
FUND-312, Source text
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337848496316.pdf
FUND-101, Source text
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337815959196.pdf


## 30. Two information flows across the firm

Cross-team collaboration

### Slide copy

- Front office
- Middle office
- Back office
- Company A
- Company research / Quote request materials
- Event assessment / Exposure monitoring
- Related documents / Version control
- Client update V1
- Review and revise to V2
- Compare versions / Update related materials
- Quarterly client update

### Speaker notes

The first information flow follows Company A. The front office prepares research and quote request material, the middle office monitors events and related exposures, and the back office maintains the associated documents. The second follows the quarterly client update: the front office drafts V1 from existing views, the middle office checks fuller current material and revises it to V2, and the back office explains the differences and updates related documents. The links show information reuse and collaboration across teams.


## 31. Shared information, models and tools

Shared capabilities

### Slide copy

- Employees provide a business question and the relevant material
- Research, inquiries, client materials, review, risk, documents and development
- LLMs work with language and content
- Interpret questions and read sources / Compare and explain content / Draft text and code
- Tools execute specific operations
- Query, calculate and process files / Run code and tests
- Shared documents, knowledge bases and business data / with access controls, source references and version history
- Model candidates include Qwen and DeepSeek, evaluated against specific tasks

### Speaker notes

Employees provide a business question and relevant material. Applications combine LLMs with the tools required for the task. The LLM interprets questions, reads sources, compares explanations and generates text or code. Tools perform queries, calculations and file operations, and execute programs and tests. Shared documents, knowledge bases and business data retain their access rights, references and versions. Qwen and DeepSeek are possible model services to evaluate against the firm’s actual tasks.

Sources:
FUND-300, pp. 5
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf
FUND-200, pp. 4–7
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337849876845.pdf
FUND-312, pp. 7
https://www.amac.org.cn/xwfb/hydt/202601/P020260202337848496316.pdf


## 32. Suggested implementation sequence

Implementation

### Slide copy

- 1
- Research and client materials
- Research, sales, / compliance and IT
- Task examples, source catalog and initial applications
- 2
- Connect trading and operations
- Trading, operations, IT
- Field definitions, query interfaces and file workflows
- 3
- Tools and internal services
- Business teams, IT
- Business tools, user guides and maintenance ownership

### Speaker notes

Research, sales, compliance and IT can first assemble task examples and source material for research and client-communication applications. Trading, operations and IT can then connect queries and document processing so that the information prepared by the model can be used in subsequent work. Development support and internal services can follow, with clear ownership for maintenance and source updates. Each phase builds on how employees actually use the preceding applications.


## 33. Measuring use and improving workflows

Evaluation

### Slide copy

- Start with research and client communications
- Baseline task
- Use the application
- Record results
- Refine the workflow
- Task completion time
- Time spent preparing, searching and delivering
- Output adoption
- Whether teams use the analysis and materials
- Rework
- Revision rounds and repeated checks
- Usage frequency
- Whether employees continue to use the application

### Speaker notes

Start with research and client communications. Compare similar tasks before and after application use, tracking completion time, output adoption, rework and repeat usage. Use the findings to identify whether the issue is missing information, an unsuitable model explanation or an awkward query or file-handling step. Continued use and reduced preparation work provide a practical basis for deciding what to improve and extend.
