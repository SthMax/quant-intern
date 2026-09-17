# 原始来源与研究阅读入口

2026-09-08完成A/B/C/D清理，2026-09-09补充重点研究与监管复核。当时为125个来源ID。2026-09-16累计新增19项Phase 2技术/许可来源，并将5项首轮模型资料转为历史辅助阅读，2026-09-17再新增23项serving/harness来源，**当前167个稳定来源ID：149个主阅读记录、14个辅助记录、4个来源链索引。** 这些是阅读分组，不是部署数或证据等级；主阅读记录中仍有未取得正文的条目。

默认检索按[reading-index.json](../reading-index.json)中的`collection_role=main`及`reading_path`取文本。需要身份、历史或供应商背景时再读[辅助目录](../reference/README.md)。不要把原始HTML/PDF、历史审计、图片元数据或来源链索引递归当作新文章。

原始出版物文件保持原样；FUND-203的旧新浪HTML另存为`source.sina.html`，其主档改用已保存的微信原刊。仅删除FUND-093的两个错误门户响应及FUND-162的重复可见文本导出，删除前内容可由Git快照`103f14c`恢复。[清理与对照审查](../audits/2026-09-08-relevance-cleanup/README.md)。

`original.md`可能是完整提取、明确标注的节选或来源索引，具体见元数据`text_kind`。节选不冒称全文；原文件保持可追溯。原语言、作者、风险提示及公司报告数字的解释边界继续保留。

## 主阅读记录

