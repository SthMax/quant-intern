# TECH-089证据核对说明

**日期：2026-10-20｜审查者：研究agent｜人工复核：待完成。**

本包核对三场景最终汇报中的软件版本、Engram共享与KV恢复机制。来源为vLLM官方发布与固定tag源码、LMCache官方recipe与文档。原文均保留英文；本说明及基础设施报告为作者分析。

## 可支持的窄结论

1. vLLM0.30正式加入DeepSeek-V4.1-Flash；0.31发布说明加入同机DP Engram host共享，0.32是10/20读取的latest正式版。
2. 共享host表需要cpu_offload、DP>1、同机共享IPC与足够/dev/shm；两个独立serve进程不能据此自动按一份计。embedding_across_dp为另一种分片／collective方案。HBM权重副本与KV池仍独立。
3. 0.32固定DeepSeek attention.py与此前TECH-080审阅文件字节相同；Hopper584B主记录、132B索引、576B页的已审1827B/token/rank推导仍适用。静态源码不验证任何新启动池或速度。
4. LMCache recipe列Qwen3.8-27B单GPU文本验证与DeepSeek-V4.1-Flash八GPU文本验证。Qwen要保存全注意力KV及GDN状态；DeepSeek存在多组geometry、非cacheable scratch及重算路径。DeepSeek MTP尚未验证。
5. Qwen recipe没有建立“GB10＋FP8制品＋FP8 KV＋MTP3＋SSD”的完整验证结论；当前实验性align与score-level正确性限制需保留。
6. vLLM原生CPU与多级offload、LMCache MP独立服务均有官方说明；它们是可比较的实现路径，不自动证明具体选型达到热TTFT或质量目标。
7. 0.32的max_tokens由预留改为上限；本项目8192输出预留由Harness／网关显式维持。

## 冲突与限制

- LMCache V4.1 recipe的“未有tagged vLLM”警示与官方0.30/0.31/0.32发布事实冲突；该警示判定为陈旧。模型release与LMCache精度／MTP组合验证分开处理，不能把前者修订扩展成后者已验证。
- 通用hybrid设计页部分Mamba文字属于较早设计状态；当前模型recipe与对应源码用于具体支持判断。
- 0.32一般低位KV支持扩展并不证明DeepSeek V4.1的Hopper可切换到SM100专用格式，容量数字必须对应模型路径。
- 当前网页和代码描述不是本项目GPU测试。旧Spark／AgentX速度及token池继续引用TECH-076／084原配置；本包不替换这些测量。
- LMCache四份rst均以固定commit请求复核成功；L2网页仅按读取时原HTML与hash冻结。首次固定commit请求中两份网络失败，重试后逐字节核验通过。

## 输出与检查

[最终配置报告](../../infrastructure/final-configurations-2026-10-20.md)和[可复算数据](../../infrastructure/data/final-configurations-2026-10-20/README.md)分别呈现容量、速度身份、目标与价格边界。17项检查验证输入／输出长度、KV与状态字节、RAG9／3份准入、公司post-graph容量、共享主存预算及源文件一致性。未运行模型、下载权重、访问GPU、使用付费API或宣称业务质量验收。
