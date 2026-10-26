from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from xml.sax.saxutils import escape
import re,json,hashlib,difflib
R=Path(__file__).resolve().parent.parent
SOURCE=R.parent/'interactive-full-revised-2026-10-26/output/asset-management-llm-interactive-revised.pptx'
CANDIDATE=R/'build/candidate.pptx'
EXPECTED='787e009658422ca50e93744c892c3266e216cde805977ec795b0ffe040d34eb3'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED,'Source file changed'
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
with ZipFile(SOURCE) as z:
 entries=z.infolist();contents={e.filename:z.read(e.filename) for e in entries}
before=dict(contents)
changes={
 '!!trade.llm.quote.role':['LLM解析询价记录'],
 '!!trade.llm.quote.body':['交易员提供收到的报价：','“甲A卖方净价100.20，','面额2000万元可出”','提取券名、净价与面额'],
 '!!trade.user':['交易员核对记录出处与报价时间，经理据此讨论后续安排']
}
slide=contents['ppt/slides/slide11.xml'].decode();slide_original=slide;edits=[]
for name,paragraphs in changes.items():
 pos=slide.index('name="'+name+'"');a=slide.rfind('<p:sp>',0,pos);b=slide.index('</p:sp>',pos)+len('</p:sp>');old=slide[a:b]
 matches=list(re.finditer(r'<a:p(?:\s[^>]*)?>.*?</a:p>',old,re.S));assert matches,name
 oldtext=E.fromstring(old.encode()).xpath('.//a:t/text()',namespaces=N) if False else re.findall(r'<a:t>(.*?)</a:t>',old,re.S)
 template=matches[0].group();assert len(re.findall(r'<a:t>.*?</a:t>',template,re.S))==1
 newpars=''.join(re.sub(r'<a:t>.*?</a:t>',lambda _: '<a:t>'+escape(t)+'</a:t>',template,count=1,flags=re.S) for t in paragraphs)
 new=old[:matches[0].start()]+newpars+old[matches[-1].end():]
 slide=slide[:a]+new+slide[b:]
 edits.append({'shape':name,'before':oldtext,'after':paragraphs,'old_xml':old,'new_xml':new})
contents['ppt/slides/slide11.xml']=slide.encode()
check=slide
for e in reversed(edits):check=check.replace(e['new_xml'],e['old_xml'],1)
assert check==slide_original,'Unrelated slide bytes changed'
notes=contents['ppt/notesSlides/notesSlide11.xml'].decode();old_note=E.fromstring(notes.encode()).xpath('.//a:t/text()',namespaces=N)[0]
new_note='沿用经理拟买入甲公司两年内到期债券、查询持仓并汇总卖方报价的要求。LLM提取主体、到期期限和所需数据，调用业务查询。系统执行查询并返回候选券、期限和已有持仓。交易员先向交易对手询价，随后提供收到的报价消息或询价沟通记录。LLM解析交易员提供的记录，提取券名、卖方净价和可出面额，再与系统返回的候选券及持仓按券名整理在一起。演示中甲公司债A剩余1.2年，持仓面额2000万元，卖方净价为每百元面值100.20元，可出面额2000万元。全部数值为演示。交易员核对记录出处、报价时间与金额，经理根据同一份资料讨论后续安排。方案参考南方自然语言查询及兴证全球交易语料解析的做法。'
assert notes.count('<a:t>'+escape(old_note)+'</a:t>')==1
notes=notes.replace('<a:t>'+escape(old_note)+'</a:t>','<a:t>'+escape(new_note)+'</a:t>',1)
contents['ppt/notesSlides/notesSlide11.xml']=notes.encode()
assert notes.replace(escape(new_note),escape(old_note),1).encode()==before['ppt/notesSlides/notesSlide11.xml']
with ZipFile(CANDIDATE,'w') as z:
 for e in entries:z.writestr(e,contents[e.filename])
changed=[p for p in contents if contents[p]!=before[p]]
assert changed==['ppt/slides/slide11.xml','ppt/notesSlides/notesSlide11.xml'] or set(changed)=={'ppt/slides/slide11.xml','ppt/notesSlides/notesSlide11.xml'}
# Preserve a minimal source patch without modifying the committed source directory.
source_root=R.parent/'interactive-full-revised-2026-10-26'
source_changes={}
p=source_root/'src/revision-slides.mjs';old=p.read_text();new=old
old_expr="task('trade.llm.quote','LLM读取对手聊天','“甲A卖方净价100.20，\\n面额2000万元可出”\\n提取券名、净价与面额'"
new_expr="task('trade.llm.quote','LLM解析询价记录','交易员提供收到的报价：\\n“甲A卖方净价100.20，\\n面额2000万元可出”\\n提取券名、净价与面额'"
assert new.count(old_expr)==1
new=new.replace(old_expr,new_expr).replace("take('trade.user','交易员核对原话与报价时间，经理据此讨论后续安排'","take('trade.user','交易员核对记录出处与报价时间，经理据此讨论后续安排'",1)
source_changes[str(p.relative_to(R.parents[2]))]=(old,new)
p=source_root/'src/content.mjs';old=p.read_text();assert old_note in old;new=old.replace(old_note,new_note,1);source_changes[str(p.relative_to(R.parents[2]))]=(old,new)
patch=''.join(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='a/'+p,tofile='b/'+p)) for p,(a,b) in source_changes.items())
(R/'src/source-slide11.patch').write_text(patch)
public_edits=[{k:v for k,v in e.items() if not k.endswith('_xml')} for e in edits]
(R/'src/slide11-edit.json').write_text(json.dumps({'source':str(SOURCE),'source_sha256':EXPECTED,'page':11,'visible_edits':public_edits,'notes_before':old_note,'notes_after':new_note,'sources_preserved':True,'source_patch_applied':False},ensure_ascii=False,indent=2))
report={'source_sha256':EXPECTED,'candidate_sha256':hashlib.sha256(CANDIDATE.read_bytes()).hexdigest(),'changed_package_parts':changed,'other_32_slide_xml_byte_identical':True,'other_32_notes_xml_byte_identical':True,'all_relationships_theme_media_masters_unchanged':True,'slide11_outside_three_text_frames_byte_identical':True,'slide11_transitions_and_animations_unchanged':True}
(R/'build/qa/change-scope.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False))