| ID | 标题 | 原语言 | 当前分类 | 阅读／原件／元数据 | 证据边界 |
|---|---|---|---|---|---|
| FUND-001 | 关于华夏基金管理有限公司采购结果的公告 | Chinese | 主阅读 | [阅读入口](FUND-001/original.md) · [原始文件](FUND-001/source.pdf) · [元数据](FUND-001/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-002 | 华夏基金管理有限公司大模型云服务项目潜在供应商征集公告 | Chinese | 主阅读 | [阅读入口](FUND-002/original.md) · [原始文件](FUND-002/source.html) · [元数据](FUND-002/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-003 | 公司概览 | Chinese | 主阅读 | [阅读入口](FUND-003/original.md) · [原始文件](FUND-003/source.html) · [元数据](FUND-003/metadata.json) | Current capture: 2025 year-end total including subsidiaries >RMB3.2tn. Prior 2025Q2 >RMB3tn observation lacks a preserved historical snapshot and is not reverified here. |
| FUND-004 | 『基金行业金融科技获奖成果宣传活动』易方达基金：基于数智赋能的指数业务一体化平台 | Chinese | 主阅读 | [阅读入口](FUND-004/original.md) · [原始文件](FUND-004/source.pdf) · [元数据](FUND-004/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-005 | 关于我们 | Chinese | 主阅读 | [阅读入口](FUND-005/original.md) · [原始文件](FUND-005/source.html) · [元数据](FUND-005/metadata.json) | Current capture: 2026June-end EFund and subordinate institutions >RMB4.3tn. Prior 2025YE >RMB4.1tn observation lacks a preserved historical snapshot and is not reverified here. |
| FUND-006 | DeepSeek能“替代”投顾？一场专业测试引发思考 | Chinese | 主阅读 | [阅读入口](FUND-006/original.md) · [原始文件](FUND-006/source.html) · [元数据](FUND-006/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-007 | 『基金行业金融科技发展奖』富国基金：指数基金智能投资决策系统 | Chinese | 主阅读 | [阅读入口](FUND-007/original.md) · [原始文件](FUND-007/source.pdf) · [元数据](FUND-007/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-008 | 关于富国 | Chinese | 主阅读 | [阅读入口](FUND-008/original.md) · [原始文件](FUND-008/source.html) · [元数据](FUND-008/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-009 | 广发基金智能理财助理服务协议 | Chinese | 主阅读 | [阅读入口](FUND-009/original.md) · [原始文件](FUND-009/source.pdf) · [元数据](FUND-009/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-010 | 公司简介 | Chinese | 主阅读 | [阅读入口](FUND-010/original.md) · [原始文件](FUND-010/source.html) · [元数据](FUND-010/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-011 | 『基金行业金融科技获奖成果宣传活动』兴证全球基金：千询固收智能交易平台 | Chinese | 主阅读 | [阅读入口](FUND-011/original.md) · [原始文件](FUND-011/source.pdf) · [元数据](FUND-011/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-012 | 关于我们 — 公司简介 | Chinese | 主阅读 | [阅读入口](FUND-012/original.md) · [原始文件](FUND-012/source.html) · [元数据](FUND-012/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-013 | 『基金行业金融科技获奖成果宣传活动』大成基金：固收全链路数智一体化平台 | Chinese | 主阅读 | [阅读入口](FUND-013/original.md) · [原始文件](FUND-013/source.pdf) · [元数据](FUND-013/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-014 | 公司简介 | Chinese | 主阅读 | [阅读入口](FUND-014/original.md) · [原始文件](FUND-014/source.html) · [元数据](FUND-014/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-090 | 多家公募完成DeepSeek-R1版本的私有化部署 应用于多个核心业务场景 | Chinese | 主阅读 | [阅读入口](FUND-090/original.md) · [原始文件](FUND-090/source.html) · [元数据](FUND-090/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-091 | AI重构公募行业：从投研到运营，一场全链条的效率革命 | Chinese | 主阅读 | [阅读入口](FUND-091/original.md) · [原始文件](FUND-091/source.html) · [元数据](FUND-091/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-092 | 毫秒级响应背后：解码基金行业的“科技进化论” | Chinese | 主阅读 | [阅读入口](FUND-092/original.md) · [原始文件](FUND-092/source.pdf) · [元数据](FUND-092/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-100 | 【实践案例】基金投顾业务实践案例分享——易方达基金投顾智能管理项目 | Chinese | 主阅读 | [阅读入口](FUND-100/original.md) · [原始文件](FUND-100/source.html) · [元数据](FUND-100/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-101 | 『基金行业金融科技获奖成果宣传活动』易方达基金：全栈云平台及云原生应用管理体系建设与实践 | Chinese | 主阅读 | [阅读入口](FUND-101/original.md) · [原始文件](FUND-101/source.pdf) · [元数据](FUND-101/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-102 | 易方达基金：把牢党建引领“方向舵” 以高质量党建领航高质量发展 | Chinese | 主阅读 | [阅读入口](FUND-102/original.md) · [原始文件](FUND-102/source.pdf) · [元数据](FUND-102/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-103 | 易方达基金首席信息官刘硕凌：大模型时代的智能投资之路 | Chinese | 主阅读 | [阅读入口](FUND-103/original.md) · [原始文件](FUND-103/source.html) · [元数据](FUND-103/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-104 | 2023年度金融科技发展奖获奖项目名单 | Chinese | 主阅读 | [阅读入口](FUND-104/original.md) · [原始文件](FUND-104/source.pdf) · [元数据](FUND-104/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-105 | 关于举办2024年度公募基金行业信息科技创新应用直播培训的通知 | Chinese | 主阅读 | [阅读入口](FUND-105/original.md) · [原始文件](FUND-105/source.html) · [元数据](FUND-105/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-106 | E Fund: Harnessing AI Trends in China to Drive Innovation and Enhance ETF Offerings | English | 主阅读 | [阅读入口](FUND-106/original.md) · [原始文件](FUND-106/source.html) · [元数据](FUND-106/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-107 | 腾讯企业智能体 WorkBuddy Enterprise | Chinese | 主阅读 | [阅读入口](FUND-107/original.md) · [原始文件](FUND-107/source.html) · [元数据](FUND-107/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-109 | 🧧易方达基金 × ima首发基金研选Skill：从获取信息到分析判断，助你走通决策闭环 | Chinese | 主阅读 | [阅读入口](FUND-109/original.md) · [原始文件](FUND-109/source.html) · [元数据](FUND-109/metadata.json) | 微信原文已恢复；阅读副本全文比对通过；人工复核待完成 |
| FUND-110 | 易方达基金等巨头纷纷出手，DeepSeek重塑金融科技新格局 | Chinese | 主阅读 | [阅读入口](FUND-110/original.md) · [原始文件](FUND-110/source.html) · [元数据](FUND-110/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-111 | 开放、便捷、深度 财富管理迎接AI新生态 | Chinese | 主阅读 | [阅读入口](FUND-111/original.md) · [原始文件](FUND-111/source.html) · [元数据](FUND-111/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-112 | 易方达基金Buddy应用正式上线 打造触手可及的AI投资陪伴服务 | Chinese | 主阅读 | [阅读入口](FUND-112/original.md) · [原始文件](FUND-112/source.html) · [元数据](FUND-112/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-150 | 2025 CCF企业数字化发展推荐案例集 — 华安基金管理有限公司——华安“灵思”AI智能创新平台 | Chinese | 主阅读；节选 | [阅读入口](FUND-150/original.md) · [原始文件](FUND-150/source.pdf) · [元数据](FUND-150/metadata.json) | 主阅读仅华安案例PDF第23–28页；整本原PDF与图表保留 |
| FUND-151 | 2025 CCF企业数字化发展优秀案例评选结果公示 | Chinese | 主阅读 | [阅读入口](FUND-151/original.md) · [原始文件](FUND-151/source.html) · [元数据](FUND-151/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-152 | 华安基金完成DeepSeek私有化部署 | Chinese | 主阅读 | [阅读入口](FUND-152/original.md) · [原始文件](FUND-152/source.html) · [元数据](FUND-152/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-160 | 平安基金发布“AI青蚨”：破解数据“沉睡”困局 构建智能投研新范式 | Chinese | 主阅读 | [阅读入口](FUND-160/original.md) · [原始文件](FUND-160/source.html) · [元数据](FUND-160/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-161 | AI重塑资管业！从千人千面到“价值深耕”，四大机构最新研判 | Chinese | 主阅读 | [阅读入口](FUND-161/original.md) · [原始文件](FUND-161/source.html) · [元数据](FUND-161/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-200 | 『基金行业金融科技获奖成果宣传活动』南方基金：基于多智能体协同的交易助理 | Chinese | 主阅读 | [阅读入口](FUND-200/original.md) · [原始文件](FUND-200/source.pdf) · [元数据](FUND-200/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-201 | 南方基金电子直销用户服务协议 | Chinese | 主阅读 | [阅读入口](FUND-201/original.md) · [原始文件](FUND-201/source.html) · [元数据](FUND-201/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-202 | 华泰证券股份有限公司 | Chinese | 主阅读 | [阅读入口](FUND-202/original.md) · [原始文件](FUND-202/source.html) · [元数据](FUND-202/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-203 | 拥抱AI，南方基金ETFirst Skill重塑指数投资服务生态 | Chinese | 主阅读 | [阅读入口](FUND-203/original.md) · [原始文件](FUND-203/source.html) · [元数据](FUND-203/metadata.json) | 中国基金报微信原刊；新浪转载留作来源记录；仍为媒体报道 |
| FUND-210 | 博时基金：人工智能技术锻造AI投资创新引擎 | Chinese | 主阅读 | [阅读入口](FUND-210/original.md) · [原始文件](FUND-210/source.html) · [元数据](FUND-210/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-211 | 廿八载价值深耕，博时基金奋进高质量发展新征程 | Chinese | 主阅读 | [阅读入口](FUND-211/original.md) · [原始文件](FUND-211/source.html) · [元数据](FUND-211/metadata.json) | Embedded base64 image moved to local image asset for readability; original HTML unchanged. |
| FUND-212 | 致敬75周年丨博时基金以金融创新为翼助力经济高质量发展 | Chinese | 主阅读 | [阅读入口](FUND-212/original.md) · [原始文件](FUND-212/source.html) · [元数据](FUND-212/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-213 | 公司简介 | Chinese | 主阅读 | [阅读入口](FUND-213/original.md) · [原始文件](FUND-213/source.html) · [元数据](FUND-213/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-214 | 博时基金董事长张东：把握“十五五”财富管理新趋势，运用AI助力高质量发展 | Chinese | 主阅读 | [阅读入口](FUND-214/original.md) · [原始文件](FUND-214/source.html) · [元数据](FUND-214/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-220 | 『基金行业金融科技获奖成果宣传活动』汇添富基金：智汇投资风险管理平台 | Chinese | 主阅读 | [阅读入口](FUND-220/original.md) · [原始文件](FUND-220/source.pdf) · [元数据](FUND-220/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-221 | 汇添富现金宝-汇添富基金打造的投资平台 | Chinese | 主阅读 | [阅读入口](FUND-221/original.md) · [原始文件](FUND-221/source.html) · [元数据](FUND-221/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-222 | 【汇添富基金副总经理兼首席信息官李骁】汇添富基金数智化赋能的实践与思考——2025年金融科技发展回顾与2026年展望 | Chinese | 主阅读 | [阅读入口](FUND-222/original.md) · [原始文件](FUND-222/source.html) · [元数据](FUND-222/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据; 属于转载；首发来源／日期仍未确认 |
| FUND-223 | AI智能体落地！汇添富直销平台率先接入DeepSeek | Chinese | 主阅读 | [阅读入口](FUND-223/original.md) · [原始文件](FUND-223/source.html) · [元数据](FUND-223/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-224 | 公司介绍 | Chinese | 主阅读 | [阅读入口](FUND-224/original.md) · [原始文件](FUND-224/source.html) · [元数据](FUND-224/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-225 | RESULTS ANNOUNCEMENT FOR THE YEAR ENDED DECEMBER 31, 2025 | English | 主阅读 | [阅读入口](FUND-225/original.md) · [原始文件](FUND-225/source.pdf) · [元数据](FUND-225/metadata.json) | English source; some Chinese corporate-name glyphs are malformed in PDF extraction. Consult original PDF for these names. |
| FUND-250 | 景顺长城基金 护航科技创新 穿越周期筑根基 | Chinese | 主阅读 | [阅读入口](FUND-250/original.md) · [原始文件](FUND-250/source.html) · [元数据](FUND-250/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-251 | 公募基金AI部署走到哪一步了？20家头部公募AI部署全景调研 | Chinese | 主阅读 | [阅读入口](FUND-251/original.md) · [原始文件](FUND-251/source.html) · [元数据](FUND-251/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-252 | 公司概况 | Chinese | 主阅读 | [阅读入口](FUND-252/original.md) · [原始文件](FUND-252/source.html) · [元数据](FUND-252/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-253 | 长城证券股份有限公司2025年年度报告 | Chinese | 主阅读 | [阅读入口](FUND-253/original.md) · [原始文件](FUND-253/source.pdf) · [元数据](FUND-253/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-254 | 以AI融入指增业务，多家公募发力布局，各有哪些解锁动作？ | Chinese | 主阅读 | [阅读入口](FUND-254/original.md) · [原始文件](FUND-254/source.html) · [元数据](FUND-254/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-300 | 『基金行业金融科技发展奖』天弘基金：基于大模型的 FinAgent 金融智能体系统 | Chinese | 主阅读 | [阅读入口](FUND-300/original.md) · [原始文件](FUND-300/source.pdf) · [元数据](FUND-300/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-301 | 行业动态 | Chinese | 主阅读 | [阅读入口](FUND-301/original.md) · [原始文件](FUND-301/source.html) · [元数据](FUND-301/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-302 | 公司介绍 | Chinese | 主阅读 | [阅读入口](FUND-302/browser-recovered.md) · [原始文件](FUND-302/retrieval-response.html) · [元数据](FUND-302/metadata.json) | HTTP 200 anti-bot challenge (var arg1), not company-profile content · [恢复记录](FUND-302/recovery.json) |
| FUND-304 | 嘉实基金2025可持续投资报告 | Chinese | 主阅读 | [阅读入口](FUND-304/original.md) · [原始文件](FUND-304/source.pdf) · [元数据](FUND-304/metadata.json) | Some pages have little/no text; inspect original PDF for images, charts, tables and scans. |
| FUND-305 | 认识嘉实 | Chinese | 主阅读 | [阅读入口](FUND-305/original.md) · [原始文件](FUND-305/source.html) · [元数据](FUND-305/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-306 | 加入我们—嘉实招聘 | Chinese | 主阅读 | [阅读入口](FUND-306/original.md) · [原始文件](FUND-306/source.html) · [元数据](FUND-306/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-307 | 从春山可望到E路生花，嘉实基金第二届超级指数节成功举办 | Chinese | 主阅读 | [阅读入口](FUND-307/original.md) · [原始文件](FUND-307/source.html) · [元数据](FUND-307/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-308 | 『基金行业金融科技获奖成果宣传活动』鹏华基金：基于动态思维链的资管业务智能体建设 | Chinese | 主阅读 | [阅读入口](FUND-308/original.md) · [原始文件](FUND-308/source.pdf) · [元数据](FUND-308/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-309 | 行业动态 | Chinese | 主阅读 | [阅读入口](FUND-309/original.md) · [原始文件](FUND-309/source.html) · [元数据](FUND-309/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-310 | AI算力服务器采购项目招标文件 | Chinese | 主阅读；正文未取得 | [原始文件](FUND-310/retrieval-response.html) · [元数据](FUND-310/metadata.json) | Registered PDF redirects to Penghua homepage; browser independently confirmed homepage rather than cited PDF · [恢复记录](FUND-310/recovery.json) |
| FUND-312 | 『基金行业金融科技获奖成果宣传活动』工银瑞信基金：基于人工智能的一站式养老金投资运营管理平台 | Chinese | 主阅读 | [阅读入口](FUND-312/original.md) · [原始文件](FUND-312/source.pdf) · [元数据](FUND-312/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-313 | 行业动态 | Chinese | 主阅读 | [阅读入口](FUND-313/original.md) · [原始文件](FUND-313/source.html) · [元数据](FUND-313/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-314 | 【专访】工银瑞信CIO王建：2026金融大模型与智能体，从野蛮生长到合规落地、价值凸显 | Chinese | 主阅读 | [阅读入口](FUND-314/extractor-recovered.md) · [元数据](FUND-314/metadata.json) | curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.fintechinchina.com:443 · [恢复记录](FUND-314/recovery.json) |
| FUND-315 | 工银瑞信首席信息官王建：自立自强 数智融合 工银瑞信数智化发展回顾与展望 | Chinese | 主阅读 | [阅读入口](FUND-315/extractor-recovered.md) · [元数据](FUND-315/metadata.json) | curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to fintechinchina.com:443 · [恢复记录](FUND-315/recovery.json) |
| FUND-316 | 恒生电子2023可持续发展报告 | Chinese | 主阅读 | [阅读入口](FUND-316/original.md) · [原始文件](FUND-316/source.pdf) · [元数据](FUND-316/metadata.json) | Some pages have little/no text; inspect original PDF for images, charts, tables and scans. |
| FUND-317 | 亮相2026中国国际金融展，嘉实基金解构数字金融智能化跃迁 | Chinese | 主阅读 | [阅读入口](FUND-317/original.md) · [原始文件](FUND-317/source.html) · [元数据](FUND-317/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-350 | 基金公司鏖战AI | Chinese | 主阅读 | [阅读入口](FUND-350/original.md) · [原始文件](FUND-350/source.html) · [元数据](FUND-350/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-351 | 招商基金：深入推进数字金融建设，全面拥抱数智化转型 | Chinese | 主阅读 | [阅读入口](FUND-351/original.md) · [原始文件](FUND-351/source.html) · [元数据](FUND-351/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-352 | AI筑牢邮件安全防线 永赢基金以大模型守护金融数字资产 | Chinese | 主阅读 | [阅读入口](FUND-352/original.md) · [原始文件](FUND-352/source.pdf) · [元数据](FUND-352/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-353 | 行业动态 | Chinese | 主阅读 | [阅读入口](FUND-353/original.md) · [原始文件](FUND-353/source.html) · [元数据](FUND-353/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-354 | 中欧基金AI投研助手荣获央行2024年度金融科技发展奖 | Chinese | 主阅读 | [阅读入口](FUND-354/original.md) · [原始文件](FUND-354/source.html) · [元数据](FUND-354/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-356 | 中欧基金窦玉明：AI赋能时代，「三化」协同夯实长期业绩根基 | Chinese | 主阅读 | [阅读入口](FUND-356/original.md) · [原始文件](FUND-356/source.html) · [元数据](FUND-356/metadata.json) | 微信原文已恢复；阅读副本全文比对通过；人工复核待完成 |
| FUND-359 | 华泰柏瑞量化团队：“人机协同”迈入深水区，AI投研构筑长期护城河 | Chinese | 主阅读 | [阅读入口](FUND-359/original.md) · [原始文件](FUND-359/source.pdf) · [元数据](FUND-359/metadata.json) | 正文、结尾和风险提示完整；媒体报道属性保留 |
| FUND-400 | 公募非货规模最新座次出炉，万亿公募增至3家，中段座次重排 | Chinese | 主阅读 | [阅读入口](FUND-400/original.md) · [原始文件](FUND-400/source.html) · [元数据](FUND-400/metadata.json) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-401 | 基金管理机构非货币公募基金月均规模（20家）（2024年三季度） | Chinese | 主阅读 | [阅读入口](FUND-401/original.md) · [原始文件](FUND-401/source.pdf) · [元数据](FUND-401/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-402 | 『基金行业金融科技获奖成果宣传活动』华夏基金：飞翼固收一体化智能平台 | Chinese | 主阅读 | [阅读入口](FUND-402/original.md) · [原始文件](FUND-402/source.pdf) · [元数据](FUND-402/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-403 | 『基金行业金融科技获奖成果宣传活动』国泰基金：基金组合管理平台建设 | Chinese | 主阅读 | [阅读入口](FUND-403/original.md) · [原始文件](FUND-403/source.pdf) · [元数据](FUND-403/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-001 | 生成式人工智能服务管理暂行办法 | Chinese | 主阅读 | [阅读入口](REG-001/original.md) · [原始文件](REG-001/source.html) · [元数据](REG-001/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-002 | 中华人民共和国个人信息保护法 | Chinese | 主阅读 | [阅读入口](REG-002/original.md) · [原始文件](REG-002/source.html) · [元数据](REG-002/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-003 | 证券基金经营机构信息技术管理办法 | Chinese | 主阅读 | [阅读入口](REG-003/original.md) · [原始文件](REG-003/source.html) · [元数据](REG-003/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-004 | 网络数据安全管理条例 | Chinese | 主阅读 | [阅读入口](REG-004/original.md) · [原始文件](REG-004/source.html) · [元数据](REG-004/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-005 | 证券期货业网络和信息安全管理办法 | Chinese | 主阅读 | [阅读入口](REG-005/original.md) · [原始文件](REG-005/source.pdf) · [元数据](REG-005/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-006 | 促进和规范数据跨境流动规定 | Chinese | 主阅读 | [阅读入口](REG-006/original.md) · [原始文件](REG-006/source.html) · [元数据](REG-006/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-007 | SR 26-2: Revised Guidance on Model Risk Management | English | 主阅读 | [阅读入口](REG-007/original.md) · [原始文件](REG-007/source.html) · [元数据](REG-007/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-008 | Supervisory Guidance on Model Risk Management | English | 主阅读 | [阅读入口](REG-008/original.md) · [原始文件](REG-008/source.html) · [元数据](REG-008/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-009 | 关于发布《基金经营机构大模型技术应用规范》团体标准的公告 | Chinese | 主阅读 | [阅读入口](REG-009/original.md) · [原始文件](REG-009/source.html) · [元数据](REG-009/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-010 | 基金经营机构大模型技术应用规范 — T/AMAC 0004-2026 | Chinese | 主阅读 | [阅读入口](REG-010/original.md) · [原始文件](REG-010/source.pdf) · [元数据](REG-010/metadata.json) | Some pages have little/no text; inspect original PDF for images, charts, tables and scans. |
| REG-011 | 基金行业生成式人工智能可解释性治理探讨 | Chinese | 主阅读 | [阅读入口](REG-011/original.md) · [原始文件](REG-011/source.pdf) · [元数据](REG-011/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-012 | 中华人民共和国标准化法（2017年修订） | Chinese | 主阅读 | [阅读入口](REG-012/original.md) · [原始文件](REG-012/source.html) · [元数据](REG-012/metadata.json) | 原登记来源类型和核验范围保留；人工核验待完成 |

| FUND-113 | MENTOR: a multi-agent framework for event and narrative trend prediction with optimized reasoning | English | 主阅读 | [阅读入口](FUND-113/original.md) · [原始文件](FUND-113/source.pdf) · [元数据](FUND-113/metadata.json) | 研究／客户端资料；非生产系统复现；具体范围见技术审查 |
| FUND-114 | MENTOR supplementary materials | English | 主阅读 | [阅读入口](FUND-114/original.md) · [原始文件](FUND-114/source.pdf) · [元数据](FUND-114/metadata.json) | 研究／客户端资料；非生产系统复现；具体范围见技术审查 |
| FUND-115 | 指数直通车 Index-Hub Skills：官方查询客户端与接口文档 | Chinese / English | 主阅读 | [阅读入口](FUND-115/original.md) · [原始文件](FUND-115/repository/files/README.md) · [元数据](FUND-115/metadata.json) | 研究／客户端资料；非生产系统复现；具体范围见技术审查 |
| FUND-116 | 指数直通车 AI Skills 帮助文档 | Chinese | 主阅读 | [阅读入口](FUND-116/original.md) · [原始文件](FUND-116/source.pdf) · [元数据](FUND-116/metadata.json) | 研究／客户端资料；非生产系统复现；具体范围见技术审查 |
| FUND-117 | SLAG: Enhancing LLMs for Expert Question Answering by Synergizing with Knowledge Graphs | Chinese / English | 主阅读 | [阅读入口](FUND-117/original.md) · [原始文件](FUND-117/repository/files/README.md) · [元数据](FUND-117/metadata.json) | 研究／客户端资料；非生产系统复现；具体范围见技术审查 |
| FUND-118 | FinCoT / Financial Fast Reasoning Distillation: public reasoning datasets | Chinese / English | 主阅读 | [阅读入口](FUND-118/original.md) · [原始文件](FUND-118/repository/files/README.md) · [元数据](FUND-118/metadata.json) | 研究／客户端资料；非生产系统复现；具体范围见技术审查 |
| FUND-119 | NLPCC 2026 Shared Task 4: Investment Agent Starter | Chinese / English | 主阅读 | [阅读入口](FUND-119/original.md) · [原始文件](FUND-119/repository/files/README-CN.md) · [元数据](FUND-119/metadata.json) | 研究／客户端资料；非生产系统复现；具体范围见技术审查 |
| REG-013 | 中华人民共和国网络安全法（2025年修正） | Chinese | 主阅读 | [阅读入口](REG-013/original.md) · [原始文件](REG-013/source.html) · [元数据](REG-013/metadata.json) | 公开条文与定向版本复核2026-09-09；机构适用性与人工核验待完成 |
| REG-014 | 中华人民共和国数据安全法 | Chinese | 主阅读 | [阅读入口](REG-014/original.md) · [原始文件](REG-014/source.html) · [元数据](REG-014/metadata.json) | 公开条文与定向版本复核2026-09-09；机构适用性与人工核验待完成 |
| REG-015 | 个人信息保护合规审计管理办法 | Chinese | 主阅读 | [阅读入口](REG-015/original.md) · [原始文件](REG-015/source.html) · [元数据](REG-015/metadata.json) | 公开条文与定向版本复核2026-09-09；机构适用性与人工核验待完成 |
| REG-016 | 人工智能生成合成内容标识办法 | Chinese | 主阅读 | [阅读入口](REG-016/original.md) · [原始文件](REG-016/source.html) · [元数据](REG-016/metadata.json) | 公开条文与定向版本复核2026-09-09；机构适用性与人工核验待完成 |

| FUND-122 | A survey on large language model-based alpha mining | English | 主阅读 | [阅读入口](FUND-122/original.md) · [原始文件](FUND-122/source.pdf) · [元数据](FUND-122/metadata.json) | 量化研究／方法；具体实现与评价边界见量化审查 |

| FUND-227 | 基于大模型的指标异动归因分析方法、系统、设备和介质（CN121958380A） | Chinese | 主阅读 | [阅读入口](FUND-227/original.md) · [原始文件](FUND-227/source.html) · [元数据](FUND-227/metadata.json) | 技术申请披露；镜像缺图，待补原件；不证明投产 |

| FUND-320 | 一种基于知识图谱的智能问答系统优化方法及装置（CN120804142A） | Chinese | 主阅读 | [阅读入口](FUND-320/original.md) · [HTML](FUND-320/source.html) · [元数据](FUND-320/metadata.json) | 明确LLM生成图查询；原PDF与投产对应待核 |

| FUND-321 | 基于数字金融的公募基金全场景智能财富管理平台 | Chinese | 主阅读 | [阅读入口](FUND-321/original.md) · [PDF](FUND-321/source.pdf) · [元数据](FUND-321/metadata.json) | 原21家样本外补充；不自动认定4分或单卡可复现 |
| FUND-322 | 基金行业人工智能大模型应用及建设探索 | Chinese | 主阅读 | [阅读入口](FUND-322/original.md) · [PDF](FUND-322/source.pdf) · [元数据](FUND-322/metadata.json) | 原21家样本外补充；不自动认定4分或单卡可复现 |

| FUND-215 | 智启金融新范式，博时前瞻布局企业级“龙虾”生态，赋能资管全链条 | Chinese | 主阅读 | [正文](FUND-215/original.md) · [HTML](FUND-215/source.html) · [元数据](FUND-215/metadata.json) | 2026披露；China；未独立复现 |
| FUND-323 | A Trend Following Deep Dive: AlphaTrend and Agentic Research Workflows | English | 主阅读 | [正文](FUND-323/original.md) · [HTML](FUND-323/source.html) · [元数据](FUND-323/metadata.json) | 2026披露；Overseas comparison；未独立复现 |
| FUND-324 | Anything Can Be Language Now: My Thoughts on the Future of Features Research | English | 主阅读 | [正文](FUND-324/original.md) · [HTML](FUND-324/source.html) · [元数据](FUND-324/metadata.json) | 2026披露；Overseas comparison；未独立复现 |

## 辅助记录

| ID | 标题 | 原语言 | 当前分类 | 阅读／原件／元数据 | 证据边界 |
|---|---|---|---|---|---|
| FUND-162 | 平安基金管理有限公司 | Chinese | 辅助；节选 | [阅读入口](FUND-162/original.md) · [原始文件](FUND-162/source.html) · [元数据](FUND-162/metadata.json) | 辅助材料，未用于新增LLM实施计数；原有证据边界保留 |
| FUND-255 | 强强联手！景顺长城量化团队携手清华大学研究碳中和 | Chinese | 辅助 | [阅读入口](../reference/FUND-255.md) · [原始文件](FUND-255/source.html) · [元数据](FUND-255/metadata.json) | 辅助材料，未用于新增LLM实施计数；原有证据边界保留 |
| FUND-357 | 钱拓科技 · FDE金融AI服务商 | Chinese | 辅助 | [阅读入口](../reference/FUND-357.md) · [原始文件](FUND-357/source.html) · [元数据](FUND-357/metadata.json) | 辅助材料，未用于新增LLM实施计数；原有证据边界保留 |
| FUND-405 | 国泰基金管理有限公司旗下部分基金2025年年度报告提示性公告 | Chinese | 辅助；节选 | [阅读入口](FUND-405/original.md) · [原始文件](FUND-405/source.pdf) · [元数据](FUND-405/metadata.json) | 辅助材料，未用于新增LLM实施计数；原有证据边界保留 |

| FUND-120 | The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting | English | 辅助；非LLM | [阅读入口](FUND-120/original.md) · [原始文件](FUND-120/source.pdf) · [元数据](FUND-120/metadata.json) | 量化研究／方法；具体实现与评价边界见量化审查  不纳入LLM报告主案例与评分 |
| FUND-121 | The Label Horizon Paradox — Open-Source Demo | English | 辅助；非LLM | [阅读入口](FUND-121/original.md) · [原始文件](FUND-121/files/README.md) · [元数据](FUND-121/metadata.json) | 量化研究／方法；具体实现与评价边界见量化审查  不纳入LLM报告主案例与评分 |
| FUND-318 | 因子挖掘方法、装置、设备、存储介质和程序产品（CN116562377A） | Chinese | 辅助；非LLM | [阅读入口](FUND-318/original.md) · [原始文件](FUND-318/source.pdf) · [元数据](FUND-318/metadata.json) | 技术申请披露；PDF已核；不证明投产  不纳入LLM报告主案例与评分 |
| FUND-319 | 基于类别不平衡机器学习框架的债券违约预测方法和装置（CN114676932A） | Chinese | 辅助；非LLM | [阅读入口](FUND-319/original.md) · [原始文件](FUND-319/source.pdf) · [元数据](FUND-319/metadata.json) | 技术申请披露；PDF已核；不证明投产  不纳入LLM报告主案例与评分 |
| FUND-226 | 基金久期计算方法、装置、计算机设备和可读存储介质（CN121937219A） | Chinese | 辅助；非LLM | [阅读入口](FUND-226/original.md) · [原始文件](FUND-226/source.html) · [元数据](FUND-226/metadata.json) | 技术申请披露；镜像缺图，待补原件；不证明投产  不纳入LLM报告主案例与评分 |

## 来源链索引（不重复阅读）

| ID | 标题 | 原语言 | 当前分类 | 阅读／原件／元数据 | 证据边界 |
|---|---|---|---|---|---|
| FUND-093 | 亮相2026中国国际金融展 嘉实基金解构数字金融智能化跃迁 | Chinese | 索引 → FUND-317 | [阅读入口](FUND-317/original.md) · [元数据](FUND-093/metadata.json) | 只保留来源链；主档为FUND-317；旧出版物不构成独立印证 |
| FUND-108 | 🧧易方达基金 × ima首发基金研选Skill：从获取信息到分析判断，助你走通决策闭环 | Chinese | 索引 → FUND-109 | [阅读入口](FUND-109/original.md) · [原始文件](FUND-108/source.html) · [元数据](FUND-108/metadata.json) | 只保留来源链；主档为FUND-109；旧出版物不构成独立印证 |
| FUND-355 | 中欧基金窦玉明：AI赋能时代，「三化」协同夯实长期业绩根基 | Chinese | 索引 → FUND-356 | [阅读入口](FUND-356/original.md) · [原始文件](FUND-355/source.html) · [元数据](FUND-355/metadata.json) | 只保留来源链；主档为FUND-356；旧出版物不构成独立印证 |
| FUND-358 | 华泰柏瑞量化团队：“人机协同”迈入深水区，AI投研构筑长期护城河 | Chinese | 索引 → FUND-359 | [阅读入口](FUND-359/original.md) · [原始文件](FUND-358/source.html) · [元数据](FUND-358/metadata.json) | 只保留来源链；主档为FUND-359；旧出版物不构成独立印证 |

## Phase 2模型与部署来源（2026-09-16）

原始模型卡、配置、许可与索引按固定repo修订保存；未下载权重。多文件来源的获取URL、SHA-256和核对范围均在metadata中。模型初筛分析见[研究笔记](../models/model-survey-2026-09-16.md)。

| ID | 标题 | 阅读与原件 | 支持范围 |
|---|---|---|---|
| TECH-001 | Qwen/Qwen3.5-4B official model card and configuration | [原文](TECH-001/original.md) · [元数据与其他原件](TECH-001/metadata.json) | Model/config/license claims and artifact size; not local benchmarks |
| TECH-002 | Qwen/Qwen3.5-9B official model card and configuration | [原文](TECH-002/original.md) · [元数据与其他原件](TECH-002/metadata.json) | Model/config/license claims and artifact size; not local benchmarks |
| TECH-003 | Qwen/Qwen3.5-35B-A3B official model card and configuration | [原文](TECH-003/original.md) · [元数据与其他原件](TECH-003/metadata.json) | Model/config/license claims and artifact size; not local benchmarks |
| TECH-004 | Qwen/Qwen3.8-27B official model card and configuration | [原文](TECH-004/original.md) · [元数据与其他原件](TECH-004/metadata.json) | Model/config/license claims and artifact size; not local benchmarks |
| TECH-005 | google/gemma-4-12B-it official model card and configuration | [原文](TECH-005/original.md) · [元数据与其他原件](TECH-005/metadata.json) | Model/config/license claims and artifact size; not local benchmarks |
| TECH-006 | google/gemma-4-26B-A4B-it official model card and configuration | [原文](TECH-006/original.md) · [元数据与其他原件](TECH-006/metadata.json) | Model/config/license claims and artifact size; not local benchmarks |
| TECH-007 | mistralai/Mistral-Small-4-119B-2603 official model card and configuration | [原文](TECH-007/original.md) · [元数据与其他原件](TECH-007/metadata.json) | Model/config/license claims and artifact size; not local benchmarks |
| TECH-008 | deepseek-ai/DeepSeek-V4.1-Flash official model card and configuration | [原文](TECH-008/original.md) · [元数据与其他原件](TECH-008/metadata.json) | Model/config/license claims and artifact size; not local benchmarks |
| TECH-009 | vLLM v0.29.0 release and model registry | [原文](TECH-009/original.md) · [元数据与其他原件](TECH-009/metadata.json) | Released architecture registration |
| TECH-010 | Qwen3.8-27B vLLM deployment recipe | [原文](TECH-010/original.md) · [元数据与其他原件](TECH-010/metadata.json) | Upstream tested configurations and limits |
| TECH-011 | DeepSeek-V4.1 support tracking and initial integration PR | [原文](TECH-011/original.md) · [元数据与其他原件](TECH-011/metadata.json) | Integration timing versus release; issue text may lag PR state |
| TECH-012 | Gemma 4 Apache License 2.0 | [原文](TECH-012/original.md) · [元数据与其他原件](TECH-012/metadata.json) | Declared Gemma 4 license text |

### 第二轮模型与许可补充

候选按专业个人工作站和共享服务重排。TECH-001–003、005、007属于历史辅助来源，原件保留；当前8项候选与条款分析分别见[模型研究](../models/model-survey-2026-09-16.md)和[许可专项](../models/license-review-2026-09-16.md)。

| ID | 标题 | 阅读与原件 | 支持范围 |
|---|---|---|---|
| TECH-013 | Qwen/Qwen3.6-35B-A3B official model card, configuration and license | [原文](TECH-013/original.md) · [元数据与其他原件](TECH-013/metadata.json) | Exact model artifact, license conditions, configuration and tensor size |
| TECH-014 | google/gemma-4-31B-it official model card, configuration and license | [原文](TECH-014/original.md) · [元数据与其他原件](TECH-014/metadata.json) | Exact model artifact, license conditions, configuration and tensor size |
| TECH-015 | zai-org/GLM-5.3 official model card, configuration and license | [原文](TECH-015/original.md) · [元数据与其他原件](TECH-015/metadata.json) | Exact model artifact, license conditions, configuration and tensor size |
| TECH-016 | zai-org/GLM-5.3-Flash official model card, configuration and license | [原文](TECH-016/original.md) · [元数据与其他原件](TECH-016/metadata.json) | Exact model artifact, license conditions, configuration and tensor size |
| TECH-017 | moonshotai/Kimi-K3 official model card, configuration and license | [原文](TECH-017/original.md) · [元数据与其他原件](TECH-017/metadata.json) | Exact model artifact, license conditions, configuration and tensor size |
| TECH-018 | Muse Spark 1.2 open-weights announcement and Meta model inventory | [原文](TECH-018/original.md) · [元数据与其他原件](TECH-018/metadata.json) | Planned open weights and current publisher inventory; not a self-hosting grant |
| TECH-019 | Apache License Version 2.0 | [原文](TECH-019/original.md) · [元数据与其他原件](TECH-019/metadata.json) | Apache entity definition, grants, distribution and warranty conditions |

## Serving与Harness（2026-09-17）

以下记录保存官方repo README、许可、commit/release与所读专题文档。代码仅用于静态核验，不表示本地执行。版本和功能层次见[serving调研](../infrastructure/serving-framework-survey-2026-09-17.md)及[harness调研](../infrastructure/harness-survey-2026-09-17.md)。

| ID | 标题 | 阅读与原件 | 支持范围 |
|---|---|---|---|
| TECH-020 | vllm-project/vllm official repository and license snapshot | [原文](TECH-020/original.md) · [元数据/专题原件](TECH-020/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-021 | sgl-project/sglang official repository and license snapshot | [原文](TECH-021/original.md) · [元数据/专题原件](TECH-021/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-022 | lightseekorg/tokenspeed official repository and license snapshot | [原文](TECH-022/original.md) · [元数据/专题原件](TECH-022/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-023 | ml-explore/mlx-lm official repository and license snapshot | [原文](TECH-023/original.md) · [元数据/专题原件](TECH-023/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-024 | Blaizzy/mlx-vlm official repository and license snapshot | [原文](TECH-024/original.md) · [元数据/专题原件](TECH-024/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-025 | ggml-org/llama.cpp official repository and license snapshot | [原文](TECH-025/original.md) · [元数据/专题原件](TECH-025/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-026 | kvcache-ai/ktransformers official repository and license snapshot | [原文](TECH-026/original.md) · [元数据/专题原件](TECH-026/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-027 | ikawrakow/ik_llama.cpp official repository and license snapshot | [原文](TECH-027/original.md) · [元数据/专题原件](TECH-027/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-028 | langchain-ai/langchain official repository and license snapshot | [原文](TECH-028/original.md) · [元数据/专题原件](TECH-028/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-029 | langchain-ai/langgraph official repository and license snapshot | [原文](TECH-029/original.md) · [元数据/专题原件](TECH-029/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-030 | langgenius/dify official repository and license snapshot | [原文](TECH-030/original.md) · [元数据/专题原件](TECH-030/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-031 | run-llama/llama_index official repository and license snapshot | [原文](TECH-031/original.md) · [元数据/专题原件](TECH-031/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-032 | deepset-ai/haystack official repository and license snapshot | [原文](TECH-032/original.md) · [元数据/专题原件](TECH-032/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-033 | FlowiseAI/Flowise official repository and license snapshot | [原文](TECH-033/original.md) · [元数据/专题原件](TECH-033/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-034 | n8n-io/n8n official repository and license snapshot | [原文](TECH-034/original.md) · [元数据/专题原件](TECH-034/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-035 | anomalyco/opencode official repository and license snapshot | [原文](TECH-035/original.md) · [元数据/专题原件](TECH-035/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-036 | earendil-works/pi official repository and license snapshot | [原文](TECH-036/original.md) · [元数据/专题原件](TECH-036/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-037 | deepseek-ai/deepseek-harness official repository and license snapshot | [原文](TECH-037/original.md) · [元数据/专题原件](TECH-037/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-038 | openai/codex official repository and license snapshot | [原文](TECH-038/original.md) · [元数据/专题原件](TECH-038/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-039 | anthropics/claude-code official repository and license snapshot | [原文](TECH-039/original.md) · [元数据/专题原件](TECH-039/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-040 | NVIDIA/TensorRT-LLM official repository and license snapshot | [原文](TECH-040/original.md) · [元数据/专题原件](TECH-040/metadata.json) | Serving；文档/代码证据，非本地实测 |
| TECH-041 | langchain-ai/deepagents official repository and license snapshot | [原文](TECH-041/original.md) · [元数据/专题原件](TECH-041/metadata.json) | Harness；文档/代码证据，非本地实测 |
| TECH-042 | Run local agentic AI on the Mac using MLX — WWDC26 | [原文](TECH-042/original.md) · [元数据/专题原件](TECH-042/metadata.json) | Serving；文档/代码证据，非本地实测 |
