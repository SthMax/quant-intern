from pathlib import Path
from zipfile import ZipFile
from copy import deepcopy
from lxml import etree as E
import json,hashlib,re
from native import *
SOURCE=ROOT.parent/'static-business-2026-10-28/output/asset-management-llm-static-en.pptx'
SHA='f6df29e6361e34aa763177a67d54890e782f76bf08f474db0f9ecaecabebd5ba'
APPROVED=json.loads((ROOT/'src/approved-content.json').read_text())
BUILD=ROOT/'build';QA=BUILD/'qa'

def research_proposal(p):
    p.family='Three-source convergence, LLM/tool exchange, draft and analyst judgment'
    p.discussion='8'
    p.caption('research.scope','Company A: quarterly growth and sustainability',M,4.04,MW,12,BLUE,.55)
    p.finance('input.quarter.results',M,4.70)
    p.document('input.meeting.notes','[2] Meeting notes','Restocking lifted\nshipments',M,7.95,4.50,1.85,TEAL,11.5)
    p.document('input.research.reports','[3] Reports','A: demand recovery\ncan sustain growth\nB: continued restocking\nis uncertain',M,10.05,4.50,2.58,TEAL,10.5)
    p.node('actor.llm','LLM','Compare sources\nLink drivers\nCompare views',12.20,5.25,4.05,2.70,'llm',size=11.5)
    p.merge('flow.sources.to.llm',[(11.23,6.20),(11.23,8.875),(11.23,11.29)],11.65,(12.20,6.60),TEAL)
    p.node('tool.calculation','Tools','Revenue +10%\nSales volume +10%\nAverage price unchanged',12.20,9.30,4.45,3.20,'tool',size=11.5)
    p.line('flow.llm.calculate.request',13.10,8.02,13.10,9.20)
    p.line('flow.calculate.result.return',15.24,9.20,15.24,8.02)
    p.caption('calculate.request.label','Calculate',12.13,8.43,1.55,8.5,h=.38)
    p.caption('calculate.return.label','Result',14.62,8.43,1.55,8.5,h=.38)
    p.document('output.research.draft','Draft research view','Volume drove growth [1]\nRestocking supported shipments [2]\nSustainability: views differ [3]\nWatch demand and input costs',17.02,4.94,7.11,4.10,TEAL,12)
    p.line('flow.llm.to.research.draft',16.25,6.60,16.92,6.60)
    p.node('human.analyst.judgment','Analyst','Check sources\nTest thesis\nForm view',17.02,9.90,7.11,2.40,'human',size=11.5)
    p.line('flow.draft.to.analyst',20.57,9.10,20.57,9.80,TEAL)
    p.narration="Company A's revenue and sales volume both rose by ten percent from the prior quarter. The calculation tool establishes that average selling price was unchanged. The LLM compares that result with meeting notes and research reports. Restocking explains higher shipments, but the two reports disagree about whether growth will continue. The draft therefore distinguishes the observed volume increase from the uncertainty over continued restocking. Its source markers refer to the financials, meeting notes and research reports. The analyst checks those sources, tests the restocking thesis and forms the investment view, including follow-up on demand and input costs."

def trading_workflow(p):
    p.family='Manager/trader/system/counterparty request and return exchanges'
    p.discussion='9'
    p.document('material.manager.request','Company A bonds','Maturity: within two years\nCheck holdings\nCollect offer quotes',M,4.18,5.47,2.45,TEAL,11.5)
    p.node('actor.portfolio.manager','Portfolio manager','Define request',M,7.22,4.50,1.50,'human')
    p.node('actor.trader','Trader','Screen / request / summarize',13.20,7.22,4.30,1.50,'human',size=10.5)
    p.node('actor.market.holdings.systems','Market / holdings systems','Bonds and holdings\nData timestamp',19.17,4.18,4.96,2.20,'tool',size=11.5)
    p.node('actor.counterparty','Counterparty','Offer price\nAvailable size',19.17,10.05,4.96,2.10,'role',size=11.5)
    p.line('flow.manager.defines.request',8.98,7.12,8.98,6.73)
    p.route('flow.request.to.trader',[(12.20,5.40),(12.70,5.40),(12.70,7.57),(13.10,7.57)],TEAL)
    p.route('flow.trader.query',[(15.20,7.12),(15.20,5.05),(19.07,5.05)])
    p.caption('query.label','Query',16.35,4.53,2.3,10.5)
    p.route('flow.systems.query.result',[(21.45,6.48),(21.45,6.84),(16.18,6.84),(16.18,7.12)])
    p.caption('query.result.label','Bonds + holdings',17.10,6.29,4.80,10)
    p.route('flow.trader.requests.offers',[(17.60,7.65),(18.45,7.65),(18.45,10.55),(19.07,10.55)])
    p.caption('offer.request.label','Request offers',15.20,9.54,2.60,9.5)
    p.route('flow.counterparty.returns.quotes',[(19.07,11.28),(17.95,11.28),(17.95,8.30),(17.60,8.30)])
    p.caption('offer.return.label','Offer quotes',15.18,11.35,2.60,9.5)
    p.route('flow.trader.summary.to.manager',[(14.22,8.82),(14.22,9.56),(8.98,9.56),(8.98,8.82)])
    p.caption('summary.return.label','Bond / quote summary',10.0,9.78,5.8,10.5)
    p.caption('work.repetition','Repeated filters, system switches and message copying',M,12.02,MW,10.5,GRAY,.5)
    p.narration="The portfolio manager asks the trader to identify Company A bonds maturing within two years, check the portfolio's holdings and collect offer quotes. The trader queries market and holdings systems, records the data timestamp and then specifies the bonds and buying interest to counterparties. Counterparties return offer prices and available size. The trader summarizes the bonds and received quotes and discusses the next step with the portfolio manager. The trader and existing systems perform these steps in the current workflow. Repeated entry of filters, switching between systems and copying quote messages are the work to be addressed by the later proposal."

