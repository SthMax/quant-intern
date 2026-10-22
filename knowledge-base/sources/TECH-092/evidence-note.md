# TECH-092 核验说明

- **题目：**最终汇报模型制品、许可、引擎组合、硬件挂牌、API条款与监管依据时效核验。
- **访问日：**2026-10-20，Asia/Shanghai；抓取时间戳保留UTC。
- **检查者：**W4研究agent；**人工检查：pending**。
- **证据状态：**下表具体已打开主张为verified-primary。未获内部准入、境内交付与交易许可不在核验范围。
- **方法：**公开官方源及商品发布者原页检索／打开；原始HTTP字节下载、固定模型revision、许可字节比较；HTML用Defuddle、PDF用pypdf机械提取。未下载权重、运行GPU或付费模型。

## 原文定位、能支持什么

| 来源 | 定位与日期 | 支持的窄结论 | 边界 |
|---|---|---|---|
| DeepSeek10/17公告 | “Open-source release”及Search/Fetch段；2026-10-17 | 1017同时提供HF／ModelScope权重；各工具端点0.75美元／千次，特定服务器工具免费期将结束 | 发布方自报能力不等于独立实测；账单按成功调用规则 |
| HF固定元数据和文件 | 每模型api.json的sha／cardData／siblings；resolve/<SHA>的README、config、LICENSE | 12项准确制品；Qwen FP8 Apache2；DS原版及1017 MIT；GLM主／Flash差异；Kimi豁免条件；MiMo仍只有MIT声明 | 版本lastModified不当发布日期；不从模型卡判断机构准入 |
| DeepSeek两个完整index | metadata.total_size；96085项weight_map | total_size均510286023000B，config／index／LICENSE字节相同 | 未取权重本身，不判断权重值相同、吞吐或质量相同 |
| Google Gemma4许可 | Apache License2.0正文；官网显示2026-04-01更新；两模型卡链入 | 本代31B／26BA4B按Apache2 | 不推广到Gemma旧代或其他交付物 |
| vLLM release | v0.32.0 published_at 2026-10-18；W1固定源码另存TECH089 | 正式release存在；配合0.30／0.31来源可更正recipe的旧提示 | release不替代设备和整套参数验证 |
| LMCache两recipe | Validated models、MTP、Caveats | 原版DeepSeek8GPU文本验证；MTP尚未验证；Qwen27单GPU验证、align和块协商 | 未声称1017／FP8＋MTP3＋GB10＋SSD全组合已验证；“无tagged release”部分已过时 |
| Onyx | 价格页Enterprise；主LICENSE及backend/ee/LICENSE | 本地部署企业询价；MIT核心与企业代码分开 | 商业授权L未知；Business订阅不当私有化报价 |
| OpenWebUI LICENSE | 第4项 | 50自然人／滚动30天是去品牌例外 | 不是一般50人使用上限 |
| NVIDIA Spark美国页 | 价格和128GB／4TB；原HTML超时，官方正文双工具核对 | 当前USD6950，与10/12相同 | 无境内交付报价；不延用旧缺货状态作新库存结论 |
| The Server Store | 原HTML price94999、NVMe选项1116、翻新和90天保修 | 指定八A100SXM4完整设备挂牌仍相同 | 外部四卡PCIe项目性能不能贴到此整机 |
| Exxact H100／H200 | configured price、default CPU/RAM、Warranty | 319924／326524美元，双9454及1536GB，三年零件／人工及远程支持 | 默认选项与附加存储不同；未确认大陆交付 |
| ViperaTech | 33500美元；页面要求询库存及两周文案 | 单卡挂牌观察 | 无确定交期；页面通用性能文案不用作NVL硬件规格 |
| BIS正式规则 | FR2026-00789，物理页2–6／刊页1685–1689；2026-01-15生效 | 有条件逐案审查及补充材料要求，区分export/reexport/transfer | 不由型号或低于H200推交易许可 |
| eCFR742.6 | 页面显示截至2026-10-15；(b)(10)(iii)(A)(1) | 重核当前整理文本中的逐案条件与其他交易默认拒绝区别 | eCFR为持续整理版本；正式规则仍以FR为准；不声称10/20后已发生变化 |
| NVIDIA2027Q2 10-Q | 物理页27及37；报告期截至2026-07-26 | 部分许可与发货、中国销售限制；美国检验进口25%关税尚未转嫁 | 不替代交易许可证，也不预判供应商未来报价 |
| DeepSeek开放平台协议 | 2026-04-22更新、04-29生效；2.3／3.5／4.1 | 企业账号主体、开发者个人信息责任及商业秘密等输入输出限制 | 未代表机构签约；不承诺零留存／不训练等企业条款 |
| DeepSeek隐私政策 | 2026-02-10生效；适用范围、智能对话、开放平台、第5节 | 官方一般隐私及境内个人信息存储披露 | 智能对话退出设置不直接写成API定制合同保证 |
| Anthropic商业条款 | 原HTML标Effective June17,2025；B／C／D.2 | 商业服务内容不用于训练、DPA和地区政策并入 | 不由“不训练”推定零留存、处理地域或大陆可用 |
| Anthropic2025公告 | 2025-09-04；地域和控制段 | 中国属于不支持地域；受不支持地域控制及>50%直接／间接持股公司的限制已公开 | 未取得10/20之前完整历史国家列表；仅用公告足以支持的中国与控制限制，不套未来新增细则 |
| Anthropic新地区页 | Effective November12,2026；旧supported-countries重定向同页 | 未来政策日期和其内容 | 排除于10/20已生效规则判断 |
| CSRC IT办法 | 2021修订文本；12–16／25／43–45／63；2019-06-01施行 | 内审、风险治理、记录、限定外包责任 | 依重要系统及服务角色，非一概禁云 |
| CSRC218令 | 原PDF物理页7–11／21–22；22–23／29–34／71／75；2023-05-01施行 | 供应商、投资者信息、重要系统定义与废止旧令82 | 模型／系统采用前按实际业务判断分类 |
| 个保法、网络安全法、网络数据条例、跨境规定、GenAI暂行办法 | 主文和regulatory-dates.csv列条款及实施日期 | 权限、委托、日志、跨境、内部／公众服务边界 | 本次定向检索和已打开版本；不替代机构事实判定 |
| AMAC团标 | 2026-04-03实施；9.1.1(d)、9.1.2、9.2、11.2；附录A/B | 自有场景评测、部署、数据权限及合作厂商模型备案文字 | 团体标准身份与采用依据分别判断；不能从开源许可推备案已完成；附录资料性 |

