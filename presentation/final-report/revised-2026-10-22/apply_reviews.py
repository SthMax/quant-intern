"""Apply Chinese-language review, then audience and presenter revisions."""
from pathlib import Path
import json,hashlib

R=Path(__file__).resolve().parent
d=json.loads((R/'data/slides.json').read_text());s=d['slides']
patch_file=R/'qa/chinese-replacements.json'
patches=json.loads(patch_file.read_text()) if patch_file.exists() else []
if isinstance(patches,dict):patches=patches.get('replacements',patches.get('changes'))
deferred=[]
for c in patches:
 target=s[c['slide_id']-1]
 for key in c['path'][:-1]:target=target[key]
 key=c['path'][-1]
 if target[key]==c['old']:target[key]=c['new']
 else:deferred.append(c)

# These revisions address audience fit and the actual rendering, beyond wording.
s[0]['title']='大语言模型在公募基金\n工作中的应用'
s[3]['title']='大语言模型怎样利用我们提供的资料'
s[3]['lead']='大语言模型（LLM）根据看到的内容生成回答或操作指令。公司的当前资料，需要随任务提供或通过检索取得。'
s[6]['title']='文字问答与Agent任务'
s[6]['chat']='只要求文字回答\n得到解释或一段代码\n员工再复制内容\n运行代码、整理文件'
s[6]['steps']=['读取财报','选择口径','调用Python\n执行计算','核对结果\n保存Excel']
s[6]['notes']='如果只要求一段文字回答，后续操作仍由员工完成。委托Agent任务时，应用会围绕目标多次调用模型和工具：先读文件，确定要算什么，调用Python，检查返回结果，最后保存Excel和说明。这里的Agent是组织这些步骤的应用，例如OpenCode或Hermes；语言模型负责判断和生成，真正打开文件、计算和写入的是工具。一次任务往往包含多轮调用，因此需要保留前面读到的材料和工具结果。'
s[7]['choices'][1][1]='查询公司文件盘（NAS）\n按权限回答，并给出出处'
s[7]['choices'][0][1]='处理自己的文件与表格\n编写和修改代码'
s[7]['choices'][2][1]='多人开展分析与计算\n生成各自的工作文件'
s[11]['foot']='单Spark外部测试，随机token输入，未使用前缀缓存；完整配置见备查。'
s[11]['title']='Spark的长材料：先处理输入，再生成回答'
s[11]['meaning']='生成500个token，纯输出约25–34秒。1M容量测试首次等待约80分钟（仅输出64 token）。'
s[12]['first']=['未命中旧内容','重新处理接近512K输入','约26分钟（估算）']
s[12]['later']=['旧内容可复用','只处理追加的工具结果','新增1K约5秒；新增8K约40秒']
s[12]['practical']=['接着同一个任务追问','保留已处理内容，新材料追加在末尾']
s[12]['cache_parts']=[['已处理内容','财报、附注、先前对话与计算结果'],['本轮新增','一段新的工具结果']]
s[16]['acceptance']='检查：有权能查、无权不返回、改版后引用新版、撤权后查不到。引用能打开对应原文。'
s[15]['evidence'][1]='现行版：限额3万元\n7月1日起生效'
s[17]['resources']=['4×RTX PRO 6000D 84GB','3张卡运行Qwen27回答问题','1张卡处理检索，另配2台CPU服务器']
s[17]['scope']='本页预算对应上述完整硬件配置。资料可先接入一个部门目录，再逐步扩展。'
s[18]['title']='多人共用模型，分别完成项目工作'
s[18]['project']='团队任务：比较多家公司的收入变化，汇总成分析材料。'
s[18]['jobs']=[['研究员提出任务','比较多家公司的财报','返回各自项目的比较表与说明'],['量化同事运行工具','读取授权数据并执行计算脚本','返回计算结果、代码与测试'],['负责人查看产物','汇总获授权的比较表与证据','形成跨公司分析材料']]
s[18]['model']='共享端暂定DeepSeek-V4.1-Flash，供多人处理多材料分析和工具任务。'
s[18]['selection']='较大的模型集中运行，员工无需各自购置服务器；个人Qwen仍可处理日常文件任务。'
s[18]['notes']='假设团队要比较多家公司。研究员分别向自己的助手提交财报，量化同事通过授权接口取得数据、运行比较脚本，负责人查看得到授权的工作底稿并形成汇总。每一步都可以调用同一套DeepSeek模型服务，任务、文件和结果仍按员工权限分别保存。共享的价值是把较大的模型集中部署，员工不必各自购置服务器。DeepSeek暂作公司共享候选，公开金融研究评测提供了能力参照；个人Qwen继续处理日常文件任务。'
s[21]['note']='八卡H200用于研究20份1M长会话；A100方案侧重已有设备复用与较低购置预算。'
s[22]['title']='20人共享服务的响应目标'
s[22]['stages']=[['第一段何时出现','新资料处理、缓存读回和排队都会形成等待。'],['为什么工具任务还要时间','读取文件、查询业务系统和运行计算，也需要时间。']]
s[22]['public']='公开H200回放：32路，约157K输入、95%前缀命中；95%的请求约2.6秒内开始输出。'
s[23]['items'][3][2]='升级、故障处理，检查原有任务是否正常'
s[23]['engine']='A100使用适配后的vLLM模型服务，沿用现成的请求管理、监控与接口。'
s[24]['routes'][1][1]='把获准内容发给供应商模型\n再接收结果'
s[26]['charts'][0]['title']='个人：每工作日3项'
s[26]['charts'][1]['title']='公司：20人，每人每工作日5项'
s[26]['charts'][0]['format']='0.0'
s[26]['charts'][1]['format']='0'
s[26]['detail']='每年250个工作日；个人用量年增10%，公司年增25%。预算含技术实施、维护与工具费用。'
s[26]['notes']=s[26]['notes'].replace('首年每天3项','首年每工作日3项').replace('首年各每天5项','首年各每工作日5项')+' 每年按250个工作日计算，业务人员逐项复核的时间另外计入净节省。'
s[27]['foot']='三年预算，包含模型与工具服务器、部署、技术维护和运行费用。'
s[27]['insights']=[['硬件与设施包括','模型整机、工具节点和初始机房接入。'],['技术维护包括','日常监控、故障处理、升级后检查。'],['运行费用包括','用电、机位和软件支持。']]
s[28]['cases'][0][1]='20人，首年每人每工作日5项'
s[28]['cases'][1][1]='20人，首年每人每工作日10项'
s[28]['conclusion']='高用量情景从第二年增加一台GPU服务器，三年本地预算升至约713万元。'
s[28]['foot']='每年250个工作日；中量年增25%，高量年增50%；按100K–170K多轮任务规划容量。'
s[28]['notes']=s[28]['notes'].replace('首年各每天5项','首年各每工作日5项').replace('首年每天10项','首年每工作日10项')+' 每年按250个工作日计算。'
s[31]['closing']='个人助手处理手边文件；知识库提供授权资料；共享助手承接多人任务。先从公告提取与代码测试开始。'
s[35]['rows'][3][1]='单路110–140\n32路总1,040–1,379 token/s'
s[36]['rows'][0][0]='DeepSeek低峰\n输入／缓存读／输出'

