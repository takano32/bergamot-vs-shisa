#!/usr/bin/env bash
# 5系の訳を順に作る（2コアなので並列にしない）。ログは第1引数のディレクトリへ。
set -u
LOG=${1:-/tmp}
cd "$(dirname "$0")/.."
ts() { date +%H:%M:%S; }
echo "$(ts) bergamot"; .venv/bin/python scripts/run_bergamot.py > "$LOG/bergamot.log" 2>&1
echo "$(ts) shisa"; node scripts/run_shisa.mjs "" results/shisa.jsonl > "$LOG/shisa.log" 2>&1
echo "$(ts) shisa_strict"; SHISA_PROMPT=strict node scripts/run_shisa.mjs "" results/shisa_strict.jsonl > "$LOG/shisa_strict.log" 2>&1
echo "$(ts) cat08"; PYODIDE_MODEL=hf-cat-translate-0.8b SHISA_PROMPT=card node scripts/run_shisa.mjs "" results/cat08.jsonl > "$LOG/cat08.log" 2>&1
echo "$(ts) cat14"; PYODIDE_MODEL=hf-cat-translate-1.4b SHISA_PROMPT=card node scripts/run_shisa.mjs "" results/cat14.jsonl > "$LOG/cat14.log" 2>&1
echo "$(ts) done"
