# 採点の結果（COMET-QE と LLM 判定）

COMET-QE は `results/comet.jsonl`、LLM 判定は `results/llm_judge.jsonl`。判定の基準は README の「採点の基準」。
LLM 判定は2回に分かれている。1回目は bergamot・shisa・shisa_strict を同時に見て付けた。2回目は cat08・cat14 を同時に見て付けた（判定役のセッションが別、既存の判定はやり直していない）。回をまたぐ LLM の差は、判定役の違いを含む。

## 全体の平均（30文）

| 系 | COMET-QE（訳のまま） | COMET-QE（注釈を切った先頭行） | LLM 正確さ | LLM 自然さ | LLM 注釈減点 | LLM 総合 |
|---|---|---|---|---|---|---|
| Firefox翻訳 | 0.294 | 0.294 | 4.20 | 3.97 | 0.00 | 8.17 |
| Shisa350M | 0.285 | 0.332 | 3.80 | 3.77 | -0.20 | 7.37 |
| Shisa350M厳 | 0.138 | 0.361 | 3.97 | 3.70 | -0.53 | 7.13 |
| CAT-Translate 0.8B | 0.328 | 0.328 | 4.63 | 4.70 | 0.00 | 9.33 |
| CAT-Translate 1.4B | 0.351 | 0.351 | 4.27 | 4.10 | 0.00 | 8.37 |

## 方向別、種類別、方向×種類の平均

| 群 | n | Firefox翻訳 COMET / LLM 総合 | Shisa350M COMET / LLM 総合 | Shisa350M厳 COMET / LLM 総合 | CAT-Translate 0.8B COMET / LLM 総合 | CAT-Translate 1.4B COMET / LLM 総合 |
|---|---|---|---|---|---|---|
| en→ja | 15 | 0.353 / 8.27 | 0.339 / 8.07 | 0.110 / 8.00 | 0.320 / 9.20 | 0.357 / 8.33 |
| ja→en | 15 | 0.235 / 8.07 | 0.231 / 6.67 | 0.167 / 6.27 | 0.337 / 9.47 | 0.345 / 8.40 |
| 技術文 | 10 | 0.198 / 8.40 | 0.139 / 7.30 | 0.085 / 7.80 | 0.189 / 9.70 | 0.192 / 8.80 |
| 会話 | 10 | 0.200 / 7.30 | 0.308 / 6.70 | 0.309 / 6.50 | 0.315 / 9.10 | 0.319 / 8.40 |
| Web記事風 | 10 | 0.485 / 8.80 | 0.409 / 8.10 | 0.021 / 7.10 | 0.481 / 9.20 | 0.541 / 7.90 |
| en→ja 技術文 | 5 | 0.242 / 8.40 | 0.190 / 7.80 | 0.141 / 8.20 | 0.171 / 10.00 | 0.195 / 9.00 |
| en→ja 会話 | 5 | 0.305 / 7.80 | 0.284 / 9.00 | 0.283 / 8.40 | 0.322 / 9.00 | 0.322 / 7.60 |
| en→ja Web記事風 | 5 | 0.513 / 8.60 | 0.543 / 7.40 | -0.095 / 7.40 | 0.465 / 8.60 | 0.553 / 8.40 |
| ja→en 技術文 | 5 | 0.153 / 8.40 | 0.087 / 6.80 | 0.029 / 7.40 | 0.207 / 9.40 | 0.189 / 8.60 |
| ja→en 会話 | 5 | 0.096 / 6.80 | 0.331 / 4.40 | 0.336 / 4.60 | 0.307 / 9.20 | 0.316 / 9.20 |
| ja→en Web記事風 | 5 | 0.457 / 9.00 | 0.275 / 8.80 | 0.136 / 6.80 | 0.496 / 9.80 | 0.528 / 7.40 |

## 文ごとの点

COMET は訳のまま。LLM は 正確さ/自然さ/注釈減点 の総合。最良は、その指標で一番高い系（同点は「=」）。

