"""Approved business-English revision, applied to actual authoritative native text."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parent.parent
D=json.loads((R/'src/baseline-text.json').read_text())
P=json.loads((R/'src/review-preferred-pairs.json').read_text())
review=(R.parent/'english-business-review-2026-10-26/BUSINESS-ENGLISH-REVIEW.md').read_text()
sections={int(m.group(1)):m.group(2) for m in re.finditer(r'### (\d\d)\. (.*?)(?=\n### \d\d\.|\n## Terminology)',review,re.S)}
T={i:re.search(r'\*\*Recommended title:\*\* \*\*([^*]+)\*\*',s).group(1) for i,s in sections.items()}
T[20]='Risk analysis at China Universal and Tianhong'
V1="Higher sales volumes drove Company A’s revenue growth.\nWe are monitoring raw-material costs."
V2='Channel restocking supported Company A’s sales volume growth.\nWe are monitoring whether restocking continues, alongside raw-material costs.'
OV={
2:{'scope.head0':'Inputs','scope.head2':'Outputs','scope.work2':'Query systems\nand run tasks','scope.work3':'Draft documents\nand code','scope.output1':'Quote requests\nand comparisons'},
3:{'task.files.outcome':'Extract and maintain\ndocument records','task.dev.outcome':'Develop internal\nbusiness tools','task.review.outcome':'Check claims against\nsource material','map.route2.text':'Quarterly client update: drafting, review and change tracking'},
4:{'research.evidence.3.text':'Report A: demand recovery can sustain growth.\nReport B: continued restocking is uncertain.','research.manual.2':'Compare\nresearch views'},
5:{'driver.result':'The LLM links operating drivers to earnings changes.\nAnalysts assess the quality of growth.'},
6:{'views.method.body':'Select relevant reports\nSummarize by topic\nConsolidate and review summaries','views.consensus.title':'Shared finding','views.difference.title':'Unresolved question'},
7:{'elements.stat':'Research preparation efficiency: approximately 50% higher\nReported by Zhong Ou, as of May 2026'},
8:{'research.evidence.1.text':'Revenue (RMB m): 100 / 110\nSales volume (m units): 1.0 / 1.1','research.tool.body':'Revenue: +10%\nSales volume: +10%\nAverage selling price: unchanged','research.result.text':'Higher sales volume drove revenue growth [1], with channel restocking supporting shipments [2].\nResearch views differ on whether growth is sustainable [3]. Monitor demand and input costs.','research.result.title':'Draft research summary','research.evidence.3.text':'A: demand recovery can sustain growth\nB: continued restocking is uncertain'},
9:{'trade.intent.role':'1  Define the request','trade.intent.body':'Portfolio manager\nCompany A bonds\nMaturing within two years\nCheck current holdings\nCollect offer quotes','trade.query.role':'2  Screen bonds\nand check holdings','trade.query.body':'Trader\nFind bonds and holdings\nRecord the data timestamp','trade.inquire.role':'3  Request quotes','trade.inquire.body':'Trader\nSpecify the bonds\nState buying interest\nRequest offer prices\nand available size\nReceive quotes','trade.compare.role':'4  Summarize quotes','trade.compare.body':'Trader\nSummarize bonds and quotes\nDiscuss next steps with\nthe portfolio manager','trade.system.role':'Market and\nholdings systems','trade.ask.label':'Quote request'},
10:{'trade.case1.1.body':'Interpret the request\nSelect the required tools','trade.case2.2.body':'Match the quote request\nSend details to\nthe trading system','trade.case2.1.body':'Extract bond, side,\nprice and size','trade.case1.scope':'Xiaonan supports queries, bond screening, trading instructions and notifications'},
11:{'trade.llm.query.role':'LLM identifies\nquery criteria','trade.llm.quote.role':'LLM extracts supplied\nquote details','trade.system.body':'Bond A (Company A)\nTime to maturity: 1.2 years\nCurrent holding:\nRMB 20m face value','trade.result.title':'LLM prepares a bond and quote summary','trade.user':'The trader verifies quote sources, timestamps and amounts.\nThe portfolio manager reviews the summary with the trader.'},
12:{'client.material0':'Portfolio managers’\ninvestment views','client.manual.1':'Confirm the fund\nand reporting period'},
13:{'client.views.source.text':'“Company A’s revenue rose as sales volumes increased.\nWe are watching raw-material costs.”','client.views.result.text':'Higher sales volume supported revenue growth.\nRaw-material costs remain a focus.','client.views.result.title':'Summary for client-facing teams'},
14:{'tender.llm.body':'Retrieve the process description\nIdentify responsibilities\nDraft the response','tender.answer.body':'Analysts conduct company research.\nPortfolio managers discuss the resulting investment views.\nSource: internal research process description.'},
15:{'client.input.manager':'Existing investment view\nSales volume and input costs','client.input.product':'Product information\nQ2 2026, V1','client.llm.body':'Select relevant source content\nDraft the client update'},
16:{'review.questions':'Does the draft explain the growth driver?\nDoes it preserve the source’s uncertainty?','review.reference.text':'“Channel restocking lifted sales volumes.\nWe are monitoring whether it will continue.”'},
17:{'comment.meta.role':'Fund details','comment.view.role':'Investment rationale','comment.risk.role':'Risk disclosure','comment.view.body':'Identify channel restocking as the volume driver and retain uncertainty over its continuation.','comment.risk.body':'State that the fund’s NAV can fluctuate and investors may lose capital.','review.case':'LLM-assisted review\nPenghua suggests edits based on review rules. Yingmi supports initial checks, revision and repeat review.'},
18:{'review.inputs.body':'Client update V1 and current product sources\nPresentation: restocking supported sales volume growth.\nContinued restocking remains uncertain.','review.tool.role':'Document tools locate\nrelevant information','review.tool.body':'Match fund names, reporting periods\nand source passages','review.llm.role':'LLM explains issues\nand proposes revisions','review.llm.body':'Add channel restocking as the sales volume driver\nRetain uncertainty over continued restocking\nUse the product’s specific risk wording'},
19:{'risk.question.0.body':'Query holdings\nIdentify exposed funds\nand holding amounts','risk.question.1.body':'Review contracts and internal policies\nIdentify applicable clauses'},
20:{'risk.rules.tool.role':'System links monitoring rules\nto source documents','risk.event.input.text':'Event details, comparable past events,\nindustry relationships and market sentiment'},
21:{'risk.evidence.mail.text':'Company A’s credit rating is on watch.\nOperating cash flow is under pressure.','risk.result.body':'Cash-flow pressure affects the issuer’s capacity to service debt.\nReview the credit assessment.\n\nAffected fund: Product A\nResearch follow-up: assess cash-flow trends','risk.user':'Risk staff verify exposures and requirements. Analysts update the credit assessment.\nPortfolio managers discuss the response.'},
22:{'ops.head0':'Input documents','ops.head1':'Processing tasks','ops.head2':'Outputs','ops.row2.0':'Related documents','ops.row2.1':'Apply the same revision','ops.row2.2':'Updated documents'},
23:{'ops.form.body':'Read document content\nExtract required data\nPopulate client-service records\nfrom faxes and forms','ops.stat':'HuaAn reports automated data entry for more than 80% of faxes handled by its direct-sales counter.','ops.compare.old.label':'V1 investment view','ops.compare.old.text':V1,'ops.compare.new.label':'V2 investment view: additions highlighted','ops.compare.new.line1':V2.split('\n')[0],'ops.compare.new.line2':V2.split('\n')[1]},
24:{'ops.tool.role':'Document tools match passages','ops.tool.body':'Identify changes to the fund name,\nreporting period and wording','changeLog.watch.label':'Monitoring changes','changeLog.watch.body':'Added: whether restocking continues.\nRetained: raw-material cost monitoring.','changeLog.driver.label':'Added growth driver','changeLog.driver.body':'Channel restocking supported sales volume growth','changeLog.sync.label':'Related materials','changeLog.sync.body':'Other client updates and product Q&A\nusing this investment view','ops.user':'Operations checks the change summary, files it with V2 and updates related materials.'},
25:{'dev.requirements.role':'Define requirements','dev.code.role':'Write code','dev.debug.role':'Test the tool','dev.request':'Developer workflow\nBusiness request: identify changes between the two report versions, excluding repeated page headers.'},
27:{'dev.samples.role':'1  Developer defines\nexamples','dev.generate.role':'2  LLM drafts code\nand tests','dev.test.role':'3  Test runner\nruns tests','dev.feedback.role':'4  Developer\nexplains failures','dev.revise.role':'5  LLM revises code','dev.deliver.role':'6  Developer retests','dev.test.body':'Body-text changes detected\nHeader changes incorrectly flagged','dev.feedback.body':'Exclude repeated page headers\nRetain genuine body-text changes'},
28:{'other.1.flow.1':'LLM assesses email context and intent,\nthen invokes detection tools','other.2.flow.1':'LLM interprets the question\nAlgorithms quantify contributions\nto the selected metric'},
29:{'recommend.head':'','task.files.outcome':'Operations: records and\nchange summaries'},
30:{'cross.0.0':'Company research\nBond and quote summaries','cross.0.2':'Maintain related documents\nTrack revisions','cross.1.0':'Draft client update V1','cross.1.1':'Review and revise V1 to V2'},
31:{'arch.workflow':'Applications across the seven business areas'},
32:{'phase.0.title':'Research and\nclient communications','phase.1.title':'Trading and\noperations integration','phase.2.title':'Development support\nand internal services'},
33:{'evaluation.0.body':'Time from starting the task\nto completing the output','evaluation.1.title':'Use of outputs','evaluation.3.title':'Repeat usage'}
}
# Replacements where the review groups several quoted labels in a single numbered item.
EXTRA={
3:[('Turn files into usable records','Extract and maintain document records'),('Turn requests into tools','Develop internal business tools')],
4:[('Volume (m units)','Sales volume (m units)')],
6:[('Identify common ground','Shared finding'),('Preserve the disagreement','Unresolved question')],
9:[('Ask for price and size','Request offer prices and available size')],
12:[('Previous client materials','Previous client communications')],
26:[('Give errors back to the LLM','Provide error details to the LLM')],
27:[('Add a header-change test','Add a regression test for header changes'),('Provide the tool and guide','Deliver the tool and user guide')],
}
def apply(text,pairs):
 for old,new in sorted(pairs,key=lambda x:len(x[0]),reverse=True):
  # Normalize old line breaks without flattening untouched text.
  pat=r'\s+'.join(re.escape(w) for w in old.split())
  text=re.sub(pat,lambda m:new,text)
 return text
manifest=[]
for slide in D['slides']:
 i=slide['slide'];shapes=[]
 for shape in slide['shapes']:
  key=shape['name'].removeprefix('!!');txt=shape['text']
  if key=='heading':txt=T[i]
  else:txt=apply(txt,P[str(i)]+EXTRA.get(i,[]))
  if key=='subtitle':
   txt=txt.replace('Peer practices','Industry examples').replace('Proposed approach','Proposed application').replace('Workflow','Current workflow').replace('Front office  /  Research','Front office  /  Investment research').replace('Front office  /  Client materials','Front office  /  Client communications').replace('Middle office  /  Content review','Middle office  /  Client-material review').replace('Back office  /  Tool development','Back office  /  Internal tool development')
   if i in [2,3]:txt='Application overview'
  if key=='nav.home':txt='Overview'
  if key=='clientDoc.label.view':txt='Investment view'
  if key=='clientDoc.value.view':txt=V2 if i==18 else V1
  if key=='clientDoc.value.risk' and i==18:txt='The fund’s NAV fluctuates with market conditions.\nCapital is at risk.'
  if key.endswith('.qualifier'):
   txt=txt.replace('Version check','Version comparison').replace('Change log','Change summary').replace('Dev example','Tool example')
  txt=OV.get(i,{}).get(key,txt)
  # Slide labels are fragments, not review sentences.
  if key.endswith(('.role','.title','.label')) or key.startswith(('task.','scope.','evaluation.flow','evaluation.main')):txt=txt.rstrip('.')
  shapes.append({'name':shape['name'],'source':shape['text'],'english':txt})
 notes=slide['notes']
 if isinstance(notes,list):notes='\n'.join(notes)
 notes=apply(notes,P[str(i)])
 notes=notes.replace('peer practices','industry examples').replace('peer applications','industry examples').replace('peer approaches','industry approaches').replace('seven workflows','seven application areas').replace('proposed approach','proposed application').replace('watch points','factors to monitor').replace('watch point','factor to monitor').replace('source period','reporting period').replace('change log','change summary').replace('File tools','Document tools').replace('ratings watch','credit rating on watch')
 if i==1:notes=notes.replace('how LLMs','how large language models (LLMs)')
 if i==3:notes=notes.replace('bond inquiries','quote preparation')
 if i==5:notes=notes.replace('associated manual data preparation and calculations fell','time required for manual data preparation and calculations fell')
 if i==9:notes=notes.replace('The task is to prepare','A request for quote (RFQ) asks counterparties for offer prices and available size. The task is to prepare',1)
 if i==11:notes=notes.replace('quote messages or quote request records','quote messages or quote records').replace('parses those supplied records','extracts details from those supplied records').replace('held face value is RMB 20m','the current holding is RMB 20m face value')
 if i==12:notes=notes.replace('institutional RFP responses','institutional request for proposal (RFP) responses').replace('portfolio manager views','portfolio managers’ investment views')
 if i==14:notes=notes.replace('links knowledge maintenance','supports knowledge-base maintenance')
 if i==15:notes=notes.replace('The product material supplied is the Q2 version, so the resulting document is V1.','V1 is the initial draft, prepared from the supplied Q2 product information.').replace('checks the view and submits the same update','checks the investment view and submits V1')
 if i==17:notes=notes.replace('outdated product details','the full fund name and current reporting period').replace('persistence factor to monitor','uncertainty over continued restocking');notes+='\nNAV means net asset value.'
 if i==18:notes=notes.replace('V2 adds channel restocking and its persistence','V2 identifies channel restocking as the sales volume driver and retains uncertainty over whether restocking continues')
 if i==19:notes=notes.replace('Company A is on credit rating on watch','Company A’s credit rating is on watch')
 if i==21:notes=notes.replace('Cash-flow pressure is relevant to debt-servicing capacity, so the credit view needs refreshing and cash-flow trends require further research.','Cash-flow pressure affects the issuer’s capacity to service debt. The credit assessment and cash-flow trends require further review.')
 if i==23:notes=notes.replace('counter-service faxes and forms and uses it for business entry','faxes and forms handled by its direct-sales counter and uses it to populate client-service records').replace('more than 80% of these faxes used automated data entry','more than 80% of these faxes were processed using automated data entry')
 if i==26:notes=notes.replace('uses local models','uses locally deployed models')
 if i==28:notes=notes.replace('algorithms calculating drivers','algorithms quantifying contributions to the selected metric')
 if i==29:notes=notes.replace('a query and quote summary','a bond and quote summary').replace('sourced company analysis','research summaries with source references')
 if i==30:notes=notes.replace('quote request material','bond and quote summaries').replace('the middle office checks fuller current material and revises it to V2','the author revises V1 using review findings, and the reviewer checks V2')
 if i==33:notes=notes.replace('completion time, output adoption','elapsed task completion time, use of outputs');notes+='\nTask completion time is the elapsed time from starting the task to completing the output. Repeat usage means whether employees continue to use the application.'
 # Focused reviewer residual corrections.
 if i==1:notes=notes.replace('It starts with industry examples, then develops proposed applications for the firm.','Each topic covers the current workflow, relevant industry examples and a proposed application for the firm.')
 if i==11:notes=notes.replace('The LLM extracts details from those supplied records, extracts the bond, clean price and available face value, and combines them with the system results.','The LLM extracts the bond, clean price and available face value from the supplied records, then combines these details with the system results.')
 if i==14:notes=notes.replace('supports knowledge-base maintenance, question analysis and review with RFP response generation','supports knowledge-base maintenance, question analysis, review and RFP response generation')
 if i==30:notes=notes.replace('The second follows the quarterly client update: the front office drafts V1 from existing views, the author revises V1 using review findings, and the reviewer checks V2, and the back office explains the differences and updates related documents.','The second follows the quarterly client update. The front office drafts V1 from existing views. The author revises it using review findings, and the reviewer checks V2. The back office explains the differences and updates related documents.')
 notes=notes.replace('review..','review.').replace('communications..','communications.')
 table=[['Bond / time to maturity' ,'Current holding\n(RMB m face value)','Clean price\nper RMB 100 face value','Available size\n(RMB m face value)'],['Bond A / 1.2 years','20','100.20','20']] if i==11 else None
 manifest.append({'page':i,'title':T[i],'shapes':shapes,'table':table,'notes':notes})
 if i%6==0 or i==33:
  (R/'src/business-manifest.json').write_text(json.dumps({'slides':manifest},ensure_ascii=False,indent=2))
  print(f'Saved revised copy batch through slide {i:02d}')
md=['# Revised business English copy','','Current workflow / Industry examples / Proposed application. Company A remains teal; the quarterly client update remains purple.','']
for s in manifest:
 md += [f"## {s['page']:02d}. {s['title']}",'','### Slide copy','']
 for t in s['shapes']:
  if t['english'] and not t['name'].startswith(('!!nav.','!!task.','!!heading','!!page','!!example','!!story.header.')):md.append('- '+t['english'].replace('\n',' / '))
  elif t['name'].endswith('.outcome'):md.append('- '+t['english'].replace('\n',' / '))
 if s['table']:
  md += ['']+['| '+' | '.join(row).replace('\n',' ')+' |' for row in s['table']]
 md += ['','### Speaker notes','',s['notes'],'']
(R/'ENGLISH-COPY.md').write_text('\n'.join(md))
