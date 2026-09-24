# 第四周：本地大模型部署方案

[第四周Release：四份PDF](https://github.com/SthMax/quant-intern/releases/tag/phase2-week4-2026-09-24)

[演示PDF](output/week4-deployment-options.pdf)

> 已同步四配置比较：单6000D、双6000D、M5 Ultra 256GB和DGX Spark；FP8权重、完整精度KV、单人20+目标。[三个场景的详细方案PDF](../../reports/week4-deployment-2026-09-24/README.md)与本演示稿配套。

资料截止2026年9月24日，价格分别保留9月21日／24日观察或估算日期。16:9 Beamer演示稿，共16页，其中12页主稿、4页附录，按用户指定的场景1、2、3排序。

主稿围绕配置选择、落地方式和业务产物组织。场景一比较四种硬件的预算、长context容量和单人速度；场景二比较Onyx Enterprise与Milvus自建；场景三介绍共享模型、Hermes与公司工具。预算分别注明主机、完整知识库硬件、Agent新增投入及合计范围。个人与知识库统一主用Qwen3.8-27B FP8，KV保持BF16／FP16；通用Agent以每任务262K和20并发为主口径，另列每任务最大context。速度为工程估算。

## 文件

- `main.tex`、`theme.tex`、`slides.tex`：Beamer入口、版式与内容，图形和图表均为原生矢量。
- `prepare.py`：从三套方案数据提取用于展示的数值。
- `data/slide-data.tex`、`data/source-manifest.json`：显示数值及逐项出处与来源哈希。
- `speaker-notes.md`：主稿讲述提示与问答时的口径。
- `build.sh`：使用XeLaTeX／latexmk构建PDF。
- `qa/checks.json`、`qa/review.md`：校验与版式审阅记录。

源方案位于`knowledge-base/infrastructure/`的三个`scenario-*.md`文件及对应数据目录。

## 构建

```bash
./build.sh
```

需要XeLaTeX、latexmk、ctex与Beamer。中文使用macOS黑体，西文使用TeX Gyre Heros；PDF嵌入字体，可直接分享。构建和逐页渲染文件留在忽略跟踪的目录中。

## 讲述顺序

| 页码 | 内容 |
|---|---|
| 1-2 | 主题与预算总览 |
| 3-5 | 四配置、个人工具环境与长context速度 |
| 6-8 | NAS权限知识库、平台与硬件选择 |
| 9-11 | 通用Agent、模型服务器与工具执行 |
| 12 | 配置选择与首批交付 |
| 13-16 | 计算口径、预算依据、缓存容量、主要来源 |
