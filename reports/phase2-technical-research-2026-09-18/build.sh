#!/usr/bin/env bash
set -euo pipefail
REPORT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPORT_DIR"
if command -v latexmk >/dev/null 2>&1; then
  REPORT_LATEXMK="$(command -v latexmk)"
elif [[ -x /Library/TeX/texbin/latexmk ]]; then
  REPORT_LATEXMK=/Library/TeX/texbin/latexmk
  export PATH="/Library/TeX/texbin:$PATH"
else
  echo 'latexmk with XeLaTeX is required.' >&2
  exit 1
fi
mkdir -p build
"$REPORT_LATEXMK" -norc -xelatex -interaction=nonstopmode -halt-on-error -synctex=1 -outdir=build main.tex
cp build/main.pdf report.pdf
