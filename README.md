# bergamot-vs-shisa

Firefox 内蔵翻訳のモデル（Mozilla の Firefox Translations、エンジンは Bergamot 系）と、ブラウザの中で動く Shisa V2.1c LFM2 350M（[takano32/pyodide-llm](https://github.com/takano32/pyodide-llm) の既定モデル）に、同じ日英の文を通して訳を並べる実験。ブラウザ拡張で LLM 翻訳を作る前に、350M が内蔵翻訳の品質に届くかを見るための下調べ。

## 結果の見方

- `results/scores.md`: 採点の結果（平均、文ごとの点、COMET と LLM 判定の食い違い、系どうしの差の目安）。まずここを見る。
- `results/compare.md`: 30文の訳が並んでいる。点は付けていない。
- `results/comet.jsonl`: COMET-QE の点（1行が1文・1系）。`comet_qe` は訳のまま、`comet_qe_first_line` は最初の空でない行だけ。
- `results/llm_judge.jsonl`: LLM 判定の点（正確さ、自然さ、注釈減点、総合）と一行の理由。`label` は判定時に付けた匿名ラベル（X、Y、Z）。

データと訳:

- `data/sentences.jsonl`: 日→英 15本、英→日 15本。技術文、会話、Web 記事風を各5本ずつ。
- `results/bergamot.jsonl`: Firefox 翻訳モデルの訳。
- `results/shisa.jsonl`: Shisa 350M の訳（温度0の貪欲、seed 1、CPU の WASM。この箱に GPU は無い）。生の出力は `raw`、速度は `meta`。
- `results/shisa_strict.jsonl`: Shisa 350M に厳しい指示文を与えた訳（`SHISA_PROMPT=strict`）。

## 採点の基準

### COMET-QE（機械による採点）

- モデルは `Unbabel/wmt20-comet-qe-da`（Apache-2.0、Hugging Face で gated ではない。[モデルカード](https://huggingface.co/Unbabel/wmt20-comet-qe-da)）。原文と訳だけを見る reference-less の QE で、正解訳は使わない。
- 本命の `Unbabel/wmt22-cometkiwi-da` は gated（利用条件への同意とトークンが要る）。この箱にはトークンが無いので、迂回はせず gated でない wmt20 版を使った。
- CPU で実行（`gpus=0`）。モデルカードには、スコアに上限が無く、ノイズも大きいと書いてある。絶対値より、系どうしの差を見る。
- 点は2種類。`comet_qe` は訳のまま、`comet_qe_first_line` は最初の空でない行だけで、注釈の影響を測るため。

### LLM 判定（Claude による読み）

- 判定役は Claude（Haiku 5.5）。原文と3つの訳を読んで、一文ずつ点を付けた。判定役が Claude なので、Claude の文体や訳語の好みが混ざる。
- 匿名化: 文ごとに3系の順番を乱数（seed 20261105）で入れ替え、X、Y、Z と名付けて読んだ。ただし注釈の付き方から系が推測できる文が多く、完全な匿名にはなっていない。
- 点の基準:
  - 正確さ（1〜5）: 5 誤り、抜け、足しが無い。4 小さな言い換えのずれ。3 重要な語の誤訳か、読みに響く抜けが1点。2 主要な意味が違う（否定、順序、取り違え、別の選択肢）。1 訳になっていない（向きの取り違え、答えや説明への置き換え）。
  - 自然さ（1〜5）: 5 そのまま使える。4 小さな不自然さが1点。3 不自然な語や文体が複数（場面に合わない文体を含む）。2 意味は取れるが破綻が目立つ。1 読めない。
  - 注釈減点（0 か -1）: 訳の後ろに注釈、解説、代替案、質問返し、指示文の漏れがあれば -1。内容が正しくても減点する。
  - 総合 = 正確さ + 自然さ + 注釈減点（2〜10）。
- 向きを取り違えた出力（日→英なのに日本語で返したなど）は、正確さも自然さも 1 にする。
- 判定は、COMET を動かして数字を見る前に全部書き終えた。

### 食い違いの定義

同じ文の2系の組で、LLM 総合の差が 2 点以上あるのに、COMET-QE の差の向きが逆のもの（COMET の同点は除く）。2 点は、正確さか自然さのどちらかで2段階の差がある程度の幅として、判定の前に決めた。

## COMET の入れ方（この箱の注意）

この箱は aarch64、Python 3.14、CPU のみ。次の3点で、普通の手順のままでは入らなかった。

- torch は CUDA 版ではなく CPU 版を指定する。PyPI の torch は nvidia 系の大きな依存を引く。
- unbabel-comet 2.2.7 は `numpy<2.0.0` を固定している（[PyPI の依存](https://pypi.org/pypi/unbabel-comet/json)）。一方、numpy 1.26.4 には Python 3.14 向けの wheel が無い（[PyPI の numpy 1.26.4](https://pypi.org/pypi/numpy/1.26.4/json) に cp314 のファイルが無い）。pip はこのため numpy をソースからビルドし始め、6分以上終わらなかったので止めた。そこで unbabel-comet は `--no-deps` で入れ、依存は numpy 2 系で揃えた。
- COMET 2.2.7 は `functools._HashedSeq` を import するが、Python 3.14 の functools には無い。`scripts/comet_score.py` の冒頭で、CPython 3.13 までと同じ定義を差し込んでいる。COMET のファイルは書き換えていない。

入れ方: `.venv/bin/pip install -r requirements-comet.txt` のあと、`.venv/bin/pip install --no-deps unbabel-comet==2.2.7`。版は `requirements-comet.txt` に全部書いてある。

## 再現

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
npm install
python3 scripts/fetch_models.py          # models/ に en-ja と ja-en のモデルを取り出す（リポには入れない）
.venv/bin/python scripts/run_bergamot.py # results/bergamot.jsonl
node scripts/run_shisa.mjs               # results/shisa.jsonl（公開サイトを開く。初回はモデル 379 MB を取って変換、約90秒）
python3 scripts/compare.py               # results/compare.md
.venv/bin/pip install -r requirements-comet.txt && .venv/bin/pip install --no-deps unbabel-comet==2.2.7
.venv/bin/python scripts/comet_score.py  # results/comet.jsonl（初回は COMET のモデル 2.3GB を .cache/huggingface に取る）
.venv/bin/python scripts/make_scores.py  # results/scores.md
```

必要なもの: Python 3、Node.js、`zstd`、Google Chrome（`/usr/bin/google-chrome`、別の場所なら `SHISA_CHROME`）。COMET の採点は CPU で約10分（この箱、他の作業と並行して）。

LLM 判定は、スクリプトで再現するものではない。`results/llm_judge.jsonl` の点と理由が、判定の記録そのもの。

## 結果

| 系 | COMET-QE（訳のまま） | COMET-QE（先頭行だけ） | LLM 正確さ | LLM 自然さ | LLM 注釈減点 | LLM 総合 |
|---|---|---|---|---|---|---|
| Firefox 翻訳 | 0.294 | 0.294 | 4.20 | 3.97 | 0.00 | 8.17 |
| Shisa 350M | 0.285 | 0.332 | 3.80 | 3.77 | -0.20 | 7.37 |
| Shisa 350M（厳しい指示文） | 0.138 | 0.361 | 3.97 | 3.70 | -0.53 | 7.13 |

- 方向別の LLM 総合: 英→日は Firefox 8.27、Shisa 8.07、厳しい版 8.00 でほぼ並ぶ。日→英は Firefox 8.07、Shisa 6.67、厳しい版 6.27 で差が出た。日→英の会話文（5本）では、Shisa の2本が日本語のまま返していて、この2本が差の大部分になっている。
- 種類別の LLM 総合: 技術文は Firefox 8.40、Shisa 7.30、厳しい版 7.80。会話は 7.30、6.70、6.50。Web 記事風は 8.80、8.10、7.10。
- 差の大きさ（文ごとの差の平均と、約95%の幅）: LLM の Firefox − Shisa は 0.80（−0.29〜1.89）、Firefox − 厳しい版は 1.03（−0.14〜2.21）。COMET-QE の Firefox − Shisa は 0.009（−0.084〜0.102）、Firefox − 厳しい版は 0.156（0.005〜0.307）。30文では、どの差も確かとは言えない。
- 注釈の影響: 厳しい版は注釈つきの文が16あり、先頭行だけにすると COMET-QE の点が平均 0.22 上がる。通常の Shisa は注釈が6文で、上がり幅は 0.05。
- COMET と LLM 判定の食い違いは13組。目立つ例は次の2つ。
  - 文25（日→英、会話）: Shisa は日本語の文を返した。COMET-QE はそれに 0.881 という、この文で最も高い点を付けた（Firefox は 0.316）。LLM 判定は Shisa 2 点、Firefox 9 点。COMET-QE は、訳の言語が合っているかをほとんど見ていないように見える。
  - 文3（英→日、技術文）: Firefox の訳は lazily を「簡潔に」と取り違えた（LLM 6 点）。COMET-QE はこれに 0.379 を付け、正しい訳の Shisa（0.248、LLM 9 点）より高くした。

## 注意

- 訳したエンジンは `fxtranslate`（Rust 製の実装）で、Firefox が使うのと同じモデルを読ませている。Firefox に載っている Bergamot の C++ 実装そのものではない。PyPI の `bergamot` は Python 3.10 までの wheel しかなかったので使っていない。
- `fxtranslate` 自身のモデル取得はこの箱の TLS で失敗した（証明書の署名エラー）。そこでモデルは `scripts/fetch_models.py` で Mozilla の Remote Settings から自前で取り、ハッシュを確かめて置いている。
- Shisa 側の指示文は2種類（`scripts/run_shisa.mjs` の `prompt`。`SHISA_PROMPT=strict` で厳しい版）。厳しい版は `results/shisa_strict.jsonl`。
- COMET-QE の点は、訳の言語が原文と同じでも、それらしい文なら高く出ることがある（文25）。向きの検査は別にやる必要がある。
- LLM 判定は Claude 自身の読みで、30文・1人の判定。判定役を変えれば点も変わる。

## 気づいたこと（機械で数えたもの。訳の良し悪しの採点ではない）

30文のうち、訳のあとに注釈や余計な文が付いた出力は Firefox 翻訳モデルが0、Shisa 350M が6（指示文が基本のとき）、16（厳しい指示文のとき）。訳す向きを取り違えた（日→英の指示で日本語を返した等）出力は、前から順に0、2、3。厳しい指示文で「注釈をつけるな」と書いたのに、その文言を注釈の中で繰り返す出力が出ており、350M にとって指示文を厳しくしても直らなかった。実装に使うなら、出力を最初の1行で切る、向きを後で検査する、などの後処理が要る。

## 現状と未了

- 済み: 両方向のモデルがある（en-ja、ja-en）ことの確認、30文の両側の出力（Shisa は指示文2種類）、ヘッドレス Chrome で CPU の WASM 実行（約2〜4秒/文）、COMET-QE（wmt20）での採点、LLM 判定（Claude）、表と食い違いの集計。
- 未了: CometKiwi（gated。使うには Hugging Face で利用条件に同意し、トークンを用意する必要がある）。指示文を変えた Shisa の再試行、文数を増やすこと、WebGPU のある環境での速度。
