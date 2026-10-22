"""Draw editable SVG comparison charts from the archived CSV tables."""
import csv, pathlib
from html import escape

HERE=pathlib.Path(__file__).resolve().parent
COLORS=['#0f5f78','#39a5a3','#dfa342']
def rows(name):return list(csv.DictReader((HERE/name).open()))
def svg_chart(path,title,subtitle,groups,series,footer):
    # groups = [(model label, values)]; fixed 0–100 axis for every figure.
    rowh=98 if len(series)>1 else 65
    top=182; bottom=top+rowh*len(groups); height=bottom+160
    x0=485; width=1000
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="{height}" viewBox="0 0 1600 {height}" role="img" aria-label="{escape(title)}">',
       '<rect width="1600" height="100%" fill="#fff"/>',
       '<g font-family="PingFang SC,Microsoft YaHei,Noto Sans CJK SC,Arial,sans-serif" fill="#163248">',
       f'<text x="45" y="52" font-size="32" font-weight="600">{escape(title)}</text>',
       f'<text x="45" y="91" font-size="21" fill="#526777">{escape(subtitle)}</text>']
    for i,label in enumerate(series):
        x=485+i*280
        s += [f'<rect x="{x}" y="116" width="22" height="18" rx="2" fill="{COLORS[i]}"/>',
              f'<text x="{x+32}" y="132" font-size="20">{escape(label)}</text>']
    for tick in range(0,101,20):
        x=x0+tick*width/100
        s += [f'<line x1="{x}" y1="{top-12}" x2="{x}" y2="{bottom}" stroke="#e3ebef"/>',
              f'<text x="{x}" y="{bottom+31}" font-size="18" text-anchor="middle" fill="#526777">{tick}</text>']
    for i,(label,values) in enumerate(groups):
        y=top+i*rowh
        s.append(f'<text x="45" y="{y+36}" font-size="23" font-weight="500">{escape(label)}</text>')
        for j,value in enumerate(values):
            yy=y+j*23
            w=float(value)*width/100
            s += [f'<rect x="{x0}" y="{yy}" width="{w:.2f}" height="18" rx="3" fill="{COLORS[j]}"/>',
                  f'<text x="{x0+w+8:.2f}" y="{yy+16}" font-size="18">{float(value):.2f}'.rstrip('0').rstrip('.')+'</text>']
    s.append(f'<text x="{x0+width/2}" y="{bottom+63}" font-size="20" text-anchor="middle">分数（0–100；越高越好）</text>')
    for i,line in enumerate(footer):s.append(f'<text x="45" y="{bottom+102+i*26}" font-size="18" fill="#526777">{escape(line)}</text>')
    s.extend(['</g>','</svg>'])
    (HERE/path).write_text('\n'.join(s)+'\n')

extract=rows('extractbench.csv')
names=['Qwen3.8-27B FP8','Qwen3.6-35B-A3B FP8','DeepSeek-V4.1-Flash 原版','GLM-5.3-Flash','Kimi K3','Gemma 4 26B A4B']
svg_chart('extractbench-length.svg','短文提取较好，长列表完整性仍需专门处理','ExtractBench原版 · 相同370份文档及schema · 分长度的value F1',
 [(n,[r[k] for k in ['short_f1','medium_f1','long_f1']]) for n,r in zip(names,extract)],
 ['短文 ≤10页','中篇 11–50页','长篇 >50页'],
 ['来源：基准作者CSV，修订56b8fdd；资料截止2026-10-20。','短／中／长文各252／98／20份；端点、thinking、输出上限不同，完整条件见配套表。'])

finance=rows('finance-agent-v2.csv')
svg_chart('finance-agent-v2.svg','金融研究任务需要保留GLM与MiMo对照','Finance Agent v2 · 关键条件门槛＋加权部分得分 · 2026-10-18作者榜',
 [(r['model'].replace('DeepSeek V4.1 Flash','DeepSeek V4.1 Flash'),[r['partial_credit_pct']]) for r in finance],['主指标'],
 ['来源：Vals AI Finance Agent v2；同一默认harness、六种工具、每题2小时。','1017版本单列；分数不是整题成功率，未披露逐模型完整推理参数和置信区间。'])

biz=rows('bizbench.csv')
svg_chart('bizbench-goal-strict.svg','目标完成后，还要检查过程与授权','BizBench v1 · 相同50项业务任务 × 每项3次 · 作者论文2026-10-14',
 [(r['model'],[r['goal_pct'],r['strict_success_pct']]) for r in biz],['目标完成G','G、P、F全部通过'],
 ['来源：BizBench表1；用户模拟器均为DeepSeek-V4.1-Flash。','支付业务基准，用于说明评价方法；不是基金业务验收结果。'])

aa=rows('artificial-analysis.csv');order=['Qwen3.8-27B','DeepSeek-V4.1-Flash','GLM-5.3-Flash','MiMo-V2.6-Flash','Kimi-K3','Gemma-4-31B']
labels=['Qwen3.8-27B xhigh','DeepSeek-V4.1-Flash max','GLM-5.3-Flash','MiMo-V2.6-Flash','Kimi K3 max','Gemma 4 31B reasoning']
svg_chart('aa-selected.svg','按任务比较长资料推理、自动化与代码','Artificial Analysis作者同站分项 · 2026-10-20快照 · 各指标独立',
 [(label,[next(r['score_pct'] for r in aa if r['model']==n and r['benchmark']==m) for m in ['AA-LCR v1.1','AutomationBench-AA','Terminal-Bench 4.0']]) for n,label in zip(order,labels)],
 ['AA-LCR v1.1','AutomationBench-AA','Terminal-Bench 4.0'],
 ['来源：AA模型对照页与方法；AA-LCR约100K多文档问答，不是接近满1M窗口测试。','模型沿用作者thinking标签；分项各有任务及harness，不合成总分。'])
print('Wrote 4 editable SVG figures.')
