# bergamot-vs-shisa

Firefox 内蔵翻訳のモデル（Mozilla の Firefox Translations、エンジンは Bergamot 系）と、ブラウザの中で動く Shisa V2.1c LFM2 350M（[takano32/pyodide-llm](https://github.com/takano32/pyodide-llm) の既定モデル）に、同じ日英の文を通して訳を並べる実験。ブラウザ拡張で LLM 翻訳を作る前に、350M が内蔵翻訳の品質に届くかを見るための下調べ。

## 結果の見方

`results/compare.md` に30文の訳が並んでいる。人が目で見て比べる前提で、点数は付けていない。

- `data/sentences.jsonl`: 日→英 15本、英→日 15本。技術文、会話、Web 記事風を各5本ずつ。
- `results/bergamot.jsonl`: Firefox 翻訳モデルの訳。
- `results/shisa.jsonl`: Shisa 350M の訳（温度0の貪欲、seed 1、CPU の WASM。この箱に GPU は無い）。生の出力は `raw`、速度は `meta`。

## 再現

必要なもの: Python 3、Node.js、`zstd`、Google Chrome（`/usr/bin/google-chrome`、別の場所なら `SHISA_CHROME`）。

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
npm install
python3 scripts/fetch_models.py          # models/ に en-ja と ja-en のモデルを取り出す（リポには入れない）
.venv/bin/python scripts/run_bergamot.py # results/bergamot.jsonl
node scripts/run_shisa.mjs               # results/shisa.jsonl（公開サイトを開く。初回はモデル 379 MB を取って変換、約90秒）
python3 scripts/compare.py               # results/compare.md
```

## 注意

- 訳したエンジンは `fxtranslate`（Rust 製の実装）で、Firefox が使うのと同じモデルを読ませている。Firefox に載っている Bergamot の C++ 実装そのものではない。PyPI の `bergamot` は Python 3.10 までの wheel しかなかったので使っていない。
- `fxtranslate` 自身のモデル取得はこの箱の TLS で失敗した（証明書の署名エラー）。そこでモデルは `scripts/fetch_models.py` で Mozilla の Remote Settings から自前で取り、ハッシュを確かめて置いている。
- Shisa 側の指示文は英語の1種類だけ（`scripts/run_shisa.mjs` の `prompt`）。Shisa は指示文に敏感で、出力の揺れの一部は指示文のせいかもしれない。

## 現状と未了

- 済み: 両方向のモデルがある（en-ja、ja-en）ことの確認、30文の両側の出力。
- 未了: 自動採点（LLM 判定や COMET）はしていない。指示文を変えた Shisa の再試行、文数を増やすこと、WebGPU のある環境での速度は試していない。
