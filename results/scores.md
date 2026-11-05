# 採点の結果（COMET-QE と LLM 判定、100文）

COMET-QE は `results/comet.jsonl`、LLM 判定は `results/llm_judge.jsonl`。判定の基準は README の「採点の基準」。
LLM 判定は、5系を1回でまとめて、系の名前を伏せ、文ごとに並びを入れ替えて付けた（判定役は1人・1セッション）。

## 網羅の表（文の本数）

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

## 全体の平均（100文）

| 系 | COMET-QE（訳のまま） | COMET-QE（注釈を切った先頭行） | LLM 正確さ | LLM 自然さ | LLM 注釈減点 | LLM 総合 |
|---|---|---|---|---|---|---|
| Firefox翻訳 | 0.235 | 0.235 | 3.83 | 3.73 | 0.00 | 7.56 |
| Shisa350M | 0.238 | 0.305 | 3.18 | 3.34 | -0.35 | 6.17 |
| Shisa350M厳 | 0.045 | 0.341 | 2.64 | 2.74 | -0.67 | 4.71 |
| CAT 0.8B | 0.333 | 0.333 | 4.42 | 4.34 | 0.00 | 8.76 |
| CAT 1.4B | 0.367 | 0.367 | 4.44 | 4.36 | 0.00 | 8.80 |

## 方向別

各セルは「LLM 総合 / COMET-QE（訳のまま）」の平均。

| 群 | n | Firefox翻訳 | Shisa350M | Shisa350M厳 | CAT 0.8B | CAT 1.4B |
|---|---|---|---|---|---|---|
| en→ja | 50 | 7.44 / 0.296 | 6.58 / 0.208 | 6.00 / -0.027 | 8.86 / 0.365 | 9.00 / 0.430 |
| ja→en | 50 | 7.68 / 0.175 | 5.76 / 0.268 | 3.42 / 0.117 | 8.66 / 0.301 | 8.60 / 0.304 |

## 分野別

各セルは「LLM 総合 / COMET-QE（訳のまま）」の平均。

| 群 | n | Firefox翻訳 | Shisa350M | Shisa350M厳 | CAT 0.8B | CAT 1.4B |
|---|---|---|---|---|---|---|
| 技術文書（tech） | 10 | 7.40 / 0.001 | 7.30 / 0.102 | 6.70 / 0.115 | 8.50 / 0.006 | 8.70 / 0.106 |
| UI の文言（ui） | 10 | 7.80 / 0.243 | 6.70 / 0.262 | 4.80 / 0.184 | 9.70 / 0.280 | 9.20 / 0.219 |
| ニュース（news） | 10 | 8.80 / 0.479 | 5.40 / 0.286 | 4.10 / -0.163 | 9.20 / 0.530 | 9.00 / 0.516 |
| Web 記事・ブログ（web） | 10 | 7.20 / 0.278 | 5.70 / 0.378 | 4.80 / 0.271 | 8.80 / 0.406 | 9.20 / 0.492 |
| ビジネスメール（biz） | 10 | 6.80 / 0.260 | 5.90 / 0.212 | 4.70 / 0.138 | 8.00 / 0.356 | 7.70 / 0.341 |
| くだけた会話（casual） | 10 | 7.00 / 0.051 | 6.40 / 0.105 | 5.10 / -0.105 | 8.80 / 0.083 | 8.40 / 0.190 |
| 接客・丁寧な会話（polite） | 10 | 7.60 / 0.237 | 7.20 / 0.302 | 3.90 / 0.075 | 8.70 / 0.445 | 8.60 / 0.439 |
| 法律・規約（legal） | 10 | 9.20 / 0.497 | 5.60 / 0.399 | 4.20 / -0.067 | 8.30 / 0.501 | 9.30 / 0.530 |
| 文学的な文（lit） | 10 | 7.90 / 0.308 | 6.20 / 0.194 | 5.00 / -0.015 | 8.80 / 0.414 | 9.60 / 0.465 |
| SNS の短文（sns） | 10 | 5.90 / -0.001 | 5.30 / 0.142 | 3.80 / 0.016 | 8.80 / 0.309 | 8.30 / 0.370 |

## 現象別（1文に複数のタグがつくので、群は重なる）

各セルは「LLM 総合 / COMET-QE（訳のまま）」の平均。

| 群 | n | Firefox翻訳 | Shisa350M | Shisa350M厳 | CAT 0.8B | CAT 1.4B |
|---|---|---|---|---|---|---|
| 敬語・丁寧さ（hon） | 21 | 7.95 / 0.270 | 6.43 / 0.324 | 3.71 / 0.173 | 8.57 / 0.424 | 8.43 / 0.417 |
| 主語の省略（pro） | 32 | 7.38 / 0.089 | 5.75 / 0.294 | 2.97 / 0.114 | 8.56 / 0.269 | 8.53 / 0.288 |
| 慣用句・口語表現（idm） | 23 | 6.61 / 0.099 | 5.52 / 0.190 | 4.74 / 0.081 | 8.26 / 0.271 | 8.30 / 0.358 |
| 数字・日付・単位（num） | 26 | 7.31 / 0.292 | 6.15 / 0.341 | 5.12 / 0.090 | 9.12 / 0.430 | 8.77 / 0.410 |
| 固有名詞（prop） | 11 | 7.73 / 0.337 | 4.27 / 0.252 | 3.82 / -0.163 | 8.55 / 0.451 | 8.64 / 0.471 |
| 多義語（poly） | 11 | 7.55 / 0.187 | 7.18 / 0.118 | 5.91 / 0.034 | 9.18 / 0.264 | 9.09 / 0.283 |
| 否定（neg） | 24 | 7.96 / 0.281 | 5.83 / 0.312 | 4.75 / 0.028 | 9.08 / 0.339 | 9.08 / 0.394 |
| 疑問（q） | 17 | 6.82 / 0.075 | 6.59 / 0.078 | 5.00 / -0.090 | 8.76 / 0.163 | 9.06 / 0.217 |
| 長文（long） | 11 | 7.82 / 0.170 | 6.55 / 0.174 | 6.09 / 0.038 | 8.09 / 0.191 | 9.09 / 0.203 |
| 短い断片（frag） | 17 | 7.88 / 0.146 | 6.24 / 0.185 | 3.71 / -0.025 | 9.41 / 0.251 | 9.29 / 0.287 |
| コード・記号混じり（code） | 9 | 6.89 / -0.036 | 6.22 / -0.019 | 5.11 / -0.038 | 8.22 / -0.047 | 8.44 / 0.105 |
| Markdown（md） | 7 | 8.29 / 0.385 | 7.00 / 0.240 | 6.86 / 0.077 | 8.71 / 0.394 | 8.86 / 0.424 |