| id | 向き | 種類 | Firefox翻訳 COMET | Shisa350M COMET | Shisa350M厳 COMET | CAT-Translate 0.8B COMET | CAT-Translate 1.4B COMET | Firefox翻訳 LLM | Shisa350M LLM | Shisa350M厳 LLM | CAT-Translate 0.8B LLM | CAT-Translate 1.4B LLM | COMET 最良 | LLM 最良 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | en→ja | tech | 0.202 | -0.023 | 0.180 | 0.019 | 0.025 | 8 | 6 | 9 | 10 | 9 | Firefox翻訳 | CAT-Translate 0.8B |
| 2 | en→ja | tech | 0.361 | 0.523 | 0.523 | 0.335 | 0.456 | 9 | 9 | 9 | 10 | 8 | Shisa350M / Shisa350M厳 | CAT-Translate 0.8B |
| 3 | en→ja | tech | 0.379 | 0.248 | -0.176 | 0.287 | 0.346 | 6 | 9 | 8 | 10 | 9 | Firefox翻訳 | CAT-Translate 0.8B |
| 4 | en→ja | tech | -0.168 | -0.059 | 0.005 | -0.164 | -0.219 | 9 | 10 | 10 | 10 | 10 | Shisa350M厳 | Shisa350M / Shisa350M厳 / CAT-Translate 0.8B / CAT-Translate 1.4B （同点含む） |
| 5 | en→ja | tech | 0.438 | 0.263 | 0.172 | 0.381 | 0.368 | 10 | 5 | 5 | 10 | 9 | Firefox翻訳 | Firefox翻訳 / CAT-Translate 0.8B （同点含む） |
| 6 | en→ja | conv | 0.313 | 0.067 | 0.391 | 0.373 | 0.248 | 9 | 9 | 8 | 10 | 8 | Shisa350M厳 | CAT-Translate 0.8B |
| 7 | en→ja | conv | 0.268 | 0.238 | -0.082 | 0.283 | 0.407 | 9 | 8 | 8 | 9 | 7 | CAT-Translate 1.4B | Firefox翻訳 / CAT-Translate 0.8B （同点含む） |
| 8 | en→ja | conv | 0.009 | 0.351 | 0.156 | 0.066 | 0.117 | 5 | 9 | 6 | 8 | 5 | Shisa350M | Shisa350M |
| 9 | en→ja | conv | 0.373 | 0.180 | 0.381 | 0.303 | 0.366 | 9 | 9 | 10 | 9 | 10 | Shisa350M厳 | Shisa350M厳 / CAT-Translate 1.4B （同点含む） |
| 10 | en→ja | conv | 0.561 | 0.585 | 0.570 | 0.586 | 0.474 | 7 | 10 | 10 | 9 | 8 | CAT-Translate 0.8B | Shisa350M / Shisa350M厳 （同点含む） |
| 11 | en→ja | web | 0.664 | 0.648 | 0.353 | 0.442 | 0.691 | 10 | 7 | 9 | 9 | 9 | CAT-Translate 1.4B | Firefox翻訳 |
| 12 | en→ja | web | 0.421 | 0.595 | 0.573 | 0.638 | 0.665 | 8 | 8 | 9 | 9 | 8 | CAT-Translate 1.4B | Shisa350M厳 / CAT-Translate 0.8B （同点含む） |
| 13 | en→ja | web | 0.526 | 0.323 | -0.896 | 0.489 | 0.570 | 8 | 8 | 7 | 7 | 8 | CAT-Translate 1.4B | Firefox翻訳 / Shisa350M / CAT-Translate 1.4B （同点含む） |
| 14 | en→ja | web | 0.353 | 0.555 | -0.241 | 0.152 | 0.242 | 7 | 6 | 5 | 8 | 8 | Shisa350M | CAT-Translate 0.8B / CAT-Translate 1.4B （同点含む） |
| 15 | en→ja | web | 0.603 | 0.593 | -0.265 | 0.606 | 0.600 | 10 | 8 | 7 | 10 | 9 | CAT-Translate 0.8B | Firefox翻訳 / CAT-Translate 0.8B （同点含む） |
| 16 | ja→en | tech | 0.021 | 0.209 | 0.046 | 0.260 | 0.280 | 5 | 6 | 8 | 9 | 10 | CAT-Translate 1.4B | CAT-Translate 1.4B |
| 17 | ja→en | tech | 0.348 | 0.273 | 0.145 | 0.316 | 0.397 | 10 | 7 | 7 | 10 | 9 | CAT-Translate 1.4B | Firefox翻訳 / CAT-Translate 0.8B （同点含む） |
| 18 | ja→en | tech | 0.264 | 0.156 | 0.137 | 0.300 | 0.165 | 10 | 7 | 9 | 10 | 9 | CAT-Translate 0.8B | Firefox翻訳 / CAT-Translate 0.8B （同点含む） |
| 19 | ja→en | tech | -0.181 | -0.437 | -0.287 | -0.194 | -0.256 | 7 | 10 | 9 | 8 | 6 | Firefox翻訳 | Shisa350M |
| 20 | ja→en | tech | 0.313 | 0.236 | 0.103 | 0.356 | 0.361 | 10 | 4 | 4 | 10 | 9 | CAT-Translate 1.4B | Firefox翻訳 / CAT-Translate 0.8B （同点含む） |
| 21 | ja→en | conv | -0.047 | 0.174 | 0.119 | 0.210 | 0.262 | 8 | 6 | 5 | 6 | 9 | CAT-Translate 1.4B | CAT-Translate 1.4B |
| 22 | ja→en | conv | -0.040 | -0.068 | -0.005 | 0.176 | 0.032 | 5 | 3 | 5 | 10 | 7 | CAT-Translate 0.8B | CAT-Translate 0.8B |
| 23 | ja→en | conv | 0.229 | 0.305 | 0.344 | 0.209 | 0.367 | 8 | 2 | 2 | 10 | 10 | CAT-Translate 1.4B | CAT-Translate 0.8B / CAT-Translate 1.4B （同点含む） |
| 24 | ja→en | conv | 0.021 | 0.365 | 0.365 | 0.420 | 0.399 | 4 | 9 | 9 | 10 | 10 | CAT-Translate 0.8B | CAT-Translate 0.8B / CAT-Translate 1.4B （同点含む） |
| 25 | ja→en | conv | 0.316 | 0.881 | 0.855 | 0.519 | 0.522 | 9 | 2 | 2 | 10 | 10 | Shisa350M | CAT-Translate 0.8B / CAT-Translate 1.4B （同点含む） |
| 26 | ja→en | web | 0.530 | 0.288 | 0.258 | 0.528 | 0.706 | 9 | 8 | 7 | 9 | 2 | CAT-Translate 1.4B | Firefox翻訳 / CAT-Translate 0.8B （同点含む） |
| 27 | ja→en | web | 0.489 | 0.668 | 0.668 | 0.655 | 0.663 | 8 | 10 | 10 | 10 | 9 | Shisa350M / Shisa350M厳 | Shisa350M / Shisa350M厳 / CAT-Translate 0.8B （同点含む） |
| 28 | ja→en | web | 0.460 | 0.506 | 0.191 | 0.427 | 0.420 | 8 | 10 | 8 | 10 | 8 | Shisa350M | Shisa350M / CAT-Translate 0.8B （同点含む） |
| 29 | ja→en | web | 0.215 | 0.159 | -0.822 | 0.280 | 0.285 | 10 | 8 | 1 | 10 | 10 | CAT-Translate 1.4B | Firefox翻訳 / CAT-Translate 0.8B / CAT-Translate 1.4B （同点含む） |
| 30 | ja→en | web | 0.593 | -0.244 | 0.386 | 0.592 | 0.567 | 10 | 8 | 8 | 10 | 8 | Firefox翻訳 | Firefox翻訳 / CAT-Translate 0.8B （同点含む） |