def batch_one(p):
    i=p.i
    if i==1:
        p.family='Opening context and business scene';p.discussion='1'
        q=deepcopy(p.source.find('.//p:pic',NS));p.id+=1;nv=q.find('./p:nvPicPr/p:cNvPr',NS);nv.set('id',str(p.id));nv.set('name','cover.business.scene');p.tree.append(q)
        p.caption('cover.scope','Mainland asset management',L,4.45,10.40,16,BLUE,.8)
        p.caption('cover.date','October 2026',L,10.80,10.40,13,GRAY,.6)
        p.narration="This report considers where large language models could support employee work in a mainland asset manager. It follows employee work through the front office, middle office and back office. Industry examples show what peer institutions have reported. The company proposals then identify supplied information, the LLM's particular contribution, the operations performed by tools and the colleagues who use the output. Two examples recur throughout the report: Company A and a quarterly client update."
    elif i==2:
        p.family='Aggregate inputs, LLM/tool exchange and output fan-out';p.discussion='2'
        ys=[4.30,6.15,8.00,9.85]
        for j,(lab,y) in enumerate(zip(['Documents','Data','Messages','Business requests'],ys)):
            p.node('input.family.'+str(j),lab,'',M,y,4.50,1.25,'material')
        p.node('actor.llm','LLM','Read / compare\nExplain / draft',12.20,5.65,4.05,2.35,'llm')
        p.node('tool.operations','Tools','Retrieve / query\nCalculate / run',12.20,9.55,4.05,2.30,'tool')
        p.merge('flow.inputs.merge',[(11.23,y+.625) for y in ys],11.65,(12.20,6.825))
        for j,(lab,y) in enumerate(zip(['Company analysis','Quote requests / comparisons','Client materials','Business tools'],ys)):
            p.node('output.family.'+str(j),lab,'',17.02,y,7.11,1.25,'material')
        p.line('flow.llm.output.bus',16.25,6.825,16.65,6.825,arrow=False)
        p.line('flow.output.bus',16.65,4.925,16.65,10.475,arrow=False)
        for j,y in enumerate(ys):p.line('flow.output.fanout.'+str(j),16.65,y+.625,16.92,y+.625)
        p.line('flow.llm.tool.request',13.10,8.10,13.10,9.45);p.line('flow.tool.llm.result',15.24,9.45,15.24,8.10)
        p.caption('tool.request.label','Request',12.15,8.65,1.5,8.5,h=.35);p.caption('tool.result.label','Result',14.65,8.65,1.5,8.5,h=.35)
        p.caption('scope.purpose','Specific employee tasks determine the application',M,12.18,MW,11,BLUE,.48)
        p.narration="Documents, data, messages and business requests supply the information for different employee tasks. Depending on the task, an LLM retrieves and organizes information, calculates and explains results with tools, queries systems and runs tasks, or drafts documents and code. The distinction on this page is functional: the LLM reads, compares, explains and drafts, while tools retrieve data, query systems, perform calculations and execute operations. These combinations can produce company analysis, quote requests and comparisons, client materials and internal business tools. The proposals address specific employee tasks."
    elif i==3:
        p.family='Firm hierarchy and seven task nodes';p.discussion='3'
        p.node('firm.root','Asset management firm','',9.15,4.04,7.10,.95,'llm')
        p.line('firm.trunk',12.70,5.00,12.70,5.38,arrow=False);p.line('firm.branch',4.825,5.38,20.575,5.38,arrow=False)
        groups=[('Front office',[('Research','Company analysis'),('Trading support','Quote requests'),('Client materials','Client communications')]),('Middle office',[('Content review','Source-based checks'),('Risk analysis','Exposure / impact')]),('Back office',[('Document processing','Records / revisions'),('Tool development','Internal business tools')])]
        for j,(office,tasks) in enumerate(groups):
            x=[1.27,9.15,17.02][j];w=[7.11,7.10,7.11][j];p.line('firm.office.branch.'+str(j),x+w/2,5.38,x+w/2,5.64,arrow=False)
            p.node('firm.office.'+str(j),office,'',x,5.72,w,.95,'llm')
            for k,(task,outcome) in enumerate(tasks):p.node('firm.task.'+str(j)+'.'+str(k),task,outcome,x,6.98+k*1.21,w,1.06,'material',size=10.5)
        p.node('story.issuer','Company A','Research / trading / risk / operations',1.27,11.36,10.93,1.15,'issuer',size=10.5)
        p.node('story.client','Quarterly client update','Drafting / review / change tracking',13.20,11.36,10.93,1.15,'client',size=10.5)
        p.narration="The seven application areas follow the firm's existing work. Front-office topics are research, trading support and client materials. Middle-office topics are content review and risk analysis. Back-office topics are document processing and tool development. Research prepares company analysis, trading support prepares quote requests, and client-facing teams prepare communications. Reviewers check claims against source material, risk teams link events to exposures, operations maintains document records and developers build internal tools. Company A connects the research, trading, risk and operations examples. The quarterly client update connects drafting, review and revision tracking. These tasks connect the firm's front, middle and back offices."
    elif i==4:
        p.family='Three research sources into analyst preparation and a research view';p.discussion='4'
        p.finance('research.source.financials',M,4.18)
        p.document('research.source.meeting','Meeting notes','Restocking lifted\nshipments.\nAssess continuation.',12.20,4.18,4.05,3.1,TEAL,10.5)
        p.document('research.source.reports','Two research reports','A: demand recovery can\nsustain growth.\nB: continued restocking\nis uncertain.',17.02,4.18,7.11,3.1,TEAL,11.5)
        for x,yy in [(8.98,7.18),(14.225,7.28),(20.575,7.28)]:p.line('source.collection.'+str(x),x,yy,x,7.65,TEAL,.75,False)
        p.line('research.collection.bus',8.65,7.65,20.575,7.65,TEAL,.75,False);p.line('research.collection.to.analyst',8.65,7.65,8.65,8.35,TEAL)
        p.caption('analyst.sequence.label','Analyst preparation',11.25,7.92,12.88,11.5,BLUE,.45)
        xs=[6.73,11.25,15.77,20.29];labs=['Find sources','Extract / calculate','Compare views','Record reasoning']
        for j,(x,lab) in enumerate(zip(xs,labs)):
            p.node('analyst.action.'+str(j),lab,'',x,8.50,3.84,1.45,'human')
            if j<3:p.line('analyst.sequence.'+str(j),x+3.91,9.225,xs[j+1]-.10,9.225)
        p.node('output.research.view','Research view','Is growth sustainable?',12.20,10.90,7.10,1.52,'issuer',size=11.5)
        p.route('analysis.to.view',[(22.21,10.02),(22.21,11.66),(19.40,11.66)],TEAL)
        p.narration="The analyst asks what drove Company A's revenue growth and whether that growth is sustainable. The financial table compares the prior and current quarter: revenue rises from RMB100 million to RMB110 million, while sales volume rises from 1.0 million to 1.1 million units. Meeting notes identify restocking as a shipment driver. One research report considers demand recovery sufficient to sustain growth, while the other considers continued restocking uncertain. The analyst must find relevant sources, extract data and calculate changes, compare these views and record the reasoning. Repeated searching, extraction and checking take time away from assessing the business. This page describes the existing human workflow, before introducing an LLM proposal."
    elif i==5:
        p.family='Earnings decomposition with tool support and analyst judgment';p.discussion='5'
        p.node('role.llm.structure','LLM structures the analysis','Link operating drivers to earnings changes',M,4.10,MW,1.18,'llm',size=11.5)
        p.node('analysis.net.profit','Change in net profit','',M,7.09,3.40,1.45,'llm')
        p.line('earnings.trunk',10.70,6.40,10.70,10.0,arrow=False);p.line('earnings.root.link',10.13,7.815,10.70,7.815,arrow=False)
        rows=[('Revenue','Volume / price',5.80),('Cost of sales','Materials / production',7.60),('Expenses','Distribution / selling',9.40)]
        for j,(a,b,y) in enumerate(rows):
            p.line('earnings.branch.'+str(j),10.70,y+.60,11.10,y+.60,arrow=False)
            p.node('earnings.category.'+str(j),a,'',11.10,y,3.30,1.20,'material')
            p.line('earnings.driver.link.'+str(j),14.40,y+.60,15.15,y+.60,arrow=False)
            p.node('earnings.driver.'+str(j),b,'',15.25,y,4.55,1.20,'material',size=11.5)
        p.node('tool.data.calculation','Data / calculation tools','Retrieve data\nCalculate changes',20.57,5.80,3.56,4.80,'tool',size=11)
        p.line('tool.support.entry',20.47,8.20,20.12,8.20,arrow=False);p.line('tool.support.bus',20.12,6.40,20.12,10.00,arrow=False)
        for j,y in enumerate([6.40,8.20,10.00]):p.line('tool.driver.support.'+str(j),20.12,y,19.90,y,GRAY,.75,True)
        p.node('human.analyst.quality','Analyst assesses quality of growth','',11.10,11.45,13.03,1.00,'human')
        p.shape('analysis.driver.structure',M,5.55,13.25,5.30,None,RULE,.5)
        p.line('analysis.to.quality',13.355,10.95,13.355,11.35)
        p.narration="Tianhong's reported approach separates structuring the analysis from obtaining data and making the investment judgment. The LLM organizes a change in net profit into revenue, cost of sales and expenses, then links those categories to operating drivers. Revenue depends on sales volume and selling price; materials and production costs affect cost of sales; distribution and selling costs affect expenses. Data feeds and calculation tools supply the evidence and numerical work. The decomposition connects each earnings category to its operating evidence. Analysts use the driver analysis to assess the quality and sustainability of earnings growth."
    elif i==6:
        p.family='Two hypotheses merge into comparison and split into shared/open findings';p.discussion='6'
        p.document('source.report.a','Report A','Higher volume lifted\nrevenue.\nDemand recovery can\nsustain growth.',M,4.25,4.50,3.05,TEAL,11)
        p.document('source.report.b','Report B','Restocking lifted\nshipments.\nContinued restocking\nremains uncertain.',M,8.15,4.50,3.05,TEAL,11)
        p.node('role.llm.compare','LLM compares views','Find agreement\nIdentify difference',12.20,6.40,4.05,2.20,'llm',size=11.5)
        p.merge('reports.to.comparison',[(11.23,5.775),(11.23,9.675)],11.65,(12.20,7.50),TEAL)
        p.node('output.shared.finding','Shared finding','Higher volumes\nsupported revenue',17.02,4.75,7.11,2.05,'issuer')
        p.node('output.open.question','Open question','Is volume growth\nsustainable?',17.02,8.05,7.11,2.05,'issuer')
        p.line('comparison.findings.entry',16.25,7.50,16.65,7.50,arrow=False);p.line('comparison.findings.bus',16.65,5.775,16.65,9.075,arrow=False)
        p.line('comparison.shared',16.65,5.775,16.92,5.775);p.line('comparison.open',16.65,9.075,16.92,9.075)
        p.node('human.analyst.investigates','Analyst investigates disagreement','',17.02,11.22,7.11,1.12,'human')
        p.line('open.to.analyst',20.57,10.20,20.57,11.12)
        p.route('analyst.source.check.return',[(20.575,12.44),(20.575,12.50),(6.48,12.50),(6.48,5.775)],GRAY,.7,False)
        p.line('analyst.check.report.a',6.48,5.775,6.63,5.775,GRAY,.7)
        p.line('analyst.check.report.b',6.48,9.675,6.63,9.675,GRAY,.7)
        p.caption('source.check.label','Source check',12.15,12.00,4.5,9.5)
        p.narration="Fullgoal uses LLMs to compare reports addressing a common research question. The workflow selects relevant reports, summarizes them by topic, then consolidates and reviews the summaries. In this illustration, the reports agree that higher volumes supported revenue. Their disagreement concerns sustainability: one points to demand recovery, while the other sees uncertainty over continued restocking. The useful output is therefore both an agreed finding and an unresolved question, with links back to source material. Analysts investigate the disagreement in the original reports and form their research view."
    elif i==7:
        p.family='Source material populates a structured research template and human check';p.discussion='7'
        for j,(title,body,y) in enumerate([('Financials','Data / calculations',4.40),('Meeting notes','Restocking context',6.55),('Research reports','Continuation question',8.70)]):p.node('source.template.'+str(j),title,body,M,y,4.0,1.65,'issuer',size=10.5)
        p.node('role.llm.populate','LLM','Populate template',11.43,6.55,4.00,2.05,'llm')
        p.merge('template.sources.merge',[(10.73,5.225),(10.73,7.375),(10.73,9.525)],11.08,(11.43,7.575),TEAL)
        p.document('output.research.template','Research template','',16.25,4.40,7.88,5.92,TEAL)
        for j,(label,val) in enumerate([('Operating performance','Sales volume up 10%'),('Business driver','Restocking lifted shipments'),('Open question','Will restocking continue?')]):
            yy=5.62+j*1.40;p.text('template.field.'+str(j),label,16.52,yy,7.33,.50,10.5,True,BLUE);p.text('template.value.'+str(j),val,16.52,yy+.57,7.33,.63,12)
            if j<2:p.line('template.row.rule.'+str(j),16.52,yy+1.25,23.86,yy+1.25,RULE,.5,False)
        p.line('llm.to.template',15.53,7.575,16.15,7.575)
        p.node('human.analyst.template.check','Analyst','Check entries / add assessment',16.25,11.13,7.88,1.30,'human',size=10.5)
        p.line('template.to.analyst',20.19,10.42,20.19,11.03,TEAL)
        p.text('evidence.efficiency',[{'text':'Approximately 50% higher','size':13,'bold':True,'color':BLUE},{'text':'Research-preparation efficiency','size':10,'color':INK},{'text':'Reported by Zhong Ou, May 2026','size':9.5,'color':GRAY}],M,11.04,8.82,1.45)
        p.narration="Zhong Ou reports using LLMs to populate research templates from source material. Financials and calculations support the operating-performance entry, meeting notes support the business-driver entry, and research reports identify an open question. The illustrative template records a ten-percent increase in sales volume, restocking as the shipment driver, and the question of whether restocking will continue. The analyst checks the entries against their sources and adds an independent assessment. The reported approximately fifty-percent improvement concerns research-preparation efficiency, as reported by Zhong Ou as of May 2026."
    elif i==10:
        p.family='Two attributed trading support lanes';p.discussion='10'
        xs=[M,11.25,15.77,20.29];ww=[3.70,3.70,3.70,3.84]
        lanes=[('Southern / Xiaonan',4.18,[('User request','Bond query / task','role'),('LLM','Interpret / select tools','llm'),('Systems','Run / return result','tool'),('User','Review / confirm','human')]),('Aegon-Industrial / Qtrade',8.02,[('Qtrade records','Bond / side\nPrice / size','material'),('AI','Extract fields','llm'),('Match / route','Match request\nRoute details','tool'),('Trading system','Receive details','tool'),('Portfolio manager','Submit instruction','human')])]
        for row,(label,y,nodes) in enumerate(lanes):
            p.caption('peer.label.'+str(row),label,M,y,MW,12.5,BLUE,.60)
            px=xs if row==0 else [6.73,10.355,13.98,17.605,21.23];pw=ww if row==0 else [2.90]*5
            for j,(title,body,kind) in enumerate(nodes):
                p.node('peer.'+str(row)+'.step.'+str(j),title,body,px[j],y+.90,pw[j],2.10 if row==0 else 2.60,kind,size=10.5)
                if j<len(nodes)-1:p.line('peer.'+str(row)+'.flow.'+str(j),px[j]+pw[j]+.08,y+1.95,px[j+1]-.10,y+1.95)
        p.caption('xiaonan.scope','Queries / screening / instructions / notifications',M,7.35,MW,10.5,GRAY,.45)
        p.narration="Southern Asset Management's Xiaonan trading assistant supports queries, bond screening, trading instructions and notifications. The user supplies a request; the LLM interprets it and selects tools; systems perform the task and return a result; the user reviews the data and confirms the next step. Aegon-Industrial's reported use is different: AI extracts bond, side, price and size from Qtrade records, matches the relevant quote request and routes details to the trading system. The portfolio manager then submits the instruction. Systems execute requests, AI interprets language or extracts fields, and colleagues review results and submit instructions."
    elif i==11:
        p.family='Request and trader-supplied quote paths merge into native result table';p.discussion='11'
        p.document('input.bond.request','Manager request','Company A / buy\nWithin two years',M,4.18,4.96,2.50,TEAL,12)
        p.node('role.llm.criteria','LLM criteria','Issuer / side / maturity',12.20,4.18,4.05,2.50,'llm',size=11)
        p.node('tool.holdings.result','Systems result','Bond A: 1.2 years\nHolding: RMB 20m\nface value',17.02,4.18,7.11,2.50,'tool',size=11.5)
        p.line('request.to.criteria',11.79,5.43,12.10,5.43,TEAL)
        p.line('criteria.query',16.35,5.06,16.92,5.06);p.line('systems.return',16.92,6.05,16.35,6.05)
        p.document('input.trader.quote','Quote from trader','Bond A: 100.20\nAvailable: RMB 20m face',M,6.87,4.96,1.75,TEAL,10.5)
        p.node('role.llm.quote.extraction','LLM extracts','Bond / price / size',12.20,6.87,4.05,1.75,'llm',size=10.5)
        p.line('quote.to.extraction',11.79,7.745,12.10,7.745,TEAL)
        p.text('role.llm.common.summary','LLM prepares the summary',M,8.75,MW,.50,12,True,BLUE,align='ctr',anchor='ctr',fill='EAF3FA',line=BLUE,pad=.02)
        p.line('quote.fields.to.summary',14.225,8.66,14.225,8.72)
        p.line('holdings.to.summary',20.575,6.78,20.575,8.72)
        p.caption('holdings.path.label','Holdings',21.0,8.12,3.0,10.5)
        p.table(M,9.30,MW)
        p.text('human.trader.verifies','Trader verifies',M,12.18,7.10,.47,11,True,INK,anchor='ctr',fill=LIGHT,line=GRAY,pad=.03)
        p.text('human.manager.reviews','Manager reviews with trader',15.12,12.18,9.01,.47,11,True,INK,anchor='ctr',fill=LIGHT,line=GRAY,pad=.03)
        p.line('table.to.trader',10.28,12.02,10.28,12.13);p.line('trader.to.manager.review',13.93,12.415,15.02,12.415)
        p.narration="The portfolio manager asks for Company A bonds on the buy side, maturing within two years, with current holdings checked and offer quotes collected. The LLM identifies query criteria and systems return Bond A, which matures in 1.2 years, together with the current RMB 20 million face-value holding. The second input is separate: the trader supplies the received quote. The LLM extracts Bond A, a clean price of 100.20 per RMB 100 face value, and RMB 20 million face value available. It combines those fields in the summary table, retaining different columns for current holdings and available size. The trader verifies quote sources, timestamps and amounts; the portfolio manager reviews the summary with the trader. The trader supplies the received quote records and the LLM extracts their details."
    else:return False
    return True

