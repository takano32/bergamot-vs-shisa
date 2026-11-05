#!/usr/bin/env python3
"""results/comet.jsonl（COMET-QE）と results/llm_judge.jsonl（LLM 判定）から results/scores.md を作る。

- 網羅の表（分野と現象タグごとの本数）
- 全体、方向別、分野別、現象別の平均（COMET と LLM 総合）
- 文ごとの表（5系の点と、各指標の最良）
- 食い違い: 同じ文の2系の組で、LLM 総合の差が2点以上あるのに COMET の差の向きが逆のもの
- 注釈を切った点（comet_qe_first_line）と原文のままの点（comet_qe）の差
- 系どうしの差の目安（文ごとの対応のある差の平均と、その2倍の標準誤差で作った約95%の幅）

LLM 判定は5系を1回でまとめて、系の名前を伏せ、文ごとに並びを入れ替えて付けた（scripts/make_blind.py）。
"""
import itertools
import json
import math
import statistics
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SYSTEMS = ["bergamot", "shisa", "shisa_strict", "cat08", "cat14"]
LABEL = {"bergamot": "Firefox翻訳", "shisa": "Shisa350M", "shisa_strict": "Shisa350M厳", "cat08": "CAT 0.8B", "cat14": "CAT 1.4B"}
PAIRS = list(itertools.combinations(SYSTEMS, 2))
GAP = 2  # LLM 総合の差がこの点以上なら「明確な差」（README に書いた定義）
DOMAINS = [("tech", "技術文書"), ("ui", "UI の文言"), ("news", "ニュース"), ("web", "Web 記事・ブログ"), ("biz", "ビジネスメール"),
           ("casual", "くだけた会話"), ("polite", "接客・丁寧な会話"), ("legal", "法律・規約"), ("lit", "文学的な文"), ("sns", "SNS の短文")]
TAGS = [("hon", "敬語・丁寧さ"), ("pro", "主語の省略"), ("idm", "慣用句・口語表現"), ("num", "数字・日付・単位"), ("prop", "固有名詞"),
        ("poly", "多義語"), ("neg", "否定"), ("q", "疑問"), ("long", "長文"), ("frag", "短い断片"), ("code", "コード・記号混じり"), ("md", "Markdown")]


def load_jsonl(path):
    return [json.loads(line) for line in open(path, encoding="utf-8")]


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def fmt(x, nd=2):
    return "-" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{nd}f}"


