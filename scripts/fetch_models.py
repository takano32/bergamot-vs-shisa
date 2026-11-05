#!/usr/bin/env python3
"""Mozilla Remote Settings から Firefox 翻訳モデル(en-ja, ja-en)を models/ に取り出す。
fxtranslate 自身の取得は箱の TLS で失敗するため、標準ライブラリ + zstd CLI で自前取得する。"""
import hashlib, json, subprocess, sys, urllib.request
from pathlib import Path

API = "https://firefox.settings.services.mozilla.com/v1/buckets/main/collections/translations-models-v2/records"
CDN = "https://firefox-settings-attachments.cdn.mozilla.net/"
OUT = Path(__file__).resolve().parent.parent / "models"
PAIRS = [("en", "ja"), ("ja", "en")]

records = json.load(urllib.request.urlopen(API))["data"]
for s, t in PAIRS:
    cand = [r for r in records if r.get("sourceLanguage") == s and r.get("targetLanguage") == t
            and r["fileType"] in ("model", "vocab", "srcvocab", "trgvocab")]
    # 各 fileType で最新の version を採る
    best = {}
    for r in cand:
        k = r["fileType"]
        if k not in best or tuple(map(float, r["version"].split("."))) > tuple(map(float, best[k]["version"].split("."))):
            best[k] = r
    d = OUT / f"{s}-{t}"
    d.mkdir(parents=True, exist_ok=True)
    for r in best.values():
        dest = d / r["name"]
        if dest.exists():
            continue
        a = r["attachment"]
        blob = urllib.request.urlopen(CDN + a["location"]).read()
        assert hashlib.sha256(blob).hexdigest() == a["hash"], r["name"]
        raw = subprocess.run(["zstd", "-dc"], input=blob, capture_output=True, check=True).stdout
        dest.write_bytes(raw)
        print(s, t, r["name"], r["version"], len(raw))