def batch_two(p):
    i=p.i
    if i==12:
        p.family='Client question and source families into human preparation and client material';p.discussion='12'
        p.node('input.client.question','Client question','Company A\nWhat changed?\nWhat to watch?',M,4.18,4.50,2.35,'client',size=11)
        for j,(title,body,y) in enumerate([('PM views','Investment views',6.78),('Product sources','Fund / period',8.43),('Previous updates','Client wording',10.08)]):p.node('input.client.source.'+str(j),title,body,M,y,4.50,1.40,'client',size=10.5)
        p.node('actor.relationship.manager','Relationship manager','Select / check\nAdapt',12.20,6.20,4.05,2.85,'human',size=11.5)
        p.merge('client.sources.merge',[(11.23,5.355),(11.23,7.48),(11.23,9.13),(11.23,10.78)],11.65,(12.20,7.625),PURPLE)
        p.document('output.quarterly.update','Quarterly update','Company A\nQuarterly explanation',17.02,5.45,7.11,2.80,PURPLE,12)
        p.node('output.related.responses','Related responses','Product Q&A / RFPs',17.02,9.80,7.11,1.80,'material')
        p.line('client.output.entry',16.25,7.625,16.65,7.625,arrow=False);p.line('client.output.branch',16.65,6.85,16.65,10.70,arrow=False)
        p.line('client.output.update',16.65,6.85,16.92,6.85,PURPLE);p.line('client.output.related',16.65,10.70,16.92,10.70)
        p.narration="A client relationship manager prepares a quarterly update using portfolio managers' investment views, product documentation and previous client communications. The client wants to know what changed in Company A's business during the quarter and what to watch next. The manager selects the relevant views, confirms the fund and reporting period and adapts the explanation to the client's questions. The same sources also support product questions and institutional RFP responses. Searching for the relevant material and repeating the checks for each update are the preparation work to be addressed by the later drafting proposal."
    elif i==13:
        p.family='Multi-source consolidation into client-facing summary and use';p.discussion='13'
        for j,(title,y) in enumerate([('Presentations',4.35),('Commentary',6.55),('Research reports',8.75)]):p.document('input.views.'+str(j),title,'',M,y,4.50,1.50,GRAY)
        p.node('role.llm.consolidates','LLM','Find\nDeduplicate\nSummarize',12.20,6.15,4.05,2.70,'llm')
        p.merge('views.sources.merge',[(11.23,5.10),(11.23,7.30),(11.23,9.50)],11.65,(12.20,7.50))
        p.document('output.client.summary','Client-team summary','Company A\nHigher sales volume\nsupported revenue growth.\nRaw-material costs\nremain a focus.',17.02,4.70,7.11,4.60,PURPLE,12)
        p.line('llm.client.summary',16.25,7.50,16.92,7.50,PURPLE)
        p.node('human.client.team','Client-facing team','Use summary',17.02,10.35,7.11,1.80,'human')
        p.line('summary.to.team',20.575,9.40,20.575,10.25,PURPLE)
        p.caption('related.commentary.scope','Weekly sector views / daily market commentary',M,11.80,9.70,10.5,GRAY,.5)
        p.narration="Tianhong uses LLMs to consolidate recent investment views by portfolio manager or product. Presentations, commentary and reports may contain overlapping explanations. The LLM finds the relevant views, removes duplication and prepares a clear summary for client-facing colleagues. In the recurring Company A example, higher sales volume supported revenue growth and raw-material costs remain a focus. The client-facing team uses the summary with its source basis available for checking. Tianhong also applies the approach to weekly sector views and daily market commentary."
    elif i==14:
        p.family='Question and internal process source into a traceable RFP answer';p.discussion='14'
        p.document('input.rfp.question','Client question','How is investment\nresearch organized?',M,4.35,4.50,2.20,GRAY,11.5)
        p.document('input.internal.process','Internal process','',M,7.25,4.50,3.35,GRAY)
        for j,(t,y) in enumerate([('Analyst',8.12),('Company research',8.90),('PM discussion',9.68)]):
            p.text('process.source.step.'+str(j),t,M+.20,y,4.10,.52,10.5,True,INK,align='ctr',fill=LIGHT,line=GRAY,pad=.02)
            if j<2:p.line('process.source.link.'+str(j),M+2.25,y+.57,M+2.25,y+.73,GRAY,.65)
        p.node('role.llm.rfp','LLM','Retrieve\nIdentify roles\nDraft',12.20,6.25,4.05,2.65,'llm',size=11.5)
        p.merge('rfp.inputs.merge',[(11.23,5.45),(11.23,8.925)],11.65,(12.20,7.575))
        p.document('output.rfp.response','Draft RFP response','Analysts conduct company research.\nPortfolio managers discuss the resulting investment views.\n\nSource: internal research process description.',17.02,4.35,7.11,5.75,BLUE,11.5)
        p.line('rfp.draft.flow',16.25,7.575,16.92,7.575)
        p.node('human.rfp.business.check','Business team','Check / tailor answer',17.02,10.95,7.11,1.50,'human',size=11.5)
        p.line('rfp.answer.check',20.575,10.20,20.575,10.85)
        p.narration="ICBCUBS FundGPT supports knowledge-base maintenance, question analysis, review and RFP drafting. An institutional client asks how investment research is organized. The supplied internal process description identifies analysts' company research and portfolio managers' discussion of the resulting view. The LLM retrieves that description, identifies responsibilities and drafts a response with a source reference. The business team checks the answer and its source, then addresses the client's specific requirements. This independent RFP example uses the same source-backed drafting principle as other client-material tasks."
    elif i==15:
        p.family='Three supplied inputs into LLM selection/drafting, V1 evidence and client-team check';p.discussion='15'
        for j,(title,body,y,h) in enumerate([('Client question','What matters this quarter?',4.30,1.80),('Investment view','Sales volume / input costs',6.55,1.80),('Product source','Q2 2026 / V1',8.80,1.80)]):p.document('input.drafting.'+str(j),title,body,M,y,4.0,h,PURPLE,10.5)
        p.node('role.llm.drafting','LLM','Select sources\nDraft update',11.43,6.60,4.05,2.55,'llm')
        p.merge('draft.inputs.merge',[(10.73,5.20),(10.73,7.45),(10.73,9.70)],11.08,(11.43,7.875),PURPLE)
        p.client_evidence('output.client.v1',16.25,4.30,7.88,6.45,1,True,True,False,12)
        p.line('llm.to.v1',15.48,7.875,16.15,7.875,PURPLE)
        p.node('human.client.submission','Client team: check / submit V1','',16.25,11.35,7.88,1.00,'human')
        p.line('v1.to.client.check',20.19,10.85,20.19,11.25,PURPLE)
        p.narration="The author supplies the client's question, the existing investment view and the relevant product information. The LLM selects source content and drafts the quarterly client update. V1 records the shorter fund name, the Q2 product-information source, the existing view that sales volume drove revenue growth and raw-material costs remain under monitoring, and the generic risk sentence. These fields create the material that colleagues will review next. The client team checks the investment view and submits V1 for review. The author retains responsibility for the supplied context and the draft's use with the client."
    elif i==16:
        p.family='V1 and current-source claims into human comparison and explicit missing elements';p.discussion='16'
        p.document('evidence.v1.view','V1 investment view','Higher sales volumes drove Company A’s revenue growth.\nWe are monitoring raw-material costs.',M,4.30,7.11,4.15,PURPLE,12)
        p.document('evidence.pm.source','Current PM source','Channel restocking lifted sales volumes.\nWe are monitoring whether it will continue.',17.02,4.30,7.11,4.15,GRAY,12)
        p.line('review.focus.v1',M+.10,5.17,M+.10,7.70,GRAY,2,False)
        p.line('review.focus.source',17.12,5.17,17.12,7.70,GRAY,2,False)
        for x in [10.285,20.575]:p.route('comparison.input.'+str(x),[(x,8.55),(x,8.90),(15.43,8.90)],GRAY,.75,False)
        p.node('human.reviewer.compares','Reviewer compares','Growth driver included?\nUncertainty retained?',12.20,9.30,6.46,1.90,'human',size=11.5)
        p.line('claims.to.reviewer',15.43,8.90,15.43,9.20)
        p.text('finding.driver','Restocking driver absent',M,11.78,8.15,.66,11.5,True,INK,anchor='ctr',fill=LIGHT,line=GRAY,pad=.05)
        p.text('finding.uncertainty','Continuation uncertainty absent',15.62,11.78,8.51,.66,11.5,True,INK,anchor='ctr',fill=LIGHT,line=GRAY,pad=.05)
        p.line('comparison.findings.trunk',15.43,11.30,15.43,11.55,arrow=False)
        p.line('comparison.findings.fork',10.805,11.55,19.875,11.55,arrow=False)
        p.line('comparison.finding.driver',10.805,11.55,10.805,11.68)
        p.line('comparison.finding.uncertainty',19.875,11.55,19.875,11.68)
        p.narration="The reviewer compares the client's V1 investment view with the current portfolio-manager presentation. V1 states the observed sales-volume increase and retains raw-material-cost monitoring. The current source adds the specific driver, channel restocking, and uncertainty about its continuation. The review therefore asks whether the draft explains the growth driver and preserves the source's uncertainty. Fund details, source version and risk disclosure are also checked against current material. Reviewers check the draft’s statements against current sources."
    elif i==17:
        p.family='Source/rule-based LLM review, three explained findings and author/recheck loop';p.discussion='17'
        p.document('input.review.v1','V1 material','Fund / source\nInvestment view / risk',M,4.30,4.50,1.90,PURPLE,11)
        p.document('input.review.rules','Sources / rules','Current product sources\nReview requirements',M,6.70,4.50,2.15,GRAY,11)
        p.node('role.llm.review','LLM review','Explain suggested edits',12.20,5.55,4.05,2.10,'llm',size=11)
        p.merge('review.inputs.merge',[(11.23,5.25),(11.23,7.775)],11.65,(12.20,6.60))
        p.caption('peer.penghua','Penghua: suggested edits',12.20,4.47,4.65,10.5,BLUE,.5)
        vals=[('Fund / period','Full fund name\nCurrent reporting period',4.20),('Investment rationale','Restocking driver\nContinuation uncertainty',6.45),('Risk wording','NAV fluctuation\nCapital at risk',8.70)]
        for j,(title,body,y) in enumerate(vals):p.node('output.review.finding.'+str(j),title,body,17.02,y,7.11,1.85,'material',size=11)
        p.line('review.findings.entry',16.25,6.60,16.65,6.60,arrow=False);p.line('review.findings.bus',16.65,5.125,16.65,9.625,arrow=False)
        for j,y in enumerate([5.125,7.375,9.625]):p.line('review.finding.branch.'+str(j),16.65,y,16.92,y)
        p.shape('review.findings.group',16.85,4.04,7.28,6.67,None,RULE,.5)
        p.caption('peer.yingmi','Yingmi\nReview / revision /\nrepeat review',M,9.55,4.50,10.5,BLUE,1.45)
        p.node('human.author.revises','Author revises','',12.20,11.30,4.05,1.10,'human')
        p.node('human.review.recheck','Repeat review','',17.02,11.30,7.11,1.10,'human')
        p.route('findings.to.author',[(20.49,10.81),(20.49,10.98),(14.225,10.98),(14.225,11.20)])
        p.line('author.to.recheck',16.35,11.85,16.92,11.85)
        p.route('recheck.return',[(20.575,12.45),(20.575,12.55),(11.43,12.55),(11.43,7.30),(12.10,7.30)],GRAY,.7)
        p.narration="Penghua's reported use suggests edits using review rules. Yingmi's reported scope includes initial checks, revision and repeat review. Applied to the client-update example, the findings explain three issues: the full fund name and current reporting period, the restocking growth driver and uncertainty over continuation, and the product's specific NAV and capital-risk wording. The author revises the material and a repeat review checks the changes. Penghua's reported ninety-one percent figure concerns acceptance of suggested edits. Authors revise the material and reviewers check the changes again."
    elif i==18:
        p.family='Small V1/current sources through matching and explanation into exact V2 evidence and approval';p.discussion='18';p.custom.append('Output paper14.80–24.13 provides9.33cm for the complete two-sentence V2 evidence; left source/matching region6.73–10.80 and LLM11.43–14.23 retain the handoff.')
        p.document('input.revision.v1','V1 material','Q2 product source',M,4.30,4.07,1.60,PURPLE,10.5)
        p.document('input.revision.source','Current source','Restocking lifted volume\nContinuation uncertain',M,6.25,4.07,2.65,GRAY,10.5)
        p.node('tool.document.matching','Document tools','Match passages',M,9.40,4.07,1.70,'tool',size=11.5)
        p.merge('revision.sources.collect',[(10.80,5.10),(10.80,7.575)],11.10,(11.10,8.99),GRAY)
        p.route('collected.to.matching',[(11.10,8.99),(8.765,8.99),(8.765,9.30)],GRAY)
        p.node('role.llm.revisions','LLM','Explain\nPropose edits',11.43,9.40,2.80,2.05,'llm',size=11)
        p.line('matching.to.explanation',10.90,10.25,11.33,10.25)
        p.client_evidence('output.client.v2',14.80,4.30,9.33,7.15,2,True,False,True,12)
        p.line('explanation.to.v2',14.33,10.25,14.70,10.25,PURPLE)
        p.text('human.author.approves','Author approves',14.80,11.85,4.10,.62,11.5,True,INK,anchor='ctr',fill=LIGHT,line=GRAY,pad=.04)
        p.text('human.reviewer.checks','Reviewer checks',20.10,11.85,4.03,.62,11.5,True,INK,anchor='ctr',fill=LIGHT,line=GRAY,pad=.04)
        p.route('v2.to.approval',[(19.465,11.55),(19.465,11.70),(16.85,11.70),(16.85,11.80)],PURPLE)
        p.line('approval.to.check',19.00,12.16,20.00,12.16)
        p.narration="The author supplies V1 and current sources. The presentation states that restocking supported sales-volume growth and that continued restocking remains uncertain. Document tools match fund names, reporting periods and source passages. The LLM then explains the mismatches and proposes revisions. V2 adds the restocking driver, retains uncertainty over whether restocking continues and keeps raw-material-cost monitoring. It also uses the full fund name, the Q3 product source and the product's specific risk disclosure. The author approves the edits and the reviewer checks the sources, rationale and revised update."
    elif i==19:
        p.family='Company A alert prompts parallel human evidence collection and assessment';p.discussion='19'
        p.node('input.risk.alert','Company A alert','Credit rating on watch\nOperating cash flow under pressure',M,4.25,MW,1.80,'issuer',size=12)
        p.node('human.risk.analyst','Risk analyst','Gather evidence',M,7.00,4.50,1.65,'human')
        for j,(title,body,y) in enumerate([('Holdings','Exposed funds?',6.60),('Contracts / policies','Applicable rules?',8.72),('Issuer research','Event impact?',10.84)]):p.node('source.risk.'+str(j),title,body,12.20,y,4.05,1.65,'material',size=10.5)
        p.line('alert.to.analyst',8.98,6.15,8.98,6.90,TEAL)
        p.line('analyst.evidence.entry',11.33,7.825,11.65,7.825,arrow=False);p.line('analyst.evidence.branch',11.65,7.425,11.65,11.665,arrow=False)
        for j,y in enumerate([7.425,9.545,11.665]):p.line('risk.parallel.search.'+str(j),11.65,y,12.10,y)
        p.node('output.human.assessment','Event assessment','Exposure / rules / impact',17.02,8.20,7.11,2.25,'material',size=11.5)
        p.merge('risk.evidence.converges',[(16.25,7.425),(16.25,9.545),(16.25,11.665)],16.65,(17.02,9.325))
        p.narration="A risk analyst receives a Company A alert: the credit rating is on watch and operating cash flow is under pressure. The analyst gathers three types of evidence in parallel. Holdings identify the exposed funds and holding amounts. Contracts and internal policies identify applicable rules and clauses. Issuer research supports assessment of the event's impact. These searches repeatedly use the same issuer across systems and documents. The analyst brings the evidence together in an event assessment for risk work and discussion."
    elif i==20:
        p.family='Distinct source-extraction/rule explanation and event-comparison peer mechanisms';p.discussion='20'
        p.caption('peer.china.universal','China Universal',M,4.05,8.52,13,BLUE,.6);p.caption('peer.tianhong','Tianhong',16.25,4.05,7.88,13,BLUE,.6)
        p.node('input.custodian.alert','Custodian alert','',M,5.05,3.30,1.50,'material')
        p.node('role.alert.extraction','LLM','Extract / route',10.95,5.05,3.80,1.50,'llm',size=10.5)
        p.line('custodian.to.extraction',10.13,5.80,10.85,5.80)
        p.node('output.risk.workspace','Risk workspace','',M,7.10,8.02,.95,'material')
        p.line('alert.to.workspace',12.85,6.65,12.85,7.00)
        p.document('input.rule.sources','Sources','Regulations\nControls\nContracts',M,8.70,3.30,2.20,GRAY,10.5)
        p.node('tool.rule.links','System','Link rules to source',10.95,8.70,3.80,1.90,'tool',size=10.5)
        p.line('source.rule.links',10.13,9.65,10.85,9.65)
        p.node('output.rule.explanation','LLM trigger explanation','Source basis',M,11.05,8.02,1.45,'llm',size=10.5)
        p.line('rule.link.explanation',12.85,10.70,12.85,10.95)
        p.document('input.event.cases','Event / past cases','Event details\nComparable events',16.25,5.05,7.88,2.10,GRAY,11.5)
        p.node('role.event.assessment','LLM assessment','Compare cases\nOutline impact / follow-up',16.25,7.85,7.88,2.10,'llm',size=11.5)
        p.line('events.to.assessment',20.19,7.25,20.19,7.75)
        p.node('human.event.discussion','Investment / risk teams','Discuss implications',16.25,10.65,7.88,1.80,'human',size=11.5)
        p.line('assessment.to.discussion',20.19,10.05,20.19,10.55)
        p.narration="China Universal uses LLMs to read custodian risk alerts, extract relevant risk information and route it to the risk team's workspace. A related function links monitoring rules with regulations, internal controls and contract terms. The LLM explains the source-text basis for a rule trigger. Tianhong uses event details, comparable past events, industry relationships and market sentiment to support an LLM-drafted event assessment. The assessment compares the event with past cases and outlines potential impacts and follow-up actions. Investment and risk teams discuss the implications. The source-grounded rule explanation and the event-comparison assessment are distinct reported functions."
    elif i==21:
        p.family='Supplied alert/holding/requirement merge into assessment and human follow-through';p.discussion='21'
        p.document('input.alert','Company A alert','Credit watch\nCash-flow pressure',M,4.20,4.50,2.0,TEAL,11.5)
        p.document('input.holdings.record','Holdings record','Product A holds\nCompany A bonds\nRMB 20m face value',M,6.40,4.50,2.30,TEAL,11)
        p.document('input.monitoring.rule','Requirement','Update issuer research\nafter a credit event',M,8.95,4.50,1.85,GRAY,11)
        p.node('role.llm.link.evidence','LLM','Match issuer / exposure\nInterpret clauses / research\nDraft assessment',12.20,6.40,4.05,3.00,'llm',size=10.5)
        p.merge('credit.inputs.merge',[(11.23,5.20),(11.23,7.55),(11.23,9.875)],11.65,(12.20,7.90),TEAL)
        p.document('output.credit.assessment','Assessment / follow-up','Cash-flow pressure affects\ncapacity to service debt.\n\nAffected fund: Product A\nResearch follow-up:\nassess cash-flow trends',17.02,4.20,7.11,6.15,TEAL,11.5)
        p.line('llm.credit.output',16.25,7.90,16.92,7.90)
        steps=[('Risk staff','Verify'),('Analyst','Update assessment'),('Portfolio manager','Discuss response')]
        xs=[M,12.65,18.57];ws=[5.57,5.57,5.56]
        for j,((title,body),x,w) in enumerate(zip(steps,xs,ws)):
            p.node('human.credit.action.'+str(j),title,body,x,11.20,w,1.30,'human',size=10.5)
            if j<2:p.line('human.credit.handoff.'+str(j),x+w+.08,11.85,xs[j+1]-.10,11.85)
        p.route('assessment.to.risk.staff',[(20.575,10.45),(20.575,11.00),(9.515,11.00),(9.515,11.10)],TEAL)
        p.narration="The proposal begins with supplied evidence: the Company A alert, a current holding record showing that Product A holds RMB 20 million face value of Company A bonds, and a requirement to update issuer research after a credit event. The LLM identifies the issuer, links fund exposure, reviews applicable clauses and issuer research, and drafts an assessment. Cash-flow pressure affects the issuer's capacity to service debt. The output identifies Product A and a research follow-up to assess cash-flow trends. Risk staff verify exposures and requirements, analysts update the credit assessment, and portfolio managers discuss the response."
    elif i==22:
        p.family='Operations record entry and connected version-comparison/related-revision workflows';p.discussion='22'
        p.document('input.fax.scan','Fax / scan','',M,4.30,4.50,1.60,GRAY)
        p.node('human.ops.entry','Operations','Enter / validate',12.20,4.30,4.05,1.60,'human',size=11)
        p.node('output.business.record','Business record','',17.02,4.30,7.11,1.60,'material')
        p.line('fax.to.ops',11.33,5.10,12.10,5.10);p.line('ops.to.record',16.35,5.10,16.92,5.10)
        p.document('input.existing.versions','Existing V1 / V2','Quarterly client update',M,7.10,4.50,1.70,PURPLE,10.5)
        p.node('human.ops.compare','Operations','Compare versions',12.20,7.10,4.05,1.70,'human',size=11)
        p.document('output.manual.change.summary','Change summary','Detected differences',17.02,7.10,7.11,1.70,PURPLE,11)
        p.line('versions.to.compare',11.33,7.95,12.10,7.95,PURPLE);p.line('comparison.to.summary',16.35,7.95,16.92,7.95,PURPLE)
        p.document('input.related.documents','Related docs','Client files / Q&A',M,10.35,4.50,1.85,GRAY,10.5)
        p.node('human.ops.revise','Operations','Apply changes',12.20,10.35,4.05,1.85,'human',size=11)
        p.node('output.updated.materials','Updated materials','Related files / Q&A',17.02,10.35,7.11,1.85,'material',size=11)
        p.route('summary.guides.related.revision',[(20.575,8.90),(20.575,9.55),(14.225,9.55),(14.225,10.25)],PURPLE)
        p.line('related.docs.to.revision',11.33,11.275,12.10,11.275,PURPLE);p.line('revision.to.materials',16.35,11.275,16.92,11.275,PURPLE)
        p.narration="Operations handles several forms of document work. For faxes and scans, colleagues read the material, enter fields, validate them and save a business record. For client-update versions, colleagues compare V1 and V2, interpret the differences and prepare a change summary. That summary then guides the same revision across related client files and product questions and answers. The related documents are inputs to the revision work, and updated materials are its output. Rekeying information and interpreting changes consume time in this current manual workflow."
    elif i==23:
        p.family='HuaAn extraction lane and ICBCUBS existing-version comparison into evidence result';p.discussion='23';p.custom.append('Comparison result14.80–24.13 is enlarged to hold both approved V1/V2 investment-view excerpts; left version inputs and comparison role occupy6.73–14.15.')
        p.caption('peer.huaan','HuaAn: automated entry',M,4.00,MW,12.5,BLUE,.6)
        p.document('input.huaan.form','Fax / form','',M,4.65,4.50,1.10,GRAY)
        p.node('role.form.extraction','Model extracts','',12.20,4.65,4.05,1.10,'llm')
        p.node('output.client.service.record','Client-service record','',17.02,4.65,7.11,1.10,'material')
        p.line('fax.model',11.33,5.20,12.10,5.20);p.line('model.record',16.35,5.20,16.92,5.20)
        p.caption('evidence.huaan.scope','Direct-sales counter: more than 80% of faxes entered automatically',M,5.98,MW,10.5,BLUE,.5)
        p.caption('peer.icbcubs','ICBCUBS: compare existing versions',M,6.83,7.75,11.5,BLUE,.55)
        p.document('input.compare.v1','Existing V1','',M,7.65,3.60,1.35,PURPLE)
        p.document('input.compare.v2','Existing V2','',M,9.35,3.60,1.35,PURPLE)
        p.node('role.model.compares','Model','Compare versions',11.10,8.30,3.05,2.10,'llm',size=10.5)
        p.merge('existing.versions.merge',[(10.33,8.325),(10.33,10.025)],10.70,(11.10,9.35),PURPLE)
        p.shape('output.comparison.paper',14.80,6.55,9.33,6.05,'FFFFFF',PURPLE,.8)
        p.text('output.comparison.title','Comparison result',15.00,6.70,8.93,.55,12.5,True,PURPLE)
        p.text('comparison.v1.label','V1 investment view',15.00,7.36,8.93,.44,10.5,True,PURPLE)
        h=p.excerpt('comparison.v1',['Higher sales volumes drove Company A’s revenue growth.','We are monitoring raw-material costs.'],15.00,7.85,8.93,11.5,.52)
        yy=7.85+h+.08;p.text('comparison.v2.label','V2 investment view',15.00,yy,8.93,.44,10.5,True,PURPLE)
        p.excerpt('comparison.v2',['Channel restocking supported Company A’s sales volume growth.','We are monitoring whether restocking continues, alongside raw-material costs.'],15.00,yy+.50,8.93,11.5,.52,['Channel restocking supported','sales volume','whether restocking continues, alongside'])
        p.line('compare.to.comparison.result',14.25,9.35,14.70,9.35,PURPLE)
        p.narration="HuaAn reports automated data entry for more than eighty percent of faxes handled by its direct-sales counter. The model reads document content, extracts required fields and populates client-service records. ICBCUBS's document-comparison use starts with two existing versions in PDF, Word or scanned form. The model reads and compares them, highlights additions, checks typographical issues and supports export. In the client-update example, the result identifies the added restocking driver and the question of whether restocking continues, while raw-material-cost monitoring is retained. Both V1 and V2 are supplied inputs to comparison."
    elif i==24:
        p.family='Tool matching and LLM semantic change summary feed operations filing/propagation';p.discussion='24'
        p.document('input.analysis.versions','Existing V1 / V2','Quarterly update',M,4.25,4.50,1.75,PURPLE,10.5)
        p.node('tool.passage.matching','Document tools','Match passages',12.20,4.25,4.05,1.75,'tool',size=11)
        p.node('role.semantic.change','LLM explains','Interpret changes',17.02,4.25,7.11,1.75,'llm',size=11.5)
        p.line('versions.to.tools',11.33,5.125,12.10,5.125,PURPLE);p.line('tools.to.llm.change',16.35,5.125,16.92,5.125)
        p.document('output.semantic.summary','Change summary','Added driver: channel restocking\nAdded question: whether restocking continues\nRetained: raw-material cost monitoring',M,7.05,9.52,3.65,PURPLE,12)
        p.route('llm.to.semantic.summary',[(20.575,6.10),(20.575,6.60),(11.49,6.60),(11.49,6.95)],PURPLE)
        p.node('human.operations.use','Operations','Check summary',17.02,7.75,7.11,1.65,'human',size=11.5)
        p.line('summary.to.operations',16.35,8.575,16.92,8.575,PURPLE)
        p.node('output.filed.v2','Filed with V2','Record retained',17.02,10.30,3.40,2.05,'client',size=10.5)
        p.node('output.related.revision','Related updates','Client files / Q&A',20.92,10.30,3.21,2.05,'material',size=10.5)
        p.line('operations.output.trunk',20.575,9.50,20.575,9.83,arrow=False);p.line('operations.output.branch',18.72,9.83,22.525,9.83,arrow=False)
        p.line('operations.filing',18.72,9.83,18.72,10.20,PURPLE);p.line('operations.related.updates',22.525,9.83,22.525,10.20,PURPLE)
        p.narration="Operations supplies both quarterly-update versions. Document tools identify matching passages and changes to the fund name, reporting period and wording. The LLM then explains what the changes mean, separating new and retained information. The semantic summary records restocking as the added growth driver, continuation of restocking as the added monitoring question, and raw-material costs as retained monitoring. Operations checks the summary, files it with V2 and identifies related client updates and product questions and answers that use the same investment view. Colleagues then apply the relevant revision to those materials."
    else:return False
    return True

