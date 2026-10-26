from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,hashlib
R=Path(__file__).resolve().parent.parent
source=R.parent/'interactive-full-revised-2026-10-26/output/asset-management-llm-interactive-revised.pptx'
final=R/'output/asset-management-llm-slide11-corrected.pptx'
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','m':'http://schemas.microsoft.com/office/powerpoint/2015/09/main'}
with ZipFile(source) as a,ZipFile(final) as b:
 assert a.namelist()==b.namelist()
 changed=[p for p in a.namelist() if a.read(p)!=b.read(p)]
 assert set(changed)=={'ppt/slides/slide11.xml','ppt/notesSlides/notesSlide11.xml'}
 links=0;morphs=0
 for i in range(1,34):
  name=f'ppt/slides/slide{i}.xml';x=E.fromstring(a.read(name));y=E.fromstring(b.read(name))
  if i!=11:assert a.read(name)==b.read(name)
  for expr in ['.//p:timing','.//m:morph','.//a:hlinkClick','.//p:spPr']:
   ax=[E.tostring(e,method='c14n') for e in x.findall(expr,N)];bx=[E.tostring(e,method='c14n') for e in y.findall(expr,N)];assert ax==bx,(i,expr)
  links+=len(y.findall('.//a:hlinkClick',N));morphs+=len(y.findall('.//m:morph',N))
 text='\n'.join(E.fromstring(b.read('ppt/slides/slide11.xml')).xpath('.//a:t/text()',namespaces=N))
 note='\n'.join(E.fromstring(b.read('ppt/notesSlides/notesSlide11.xml')).xpath('.//a:t/text()',namespaces=N))
 assert 'LLM解析询价记录' in text and '交易员提供收到的报价' in text
 assert '记录出处与报价时间' in text
 assert '交易员先向交易对手询价' in note and '交易员提供的记录' in note
 assert 'LLM读取对手聊天' not in text
 assert '净价（元/百元面值）' in text and '持仓面额（万元）' in text
report={'final_path':str(final),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'final_sha256':hashlib.sha256(final.read_bytes()).hexdigest(),'final_equals_candidate':final.read_bytes()==(R/'build/candidate.pptx').read_bytes(),'changed_package_parts':changed,'other_32_slide_xml_identical':True,'other_32_notes_identical':True,'all_shape_geometry_and_style_unchanged':True,'all_links_and_animations_unchanged':True,'slide_count':33,'native_links':links,'morphs':morphs,'navigation_color_proposal_applied':False,'source_patch_applied':False}
(R/'build/qa/final-scope-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
(R/'build/qa/slide11-final-text.txt').write_text(text+'\n\n讲者备注\n'+note)
print(json.dumps(report,ensure_ascii=False))
