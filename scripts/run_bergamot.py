#!/usr/bin/env python3
"""Firefox 翻訳モデル（Bergamot と同じモデル）で data/sentences.jsonl を訳し results/bergamot.jsonl に書く。
実行は fxtranslate（Rust 製のエンジン）。モデルは scripts/fetch_models.py で models/ に置く。"""
import json, time
from pathlib import Path
from fxtranslate import Translator

root = Path(__file__).resolve().parent.parent
m = root / "models"
def load(src, tgt):
    d = m / f"{src}-{tgt}"
    if src == "en":
        return Translator(model=(d/"model.enja.intgemm.alphas.bin").read_bytes(), src_vocab=(d/"srcvocab.enja.spm").read_bytes(), trg_vocab=(d/"trgvocab.enja.spm").read_bytes())
    v = (d/"vocab.jaen.spm").read_bytes()
    return Translator(model=(d/"model.jaen.intgemm.alphas.bin").read_bytes(), src_vocab=v, trg_vocab=v)
tr = {("en","ja"): load("en","ja"), ("ja","en"): load("ja","en")}
(root/"results").mkdir(exist_ok=True)
with open(root/"data/sentences.jsonl") as f, open(root/"results/bergamot.jsonl","w") as out:
    for line in f:
        r = json.loads(line)
        t0 = time.time()
        r["hyp"] = tr[(r["src_lang"], r["tgt_lang"])].translate_long(r["src"])
        r["seconds"] = round(time.time()-t0, 3)
        out.write(json.dumps(r, ensure_ascii=False)+"\n")
        print(r["id"], r["hyp"])
