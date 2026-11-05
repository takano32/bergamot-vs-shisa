#!/usr/bin/env python3
"""判定役が書いた点（id、label、acc、nat、pen、why の jsonl）と results/llm_key.json を結び、results/llm_judge.jsonl を作る。
  python3 scripts/join_judge.py <判定の jsonl>
検査: 500行そろっているか、点の範囲（acc 1〜5、nat 1〜5、pen は 0 か -1）。total = acc + nat + pen。
"""
import json, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SYSTEMS = ["bergamot", "shisa", "shisa_strict", "cat08", "cat14"]
key = json.loads((REPO / "results/llm_key.json").read_text(encoding="utf-8"))["key"]
sents = {r["id"]: r for r in map(json.loads, open(REPO / "data/sentences.jsonl", encoding="utf-8"))}
got = {}
for line in open(sys.argv[1], encoding="utf-8"):
    if not line.strip():
        continue
    j = json.loads(line)
    k = (j["id"], j["label"])
    assert k not in got, f"重複 {k}"
    assert 1 <= j["acc"] <= 5 and 1 <= j["nat"] <= 5 and j["pen"] in (0, -1), j
    got[k] = j
missing = [(i, l) for i in sents for l in "ABCDE" if (i, l) not in got]
assert not missing, f"足りない {len(missing)} 行: {missing[:10]}"
rows = []
for i in sorted(sents):
    s = sents[i]
    for lab in "ABCDE":
        j = got[(i, lab)]
        rows.append({"id": i, "system": key[str(i)][lab], "label": lab, "src_lang": s["src_lang"], "tgt_lang": s["tgt_lang"],
                     "category": s["category"], "acc": j["acc"], "nat": j["nat"], "pen": j["pen"], "total": j["acc"] + j["nat"] + j["pen"], "why": j["why"]})
rows.sort(key=lambda r: (SYSTEMS.index(r["system"]), r["id"]))
with open(REPO / "results/llm_judge.jsonl", "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote results/llm_judge.jsonl", len(rows))
