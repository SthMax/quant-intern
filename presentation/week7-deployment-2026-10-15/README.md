# 第7周汇报：长上下文Agent部署与推理优化

[打开新版PDF](output/gpt-pro/week7-long-context-revised-kv-offload.pdf) · [可编辑PPTX](output/gpt-pro/week7-long-context-revised-kv-offload.pptx) · [阅读汇报讲稿](speaker-notes.md) · [GitHub Release](https://github.com/SthMax/quant-intern/releases/tag/phase3-week7-2026-10-15)

## 10月15日发布版本

用户提供的Pro修订版共34页，含27页正文和7页附录，增加分层KV缓存、读取时间算例及可点击来源。发布文件为新版PDF、对应PPTX，以及补充了KV offload讲解的`speaker-notes.md`。

讲稿第五部分保存本次聊天中的KV offload说明：AI Infra Book章节、vLLM原生卸载与LMCache MP、CPU／SSD读取算例、公司服务器与Spark的差别，以及所选模型的支持情况和原始链接。

本次沿用用户提供的PPTX和PDF。文件清单与哈希见[发布检查记录](qa/release-2026-10-15.json)，发布介绍见[release-notes.md](release-notes.md)。

## Pro版修改材料

10月15日用户提供的[Pro版PDF](output/gpt-pro/week7-long-context-redesign.pdf)与[PPTX](output/gpt-pro/week7-long-context-redesign.pptx)共32页，已随审阅前版本提交为`e521364`。

[交给Pro的补充说明](pro-revision-brief-2026-10-15.md)列出六处页面补充、两页分层KV缓存内容、传输算例和原始链接。补充内容已纳入用户提供的34页修订稿；下方继续保留此前Beamer的文件和构建说明。

## 此前Beamer版本

2026年10月14日制作，供10月15日汇报。按Spark个人方案、DeepSeek公司方案、A100定制推理和AI Infra Book四部分讲解；预算随部署方案介绍，公司知识库作为共享检索接口简述。

讲稿已经用户认可，Beamer共25页：20页主稿、5页附录。沿用此前演示稿的16:9版式与配色，主稿介绍方案、性能、预算和原理，附录提供实测、容量计算、公开测试与价格构成。研究计算和原始来源继续维护在知识库，本目录集中保存此次汇报材料。

研究整理检查点为`133c798`；本次逐段中文改写前的检查点为`3899e73`。编辑意见见[措辞审查](../../knowledge-base/audits/2026-10-13-editorial-review/README.md)，执行进度见[第7周计划](../../weekly/week-07-plan.md)。

10月14日补充A100与modified vLLM的比较：区分模型能力与引擎增量，按官方原生制品重算权重占用，并明确公司A100采用modified vLLM。公开速度保留卡数、互联和负载，讲稿不将跨设备结果写成同机性能结论。

## 逐段中文审改

10月14日按用户反馈，由一名语文老师agent分六批审改全部85个段落、表格或列表单元，再通读整篇。主agent核对技术含义和数值，删除重复段落，统一“上下文”“KV Cache”“缓存命中”“prefill”“decode”等用语。

[逐段原文与修改记录](../../knowledge-base/audits/2026-10-14-chinese-prose/teacher-review.md)保留每段的问题和最终改文。用户指出的七项均已落实，用户已认可讲稿。Beamer制作保留该版讲稿原文。


## 此前Beamer页码与材料

| 页码 | 内容 |
|---|---|
| 1–2 | 封面与四个主题 |
| 3–6 | Spark个人方案：架构、上下文与速度、缓存复用、共享容量及费用 |
| 7 | 公司知识库的一页回顾 |
| 8–11 | DeepSeek公司方案：架构、20会话容量、活动请求与等待任务、整机预算 |
| 12–16 | A100项目：架构、贡献归属、modified vLLM性能与消融、原生权重显存 |
| 17–19 | AI Infra Book：任务耗时、合批与带宽、工具环境内存 |
| 20 | 配置与使用方式总结 |
| 21–25 | 附录：Spark实测、缓存预算、AgentX回放、费用构成、主要来源 |

## 此前Beamer文件组织与构建

- 此前Beamer PDF：[output/pdf/week7-long-context-deployment.pdf](output/pdf/week7-long-context-deployment.pdf)。
- LaTeX入口：[main.tex](main.tex)；内容：[slides.tex](slides.tex)；样式：[theme.tex](theme.tex)。
- 已认可的[讲稿](speaker-notes.md)保留完整解释；[页码映射](data/slide-map.json)对应讲稿小节与知识库来源。
- [prepare.py](prepare.py)读取已有研究计算，生成数值宏和来源哈希；不运行GPU实验。
- [verify.py](verify.py)检查PDF页数、字体、文字边界、关键数字、来源和讲稿完整性。
- [检查记录](qa/review.md)与机器检查结果保存在`qa/`；`build/`及渲染PNG为忽略跟踪的中间文件。

此前Beamer的源码、来源哈希与检查记录对应`e521364`提交；10月15日讲稿新增KV offload内容，旧PDF保留原版。需要复核旧构建时，请使用该提交的讲稿与数据。

本机使用XeLaTeX／latexmk和现有中文字体：

```bash
bash presentation/week7-deployment-2026-10-15/build.sh
```

验证需Python的`pdfplumber`和`pypdf`。本次已检查全部25页；四份此前发布的PDF保持原版本。