## 文ごとの点

COMET は訳のまま。LLM は 正確さ + 自然さ + 注釈減点。最良は、その指標で一番高い系（同点は並べる）。

| id | 向き | 分野 | Firefox翻訳 COMET | Shisa350M COMET | Shisa350M厳 COMET | CAT 0.8B COMET | CAT 1.4B COMET | Firefox翻訳 LLM | Shisa350M LLM | Shisa350M厳 LLM | CAT 0.8B LLM | CAT 1.4B LLM | COMET 最良 | LLM 最良 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | en→ja | tech | 0.249 | 0.310 | 0.300 | 0.276 | 0.352 | 6 | 10 | 10 | 8 | 7 | CAT 1.4B | Shisa350M / Shisa350M厳 |
| 2 | en→ja | tech | -0.015 | 0.239 | 0.233 | 0.172 | 0.298 | 8 | 8 | 7 | 10 | 7 | CAT 1.4B | CAT 0.8B |
| 3 | en→ja | tech | -0.334 | -0.115 | -0.255 | -0.313 | 0.110 | 4 | 7 | 7 | 7 | 9 | CAT 1.4B | CAT 1.4B |
| 4 | en→ja | tech | -0.089 | -0.118 | -0.161 | -0.226 | -0.213 | 5 | 8 | 10 | 7 | 10 | Firefox翻訳 | Shisa350M厳 / CAT 1.4B |
| 5 | en→ja | tech | 0.064 | 0.196 | 0.164 | -0.045 | 0.198 | 10 | 5 | 5 | 10 | 10 | CAT 1.4B | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 6 | en→ja | ui | 0.268 | -0.068 | -0.315 | 0.006 | -0.257 | 7 | 5 | 4 | 10 | 10 | Firefox翻訳 | CAT 0.8B / CAT 1.4B |
| 7 | en→ja | ui | 0.249 | 0.327 | -0.411 | 0.290 | 0.327 | 7 | 7 | 4 | 10 | 7 | Shisa350M / CAT 1.4B | CAT 0.8B |
| 8 | en→ja | ui | 0.376 | 0.264 | 0.175 | 0.441 | 0.181 | 7 | 5 | 3 | 10 | 8 | CAT 0.8B | CAT 0.8B |
| 9 | en→ja | ui | 0.662 | 0.643 | 0.643 | 0.723 | 0.720 | 7 | 10 | 10 | 9 | 9 | CAT 0.8B | Shisa350M / Shisa350M厳 |
| 10 | en→ja | ui | 0.418 | 0.070 | 0.565 | 0.448 | 0.477 | 10 | 6 | 8 | 9 | 10 | Shisa350M厳 | Firefox翻訳 / CAT 1.4B |
| 11 | en→ja | news | 0.536 | 0.563 | -0.178 | 0.662 | 0.628 | 9 | 5 | 4 | 10 | 9 | CAT 0.8B | CAT 0.8B |
| 12 | en→ja | news | 0.598 | 0.152 | -1.272 | 0.659 | 0.655 | 10 | 4 | 4 | 10 | 10 | CAT 0.8B | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 13 | en→ja | news | 0.636 | 0.540 | -0.229 | 0.608 | 0.654 | 10 | 8 | 4 | 10 | 10 | CAT 1.4B | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 14 | en→ja | news | 0.279 | -0.150 | -0.187 | 0.493 | 0.515 | 7 | 3 | 3 | 7 | 7 | CAT 1.4B | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 15 | en→ja | news | 0.417 | 0.564 | 0.183 | 0.552 | 0.491 | 10 | 9 | 5 | 10 | 10 | Shisa350M | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 16 | en→ja | web | 0.460 | 0.355 | 0.287 | 0.523 | 0.630 | 8 | 6 | 6 | 9 | 10 | CAT 1.4B | CAT 1.4B |
| 17 | en→ja | web | 0.338 | 0.492 | 0.527 | 0.425 | 0.496 | 5 | 9 | 9 | 8 | 10 | Shisa350M厳 | CAT 1.4B |
| 18 | en→ja | web | 0.712 | 0.240 | -0.620 | 0.731 | 0.676 | 8 | 8 | 9 | 10 | 10 | CAT 0.8B | CAT 0.8B / CAT 1.4B |
| 19 | en→ja | web | 0.094 | -0.497 | -0.515 | 0.253 | 0.394 | 7 | 5 | 4 | 8 | 9 | CAT 1.4B | CAT 1.4B |
| 20 | en→ja | web | 0.312 | 0.211 | -0.396 | 0.212 | 0.482 | 7 | 6 | 5 | 9 | 10 | CAT 1.4B | CAT 1.4B |
| 21 | en→ja | biz | 0.548 | 0.482 | 0.466 | 0.622 | 0.551 | 9 | 7 | 5 | 10 | 9 | CAT 0.8B | CAT 0.8B |
| 22 | en→ja | biz | 0.323 | 0.459 | -0.274 | 0.459 | 0.548 | 6 | 7 | 6 | 9 | 10 | CAT 1.4B | CAT 1.4B |
| 23 | en→ja | biz | 0.480 | 0.410 | 0.121 | 0.452 | 0.437 | 10 | 6 | 4 | 8 | 7 | Firefox翻訳 | Firefox翻訳 |
| 24 | en→ja | biz | 0.261 | 0.018 | -0.192 | 0.412 | 0.252 | 6 | 4 | 5 | 8 | 8 | CAT 0.8B | CAT 0.8B / CAT 1.4B |
| 25 | en→ja | biz | 0.295 | 0.438 | 0.438 | 0.288 | 0.357 | 3 | 10 | 10 | 8 | 9 | Shisa350M / Shisa350M厳 | Shisa350M / Shisa350M厳 |
| 26 | en→ja | casual | 0.391 | 0.055 | 0.055 | 0.406 | 0.510 | 8 | 7 | 7 | 10 | 10 | CAT 1.4B | CAT 0.8B / CAT 1.4B |
| 27 | en→ja | casual | 0.413 | 0.366 | -0.749 | 0.423 | 0.448 | 6 | 8 | 7 | 10 | 10 | CAT 1.4B | CAT 0.8B / CAT 1.4B |
| 28 | en→ja | casual | 0.140 | 0.443 | 0.443 | 0.531 | 0.551 | 7 | 8 | 8 | 9 | 5 | CAT 1.4B | CAT 0.8B |
| 29 | en→ja | casual | -0.027 | -0.288 | -0.295 | -0.217 | 0.021 | 10 | 5 | 5 | 7 | 10 | CAT 1.4B | Firefox翻訳 / CAT 1.4B |
| 30 | en→ja | casual | -0.256 | -0.284 | -0.048 | -0.317 | -0.002 | 4 | 6 | 7 | 7 | 7 | CAT 1.4B | Shisa350M厳 / CAT 0.8B / CAT 1.4B |
| 31 | en→ja | polite | 0.510 | 0.377 | 0.297 | 0.510 | 0.570 | 9 | 6 | 5 | 8 | 8 | CAT 1.4B | Firefox翻訳 |
| 32 | en→ja | polite | -0.288 | 0.255 | 0.425 | 0.355 | 0.348 | 5 | 4 | 6 | 10 | 10 | Shisa350M厳 | CAT 0.8B / CAT 1.4B |
| 33 | en→ja | polite | 0.649 | 0.416 | -0.155 | 0.730 | 0.730 | 10 | 7 | 8 | 10 | 10 | CAT 0.8B / CAT 1.4B | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 34 | en→ja | polite | 0.378 | 0.496 | 0.386 | 0.517 | 0.524 | 5 | 9 | 5 | 10 | 10 | CAT 1.4B | CAT 0.8B / CAT 1.4B |
| 35 | en→ja | polite | -0.046 | -0.105 | 0.459 | 0.485 | 0.485 | 3 | 8 | 10 | 10 | 10 | CAT 0.8B / CAT 1.4B | Shisa350M厳 / CAT 0.8B / CAT 1.4B |
| 36 | en→ja | legal | 0.327 | 0.449 | -0.444 | 0.363 | 0.568 | 10 | 4 | 3 | 9 | 7 | CAT 1.4B | Firefox翻訳 |
| 37 | en→ja | legal | 0.622 | 0.547 | -0.027 | 0.509 | 0.513 | 10 | 7 | 5 | 7 | 9 | Firefox翻訳 | Firefox翻訳 |
| 38 | en→ja | legal | 0.435 | 0.549 | 0.073 | 0.623 | 0.569 | 6 | 5 | 6 | 6 | 10 | CAT 0.8B | CAT 1.4B |
| 39 | en→ja | legal | 0.470 | 0.340 | -0.339 | 0.338 | 0.450 | 10 | 4 | 4 | 8 | 10 | Firefox翻訳 | Firefox翻訳 / CAT 1.4B |
| 40 | en→ja | legal | 0.572 | 0.488 | 0.165 | 0.647 | 0.584 | 10 | 8 | 6 | 10 | 10 | CAT 0.8B | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 41 | en→ja | lit | 0.607 | 0.457 | 0.324 | 0.296 | 0.602 | 8 | 7 | 6 | 10 | 9 | Firefox翻訳 | CAT 0.8B |
| 42 | en→ja | lit | 0.282 | 0.333 | 0.446 | 0.540 | 0.371 | 8 | 6 | 7 | 10 | 10 | CAT 0.8B | CAT 0.8B / CAT 1.4B |
| 43 | en→ja | lit | 0.439 | -0.400 | -0.265 | 0.391 | 0.571 | 10 | 5 | 6 | 10 | 9 | CAT 1.4B | Firefox翻訳 / CAT 0.8B |
| 44 | en→ja | lit | 0.642 | -0.059 | -0.624 | 0.577 | 0.657 | 7 | 8 | 7 | 8 | 10 | CAT 1.4B | CAT 1.4B |
| 45 | en→ja | lit | 0.266 | 0.067 | -0.085 | 0.308 | 0.445 | 7 | 7 | 6 | 9 | 9 | CAT 1.4B | CAT 0.8B / CAT 1.4B |
| 46 | en→ja | sns | 0.044 | -0.158 | -0.089 | 0.433 | 0.432 | 6 | 6 | 4 | 10 | 8 | CAT 0.8B | CAT 0.8B |
| 47 | en→ja | sns | -0.418 | 0.172 | -0.091 | 0.226 | 0.444 | 3 | 4 | 3 | 8 | 9 | CAT 1.4B | CAT 1.4B |
| 48 | en→ja | sns | -0.294 | -0.326 | -0.047 | -0.089 | 0.293 | 10 | 9 | 3 | 9 | 9 | CAT 1.4B | Firefox翻訳 |
| 49 | en→ja | sns | 0.612 | 0.568 | -0.078 | 0.611 | 0.602 | 10 | 10 | 8 | 10 | 9 | Firefox翻訳 | Firefox翻訳 / Shisa350M / CAT 0.8B |
| 50 | en→ja | sns | 0.185 | -0.378 | -0.197 | -0.079 | 0.252 | 4 | 3 | 7 | 4 | 7 | CAT 1.4B | Shisa350M厳 / CAT 1.4B |
| 51 | ja→en | tech | 0.482 | 0.546 | 0.938 | 0.581 | 0.573 | 10 | 10 | 2 | 9 | 8 | Shisa350M厳 | Firefox翻訳 / Shisa350M |
| 52 | ja→en | tech | -0.243 | -0.155 | -0.160 | -0.354 | -0.361 | 10 | 7 | 5 | 10 | 10 | Shisa350M | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 53 | ja→en | tech | 0.155 | 0.394 | 0.310 | 0.397 | 0.398 | 7 | 7 | 7 | 10 | 9 | CAT 1.4B | CAT 0.8B |
| 54 | ja→en | tech | -0.149 | -0.154 | -0.149 | -0.273 | -0.261 | 7 | 7 | 7 | 7 | 7 | Firefox翻訳 | Firefox翻訳 / Shisa350M / Shisa350M厳 / CAT 0.8B / CAT 1.4B |
| 55 | ja→en | tech | -0.107 | -0.124 | -0.075 | -0.158 | -0.032 | 7 | 4 | 7 | 7 | 10 | CAT 1.4B | CAT 1.4B |
| 56 | ja→en | ui | -0.604 | -0.078 | 0.121 | -0.592 | -0.592 | 10 | 8 | 1 | 10 | 10 | Shisa350M厳 | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 57 | ja→en | ui | 0.668 | 0.645 | 0.631 | 0.704 | 0.704 | 9 | 9 | 8 | 10 | 10 | CAT 0.8B / CAT 1.4B | CAT 0.8B / CAT 1.4B |
| 58 | ja→en | ui | 0.364 | 0.434 | 0.296 | 0.465 | 0.437 | 8 | 10 | 8 | 9 | 10 | CAT 0.8B | Shisa350M / CAT 1.4B |
| 59 | ja→en | ui | -0.326 | 0.175 | -0.055 | -0.100 | -0.163 | 3 | 1 | 1 | 10 | 8 | Shisa350M | CAT 0.8B |
| 60 | ja→en | ui | 0.354 | 0.208 | 0.188 | 0.416 | 0.354 | 10 | 6 | 1 | 10 | 10 | CAT 0.8B | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 61 | ja→en | news | 0.560 | 0.518 | 0.445 | 0.558 | 0.574 | 9 | 6 | 5 | 10 | 9 | CAT 1.4B | CAT 0.8B |
| 62 | ja→en | news | 0.510 | 0.216 | 0.229 | 0.458 | 0.458 | 6 | 4 | 7 | 10 | 10 | Firefox翻訳 | CAT 0.8B / CAT 1.4B |
| 63 | ja→en | news | 0.414 | 0.309 | -0.292 | 0.263 | 0.277 | 10 | 8 | 4 | 8 | 8 | Firefox翻訳 | Firefox翻訳 |
| 64 | ja→en | news | 0.405 | 0.413 | 0.248 | 0.508 | 0.457 | 7 | 4 | 4 | 8 | 9 | CAT 0.8B | CAT 1.4B |
| 65 | ja→en | news | 0.434 | -0.266 | -0.576 | 0.539 | 0.448 | 10 | 3 | 1 | 9 | 8 | CAT 0.8B | Firefox翻訳 |
| 66 | ja→en | web | 0.251 | 0.259 | 0.385 | 0.482 | 0.450 | 7 | 7 | 7 | 8 | 8 | CAT 0.8B | CAT 0.8B / CAT 1.4B |
| 67 | ja→en | web | 0.205 | 0.734 | 0.734 | 0.283 | 0.458 | 8 | 2 | 2 | 7 | 8 | Shisa350M / Shisa350M厳 | Firefox翻訳 / CAT 1.4B |
| 68 | ja→en | web | 0.202 | 0.538 | 0.865 | 0.510 | 0.519 | 6 | 10 | 2 | 10 | 10 | Shisa350M厳 | Shisa350M / CAT 0.8B / CAT 1.4B |
| 69 | ja→en | web | 0.152 | 0.731 | 0.765 | 0.425 | 0.350 | 9 | 2 | 2 | 10 | 8 | Shisa350M厳 | CAT 0.8B |
| 70 | ja→en | web | 0.055 | 0.714 | 0.681 | 0.211 | 0.467 | 7 | 2 | 2 | 9 | 9 | Shisa350M | CAT 0.8B / CAT 1.4B |
| 71 | ja→en | biz | 0.258 | 0.278 | 0.085 | 0.410 | 0.403 | 7 | 1 | 1 | 8 | 8 | CAT 0.8B | CAT 0.8B / CAT 1.4B |
| 72 | ja→en | biz | -0.039 | -0.271 | 0.534 | 0.182 | 0.415 | 5 | 3 | 1 | 7 | 8 | Shisa350M厳 | CAT 1.4B |
| 73 | ja→en | biz | -0.148 | 0.366 | 0.040 | 0.092 | 0.190 | 5 | 9 | 4 | 6 | 7 | Shisa350M | Shisa350M |
| 74 | ja→en | biz | 0.446 | -0.054 | 0.117 | 0.383 | -0.027 | 10 | 7 | 6 | 7 | 3 | Firefox翻訳 | Firefox翻訳 |
| 75 | ja→en | biz | 0.178 | -0.008 | 0.046 | 0.256 | 0.283 | 7 | 5 | 5 | 9 | 8 | CAT 1.4B | CAT 0.8B |
| 76 | ja→en | casual | -0.147 | -0.075 | -0.102 | -0.116 | -0.012 | 6 | 7 | 7 | 9 | 8 | CAT 1.4B | CAT 0.8B |
| 77 | ja→en | casual | 0.271 | 0.152 | -0.537 | 0.195 | 0.251 | 8 | 10 | 1 | 10 | 10 | Firefox翻訳 | Shisa350M / CAT 0.8B / CAT 1.4B |
| 78 | ja→en | casual | 0.121 | 0.426 | 0.493 | 0.075 | 0.155 | 5 | 2 | 2 | 10 | 7 | Shisa350M厳 | CAT 0.8B |
| 79 | ja→en | casual | -0.413 | 0.222 | -0.212 | -0.213 | -0.194 | 7 | 2 | 6 | 6 | 9 | Shisa350M | CAT 1.4B |
| 80 | ja→en | casual | 0.013 | 0.030 | -0.097 | 0.062 | 0.176 | 9 | 9 | 1 | 10 | 8 | CAT 1.4B | CAT 0.8B |
| 81 | ja→en | polite | -0.040 | 0.111 | 0.110 | 0.216 | 0.133 | 7 | 10 | 1 | 8 | 10 | CAT 0.8B | Shisa350M / CAT 1.4B |
| 82 | ja→en | polite | 0.607 | 0.586 | -0.068 | 0.972 | 0.852 | 9 | 9 | 1 | 2 | 2 | CAT 0.8B | Firefox翻訳 / Shisa350M |
| 83 | ja→en | polite | -0.431 | -0.081 | -0.322 | -0.415 | -0.372 | 9 | 3 | 1 | 10 | 8 | Shisa350M | CAT 0.8B |
| 84 | ja→en | polite | 0.600 | 0.616 | 0.127 | 0.606 | 0.596 | 9 | 9 | 1 | 10 | 10 | Shisa350M | CAT 0.8B / CAT 1.4B |
| 85 | ja→en | polite | 0.432 | 0.353 | -0.506 | 0.476 | 0.522 | 10 | 7 | 1 | 9 | 8 | CAT 1.4B | Firefox翻訳 |
| 86 | ja→en | legal | 0.502 | 0.230 | 0.260 | 0.530 | 0.532 | 9 | 6 | 6 | 8 | 10 | CAT 1.4B | CAT 1.4B |
| 87 | ja→en | legal | 0.556 | 0.376 | 0.056 | 0.619 | 0.568 | 10 | 6 | 1 | 10 | 10 | CAT 0.8B | Firefox翻訳 / CAT 0.8B / CAT 1.4B |
| 88 | ja→en | legal | 0.543 | 0.279 | 0.260 | 0.537 | 0.559 | 10 | 4 | 5 | 8 | 10 | CAT 1.4B | Firefox翻訳 / CAT 1.4B |
| 89 | ja→en | legal | 0.495 | 0.414 | -0.452 | 0.539 | 0.473 | 7 | 5 | 1 | 10 | 10 | CAT 0.8B | CAT 0.8B / CAT 1.4B |
| 90 | ja→en | legal | 0.453 | 0.314 | -0.217 | 0.307 | 0.484 | 10 | 7 | 5 | 7 | 7 | CAT 1.4B | Firefox翻訳 |
| 91 | ja→en | lit | 0.535 | 0.080 | 0.205 | 0.547 | 0.615 | 10 | 9 | 7 | 10 | 9 | CAT 1.4B | Firefox翻訳 / CAT 0.8B |
| 92 | ja→en | lit | 0.649 | 0.859 | -0.298 | 0.648 | 0.636 | 10 | 2 | 1 | 9 | 10 | Shisa350M | Firefox翻訳 / CAT 1.4B |
| 93 | ja→en | lit | 0.326 | 0.042 | 0.169 | 0.541 | 0.371 | 5 | 9 | 8 | 9 | 10 | CAT 0.8B | CAT 1.4B |
| 94 | ja→en | lit | -0.354 | 0.160 | -0.352 | -0.130 | 0.003 | 7 | 7 | 1 | 4 | 10 | Shisa350M | CAT 1.4B |
| 95 | ja→en | lit | -0.314 | 0.402 | 0.329 | 0.423 | 0.379 | 7 | 2 | 1 | 9 | 10 | CAT 0.8B | CAT 1.4B |
| 96 | ja→en | sns | 0.253 | 0.413 | -0.221 | 0.412 | 0.397 | 4 | 2 | 1 | 10 | 9 | Shisa350M | CAT 0.8B |
| 97 | ja→en | sns | -0.265 | 0.268 | 0.151 | 0.283 | 0.269 | 3 | 6 | 5 | 10 | 8 | CAT 0.8B | CAT 0.8B |
| 98 | ja→en | sns | -0.145 | 0.812 | 0.765 | 0.637 | 0.578 | 7 | 2 | 2 | 10 | 10 | Shisa350M | CAT 0.8B / CAT 1.4B |
| 99 | ja→en | sns | 0.528 | 0.272 | 0.057 | 0.556 | 0.523 | 8 | 7 | 1 | 9 | 9 | CAT 0.8B | CAT 0.8B / CAT 1.4B |
| 100 | ja→en | sns | -0.515 | -0.225 | -0.088 | 0.100 | -0.084 | 4 | 4 | 4 | 8 | 5 | CAT 0.8B | CAT 0.8B |

