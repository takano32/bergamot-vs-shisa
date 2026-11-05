#!/usr/bin/env python3
"""results/comet.jsonl（COMET-QE）と results/llm_judge.jsonl（LLM 判定）から results/scores.md を作る。

- 全体、方向別、種類別、方向×種類の平均（COMET と LLM 総合）
- 文ごとの表（5系の点と、各指標の最良）
- 食い違い: 同じ文の2系の組で、LLM 総合の差が2点以上あるのに COMET の差の向きが逆のもの
- 注釈を切った点（comet_qe_first_line）と原文のままの点（comet_qe）の差
- 系どうしの差の目安（文ごとの対応のある差の平均と、その2倍の標準誤差で作った約95%の幅）

LLM 判定は2回に分かれている（bergamot・shisa・shisa_strict は1回目、cat08・cat14 は2回目で、判定役のセッションが別）。
1回目の判定は3系を同時に見て付けたもので、2回目は2系を同時に見て付けた。判定役が違うので、回をまたぐ差は割り引いて読む。
"""
import itertools
import json
import math
import statistics
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SYSTEMS = ["bergamot", "shisa", "shisa_strict", "cat08", "cat14"]
LABEL = {
    "bergamot": "Firefox翻訳",
    "shisa": "Shisa350M",
    "shisa_strict": "Shisa350M厳",
    "cat08": "CAT-Translate 0.8B",
    "cat14": "CAT-Translate 1.4B",
}
PAIRS = list(itertools.combinations(SYSTEMS, 2))  # 全部の組（10組）
PASS = {"bergamot": 1, "shisa": 1, "shisa_strict": 1, "cat08": 2, "cat14": 2}  # LLM 判定の回（1 回目は3系、2 回目は2系）
DISAGREE_LLM_GAP = 2  # LLM 総合の差がこの点以上なら「明確に差がある」とみなす（判定前に決めた）


