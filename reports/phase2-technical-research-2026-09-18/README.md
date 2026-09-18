# 本地大模型技术与应用调研

Phase 2第3周阶段报告，资料截至2026年9月18日。沿用Phase 1报告的LaTeX排版和正式叙述方式，以介绍与分析为主。

- [PDF报告](report.pdf)：24个物理页，正文页码1–23；含5幅流程/结构图、15张表、50项来源。
- [主文件](main.tex)：摘要、目录与章节组织。
- [模型](models.tex)、[许可](licenses.tex)、[推理服务](serving.tex)、[业务应用](applications.tex)、[部署分析](deployment.tex)。
- [版本与口径附录](appendix.tex)、[参考文献](references.tex)。
- [来源与文件哈希](data/source-manifest.json)、[模型制品记录](data/model-artifacts.json)。
- [验证结果](qa/checks.json)、[版面与内容检查记录](qa/review.md)。
- [独立模拟mentor初评](editorial/mentor-review-v1.md)、[修订与历史复核记录](editorial/revision-notes.md)。初评对应此前22页版本，保留原文供追溯。

## 内容与表达

报告从基金业务中的材料、任务和产物出发，介绍模型、Serving framework、Harness与完整应用的分工。模型部分覆盖8项候选及许可差异；应用部分重点解释员工工作台、资料研究平台、固定流程与通用助手做什么、具有什么优点，并以说明性业务任务分析其用途。修订版以两期虚构财报和一份CSV贯穿工作台、固定流程与通用助手，并给出专业个人机和部门共享两套参考组合。

第2章按“规模与架构—Qwen与Gemma—大型模型—显存与内存”组织，评测结果融入具体模型介绍。正文直接介绍能力、优势、原理和业务价值，摘要与结论归纳三层系统如何形成工作效率。版本、协议、许可门槛及研究方法集中于附录。图1分开呈现模型和工具的请求与返回。

这是基于官方资料的阶段性研究报告，尚无本项目GPU部署、任务benchmark、设备报价或三年TCO结果。报告中的财报分析、事件提取与材料预审为说明性用法，不是已发生的MSIM部署。

## 构建

使用现有TeX Live/MacTeX、XeLaTeX和latexmk，中文字体沿用macOS宋体与黑体。首次编译时通过LaTeX Compile技能检测并调用现有TeX环境。

```bash
python3 prepare.py
./build.sh
```

`prepare.py`按正文引用顺序生成文献编号、来源清单与模型制品记录，并先核对原始文件哈希。正文日期使用Asia/Shanghai，manifest保留原始抓取时间。`build.sh`将编译中间文件放在`build/`，输出稳定文件名`report.pdf`。

验证需要安装有pypdf和pdfplumber的Python：

```bash
python3 verify.py
mkdir -p qa/render-user-final
pdftoppm -scale-to 1400 -png report.pdf qa/render-user-final/page
```

PNG、抽取文本及编译文件已由本目录`.gitignore`排除。源码、PDF、数据清单和检查记录集中保存在本目录。此前Phase 1报告与PPT保持不变。
