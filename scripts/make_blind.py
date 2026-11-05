#!/usr/bin/env python3
"""LLM 判定の匿名入力を作る。文ごとに5系の並びを乱数で入れ替えて A〜E の名前を付け、
  - 判定役が読む入力（系の名前なし）を第1引数のパスに書く
  - 対応表（id と label から系を引く）を results/llm_key.json に書く
判定役は、判定を書き終えるまで llm_key.json を開かない。
  python3 scripts/make_blind.py <入力ファイルの出力先> [seed]
"""
import json, random, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SYSTEMS = ["bergamot", "shisa", "shisa_strict", "cat08", "cat14"]
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20261107
rng = random.Random(seed)
sents = [json.loads(l) for l in open(REPO / "data/sentences.jsonl", encoding="utf-8")]
hyps = {s: {r["id"]: r["hyp"] for r in map(json.loads, open(REPO / f"results/{s}.jsonl", encoding="utf-8"))} for s in SYSTEMS}
key, lines = {}, []
for r in sents:
    order = SYSTEMS[:]
    rng.shuffle(order)
    key[str(r["id"])] = {lab: sysname for lab, sysname in zip("ABCDE", order)}
    tgt = {"ja": "日本語", "en": "英語"}[r["tgt_lang"]]
    lines.append(f"### {r['id']}  （{r['src_lang']}→{r['tgt_lang']}、目標は{tgt}）")
    lines.append(f"原文: {r['src']}")
    for lab, sysname in zip("ABCDE", order):
        h = hyps[sysname][r["id"]].strip().replace("\n", " ⏎ ")
        lines.append(f"{lab}: {h}")
    lines.append("")
Path(sys.argv[1]).write_text("\n".join(lines), encoding="utf-8")
(REPO / "results/llm_key.json").write_text(json.dumps({"seed": seed, "key": key}, ensure_ascii=False, indent=0), encoding="utf-8")
print("wrote", sys.argv[1], "and results/llm_key.json (seed", seed, ")")
