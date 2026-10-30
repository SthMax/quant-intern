"""Preserve native source diagrams and compose the agreed 28-slide edition."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from copy import deepcopy
from lxml import etree as E
import hashlib,json,re
from native import *

SOURCE=ROOT.parent/'visual-workflows-2026-10-28/output/asset-management-llm-visual-en.pptx'
SHA='1dae3a54c474190f1ca41ddbbd1a923d61929df714f861828547a59ddd39a2e4'
OLD_NOTES=json.loads((ROOT/'src/original-speaker-notes.json').read_text())
OLD_ARCHIVE=json.loads((ROOT/'src/original-source-notes.json').read_text())
APPROVED=json.loads((ROOT/'src/original-approved-content.json').read_text())
BUILD=ROOT/'build';QA=BUILD/'qa'
BASE=[1,2,3,4,5,6,8,9,10,11,12,14,18,19,20,21,22,23,25,26,27,29,30,32,33,7,13,28]
INPUTS=[[1],[2,31],[3],[4],[5],[6],[8],[9],[10],[11],[12,16],[14,17],[15,16,18,24],[19],[20],[21],[22],[23],[25],[26],[27],[29],[30],[31,32],[33],[7],[13],[28]]
PLAN=[]
for line in (ROOT/'HANDOFF.md').read_text().splitlines():
    cells=[s.strip() for s in line.split('|')[1:-1]]
    if len(cells)==4 and cells[0].isdigit():PLAN.append({'slide':int(cells[0]),'title':cells[2],'subtitle':cells[3]})
assert len(PLAN)==28

def shape_name(s):
    a=s.find('.//p:cNvPr',NS)
    return a.get('name','') if a is not None else ''

def change(p,name,value):
    s=next(s for s in p.tree if shape_name(s)==name);b=s.find('./p:txBody',NS)
    old=b.findall('./a:p',NS)
    for q in old:b.remove(q)
    for i,text in enumerate(value.split('\n')):
        q=deepcopy(old[min(i,len(old)-1)])
        for a in list(q):
            if E.QName(a).localname not in ['pPr','endParaRPr']:q.remove(a)
        r=n(q,A,'r');rp=old[min(i,len(old)-1)].find('./a:r/a:rPr',NS)
        if rp is not None:r.append(deepcopy(rp))
        n(r,A,'t').text=text;b.append(q)

def retained(p,source):
    for q in source.find('./p:cSld/p:spTree',NS):
        name=shape_name(q)
        if E.QName(q).localname in ['nvGrpSpPr','grpSpPr'] or name in ['title','subtitle','source.note'] or name.startswith('map.'):continue
        p.tree.append(deepcopy(q))
    p.family='Retained native source mechanism'

def firm_map(p,outputs=False):
    p.family='Six application areas in three offices'
    p.node('firm.root','Proposed applications' if outputs else 'Asset management firm','',9.15,4.04,7.10,.95,'llm')
    p.line('firm.trunk',12.70,5.00,12.70,5.38,arrow=False);p.line('firm.branch',4.825,5.38,20.575,5.38,arrow=False)
    groups=[('Front office',[('Research','Analyst: summary with sources' if outputs else 'Company analysis'),('Trading support','Trader: holdings and quote summary' if outputs else 'Bond and quote preparation'),('Client communications','Client team: approved material' if outputs else 'Drafting, review and approval')]),('Middle office',[('Risk analysis','Risk team: assessment and follow-up' if outputs else 'Exposure, impact and follow-up')]),('Back office',[('Record entry','Operations: validated records' if outputs else 'Capture and validation'),('Tool development','Developer: code and tests' if outputs else 'Internal business tools')])]
    for j,(office,tasks) in enumerate(groups):
        x=[1.27,9.15,17.02][j];w=[7.11,7.10,7.11][j]
        p.line('firm.office.branch.'+str(j),x+w/2,5.38,x+w/2,5.64,arrow=False)
        p.node('firm.office.'+str(j),office,'',x,5.72,w,.95,'llm')
        for k,(task,outcome) in enumerate(tasks):p.node('firm.task.'+str(j)+'.'+str(k),task,outcome,x,6.98+k*1.45,w,1.30,'material',size=10.5)
    if outputs:
        p.text('human.shared.judgment','Colleagues verify outputs and exercise professional judgment',L,12.00,W,.65,12,True,INK,align='ctr',anchor='ctr',fill=LIGHT,line=GRAY,pad=.04)
    else:
        p.node('story.issuer','Company A','Research / trading / risk / records',1.27,11.75,10.93,1.10,'issuer',size=10.5)
        p.node('story.client','Quarterly client update','Drafting / review / approval',13.20,11.75,10.93,1.10,'client',size=10.5)

def client_workflow(p):
    p.family='Client sources, author drafting, middle-office review, revision and approval'
    p.document('input.client.question','Client question','Quarterly changes?',M,4.25,4.50,1.75,PURPLE,11.5)
    p.document('input.client.pm.views','PM views','Investment explanation',M,6.45,4.50,1.75,PURPLE,11.5)
    p.document('input.client.product','Product sources','Fund / period / risk\nPrior client material',M,8.65,4.50,2.25,GRAY,11.5)
    p.node('human.client.author','Front-office author','Select sources\nDraft wording',12.20,5.20,4.05,2.25,'human',size=11.5)
    p.merge('sources.to.author',[(11.23,5.125),(11.23,7.325),(11.23,9.775)],11.65,(12.20,6.325),GRAY)
    p.document('output.client.draft','Draft client material','Investment view\nFund, period and risk',17.02,4.60,7.11,2.30,PURPLE,12)
    p.line('author.to.draft',16.25,6.325,16.92,6.325)
    p.node('human.middle.reviewer','Middle-office reviewer','Check current sources\nExplain issues',17.02,7.55,7.11,1.90,'human',size=11.5)
    p.line('draft.to.review',20.575,7.00,20.575,7.45,PURPLE)
    p.node('human.author.revision','Author revises','Address findings',12.20,9.10,4.05,1.60,'human',size=11.5)
    p.route('review.findings.to.author',[(16.92,8.50),(16.62,8.50),(16.62,9.90),(16.35,9.90)])
    p.document('output.client.approved','Approved client material','Checked against current sources',17.02,10.65,7.11,1.90,PURPLE,11.5)
    p.route('revision.to.approval',[(14.225,10.80),(14.225,11.60),(16.92,11.60)])
    p.caption('approval.role','Approval',12.20,11.00,1.75,10.5)

def client_peers(p):
    p.family='Separate attributed ICBCUBS drafting and Penghua review mechanisms'
    p.caption('case.icbcubs','ICBCUBS: institutional RFP drafting',M,4.08,MW,13,BLUE,.55)
    p.document('peer.rfp.source','Knowledge base','Research roles\nProcess description',M,4.95,4.50,2.45,GRAY,11.5)
    p.node('peer.fundgpt','FundGPT','Retrieve sources\nDraft response',12.20,4.95,4.05,2.45,'llm',size=11.5)
    p.document('peer.rfp.response','RFP response','Relevant responsibilities\nSource-backed explanation\nSource reference',17.02,4.95,7.11,2.45,BLUE,11.5)
    p.line('knowledge.to.fundgpt',11.33,6.175,12.10,6.175);p.line('fundgpt.to.response',16.35,6.175,16.92,6.175)
    p.caption('peer.rfp.human','Business team checks the answer and sources',M,7.65,MW,11,GRAY,.45)
    p.caption('case.penghua','Penghua: marketing-material review',M,8.30,MW,13,BLUE,.55)
    p.document('peer.review.inputs','Draft and rules','Marketing material\nReview requirements',M,9.10,4.50,2.60,GRAY,11.5)
    p.node('peer.penghua.llm','LLM reviews','Explain findings\nSuggest edits',12.20,9.10,4.05,2.60,'llm',size=11.5)
    p.document('peer.review.output','Suggested revisions','Fund information\nRisk wording\nReview rationale',17.02,9.10,7.11,2.60,GRAY,11.5)
    p.line('rules.to.review',11.33,10.40,12.10,10.40);p.line('review.to.revisions',16.35,10.40,16.92,10.40)
    p.caption('peer.review.human','Author revises and reviewer checks',M,12.00,MW,11,GRAY,.45)

def evidence_paper(p,name,title,period,paras,x,y,w,h,changes=()):
    p.shape(name+'.paper',x,y,w,h,'FFFFFF',PURPLE,.8)
    p.text(name+'.title',title,x+.20,y+.14,w-.40,.55,13,True,PURPLE)
    p.text(name+'.period',period,x+.20,y+.82,w-.40,.42,10.5,False,GRAY)
    p.text(name+'.view.label','Investment view',x+.20,y+1.36,w-.40,.42,10.5,True)
    p.excerpt(name+'.view',paras,x+.20,y+1.92,w-.40,12,.56,changes)

def client_proposal(p):
    p.family='Sources to drafting and V1, current-source matching, explained revision to V2 and human approval'
    p.node('input.supplied.sources','Sources','Client / PM input',M,4.18,4.10,1.35,'client',size=10.5)
    p.node('role.llm.drafts','LLM drafts','',11.43,4.18,3.80,1.35,'llm')
    p.line('sources.to.llm.draft',10.93,4.855,11.33,4.855,PURPLE)
    p.document('input.current.review.sources','Current review sources','PM view / product information',17.02,4.18,7.11,1.35,GRAY,10.5)
    v1=['Higher sales volumes drove Company A’s revenue growth.','We are monitoring raw-material costs.']
    v2=['Channel restocking supported Company A’s sales volume growth.','We are monitoring whether restocking continues, alongside raw-material costs.']
    evidence_paper(p,'evidence.client.v1','Draft V1','Q2 product source',v1,M,6.08,7.10,4.35)
    evidence_paper(p,'evidence.client.v2','Revised V2','Q3 product source',v2,15.25,6.08,8.88,4.35,['Channel restocking supported','sales volume','whether restocking continues, alongside'])
    p.route('draft.to.v1',[(13.33,5.63),(13.33,5.83),(10.28,5.83),(10.28,5.98)],PURPLE)
    p.node('tool.review.match','Document tools','Match passages',M,11.15,4.50,1.75,'tool',size=11.5)
    p.node('role.llm.revises','LLM revises','Explain mismatches\nPropose edits',11.65,11.15,4.80,1.75,'llm',size=11.5)
    p.node('human.approval','Author / reviewer','Author approves\nMiddle office checks',18.00,11.15,6.13,1.75,'human',size=11.5)
    p.line('v1.to.match',8.98,10.53,8.98,11.05,PURPLE)
    p.route('current.sources.to.match',[(20.575,5.63),(20.575,5.80),(14.50,5.80),(14.50,10.77),(8.98,10.77)],GRAY,.75,False)
    p.line('matched.passages.to.llm',11.33,12.025,11.55,12.025)
    p.route('revisions.to.v2',[(16.55,12.025),(16.80,12.025),(16.80,10.53)],PURPLE)
    p.line('v2.to.human.approval',21.05,10.53,21.05,11.05,PURPLE)

def records_workflow(p):
    p.family='Received document, manual capture, source validation and business record'
    p.document('input.received.document','Fax / form','Received information\nRequired fields',M,4.50,4.50,3.45,GRAY,12)
    p.node('human.operations.capture','Operations','Read / enter fields',12.20,4.50,4.05,2.05,'human',size=11.5)
    p.document('record.unchecked','Entered record','Fields awaiting validation',17.02,4.50,7.11,2.05,GRAY,11.5)
    p.line('document.to.capture',11.33,5.525,12.10,5.525);p.line('capture.to.record',16.35,5.525,16.92,5.525)
    p.node('human.operations.validate','Operations','Check source\nCorrect fields',12.20,9.00,4.05,2.20,'human',size=11.5)
    p.document('output.business.record','Business record','Validated fields\nSource reference',17.02,9.00,7.11,2.20,GRAY,11.5)
    p.route('record.to.validation',[(20.575,6.65),(20.575,7.85),(14.225,7.85),(14.225,8.90)])
    p.route('source.to.validation',[(8.98,8.05),(8.98,10.10),(12.10,10.10)],GRAY,.75)
    p.line('validated.to.record',16.35,10.10,16.92,10.10)
    p.caption('records.pain','Repeated reading, field entry and source checks',M,12.15,MW,12,BLUE,.48)

def records_proposal(p):
    p.family='Attributed HuaAn extraction evidence and separate company extraction-validation-record proposal'
    p.caption('case.huaan','HuaAn: automated fax entry',M,4.08,MW,13,BLUE,.55)
    p.document('huaan.input','Fax / form','Direct-sales counter',M,4.95,4.50,1.85,GRAY,11.5)
    p.node('huaan.model','Model extracts','Required fields',12.20,4.95,4.05,1.85,'llm',size=11.5)
    p.node('huaan.output','Client-service record','Populated fields',17.02,4.95,7.11,1.85,'material',size=11.5)
    p.line('huaan.doc.to.model',11.33,5.875,12.10,5.875);p.line('huaan.model.to.record',16.35,5.875,16.92,5.875)
    p.caption('huaan.metric','Direct-sales counter: more than 80% of faxes entered automatically',M,7.10,MW,11,BLUE,.50)
    p.caption('proposal.record.entry','Proposed application: record entry and validation',M,8.25,MW,13,BLUE,.55)
    p.document('company.record.input','Document','Source information',M,9.15,3.20,2.25,GRAY,10.5)
    p.node('company.record.llm','LLM extracts','Required fields',10.43,9.15,3.70,2.25,'llm',size=11.5)
    p.node('company.record.validation','Operations','Validate source\nCorrect fields',14.63,9.15,4.20,2.25,'human',size=11.5)
    p.document('company.record.output','Business record','Validated fields\nSource reference',19.33,9.15,4.80,2.25,GRAY,11.5)
    for j,(a,b) in enumerate([(9.93,10.33),(14.23,14.53),(18.93,19.23)]):p.line('record.entry.sequence.'+str(j),a,10.275,b,10.275)
    p.caption('record.accountability','Staff validate the extracted information before record entry',M,12.05,MW,11.5,GRAY,.50)

CUSTOM={3:firm_map,11:client_workflow,12:client_peers,13:client_proposal,17:records_workflow,18:records_proposal,22:lambda p:firm_map(p,True)}
NARRATION={
1:"This report considers how LLMs could support colleagues in a mainland asset manager. It follows front-office, middle-office and back-office work. Industry examples establish reported uses, and the company proposals connect those uses to specific employee tasks. Company A and a quarterly client update provide recurring examples. The six application areas cover research, trading support, client communications, risk analysis, record entry and tool development.",
2:"Documents, data, messages and business requests supply information for employee tasks. The LLM reads, compares, explains and drafts. Tools retrieve information, query systems, calculate results and execute operations. Approved documents, knowledge bases and business data provide shared sources, with references and version history available for checking. The application returns company analysis, quote summaries, client materials or working tools. Colleagues check the source basis and use the output in their work.",
3:"The six application areas follow the firm's work from front office to middle office and back office. Front-office areas are company research, trading support and client communications. Client communications includes drafting, source review, revision and approval, with middle-office reviewers participating in that workflow. Risk analysis connects credit events to exposures and follow-up. Back-office areas are record entry and tool development. Company A connects research, trading and risk information. The quarterly client update connects drafting and review, and supplies examples for the comparison-tool requirement.",
11:"The client team begins with a client question, investment views, product information and previous material. The front-office author selects relevant information and drafts the explanation. A middle-office reviewer checks the draft against current sources, including fund details, reporting periods and risk wording. The reviewer explains any issues so the author can revise the material. Review and approval lead to an approved client communication. Repeated source searches, manual checks and revision handoffs make this preparation work a candidate for support.",
12:"ICBCUBS FundGPT supports institutional RFP drafting through internal knowledge and source retrieval. In the RFP illustration, a question about investment research leads to relevant responsibilities and a source-backed response. The business team checks the answer and source. Penghua's marketing-material review applies review requirements and produces explained suggested edits, including fund information and risk wording. Authors revise material and reviewers check it. Penghua reported a ninety-one-percent acceptance rate for suggested edits. Yingmi separately supports initial checks, revision and repeat review; that reported scope provides another example of review follow-through.",
13:"The author supplies the client question, investment view and relevant product material. The LLM drafts V1. Its investment view states that higher sales volume drove Company A's revenue and retains raw-material-cost monitoring. Current review sources add channel restocking and uncertainty over whether it continues. Document tools match the draft with relevant source passages. The LLM explains the mismatches and proposes revisions. V2 adds the restocking driver and continuation question while retaining cost monitoring. The author approves the edits, and the middle-office reviewer checks the sources and revised material before approval. The full fund name, Q3 product source and specific risk disclosure are also part of V2.",
17:"Operations receives a fax or form, reads its content and enters the required fields. Staff check the entered information against the original document, correct errors or omissions and create the business record with its source reference. Reading the same material, rekeying fields and repeating source checks consume staff time. The purpose of this workflow is an accurate record that colleagues can use in subsequent operations.",
18:"HuaAn reports automated entry for more than eighty percent of faxes handled by its direct-sales counter. Its model reads document content, extracts required fields and populates client-service records. Our proposed application starts with incoming documents and uses an LLM to extract required fields. Operations checks those fields against the source, corrects them and enters the validated business record. The proposed workflow keeps source references with the record and places staff validation before record entry.",
22:"The six proposals give colleagues concrete outputs. Analysts receive research summaries with sources. Traders receive holdings and received-quote summaries. Client teams receive drafted and reviewed materials, with middle-office review contributing to approval. Risk teams receive exposure assessments and follow-up items. Operations receives extracted fields for validation and record entry. Developers receive code and tests for an internal comparison tool. Colleagues verify those outputs and exercise professional judgment in their use.",
23:"Company A provides a common issuer identity across research, trading support, risk and issuer-related records. Colleagues share company analysis, bond and quote summaries, event assessments and exposure information. Approved information supports maintained records in operations. The quarterly client update connects the client team's V1 with the author and reviewer's approved V2. Approved material then supports filing and related-material updates. Shared source references and version history support these handoffs across the front, middle and back offices."
}

def notes_body(root):
    for s in root.findall('.//p:sp',NS):
        ph=s.find('./p:nvSpPr/p:nvPr/p:ph',NS)
        if ph is not None and ph.get('type')=='body':return s.find('./p:txBody',NS)
    raise ValueError('Missing notes body')

def notes_record(i):
    old=OLD_NOTES[BASE[i-1]-1];speech=NARRATION.get(i,old['narration']);support=list(old['supporting_wording'])
    if i==2:support=['Shared sources: approved documents, knowledge bases and business data. Preserve source references and version history for checking.']
    if i==3:support=[]
    if i==11:support=['Preparation uses portfolio-manager views, product information and previous client communications. Middle-office review checks the current fund details, period, investment view and risk disclosure.']
    if i==12:support=['ICBCUBS FundGPT supports knowledge-base maintenance, question analysis, review and RFP drafting.','Penghua applies 71 review rules across seven categories. Its reported 91% figure concerns acceptance of suggested edits.','Yingmi accepts text or files, identifies issues and reasons, suggests changes and supports repeat review after revision.']
    if i==13:
        support=list(OLD_NOTES[17]['supporting_wording'])+list(OLD_NOTES[23]['supporting_wording'])+['Current portfolio-manager source: channel restocking lifted sales volume; continuation remains uncertain. Raw-material-cost monitoring is retained.','These V1/V2 materials illustrate the company proposal.']
    if i==17:support=['Current capture workflow: read incoming faxes/forms, enter fields, validate against the source and create the business record.']
    if i==18:support=['HuaAn reports automated data entry for more than 80% of faxes handled by its direct-sales counter.','In the company proposal, operations validates extracted fields against incoming documents before record entry.','ICBCUBS FundGPT also supports comparison of two existing PDF, Word or scanned versions, difference highlighting, typo checking and export.']
    if i==22:support=[]
    if i==24:
        support+=['Implementation support: use approved documents, knowledge bases and business data. Define access controls, source references, version ownership and maintenance responsibility. LLMs interpret and draft; tools query systems, calculate, process files and run code/tests. Qwen and DeepSeek are candidates for evaluation on the company tasks.']
    urls=[]
    for oldi in INPUTS[i-1]:urls+=OLD_NOTES[oldi-1]['source_urls']
    urls=list(dict.fromkeys(urls))
    sections=['Suggested spoken explanation',speech]
    if support or urls:sections+=['','Sources and supporting material','\n\n'.join(support),'\n'.join(urls)]
    return {'slide':i,'original_pages':INPUTS[i-1],'narration':speech,'supporting_wording':support,'source_urls':urls,'full_notes':'\n'.join(sections)}

def footer_for(i,oldroot):
    if i==12:return 'Sources: ICBCUBS; Penghua / AMAC; Yingmi'
    if i==13:return 'Sources: Tianhong; Penghua / AMAC; Yingmi'
    if i==18:return 'Sources: HuaAn / CCF'
    for s in oldroot.findall('.//p:sp',NS):
        if shape_name(s)=='source.note':return ' '.join(s.xpath('.//a:t/text()',namespaces=NS))
    return None

def xmlbytes(r):return E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True)

def main():
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SHA
    QA.mkdir(parents=True,exist_ok=True)
    with ZipFile(SOURCE) as z:data={x:z.read(x) for x in z.namelist()}
    out={k:v for k,v in data.items() if not re.match(r'ppt/(slides|notesSlides)/(slide\d+\.xml|notesSlide\d+\.xml|_rels/(slide|notesSlide)\d+\.xml\.rels)$',k)}
    PR='http://schemas.openxmlformats.org/package/2006/relationships';CT='http://schemas.openxmlformats.org/package/2006/content-types'
    manifest=[];records=[]
    for i,oldi in enumerate(BASE,1):
        oldroot=E.fromstring(data[f'ppt/slides/slide{oldi}.xml'])
        content={'!!heading':PLAN[i-1]['title'],'!!subtitle':PLAN[i-1]['subtitle']}
        if i==1:content.update({'!!cover.title':PLAN[0]['title'],'!!cover.kicker':PLAN[0]['subtitle']})
        foot=footer_for(i,oldroot)
        if foot:content['!!source']=foot
        p=Page(i,oldroot,content)
        if i in CUSTOM:CUSTOM[i](p)
        else:
            retained(p,oldroot)
            if i==2:
                change(p,'scope.purpose','Colleagues check outputs against approved sources')
                for name,xx,ww in [('tool.request.label',11.80,1.15),('tool.result.label',15.45,1.10)]:
                    sh=next(q for q in p.tree if shape_name(q)==name)
                    xf=sh.find('./p:spPr/a:xfrm',NS);xf.find('./a:off',NS).set('x',str(cm(xx)));xf.find('./a:ext',NS).set('cx',str(cm(ww)))
            if i==7:
                for name,xx,ww in [('calculate.request.label',13.35,1.40),('calculate.return.label',15.45,1.10)]:
                    sh=next(q for q in p.tree if shape_name(q)==name)
                    xf=sh.find('./p:spPr/a:xfrm',NS);xf.find('./a:off',NS).set('x',str(cm(xx)));xf.find('./a:ext',NS).set('cx',str(cm(ww)))
            if i==23:
                change(p,'issuer.office.state.2','Operations\nIssuer-related records\nValidated information')
                change(p,'client.office.state.1','Approved V2\nAuthor / reviewer')
                change(p,'client.office.state.2','Approved material\nFiling / related updates')
        for j,cn in enumerate(p.root.findall('.//p:cNvPr',NS),1):cn.set('id',str(j))
        out[f'ppt/slides/slide{i}.xml']=xmlbytes(p.root)
        rel=E.fromstring(data[f'ppt/slides/_rels/slide{oldi}.xml.rels'])
        for r in list(rel):
            if r.get('Type','').endswith('/slide'):rel.remove(r)
            elif r.get('Type','').endswith('/notesSlide'):r.set('Target',f'../notesSlides/notesSlide{i}.xml')
        out[f'ppt/slides/_rels/slide{i}.xml.rels']=xmlbytes(rel)
        rec=notes_record(i);records.append(rec)
        nr=E.fromstring(data[f'ppt/notesSlides/notesSlide{oldi}.xml']);body=notes_body(nr)
        for q in body.findall('./a:p',NS):body.remove(q)
        for line in rec['full_notes'].split('\n'):
            q=n(body,A,'p');r=n(q,A,'r');pr=n(r,A,'rPr',sz='1200');n(pr,A,'latin',typeface='Arial');n(r,A,'t').text=line
        out[f'ppt/notesSlides/notesSlide{i}.xml']=xmlbytes(nr)
        nrel=E.fromstring(data[f'ppt/notesSlides/_rels/notesSlide{oldi}.xml.rels'])
        for r in nrel:
            if r.get('Type','').endswith('/slide'):r.set('Target',f'../slides/slide{i}.xml')
        out[f'ppt/notesSlides/_rels/notesSlide{i}.xml.rels']=xmlbytes(nrel)
        manifest.append({'slide':i,'original_pages':INPUTS[i-1],'base_original_page':oldi,'main_or_appendix':'main' if i<=25 else 'appendix','title':PLAN[i-1]['title'],'subtitle':PLAN[i-1]['subtitle'],'family':p.family,'new_composition':i in CUSTOM,'custom_spans':p.custom})
    pres=E.fromstring(data['ppt/presentation.xml']);ids=pres.find('./p:sldIdLst',NS)
    for q in list(ids):ids.remove(q)
    rel=E.fromstring(data['ppt/_rels/presentation.xml.rels'])
    for q in list(rel):
        if q.get('Type','').endswith('/slide'):rel.remove(q)
    for i in range(1,29):
        q=n(ids,P,'sldId',id=255+i);q.set('{'+R+'}id','rIdNewSlide'+str(i))
        E.SubElement(rel,'{'+PR+'}Relationship',Id='rIdNewSlide'+str(i),Type=R+'/slide',Target=f'slides/slide{i}.xml')
    out['ppt/presentation.xml']=xmlbytes(pres);out['ppt/_rels/presentation.xml.rels']=xmlbytes(rel)
    ct=E.fromstring(data['[Content_Types].xml'])
    for q in list(ct):
        if re.match(r'/ppt/(slides/slide|notesSlides/notesSlide)\d+\.xml$',q.get('PartName','')):ct.remove(q)
    for i in range(1,29):
        E.SubElement(ct,'{'+CT+'}Override',PartName=f'/ppt/slides/slide{i}.xml',ContentType='application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
        E.SubElement(ct,'{'+CT+'}Override',PartName=f'/ppt/notesSlides/notesSlide{i}.xml',ContentType='application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml')
    out['[Content_Types].xml']=xmlbytes(ct)
    app=E.fromstring(data['docProps/app.xml'])
    for q in app:
        if E.QName(q).localname in ['Slides','Notes']:q.text='28'
    out['docProps/app.xml']=xmlbytes(app)
    with ZipFile(BUILD/'candidate.pptx','w',ZIP_DEFLATED) as z:
        for name,value in out.items():
            info=ZipInfo(name,date_time=(2026,10,30,0,0,0));info.compress_type=ZIP_DEFLATED;z.writestr(info,value)
    (ROOT/'src/speaker-notes.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
    (ROOT/'src/page-plan.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    (QA/'layout-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    print('Built 25 main + 3 appendix slides:',hashlib.sha256((BUILD/'candidate.pptx').read_bytes()).hexdigest())
if __name__=='__main__':main()
