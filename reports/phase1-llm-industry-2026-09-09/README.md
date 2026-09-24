# 基金公司LLM应用调研

**2026-09-21：**当前仓库版本已完成机构匿名化，研究内容与资料截止日沿用原稿。历史Release保留原发布版本。

当前版本基于用户手动修改和批注逐段重写，强调明确的行业发现、LLM作用、业务成果与项目建议。修订日期为2026年9月11日，研究资料截止日保持2026年9月9日。

- [PDF报告](report.pdf)：21个物理页，页脚编号1–20。
- [LaTeX正文](main.tex)、[公司表A](landscape.tex)、[法规附录](governance-appendix.tex)、[实验结果与接入条件](quant-evidence.tex)。
- [本次逐段修改说明](editorial/assertive-revision.md)、[用户修改与批注](editorial/user-edits-2026-09-11.patch)。
- [当前PDF检查记录](qa/review.md)、[PDF机器校验](qa/checks.json)、[与检查点的对照](qa/assertive-revision-checks.json)。
- [来源与原件哈希](data/source-manifest.json)、[同口径规模数据](data/cohort.json)。

报告保留投研分析、数据查询、知识与合规、LLM辅助量化四个方向。案例按业务问题、LLM处理过程、产物与成果展开；量化部分介绍文本信号、因子生成与迭代、研究Agent工具调用。摘要和结尾明确建议推进本地部署，以公告事件提取作为量化原型，再扩展到因子表达式、代码与研究Agent。

正文集中介绍方法与价值，实验数字、数据范围和具体接入条件保留在附录。国内材料以2026年披露为主，2025年MENTOR为方法补充；Man AHL与QuantaAlpha为外部研究对照。本次仅修订报告，未执行模型/API实验、本地部署或回测，PPT和知识库原件保持不变。

## 编译与校验

macOS安装有XeLaTeX/latexmk的TeX Live或MacTeX后，从本目录运行：

```bash
./build.sh
```

当前使用TeX Live 2026、macOS宋体和黑体，以及TeX Gyre字体。中文可搜索和复制，接收者阅读PDF无需另装字体。跨平台编译时需在`preamble.tex`指定当地可用的中文字体。

如需根据知识库重新生成来源目录、编号和哈希清单：

```bash
python3 prepare.py
./build.sh
```

使用已安装pypdf/pdfplumber的Python进行机器校验：

```bash
python3 verify.py
```

当前引用46项来源，机器校验核对117个原件或代码文件哈希、46个外链及20家公司的规模值。PDF经过全页渲染检查，版本与路径见`qa/render-manifest.json`。PNG、抽取文本和编译中间文件不提交。

## 历史版本与评审

2026-09-16起，组织结构与案例去重按[独立修订计划](editorial/fixing-plan.md)推进，与Phase 2模型研究分别安排。本链接记录下一轮修订安排，当前PDF尚未据此重写。

- `39a2417`：首次独立mentor评审前的旧稿。
- `fc2cf1d`：按两轮独立评审完成的业务版报告。
- `0b85429`：叙述方式讨论前的检查点。
- `94c1b25`：按当时确认的口吻重写，加入表A概览。
- `98bab07`：局部修正口语措辞。
- `15b46fb`：明确LLM职责的版本，本次用户手动修改前的检查点。

历史mentor评审、`editorial/llm-role-revision.md`和`qa/role-revision-checks.json`记录此前版本，保持原样。本次修订未新增独立mentor审阅；当前编辑与检查记录分别见`editorial/assertive-revision.md`和`qa/review.md`。

研究基线`e51e4c9`的原始材料和`PROJECT_PLAN.md`保持不变。`data/report-manifest.json`中的研究管理数量不是公司生产部署数量。当前PDF身份以`qa/checks.json`中的SHA-256为准。
