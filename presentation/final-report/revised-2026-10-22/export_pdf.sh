#!/usr/bin/env bash
set -euo pipefail
report_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
runtime_dir="/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies"
"$runtime_dir/python/bin/python3" - "$report_dir" <<'PY'
from pathlib import Path
from xml.sax.saxutils import escape
import sys
root=Path(sys.argv[1]);cache=root/'build/fontconfig-cache';cache.mkdir(exist_ok=True)
font=next(Path('/System/Library/AssetsV2').glob('com_apple_MobileAsset_Font*/*.asset/AssetData/PingFang.ttc'))
xml='<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd"><fontconfig>'
xml+=''.join('<dir>'+escape(p)+'</dir>' for p in ['/System/Library/Fonts','/Library/Fonts',str(font.parent)])
xml+='<cachedir>'+escape(str(cache))+'</cachedir></fontconfig>'
(root/'build/fonts.conf').write_text(xml)
PY
FONTCONFIG_FILE="$report_dir/build/fonts.conf" "$runtime_dir/bin/override/soffice" --headless --convert-to pdf --outdir "$report_dir/output" "$report_dir/output/final-report-2026-10-22.pptx"
"$runtime_dir/python/bin/python3" - "$report_dir" <<'PY'
from pypdf import PdfReader,PdfWriter
from pathlib import Path
import sys
root=Path(sys.argv[1]);p=root/'output/final-report-2026-10-22.pdf'
w=PdfWriter();w.clone_document_from_reader(PdfReader(p));w.add_metadata({'/Title':'LLM在公募基金工作中的应用','/Author':'Intern','/Subject':'2026年10月22日，32页正文与6页备查，16:9'})
temporary=root/'build/pdf-metadata.pdf'
with temporary.open('wb') as f:w.write(f)
temporary.replace(p)
PY
mkdir -p "$report_dir/qa/pdf-render"
"$runtime_dir/bin/override/pdftoppm" -scale-to 1600 -png "$report_dir/output/final-report-2026-10-22.pdf" "$report_dir/qa/pdf-render/page"