def batch_three(p):
    i=p.i
    if i==25:
        p.family='Header/body sample distinction, developer actions and concrete debug return';p.discussion='25'
        for j,x in enumerate([M,12.20]):
            w=4.50 if j==0 else 4.05;p.document('input.dev.version.'+str(j),'V1 sample' if j==0 else 'V2 sample','',x,4.25,w,2.80,PURPLE)
            p.text('sample.header.'+str(j),'Repeated header',x+.18,5.08,w-.36,.60,10.5,False,GRAY,align='ctr',fill=LIGHT,line=GRAY,pad=.03)
            p.text('sample.body.'+str(j),'Body text',x+.18,6.10,w-.36,.60,11.5,True,PURPLE,align='ctr',line=PURPLE,pad=.03)
            p.caption('sample.ignore.'+str(j),'Ignore',x+.18,5.72,w-.36,9.5,GRAY,.35)
        p.node('input.comparison.rule','Business rule','Ignore repeated headers\nCompare body text',17.02,4.25,7.11,2.80,'material')
        for x in [8.98,14.225,20.575]:p.line('development.inputs.'+str(x),x,7.15,x,7.68,arrow=False)
        p.line('development.requirements.merge',8.98,7.68,20.575,7.68,arrow=False)
        p.line('inputs.to.requirements',8.98,7.68,8.98,8.30)
        for j,(title,body,x,w) in enumerate([('Developer','Requirements',M,4.50),('Developer','Code',12.20,4.05),('Developer','Test',17.02,7.11)]):
            p.node('human.development.'+str(j),title,body,x,8.40,w,1.65,'human')
            if j<2:p.line('development.action.'+str(j),x+w+.10,9.225,[12.10,16.92][j],9.225)
        p.document('output.comparison.tool','Comparison tool','Code artifact',M,10.85,4.50,1.60,GRAY,10.5)
        p.node('output.test.failure','Test failure','Repeated header wrongly flagged',17.02,10.85,7.11,1.60,'material',size=11)
        p.route('code.to.tool.artifact',[(13.00,10.15),(13.00,10.45),(8.98,10.45),(8.98,10.75)])
        p.line('test.failure.output',20.575,10.15,20.575,10.75)
        p.route('failure.to.debug',[(16.92,11.65),(15.25,11.65),(15.25,10.15)])
        p.caption('debug.return.label','Debug',15.45,10.80,1.40,9.5)
        p.narration="The requested business tool compares two versions while ignoring repeated page headers. The developer translates that rule into requirements, including additions, deletions and edits to genuine body text. Code must read files, match paragraphs and locate the changes. Line and page breaks can disrupt matching, and a changed header can be flagged incorrectly. Testing exposes those false positives, which return to coding and debugging. A working comparison tool and its results follow repeated implementation, testing and correction. Separating repeated headers from genuine body changes is part of the developer’s testing criteria."
    elif i==26:
        p.family='Two equal peer coding-support flows with scoped developer responsibility';p.discussion='26'
        cases=[('E Fund',4.10,4.95,[('Developer task','Examples / expected results','human'),('LLM','Code / tests','llm'),('Developer','Run / check / feedback','human')]),('Invesco Great Wall',8.50,9.35,[('Quantitative team','Coding task','human'),('Local model','Coding support','llm'),('Developer','Check output','human')])]
        for row,(name,labely,y,vals) in enumerate(cases):
            p.caption('peer.development.'+str(row),name,M,labely,MW,13,BLUE,.60)
            for j,((title,body,kind),x,w) in enumerate(zip(vals,[M,12.20,17.02],[4.50,4.05,7.11])):
                p.node('peer.development.'+str(row)+'.'+str(j),title,body,x,y,w,2.10,kind,size=10.5)
                if j<2:p.line('peer.development.flow.'+str(row)+'.'+str(j),x+w+.10,y+1.05,[12.10,16.92][j],y+1.05)
        p.route('efund.test.feedback',[(20.575,7.15),(20.575,7.70),(14.225,7.70),(14.225,7.15)],GRAY,.75)
        p.caption('efund.feedback.label','Test feedback',15.15,7.20,5.0,10.5,GRAY,.45)
        p.narration="E Fund uses LLMs in development and testing. A developer supplies examples, expected results and the required behavior. The LLM can draft processing code and tests, while the developer runs the code, checks results and supplies error details for refinement. Invesco Great Wall's quantitative team uses locally deployed models for coding support. The team's coding task and the model's assistance are followed by developer checking. The reported scopes differ, and both uses depend on colleagues specifying work and reviewing the output."
    elif i==27:
        p.family='Concrete failure and human feedback drive six-stage code/retest loop';p.discussion='27'
        p.caption('development.requirement','Compare V1/V2 body text. Ignore repeated page headers.',M,4.00,MW,11.5,BLUE,.55)
        vals=[('1 Developer','Define examples\nExpected results','human'),('2 LLM','Code / tests','llm'),('3 Test runner','Run tests','tool')]
        for j,((title,body,kind),x,w) in enumerate(zip(vals,[M,12.20,17.02],[4.50,4.05,7.11])):
            p.node('development.top.'+str(j),title,body,x,4.85,w,1.90,kind,size=11)
            if j<2:p.line('development.top.flow.'+str(j),x+w+.10,5.80,[12.10,16.92][j],5.80)
        p.document('input.dev.examples','V1 / V2 examples','Expected differences\nmarked',M,7.15,4.50,2.30,PURPLE,11.5)
        p.line('examples.to.developer',8.98,7.05,8.98,6.85,PURPLE)
        p.document('output.test.results','Test results','Body changes detected\nHeaders wrongly flagged',17.02,7.15,7.11,2.30,GRAY,12)
        p.line('runner.to.results',20.575,6.85,20.575,7.05)
        bottom=[('6 Developer','Retest / deliver\nTool + user guide',M,4.50,'human'),('5 LLM','Fix header filter\nAdd regression test',12.20,4.05,'llm'),('4 Developer','Exclude headers\nRetain body changes',17.02,7.11,'human')]
        for j,(title,body,x,w,kind) in enumerate(bottom):p.node('development.bottom.'+str(j),title,body,x,10.05,w,2.35,kind,size=11.5)
        p.line('results.to.explanation',20.575,9.55,20.575,9.95)
        p.line('feedback.to.revision',16.92,11.225,16.35,11.225);p.line('revision.to.retest',12.10,11.225,11.33,11.225)
        p.narration="The developer defines examples and expected differences using the quarterly-update V1 and V2. The requirement is to compare body text and ignore repeated headers. The LLM drafts paragraph-matching code and tests, and a test runner executes them. In the illustrated failure, body changes are detected but header changes are also flagged. The developer explains the distinction: exclude repeated page headers while retaining genuine body-text changes. The LLM revises the header filter and adds a regression test. The developer reviews and reruns the code, then delivers the tool and user guide after the checks."
    elif i==28:
        p.family='Three attributed source/interpretation/tool/output mechanisms';p.discussion='28'
        p.caption('other.employee.attribution','Employee support: China Merchants Fund / Ping An Fund',M,4.00,MW,11.5,BLUE,.55)
        for j,(title,body,x,w,kind) in enumerate([('Employee asks','Policy / process',M,4.50,'human'),('LLM','Retrieve / explain',12.20,4.05,'llm'),('Employee guidance','',17.02,7.11,'material')]):
            p.node('other.employee.'+str(j),title,body,x,4.72,w,1.65,kind,size=11)
            if j<2:p.line('other.employee.flow.'+str(j),x+w+.10,5.545,[12.10,16.92][j],5.545)
        p.caption('other.security.attribution','Email security: Maxwealth Fund',M,6.73,MW,11.5,BLUE,.55)
        xs=[M,11.25,15.77,20.29];ws=[3.70,3.70,3.70,3.84]
        for j,(title,body,kind) in enumerate([('Email / links','Attachments','material'),('LLM','Context / intent','llm'),('Detection tools','','tool'),('Security response','','material')]):
            p.node('other.security.'+str(j),title,body,xs[j],7.45,ws[j],1.65,kind,size=10.5)
            if j<3:p.line('other.security.flow.'+str(j),xs[j]+ws[j]+.10,8.275,xs[j+1]-.10,8.275)
        p.caption('other.analytics.attribution','Business analytics: China Universal patent proposal',M,9.47,MW,11.5,BLUE,.55)
        for j,(title,body,kind) in enumerate([('Request','Fund / period / metric','material'),('LLM','Interpret question','llm'),('Algorithms','Quantify contributions','tool'),('LLM summary','Analytical text','llm')]):
            p.node('other.analytics.'+str(j),title,body,xs[j],10.18,ws[j],2.20,kind,size=10.5)
            if j<3:p.line('other.analytics.flow.'+str(j),xs[j]+ws[j]+.10,11.28,xs[j+1]-.10,11.28)
        p.narration="Additional back-office uses combine language work with sources and execution tools. China Merchants Fund and Ping An Fund use LLMs to retrieve and explain guidance for employee policy and process questions. Maxwealth Fund's email-security use considers email content, attachments and links; the LLM assesses context and intent and invokes detection tools. In a China Universal patent proposal, the LLM interprets a business-analytics request, algorithms quantify contributions to the selected metric and the LLM drafts the analytical summary. The requested fund, period and metric remain the starting point, and quantitative computation belongs to the algorithms."
    elif i==29:
        p.family='Seven recipient/output nodes in the firm hierarchy';p.discussion='29'
        p.node('firm.root','Company applications','',9.15,4.04,7.10,.95,'llm')
        p.line('firm.trunk',12.70,5.00,12.70,5.38,arrow=False);p.line('firm.branch',4.825,5.38,20.575,5.38,arrow=False)
        groups=[('Front office',[('Research','Analyst: summary with sources'),('Trading support','Trader: bond and quote summary'),('Client materials','Client team: updates and Q&A')]),('Middle office',[('Content review','Reviewer: findings and revisions'),('Risk analysis','Risk team: assessment / follow-up')]),('Back office',[('Document processing','Operations: records / change summaries'),('Tool development','Developer: code and tests')])]
        for j,(office,tasks) in enumerate(groups):
            x=[1.27,9.15,17.02][j];w=[7.11,7.10,7.11][j];p.line('firm.office.branch.'+str(j),x+w/2,5.38,x+w/2,5.64,arrow=False)
            p.node('firm.office.'+str(j),office,'',x,5.72,w,.95,'llm')
            for k,(task,outcome) in enumerate(tasks):p.node('firm.output.'+str(j)+'.'+str(k),task,outcome,x,6.98+k*1.38,w,1.20,'material',size=10.5)
        p.text('human.shared.judgment','People verify the results and exercise professional judgment',L,11.90,W,.65,12,True,INK,align='ctr',anchor='ctr',fill=LIGHT,line=GRAY,pad=.04)
        p.narration="The seven proposals produce identifiable outputs for colleagues. Analysts receive source-backed research summaries; traders receive bond and quote summaries; client-facing teams receive updates and responses. Reviewers receive explained findings and proposed revisions, risk teams receive assessments and follow-up items, operations receives records and change summaries, and developers receive code and test material. LLMs support reading, comparison and drafting across these tasks. Colleagues verify the output, use the relevant sources and exercise professional judgment in the business decision."
    elif i==30:
        p.family='Two recurring material lanes share information and version states across offices';p.discussion='30';p.custom.append('Main office columns6.73/12.65/18.57 are equal5.56–5.57cm spans inside the map-adjusted mechanism region.')
        xs=[M,12.65,18.57];ws=[5.57,5.57,5.56]
        for j,office in enumerate(['Front office','Middle office','Back office']):p.caption('cross.office.'+str(j),office,xs[j],4.10,ws[j],13,BLUE,.60)
        p.caption('story.issuer.label','Company A information',M,5.00,MW,12,TEAL,.50)
        issuer=[('Research / trading','Company analysis\nBond / quote summary'),('Risk work','Event assessment\nExposure monitoring'),('Operations','Related documents\nRevision tracking')]
        for j,(title,body) in enumerate(issuer):p.node('issuer.office.state.'+str(j),title,body,xs[j],5.75,ws[j],2.35,'issuer',size=11)
        for j in range(2):
            p.line('issuer.share.forward.'+str(j),xs[j]+ws[j]+.08,6.48,xs[j+1]-.10,6.48,TEAL)
            p.line('issuer.share.return.'+str(j),xs[j+1]-.10,7.33,xs[j]+ws[j]+.08,7.33,TEAL)
        p.caption('story.client.label','Quarterly client update',M,8.80,MW,12,PURPLE,.50)
        for j,(title,body) in enumerate([('Draft V1','Client team'),('Reviewed V2','Author / reviewer'),('Version comparison','Related updates')]):
            p.node('client.office.state.'+str(j),title,body,xs[j],9.55,ws[j],2.30,'client',size=11.5)
            if j<2:p.line('client.version.handoff.'+str(j),xs[j]+ws[j]+.08,10.70,xs[j+1]-.10,10.70,PURPLE)
        p.narration="Company A provides a common issuer identity across research, trading support, risk work and document maintenance. Colleagues share company analysis, bond and quote summaries, event assessments, exposure information and related records. The same information supports several teams' work. The quarterly client update is a second recurring object: the client team prepares V1, author and reviewer produce the reviewed V2, and operations compares versions and updates related material. Shared sources and version history help colleagues avoid repeated searches and inconsistent explanations across the front, middle and back offices."
    elif i==31:
        p.family='Staff/application/output return plus LLM-tool exchange and shared-source dependencies';p.discussion='31'
        p.node('human.staff.request.check','Staff','Request / check',M,4.50,4.50,1.60,'human')
        p.node('role.business.application','Application','Seven tasks',12.20,4.50,4.05,1.60,'llm')
        p.document('output.client.draft','Client-update draft','For staff check',17.02,4.50,7.11,1.60,PURPLE,11.5)
        p.line('staff.to.application',11.33,5.30,12.10,5.30);p.line('application.to.output',16.35,5.30,16.92,5.30,PURPLE)
        p.route('output.return.to.staff',[(20.575,4.40),(20.575,4.10),(8.98,4.10),(8.98,4.40)],PURPLE)
        p.shape('application.responsibility.scope',M,6.75,MW,5.65,None,RULE,.5)
        p.line('application.role.trunk',14.225,6.20,14.225,7.02,arrow=False);p.line('application.role.branch',10.285,7.02,20.575,7.02,arrow=False)
        p.line('application.to.llm',10.285,7.02,10.285,7.55);p.line('application.to.tools',20.575,7.02,20.575,7.55)
        p.node('role.shared.llm','LLM','Interpret / compare\nDraft content',M,7.65,7.11,2.05,'llm')
        p.node('role.shared.tools','Tools','Query / calculate\nProcess / execute',17.02,7.65,7.11,2.05,'tool')
        p.line('llm.tool.request',13.94,8.30,16.92,8.30);p.caption('llm.tool.request.label','Request',14.25,7.80,2.45,9.5)
        p.line('tool.llm.result',16.92,9.18,13.94,9.18);p.caption('tool.llm.result.label','Result',14.25,9.30,2.45,9.5)
        p.node('shared.approved.sources','Approved shared sources','Documents / knowledge bases / business data',M,10.72,MW,1.43,'material',size=11.5)
        for x in [10.285,20.575]:p.line('source.dependency.'+str(x),x,10.72,x,9.70,GRAY,.75,False)
        p.narration="Employees provide a business question and relevant material to an application supporting one of the seven tasks. The application combines language-model work with operational tools. The LLM interprets questions, compares sources and drafts content. Tools query systems, perform calculations, process files and run code or tests. Shared approved documents, knowledge bases and business data support both roles, with access controls, source references and version history. The application returns a concrete business output, such as a client-update draft, for staff to check and use. Qwen and DeepSeek are candidates for evaluation on the company's tasks."
    elif i==32:
        p.family='Attached stage markers, business phases, aligned teams and deliverable objects';p.discussion='32';p.custom.append('Three equal main-stage columns6.73/12.65/18.57 balance phase labels and deliverable objects after the persistent map.')
        xs=[M,12.65,18.57];ws=[5.57,5.57,5.56];p.line('phase.timeline',7.18,5.075,23.85,5.075,BLUE,1.3)
        data=[('Research / client\ncommunications','Research / Sales\nCompliance / IT','Sample tasks\nSource inventory\nInitial applications'),('Trading /\noperations','Trading / Operations\nIT','Data definitions\nQuery interfaces\nDocument workflows'),('Development /\ninternal services','Business teams / IT','Business tools\nUser guides\nNamed maintenance owner')]
        for j,(title,teams,outputs) in enumerate(data):
            x=xs[j];p.text('phase.marker.'+str(j),str(j+1),x,4.65,.90,.85,16,True,'FFFFFF',align='ctr',anchor='ctr',fill=BLUE,geometry='ellipse')
            p.text('phase.title.'+str(j),title,x,5.90,ws[j],1.25,13,True,BLUE)
            p.caption('phase.teams.label.'+str(j),'Participating teams',x,7.45,ws[j],9.5,GRAY,.4)
            p.text('phase.teams.'+str(j),teams,x,8.03,ws[j],.97,10.5)
            p.document('phase.deliverables.'+str(j),'Deliverables',outputs,x,9.30,ws[j],2.95,GRAY,11.5)
        p.narration="Implementation proceeds through three business-led phases. The first focuses on research and client communications, with research, sales, compliance and IT contributing sample tasks, a source inventory and initial applications. The second integrates trading and operations, with trading, operations and IT defining data, system-query interfaces and document workflows. The third expands development support and internal services, with business teams and IT delivering tools, user guides and named maintenance ownership. Each phase has an identifiable business scope and a usable deliverable. The work can be planned and assessed against those business deliverables."
    elif i==33:
        p.family='Baseline enters use/results/review cycle with four measures attached to results';p.discussion='33'
        p.caption('evaluation.initial.focus','Initial focus: research / client communications',M,4.00,MW,12,BLUE,.55)
        p.node('input.evaluation.baseline','Baseline','Current task outcomes',M,4.85,4.50,1.70,'material',size=11)
        p.node('activity.application.use','Application use','Employee task',12.20,4.85,4.05,1.70,'role',size=11)
        p.node('activity.record.results','Record results','',17.02,4.85,7.11,1.70,'material')
        p.line('baseline.to.use',11.33,5.70,12.10,5.70);p.line('use.to.results',16.35,5.70,16.92,5.70)
        p.node('output.results.measures','Outcome measures','Completion time\nOutput use\nRework\nRepeat usage',17.02,7.40,7.11,3.40,'material')
        p.line('results.to.measures',20.575,6.65,20.575,7.30)
        p.node('human.team.refines','Team review','Compare with baseline\nRefine workflow',M,9.40,9.52,2.30,'human')
        p.line('measures.to.team',16.92,10.25,16.35,10.25)
        p.line('baseline.to.comparison',8.98,6.65,8.98,9.30,GRAY,.75)
        p.route('refined.workflow.return',[(11.49,9.30),(11.49,8.55),(14.225,8.55),(14.225,6.65)])
        p.caption('refinement.return.label','Refined task',12.12,8.04,3.95,10.5)
        p.narration="Evaluation begins with a baseline for research and client-communications tasks. Colleagues use the application and record the outcome. Completion time runs from starting the task to completing its output. Output use records whether teams actually use the analysis and materials. Rework records revision rounds and repeated checks. Repeat usage records whether employees continue to use the application. The team compares those results with the baseline, reviews where the workflow needs improvement and refines it before subsequent use. The baseline comparison establishes the effect on actual employee work."
    else:return False
    return True

