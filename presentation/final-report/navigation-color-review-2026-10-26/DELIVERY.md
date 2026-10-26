# 本轮交付

## 导航与颜色方案

`NAVIGATION-COLOR-PROPOSAL.md`为方案说明，尚未应用到PPT。

推荐：左栏定位部门和主题，现有副标题行显示工作任务、同行做法、公司方案三步，页脚显示本题页次与全稿页码。案例多页保持同一步选中，不另增案例计数。青绿色专属甲公司，紫色专属客户沟通稿，跟随具体资料和文件持续出现；人、LLM、工具统一用中性角色块与明确文字区分。V1与V2均属同一紫色主线，修改文字用淡黄色标记并以文字说明状态。

文档给出第8、9、10、11、17、24页的具体显示示例，包含位置、字号、色值、对象标记与现有冲突的处理方法。

## 第11页修正版

文件：`output/asset-management-llm-slide11-corrected.pptx`

SHA256：`9f5fdb8dadf1bc7dd883908c99e5d02c1e3735c3e2c76b000936b72c1a380ad2`

可见修正：

- `LLM读取对手聊天`改为`LLM解析询价记录`。
- 报价例子前明确写出`交易员提供收到的报价`。
- 页底说明交易员核对`记录出处与报价时间`。
- 备注说明交易员先向交易对手询价，再提供收到的报价消息或沟通记录，LLM解析这些记录并整理查询结果与报价。

净价、面额、买入询价语境与原来源保持一致。第9页已明确由交易员询价、由交易对手返回报价，本轮未修改。

## 精确修改与验证

采用原PPTX的原生XML文字修改。只有`ppt/slides/slide11.xml`与`ppt/notesSlides/notesSlide11.xml`发生变化。其余32页、其余备注、所有关系文件、母版、主题、媒体等全部逐字节一致。

第11页仅改三个文字框中的段落文字及讲者备注。形状位置、大小、字体、颜色、链接、Morph和出现动画均保持原样。全稿仍为33页、407个原生链接、33页Morph。

Finalizer通过，布局警告为0，成品与候选文件字节一致。第11页已通过Artifact Tool渲染和独立LibreOffice转换检查，文字可读，无溢出。PowerPoint原生抽查由root继续。

预览：`build/qa/slide11-corrected.png`。检查记录：`build/qa/final-scope-check.json`、`change-scope.json`与`finalizer-interactive.json`。

## 修改源

- `src/correct_slide11.py`：从原成品生成局部修改候选，并检查修改范围。
- `src/slide11-edit.json`：可见文字与备注的前后内容。
- `src/source-slide11.patch`：对应原制作源第11页的最小补丁，尚未应用到已提交的原目录。
- `src/finalize.mjs`：验证并保存新成品，保留原始交互XML。
- `src/check_final.py`：对成品与原稿进行包级、页面级及交互一致性检查。

原成品与原制作目录均未覆盖，本轮没有commit或push。
