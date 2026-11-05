# bergamot-vs-shisa

Firefox 内蔵翻訳のモデル（Mozilla の Firefox Translations、エンジンは Bergamot 系）と、ブラウザの中で動く小型 LLM 数種に、同じ日英100文を通して訳を並べ、採点する実験。ブラウザ拡張で LLM 翻訳を作る前に、小型 LLM が内蔵翻訳の品質に届くかを見るための下調べ。

比べる5系:

- Firefox 翻訳（`fxtranslate` に Firefox と同じモデルを読ませたもの）
- Shisa V2.1c LFM2 350M（[takano32/pyodide-llm](https://github.com/takano32/pyodide-llm) の既定モデル）の基本の指示文
- 同じ Shisa 350M の厳しい指示文（注釈と原文の言語への戻りを禁じる）
- CAT-Translate 0.8B（CyberAgent の日英翻訳専用モデル、[モデルカード](https://huggingface.co/cyberagent/CAT-Translate-0.8b)）
- CAT-Translate 1.4B

## 結果の見方

- `results/scores.md`: 採点の結果。まずここを見る（網羅の表、全体、方向別、分野別、現象別、文ごとの点、COMET と LLM の食い違い、系どうしの差の目安）。
- `results/compare.md`: 100文の訳が5系ぶん並んでいる（点は付けていない）。
- `data/sentences.jsonl`: 100文。`category` が分野、`tags` が現象タグ。
- `results/{bergamot,shisa,shisa_strict,cat08,cat14}.jsonl`: 5系の訳。Shisa と CAT は生の出力が `raw`、速度が `meta`。
- `results/comet.jsonl`: COMET-QE の点（1行が1文・1系）。`comet_qe` は訳のまま、`comet_qe_first_line` は最初の空でない行だけ。
- `results/llm_judge.jsonl`: LLM 判定の点（正確さ、自然さ、注釈減点、総合）と一行の理由。`label` は判定時の匿名ラベル（A〜E）。
- `results/llm_blind_input.md`: 判定役が読んだ入力そのもの（系の名前なし）。`results/llm_key.json`: ラベルと系の対応表。

## 例文100本の設計（網羅の軸）

10分野 × 10本。各分野を英→日5本、日→英5本にして、方向と分野の偏りを無くした。文は全部この実験のために書いた自作で、既存の文章の引き写しも、訳が広く知られた有名な文も入れていない。元データは `scripts/build_sentences.py`（`python3 scripts/build_sentences.py` で `data/sentences.jsonl` を作り直す）。

分野（10種）: 技術文書、UI の文言、ニュース、Web 記事・ブログ、ビジネスメール、くだけた会話、接客・丁寧な会話、法律・規約、文学的な文、SNS の短文。

現象タグ（12種。1文に複数つく）: 敬語・丁寧さ、主語の省略、慣用句・口語表現、数字・日付・単位、固有名詞、多義語、否定、疑問、長文、短い断片、コード・記号混じり、Markdown。手で付けたのは敬語、主語の省略、慣用句、数字、固有名詞、多義語、否定、疑問。長文（日本語45字以上か英語25語以上）、短い断片（日本語20字以下か英語6語以下）、コード（バッククォート、`{name}`、`#`タグ、`@`宛先）、Markdown（`**`、リンク、見出し）は規則で機械的に付けた。

| 分野 | 英→日 | 日→英 | 計 |
|---|---|---|---|
| 技術文書（tech） | 5 | 5 | 10 |
| UI の文言（ui） | 5 | 5 | 10 |
| ニュース（news） | 5 | 5 | 10 |
| Web 記事・ブログ（web） | 5 | 5 | 10 |
| ビジネスメール（biz） | 5 | 5 | 10 |
| くだけた会話（casual） | 5 | 5 | 10 |
| 接客・丁寧な会話（polite） | 5 | 5 | 10 |
| 法律・規約（legal） | 5 | 5 | 10 |
| 文学的な文（lit） | 5 | 5 | 10 |
| SNS の短文（sns） | 5 | 5 | 10 |

| 現象タグ | 英→日 | 日→英 | 計 |
|---|---|---|---|
| 敬語・丁寧さ（hon） | 6 | 15 | 21 |
| 主語の省略（pro） | 0 | 32 | 32 |
| 慣用句・口語表現（idm） | 14 | 9 | 23 |
| 数字・日付・単位（num） | 16 | 10 | 26 |
| 固有名詞（prop） | 5 | 6 | 11 |
| 多義語（poly） | 5 | 6 | 11 |
| 否定（neg） | 14 | 10 | 24 |
| 疑問（q） | 11 | 6 | 17 |
| 長文（long） | 4 | 7 | 11 |
| 短い断片（frag） | 7 | 10 | 17 |
| コード・記号混じり（code） | 5 | 4 | 9 |
| Markdown（md） | 4 | 3 | 7 |

偏りの読み方: 分野は完全に均等。現象は均等にできていない。主語の省略は日本語を原文とする文でしか起きないので、英→日は0本。敬語は日→英に15本、英→日に6本。長文（11本）、コード（9本）、Markdown（7本）は少なく、この3つの平均は本数が少ないぶん揺れる。

## 採点の基準

### COMET-QE（機械による採点）

- モデルは `Unbabel/wmt20-comet-qe-da`（Apache-2.0、Hugging Face で gated ではない。[モデルカード](https://huggingface.co/Unbabel/wmt20-comet-qe-da)）。原文と訳だけを見る reference-less の QE で、正解訳は使わない。
- 本命の `Unbabel/wmt22-cometkiwi-da` は gated（利用条件への同意とトークンが要る）。この箱にはトークンが無いので、迂回はせず gated でない wmt20 版を使った。
- CPU で実行（`gpus=0`）。モデルカードには、スコアに上限が無く、ノイズも大きいと書いてある。絶対値より、系どうしの差を見る。
- 点は2種類。`comet_qe` は訳のまま、`comet_qe_first_line` は最初の空でない行だけで、注釈の影響を測るため。

### LLM 判定（Claude による読み）

- 判定役は Claude（Sonnet 5.5）が1人、1セッション。5系の訳を1回でまとめて読んだ（前回のように判定の回を分けていない）。
- 匿名化: 文ごとに5系の並びを乱数（seed 20261107）で入れ替え、A〜E と名付けた。`scripts/make_blind.py` が入力ファイルと対応表を作る。判定役は判定を全部書き終えるまで対応表を開かず、COMET の数字も見ていない（COMET は判定の記録をコミットしたあとに終わった。コミット 803f358）。
- 匿名が完全でない点: 注釈の付き方や文体、書式の癖から、どの系かが推測できる文が多い（特に Shisa の注釈と、向きの取り違え）。判定役が実際に系を推測したか、推測が点に影響したかは分けられない。
- 判定の記録は `results/llm_judge.jsonl`（`scripts/join_judge.py` が対応表と結んで作る）。

点の基準:

- 正確さ（1〜5）: 5 誤り、抜け、足しが無い。4 小さな言い換えのずれ。3 重要な語の誤訳か、読みに響く抜けが1点。2 主要な意味が違う（否定、順序、取り違え、別の選択肢）。1 訳になっていない（向きの取り違え、答えや説明への置き換え）。
- 自然さ（1〜5）: 5 そのまま使える。4 小さな不自然さが1点。3 不自然な語や文体が複数（場面に合わない文体を含む）。2 意味は取れるが破綻が目立つ。1 読めない。
- 注釈減点（0 か -1）: 訳の後ろに注釈、解説、代替案、質問返し、指示文の漏れがあれば -1。内容が正しくても減点する。
- 総合 = 正確さ + 自然さ + 注釈減点（1〜10）。
- 向きを取り違えた出力（日→英なのに日本語で返したなど）は、正確さも自然さも 1 にする。

### 食い違いの定義

同じ文の2系の組で、LLM 総合の差が 2 点以上あるのに、COMET-QE の差の向きが逆のもの（COMET の同点は除く）。2 点は、正確さか自然さのどちらかで2段階の差がある程度の幅として決めた（前回の定義を引き継いだ）。全部の組は 10組 × 100文 = 1000組。

### 差の目安

文ごとの差の平均と、標準誤差の2倍で作った約95%の幅。幅が0をまたぐ差は、100文では区別できていないと読む。

## 結果

全体（100文）:

| 系 | COMET-QE（訳のまま） | COMET-QE（先頭行だけ） | LLM 正確さ | LLM 自然さ | LLM 注釈減点 | LLM 総合 |
|---|---|---|---|---|---|---|
| Firefox 翻訳 | 0.235 | 0.235 | 3.83 | 3.73 | 0.00 | 7.56 |
| Shisa 350M | 0.238 | 0.305 | 3.18 | 3.34 | -0.35 | 6.17 |
| Shisa 350M（厳しい指示文） | 0.045 | 0.341 | 2.64 | 2.74 | -0.67 | 4.71 |
| CAT-Translate 0.8B | 0.333 | 0.333 | 4.42 | 4.34 | 0.00 | 8.76 |
| CAT-Translate 1.4B | 0.367 | 0.367 | 4.44 | 4.36 | 0.00 | 8.80 |

- LLM 総合で見ると CAT の2系が Firefox より上で（0.8B との差 +1.20、幅 0.72〜1.68。1.4B との差 +1.24、幅 0.74〜1.74）、Firefox は Shisa 350M より上（+1.39、幅 0.78〜2.00）。CAT 0.8B と 1.4B の差は -0.04（幅 -0.36〜0.28）で、区別できていない。
- 文ごとの最高点（同点は各系に数える）: CAT 1.4B が61文、CAT 0.8B が57文、Firefox が33文、Shisa が12文、厳しい版が8文。
- COMET-QE では、CAT 1.4B が 0.8B より 0.034 高い（幅 0.007〜0.060）。Firefox と Shisa 350M の差は -0.003 で区別できない（幅 -0.068〜0.062）。厳しい版は訳のままだと 0.045 まで落ち、先頭行だけにすると 0.341 に戻る（注釈の影響）。

方向別（LLM 総合 / COMET-QE）:

| 方向 | Firefox | Shisa | Shisa 厳 | CAT 0.8B | CAT 1.4B |
|---|---|---|---|---|---|
| 英→日（50） | 7.44 / 0.296 | 6.58 / 0.208 | 6.00 / -0.027 | 8.86 / 0.365 | 9.00 / 0.430 |
| 日→英（50） | 7.68 / 0.175 | 5.76 / 0.268 | 3.42 / 0.117 | 8.66 / 0.301 | 8.60 / 0.304 |

分野別・現象別の表は `results/scores.md` にある（各セルは LLM 総合 / COMET-QE）。目立つところ:

- 分野: Firefox と CAT の差が小さいのは法律・規約（Firefox 9.20、0.8B 8.30、1.4B 9.30）とニュース（8.80、9.20、9.00）で、定型の文に近い。いちばん低いのは SNS の短文（5.90）。CAT の2系はどの分野も 7.7 以上で、低いのはビジネスメール（0.8B 8.00、1.4B 7.70）。Shisa 350M が低いのはニュース（5.40）、SNS（5.30）、法律（5.60）で、技術文書（7.30）と接客（7.20）はまだ近い。
- 現象: 固有名詞で Shisa が落ち（4.27、Firefox 7.73、CAT 8.55 と 8.64）、疑問で Firefox が落ちる（6.82、CAT 8.76 と 9.06）。コード・記号混じりは全系で低め（Firefox 6.89、CAT 8.22 と 8.44）。長文では CAT 0.8B が 8.09、1.4B が 9.09（長文は11本）。慣用句は Firefox が 6.61 で、CAT は 8.26 と 8.30。

注釈と向きの取り違え（機械で数えた。定義は下の「気づいたこと」）:

| 系 | 注釈のある文 | 向きの取り違え |
|---|---|---|
| Firefox | 0 | 0 |
| Shisa 350M | 36 | 11 |
| Shisa 350M（厳しい指示文） | 64 | 27 |
| CAT 0.8B | 0 | 1（文82） |
| CAT 1.4B | 0 | 3（文54、74、82） |

CAT の向きの数え方に注意: 文82は両モデルとも原文の日本語（0.8B）か、日本語の言い換え（1.4B）をそのまま返した。文74（1.4B）は英語の文に日本語を混ぜた。文54（1.4B）は先頭の「注意:」が日本語のまま残っただけで、訳は英語になっている（機械の数え方では取り違えに数えられる）。

速度（文あたりの時間。この箱で2コア。ページが決めるスレッド数は2〜4と揺れていて、そろえていない）:

| 系 | 平均 | 中央値 | 速さ（平均 tok/s） | 起動まで（取得と変換、キャッシュ前） |
|---|---|---|---|---|
| Firefox 翻訳 | 0.18 秒 | - | - | - |
| Shisa 350M | 3.9 秒 | 3.0 秒 | 17.9 | 85 秒 |
| Shisa 350M（厳しい指示文） | 4.5 秒 | 3.5 秒 | 22.6 | - |
| CAT-Translate 0.8B | 4.0 秒 | 3.7 秒 | 8.9 | 173 秒 |
| CAT-Translate 1.4B | 6.2 秒 | 5.0 秒 | 6.3 | 297 秒 |

起動までの秒数は、Shisa は基本の指示文の実行、CAT は各実行のログの `ready:` の時刻。厳しい版は同じモデルで、起動の時間を取っていない。訳の総時間は5系で約43分（12:45〜13:28）、COMET-QE の採点は500組で約28分。

COMET と LLM 判定の食い違い: 1000組のうち、COMET の向きが逆になったのは244組。LLM の差が2点以上ある組は638組で、そのうち向きが逆だったのが172組（`results/scores.md` に全部の表）。

目立つ例:

- 文82（日→英、接客。「恐れ入りますが、こちらの商品は在庫を切らしております。」）: CAT 0.8B は原文の日本語をそのまま返した（LLM 2 点）。COMET-QE はこれに 0.972 を付け、この文でいちばん高い点にした（英語に訳した Firefox は 0.607、LLM 9 点）。向きを取り違えた Shisa 350M は、全体でも COMET の平均が 0.524 で、向きが合っている文の平均 0.203 より高い。COMET-QE はこの設定では訳の言語を見ていない。
- 文56（日→英、UI。「保存せずに閉じる」）: Firefox も CAT 0.8B・1.4B も "Close without saving" と正しく訳した（LLM 10 点）のに、COMET-QE は -0.604、-0.592 と低く付けた。Shisa の厳しい版は日本語で返した（LLM 1 点）が COMET は 0.121 で、COMET の順位は逆になっている。

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
python3 scripts/build_sentences.py        # data/sentences.jsonl（100文）
python3 scripts/fetch_models.py           # models/ に en-ja と ja-en のモデルを取り出す（リポには入れない）
scripts/run_all.bash /tmp                 # 5系の訳を順に作る（Firefox、Shisa 基本、Shisa 厳しい版、CAT 0.8B、CAT 1.4B）。ログは第1引数の場所へ
python3 scripts/compare.py                # results/compare.md
.venv/bin/pip install -r requirements-comet.txt && .venv/bin/pip install --no-deps unbabel-comet==2.2.7
.venv/bin/python scripts/comet_score.py   # results/comet.jsonl（初回は COMET のモデル 2.3GB を .cache/huggingface に取る）
python3 scripts/make_blind.py /tmp/blind.md   # LLM 判定の匿名入力と results/llm_key.json
python3 scripts/join_judge.py <判定の jsonl>  # 判定役が書いた点（id, label, acc, nat, pen, why）を結んで results/llm_judge.jsonl
.venv/bin/python scripts/make_scores.py   # results/scores.md
python3 scripts/count_flags.py bergamot shisa shisa_strict cat08 cat14  # 注釈と向きの取り違えの数
```

`run_shisa.mjs` の第1引数 `""` は既定のサイト（`SHISA_SITE` か `https://takano32.github.io/pyodide-llm/`）を使う意味。CAT-Translate のモデルは同じ公開サイトに id（`hf-cat-translate-0.8b`、`hf-cat-translate-1.4b`）がある。

必要なもの: Python 3、Node.js、`zstd`、Google Chrome（`/usr/bin/google-chrome`、別の場所なら `SHISA_CHROME`）。

LLM 判定は、スクリプトで再現するものではない。`results/llm_judge.jsonl` の点と理由が、判定の記録そのもの。判定の入力（`results/llm_blind_input.md`）と対応表（`results/llm_key.json`）は残してあるので、別の判定役で付け直して比べられる。

## 注意

- 訳したエンジンは `fxtranslate`（Rust 製の実装）で、Firefox が使うのと同じモデルを読ませている。Firefox に載っている Bergamot の C++ 実装そのものではない。PyPI の `bergamot` は Python 3.10 までの wheel しかなかったので使っていない。
- `fxtranslate` 自身のモデル取得はこの箱の TLS で失敗した（証明書の署名エラー）。そこでモデルは `scripts/fetch_models.py` で Mozilla の Remote Settings から自前で取り、ハッシュを確かめて置いている。
- Shisa 側の指示文は2種類（`scripts/run_shisa.mjs` の `prompt`。`SHISA_PROMPT=strict` で厳しい版）。CAT-Translate の指示文は、モデルカードの書式をそのまま使った（`SHISA_PROMPT=card`）。`Translate the following {src_lang} text into {tgt_lang}.` に続けて空行、原文。言語名は Japanese と English。chat template の包みはページ側（pyodide-llm の定義、`template: SARASHINA`）が行う。
- 生成の上限は、スクリプトが 300 を入れたのに、ページのスライダーの刻みで 304 になる（前回確かめた挙動で、今回は再確認していない）。モデルカードの `max_new_tokens=512` とは違う。今回の100文で上限に届いて切れた出力があったかは調べていない。
- 公開サイトは `takano32.github.io/pyodide-llm`。両モデルの id が載っている。手元の pyodide-llm の定義とは照合していない。ページの `meta` に出るスレッド数は実行ごとに 2 か 4 か不明で揺れていた。原因は調べていない。
- COMET-QE の点は、訳の言語が原文と同じでも、それらしい文なら高く出る（文82）。向きの検査は別にやる必要がある。
- LLM 判定は Claude 自身の読みで、100文・1人・1回。判定役（Sonnet 5.5）は、例文を書いた作者でもある。同じ系統のモデルが書いて読むので、癖の偏りが出うる。判定役を変えれば点も変わる。前回の判定役は Haiku で、今回と点を比べていない。
- 例文は10分野×10本で網羅を狙ったが、100文では分野内の差を言い切るには少ない（分野別の平均は各10文）。

## 気づいたこと（機械で数えたもの。訳の良し悪しの採点ではない）

数え方は `scripts/count_flags.py`。

- 注釈のある出力: 空でない行が2行以上ある文の数。
- 向きの取り違え: 目標が英語なのに最初の空でない行に日本語の字（ひらがな、カタカナ、漢字）がある、または目標が日本語なのに最初の行に日本語の字が無い。注釈の中の日本語は数えない。

100文で、Shisa 350M は36文に注釈がつき、11文で向きを取り違えた。厳しい指示文にすると注釈は64文、向きの取り違えは27文に増えた（指示文を厳しくしても直らず、悪化した。理由は調べていない）。Firefox は注釈も向きの取り違えもなし。CAT の2系は注釈なしで、向きの取り違えは上の表のとおり少ない。実装に使うなら、出力を最初の1行で切る、向きを後で検査する、などの後処理が要るのは Shisa の系だけになる。

## 現状と未了

- 済み: 100文（10分野、現象タグ12種）の5系での訳、COMET-QE の採点、LLM 判定（1回、匿名）、表と食い違いの集計。
- 未了: CometKiwi（gated。使うには Hugging Face で利用条件に同意し、トークンを用意する必要がある。試していない）。CAT-Translate 3.3B（取得 6.7 GB）と 7B（同 8.0 GB）。公開サイトに id はあるが、試していない。別の判定役での付け直し。WebGPU のある環境での速度。
