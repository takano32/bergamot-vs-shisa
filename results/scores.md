# 採点の結果（COMET-QE と LLM 判定）

COMET-QE は `results/comet.jsonl`、LLM 判定は `results/llm_judge.jsonl`。判定の基準は README の「採点の基準」。

## 全体の平均（30文）

| 系 | COMET-QE（訳のまま） | COMET-QE（注釈を切った先頭行） | LLM 正確さ | LLM 自然さ | LLM 注釈減点 | LLM 総合 |
|---|---|---|---|---|---|---|
| Firefox翻訳 | 0.294 | 0.294 | 4.20 | 3.97 | 0.00 | 8.17 |
| Shisa350M | 0.285 | 0.332 | 3.80 | 3.77 | -0.20 | 7.37 |
| Shisa350M厳 | 0.138 | 0.361 | 3.97 | 3.70 | -0.53 | 7.13 |

## 方向別、種類別、方向×種類の平均

| 群 | n | Firefox翻訳 COMET / LLM 総合 | Shisa350M COMET / LLM 総合 | Shisa350M厳 COMET / LLM 総合 |
|---|---|---|---|---|
| en→ja | 15 | 0.353 / 8.27 | 0.339 / 8.07 | 0.110 / 8.00 |
| ja→en | 15 | 0.235 / 8.07 | 0.231 / 6.67 | 0.167 / 6.27 |
| 技術文 | 10 | 0.198 / 8.40 | 0.139 / 7.30 | 0.085 / 7.80 |
| 会話 | 10 | 0.200 / 7.30 | 0.308 / 6.70 | 0.309 / 6.50 |
| Web記事風 | 10 | 0.485 / 8.80 | 0.409 / 8.10 | 0.021 / 7.10 |
| en→ja 技術文 | 5 | 0.242 / 8.40 | 0.190 / 7.80 | 0.141 / 8.20 |
| en→ja 会話 | 5 | 0.305 / 7.80 | 0.284 / 9.00 | 0.283 / 8.40 |
| en→ja Web記事風 | 5 | 0.513 / 8.60 | 0.543 / 7.40 | -0.095 / 7.40 |
| ja→en 技術文 | 5 | 0.153 / 8.40 | 0.087 / 6.80 | 0.029 / 7.40 |
| ja→en 会話 | 5 | 0.096 / 6.80 | 0.331 / 4.40 | 0.336 / 4.60 |
| ja→en Web記事風 | 5 | 0.457 / 9.00 | 0.275 / 8.80 | 0.136 / 6.80 |

## 文ごとの点

COMET は訳のまま。LLM は 正確さ/自然さ/注釈減点 の総合。最良は、その指標で一番高い系（同点は「=」）。

| id | 向き | 種類 | Firefox翻訳 COMET | Shisa350M COMET | Shisa350M厳 COMET | Firefox翻訳 LLM | Shisa350M LLM | Shisa350M厳 LLM | COMET 最良 | LLM 最良 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | en→ja | tech | 0.202 | -0.023 | 0.180 | 8 | 6 | 9 | Firefox翻訳 | Shisa350M厳 |
| 2 | en→ja | tech | 0.361 | 0.523 | 0.523 | 9 | 9 | 9 | Shisa350M / Shisa350M厳 | Firefox翻訳 / Shisa350M / Shisa350M厳 （同点含む） |
| 3 | en→ja | tech | 0.379 | 0.248 | -0.176 | 6 | 9 | 8 | Firefox翻訳 | Shisa350M |
| 4 | en→ja | tech | -0.168 | -0.059 | 0.005 | 9 | 10 | 10 | Shisa350M厳 | Shisa350M / Shisa350M厳 （同点含む） |
| 5 | en→ja | tech | 0.438 | 0.263 | 0.172 | 10 | 5 | 5 | Firefox翻訳 | Firefox翻訳 |
| 6 | en→ja | conv | 0.313 | 0.067 | 0.391 | 9 | 9 | 8 | Shisa350M厳 | Firefox翻訳 / Shisa350M （同点含む） |
| 7 | en→ja | conv | 0.268 | 0.238 | -0.082 | 9 | 8 | 8 | Firefox翻訳 | Firefox翻訳 |
| 8 | en→ja | conv | 0.009 | 0.351 | 0.156 | 5 | 9 | 6 | Shisa350M | Shisa350M |
| 9 | en→ja | conv | 0.373 | 0.180 | 0.381 | 9 | 9 | 10 | Shisa350M厳 | Shisa350M厳 |
| 10 | en→ja | conv | 0.561 | 0.585 | 0.570 | 7 | 10 | 10 | Shisa350M | Shisa350M / Shisa350M厳 （同点含む） |
| 11 | en→ja | web | 0.664 | 0.648 | 0.353 | 10 | 7 | 9 | Firefox翻訳 | Firefox翻訳 |
| 12 | en→ja | web | 0.421 | 0.595 | 0.573 | 8 | 8 | 9 | Shisa350M | Shisa350M厳 |
| 13 | en→ja | web | 0.526 | 0.323 | -0.896 | 8 | 8 | 7 | Firefox翻訳 | Firefox翻訳 / Shisa350M （同点含む） |
| 14 | en→ja | web | 0.353 | 0.555 | -0.241 | 7 | 6 | 5 | Shisa350M | Firefox翻訳 |
| 15 | en→ja | web | 0.603 | 0.593 | -0.265 | 10 | 8 | 7 | Firefox翻訳 | Firefox翻訳 |
| 16 | ja→en | tech | 0.021 | 0.209 | 0.046 | 5 | 6 | 8 | Shisa350M | Shisa350M厳 |
| 17 | ja→en | tech | 0.348 | 0.273 | 0.145 | 10 | 7 | 7 | Firefox翻訳 | Firefox翻訳 |
| 18 | ja→en | tech | 0.264 | 0.156 | 0.137 | 10 | 7 | 9 | Firefox翻訳 | Firefox翻訳 |
| 19 | ja→en | tech | -0.181 | -0.437 | -0.287 | 7 | 10 | 9 | Firefox翻訳 | Shisa350M |
| 20 | ja→en | tech | 0.313 | 0.236 | 0.103 | 10 | 4 | 4 | Firefox翻訳 | Firefox翻訳 |
| 21 | ja→en | conv | -0.047 | 0.174 | 0.119 | 8 | 6 | 5 | Shisa350M | Firefox翻訳 |
| 22 | ja→en | conv | -0.040 | -0.068 | -0.005 | 5 | 3 | 5 | Shisa350M厳 | Firefox翻訳 / Shisa350M厳 （同点含む） |
| 23 | ja→en | conv | 0.229 | 0.305 | 0.344 | 8 | 2 | 2 | Shisa350M厳 | Firefox翻訳 |
| 24 | ja→en | conv | 0.021 | 0.365 | 0.365 | 4 | 9 | 9 | Shisa350M / Shisa350M厳 | Shisa350M / Shisa350M厳 （同点含む） |
| 25 | ja→en | conv | 0.316 | 0.881 | 0.855 | 9 | 2 | 2 | Shisa350M | Firefox翻訳 |
| 26 | ja→en | web | 0.530 | 0.288 | 0.258 | 9 | 8 | 7 | Firefox翻訳 | Firefox翻訳 |
| 27 | ja→en | web | 0.489 | 0.668 | 0.668 | 8 | 10 | 10 | Shisa350M / Shisa350M厳 | Shisa350M / Shisa350M厳 （同点含む） |
| 28 | ja→en | web | 0.460 | 0.506 | 0.191 | 8 | 10 | 8 | Shisa350M | Shisa350M |
| 29 | ja→en | web | 0.215 | 0.159 | -0.822 | 10 | 8 | 1 | Firefox翻訳 | Firefox翻訳 |
| 30 | ja→en | web | 0.593 | -0.244 | 0.386 | 10 | 8 | 8 | Firefox翻訳 | Firefox翻訳 |