def main():
    sents = {r["id"]: r for r in load_jsonl(REPO / "data/sentences.jsonl")}
    comet = {(r["id"], r["system"]): r for r in load_jsonl(REPO / "results/comet.jsonl")}
    llm = {(r["id"], r["system"]): r for r in load_jsonl(REPO / "results/llm_judge.jsonl")}
    hyps = {s: {r["id"]: r["hyp"] for r in load_jsonl(REPO / f"results/{s}.jsonl")} for s in SYSTEMS}
    ids = sorted(sents)
    N = len(ids)

    def direction(i):
        return f"{sents[i]['src_lang']}→{sents[i]['tgt_lang']}"

    def val(i, s, key):
        return comet[(i, s)][key] if key.startswith("comet") else llm[(i, s)][key]

    def gm(g, s, key):
        return mean([val(i, s, key) for i in g])

    out = []
    w = out.append
    w("# 採点の結果（COMET-QE と LLM 判定、100文）")
    w("")
    w("COMET-QE は `results/comet.jsonl`、LLM 判定は `results/llm_judge.jsonl`。判定の基準は README の「採点の基準」。")
    w("LLM 判定は、5系を1回でまとめて、系の名前を伏せ、文ごとに並びを入れ替えて付けた（判定役は1人・1セッション）。")
    w("")

    # 網羅
    w("## 網羅の表（文の本数）")
    w("")
    w("| 分野 | 英→日 | 日→英 | 計 |")
    w("|---|---|---|---|")
    for k, name in DOMAINS:
        a = sum(1 for i in ids if sents[i]["category"] == k and sents[i]["src_lang"] == "en")
        b = sum(1 for i in ids if sents[i]["category"] == k and sents[i]["src_lang"] == "ja")
        w(f"| {name}（{k}） | {a} | {b} | {a + b} |")
    w("")
    w("| 現象タグ | 英→日 | 日→英 | 計 |")
    w("|---|---|---|---|")
    for k, name in TAGS:
        a = sum(1 for i in ids if k in sents[i]["tags"] and sents[i]["src_lang"] == "en")
        b = sum(1 for i in ids if k in sents[i]["tags"] and sents[i]["src_lang"] == "ja")
        w(f"| {name}（{k}） | {a} | {b} | {a + b} |")
    w("")

    # 全体
    w(f"## 全体の平均（{N}文）")
    w("")
    w("| 系 | COMET-QE（訳のまま） | COMET-QE（注釈を切った先頭行） | LLM 正確さ | LLM 自然さ | LLM 注釈減点 | LLM 総合 |")
    w("|---|---|---|---|---|---|---|")
    for s in SYSTEMS:
        w(f"| {LABEL[s]} | {fmt(gm(ids, s, 'comet_qe'), 3)} | {fmt(gm(ids, s, 'comet_qe_first_line'), 3)} | "
          f"{fmt(gm(ids, s, 'acc'))} | {fmt(gm(ids, s, 'nat'))} | {fmt(gm(ids, s, 'pen'))} | {fmt(gm(ids, s, 'total'))} |")
    w("")

    def group_table(title, groups, note):
        w(f"## {title}")
        w("")
        w(note)
        w("")
        w("| 群 | n | " + " | ".join(f"{LABEL[s]}" for s in SYSTEMS) + " |")
        w("|---|---|" + "---|" * len(SYSTEMS))
        for name, g in groups:
            w(f"| {name} | {len(g)} | " + " | ".join(f"{fmt(gm(g, s, 'total'))} / {fmt(gm(g, s, 'comet_qe'), 3)}" for s in SYSTEMS) + " |")
        w("")

    note = "各セルは「LLM 総合 / COMET-QE（訳のまま）」の平均。"
    group_table("方向別", [(d, [i for i in ids if direction(i) == d]) for d in ["en→ja", "ja→en"]], note)
    group_table("分野別", [(f"{name}（{k}）", [i for i in ids if sents[i]["category"] == k]) for k, name in DOMAINS], note)
    group_table("現象別（1文に複数のタグがつくので、群は重なる）", [(f"{name}（{k}）", [i for i in ids if k in sents[i]["tags"]]) for k, name in TAGS], note)

    # 文ごと
    w("## 文ごとの点")
    w("")
    w("COMET は訳のまま。LLM は 正確さ + 自然さ + 注釈減点。最良は、その指標で一番高い系（同点は並べる）。")
    w("")
    w("| id | 向き | 分野 | " + " | ".join(f"{LABEL[s]} COMET" for s in SYSTEMS) + " | " + " | ".join(f"{LABEL[s]} LLM" for s in SYSTEMS) + " | COMET 最良 | LLM 最良 |")
    w("|---|---|---|" + "---|" * (2 * len(SYSTEMS)) + "---|---|")
    for i in ids:
        cs = {s: comet[(i, s)]["comet_qe"] for s in SYSTEMS}
        ls = {s: llm[(i, s)]["total"] for s in SYSTEMS}
        cm, lm = max(cs.values()), max(ls.values())
        w(f"| {i} | {direction(i)} | {sents[i]['category']} | " + " | ".join(fmt(cs[s], 3) for s in SYSTEMS) + " | " + " | ".join(str(ls[s]) for s in SYSTEMS)
          + " | " + " / ".join(LABEL[s] for s in SYSTEMS if cs[s] == cm) + " | " + " / ".join(LABEL[s] for s in SYSTEMS if ls[s] == lm) + " |")
    w("")

    # 食い違い
    w("## COMET と LLM 判定の食い違い")
    w("")
    w(f"定義: 同じ文の2系で、LLM 総合の差が {GAP} 点以上あるのに、COMET の差の向きが逆のもの（COMET の同点は除く）。")
    w("")
    flagged, rev = [], 0
    for i in ids:
        for a, b in PAIRS:
            dl = llm[(i, a)]["total"] - llm[(i, b)]["total"]
            dc = comet[(i, a)]["comet_qe"] - comet[(i, b)]["comet_qe"]
            if dl != 0 and dc != 0 and (dl > 0) != (dc > 0):
                rev += 1
                if abs(dl) >= GAP:
                    flagged.append((i, a, b, dl, dc))
    big = sum(1 for i in ids for a, b in PAIRS if abs(llm[(i, a)]["total"] - llm[(i, b)]["total"]) >= GAP)
    w(f"- 全部の組は {len(PAIRS) * N} 組（10組×{N}文）。向きが逆になったのは {rev} 組。LLM の差が {GAP} 点以上ある組は {big} 組で、そのうち向きが逆なのが下の {len(flagged)} 組。")
    w("")
    if flagged:
        flagged.sort(key=lambda t: -abs(t[3]))
        w("| id | 向き | 分野 | 組 | LLM 総合の差（左−右） | COMET の差（左−右） |")
        w("|---|---|---|---|---|---|")
        for i, a, b, dl, dc in flagged:
            w(f"| {i} | {direction(i)} | {sents[i]['category']} | {LABEL[a]} と {LABEL[b]} | {dl:+d} | {dc:+.3f} |")
    else:
        w("該当なし。")
    w("")

    # 注釈
    w("## 注釈を切ると COMET はどう変わるか")
    w("")
    w("「注釈のある文数」は、訳の後ろに空でない行が続く出力の数。平均の差は `comet_qe_first_line` − `comet_qe`。")
    w("")
    w("| 系 | 注釈のある文数 | 平均の差（先頭行−訳のまま） |")
    w("|---|---|---|")
    for s in SYSTEMS:
        diffs = [comet[(i, s)]["comet_qe_first_line"] - comet[(i, s)]["comet_qe"] for i in ids]
        n_multi = sum(1 for i in ids if len([l for l in hyps[s][i].splitlines() if l.strip()]) > 1)
        w(f"| {LABEL[s]} | {n_multi} | {fmt(mean(diffs), 4)} |")
    w("")

    # 差の目安
    w("## 系どうしの差の目安（文の対応をとった差）")
    w("")
    w(f"差の平均と、標準誤差の2倍（約95%の幅）。n={N}。幅が0をまたぐ差は、この文数では区別できていない。")
    w("")
    w("| 組 | 指標 | 平均の差（左−右） | 約95%の幅 | 0 をまたぐか |")
    w("|---|---|---|---|---|")
    for a, b in PAIRS:
        for key, name in [("comet_qe", "COMET-QE"), ("total", "LLM 総合")]:
            ds = [val(i, a, key) - val(i, b, key) for i in ids]
            m = mean(ds)
            se = statistics.stdev(ds) / math.sqrt(len(ds))
            nd = 3 if key == "comet_qe" else 2
            cross = "またぐ" if (m - 2 * se) <= 0 <= (m + 2 * se) else "またがない"
            w(f"| {LABEL[a]} − {LABEL[b]} | {name} | {fmt(m, nd)} | {fmt(m - 2 * se, nd)} 〜 {fmt(m + 2 * se, nd)} | {cross} |")
    w("")
    (REPO / "results/scores.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote results/scores.md")


if __name__ == "__main__":
    main()
