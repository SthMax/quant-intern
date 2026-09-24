#!/usr/bin/env bash
set -euo pipefail
REPORT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
TASK_RUNTIME="${CODEX_WORKSPACE_RUNTIME:-$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies}"
"$TASK_RUNTIME/node/bin/node" "$REPORT_DIR/build.mjs"
"$TASK_RUNTIME/python/bin/python3" "$REPORT_DIR/finalize.py"
