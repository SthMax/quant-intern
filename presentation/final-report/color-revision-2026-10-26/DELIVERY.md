# 主线配色修订交付

成品：`output/asset-management-llm-story-colors.pptx`

SHA256：`e0dd5d80c18d5f391968245f79d70941c87e8180faf44e86f3a123f31cfd4faa`

青绿色专属甲公司，紫色专属客户沟通稿。固定名字、资料色条和文档标题线持续追踪对象；人员、LLM、工具与测试块使用中性色。V1/V2同紫，修订文字用淡黄定位。

本轮没有实施导航进度方案。原有阶段文字、页码、导航位置与407个跳转全部保留。33页业务文字、表格数据、来源、讲稿和原对象位置未改，第11页最新措辞完整保留。

新增正文标记继承所属原对象的显现时刻，页顶标签始终显示。原动画对象、顺序和延时保持不变。

## 验证与预览

33页完成独立渲染和逐页静态检查；对象级颜色/内容检查与finalizer通过，布局警告为0。root已完成PowerPoint原生抽查，确认文档色条与结果同步出现、导航正常、双线颜色清楚。

- 逐页预览：`build/qa/final-render/`及`build/qa/lo-render/`。
- 全稿与代表页总览：`build/qa/all-slides.png`、`representative-pages.png`。
- 原生记录：`build/qa/native-playback-2026-10-26.json`。
- 对象与显现检查：`build/qa/color-and-content-check.json`、`appearance-bindings.json`。

## 可复现来源

逐页映射见`COLOR-MAP.md`及`src/color-map.json`。必要作者脚本均在`src/`，渲染与临时产物留在`build/`。

按顺序运行：`color_plan.py`、`create-overlays.mjs`、`apply_colors.py`、`finalize.mjs`，最后用`check_colors.py`检查。原生标签由Artifact Tool创建，再合入第11页修正版；原始文字和交互XML不重新导出。再次运行finalizer前需为已有成品与验证记录另存版本。
