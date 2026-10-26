from pathlib import Path
import json
R=Path(__file__).resolve().parent.parent
(R/'build/qa').mkdir(parents=True,exist_ok=True)
(R/'output').mkdir(parents=True,exist_ok=True)
C={'issuer':'317F7B','issuerTint':'EFF6F4','client':'7363A6','clientTint':'F3F0F8','neutral':'F3F7FA','ink':'20262C','muted':'707C88','yellow':'FFF0BE','blue':'005A9C'}
P={i:{'page':i,'header':[],'neutral_roots':[],'text_neutral':[],'styles':[],'overlays':[],'note':''} for i in range(1,34)}
def header(i,kind,qualifier=''):
 P[i]['header'].append({'kind':kind,'name':{'issuer':'甲公司','client':'客户沟通稿','neutral':'机构标书'}[kind],'qualifier':qualifier})
def neutral(i,*names):P[i]['neutral_roots']+=list(names)
def textneutral(i,*names):P[i]['text_neutral']+=list(names)
def style(i,name,**v):P[i]['styles'].append({'name':'!!'+name,**v})
def bar(i,name,kind,x,y,h,w=6):P[i]['overlays'].append({'type':'bar','name':'!!story.'+kind+'.'+name,'x':x,'y':y,'w':w,'h':h,'color':C[kind]})
def label(i,name,kind,text,x,y,w,h=34,size=22):P[i]['overlays'].append({'type':'text','name':'!!story.'+kind+'.'+name,'x':x,'y':y,'w':w,'h':h,'text':text,'size':size,'color':C[kind]})
for i in [3,29,30]:header(i,'issuer');header(i,'client')
for i in [4,5,6,7,8,9,10,11,19,20,21]:header(i,'issuer','方法参考' if i in [5,6,7,10,20] else '')
for i,q in {12:'材料准备',13:'观点准备',15:'V1编写',16:'V1审核',17:'V1审核',18:'V2修订',22:'文件示例',23:'版本比对',24:'变更说明',25:'开发样例',26:'方法参考',27:'开发样例'}.items():header(i,'client',q)
header(14,'neutral','独立案例')
neutral(2,*['scope.work'+str(i) for i in range(4)])
neutral(4,'research.question',*['research.manual.'+str(i) for i in range(4)])
for j,x in enumerate([426,810,1194],1):
 bar(4,'source.'+str(j),'issuer',x-12,333,133)
 style(4,f'research.evidence.{j}.label',text=C['issuer']);style(4,f'research.evidence.{j}.rule',line=C['issuer'])
neutral(5,'driver.tools')
P[5]['note']='天弘公司名称及通用驱动树保留品牌蓝；页眉甲公司标记注明方法参考，工具为中性。'
neutral(6,'views.method');textneutral(6,'views.consensus.title','views.difference.title')
for k,x in [('reportA',426),('reportB',810)]:
 bar(6,'views.'+k,'issuer',x-12,330,197);style(6,'views.'+k+'.label',text=C['issuer']);style(6,'views.'+k+'.rule',line=C['issuer'])
bar(6,'analysis','issuer',420,592,126);style(6,'views.result',line=C['issuer'])
neutral(7,'elements.left','elements.right',*['element.'+str(i)+'.source' for i in range(3)])
bar(7,'source.group','issuer',414,375,278);bar(7,'analysis.table','issuer',778,375,288)
neutral(8,'research.question','research.llm','research.tool');textneutral(8,'research.result.title')
bar(8,'source.group','issuer',414,310,294);bar(8,'analysis','issuer',420,633,93)
for j in range(1,4):style(8,f'research.evidence.{j}.label',text=C['issuer']);style(8,f'research.evidence.{j}.rule',line=C['issuer'])
style(8,'research.result',line=C['issuer'])
neutral(9,'trade.intent','trade.query','trade.inquire','trade.compare','trade.system','trade.counterparty');textneutral(9,'trade.data.label')
bar(9,'inquiry.subject','issuer',436,374,29,4)
neutral(10,*[f'trade.case{k}.{j}' for k in [1,2] for j in range(4)])
P[10]['note']='南方与兴证全球名称仍为蓝底白字；主线标签仅表示当前甲公司叙事的方法参考。'
neutral(11,'trade.intent','trade.llm.query','trade.system','trade.llm.quote');textneutral(11,'trade.result.title')
bar(11,'quote.table','issuer',420,598,126);bar(11,'holdings.data','issuer',820,389,96,4);bar(11,'quote.record','issuer',1204,420,60,4)
neutral(12,*['client.material'+str(i) for i in range(3)],*['client.manual.'+str(i) for i in range(3)])
bar(12,'prior.material','client',1188,474,68)
neutral(13,'client.views.llm');style(13,'client.views.result',line=C['client']);style(13,'client.views.result.title',text=C['client']);bar(13,'view.summary','client',420,584,126)
neutral(14,'tender.question','tender.llm','tender.answer');P[14]['note']='机构标书是独立案例，使用中性页眉，不归为同一份客户沟通稿。'
neutral(15,'client.input.customer','client.input.manager','client.input.product','client.llm')
neutral(17,'comment.meta','comment.view','comment.risk')
neutral(18,'review.inputs','review.tool','review.llm')
for i,x,y,w,h in [(15,1008,245,524,510),(16,426,289,690,435),(17,426,289,690,435),(18,1008,245,524,510)]:
 style(i,'clientDoc',line=C['client']);style(i,'clientDoc.title',text=C['client']);style(i,'clientDoc.version',text=C['client']);style(i,'clientDoc.rule',line=C['client']);bar(i,'document','client',x-6,y,h)
 for key in ['product','period','view','risk']:style(i,'clientDoc.label.'+key,text=C['ink'])