## COMET と LLM 判定の食い違い

判定の定義: 同じ文の2系で、LLM 総合の差が 2 点以上あるのに、COMET の差の向きが逆のもの（COMET 同点は除く）。

- 向きが逆になった組は全部で 19 組（90 組のうち）。そのうち LLM の差が 2 点以上のものが下の 13 組。

| id | 向き | 種類 | 組 | LLM 総合の差（左−右） | COMET の差（左−右） |
|---|---|---|---|---|---|
| 3 | en→ja | tech | Firefox翻訳 と Shisa350M | -3 | +0.131 |
| 3 | en→ja | tech | Firefox翻訳 と Shisa350M厳 | -2 | +0.554 |
| 11 | en→ja | web | Shisa350M と Shisa350M厳 | -2 | +0.296 |
| 16 | ja→en | tech | Shisa350M と Shisa350M厳 | -2 | +0.163 |
| 18 | ja→en | tech | Shisa350M と Shisa350M厳 | -2 | +0.019 |
| 19 | ja→en | tech | Firefox翻訳 と Shisa350M | -3 | +0.257 |
| 19 | ja→en | tech | Firefox翻訳 と Shisa350M厳 | -2 | +0.107 |
| 21 | ja→en | conv | Firefox翻訳 と Shisa350M | +2 | -0.222 |
| 21 | ja→en | conv | Firefox翻訳 と Shisa350M厳 | +3 | -0.167 |
| 23 | ja→en | conv | Firefox翻訳 と Shisa350M | +6 | -0.076 |
| 23 | ja→en | conv | Firefox翻訳 と Shisa350M厳 | +6 | -0.115 |
| 25 | ja→en | conv | Firefox翻訳 と Shisa350M | +7 | -0.565 |
| 25 | ja→en | conv | Firefox翻訳 と Shisa350M厳 | +7 | -0.539 |

## 注釈を切ると COMET はどう変わるか

「注釈のある文数」は、訳の後ろに空でない行が続く出力の数。`comet_qe_first_line` から `comet_qe` を引いた平均は、先頭行だけの採点との差（0 に近いほど、注釈の有無が COMET に効いていない）。

| 系 | 注釈のある文数 | 平均の差（先頭行−訳のまま） |
|---|---|---|
| Firefox翻訳 | 0 | 0.0000 |
| Shisa350M | 6 | 0.0466 |
| Shisa350M厳 | 16 | 0.2227 |

## 系どうしの差の目安（文の対応をとった差）

差の平均と、その標準誤差の2倍（約95%の幅）。幅が0をまたぐ差は、30文では区別できていない。

| 組 | 指標 | 平均の差（左−右） | 約95%の幅 |
|---|---|---|---|
| Firefox翻訳 − Shisa350M | COMET-QE | 0.009 | -0.084 〜 0.102 |
| Firefox翻訳 − Shisa350M | LLM 総合 | 0.80 | -0.29 〜 1.89 |
| Firefox翻訳 − Shisa350M厳 | COMET-QE | 0.156 | 0.005 〜 0.307 |
| Firefox翻訳 − Shisa350M厳 | LLM 総合 | 1.03 | -0.14 〜 2.21 |
| Shisa350M − Shisa350M厳 | COMET-QE | 0.147 | 0.005 〜 0.289 |
| Shisa350M − Shisa350M厳 | LLM 総合 | 0.23 | -0.43 〜 0.90 |