## COMET と LLM 判定の食い違い

定義: 同じ文の2系で、LLM 総合の差が 2 点以上あるのに、COMET の差の向きが逆のもの（COMET の同点は除く）。

- 全部の組は 1000 組（10組×100文）。向きが逆になったのは 244 組。LLM の差が 2 点以上ある組は 638 組で、そのうち向きが逆なのが下の 172 組。

| id | 向き | 分野 | 組 | LLM 総合の差（左−右） | COMET の差（左−右） |
|---|---|---|---|---|---|
| 56 | ja→en | ui | Firefox翻訳 と Shisa350M厳 | +9 | -0.725 |
| 56 | ja→en | ui | Shisa350M厳 と CAT 0.8B | -9 | +0.713 |
| 56 | ja→en | ui | Shisa350M厳 と CAT 1.4B | -9 | +0.713 |
| 59 | ja→en | ui | Shisa350M と CAT 0.8B | -9 | +0.275 |
| 59 | ja→en | ui | Shisa350M厳 と CAT 0.8B | -9 | +0.045 |
| 83 | ja→en | polite | Shisa350M厳 と CAT 0.8B | -9 | +0.093 |
| 51 | ja→en | tech | Firefox翻訳 と Shisa350M厳 | +8 | -0.456 |
| 51 | ja→en | tech | Shisa350M と Shisa350M厳 | +8 | -0.392 |
| 68 | ja→en | web | Shisa350M と Shisa350M厳 | +8 | -0.326 |
| 68 | ja→en | web | Shisa350M厳 と CAT 0.8B | -8 | +0.355 |
| 68 | ja→en | web | Shisa350M厳 と CAT 1.4B | -8 | +0.346 |
| 69 | ja→en | web | Shisa350M と CAT 0.8B | -8 | +0.305 |
| 69 | ja→en | web | Shisa350M厳 と CAT 0.8B | -8 | +0.339 |
| 78 | ja→en | casual | Shisa350M と CAT 0.8B | -8 | +0.350 |
| 78 | ja→en | casual | Shisa350M厳 と CAT 0.8B | -8 | +0.417 |
| 83 | ja→en | polite | Firefox翻訳 と Shisa350M厳 | +8 | -0.109 |
| 92 | ja→en | lit | Firefox翻訳 と Shisa350M | +8 | -0.210 |
| 92 | ja→en | lit | Shisa350M と CAT 1.4B | -8 | +0.223 |
| 95 | ja→en | lit | Shisa350M と CAT 1.4B | -8 | +0.023 |
| 96 | ja→en | sns | Shisa350M と CAT 0.8B | -8 | +0.000 |
| 98 | ja→en | sns | Shisa350M と CAT 0.8B | -8 | +0.175 |
| 98 | ja→en | sns | Shisa350M と CAT 1.4B | -8 | +0.234 |
| 98 | ja→en | sns | Shisa350M厳 と CAT 0.8B | -8 | +0.128 |
| 98 | ja→en | sns | Shisa350M厳 と CAT 1.4B | -8 | +0.188 |
| 48 | en→ja | sns | Firefox翻訳 と Shisa350M厳 | +7 | -0.248 |
| 51 | ja→en | tech | Shisa350M厳 と CAT 0.8B | -7 | +0.357 |
| 56 | ja→en | ui | Shisa350M と Shisa350M厳 | +7 | -0.199 |
| 59 | ja→en | ui | Shisa350M と CAT 1.4B | -7 | +0.338 |
| 59 | ja→en | ui | Shisa350M厳 と CAT 1.4B | -7 | +0.108 |
| 69 | ja→en | web | Firefox翻訳 と Shisa350M | +7 | -0.579 |
| 69 | ja→en | web | Firefox翻訳 と Shisa350M厳 | +7 | -0.613 |
| 70 | ja→en | web | Shisa350M と CAT 0.8B | -7 | +0.502 |
| 70 | ja→en | web | Shisa350M と CAT 1.4B | -7 | +0.247 |
| 70 | ja→en | web | Shisa350M厳 と CAT 0.8B | -7 | +0.470 |
| 70 | ja→en | web | Shisa350M厳 と CAT 1.4B | -7 | +0.214 |
| 72 | ja→en | biz | Shisa350M厳 と CAT 1.4B | -7 | +0.119 |
| 79 | ja→en | casual | Shisa350M と CAT 1.4B | -7 | +0.416 |
| 82 | ja→en | polite | Firefox翻訳 と CAT 0.8B | +7 | -0.365 |
| 82 | ja→en | polite | Firefox翻訳 と CAT 1.4B | +7 | -0.245 |
| 82 | ja→en | polite | Shisa350M と CAT 0.8B | +7 | -0.386 |
| 82 | ja→en | polite | Shisa350M と CAT 1.4B | +7 | -0.266 |
| 83 | ja→en | polite | Shisa350M と CAT 0.8B | -7 | +0.334 |
| 83 | ja→en | polite | Shisa350M厳 と CAT 1.4B | -7 | +0.050 |
| 92 | ja→en | lit | Shisa350M と CAT 0.8B | -7 | +0.211 |
| 96 | ja→en | sns | Shisa350M と CAT 1.4B | -7 | +0.016 |
| 36 | en→ja | legal | Firefox翻訳 と Shisa350M | +6 | -0.122 |
| 48 | en→ja | sns | Shisa350M と Shisa350M厳 | +6 | -0.279 |
| 48 | en→ja | sns | Shisa350M厳 と CAT 0.8B | -6 | +0.042 |
| 51 | ja→en | tech | Shisa350M厳 と CAT 1.4B | -6 | +0.365 |
| 67 | ja→en | web | Firefox翻訳 と Shisa350M | +6 | -0.530 |
| 67 | ja→en | web | Firefox翻訳 と Shisa350M厳 | +6 | -0.530 |
| 67 | ja→en | web | Shisa350M と CAT 1.4B | -6 | +0.277 |
| 67 | ja→en | web | Shisa350M厳 と CAT 1.4B | -6 | +0.277 |
| 69 | ja→en | web | Shisa350M と CAT 1.4B | -6 | +0.381 |
| 69 | ja→en | web | Shisa350M厳 と CAT 1.4B | -6 | +0.414 |
| 71 | ja→en | biz | Firefox翻訳 と Shisa350M | +6 | -0.020 |
| 72 | ja→en | biz | Shisa350M厳 と CAT 0.8B | -6 | +0.352 |
| 81 | ja→en | polite | Firefox翻訳 と Shisa350M厳 | +6 | -0.150 |
| 83 | ja→en | polite | Firefox翻訳 と Shisa350M | +6 | -0.350 |
| 94 | ja→en | lit | Firefox翻訳 と Shisa350M厳 | +6 | -0.002 |
| 95 | ja→en | lit | Firefox翻訳 と Shisa350M厳 | +6 | -0.643 |
| 4 | en→ja | tech | Firefox翻訳 と Shisa350M厳 | -5 | +0.072 |
| 4 | en→ja | tech | Firefox翻訳 と CAT 1.4B | -5 | +0.124 |
| 5 | en→ja | tech | Firefox翻訳 と Shisa350M | +5 | -0.132 |
| 5 | en→ja | tech | Firefox翻訳 と Shisa350M厳 | +5 | -0.101 |
| 5 | en→ja | tech | Shisa350M と CAT 0.8B | -5 | +0.241 |
| 5 | en→ja | tech | Shisa350M厳 と CAT 0.8B | -5 | +0.209 |
| 6 | en→ja | ui | Shisa350M と CAT 1.4B | -5 | +0.190 |
| 25 | en→ja | biz | Firefox翻訳 と CAT 0.8B | -5 | +0.007 |
| 35 | en→ja | polite | Firefox翻訳 と Shisa350M | -5 | +0.059 |
| 36 | en→ja | legal | Shisa350M と CAT 0.8B | -5 | +0.087 |
| 52 | ja→en | tech | Firefox翻訳 と Shisa350M厳 | +5 | -0.083 |
| 52 | ja→en | tech | Shisa350M厳 と CAT 0.8B | -5 | +0.195 |
| 52 | ja→en | tech | Shisa350M厳 と CAT 1.4B | -5 | +0.201 |
| 67 | ja→en | web | Shisa350M と CAT 0.8B | -5 | +0.451 |
| 67 | ja→en | web | Shisa350M厳 と CAT 0.8B | -5 | +0.451 |
| 70 | ja→en | web | Firefox翻訳 と Shisa350M | +5 | -0.659 |
| 70 | ja→en | web | Firefox翻訳 と Shisa350M厳 | +5 | -0.626 |
| 78 | ja→en | casual | Firefox翻訳 と CAT 0.8B | -5 | +0.046 |
| 78 | ja→en | casual | Shisa350M と CAT 1.4B | -5 | +0.270 |
| 78 | ja→en | casual | Shisa350M厳 と CAT 1.4B | -5 | +0.337 |
| 79 | ja→en | casual | Firefox翻訳 と Shisa350M | +5 | -0.635 |
| 83 | ja→en | polite | Shisa350M と CAT 1.4B | -5 | +0.291 |
| 95 | ja→en | lit | Firefox翻訳 と Shisa350M | +5 | -0.717 |
| 98 | ja→en | sns | Firefox翻訳 と Shisa350M | +5 | -0.957 |
| 98 | ja→en | sns | Firefox翻訳 と Shisa350M厳 | +5 | -0.910 |
| 11 | en→ja | news | Firefox翻訳 と Shisa350M | +4 | -0.027 |
| 28 | en→ja | casual | CAT 0.8B と CAT 1.4B | +4 | -0.020 |
| 32 | en→ja | polite | Shisa350M厳 と CAT 0.8B | -4 | +0.070 |
| 32 | en→ja | polite | Shisa350M厳 と CAT 1.4B | -4 | +0.077 |
| 38 | en→ja | legal | CAT 0.8B と CAT 1.4B | -4 | +0.054 |
| 39 | en→ja | legal | Shisa350M と CAT 0.8B | -4 | +0.002 |
| 41 | en→ja | lit | Shisa350M厳 と CAT 0.8B | -4 | +0.028 |
| 62 | ja→en | news | Firefox翻訳 と CAT 0.8B | -4 | +0.052 |
| 62 | ja→en | news | Firefox翻訳 と CAT 1.4B | -4 | +0.052 |
| 68 | ja→en | web | Firefox翻訳 と Shisa350M厳 | +4 | -0.663 |
| 72 | ja→en | biz | Firefox翻訳 と Shisa350M厳 | +4 | -0.573 |
| 74 | ja→en | biz | Shisa350M と CAT 1.4B | +4 | -0.027 |
| 79 | ja→en | casual | Shisa350M と Shisa350M厳 | -4 | +0.434 |
| 79 | ja→en | casual | Shisa350M と CAT 0.8B | -4 | +0.435 |
| 93 | ja→en | lit | Firefox翻訳 と Shisa350M | -4 | +0.284 |
| 1 | en→ja | tech | Shisa350M と CAT 1.4B | +3 | -0.042 |
| 1 | en→ja | tech | Shisa350M厳 と CAT 1.4B | +3 | -0.052 |
| 2 | en→ja | tech | Shisa350M厳 と CAT 0.8B | -3 | +0.061 |
| 2 | en→ja | tech | CAT 0.8B と CAT 1.4B | +3 | -0.126 |
| 4 | en→ja | tech | Firefox翻訳 と Shisa350M | -3 | +0.028 |
| 6 | en→ja | ui | Firefox翻訳 と CAT 0.8B | -3 | +0.261 |
| 6 | en→ja | ui | Firefox翻訳 と CAT 1.4B | -3 | +0.525 |
| 7 | en→ja | ui | Shisa350M と CAT 0.8B | -3 | +0.037 |
| 7 | en→ja | ui | CAT 0.8B と CAT 1.4B | +3 | -0.037 |
| 8 | en→ja | ui | Shisa350M と CAT 1.4B | -3 | +0.083 |
| 9 | en→ja | ui | Firefox翻訳 と Shisa350M | -3 | +0.019 |
| 9 | en→ja | ui | Firefox翻訳 と Shisa350M厳 | -3 | +0.019 |
| 28 | en→ja | casual | Shisa350M と CAT 1.4B | +3 | -0.109 |
| 28 | en→ja | casual | Shisa350M厳 と CAT 1.4B | +3 | -0.109 |
| 30 | en→ja | casual | Firefox翻訳 と CAT 0.8B | -3 | +0.061 |
| 36 | en→ja | legal | Firefox翻訳 と CAT 1.4B | +3 | -0.241 |
| 41 | en→ja | lit | Shisa350M と CAT 0.8B | -3 | +0.161 |
| 42 | en→ja | lit | Shisa350M厳 と CAT 1.4B | -3 | +0.074 |
| 50 | en→ja | sns | Firefox翻訳 と Shisa350M厳 | -3 | +0.382 |
| 50 | en→ja | sns | Shisa350M厳 と CAT 0.8B | +3 | -0.118 |
| 52 | ja→en | tech | Firefox翻訳 と Shisa350M | +3 | -0.088 |
| 52 | ja→en | tech | Shisa350M と CAT 0.8B | -3 | +0.200 |
| 52 | ja→en | tech | Shisa350M と CAT 1.4B | -3 | +0.206 |
| 55 | ja→en | tech | Shisa350M と CAT 0.8B | -3 | +0.034 |
| 64 | ja→en | news | Firefox翻訳 と Shisa350M | +3 | -0.008 |
| 78 | ja→en | casual | Firefox翻訳 と Shisa350M | +3 | -0.304 |
| 78 | ja→en | casual | Firefox翻訳 と Shisa350M厳 | +3 | -0.371 |
| 78 | ja→en | casual | CAT 0.8B と CAT 1.4B | +3 | -0.080 |
| 89 | ja→en | legal | Firefox翻訳 と CAT 1.4B | -3 | +0.022 |
| 90 | ja→en | legal | Firefox翻訳 と CAT 1.4B | +3 | -0.031 |
| 93 | ja→en | lit | Firefox翻訳 と Shisa350M厳 | -3 | +0.158 |
| 94 | ja→en | lit | Firefox翻訳 と CAT 0.8B | +3 | -0.224 |
| 94 | ja→en | lit | Shisa350M と CAT 1.4B | -3 | +0.158 |
| 2 | en→ja | tech | Shisa350M と CAT 0.8B | -2 | +0.067 |
| 4 | en→ja | tech | Firefox翻訳 と CAT 0.8B | -2 | +0.137 |
| 4 | en→ja | tech | Shisa350M と Shisa350M厳 | -2 | +0.044 |
| 4 | en→ja | tech | Shisa350M と CAT 1.4B | -2 | +0.095 |
| 10 | en→ja | ui | Firefox翻訳 と Shisa350M厳 | +2 | -0.148 |
| 10 | en→ja | ui | Shisa350M厳 と CAT 1.4B | -2 | +0.088 |
| 18 | en→ja | web | Firefox翻訳 と CAT 1.4B | -2 | +0.036 |
| 20 | en→ja | web | Firefox翻訳 と CAT 0.8B | -2 | +0.100 |
| 24 | en→ja | biz | Firefox翻訳 と CAT 1.4B | -2 | +0.009 |
| 27 | en→ja | casual | Firefox翻訳 と Shisa350M | -2 | +0.047 |
| 28 | en→ja | casual | Firefox翻訳 と CAT 1.4B | +2 | -0.411 |
| 30 | en→ja | casual | Firefox翻訳 と Shisa350M | -2 | +0.028 |
| 36 | en→ja | legal | CAT 0.8B と CAT 1.4B | +2 | -0.205 |
| 37 | en→ja | legal | Shisa350M と CAT 1.4B | -2 | +0.034 |
| 41 | en→ja | lit | Firefox翻訳 と CAT 0.8B | -2 | +0.311 |
| 42 | en→ja | lit | Firefox翻訳 と Shisa350M | +2 | -0.051 |
| 46 | en→ja | sns | Shisa350M と Shisa350M厳 | +2 | -0.069 |
| 51 | ja→en | tech | Firefox翻訳 と CAT 1.4B | +2 | -0.091 |
| 51 | ja→en | tech | Shisa350M と CAT 1.4B | +2 | -0.027 |
| 56 | ja→en | ui | Firefox翻訳 と Shisa350M | +2 | -0.526 |
| 56 | ja→en | ui | Shisa350M と CAT 0.8B | -2 | +0.514 |
| 56 | ja→en | ui | Shisa350M と CAT 1.4B | -2 | +0.514 |
| 59 | ja→en | ui | Firefox翻訳 と Shisa350M | +2 | -0.501 |
| 59 | ja→en | ui | Firefox翻訳 と Shisa350M厳 | +2 | -0.272 |
| 65 | ja→en | news | Firefox翻訳 と CAT 1.4B | +2 | -0.014 |
| 72 | ja→en | biz | Shisa350M と Shisa350M厳 | +2 | -0.805 |
| 76 | ja→en | casual | Shisa350M と CAT 0.8B | -2 | +0.042 |
| 76 | ja→en | casual | Shisa350M厳 と CAT 0.8B | -2 | +0.014 |
| 77 | ja→en | casual | Firefox翻訳 と Shisa350M | -2 | +0.119 |
| 77 | ja→en | casual | Firefox翻訳 と CAT 0.8B | -2 | +0.077 |
| 77 | ja→en | casual | Firefox翻訳 と CAT 1.4B | -2 | +0.020 |
| 80 | ja→en | casual | CAT 0.8B と CAT 1.4B | +2 | -0.114 |
| 81 | ja→en | polite | Shisa350M と CAT 0.8B | +2 | -0.105 |
| 81 | ja→en | polite | CAT 0.8B と CAT 1.4B | -2 | +0.083 |
| 83 | ja→en | polite | CAT 0.8B と CAT 1.4B | +2 | -0.043 |
| 85 | ja→en | polite | Firefox翻訳 と CAT 1.4B | +2 | -0.090 |
| 91 | ja→en | lit | Shisa350M と Shisa350M厳 | +2 | -0.125 |
| 96 | ja→en | sns | Firefox翻訳 と Shisa350M | +2 | -0.159 |

