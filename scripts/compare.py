#!/usr/bin/env python3
"""5系の訳を並べて results/compare.md に書く。"""
import json
from pathlib import Path
root = Path(__file__).resolve().parent.parent
SYS = [("bergamot", "Firefox 翻訳"), ("shisa", "Shisa 350M"), ("shisa_strict", "Shisa 350M（厳しい指示文）"), ("cat08", "CAT 0.8B"), ("cat14", "CAT 1.4B")]
load = lambda n: {r["id"]: r for r in map(json.loads, open(root / "results" / f"{n}.jsonl", encoding="utf-8"))}
d = {n: load(n) for n, _ in SYS}
sents = [json.loads(l) for l in open(root / "data/sentences.jsonl", encoding="utf-8")]
esc = lambda t: t.replace("|", "\\|").replace("\n", " ⏎ ")
lines = ["# 5系の訳の並び（100文）", "", "| id | 向き | 分野 | タグ | 原文 | " + " | ".join(n for _, n in SYS) + " |", "|---|---|---|---|---|" + "---|" * len(SYS)]
for r in sents:
    lines.append(f"| {r['id']} | {r['src_lang']}→{r['tgt_lang']} | {r['category']} | {' '.join(r['tags'])} | {esc(r['src'])} | " + " | ".join(esc(d[k][r["id"]]["hyp"]) for k, _ in SYS) + " |")
(root / "results/compare.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(len(sents), "rows")
