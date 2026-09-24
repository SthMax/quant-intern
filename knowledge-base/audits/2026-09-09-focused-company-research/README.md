# 2026-09-09 重点公司研究与入库审计

任务：按用户1–5分标准深挖强公司，尤其易方达，核对能否获得4/5分技术材料。结果见[重点研究](../../companies/focused-research-2026-09-09.md)。

新增FUND-113–119：MENTOR论文及补充Prompt、Index-Hub仓库及官方帮助、SLAG、FinCoT、联合投资Agent比赛。监管子任务新增REG-013–016并提供[独立复核](../2026-09-09-regulatory-review/README.md)。整合后112个来源：104主阅读、4辅助、4来源链；79一手、31候选/二手、2未解决。新研究材料不增加公司或生产项目计数。

评分初始状态保存在[before-state](before-state/evidence-scores-2026-09-09.md)及对应JSON。只将易方达3→4，其余20家公司记录保持不变。原始101个来源的source.*、original.md和metadata.json保持本轮之前字节，不将文章中的错误法律引用直接改写进原文。

## 获取与验证范围

- 学术/代码入口：英文公司署名、作者研究主页、期刊原站、GitHub官方组织；见[检索记录](search-log.md)。没有再次访问受限微信页面。
- 原件：3份PDF共33页；MENTOR正文5–8、13–14页、补充1–3页以及帮助8页渲染；重点人工视觉审查算法、Prompt、实验表和数据声明。其余页面通过文本提取审阅，不声称逐页视觉复核。
- 仓库：Git commit固定、Git tree保留、下载文件逐一SHA-256。源码文档移入FUND-115/117/118/119下的repository；盈米仅放外部辅助。未下载大数据、图谱dump和大图片，不冒称完整克隆。
- 代码：对已归档Python进行AST语法检查；对检查过的纯guardrails做21次合成字符串调用，结果见[index-hub-code-review.json](index-hub-code-review.json)。不执行安装、真实API、数据库、模型或交易；未获取凭据或用户金融数据。语法和冒烟通过不能推出端到端可用。
- PDF提取留原语言、物理页号；README阅读副本只补来源说明及固定版本相对链接，原README字节另存。网页正文使用Defuddle从已保存官方HTML提取。

关键缺口：Index-Hub两子包缺配置、行情描述不一致；MENTOR数据说明存在映射疑点及版权限制；SLAG私有金融KG/实验不开放；FinCoT是数据而非训练代码；投资比赛的注释与当天新闻截止实现不同，部分数据为LFS指针。详见研究报告，均未擅自修改上游文件。

机械检查结果：[verification.json](verification.json)。审查只判断本轮归档、索引和评分修改；不表示所有行业资料已穷尽，也不表示可商用或实习机构内部获批。
