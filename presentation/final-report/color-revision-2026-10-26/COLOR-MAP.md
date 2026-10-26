# 主线颜色与对象映射

本轮没有修改导航进度方案。现有三段阶段文字、页脚计数、导航位置与跳转全部保留。权威输入为第11页修正版，业务文字、表格数据、来源和全部讲稿保持不变。

## 颜色规则

- 甲公司：青绿 #317F7B，极浅底 #EFF6F4。
- 客户沟通稿：紫 #7363A6，极浅底 #F3F0F8。V1和V2同属此色义。
- 人、LLM、工具、测试及完成状态：浅灰 #F3F7FA / 白，正文 #20262C。
- 差异定位：淡黄 #FFF0BE；版本与用途由文字说明。
- 部门/主题导航、标题及同行公司名保留原品牌蓝。
- 固定主线标记置于副标题右侧 x1204–1460；最右“示例”原位保留。正文少量6px侧条及标题线用于追踪对象。
- 新增对象名统一以 !!story. 开始，按 issuer / client 命名；同一主线跨页保持名字一致。

## 逐页对象映射

| 页 | 固定主线标记 | 主线对象（原对象名或新增标记） | 中性角色对象 | 说明 |
|---|---|---|---|---|
| 1 | 无 | 保持原有对象 | 无角色重着色 | 通用说明保持中性，不新增主线归属；原导航、阶段文字、页码与布局不变。 |
| 2 | 无 | 保持原有对象 | scope.work0、scope.work1、scope.work2、scope.work3 | 通用说明保持中性，不新增主线归属；原导航、阶段文字、页码与布局不变。 |
| 3 | 甲公司；客户沟通稿 | 保持原有对象 | 无角色重着色 |  |
| 4 | 甲公司 | research.evidence.1.label、research.evidence.1.rule、research.evidence.2.label、research.evidence.2.rule、research.evidence.3.label、research.evidence.3.rule、story.issuer.source.1、story.issuer.source.2、story.issuer.source.3 | research.question、research.manual.0、research.manual.1、research.manual.2、research.manual.3 |  |
| 5 | 甲公司（方法参考） | 保持原有对象 | driver.tools | 天弘公司名称及通用驱动树保留品牌蓝；页眉甲公司标记注明方法参考，工具为中性。 |
| 6 | 甲公司（方法参考） | views.reportA.label、views.reportA.rule、views.reportB.label、views.reportB.rule、views.result、story.issuer.views.reportA、story.issuer.views.reportB、story.issuer.analysis | views.method、views.consensus.title、views.difference.title |  |
| 7 | 甲公司（方法参考） | story.issuer.source.row.0、story.issuer.analysis.row.0、story.issuer.source.row.1、story.issuer.analysis.row.1、story.issuer.source.row.2、story.issuer.analysis.row.2 | elements.left、elements.right、element.0.source、element.1.source、element.2.source |  |
| 8 | 甲公司 | research.evidence.1.label、research.evidence.1.rule、research.evidence.2.label、research.evidence.2.rule、research.evidence.3.label、research.evidence.3.rule、research.result、story.issuer.source.group、story.issuer.analysis | research.question、research.llm、research.tool、research.result.title |  |
| 9 | 甲公司 | story.issuer.inquiry.subject | trade.intent、trade.query、trade.inquire、trade.compare、trade.system、trade.counterparty、trade.data.label |  |
| 10 | 甲公司（方法参考） | 保持原有对象 | trade.case1.0、trade.case1.1、trade.case1.2、trade.case1.3、trade.case2.0、trade.case2.1、trade.case2.2、trade.case2.3 | 南方与兴证全球名称仍为蓝底白字；主线标签仅表示当前甲公司叙事的方法参考。 |
| 11 | 甲公司 | story.issuer.quote.table、story.issuer.holdings.data、story.issuer.quote.record | trade.intent、trade.llm.query、trade.system、trade.llm.quote、trade.result.title |  |
| 12 | 客户沟通稿（材料准备） | story.client.prior.material | client.material0、client.material1、client.material2、client.manual.0、client.manual.1、client.manual.2 |  |
| 13 | 客户沟通稿（观点准备） | client.views.result、client.views.result.title、story.client.view.summary | client.views.llm |  |
| 14 | 机构标书（独立案例） | 保持原有对象 | tender.question、tender.llm、tender.answer | 机构标书是独立案例，使用中性页眉，不归为同一份客户沟通稿。 |
| 15 | 客户沟通稿（V1编写） | clientDoc、clientDoc.title、clientDoc.version、clientDoc.rule、story.client.document | client.input.customer、client.input.manager、client.input.product、client.llm |  |
| 16 | 客户沟通稿（V1审核） | clientDoc、clientDoc.title、clientDoc.version、clientDoc.rule、story.client.document | 无角色重着色 |  |
| 17 | 客户沟通稿（V1审核） | clientDoc、clientDoc.title、clientDoc.version、clientDoc.rule、story.client.document | comment.meta、comment.view、comment.risk |  |
| 18 | 客户沟通稿（V2修订） | clientDoc、clientDoc.title、clientDoc.version、clientDoc.rule、story.client.document、story.client.input.record | review.inputs、review.tool、review.llm |  |
| 19 | 甲公司 | risk.mail.rule、story.issuer.event.mail | risk.question.0、risk.question.1、risk.question.2、risk.mail.label |  |
| 20 | 甲公司（方法参考） | 保持原有对象 | risk.mail.extract、risk.rules.tool、risk.event.llm | 汇添富、天弘案例名称保持品牌蓝，邮件/条款工具和LLM块均中性；甲公司只作方法参考标记。 |
| 21 | 甲公司 | risk.result、risk.result.role、risk.evidence.mail.label、risk.evidence.mail.rule、risk.evidence.rule.label、risk.evidence.rule.rule、story.issuer.event.mail、story.issuer.event.rule、story.issuer.holdings.data、story.issuer.impact.report | risk.evidence.system、risk.llm |  |
| 22 | 客户沟通稿（文件示例） | story.client.file.versions、story.client.file.differences | ops.row0.0、ops.row0.1、ops.row0.2、ops.row1.0、ops.row1.1、ops.row1.2、ops.row2.0、ops.row2.1、ops.row2.2 | 客户稿版本输入和差异清单单独标紫；通用传真与其他文件保持中性，不把整页染紫，也不虚构甲公司单据。 |
| 23 | 客户沟通稿（版本比对） | ops.compare.old.label、ops.compare.new.label、story.client.version.v1、story.client.version.v2 | ops.form、ops.compare.read | 工银瑞信和华安名称保持品牌蓝，通用传真区域中性；V1/V2文字材料同紫，新增文字仍淡黄。 |
| 24 | 客户沟通稿（变更说明） | changeLog、changeLog.title、changeLog.rule、story.client.input.record、story.client.change.explanation | ops.inputs、ops.tool、ops.llm |  |
| 25 | 客户沟通稿（开发样例） | story.client.development.sample、story.client.development.sample.name | dev.request、dev.requirements、dev.code、dev.debug | 紫色只给两版客户稿这一开发样例；开发人员、代码、测试、反馈和修订块保持中性。 |
| 26 | 客户沟通稿（方法参考） | story.client.development.sample、story.client.development.sample.name | dev.requirements、dev.code、dev.test、dev.case.result | 紫色只给两版客户稿这一开发样例；开发人员、代码、测试、反馈和修订块保持中性。 |
| 27 | 客户沟通稿（开发样例） | dev.samples.body、story.client.development.sample | dev.request、dev.samples、dev.generate、dev.test、dev.deliver、dev.revise、dev.feedback、dev.testFeedback.label | 紫色只给两版客户稿这一开发样例；开发人员、代码、测试、反馈和修订块保持中性。 |
| 28 | 无 | 保持原有对象 | other.0.flow.0、other.0.flow.1、other.0.flow.2、other.1.flow.0、other.1.flow.1、other.1.flow.2、other.2.flow.0、other.2.flow.1、other.2.flow.2 | 通用说明保持中性，不新增主线归属；原导航、阶段文字、页码与布局不变。 |
| 29 | 甲公司；客户沟通稿 | 保持原有对象 | 无角色重着色 |  |
| 30 | 甲公司；客户沟通稿 | cross.0.0、cross.1.0、cross.0.1、cross.1.1、cross.0.2、cross.1.2 | 无角色重着色 | 两条主线并列：上行甲公司极浅青绿、下行客户稿极浅紫；对象名及对应连接线沿用各自主线色。 |
| 31 | 无 | 保持原有对象 | arch.entry、arch.workflow、arch.model、arch.tools | 通用说明保持中性，不新增主线归属；原导航、阶段文字、页码与布局不变。 |
| 32 | 无 | 保持原有对象 | 无角色重着色 | 通用说明保持中性，不新增主线归属；原导航、阶段文字、页码与布局不变。 |
| 33 | 无 | 保持原有对象 | evaluation.flow.0、evaluation.flow.1、evaluation.flow.2、evaluation.flow.3 | 通用说明保持中性，不新增主线归属；原导航、阶段文字、页码与布局不变。 |

页顶主线标签始终显示。正文标记在映射中以 appear_with 绑定原对象；原对象有显现动画时沿用其开始时刻，否则同时静态显示。第7页按三行分别绑定色条，避免提前出现跨行长条。完整机器可读映射在 `src/color-map.json`。所有着色均按页及对象名指定，不做全页XML颜色替换。第18页的修订高亮由浅绿改为淡黄。第3、29、30页并列两条主线；其他材料中的甲公司文字不会自动被染绿。
