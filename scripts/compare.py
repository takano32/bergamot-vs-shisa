#!/usr/bin/env python3
"""results/bergamot.jsonl と results/shisa.jsonl を並べて results/compare.md に書く。"""
import json
from pathlib import Path
root = Path(__file__).resolve().parent.parent
load = lambda n: {r["id"]: r for r in map(json.loads, open(root/"results"/n))}
b, s = load("bergamot.jsonl"), load("shisa.jsonl")
st = load("shisa_strict.jsonl") if (root/"results/shisa_strict.jsonl").exists() else {}
esc = lambda t: t.replace("|", "\\|").replace("\n", " ⏎ ")
lines = ["# Firefox 翻訳モデル（Bergamot と同じモデル）と Shisa 350M の訳の並び", "",
         "| id | 向き | 種類 | 原文 | Firefox 翻訳モデル | Shisa 350M | Shisa 350M（厳しい指示文） |", "|---|---|---|---|---|---|---|"]
for i in sorted(b):
    r = b[i]
    lines.append(f"| {i} | {r['src_lang']}→{r['tgt_lang']} | {r['category']} | {esc(r['src'])} | {esc(r['hyp'])} | {esc(s[i]['hyp']) if i in s else ''} | {esc(st[i]['hyp']) if i in st else ''} |")
(root/"results/compare.md").write_text("\n".join(lines) + "\n")
print(len(b), "rows")