## COMET と LLM 判定の食い違い

判定の定義: 同じ文の2系で、LLM 総合の差が 2 点以上あるのに、COMET の差の向きが逆のもの（COMET 同点は除く）。
「※判定の回が違う」は、一方が1回目（bergamot・shisa・shisa_strict）、他方が2回目（cat08・cat14）の組。LLM 総合の差に判定役の違いが混ざるので、その組の LLM 側は割り引いて読む。

- 向きが逆になった組は全部で 76 組（300 組のうち）。そのうち LLM の差が 2 点以上のものが下の 41 組。

| id | 向き | 種類 | 組 | LLM 総合の差（左−右） | COMET の差（左−右） |
|---|---|---|---|---|---|
| 1 | en→ja | tech | Firefox翻訳 と CAT-Translate 0.8B ※判定の回が違う | -2 | +0.183 |
| 2 | en→ja | tech | CAT-Translate 0.8B と CAT-Translate 1.4B | +2 | -0.121 |
| 3 | en→ja | tech | Firefox翻訳 と Shisa350M | -3 | +0.131 |
| 3 | en→ja | tech | Firefox翻訳 と Shisa350M厳 | -2 | +0.554 |
| 3 | en→ja | tech | Firefox翻訳 と CAT-Translate 0.8B ※判定の回が違う | -4 | +0.092 |
| 3 | en→ja | tech | Firefox翻訳 と CAT-Translate 1.4B ※判定の回が違う | -3 | +0.033 |
| 6 | en→ja | conv | Shisa350M厳 と CAT-Translate 0.8B ※判定の回が違う | -2 | +0.018 |
| 7 | en→ja | conv | Firefox翻訳 と CAT-Translate 1.4B ※判定の回が違う | +2 | -0.139 |
| 7 | en→ja | conv | CAT-Translate 0.8B と CAT-Translate 1.4B | +2 | -0.124 |
| 8 | en→ja | conv | Shisa350M厳 と CAT-Translate 0.8B ※判定の回が違う | -2 | +0.090 |
| 8 | en→ja | conv | CAT-Translate 0.8B と CAT-Translate 1.4B | +3 | -0.051 |
| 11 | en→ja | web | Shisa350M と Shisa350M厳 | -2 | +0.296 |
| 11 | en→ja | web | Shisa350M と CAT-Translate 0.8B ※判定の回が違う | -2 | +0.207 |
| 14 | en→ja | web | Shisa350M と CAT-Translate 0.8B ※判定の回が違う | -2 | +0.402 |
| 14 | en→ja | web | Shisa350M と CAT-Translate 1.4B ※判定の回が違う | -2 | +0.313 |
| 16 | ja→en | tech | Shisa350M と Shisa350M厳 | -2 | +0.163 |
| 18 | ja→en | tech | Shisa350M と Shisa350M厳 | -2 | +0.019 |
| 19 | ja→en | tech | Firefox翻訳 と Shisa350M | -3 | +0.257 |
| 19 | ja→en | tech | Firefox翻訳 と Shisa350M厳 | -2 | +0.107 |
| 19 | ja→en | tech | Shisa350M と CAT-Translate 0.8B ※判定の回が違う | +2 | -0.243 |
| 19 | ja→en | tech | Shisa350M と CAT-Translate 1.4B ※判定の回が違う | +4 | -0.181 |
| 19 | ja→en | tech | Shisa350M厳 と CAT-Translate 1.4B ※判定の回が違う | +3 | -0.032 |
| 21 | ja→en | conv | Firefox翻訳 と Shisa350M | +2 | -0.222 |
| 21 | ja→en | conv | Firefox翻訳 と Shisa350M厳 | +3 | -0.167 |
| 21 | ja→en | conv | Firefox翻訳 と CAT-Translate 0.8B ※判定の回が違う | +2 | -0.257 |
| 23 | ja→en | conv | Firefox翻訳 と Shisa350M | +6 | -0.076 |
| 23 | ja→en | conv | Firefox翻訳 と Shisa350M厳 | +6 | -0.115 |
| 23 | ja→en | conv | Firefox翻訳 と CAT-Translate 0.8B ※判定の回が違う | -2 | +0.020 |
| 23 | ja→en | conv | Shisa350M と CAT-Translate 0.8B ※判定の回が違う | -8 | +0.096 |
| 23 | ja→en | conv | Shisa350M厳 と CAT-Translate 0.8B ※判定の回が違う | -8 | +0.135 |
| 25 | ja→en | conv | Firefox翻訳 と Shisa350M | +7 | -0.565 |
| 25 | ja→en | conv | Firefox翻訳 と Shisa350M厳 | +7 | -0.539 |
| 25 | ja→en | conv | Shisa350M と CAT-Translate 0.8B ※判定の回が違う | -8 | +0.361 |
| 25 | ja→en | conv | Shisa350M と CAT-Translate 1.4B ※判定の回が違う | -8 | +0.359 |
| 25 | ja→en | conv | Shisa350M厳 と CAT-Translate 0.8B ※判定の回が違う | -8 | +0.336 |
| 25 | ja→en | conv | Shisa350M厳 と CAT-Translate 1.4B ※判定の回が違う | -8 | +0.334 |
| 26 | ja→en | web | Firefox翻訳 と CAT-Translate 1.4B ※判定の回が違う | +7 | -0.176 |
| 26 | ja→en | web | Shisa350M と CAT-Translate 1.4B ※判定の回が違う | +6 | -0.418 |
| 26 | ja→en | web | Shisa350M厳 と CAT-Translate 1.4B ※判定の回が違う | +5 | -0.448 |
| 26 | ja→en | web | CAT-Translate 0.8B と CAT-Translate 1.4B | +7 | -0.178 |
| 28 | ja→en | web | Firefox翻訳 と CAT-Translate 0.8B ※判定の回が違う | -2 | +0.033 |