## 注釈を切ると COMET はどう変わるか

「注釈のある文数」は、訳の後ろに空でない行が続く出力の数。平均の差は `comet_qe_first_line` − `comet_qe`。

| 系 | 注釈のある文数 | 平均の差（先頭行−訳のまま） |
|---|---|---|
| Firefox翻訳 | 0 | 0.0000 |
| Shisa350M | 36 | 0.0671 |
| Shisa350M厳 | 64 | 0.2958 |
| CAT 0.8B | 0 | -0.0000 |
| CAT 1.4B | 0 | 0.0000 |

## 系どうしの差の目安（文の対応をとった差）

差の平均と、標準誤差の2倍（約95%の幅）。n=100。幅が0をまたぐ差は、この文数では区別できていない。

| 組 | 指標 | 平均の差（左−右） | 約95%の幅 | 0 をまたぐか |
|---|---|---|---|---|
| Firefox翻訳 − Shisa350M | COMET-QE | -0.003 | -0.068 〜 0.062 | またぐ |
| Firefox翻訳 − Shisa350M | LLM 総合 | 1.39 | 0.78 〜 2.00 | またがない |
| Firefox翻訳 − Shisa350M厳 | COMET-QE | 0.190 | 0.088 〜 0.292 | またがない |
| Firefox翻訳 − Shisa350M厳 | LLM 総合 | 2.85 | 2.11 〜 3.59 | またがない |
| Firefox翻訳 − CAT 0.8B | COMET-QE | -0.098 | -0.138 〜 -0.057 | またがない |
| Firefox翻訳 − CAT 0.8B | LLM 総合 | -1.20 | -1.68 〜 -0.72 | またがない |
| Firefox翻訳 − CAT 1.4B | COMET-QE | -0.132 | -0.175 〜 -0.089 | またがない |
| Firefox翻訳 − CAT 1.4B | LLM 総合 | -1.24 | -1.74 〜 -0.74 | またがない |
| Shisa350M − Shisa350M厳 | COMET-QE | 0.193 | 0.117 〜 0.269 | またがない |
| Shisa350M − Shisa350M厳 | LLM 総合 | 1.46 | 0.90 〜 2.02 | またがない |
| Shisa350M − CAT 0.8B | COMET-QE | -0.095 | -0.150 〜 -0.040 | またがない |
| Shisa350M − CAT 0.8B | LLM 総合 | -2.59 | -3.15 〜 -2.03 | またがない |
| Shisa350M − CAT 1.4B | COMET-QE | -0.129 | -0.184 〜 -0.073 | またがない |
| Shisa350M − CAT 1.4B | LLM 総合 | -2.63 | -3.19 〜 -2.07 | またがない |
| Shisa350M厳 − CAT 0.8B | COMET-QE | -0.288 | -0.377 〜 -0.199 | またがない |
| Shisa350M厳 − CAT 0.8B | LLM 総合 | -4.05 | -4.67 〜 -3.43 | またがない |
| Shisa350M厳 − CAT 1.4B | COMET-QE | -0.322 | -0.409 〜 -0.234 | またがない |
| Shisa350M厳 − CAT 1.4B | LLM 総合 | -4.09 | -4.67 〜 -3.51 | またがない |
| CAT 0.8B − CAT 1.4B | COMET-QE | -0.034 | -0.060 〜 -0.007 | またがない |
| CAT 0.8B − CAT 1.4B | LLM 総合 | -0.04 | -0.36 〜 0.28 | またぐ |

