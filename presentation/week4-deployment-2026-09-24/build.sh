#!/usr/bin/env bash
set -euo pipefail
DECK_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$DECK_DIR"
python3 prepare.py
export PATH="/Library/TeX/texbin:$PATH"
mkdir -p build output
latexmk -norc -xelatex -interaction=nonstopmode -halt-on-error -synctex=1 -outdir=build main.tex > build/latexmk.log 2>&1
cp build/main.pdf output/week4-deployment-options.pdf