## 注釈を切ると COMET はどう変わるか

「注釈のある文数」は、訳の後ろに空でない行が続く出力の数。`comet_qe_first_line` から `comet_qe` を引いた平均は、先頭行だけの採点との差（0 に近いほど、注釈の有無が COMET に効いていない）。

| 系 | 注釈のある文数 | 平均の差（先頭行−訳のまま） |
|---|---|---|
| Firefox翻訳 | 0 | 0.0000 |
| Shisa350M | 6 | 0.0466 |
| Shisa350M厳 | 16 | 0.2227 |
| CAT-Translate 0.8B | 0 | 0.0000 |
| CAT-Translate 1.4B | 0 | 0.0000 |

## 系どうしの差の目安（文の対応をとった差）

差の平均と、その標準誤差の2倍（約95%の幅）。幅が0をまたぐ差は、30文では区別できていない。

| 組 | 指標 | 平均の差（左−右） | 約95%の幅 |
|---|---|---|---|
| Firefox翻訳 − Shisa350M | COMET-QE | 0.009 | -0.084 〜 0.102 |
| Firefox翻訳 − Shisa350M | LLM 総合 | 0.80 | -0.29 〜 1.89 |
| Firefox翻訳 − Shisa350M厳 | COMET-QE | 0.156 | 0.005 〜 0.307 |
| Firefox翻訳 − Shisa350M厳 | LLM 総合 | 1.03 | -0.14 〜 2.21 |
| Firefox翻訳 − CAT-Translate 0.8B | COMET-QE | -0.034 | -0.085 〜 0.017 |
| Firefox翻訳 − CAT-Translate 0.8B | LLM 総合 ※判定の回が違う | -1.17 | -1.82 〜 -0.51 |
| Firefox翻訳 − CAT-Translate 1.4B | COMET-QE | -0.056 | -0.106 〜 -0.007 |
| Firefox翻訳 − CAT-Translate 1.4B | LLM 総合 ※判定の回が違う | -0.20 | -1.03 〜 0.63 |
| Shisa350M − Shisa350M厳 | COMET-QE | 0.147 | 0.005 〜 0.289 |
| Shisa350M − Shisa350M厳 | LLM 総合 | 0.23 | -0.43 〜 0.90 |
| Shisa350M − CAT-Translate 0.8B | COMET-QE | -0.043 | -0.126 〜 0.040 |
| Shisa350M − CAT-Translate 0.8B | LLM 総合 ※判定の回が違う | -1.97 | -2.92 〜 -1.01 |
| Shisa350M − CAT-Translate 1.4B | COMET-QE | -0.065 | -0.144 〜 0.013 |
| Shisa350M − CAT-Translate 1.4B | LLM 総合 ※判定の回が違う | -1.00 | -2.16 〜 0.16 |
| Shisa350M厳 − CAT-Translate 0.8B | COMET-QE | -0.190 | -0.325 〜 -0.055 |
| Shisa350M厳 − CAT-Translate 0.8B | LLM 総合 ※判定の回が違う | -2.20 | -3.18 〜 -1.22 |
| Shisa350M厳 − CAT-Translate 1.4B | COMET-QE | -0.212 | -0.355 〜 -0.070 |
| Shisa350M厳 − CAT-Translate 1.4B | LLM 総合 ※判定の回が違う | -1.23 | -2.39 〜 -0.08 |
| CAT-Translate 0.8B − CAT-Translate 1.4B | COMET-QE | -0.022 | -0.056 〜 0.011 |
| CAT-Translate 0.8B − CAT-Translate 1.4B | LLM 総合 | 0.97 | 0.34 〜 1.59 |

