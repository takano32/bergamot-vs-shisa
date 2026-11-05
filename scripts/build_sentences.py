#!/usr/bin/env python3
"""data/sentences.jsonl を作る（例文100本の元データはこのファイル）。

各文: 分野 category（10種、各10本＝日→英5・英→日5）、現象タグ tags。
手で付けるタグ: hon 敬語/丁寧さ、pro 主語の省略、idm 慣用句、num 数字・日付・単位、prop 固有名詞、
poly 多義語、neg 否定、q 疑問。機械で付けるタグ（規則は下の auto_tags）: long、frag、code、md。
id は 英→日が 1〜50、日→英が 51〜100。文は全部この実験のために書いた自作。
"""
import json, re
from pathlib import Path

E, J = "en", "ja"
# (分野, 向き, 手付けのタグ, 原文)
S = [
 # --- tech 技術文書 ---
 ("tech", E, "num", "Set the timeout to 30 seconds, then restart the worker with `systemctl restart worker` and check the log."),
 ("tech", E, "neg poly", "Never commit API keys to the repository; rotate any key that has already been pushed."),
 ("tech", E, "q", "Why does the cache return stale entries after the process calls `fork()`?"),
 ("tech", E, "neg poly", "Because the scheduler runs each task in its own thread, a slow task delays only itself, but a task that holds the global lock for several seconds will stall every other worker until the lock is released, so keep critical sections short."),
 ("tech", E, "num", "Deprecated in v2.4; use `Client.connect()` instead."),
 ("tech", J, "pro hon", "ファイルが見つからない場合は、パスを確認してからもう一度実行してください。"),
 ("tech", J, "pro poly", "`mutex.lock()` を握ったまま例外を投げると、他のスレッドが永久に待たされる。"),
 ("tech", J, "pro num", "メモリ使用量が 2.5 GB を超えたらアラートを出す設定にしてある。"),
 ("tech", J, "neg num", "**注意:** `git rebase -i HEAD~3` は直近3つのコミットを書き換えるので、push 済みの履歴には使わないこと。"),
 ("tech", J, "pro", "非同期処理の戻り値を待たずに次の行へ進むと、まだ入っていない値を読んでしまうことがあり、原因の特定に時間がかかるため、まずログの出力順を確かめるとよい。"),
 # --- ui UI の文言 ---
 ("ui", E, "q neg", "Are you sure you want to delete this folder? This action cannot be undone."),
 ("ui", E, "poly", "Save changes"),
 ("ui", E, "num", "You have 3 unread messages and 1 pending invitation."),
 ("ui", E, "num neg", "Your password must be at least 12 characters and include a number."),
 ("ui", E, "", "Sign in with your account to sync bookmarks across devices. You can turn this off anytime in **Settings > Privacy**."),
 ("ui", J, "", "保存せずに閉じる"),
 ("ui", J, "neg hon", "**接続エラー:** ネットワークに接続できません。接続を確認してもう一度お試しください。"),
 ("ui", J, "hon pro", "通知を許可すると、新着メッセージをすぐにお知らせします。"),
 ("ui", J, "num", "{count} 件の項目が選択されています"),
 ("ui", J, "q hon", "設定を元に戻しますか？"),
 # --- news ニュース ---
 ("news", E, "num", "The central bank raised its benchmark rate by 0.25 percentage points to 4.5 percent on Thursday, the third increase this year."),
 ("news", E, "num prop", "Heavy rain forced the cancellation of more than 200 flights at Frankfurt airport on Monday morning."),
 ("news", E, "neg poly", "Officials said they would not release the report until the investigation had concluded."),
 ("news", E, "prop idm", "Osaka Mayor Hanako Yamamoto announced the plan at a press conference, saying the city would turn over a new leaf on public transport."),
 ("news", E, "neg num", "A new study suggests that people who walk for at least 30 minutes a day are less likely to develop heart disease, though the researchers caution that the data cannot prove a causal link and that other lifestyle factors may explain part of the difference."),
 ("news", J, "num", "政府は来月1日から、電気料金の補助を3か月間延長すると発表した。"),
 ("news", J, "prop num", "気象庁によると、台風14号は明日の昼ごろ関東地方に最も接近する見込み。"),
 ("news", J, "pro neg", "容疑者は調べに対し、「覚えていない」と話しているという。"),
 ("news", J, "prop", "日銀の植田総裁は、物価の動向を注視しながら、金融政策を慎重に判断していく考えを示した。"),
 ("news", J, "prop", "東京株式市場で日経平均は反発。"),
 # --- web Web 記事・ブログ ---
 ("web", E, "num idm", "I've been using this keyboard for three months now, and honestly, the only thing I'd change is the price."),
 ("web", E, "idm", "If you're new to gardening, start small: a few pots of herbs on a sunny windowsill will teach you more than any book."),
 ("web", E, "num", "## Top 5 mistakes beginners make when learning to code"),
 ("web", E, "idm neg", "It took me a while to warm up to the idea, but once I did, I couldn't go back."),
 ("web", E, "idm neg", "**Spoiler alert:** the ending isn't what you'd expect."),
 ("web", J, "hon pro", "この記事では、初心者でも迷わず設定できるように、手順を[画像つきの一覧](https://example.com/guide)で説明します。"),
 ("web", J, "idm neg", "結論から言うと、どちらを選んでも大きな差はありません。"),
 ("web", J, "pro num", "実際に1週間使ってみたところ、バッテリーの持ちが思ったより良くて驚いた。"),
 ("web", J, "prop hon pro", "京都の夏は蒸し暑いので、観光するなら朝のうちに回るのがおすすめです。"),
 ("web", J, "idm pro neg", "「走れば何とかなる」と思っていたが、現実はそう甘くなかった。"),
 # --- biz ビジネスメール ---
 ("biz", E, "hon", "Thank you for your prompt reply. I would appreciate it if you could send the revised quotation by Friday."),
 ("biz", E, "neg num hon", "Unfortunately, we will be unable to attend the meeting on March 14, as our team will be traveling that week."),
 ("biz", E, "num hon", "Please find the attached invoice ([No. 2026-0417](https://example.com/inv/2026-0417)) for last month's consulting services."),
 ("biz", E, "q hon", "I'm writing to follow up on my earlier message regarding the delivery schedule, which I have not yet received a response to; could you let me know when we might expect an update?"),
 ("biz", E, "idm", "Let's touch base next week."),
 ("biz", J, "hon prop pro", "お世話になっております。株式会社ミナトの高橋です。"),
 ("biz", J, "hon pro", "ご多忙のところ恐縮ですが、ご確認いただけますと幸いです。"),
 ("biz", J, "hon pro q", "来週の打ち合わせの件ですが、都合が悪くなりましたので、日程を変更させていただけないでしょうか。"),
 ("biz", J, "num", "添付の見積書は、消費税を含めて合計 1,320,000 円です。"),
 ("biz", J, "hon pro poly", "のちほど、こちらからお電話をおかけ直しいたします。"),
 # --- casual くだけた会話 ---
 ("casual", E, "idm neg", "Dude, you're not gonna believe what just happened."),
 ("casual", E, "q prop", "Wanna grab a coffee at Starbucks or something?"),
 ("casual", E, "idm", "I totally forgot it was your birthday, my bad!"),
 ("casual", E, "q idm", "No way! You got the job?"),
 ("casual", E, "q idm", "Can you hold my place in line for a sec? I need to run to the bathroom before it gets any worse."),
 ("casual", J, "idm q pro", "え、マジで？ 昨日あんなに飲んでたのに、もう朝から走ってきたの？"),
 ("casual", J, "pro q", "ちょっと待って、鍵どこ置いたっけ。"),
 ("casual", J, "neg pro", "別に怒ってないけど、ひと言くらい言ってほしかったな。"),
 ("casual", J, "pro idm", "今日はなんか疲れちゃったから、ご飯は適当でいいや。"),
 ("casual", J, "idm pro poly", "あの店、結構当たりだったよ。今度一緒に行こう。"),
 # --- polite 接客・丁寧な会話 ---
 ("polite", E, "q num", "Welcome! Do you have a reservation, or would you like a table for two?"),
 ("polite", E, "q hon", "I'm sorry, we're out of the salmon today. May I recommend the sea bass instead?"),
 ("polite", E, "q hon", "Could I have your name and phone number, please?"),
 ("polite", E, "num", "The check-out time is 11 a.m., but we can hold your luggage until you're ready to leave."),
 ("polite", E, "q poly", "Excuse me, is this seat taken?"),
 ("polite", J, "hon q pro", "いらっしゃいませ。何名様でいらっしゃいますか。"),
 ("polite", J, "hon pro idm", "恐れ入りますが、こちらの商品は在庫を切らしております。"),
 ("polite", J, "hon q pro", "お会計は別々になさいますか。"),
 ("polite", J, "hon pro", "ご不明な点がございましたら、お気軽に係の者にお申し付けください。"),
 ("polite", J, "hon pro", "お手数ですが、こちらのフォームにご記入をお願いいたします。"),
 # --- legal 法律・規約 ---
 ("legal", E, "neg", "The Licensee shall not sublicense, sell, or otherwise transfer the Software to any third party without the prior written consent of the Licensor."),
 ("legal", E, "prop", "This Agreement shall be governed by and construed in accordance with the laws of Japan."),
 ("legal", E, "num", "Either party may terminate this Agreement upon thirty (30) days' written notice."),
 ("legal", E, "neg", "In no event shall the Company be liable for any indirect, incidental, or consequential damages arising out of the use of the Service, even if advised of the possibility of such damages."),
 ("legal", E, "neg num", "Unless otherwise stated, all prices include consumption tax."),
 ("legal", J, "poly", "利用者は、本規約に同意した時点で、本サービスの利用を開始したものとみなします。"),
 ("legal", J, "neg pro", "当社は、事前の通知なく本サービスの内容を変更または終了することがあります。"),
 ("legal", J, "poly", "前項の規定にかかわらず、未成年者が本サービスを利用する場合は、親権者の同意を得なければならない。"),
 ("legal", J, "num", "本契約の有効期間は、令和8年4月1日から1年間とする。"),
 ("legal", J, "prop", "本件に関する一切の紛争は、東京地方裁判所を第一審の専属的合意管轄裁判所とする。"),
 # --- lit 文学的な文 ---
 ("lit", E, "idm", "The rain had stopped, but the street still held the dark memory of it."),
 ("lit", E, "idm", "She laughed, and for a moment the whole kitchen seemed to lean toward the sound."),
 ("lit", E, "neg", "He had never learned how to say goodbye; he only knew how to leave."),
 ("lit", E, "", "Silence settled over the harbor like snow."),
 ("lit", E, "q", "\"Are you coming?\" she asked, though she already knew the answer."),
 ("lit", J, "", "夕暮れの空が、ゆっくりと藍色に溶けていった。"),
 ("lit", J, "pro neg", "彼女は何も言わず、ただ窓の外を見ていた。"),
 ("lit", J, "poly", "蝉の声が、遠い夏の記憶を連れてきた。"),
 ("lit", J, "pro", "ふいに、懐かしい匂いがして、足が止まった。"),
 ("lit", J, "neg pro idm", "「ありがとう」の一言が、どうしても出てこなかった。"),
 # --- sns SNS の短文 ---
 ("sns", E, "idm", "just missed the last train lol, tonight's gonna be a long one"),
 ("sns", E, "num prop idm", "this ramen place near Shin-Okubo station is sooo good!! 10/10 would slurp again"),
 ("sns", E, "", "RT if you're still awake #insomnia"),
 ("sns", E, "", "can't believe it's already november"),
 ("sns", E, "", "@mika thx for the rec, just finished the book and wow"),
 ("sns", J, "idm pro", "今日の電車、人多すぎて死ぬかと思った…"),
 ("sns", J, "pro neg", "新作のコーヒー飲んでみた☕ 思ったより甘くなくて好き！"),
 ("sns", J, "num pro", "締め切りまであと3時間。無理。"),
 ("sns", J, "", "#今日の空 めっちゃ綺麗だった"),
 ("sns", J, "idm pro num", "推しのライブ当たった！！！人生で一番運を使った気がする"),
]

