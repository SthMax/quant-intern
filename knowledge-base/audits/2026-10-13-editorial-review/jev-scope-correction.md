# Jev 与 A100 推理研究的范围更正

**2026年10月13日。** 用户指出Jev属于另一项工作。核对后，区分以下两者：

1. **TypeSafe Jev**是TypeSafe发布的独立System One模型，面向结构化决策。来源：[官方介绍](https://typesafe.ai/blog/introducing-system-one-models-and-jev)，网页标题及第31–36行于10月13日读取。
2. **A100仓库中的Jev Mode**是`shi3z/deepseekv4.1-A100-custom`附带的结构化字段评分模块。`engine.py`第424–434行用现有DeepSeek的`self.model`和tokenizer建立`JevEngine`；README把它另列为结构化模式。来源：[固定版本README](https://github.com/shi3z/deepseekv4.1-A100-custom/blob/580568edd6f84537ff042ded4ee842b892bf3ff4/README.md)、[engine.py](../../sources/TECH-077/files/dsv41/engine.py)、[jev.py](../../sources/TECH-077/files/dsv41/jev.py)。

之前的写法按“出现在同一仓库”把这个附加模块并列为A100通用推理提速机制，并简称为Jev，混淆了研究对象。现已从四部分讲稿及A100主文移出，通用推理部分集中解释模型执行、通信、缓存和MTP。

此前对模拟计时的判断，**仅针对该固定仓库中的`dsv41/bench_jev.py`默认调用路径**。它没有检验TypeSafe的模型、训练、服务或benchmark。以下保留原代码分析供追溯。

## 仓库附加模块的代码分析

### 字段候选评分与默认计时脚本

该仓库的Jev Mode面对的是“情绪选正／中／负、是否需要人工选是／否”一类固定字段任务。模型给候选打分，程序再拼成JSON。它省掉了逐token生成字段名、引号、逗号和整段格式文本的过程，还能把多个字段放进一批计算。

这个思路相当于把自由写作改成选择题。真正应衡量的是一秒能正确完成多少组字段，以及每组需要等多久。

README约13,000“有效token/s”的表格则来自默认benchmark的模拟分支。源码直接使用：

\[
t=0.08+11.4+\lceil字段数/32\rceil\times12.5\text{毫秒}.
\]

100字段得到61.48毫秒，798个组装后的token除以这段时间，恰好是12,979.8 token/s。这组数值由**固定公式估算**。真正调用模型的Jev接口另有实现；当前候选评分只比较首token，较适合首token不同的短选项。[计时与调用代码](../../sources/TECH-077/files/dsv41/bench_jev.py) · [Jev实现](../../sources/TECH-077/files/dsv41/jev.py)


- **Jev：**默认模拟脚本最多实际查询前10字段，其余填默认候选，解析失败时还可能将一致率记为100%。真实HTTP实现另存，适合用固定短候选和独立正确标签评价。

[公式复算](../../infrastructure/data/deepseek-a100-project-2026-10-12/jev-formula.csv)及[原脚本](../../sources/TECH-077/files/dsv41/bench_jev.py)仍按原版本保存。