def notes_body(root):
    for s in root.findall('.//p:sp',NS):
        ph=s.find('./p:nvSpPr/p:nvPr/p:ph',NS)
        if ph is not None and ph.get('type')=='body':return s.find('./p:txBody',NS)
    raise ValueError('Missing speaker-note body')

def document_record(index):
    c=APPROVED[index-1]['text']
    return '\n'.join([c['!!clientDoc.title']+' '+c['!!clientDoc.version'],
        'Fund name: '+norm(c['!!clientDoc.value.product']),
        'Source version: '+norm(c['!!clientDoc.value.period']),
        'Investment view: '+norm(c['!!clientDoc.value.view']),
        'Risk disclosure: '+norm(c['!!clientDoc.value.risk'])])

def supporting_material(i,p):
    keys={4:['research.evidence.1.text','research.evidence.2.text','research.evidence.3.text'],6:['views.reportA.text','views.reportB.text'],7:['elements.stat'],8:['research.evidence.1.text','research.evidence.2.text','research.evidence.3.text','research.result.text'],10:['trade.case1.scope'],11:['trade.intent','trade.system.body','trade.llm.quote.body'],13:['client.views.source.text','client.views.result.text'],14:['tender.source.text','tender.answer.body','tender.case'],19:['risk.mail.text'],20:['risk.event.input.text'],21:['risk.evidence.mail.text','risk.evidence.system.body','risk.evidence.rule.text','risk.result.body'],23:['ops.stat'],24:['changeLog.driver.body','changeLog.watch.body','changeLog.sync.body'],25:['dev.request'],26:['dev.case2'],27:['dev.request'],28:['other.2.company'],31:['arch.data','arch.models']}
    vals=[p.original(k) for k in keys.get(i,[])]
    if i==1:vals.append('Cover image: AI-generated illustration of an investment-research workspace.')
    if i in [15,16,17]:vals.append(document_record(15))
    if i==16:vals.append('Current portfolio-manager presentation: '+norm(p.original('review.reference.text')))
    if i==17:
        vals += [p.original('comment.meta.body'),p.original('comment.view.body'),p.original('comment.risk.body'),'Penghua’s reported91% figure concerns acceptance of suggested edits.']
    if i==18:vals += [document_record(15),document_record(18)]
    if i==23:vals += ['V1 investment view: '+norm(APPROVED[14]['text']['!!clientDoc.value.view']),'V2 investment view: '+norm(APPROVED[17]['text']['!!clientDoc.value.view'])]
    if i==32:
        for j in range(3):vals.append(norm(p.original(f'phase.{j}.title'))+'\nParticipating teams: '+norm(p.original(f'phase.{j}.roles'))+'\nDeliverables: '+norm(p.original(f'phase.{j}.outputs')))
    if i==33:
        for j in range(4):vals.append(p.original(f'evaluation.{j}.title')+': '+norm(p.original(f'evaluation.{j}.body')))
    return vals

