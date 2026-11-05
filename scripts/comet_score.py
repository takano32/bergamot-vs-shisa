#!/usr/bin/env python3
"""results/ の訳を COMET の QE モデルで採点し、results/comet.jsonl に書く（1行＝1文・1系）。

- モデル: Unbabel/wmt20-comet-qe-da（Apache-2.0、Hugging Face で gated ではない）。
  正解訳を使わず、原文と訳だけで採点する（reference-less）。
  wmt22-cometkiwi-da は gated（利用条件の同意とトークンが要る）ので使わない。
- 計算: CPU のみ（predict の gpus=0）。モデルの重みはリポの .cache/huggingface に置く（.gitignore 済み）。
- 2種類の点を出す:
  comet_qe           … 結果ファイルの訳をそのまま採点（Shisa の注釈や余計な文も入る）
  comet_qe_first_line … 最初の空でない行だけを採点（注釈を切った訳の部分だけの点。診断用）

使い方:
  .venv/bin/python scripts/comet_score.py --check   # 読み込みと、良い訳と悪い訳の2文の動作確認
  .venv/bin/python scripts/comet_score.py          # results/comet.jsonl を作る（全部の系）
  .venv/bin/python scripts/comet_score.py --systems cat08 cat14
                                                    # 指定した系だけ採点し直し、ほかの系の既存の行は残す
"""
import argparse
import functools
import json
import os
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# モデルの重みはリポ内の .cache/huggingface に置く（.gitignore の .cache/ に入る）。
os.environ.setdefault("HF_HOME", str(REPO / ".cache" / "huggingface"))

# unbabel-comet 2.2.7 の comet/models/lru_cache.py は functools._HashedSeq を import するが、
# Python 3.14 の functools には無い。CPython 3.13 までと同じ定義を差し込んで、COMET 側のファイルには触らない。
if not hasattr(functools, "_HashedSeq"):
    class _HashedSeq(list):
        __slots__ = ("hashvalue",)

        def __init__(self, tup, hash=hash):
            self[:] = tup
            self.hashvalue = hash(tup)

        def __hash__(self):
            return self.hashvalue

    functools._HashedSeq = _HashedSeq

from comet import download_model, load_from_checkpoint  # noqa: E402

MODEL = "Unbabel/wmt20-comet-qe-da"
SYSTEMS = ["bergamot", "shisa", "shisa_strict", "cat08", "cat14"]


def first_line(text):
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return text.strip()


def score(model, pairs, batch_size):
    """pairs: [(src, mt)] -> [float]。同じ組は1回だけ計算する。"""
    uniq = list(dict.fromkeys(pairs))
    data = [{"src": s, "mt": m} for s, m in uniq]
    out = model.predict(data, batch_size=batch_size, gpus=0, progress_bar=False)
    table = dict(zip(uniq, out.scores))
    return [table[p] for p in pairs]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-size", type=int, default=8)
    ap.add_argument("--out", default=str(REPO / "results" / "comet.jsonl"))
    ap.add_argument("--check", action="store_true", help="読み込みと2文の動作確認だけ")
    ap.add_argument("--systems", nargs="+", choices=SYSTEMS, help="採点する系（既定は全部）。ほかの系の既存の行は --out に残す")
    args = ap.parse_args()
    targets = args.systems or SYSTEMS

    t0 = time.time()
    ckpt = download_model(MODEL)
    print(f"checkpoint: {ckpt} ({time.time() - t0:.0f}s)", file=sys.stderr)
    model = load_from_checkpoint(ckpt)
    print(f"loaded ({time.time() - t0:.0f}s)", file=sys.stderr)

    if args.check:
        pairs = [
            ("The cat is sitting on the mat.", "猫がマットの上に座っている。"),
            ("The cat is sitting on the mat.", "明日の株価は下がるでしょう。"),
        ]
        for (s, m), sc in zip(pairs, score(model, pairs, 2)):
            print(f"{sc:.4f}  {s} | {m}", file=sys.stderr)
        return

    sents = [json.loads(line) for line in open(REPO / "data" / "sentences.jsonl", encoding="utf-8")]
    hyps = {
        name: {r["id"]: r for r in map(json.loads, open(REPO / "results" / f"{name}.jsonl", encoding="utf-8"))}
        for name in targets
    }

    raw_pairs, fl_pairs, keys = [], [], []
    for name in targets:
        for s in sents:
            h = hyps[name][s["id"]]["hyp"]
            raw_pairs.append((s["src"], h))
            fl_pairs.append((s["src"], first_line(h)))
            keys.append((s["id"], name))

    raw = score(model, raw_pairs, args.batch_size)
    fl = score(model, fl_pairs, args.batch_size)
    print(f"scored {len(raw)} pairs ({time.time() - t0:.0f}s)", file=sys.stderr)

    meta = {s["id"]: s for s in sents}
    new_rows = {}
    for (i, name), r, x in zip(keys, raw, fl):
        m = meta[i]
        new_rows[(i, name)] = {
            "id": i,
            "system": name,
            "src_lang": m["src_lang"],
            "tgt_lang": m["tgt_lang"],
            "category": m["category"],
            "comet_qe": round(float(r), 6),
            "comet_qe_first_line": round(float(x), 6),
        }
    # 採点しなかった系の行は既存の --out から読んで残す（--systems のとき）。
    kept = {}
    if args.systems and Path(args.out).exists():
        for line in open(args.out, encoding="utf-8"):
            row = json.loads(line)
            if row["system"] not in targets:
                kept[(row["id"], row["system"])] = row
    with open(args.out, "w", encoding="utf-8") as f:
        for name in SYSTEMS:  # 系の順番は SYSTEMS の順、文の順番は sentences.jsonl の順
            for s in sents:
                key = (s["id"], name)
                row = new_rows.get(key) or kept.get(key)
                if row is not None:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
