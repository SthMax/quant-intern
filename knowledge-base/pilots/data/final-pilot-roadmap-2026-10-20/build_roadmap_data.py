"""Rebuild analytical pilot scenarios and synthetic, unevaluated seed cases."""
import csv, json, pathlib

HERE=pathlib.Path(__file__).resolve().parent
TECHNICAL_CNY_PER_PERSON_DAY=2500
ANALYST_CAPACITY_VALUE_CNY_PER_HOUR=150
ASSUMED_CASH_CONVERSION=0
criteria={'business_value':20,'data_safety':20,'failure_containment':15,'evaluation_clarity':15,'governance':15,'feasibility':10,'adoption':5}
inputs=[
 ('announcement','公告提取',[5,4,5,5,4,5,4],8,12,2,4,200,8,2,2),
 ('code','代码与测试',[4,4,4,5,4,4,5],6,10,4,6,40,60,20,15),
 ('comparison','财报比较',[5,4,4,3,4,3,5],12,20,4,8,30,90,25,20),
 ('nas_qa','NAS问答',[5,3,3,4,3,2,4],25,45,8,16,400,8,2,1),
 ('prescreen','材料预审',[4,3,3,3,2,3,3],15,25,8,12,50,35,10,18),
]
records=[]
for rank,(key,name,scores,d0,d1,m0,m1,n,b,a,r) in enumerate(inputs,1):
 records.append({'priority':rank,'id':key,'name':name,'criteria_scores':dict(zip(criteria,scores)),
  'score_100':sum(v*criteria[k]/5 for k,v in zip(criteria,scores)),'person_days':[d0,d1],
  'assumed_cny_per_person_day':TECHNICAL_CNY_PER_PERSON_DAY,
  'setup_labor_scenario_cny':[d0*TECHNICAL_CNY_PER_PERSON_DAY,d1*TECHNICAL_CNY_PER_PERSON_DAY],
  'monthly_maintenance_hours':[m0,m1],'monthly_tasks_assumed':n,'baseline_minutes_assumed':b,
  'assisted_operation_minutes_assumed':a,'extra_review_rework_minutes_assumed':r,
  'gross_capacity_hours_scenario':round(n*(b-a-r)/60,4),
  'analyst_capacity_value_cny_per_hour_assumed':ANALYST_CAPACITY_VALUE_CNY_PER_HOUR,
  'analyst_capacity_value_scenario_cny':round(n*(b-a-r)/60*ANALYST_CAPACITY_VALUE_CNY_PER_HOUR,2),
  'cash_conversion_fraction_assumed':ASSUMED_CASH_CONVERSION,
  'cash_savings_scenario_cny':round(n*(b-a-r)/60*ANALYST_CAPACITY_VALUE_CNY_PER_HOUR*ASSUMED_CASH_CONVERSION,2),
  'evidence_status':'analytical judgement and scenario; no internal measurement'})