# A few language edits were reviewed against the presenter's intermediate version.
for c in deferred:
 target=s[c['slide_id']-1]
 for key in c['path'][:-1]:target=target[key]
 key=c['path'][-1]
 assert target[key]==c['old'],(c['slide_id'],c['path'])
 target[key]=c['new']
s[11]['title']='Spark处理长材料要等多久'
s[12]['foot']='图中为输入处理时间估算；右侧假设旧内容的处理结果可完整复用。'
s[22]['notes']=s[22]['notes'].replace('较短长会话的参照','上述输入长度下的多轮任务参照')
s[25]['definition']='DeepSeek 8轮任务示例\n输入由100K增加到170K\n每轮输出2K'
s[29]['quote']='“10月6日签署1.20亿元供货合同，\n10月8日公告，尚未履行完毕。”'
s[30]['title']='收益记录：一个工时计算示例'
s[3]['lead']='大语言模型（LLM）根据看到的内容生成回答或操作指令。\n公司当前的资料，要随任务提供给它，或让它通过资料查询工具取得。'
s[22]['stages'][1][1]='文件读取、数据查询和计算也需要时间。'
s[13]['stages'][2][1]='从SSD读回中间结果\n再处理新内容'

(R/'data/slides.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
parts=['# 最终汇报讲稿\n\n2026年10月22日。32页正文，约40分钟；6页备查附录。\n']
for row in s:
 parts.append(f"## {row['id']:02d} {row['title'].replace(chr(10),' ')}\n\n{row['notes']}\n")
 if row['bridge']:parts.append('**接续：**'+row['bridge']+'\n')
 if row['sources']:parts.append('来源：'+' · '.join(f'[{u.split("/")[2]}]({u})' for u in row['sources'])+'\n')
(R/'speaker-notes.md').write_text('\n'.join(parts))
manifest=json.loads((R/'data/source-manifest.json').read_text())
manifest['slides_sha256']=hashlib.sha256((R/'data/slides.json').read_bytes()).hexdigest()
manifest['speaker_notes_sha256']=hashlib.sha256((R/'speaker-notes.md').read_bytes()).hexdigest()
manifest['chinese_replacements']=len(patches)
(R/'data/source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'Applied {len(patches)} Chinese copy edits plus presenter and rendering revisions.')
