# bergamot-vs-shisa

Firefox 内蔵翻訳のモデル（Mozilla の Firefox Translations、エンジンは Bergamot 系）と、ブラウザの中で動く Shisa V2.1c LFM2 350M（[takano32/pyodide-llm](https://github.com/takano32/pyodide-llm) の既定モデル）に、同じ日英の文を通して訳を並べる実験。ブラウザ拡張で LLM 翻訳を作る前に、350M が内蔵翻訳の品質に届くかを見るための下調べ。

後から、CyberAgent の [CAT-Translate](https://huggingface.co/cyberagent/CAT-Translate-0.8b)（日英の翻訳だけに学習した小型モデル、0.8B と 1.4B）も同じ30文に通して、同じ表に足した。

## 結果の見方

- `results/scores.md`: 採点の結果（平均、文ごとの点、COMET と LLM 判定の食い違い、系どうしの差の目安）。まずここを見る。
- `results/compare.md`: 30文の訳が並んでいる。点は付けていない（CAT-Translate は入っていない）。
- `results/comet.jsonl`: COMET-QE の点（1行が1文・1系）。`comet_qe` は訳のまま、`comet_qe_first_line` は最初の空でない行だけ。
- `results/llm_judge.jsonl`: LLM 判定の点（正確さ、自然さ、注釈減点、総合）と一行の理由。`label` は判定時に付けた匿名ラベル（Firefox 等の系の組は X、Y、Z、CAT の組は X、Y）。`pass` が 2 の行は2回目の判定（後述）。

データと訳:

- `data/sentences.jsonl`: 日→英 15本、英→日 15本。技術文、会話、Web 記事風を各5本ずつ。
- `results/bergamot.jsonl`: Firefox 翻訳モデルの訳。
- `results/shisa.jsonl`: Shisa 350M の訳（温度0の貪欲、seed 1、CPU の WASM。この箱に GPU は無い）。生の出力は `raw`、速度は `meta`。
- `results/shisa_strict.jsonl`: Shisa 350M に厳しい指示文を与えた訳（`SHISA_PROMPT=strict`）。
- `results/cat08.jsonl`: CAT-Translate 0.8B の訳（`PYODIDE_MODEL=hf-cat-translate-0.8b SHISA_PROMPT=card`。温度0、greedy）。
- `results/cat14.jsonl`: CAT-Translate 1.4B の訳（`PYODIDE_MODEL=hf-cat-translate-1.4b SHISA_PROMPT=card`。同じ条件）。

## 採点の基準

### COMET-QE（機械による採点）

- モデルは `Unbabel/wmt20-comet-qe-da`（Apache-2.0、Hugging Face で gated ではない。[モデルカード](https://huggingface.co/Unbabel/wmt20-comet-qe-da)）。原文と訳だけを見る reference-less の QE で、正解訳は使わない。
- 本命の `Unbabel/wmt22-cometkiwi-da` は gated（利用条件への同意とトークンが要る）。この箱にはトークンが無いので、迂回はせず gated でない wmt20 版を使った。
- CPU で実行（`gpus=0`）。モデルカードには、スコアに上限が無く、ノイズも大きいと書いてある。絶対値より、系どうしの差を見る。
- 点は2種類。`comet_qe` は訳のまま、`comet_qe_first_line` は最初の空でない行だけで、注釈の影響を測るため。
- CAT-Translate の2系は、あとから `--systems cat08 cat14` で採点した。ほかの系の行は、既存のものをそのまま残した（`--systems` のとき）。

### LLM 判定（Claude による読み）

判定は2回に分かれている。どちらも判定役は Claude（Haiku 5.5）で、基準は同じ。

- 1回目（Firefox、Shisa 350M、厳しい指示文の3系）: 原文と3つの訳を読んで、一文ずつ点を付けた。
  - 匿名化: 文ごとに3系の順番を乱数（seed 20261105）で入れ替え、X、Y、Z と名付けて読んだ。ただし注釈の付き方から系が推測できる文が多く、完全な匿名にはなっていない。
- 2回目（CAT-Translate 0.8B と 1.4B の2系）: 別のセッションの判定役が、原文と2つの訳を読んで点を付けた。既存の3系の判定はやり直していない。
  - 匿名化: 文ごとに2系の順番を乱数（seed 20261106）で入れ替え、X と Y と名付けた。ただし、判定役は判定の前に実行ログを見ていた（ログには系の名前が出ている）。盲検は完全ではない。
  - 判定の前に全部書き、COMET の数字は見ていない（COMET はこの後に動かした）。
- 判定の記録は `results/llm_judge.jsonl`。2回目の行には `pass: 2` を付けた。

判定役が違うので、回をまたぐ LLM の差（Firefox や Shisa と CAT の差）は、判定役の違いを含む。`scores.md` では、回をまたぐ組に「※判定の回が違う」を付けた。

点の基準（両回共通）:

- 正確さ（1〜5）: 5 誤り、抜け、足しが無い。4 小さな言い換えのずれ。3 重要な語の誤訳か、読みに響く抜けが1点。2 主要な意味が違う（否定、順序、取り違え、別の選択肢）。1 訳になっていない（向きの取り違え、答えや説明への置き換え）。
- 自然さ（1〜5）: 5 そのまま使える。4 小さな不自然さが1点。3 不自然な語や文体が複数（場面に合わない文体を含む）。2 意味は取れるが破綻が目立つ。1 読めない。
- 注釈減点（0 か -1）: 訳の後ろに注釈、解説、代替案、質問返し、指示文の漏れがあれば -1。内容が正しくても減点する。
- 総合 = 正確さ + 自然さ + 注釈減点（2〜10）。
- 向きを取り違えた出力（日→英なのに日本語で返したなど）は、正確さも自然さも 1 にする。

### 食い違いの定義

同じ文の2系の組で、LLM 総合の差が 2 点以上あるのに、COMET-QE の差の向きが逆のもの（COMET の同点は除く）。2 点は、正確さか自然さのどちらかで2段階の差がある程度の幅として、判定の前に決めた。全部の組（5系で10組、30文で300組）を数える。

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
SHISA_PROMPT=strict node scripts/run_shisa.mjs "" results/shisa_strict.jsonl  # 厳しい指示文の版
PYODIDE_MODEL=hf-cat-translate-0.8b SHISA_PROMPT=card node scripts/run_shisa.mjs "" results/cat08.jsonl  # CAT-Translate 0.8B（取得 845 MB）
PYODIDE_MODEL=hf-cat-translate-1.4b SHISA_PROMPT=card node scripts/run_shisa.mjs "" results/cat14.jsonl  # CAT-Translate 1.4B（取得 1.5 GB）
python3 scripts/compare.py               # results/compare.md
.venv/bin/pip install -r requirements-comet.txt && .venv/bin/pip install --no-deps unbabel-comet==2.2.7
.venv/bin/python scripts/comet_score.py  # results/comet.jsonl（初回は COMET のモデル 2.3GB を .cache/huggingface に取る）
.venv/bin/python scripts/make_scores.py  # results/scores.md
python3 scripts/count_flags.py bergamot shisa shisa_strict cat08 cat14  # 注釈と向きの取り違えの数（下の「気づいたこと」）
```

`run_shisa.mjs` の第1引数 `""` は既定のサイト（`SHISA_SITE` か `https://takano32.github.io/pyodide-llm/`）を使う意味。CAT-Translate のモデルは同じ公開サイトに id（`hf-cat-translate-0.8b`、`hf-cat-translate-1.4b`）がある。

必要なもの: Python 3、Node.js、`zstd`、Google Chrome（`/usr/bin/google-chrome`、別の場所なら `SHISA_CHROME`）。COMET の採点は CPU で約10分（この箱、他の作業と並行して）。CAT-Translate の2系は、取得と変換と30文を含めて1系あたり約7〜10分。

LLM 判定は、スクリプトで再現するものではない。`results/llm_judge.jsonl` の点と理由が、判定の記録そのもの。

## 結果

| 系 | COMET-QE（訳のまま） | COMET-QE（先頭行だけ） | LLM 正確さ | LLM 自然さ | LLM 注釈減点 | LLM 総合 | LLM 判定の回 |
|---|---|---|---|---|---|---|---|
| Firefox 翻訳 | 0.294 | 0.294 | 4.20 | 3.97 | 0.00 | 8.17 | 1 |
| Shisa 350M | 0.285 | 0.332 | 3.80 | 3.77 | -0.20 | 7.37 | 1 |
| Shisa 350M（厳しい指示文） | 0.138 | 0.361 | 3.97 | 3.70 | -0.53 | 7.13 | 1 |
| CAT-Translate 0.8B | 0.328 | 0.328 | 4.63 | 4.70 | 0.00 | 9.33 | 2 |
| CAT-Translate 1.4B | 0.351 | 0.351 | 4.27 | 4.10 | 0.00 | 8.37 | 2 |

方向別の LLM 総合（英→日、日→英）:

- 英→日: Firefox 8.27、Shisa 8.07、厳しい版 8.00、CAT 0.8B 9.20、CAT 1.4B 8.33。
- 日→英: Firefox 8.07、Shisa 6.67、厳しい版 6.27、CAT 0.8B 9.47、CAT 1.4B 8.40。

種類別の LLM 総合（技術文、会話、Web 記事風）:

- Firefox 8.40、7.30、8.80。Shisa 7.30、6.70、8.10。厳しい版 7.80、6.50、7.10。
- CAT 0.8B 9.70、9.10、9.20。CAT 1.4B 8.80、8.40、7.90。

差の大きさ（文ごとの差の平均と、約95%の幅）:

- 同じ判定の回の組（Firefox と Shisa の組）: LLM の Firefox − Shisa は 0.80（−0.29〜1.89）、Firefox − 厳しい版は 1.03（−0.14〜2.21）。COMET-QE の Firefox − Shisa は 0.009（−0.084〜0.102）、Firefox − 厳しい版は 0.156（0.005〜0.307）。30文では、どの差も確かとは言えない。
- CAT の2系（同じ2回目の判定）: 0.8B − 1.4B は COMET-QE で −0.022（−0.056〜0.011）、LLM 総合で 0.97（0.34〜1.59）。COMET-QE では差は出ていないが、LLM 判定は 0.8B を高く付けた。
- 回をまたぐ組（Firefox と CAT、Shisa と CAT）: COMET-QE の Firefox − 0.8B は −0.034（−0.085〜0.017）、Firefox − 1.4B は −0.056（−0.106〜−0.007）。LLM の Firefox − 0.8B は −1.17（−1.82〜−0.51）、Firefox − 1.4B は −0.20（−1.03〜0.63）。回をまたぐ LLM の差は、判定役の違いを含むので参考にとどめる。

CAT-Translate の注釈と向き（機械で数えた。定義は下の「気づいたこと」）:

- 注釈のある出力は、CAT 0.8B が 0 件、CAT 1.4B が 0 件（Firefox 0、Shisa 6、厳しい版 16）。
- 向きを取り違えた出力は、CAT 0.8B が 0 件、CAT 1.4B が 1 件（文26）。Firefox 0、Shisa 2、厳しい版 3。

速度（文あたりの時間。この箱で、他のジョブと共用、2コア）:

| 系 | 平均 | 中央値 | 速さ（平均 tok/s） | 初回の取得と変換 |
|---|---|---|---|---|
| Shisa 350M | 3.5 秒 | 2.9 秒 | 17.6 | 約90秒（379 MB） |
| CAT-Translate 0.8B | 7.6 秒 | 5.8 秒 | 6.7 | 約3分（845 MB、起動まで206秒） |
| CAT-Translate 1.4B | 9.0 秒 | 7.7 秒 | 4.8 | 約5分（1.5 GB、起動まで294秒） |

Shisa の時間は 10:59 の実行で、CAT の実行は 12:01 から。この箱の負荷が違うので、速さの差は目安として読む。Firefox 翻訳は 0.2 秒/文（fxtranslate、CPU）。

COMET と LLM 判定の食い違い: 全部の組（300組）のうち、向きが逆になったのは76組。そのうち LLM の差が2点以上のものは41組で、内訳は判定の回が同じ組が17（1回目の3系で13、2回目の2系で4）、回をまたぐ組が24。1回目だけで数えていた前の版の13組とは、数える組の範囲が違う。

目立つ例:

- 文8（英→日、会話。"I'm leaning toward taking the earlier flight."）: 1.4B は earlier flight を「前回のフライト」と取り違えた（LLM 5 点）。0.8B は「早めに飛ぶほう」で意味が残った（LLM 8 点）。それでも COMET-QE は 1.4B（0.117）を 0.8B（0.066）より高く付けた。COMET-QE は、この取り違えを見ていない。
- 文26（日→英、Web）: 1.4B は英語の "The" の後に日本語の文を残した（向きの取り違え、LLM 2 点）。COMET-QE は 0.706 を付け、この文で最も高い点になった（Firefox 0.530、0.8B 0.528）。文25の Shisa と同じ形で、COMET-QE は訳の言語を見ていない。
- 文21（日→英、会話。「遅れてごめん」）: 0.8B は "Sorry for the late reply" と、遅刻を返信の遅れに取り違えた（LLM 6 点）。1.4B は "Sorry for the delay" で正しく（LLM 9 点）。COMET-QE も 1.4B（0.262）を 0.8B（0.210）より高くした。こちらは両者が一致した例。

## 注意

- 訳したエンジンは `fxtranslate`（Rust 製の実装）で、Firefox が使うのと同じモデルを読ませている。Firefox に載っている Bergamot の C++ 実装そのものではない。PyPI の `bergamot` は Python 3.10 までの wheel しかなかったので使っていない。
- `fxtranslate` 自身のモデル取得はこの箱の TLS で失敗した（証明書の署名エラー）。そこでモデルは `scripts/fetch_models.py` で Mozilla の Remote Settings から自前で取り、ハッシュを確かめて置いている。
- Shisa 側の指示文は2種類（`scripts/run_shisa.mjs` の `prompt`。`SHISA_PROMPT=strict` で厳しい版）。厳しい版は `results/shisa_strict.jsonl`。
- CAT-Translate の指示文は、モデルカードの書式をそのまま使った（`SHISA_PROMPT=card`）。`Translate the following {src_lang} text into {tgt_lang}.` に続けて空行、原文。言語名は Japanese と English。モデルカードは、この書式を chat template で包むよう書いている。ページ側（pyodide-llm の定義、`template: SARASHINA`）が包んでいる。
- CAT-Translate の生成の上限は、スクリプトが 300 を入れたのに、ページのスライダーの刻みで 304 になった。出力の総トークン数（プロンプト込み）は最大 69 で、上限には届いていない。モデルカードの `max_new_tokens=512` とは違う値だが、今回の文では効いていない。
- 公開サイトは `takano32.github.io/pyodide-llm`（ビルド f46610e）。両モデルの id はこのビルドにある。手元の pyodide-llm（b0670514）の定義とは照合していない。
- CAT-Translate 0.8B のモデルカードは MIT と書いている。1.4B のカードは確かめていない。
- COMET-QE の点は、訳の言語が原文と同じでも、それらしい文なら高く出ることがある（文25、文26）。向きの検査は別にやる必要がある。今回の CAT 1.4B は、向きの取り違えの文でも COMET-QE の点が高かった。
- LLM 判定は Claude 自身の読みで、30文・1人の判定（回ごとに1人）。判定役を変えれば点も変わる。2回目の判定では CAT の2系が 9.33 と 8.37 で、1回目の Firefox（8.17）より高く出た。CAT の訳が実際に良いのか、2回目の判定が甘いのか、この資料では分けられない。
- 2回目の判定は、判定役が実行ログで系の名前を見ていた。盲検は完全ではない。

## 気づいたこと（機械で数えたもの。訳の良し悪しの採点ではない）

数え方は `scripts/count_flags.py`。

- 注釈のある出力: 空でない行が2行以上ある文の数。
- 向きの取り違え: 目標が英語なのに最初の空でない行に日本語の字（ひらがな、カタカナ、漢字）がある、または目標が日本語なのに最初の行に日本語の字が無い。注釈の中の日本語は数えない。この数え方で、Shisa 350M は 2、厳しい版は 3 になる（前からの結果と同じ）。

30文のうち、訳のあとに注釈や余計な文が付いた出力は Firefox 翻訳モデルが0、Shisa 350M が6（指示文が基本のとき）、16（厳しい指示文のとき）、CAT-Translate の0.8B と1.4B は0。訳す向きを取り違えた出力は、Firefox が0、Shisa が2、厳しい版が3、CAT 0.8B が0、CAT 1.4B が1（文26）。厳しい指示文で「注釈をつけるな」と書いたのに、その文言を注釈の中で繰り返す出力が出ており、350M にとって指示文を厳しくしても直らなかった。CAT-Translate は、指示文を変えずに訳だけを返した。実装に使うなら、出力を最初の1行で切る、向きを後で検査する、などの後処理が要るのは Shisa の系だけになる。

## 現状と未了

- 済み: 5系（Firefox 翻訳、Shisa 350M の2種、CAT-Translate 0.8B と 1.4B）の30文の訳、COMET-QE の5系での採点、LLM 判定（Claude、2回に分けて）、表と食い違いの集計。
- 未了: CometKiwi（gated。使うには Hugging Face で利用条件に同意し、トークンを用意する必要がある）。CAT-Translate 3.3B（取得 6.7 GB）と 7B（同 8.0 GB）。公開サイトに id はある。5系を1回の判定で揃え直すこと（既存の判定はやり直していない）。文数を増やすこと。WebGPU のある環境での速度。