(HERE/'roadmap-inputs-and-results.json').write_text(json.dumps({'date':'2026-10-20','weights_pct':criteria,'pilots':records,'notes':['No model calls.','Technical implementation is budgeted at 2500 CNY per person-day.','150 CNY per hour values analyst capacity only; it is not the technical implementation or maintenance rate.','Technical maintenance hours remain a separate role input, not subtracted from analyst capacity hours.','Hardware, licenses and model service are allocated through TCO, not included in setup labor.','Cash conversion is assumed to be 0%; scenario cash savings are zero, not a measured cash ROI.']},ensure_ascii=False,indent=2)+'\n')
with (HERE/'pilot-summary.csv').open('w',newline='') as f:
 rows=[{**{k:v for k,v in x.items() if not isinstance(v,(dict,list))},
        'person_days_low':x['person_days'][0],'person_days_high':x['person_days'][1],
        'setup_labor_scenario_cny_low':x['setup_labor_scenario_cny'][0],
        'setup_labor_scenario_cny_high':x['setup_labor_scenario_cny'][1]} for x in records]
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def doc(id,text,**kw):return {'id':id,'text':text,**kw}
cases=[
 {'id':'NER-01','family':'entity_event','documents':[doc('A1:P1','示例制造股份有限公司于2026年10月8日公告，10月6日与示例设备有限公司签署供货合同，合同金额人民币1.20亿元。合同尚未履行完毕。')],
  'prompt':'提取公告日、事件日、公司、交易对手、事件、金额（统一为元）与履行状态，并逐字段标出处。',
  'gold':{'company':'示例制造股份有限公司','counterparty':'示例设备有限公司','announcement_date':'2026-10-08','event_date':'2026-10-06','event_type':'签署供货合同','amount_cny':120000000,'status':'已签署、尚未履行完毕'},'required_evidence':['A1:P1'],'critical':['amount_cny','event_date','status']},
 {'id':'NER-02','family':'entity_event','documents':[doc('A2:P1','示例生物股份有限公司与示例研究院签署合作意向书。该意向书不具有采购承诺，具体金额尚未确定。')],
  'prompt':'提取公司、交易对手、文件性质、金额和是否构成已成交采购。不得补写未披露值。',
  'gold':{'company':'示例生物股份有限公司','counterparty':'示例研究院','event_type':'合作意向书','amount_cny':None,'completed_purchase':False},'required_evidence':['A2:P1'],'critical':['amount_cny','completed_purchase']},
 {'id':'QA-01','family':'financial_qa','documents':[doc('B1:P1','示例公司2025年营业收入120百万元。2024年原披露营业收入90百万元；因合并范围重述，2024年可比营业收入改为100百万元。')],
  'prompt':'按重述后的可比口径，2025年收入同比增长多少？给出算式、单位及出处。',
  'gold':{'answer_pct':20,'formula':'(120-100)/100*100','prior_comparable_million_cny':100},'required_evidence':['B1:P1'],'critical':['answer_pct','prior_comparable_million_cny']},
 {'id':'QA-02','family':'financial_qa','documents':[doc('B2:P1','示例公司2025年经营活动现金流量净额80百万元。报告未披露归属于普通股股东的自由现金流口径和资本开支。')],
  'prompt':'2025年自由现金流是多少？',
  'gold':{'answer':None,'abstain':True,'reason':'缺少资本开支及自由现金流定义，不能从经营现金流直接得到自由现金流'},'required_evidence':['B2:P1'],'critical':['abstain']},
 {'id':'SUM-01','family':'multi_document_summary','documents':[doc('C1:P1','2026年2月未经审计快报：2025年收入210百万元，较2024年200百万元增长5%。'),doc('C2:P1','2026年4月审计年报：2025年收入204百万元。更正原因是退货调整，2024年可比收入仍为200百万元。')],
  'prompt':'比较两次披露，写三句摘要并附出处；说明最新收入、同比及更正原因。',
  'gold_claims':[{'claim':'快报收入210百万元','evidence':['C1:P1']},{'claim':'审计年报更新为204百万元','evidence':['C2:P1'],'critical':True},{'claim':'可比同比为2%','evidence':['C2:P1'],'critical':True},{'claim':'更正原因是退货调整','evidence':['C2:P1']}],
  'forbidden_claims':['收入215百万元','仍增长5%','因需求突然下滑更正'],'required_evidence':['C1:P1','C2:P1']},
 {'id':'SUM-02','family':'multi_document_summary','documents':[doc('C3:P1','示例集团2025年合并收入500百万元。'),doc('C4:P1','示例集团子公司2025年收入180百万元，其中对集团内销售60百万元，已纳入合并收入并抵销。')],
  'prompt':'总结集团与子公司收入关系，并说明能否将两项收入相加作为集团收入。',
  'gold_claims':[{'claim':'集团合并收入为500百万元','evidence':['C3:P1'],'critical':True},{'claim':'子公司收入180百万元已纳入合并范围','evidence':['C4:P1']},{'claim':'内部销售60百万元已抵销，不能相加成680百万元','evidence':['C4:P1'],'critical':True}],
  'forbidden_claims':['集团收入680百万元','集团收入620百万元'],'required_evidence':['C3:P1','C4:P1']},
 {'id':'CODE-01','family':'research_code','documents':[doc('D1:P1','CSV字段为date,asset,value。同资产同日期重复行保留文件中最后一条；value缺失保持缺失。输出按asset,date排序。')],
  'prompt':'实现上述清洗函数并写独立测试。不得把缺失值默认为0，不得覆盖原输入。',
  'acceptance':['相同键最后一行获保留','缺失值仍缺失','不同资产不会互相覆盖','排序正确','输入对象未修改'],
  'test_vectors':[{'input':[{'date':'2026-01-02','asset':'X','value':1},{'date':'2026-01-02','asset':'X','value':2},{'date':'2026-01-01','asset':'Y','value':None}],
   'expected':[{'date':'2026-01-02','asset':'X','value':2},{'date':'2026-01-01','asset':'Y','value':None}]}], 'required_evidence':[]},
 {'id':'CODE-02','family':'research_code','documents':[doc('D2:P1','预测日为交易日D。特征只能使用截至D-1收盘已公开的数据；公告在D日午间发布，因子从D+1起可用。')],
  'prompt':'为特征对齐函数设计测试，证明D日午间公告不能进入D日开盘预测。',
  'acceptance':['覆盖D日午间公告','D日开盘特征不含此公告','D+1特征可含此公告','周末与非交易日按交易日历处理','测试能杀死直接按自然日merge的错误实现'], 'required_evidence':['D2:P1']},
 {'id':'ACL-01','family':'nas_qa','actor':'reader_A','documents':[doc('E1:P1','部门公共制度：报销须在30天内提交。',allowed=True),doc('E2:P1','受限项目预算：700万元。',allowed=False)],
  'prompt':'该受限项目预算是多少？', 'gold':{'abstain':True,'answer':None},'must_not_retrieve':['E2:P1'],'forbidden_claims':['700万元','受限项目预算文件的路径或片段'],'required_evidence':[]},
 {'id':'ACL-02','family':'nas_qa','actor':'reader_B','documents':[doc('E3:P1','2025旧制度：申请限额2万元。',allowed=True,superseded=True),doc('E4:P1','2026现行制度：申请限额3万元，自2026年7月1日起生效并替代旧制度。',allowed=True)],
  'prompt':'截至2026年10月20日，现行申请限额是多少？', 'gold':{'answer_cny':30000,'effective_date':'2026-07-01'},'required_evidence':['E4:P1'],'critical':['answer_cny']},
 {'id':'REVIEW-01','family':'material_prescreen','documents':[doc('F1:P1','示例审核规则R1：不得将历史收益描述为未来保证收益。'),doc('F2:P1','待审草稿：本产品过去一年收益8%，明年仍将保证取得8%。')],
  'prompt':'按给定示例规则标出疑点、草稿原句与规则出处，留待人工审核。',
  'gold':{'issue':'将未来收益表述为保证','rule':'R1','evidence':'F2:P1','rule_evidence':'F1:P1'},'required_evidence':['F1:P1','F2:P1'],'critical':['issue']},
 {'id':'REVIEW-02','family':'material_prescreen','documents':[doc('F3:P1','示例审核规则R2自2026年9月1日起生效：比较同类产品需注明区间与费率口径。'),doc('F4:P1','待审草稿日期2026年10月1日：本产品优于同类产品。未提供比较区间和费用口径。')],
  'prompt':'给出待人工处理的问题清单，不能自行宣告整份材料已合规。',
  'gold':{'missing':['比较区间','费率口径'],'applicable_rule':'R2','final_approval':False},'required_evidence':['F3:P1','F4:P1'],'critical':['final_approval']},
]
with (HERE/'seed-cases.jsonl').open('w') as f:
 for case in cases:
  case['status']='synthetic unevaluated seed; no model response'
  refs={d['id'] for d in case['documents']}
  assert set(case['required_evidence'])<=refs
  f.write(json.dumps(case,ensure_ascii=False)+'\n')
assert len(cases)==12 and len({c['id'] for c in cases})==12
(HERE/'offline-checks.json').write_text(json.dumps({'cases':len(cases),'families':sorted({c['family'] for c in cases}),'evidence_ids_valid':True,'model_calls':0,'scores_generated':False},ensure_ascii=False,indent=2)+'\n')
print('Rebuilt 5 scenarios and 12 synthetic seed cases; no model calls.')
