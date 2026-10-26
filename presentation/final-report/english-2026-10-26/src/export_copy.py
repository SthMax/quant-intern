from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,re
from english_copy import *
R=Path(__file__).resolve().parent.parent;SOURCE=R.parent/'color-revision-2026-10-26/output/asset-management-llm-story-colors.pptx'
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
REFS={'FUND-354':'Application design and implementation','FUND-356':'Research template; data as of May 2026','FUND-351':'Digital finance applications','FUND-160':'Internal knowledge services','FUND-103':'Intelligent service platform','FUND-254':'Quantitative team coding support','FUND-215':'Bulk document revision','FUND-227':'Example 1, steps S1–S4 and report generation'}
def references(note):
 if '来源：' not in note:return ''
 lines=note.split('来源：',1)[1].splitlines();out=['Sources:']
 for s in lines:
  if not s.strip():continue
  if s.startswith('http'):out.append(s);continue
  ids=re.findall(r'FUND-\d+|CN\d+A',s)
  if ids:
   loc=re.search(r'PDF第([0-9–、]+)页',s);tail='pp. '+loc.group(1).replace('、',', ') if loc else REFS.get(ids[0],'Source text')
   out.append(' / '.join(ids)+', '+tail)
  elif '盈米' in s:out.append('Yingmi official release and API client')
 return '\n'.join(out)
manifest=[];md=['# English copy: LLMs in Asset Management','','33 slides. Office labels: Front office / Middle office / Back office. Stages: Workflow / Peer practices / Proposed approach. Running examples: Company A / Client update.','','All economic values follow the Chinese source. Financial comparisons use prior/current quarter, not year-on-year.']
with ZipFile(SOURCE) as z:
 for i in range(1,34):
  x=E.fromstring(z.read(f'ppt/slides/slide{i}.xml'));strings=[]
  for s in x.findall('.//p:sp',N):
   name=s.find('./p:nvSpPr/p:cNvPr',N).get('name');old='\n'.join(s.xpath('./p:txBody/a:p//a:t/text()',namespaces=N))
   if not old:continue
   new=text_for(i,name,old);strings.append({'name':name,'source':old,'english':new})
  original_note='\n'.join(E.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml')).xpath('.//a:t/text()',namespaces=N));refs=references(original_note)
  notes=NOTES[i]+('\n\n'+refs if refs else '')
  manifest.append({'page':i,'title':TITLES[i],'shapes':strings,'table':TABLE11 if i==11 else None,'notes':notes,'original_notes':original_note})
  md += [f'\n## {i:02d}. {TITLES[i]}','',next((t['english'] for t in strings if t['name']=='!!subtitle'),''),'','### Slide copy','']
  for t in strings:
   if t['name'].startswith(('!!nav.','!!task.','!!map.','!!heading','!!subtitle','!!page','!!example','!!source','!!story.header.')):continue
   md.append('- '+t['english'].replace('\n',' / '))
  if i==11:md+=['','| Bond / maturity | Held face value (RMB m) | Clean price per RMB100 face value | Available face value (RMB m) |','|---|---:|---:|---:|','| Bond A / 1.2 years | 20 | 100.20 | 20 |']
  md+=['','### Speaker notes','',notes,'']
(R/'src/english-manifest.json').write_text(json.dumps({'slide_count':33,'font':'Arial','slides':manifest},ensure_ascii=False,indent=2))
(R/'ENGLISH-COPY.md').write_text('\n'.join(md).rstrip()+'\n')
print('Saved all 33 slides and speaker notes to ENGLISH-COPY.md')