def cross_pass(a, b):
    """判定の回が違う組。LLM 総合の差に判定役の違いが混ざる。"""
    return PASS[a] != PASS[b]


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

    def dirname(i):
        return f"{sents[i]['src_lang']}→{sents[i]['tgt_lang']}"

    def cat(i):
        return sents[i]["category"]

    def group_mean(ids_, system, key):
        vals = [comet[(i, system)][key] if key.startswith("comet") else llm[(i, system)][key] for i in ids_]
        return mean(vals)

    out = []
    w = out.append
    w("# 採点の結果（COMET-QE と LLM 判定）")
    w("")
    w("COMET-QE は `results/comet.jsonl`、LLM 判定は `results/llm_judge.jsonl`。判定の基準は README の「採点の基準」。")
    w("LLM 判定は2回に分かれている。1回目は bergamot・shisa・shisa_strict を同時に見て付けた。2回目は cat08・cat14 を同時に見て付けた（判定役のセッションが別、既存の判定はやり直していない）。回をまたぐ LLM の差は、判定役の違いを含む。")
    w("")

    # 1. 全体
    w("## 全体の平均（30文）")
    w("")
    w("| 系 | COMET-QE（訳のまま） | COMET-QE（注釈を切った先頭行） | LLM 正確さ | LLM 自然さ | LLM 注釈減点 | LLM 総合 |")
    w("|---|---|---|---|---|---|---|")
    for s in SYSTEMS:
        w(f"| {LABEL[s]} | {fmt(group_mean(ids, s, 'comet_qe'), 3)} | {fmt(group_mean(ids, s, 'comet_qe_first_line'), 3)} | "
          f"{fmt(group_mean(ids, s, 'acc'))} | {fmt(group_mean(ids, s, 'nat'))} | {fmt(group_mean(ids, s, 'pen'))} | {fmt(group_mean(ids, s, 'total'))} |")
    w("")

    # 2. 方向・種類・方向×種類
    w("## 方向別、種類別、方向×種類の平均")
    w("")
    head = "| 群 | n | " + " | ".join(f"{LABEL[s]} COMET / LLM 総合" for s in SYSTEMS) + " |"
    w(head)
    w("|---|---|" + "---|" * len(SYSTEMS))
    groups = []
    for d in ["en→ja", "ja→en"]:
        groups.append((d, [i for i in ids if dirname(i) == d]))
    for c, name in [("tech", "技術文"), ("conv", "会話"), ("web", "Web記事風")]:
        groups.append((name, [i for i in ids if cat(i) == c]))
    for d in ["en→ja", "ja→en"]:
        for c, name in [("tech", "技術文"), ("conv", "会話"), ("web", "Web記事風")]:
            groups.append((f"{d} {name}", [i for i in ids if dirname(i) == d and cat(i) == c]))
    for name, g in groups:
        cells = [f"{fmt(group_mean(g, s, 'comet_qe'), 3)} / {fmt(group_mean(g, s, 'total'))}" for s in SYSTEMS]
        w(f"| {name} | {len(g)} | " + " | ".join(cells) + " |")
    w("")

    # 3. 文ごとの表
    w("## 文ごとの点")
    w("")
    w("COMET は訳のまま。LLM は 正確さ/自然さ/注釈減点 の総合。最良は、その指標で一番高い系（同点は「=」）。")
    w("")
    w("| id | 向き | 種類 | " + " | ".join(f"{LABEL[s]} COMET" for s in SYSTEMS)
      + " | " + " | ".join(f"{LABEL[s]} LLM" for s in SYSTEMS) + " | COMET 最良 | LLM 最良 |")
    w("|---|---|---|" + "---|" * (2 * len(SYSTEMS)) + "---|---|")
    for i in ids:
        cs = {s: comet[(i, s)]["comet_qe"] for s in SYSTEMS}
        ls = {s: llm[(i, s)]["total"] for s in SYSTEMS}
        cmax = max(cs.values())
        lmax = max(ls.values())
        cbest = " / ".join(LABEL[s] for s in SYSTEMS if cs[s] == cmax)
        lbest = " / ".join(LABEL[s] for s in SYSTEMS if ls[s] == lmax) + (" （同点含む）" if sum(v == lmax for v in ls.values()) > 1 else "")
        w(f"| {i} | {dirname(i)} | {cat(i)} | " + " | ".join(fmt(cs[s], 3) for s in SYSTEMS)
          + " | " + " | ".join(str(ls[s]) for s in SYSTEMS) + f" | {cbest} | {lbest} |")
    w("")

    # 4. 食い違い
    w("## COMET と LLM 判定の食い違い")
    w("")
    w(f"判定の定義: 同じ文の2系で、LLM 総合の差が {DISAGREE_LLM_GAP} 点以上あるのに、COMET の差の向きが逆のもの（COMET 同点は除く）。")
    w("「※判定の回が違う」は、一方が1回目（bergamot・shisa・shisa_strict）、他方が2回目（cat08・cat14）の組。LLM 総合の差に判定役の違いが混ざるので、その組の LLM 側は割り引いて読む。")
    w("")
    flagged, reversed_any = [], 0
    for i in ids:
        for a, b in PAIRS:
            dl = llm[(i, a)]["total"] - llm[(i, b)]["total"]
            dc = comet[(i, a)]["comet_qe"] - comet[(i, b)]["comet_qe"]
            if dl != 0 and dc != 0 and (dl > 0) != (dc > 0):
                reversed_any += 1
                if abs(dl) >= DISAGREE_LLM_GAP:
                    flagged.append((i, a, b, dl, dc))
    w(f"- 向きが逆になった組は全部で {reversed_any} 組（{len(PAIRS) * len(ids)} 組のうち）。そのうち LLM の差が {DISAGREE_LLM_GAP} 点以上のものが下の {len(flagged)} 組。")
    w("")
    if flagged:
        w("| id | 向き | 種類 | 組 | LLM 総合の差（左−右） | COMET の差（左−右） |")
        w("|---|---|---|---|---|---|")
        for i, a, b, dl, dc in flagged:
            mark = " ※判定の回が違う" if cross_pass(a, b) else ""
            w(f"| {i} | {dirname(i)} | {cat(i)} | {LABEL[a]} と {LABEL[b]}{mark} | {dl:+d} | {dc:+.3f} |")
    else:
        w("該当なし。")
    w("")

    # 5. 注釈の影響
    w("## 注釈を切ると COMET はどう変わるか")
    w("")
    w("「注釈のある文数」は、訳の後ろに空でない行が続く出力の数。`comet_qe_first_line` から `comet_qe` を引いた平均は、先頭行だけの採点との差（0 に近いほど、注釈の有無が COMET に効いていない）。")
    w("")
    w("| 系 | 注釈のある文数 | 平均の差（先頭行−訳のまま） |")
    w("|---|---|---|")
    for s in SYSTEMS:
        diffs = [comet[(i, s)]["comet_qe_first_line"] - comet[(i, s)]["comet_qe"] for i in ids]
        n_multi = sum(1 for i in ids if len([l for l in hyps[s][i].splitlines() if l.strip()]) > 1)
        w(f"| {LABEL[s]} | {n_multi} | {fmt(mean(diffs), 4)} |")
    w("")

    # 6. 系どうしの差の目安
    w("## 系どうしの差の目安（文の対応をとった差）")
    w("")
    w("差の平均と、その標準誤差の2倍（約95%の幅）。幅が0をまたぐ差は、30文では区別できていない。")
    w("")
    w("| 組 | 指標 | 平均の差（左−右） | 約95%の幅 |")
    w("|---|---|---|---|")
    for a, b in PAIRS:
        for key, name in [("comet_qe", "COMET-QE"), ("total", "LLM 総合")]:
            ds = []
            for i in ids:
                x = comet[(i, a)][key] if key == "comet_qe" else llm[(i, a)][key]
                y = comet[(i, b)][key] if key == "comet_qe" else llm[(i, b)][key]
                ds.append(x - y)
            m = mean(ds)
            se = statistics.stdev(ds) / math.sqrt(len(ds))
            nd = 3 if key == "comet_qe" else 2
            mark = " ※判定の回が違う" if (key == "total" and cross_pass(a, b)) else ""
            w(f"| {LABEL[a]} − {LABEL[b]} | {name}{mark} | {fmt(m, nd)} | {fmt(m - 2 * se, nd)} 〜 {fmt(m + 2 * se, nd)} |")
    w("")

    out_path = REPO / "results/scores.md"
    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote", out_path)


if __name__ == "__main__":
    main()