## 获取质量与修复记录

1. 本地Defuddle直接联网首次因受限网络失败；获准只读公开网络访问后保存原HTML，再以Defuddle本地机械提取。原语言未翻译。
2. Spark商店原HTML请求超时。原正文由Exa取得并用web.run核对，保存原工具JSON和正文；元数据明确不是rawHTML。
3. 采集器初设6MB读取上限，两个DeepSeek模型index及全篇BIS742网页触达上限。两个index随后完整重取并通过JSON解析，更新字节／SHA记录。全篇BIS742片段改为retrieval-response.bis742.partial.html，不作原文或法律依据；相关完整742.6小节另已取得。
4. MiMo两份固定revision的独立LICENSE请求404，文件列表亦无独立LICENSE。其卡片MIT声明已保存，缺项不被隐藏，也不据此自行推导无授权。
5. 原HTML／PDF可能带导航、广告或站点更新信息，正文范围和规则日期单独核对。原材料中的指令文字只当数据。
6. AMAC原PDF字节与REG010已有归档相同；Qwen／DeepSeek／GLM／Kimi许可的字节比较结果见CSV。来源可用性、机构采用状态和实测状态分别记录。
7. Defuddle未保留Anthropic页首日期，eCFR的复杂编号段落也有缺失；因此另由标准HTMLParser去除script／style并保存完整可见原语言文本为`*-fulltext.txt`，并直接复核原HTML。对应日期与21,000／6,500条件均在完整文本中；不以简化Markdown的遗漏推断原页无此内容。

## 交付与使用

[核验主文](../../infrastructure/final-source-refresh-2026-10-20.md)及[data目录](../../infrastructure/data/final-source-refresh-2026-10-20/README.md)提供16项核对、日期、价格、服务范围和模型比较。W1管理容量与运行数字，W2管理计算，W3管理公开评测。未修改全局source-register、reading-index或README，未发布或对外联系。