for key in ['product','period','view','risk']:style(18,'clientDoc.highlight.'+key,fill=C['yellow'])
bar(18,'input.record','client',436,307,32,4)
neutral(19,*['risk.question.'+str(i) for i in range(3)]);textneutral(19,'risk.mail.label');bar(19,'event.mail','issuer',414,255,144);style(19,'risk.mail.rule',line=C['issuer'])
neutral(20,'risk.mail.extract','risk.rules.tool','risk.event.llm')
P[20]['note']='汇添富、天弘案例名称保持品牌蓝，邮件/条款工具和LLM块均中性；甲公司只作方法参考标记。'
neutral(21,'risk.evidence.system','risk.llm');style(21,'risk.result',fill='FFFFFF',line=C['issuer']);style(21,'risk.result.role',text=C['issuer'])
for k,y,h in [('mail',252,122),('rule',585,123)]:
 bar(21,'event.'+k,'issuer',414,y,h);style(21,'risk.evidence.'+k+'.label',text=C['issuer']);style(21,'risk.evidence.'+k+'.rule',line=C['issuer'])
bar(21,'holdings.data','issuer',436,475,62,4);bar(21,'impact.report','issuer',1188,299,371)
neutral(22,*[f'ops.row{i}.{j}' for i in range(3) for j in range(3)])
bar(22,'file.versions','client',420,482,87);bar(22,'file.differences','client',1176,482,87)
P[22]['note']='客户稿版本输入和差异清单单独标紫；通用传真与其他文件保持中性，不把整页染紫，也不虚构甲公司单据。'
neutral(23,'ops.form','ops.compare.read')
style(23,'ops.compare.old.label',text=C['client']);style(23,'ops.compare.new.label',text=C['client']);bar(23,'version.v1','client',810,470,111);bar(23,'version.v2','client',810,599,122)
P[23]['note']='工银瑞信和华安名称保持品牌蓝，通用传真区域中性；V1/V2文字材料同紫，新增文字仍淡黄。'
neutral(24,'ops.inputs','ops.tool','ops.llm');style(24,'changeLog',line=C['client']);style(24,'changeLog.title',text=C['client']);style(24,'changeLog.rule',line=C['client']);bar(24,'input.record','client',436,307,32,4);bar(24,'change.explanation','client',1002,245,510)
neutral(25,'dev.request','dev.requirements','dev.code','dev.debug');bar(25,'development.sample','client',414,302,33);label(25,'development.sample.name','client','客户沟通稿 V1 / V2',426,300,650)
neutral(26,'dev.requirements','dev.code','dev.test','dev.case.result');bar(26,'development.sample','client',414,327,33);label(26,'development.sample.name','client','客户沟通稿 V1 / V2',426,325,338)
neutral(27,'dev.request','dev.samples','dev.generate','dev.test','dev.deliver','dev.revise','dev.feedback');textneutral(27,'dev.testFeedback.label');bar(27,'development.sample','client',436,399,31,4);style(27,'dev.samples.body',paragraph=0,text=C['client'])
for i in [25,26,27]:P[i]['note']='紫色只给两版客户稿这一开发样例；开发人员、代码、测试、反馈和修订块保持中性。'
neutral(28,*[f'other.{i}.flow.{j}' for i in range(3) for j in range(3)])
for j in range(3):
 style(30,f'cross.0.{j}',fill=C['issuerTint'],text=C['ink']);style(30,f'cross.1.{j}',fill=C['clientTint'],text=C['ink'])
P[30]['note']='两条主线并列：上行甲公司极浅青绿、下行客户稿极浅紫；对象名及对应连接线沿用各自主线色。'
neutral(31,'arch.entry','arch.workflow','arch.model','arch.tools')
neutral(33,*['evaluation.flow.'+str(i) for i in range(4)])
for i in [1,2,28,31,32,33]:P[i]['note']=P[i]['note'] or '通用说明保持中性，不新增主线归属；原导航、阶段文字、页码与布局不变。'
# Bind body markers to the corresponding source object; page headers stay visible.
P[7]['overlays']=[]
for j,y in enumerate([375,478,581]):
 bar(7,'source.row.'+str(j),'issuer',414,y,72)
 bar(7,'analysis.row.'+str(j),'issuer',778,y,82)