def set_notes(data,i,p):
    part=f'ppt/notesSlides/notesSlide{i}.xml';x=E.fromstring(data[part]);b=notes_body(x)
    inherited='\n'.join(''.join(q.xpath('.//a:t/text()',namespaces=NS)) for q in b.findall('./a:p',NS))
    support=supporting_material(i,p)
    urls=list(dict.fromkeys(re.findall(r'https?://[^\s]+',inherited)))
    speech=p.narration
    sections=['Suggested spoken explanation',speech]
    if support or urls:sections += ['','Sources and supporting material','\n\n'.join(support),'\n'.join(urls)]
    value='\n'.join(sections)
    for q in b.findall('./a:p',NS):b.remove(q)
    for t in value.split('\n'):
        q=n(b,A,'p');r=n(q,A,'r');pr=n(r,A,'rPr',sz='1200');n(pr,A,'latin',typeface='Arial');n(r,A,'t').text=t
    data[part]=E.tostring(x,xml_declaration=True,encoding='UTF-8',standalone=True)
    return {'narration':speech,'supporting_wording':support,'source_urls':urls,'full_notes':value,'source_archive':inherited}

def main():
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SHA
    QA.mkdir(exist_ok=True,parents=True)
    with ZipFile(SOURCE) as z:entries=z.infolist();data={e.filename:z.read(e.filename) for e in entries}
    manifest=[];notes=[];source_notes=[]
    for i in range(1,34):
        part=f'ppt/slides/slide{i}.xml';p=Page(i,E.fromstring(data[part]),APPROVED[i-1]['text'])
        if i==8:research_proposal(p)
        elif i==9:trading_workflow(p)
        elif not batch_one(p) and not batch_two(p):batch_three(p)
        data[part]=E.tostring(p.root,xml_declaration=True,encoding='UTF-8',standalone=True)
        nr=set_notes(data,i,p);source_notes.append({'slide':i,'source_notes':nr.pop('source_archive')});notes.append({'slide':i,**nr})
        manifest.append({'slide':i,'family':p.family,'discussion_page':p.discussion,'items':p.items,'custom_spans':p.custom})
    with ZipFile(BUILD/'candidate.pptx','w') as z:
        for e in entries:z.writestr(e,data[e.filename])
    (QA/'layout-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False))
    (ROOT/'src/speaker-notes.json').write_text(json.dumps(notes,indent=2,ensure_ascii=False))
    (ROOT/'src/source-notes.json').write_text(json.dumps({'source_sha256':SHA,'slides':source_notes},indent=2,ensure_ascii=False))
    print('Visual mechanisms implemented:',sum(q['family']!='Pending' for q in manifest),'/33')
if __name__=='__main__':main()
