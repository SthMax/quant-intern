# A100 H100 H200整机价格与交付依据

**访问日期：2026年10月12日。** 本页为来源索引；供应商HTML、原始监管／披露PDF和提取文本分别保存。价格与部署预算分析见[采购更新](../../infrastructure/server-gpu-procurement-2026-10-12.md)。主agent核对，人工复核pending。

| 来源 | 本地原文 | 核对范围 |
|---|---|---|
| [The Server Store，HGX 8×A10080](https://www.theserverstore.com/nvidia-hgx-8x-a100-80gb-sxm4-nvlink-gpu-server-zt-systems) | [HTML](a100-serverstore.html) | USD94,999，默认1TB／双EPYC7V12／八GPU，4×1TB NVMe加USD1,116；90天保修及翻新身份。未取得交易交付许可。 |
| [Exxact H100，TS4-193475697](https://configurator.exxactcorp.com/configure/TS4-193475697) | [HTML](h100-exxact.html)、[Markdown提取](h100-config.md) | USD319,924；八H10080SXM5／NVSwitch，双9454、1536GB。基础U.2选项数量未显露。 |
| [Exxact H200，TS4-118380266](https://configurator.exxactcorp.com/configure/TS4-118380266) | [HTML](h200-exxact.html)、[Markdown提取](h200-config.md) | USD326,524；八H200141SXM／NVSwitch，双9454、1536GB；三年零件／人工与远程支持。 |
| [ViperaTech H200 NVL](https://viperatech.com/product/nvidia-h200-nvl-graphic-card-141-gb-passive-pcie-900-21010-0040-000) | [HTML](h200-nvl-vipera.html) | 单卡USD33,500，缺货与两周发货文字并存；采用价格，交期待核。 |
| [BIS 2026年1月13日公告](https://media.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china) | [HTML](bis-h200-policy.html) | 公告指向有条件的逐案审查，具体法律条文以下方正式文本为准。 |
| [2026-00789，91FR1684](https://www.govinfo.gov/content/pkg/FR-2026-01-15/pdf/2026-00789.pdf) | [PDF](fr-2026-00789.pdf)、[机械提取](fr-2026-00789-text.md) | 2026-01-15生效；物理第1页开头含前一通知，相关规则从该页下方BIS标题开始，第2–6页为主体。区分美国出口与再出口等路径。 |
| [NVIDIA FY2027 Q2 10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf) | [PDF](nvidia-2027-q2-10q.pdf)、[选页提取](nvidia-10q-selected-pages.md) | 2026-08-27文件，物理27／37页：H200部分许可发货、中国限制及美国进口关税尚未转嫁给客户。 |

完整原件哈希和获取异常见[metadata](metadata.json)。Federal Register直接HTML返回访问挑战，未作为法条原件归档；改用govinfo官方PDF。两个配置器的页面默认状态与正式报价不同，CNY换算和D预算中的税、价格预留、增量服务均在[JSON](../../infrastructure/data/hardware-prices-2026-10-12.json)逐项说明。
