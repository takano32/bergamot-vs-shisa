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
- Shisa 側の指示文は2種類（`scripts/run_shisa.mjs` の `prompt`。`SHISA_PROMPT=strict` で厳しい版）。厳しい版は `results/shisa_strict.jsonl`。

## 気づいたこと（機械で数えたもの。訳の良し悪しの採点ではない）

30文のうち、訳のあとに注釈や余計な文が付いた出力は Firefox 翻訳モデルが0、Shisa 350M が6（指示文が基本のとき）、16（厳しい指示文のとき）。訳す向きを取り違えた（日→英の指示で日本語を返した等）出力は、前から順に0、2、3。厳しい指示文で「注釈をつけるな」と書いたのに、その文言を注釈の中で繰り返す出力が出ており、350M にとって指示文を厳しくしても直らなかった。実装に使うなら、出力を最初の1行で切る、向きを後で検査する、などの後処理が要る。

## 現状と未了

- 済み: 両方向のモデルがある（en-ja、ja-en）ことの確認、30文の両側の出力（Shisa は指示文2種類）、ヘッドレス Chrome で CPU の WASM 実行（約2〜4秒/文）。
- 未了: 自動採点（LLM 判定や COMET）はしていない。指示文を変えた Shisa の再試行、文数を増やすこと、WebGPU のある環境での速度は試していない。
