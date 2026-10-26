# 完整版交互 PowerPoint 交接

## 成品

- `output/asset-management-llm-interactive-full.pptx`
- 33页，16:9，中文，正文、流程、文档与导航可编辑。
- SHA256：`b0761fa6b860ec9c36096581f9f9674a9ed38252c2e3c1e8cf693355e308ff14`
- 字体：PingFang SC。公司电脑可在PowerPoint中统一替换为公司字体，替换后复核中文换行。

## 放映方式

从第1页点击“进入演示”，按“下一步”顺序讲述。第3页是全景总图，第29页是七项建议回顾。第3页以后始终保留公司总图或固定左侧导航，可在问答时直接跳到各个任务。

| 导航 | 目标页 |
|---|---:|
| 公司总图 | 3 |
| 前台、研究分析 | 4 |
| 交易支持 | 9 |
| 客户材料 | 12 |
| 中台、材料审核 | 16 |
| 风险分析 | 19 |
| 后台、运营文件 | 22 |
| 工具开发 | 25 |

全部33页设置0.70秒Morph，使用稳定对象名称匹配。第33页“回总图”返回第3页。全稿407个内部跳转。

## 自动出现页

进入下列页面后，各组在150、700、1250毫秒依次出现。每页完成后点击“下一步”继续。单组页在150毫秒出现。

| 页 | 出现内容 |
|---|---|
| 4 | 财报、研报、会议资料 |
| 5 | 收入、成本、费用及对应经营因素 |
| 6 | 观点共识、分歧 |
| 7 | 研究要素的三行对应 |
| 8 | 公司季度分析结果 |
| 11 | 结构化交易字段 |
| 15 | 客户沟通稿V1 |
| 17 | 产品名称、资料期次、风险提示批注及高亮 |
| 18 | 修订后检查结果 |
| 21 | 持仓复核、补充研究、业务跟进 |
| 24 | 三项变更清单 |
| 26 | 需求、程序、测试与修订 |
| 32 | 三阶段实施建议 |

## 预览与讲述

- 逐页预览：`build/qa/lo-render/state-01.png` 至 `state-33.png`。
- 全稿缩略图：`build/qa/all-slides.png`。
- 代表页：`build/qa/representative-pages.png`。
- 每页讲者备注已写入PPT，包含讲述、衔接、来源编号、定位与URL。
- 内容与来源字典：`src/content.mjs`。
- 逐页讲述副本：`src/speaker-notes.md`。
- 封面图像与生成提示词：`assets/ASSETS.md`。

## 后续修改

主要制作源为 `build/build.mjs`，交互计划为 `src/state-plan.mjs`。生成的 `src/state-manifest.json` 同时记录最终页序、任务归属、持续对象、导航目标和出现组。导航与动画脚本 `src/add_interactions.py` 从manifest读取最终对象名称和页码。

在PowerPoint中修改文字和图形时保留对象名称，可保持跨页Morph匹配。调整页序后需复核内部链接。套母版后检查左侧导航、正文留白与文字换行。

构建顺序：生成base.pptx、执行add_interactions.py、执行finalize-interactive.mjs。最终交互候选通过验证后按原字节复制，不经过重新导出。再次运行finalizer前为旧成品与旧验证记录另存版本。

## 验证记录

- 33页逐页视觉审阅完成，最终文件通过独立LibreOffice转换复核。
- Package integrity、布局、字体、标题和可导入性检查通过，布局警告为0。
- 407个导航链接、33个Morph、13页出现动画与对象匹配检查通过。
- 同一客户沟通稿在15、16、17、18、24页的字段和观点一致性检查通过。
- 最终文件与动画candidate字节完全一致，保留原生交互特性。
- 2026年10月26日已在Microsoft PowerPoint for Mac全屏抽查：七个任务入口、前后导航、返回总图、财报驱动树及审核批注分组出现均正常。原生检查记录见 `build/qa/native-playback-2026-10-26.json`。

详细检查文件位于 `build/qa/finalizer-interactive.json`、`structure-review.json`、`visual-review.json`、`navigation.json`、`effects.json`。
