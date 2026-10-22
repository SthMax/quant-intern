#!/usr/bin/env bash
set -euo pipefail

report_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
runtime_dir="${FINAL_REPORT_RUNTIME:-/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies}"
report_node="$runtime_dir/node/bin/node"
report_python="$runtime_dir/python/bin/python3"
report_tools="$runtime_dir/bin/override"
mkdir -p "$report_dir/build" "$report_dir/output" "$report_dir/qa/pdf-render"
if [[ ! -e "$report_dir/node_modules" ]]; then
  ln -s "$runtime_dir/node/node_modules" "$report_dir/node_modules"
fi

"$report_python" "$report_dir/prepare_content.py"
"$report_python" "$report_dir/apply_editorial.py"
"$report_node" "$report_dir/build.mjs"

previous_dir="$report_dir/build/previous-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$previous_dir"
for previous_file in "$report_dir/output/final-report-2026-10-20.pptx" "$report_dir/output/final-report-2026-10-20.pdf" "$report_dir/qa/finalizer.json"; do
  if [[ -f "$previous_file" ]]; then mv "$previous_file" "$previous_dir/"; fi
done
"$report_node" "$report_dir/finalize.mjs" > "$report_dir/build/finalizer.log"

# The bundled headless converter needs explicit access to macOS CJK fonts.
"$report_python" - "$report_dir" <<'PY'
from pathlib import Path
from xml.sax.saxutils import escape
import sys
root = Path(sys.argv[1])
font = next(Path('/System/Library/AssetsV2').glob('com_apple_MobileAsset_Font*/*.asset/AssetData/PingFang.ttc'), None)
if font is None:
    raise SystemExit('PingFang.ttc is required for this presentation.')
cache = root / 'build/fontconfig-cache'
cache.mkdir(exist_ok=True)
directories = ['/System/Library/Fonts', '/Library/Fonts', str(font.parent)]
xml = '<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd"><fontconfig>'
xml += ''.join('<dir>' + escape(value) + '</dir>' for value in directories)
xml += '<cachedir>' + escape(str(cache)) + '</cachedir></fontconfig>'
(root / 'build/fonts.conf').write_text(xml)
PY
FONTCONFIG_FILE="$report_dir/build/fonts.conf" "$report_tools/soffice" --headless --convert-to pdf --outdir "$report_dir/output" "$report_dir/output/final-report-2026-10-20.pptx"
"$report_python" "$report_dir/finalize_pdf.py"
"$report_tools/pdftoppm" -scale-to 1280 -png "$report_dir/output/final-report-2026-10-20.pdf" "$report_dir/qa/pdf-render/page"
"$report_python" "$report_dir/verify.py"