def auto_tags(lang, s):
    t = []
    # long: 日本語45字以上か英語25語以上。frag: 日本語20字以下か英語6語以下。code: バッククォート、{name}、#タグ、@宛先。md: **強調**、リンク、見出し。
    n = len(s) if lang == "ja" else len(s.split())
    if (lang == "ja" and n >= 45) or (lang == "en" and n >= 25):
        t.append("long")
    if (lang == "ja" and n <= 20) or (lang == "en" and n <= 6):
        t.append("frag")
    if re.search(r"`|\{[a-z]+\}|(?<![\w/])[#@][\w぀-鿿]", s):
        t.append("code")
    if re.search(r"\*\*|\]\(|^#{1,6} ", s):
        t.append("md")
    return t

def main():
    en = [x for x in S if x[1] == E]
    ja = [x for x in S if x[1] == J]
    assert len(en) == 50 and len(ja) == 50, (len(en), len(ja))
    rows = []
    for i, (cat, lang, tags, src) in enumerate(en + ja, 1):
        tg = (lang, "ja" if lang == "en" else "en")
        rows.append({"id": i, "src_lang": tg[0], "tgt_lang": tg[1], "category": cat,
                     "tags": tags.split() + auto_tags(lang, src), "src": src})
    out = Path(__file__).resolve().parent.parent / "data" / "sentences.jsonl"
    with open(out, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("wrote", out, len(rows))

if __name__ == "__main__":
    main()