owners={
4:{**{'issuer.source.'+str(j):'research.evidence.'+str(j)+'.rule' for j in range(1,4)}},
6:{'issuer.views.reportA':'views.reportA.rule','issuer.views.reportB':'views.reportB.rule','issuer.analysis':'views.result'},
7:{**{'issuer.source.row.'+str(j):'element.'+str(j)+'.source' for j in range(3)},**{'issuer.analysis.row.'+str(j):'element.'+str(j)+'.label' for j in range(3)}},
8:{'issuer.source.group':'research.evidence.1.rule','issuer.analysis':'research.result'},
9:{'issuer.inquiry.subject':'trade.intent.body'},
11:{'issuer.quote.table':'trade.result.title','issuer.holdings.data':'trade.system.body','issuer.quote.record':'trade.llm.quote.body'},
12:{'client.prior.material':'client.material2'},13:{'client.view.summary':'client.views.result'},
15:{'client.document':'clientDoc'},16:{'client.document':'clientDoc'},17:{'client.document':'clientDoc'},
18:{'client.document':'clientDoc','client.input.record':'review.inputs.body'},19:{'issuer.event.mail':'risk.mail.rule'},
21:{'issuer.event.mail':'risk.evidence.mail.rule','issuer.event.rule':'risk.evidence.rule.rule','issuer.holdings.data':'risk.evidence.system.body','issuer.impact.report':'risk.result'},
22:{'client.file.versions':'ops.row1.0','client.file.differences':'ops.row1.2'},23:{'client.version.v1':'ops.compare.old.label','client.version.v2':'ops.compare.new.label'},
24:{'client.input.record':'ops.inputs.body','client.change.explanation':'changeLog'},
25:{'client.development.sample':'dev.request','client.development.sample.name':'dev.request'},
26:{'client.development.sample':'dev.requirements','client.development.sample.name':'dev.requirements'},27:{'client.development.sample':'dev.samples.body'}}
for page,d in P.items():
 for o in d['overlays']:
  key=o['name'].removeprefix('!!story.');assert key in owners.get(page,{}),(page,key)
  o['appear_with']='!!'+owners[page][key]

plan={'source':'../navigation-color-review-2026-10-26/output/asset-management-llm-slide11-corrected.pptx','source_sha256':'9f5fdb8dadf1bc7dd883908c99e5d02c1e3735c3e2c76b000936b72c1a380ad2','colors':C,'navigation_progress_modified':False,'slides':list(P.values())}
(R/'src/color-map.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
md=['# 主线颜色与对象映射','','本轮没有修改导航进度方案。现有三段阶段文字、页脚计数、导航位置与跳转全部保留。权威输入为第11页修正版，业务文字、表格数据、来源和全部讲稿保持不变。','','## 颜色规则','','- 甲公司：青绿 #317F7B，极浅底 #EFF6F4。','- 客户沟通稿：紫 #7363A6，极浅底 #F3F0F8。V1和V2同属此色义。','- 人、LLM、工具、测试及完成状态：浅灰 #F3F7FA / 白，正文 #20262C。','- 差异定位：淡黄 #FFF0BE；版本与用途由文字说明。','- 部门/主题导航、标题及同行公司名保留原品牌蓝。','- 固定主线标记置于副标题右侧 x1204–1460；最右“示例”原位保留。正文少量6px侧条及标题线用于追踪对象。','- 新增对象名统一以 !!story. 开始，按 issuer / client 命名；同一主线跨页保持名字一致。','','## 逐页对象映射','','| 页 | 固定主线标记 | 主线对象（原对象名或新增标记） | 中性角色对象 | 说明 |','|---|---|---|---|---|']
for i,d in P.items():
 heads='；'.join(h['name']+('（'+h['qualifier']+'）' if h['qualifier'] else '') for h in d['header']) or '无'
 colored=[x['name'].replace('!!','') for x in d['styles'] if any(v in [C['issuer'],C['client'],C['issuerTint'],C['clientTint']] for v in x.values())]+[x['name'].replace('!!','') for x in d['overlays']]
 neutralnames=d['neutral_roots']+d['text_neutral']
 md.append('| '+str(i)+' | '+heads+' | '+'、'.join(colored or ['保持原有对象'])+' | '+'、'.join(neutralnames or ['无角色重着色'])+' | '+d['note']+' |')
md+=['','页顶主线标签始终显示。正文标记在映射中以 appear_with 绑定原对象；原对象有显现动画时沿用其开始时刻，否则同时静态显示。第7页按三行分别绑定色条，避免提前出现跨行长条。完整机器可读映射在 `src/color-map.json`。所有着色均按页及对象名指定，不做全页XML颜色替换。第18页的修订高亮由浅绿改为淡黄。第3、29、30页并列两条主线；其他材料中的甲公司文字不会自动被染绿。']
(R/'COLOR-MAP.md').write_text('\n'.join(md)+'\n')
print('Wrote COLOR-MAP.md and 33-page object map')
