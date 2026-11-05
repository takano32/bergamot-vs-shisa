#!/usr/bin/env python3
"""results/ の訳を機械で数える（訳の良し悪しの採点ではない）。

- 注釈のある出力: 空でない行が2行以上ある文の数。
- 向きの取り違え: 目標が英語なのに最初の空でない行に日本語の字（ひらがな、カタカナ、漢字）がある、
  または目標が日本語なのに最初の行に日本語の字が無い。注釈の中の日本語は数えない。

使い方:
  python3 scripts/count_flags.py bergamot shisa shisa_strict cat08 cat14
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JA = re.compile(r"[぀-ヿ一-鿿]")


def main(names):
    sents = {r["id"]: r for r in map(json.loads, open(REPO / "data/sentences.jsonl", encoding="utf-8"))}
    for name in names:
        rows = {r["id"]: r for r in map(json.loads, open(REPO / "results" / f"{name}.jsonl", encoding="utf-8"))}
        multi, wrong = 0, []
        for i in sorted(sents):
            lines = [l for l in rows[i]["hyp"].splitlines() if l.strip()]
            if len(lines) > 1:
                multi += 1
            first = lines[0] if lines else ""
            tgt = sents[i]["tgt_lang"]
            has_ja = bool(JA.search(first))
            if (tgt == "en" and has_ja) or (tgt == "ja" and not has_ja):
                wrong.append(i)
        print(f"{name}: 注釈のある文 {multi}、向きの取り違え {len(wrong)}（文 {wrong}）")


if __name__ == "__main__":
    main(sys.argv[1:])
