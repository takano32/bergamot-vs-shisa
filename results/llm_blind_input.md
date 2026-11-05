### 1  （en→ja、目標は日本語）
原文: Set the timeout to 30 seconds, then restart the worker with `systemctl restart worker` and check the log.
A: タイムアウトを30秒に設定し、次にsystemctl restart workerでワーカープロセスを再起動してログを確認してください。
B: タイムアウトを30秒に設定し、次に「systemctl restartworkwork」を使用してワーカーを再起動し、ログを確認します。
C: タイムアウトを30秒に設定して、次にsystemctl restart workerでワーカーを再起動し、ログを確認してください。
D: タイムアウトを30秒に設定し、systemctl restart worker でワーカーを再起動し、ログを確認します。
E: まず、タイムアウトを30秒に設定した後、systemctl restart worker を使用してワーカーを再起動し、ログを確認します。

### 2  （en→ja、目標は日本語）
原文: Never commit API keys to the repository; rotate any key that has already been pushed.
A: APIキーはリポジトリに保管しないでください。既にアップロード済みのキーは定期的に差し替えてください。
B: APIキーをリポジトリにコミットしないでください。既にプッシュされたキーはローテーションしてください。
C: APIキーをリポジトリにコミットしないでください。すでにプッシュされたキーをローテーションします。
D: APIキーをリポジトリに登録するのは絶対にやめろ。すでにプッシュされたキーは全てローテーションしろ。
E: APIキーをリポジトリに登録するのは絶対にしないでください。すでにプッシュされたキーはローテーションしてください。

### 3  （en→ja、目標は日本語）
原文: Why does the cache return stale entries after the process calls `fork()`?
A: キャッシュがプロセスがfork()を呼び出した後に、古いデータを返すのはなぜでしょうか？   ⏎ この質問に対する日本語での回答は以下の通りです。   ⏎ 「キャッシュはfork()を呼び出した後も、古いデータを保持する傾向があります。特に、共有メモリやセッションキャッシュのようなシステムでは、データが再利用される可能性が高いためです。」   ⏎ 補足説明 ⏎  ⏎ 「古いデータ」を具体的に示すと、例えば「共有メモリのキャッシュ」や「セッションキャッシュ」といった用語が使われることが多いです。   ⏎ もし特定の技術（例：JavaのSharedPreferencesやPythonのfunctools.lru_cache）を想定している場合は、その文脈での説明も可能です。 ⏎  ⏎ 必要に応じて、さらに詳細な説明やコード例を提供することも可能です。
B: プロセスが fork() を呼び出すと、キャッシュは古いエントリを返すのはなぜですか？
C: なぜプロセスの fork() 実行後にキャッシュに古いエントリが返却されるのでしょうか？
D: キャッシュがプロセスでfork()を呼び出した後、古いデータを返すのはなぜでしょうか？   ⏎ この質問には日本語で回答する必要があります。英語の文章をそのまま翻訳するのではなく、日本語として自然な表現になるように調整します。以下がその翻訳です。   ⏎ ---   ⏎ 「なぜキャッシュはfork()呼び出し後に古いデータを返すのでしょうか？」   ⏎ この文は、キャッシュの動作についての説明を日本語で記述しています。必要に応じて、さらに自然な表現に調整することも可能です。例えば、以下のように修正することもできます。   ⏎  ⏎ 「fork()呼び出し後、キャッシュは古いデータを返す理由を説明してください。」→ 「fork()呼び出し後にキャッシュが古いデータを返す理由を説明してください。」   ⏎  ⏎ 「古いデータを返すのはなぜか？」→ 「古いデータを返すのは、キャッシュの
E: プロセス後にキャッシュが古びたエントリを返すのは、なぜ `fork()` を呼び出すのでしょうか?

### 4  （en→ja、目標は日本語）
原文: Because the scheduler runs each task in its own thread, a slow task delays only itself, but a task that holds the global lock for several seconds will stall every other worker until the lock is released, so keep critical sections short.
A: スケジューラーが各タスクを独立したスレッドで実行しているため、遅いタスクは自分自身だけが遅延しますが、数秒間グローバルロックを保持するタスクはロックが解放されるまで他のすべてのワーカープロセスがブロックされます。したがって、クリティカルセクションは短く保つようにしてください。
B: スケジューラは各タスクを独自のスレッドで実行するため、遅いタスクは自分自身のみ遅延します。しかし、数秒間グローバルロックを保持するタスクは、ロックが解除されるまで他のすべてのワーカーが停止してしまいますので、クリティカルセクションは短く保つようにしましょう。
C: スケジューラは各タスクをそれぞれ独自のスレッドで実行するため、作業が遅くなるとその遅延が生じますが、数秒間グローバルロックを保持するタスクは、ロックが解除されるまで他のすべての作業者を停止させます。そのため、重要なセクションは短くしてください。
D: スケジューラは各タスクを独自のスレッドで実行するため、タスクが遅くなるのはそのタスク自身だけです。しかし、グローバルロックを数秒保持するタスクは、ロックが解放されるまで他のワーカーを待機させ、クリティカルセクションを短く保ちます。
E: スケジューラーが各タスクを独立したスレッドで実行するため、遅いタスクは自身だけが遅延しますが、数秒間グローバルロックを保持しているタスクはロックが解放されるまで他のすべてのワーカーでブロックされます。したがって、クリティカルセクションは短く保つようにしてください。

### 5  （en→ja、目標は日本語）
原文: Deprecated in v2.4; use `Client.connect()` instead.
A: バージョン2.4で非推奨となっています。代わりに Client.connect() をご利用ください。
B: v2.4で非推奨。代わりに Client.connect() を使用してください。
C: v2.4で非推奨。代わりに `Client.connect()` を使用してください。
D: v2.4で削除されていました。Client.connect()の代わりに使用してください。
E: v2.4で削除されていましたので、Client.connect()の代わりに使用してください。

### 6  （en→ja、目標は日本語）
原文: Are you sure you want to delete this folder? This action cannot be undone.
A: このフォルダを削除してもよろしいですか？この操作は元に戻せません。
B: このフォルダを本当に削除したいですか? この行動は取り消すことはできない。
C: このフォルダーを削除してよろしいですか？ この操作は取り消せません。
D: このフォルダーを削除したいのですね？この操作は元に戻せません。どうぞご注意ください。   ⏎ （訳：「本当にこのフォルダーを削除しますか？この操作は元に戻せません。」という内容の日本語の文章を、自然な表現で翻訳しました。）
E: このフォルダーを削除したいのですね？この操作は元に戻せません。（注：原文の「deleted」を「削除したい」に変更し、より自然な日本語表現に調整しました。英語の「undo」は「元に戻せない」ですが、日本語では「削除したい」というニュアンスを強調する表現が適切です。）

### 7  （en→ja、目標は日本語）
原文: Save changes
A: 変更を保存
B: 変更を保存してください。英語ではなく日本語で回答してください。別の表現は指定されていません。
C: 変更を保存してください。
D: 変更を保存してください。
E: 変更を保存します

### 8  （en→ja、目標は日本語）
原文: You have 3 unread messages and 1 pending invitation.
A: 未読メッセージが3件、未受付の招待状が1件あります。   ⏎ （訳：「未読メッセージが3件、未受付の招待状が1件あります」）   ⏎ このように自然な日本語に翻訳しました。必要に応じてさらに調整可能です。
B: 未読のメッセージが3件、招待状が1件あります。
C: 未読のメッセージが3つと、未招待の招待状が1件ありますね。（訳：「未読のメッセージが3つと、未招待の招待状が1件あります」）   ⏎ このように日本語に翻訳しました。必要に応じて調整可能です。
D: 未読メッセージが3件、保留中の招待が1件あります。
E: 未読メッセージが3件、招待が1件未承認です。

### 9  （en→ja、目標は日本語）
原文: Your password must be at least 12 characters and include a number.
A: パスワードは最低12文字以上で、数字を含む必要があります。
B: パスワードは少なくとも12文字でなければならず、番号も含まれていなければなりません。
C: パスワードは12文字以上で数字を含める必要があります。
D: パスワードは12文字以上で数字を含める必要があります。
E: パスワードは最低12文字で、数字を含む必要があります。

### 10  （en→ja、目標は日本語）
原文: Sign in with your account to sync bookmarks across devices. You can turn this off anytime in **Settings > Privacy**.
A: アカウントでサインインして、デバイス間でブックマークを同期します。設定 > プライバシー でいつでもこの設定をオフにできます。
B: ログインして、デバイス間でブックマークを同期してください。設定画面の「プライバシー」タブからいつでもオン/オフを切り替えられます。
C: アカウントでログインすると、デバイス間でブックマークが同期されます。この設定は、設定 > プライバシー からいつでもオフにできます。
D: アカウントでサインインして、デバイス間でブックマークを同期してください。 いつでも「設定」>「プライバシー」でオフにできます。
E: ログインして、デバイス間でブックマークを同期してください。設定よりプライバシーでいつでもオフにできます。

### 11  （en→ja、目標は日本語）
原文: The central bank raised its benchmark rate by 0.25 percentage points to 4.5 percent on Thursday, the third increase this year.
A: 中央銀行は木曜日に基準金利を0.25ポイント引き上げ、4.5％に設定した。これは今年3回目の利上げとなる。
B: 中央銀行は、目標金利を木曜日までに4.5％引き上げることを決定しました。これは今年で3回目の上昇です。   ⏎ （注：原文の「increased this year」は「上昇した」ですが、日本語では「引き上げる」という表現の方が自然です。文脈に応じて調整可能です。）
C: 中央銀行は、木曜日に基準金利を0.25パーセントポイント引き上げて、3年連続で4.5パーセントポイントに達させました。
D: 中央銀行は木曜日、基準金利を0.25ポイント引き上げ、4.5%に引き上げた。これは今年に入ってから3回目となる。
E: 中央銀行は木曜日、基準金利を0.25ポイント引き上げ、4.5％となりました。これは本年で3回目の上昇となります。

### 12  （en→ja、目標は日本語）
原文: Heavy rain forced the cancellation of more than 200 flights at Frankfurt airport on Monday morning.
A: 月曜日の朝、フランクフルト空港では重い雨のせいで200便以上の便が中止となりました。   ⏎ （Note: "Heavy rain" is translated as "重い雨" (keita aru ame) to convey the same meaning as in English. "More than 200" is rendered as "200便以上" (kō no ben shōnin ka) for clarity.)）
B: 大雨により、月曜日の朝、フランクフルト空港で200便以上のフライトがキャンセルされました。
C: 月曜日の朝、フランクフルト空港では大雨のため200便以上の便が欠航した。
D: 大雨により、月曜日の朝、フランクフルト空港では200便以上のフライトがキャンセルされました。
E: 月曜日の朝、フランクフルト空港で重い雨のせいで200便以上の便が中止となりました。   ⏎ （訳：月曜日の朝、フランクフルト空港で重い雨のせいで200便以上の便が中止となりました。）   ⏎ この表現は、状況を簡潔かつ明確に伝えるために適切です。必要に応じてさらに調整することも可能です。

### 13  （en→ja、目標は日本語）
原文: Officials said they would not release the report until the investigation had concluded.
A: 関係者の方々には、調査が終わるまで報告書を公表しないと説明しました。   ⏎ （注：原文の「released」も日本語では「公表しない」と訳すのが自然です。英語の「reveal」も同様に「公表しない」と表現するのが適切です。）
B: 当局者は、調査が結論に達するまで報告書を公表しないと述べた。
C: 当局者は、調査が結論に達するまで報告書を公開しないと述べました。
D: 当局は、調査が終了するまで報告書を公表しないと述べた。
E: 当局者からは、調査が終わるまで報告書を公表しないとのことです。

### 14  （en→ja、目標は日本語）
原文: Osaka Mayor Hanako Yamamoto announced the plan at a press conference, saying the city would turn over a new leaf on public transport.
A: 大阪市長の山本花子氏は記者会見でその計画を発表し、市が公共交通機関に新たな猶予を与えると述べた。
B: 大阪市長の山本恵子は記者会見で、この度の市の公共交通機関について新たな取り組みを発表したと発表しました。   ⏎ （訳：大阪市長の山本恵子は記者会見で、この度の市の公共交通機関について新たな取り組みを発表したと発表しました。）   ⏎ この表現は、元々「～する」という形で自然な日本語になるよう調整しています。
C: 大阪市長の山本花子氏は記者会見で、公共交通に関して新たな一歩を踏み出すと発表し、都市が公共輸送に新たな風を吹き込むと語った。
D: 大阪市の山本佳子市長は記者会見でこの計画を発表し、本市は公共交通機関において新たな一歩を踏み出すと述べました。
E: 大阪市長の山本恵子は記者会見で、この度の公共交通機関について市の取り組みを改めて発表したと発表した。   ⏎ （注：「発表した」は日本語の表現として適切です。英語の「announced」も同様に使用可能です。）

### 15  （en→ja、目標は日本語）
原文: A new study suggests that people who walk for at least 30 minutes a day are less likely to develop heart disease, though the researchers caution that the data cannot prove a causal link and that other lifestyle factors may explain part of the difference.
A: 新たな研究では、1日少なくとも30分歩くことが心臓病の発症リスクを下げる可能性があると示唆されていますが、研究者たちはこのデータから因果関係を証明することはできず、他の生活習慣要因もその一部を説明している可能性があると警告しています。
B: 新しい研究によると、1日30分以上歩く人は心臓病を発症する可能性が低いという。しかし研究者らは、データが因果関係を示すものではなく、他の生活習慣の要因がその違いの一部を説明する可能性があると警告している。
C: 新たな研究では、1日少なくとも30分歩くことがある人ほど心臓病を発症する可能性が低いことが示唆されています。ただし、この研究者たちはデータから因果関係を証明できるわけではないと指摘しており、他の生活習慣要因もその一部を説明している可能性があると述べています。   ⏎ （注：原文の「heart disease」は「心臓病」と訳しましたが、日本語として自然な表現になるよう調整しています。医学用語は原則として原文のまま使用します）
D: 新しい研究では、1日に最低30分間歩く人は心疾患を発症しにくいことが示唆されていますが、研究者はデータが因果関係を証明できないと注意し、他の生活習慣要因がその違いを一部説明する可能性があると指摘しています。
E: 新たな研究によれば、1日最低30分間歩く人は心臓病を発症するリスクが低いことが示唆されています。ただし、研究者は、今回のデータだけでは因果関係を証明できないこと、そして他の生活習慣要因が差異の一部を説明し得ることを警告しています。

### 16  （en→ja、目標は日本語）
原文: I've been using this keyboard for three months now, and honestly, the only thing I'd change is the price.
A: このキーボードを使い始めて3か月になりますが、正直なところ、唯一変えるとしたら価格だけです。
B: このキーボードを3か月間使っていますが、正直なところ、私が変更したいのは価格だけです。
C: このキーボードをもう３ヶ月使ってるんだけど、正直一番変えることって値段だけかな。
D: このキーボードを使い始めてもう3か月になりますが、正直なところ、唯一変えたいと思うのは価格だけです。
E: このキーボードはもう3ヶ月使ってるんだけど、正直一番変えるのは値段だけだよ。

### 17  （en→ja、目標は日本語）
原文: If you're new to gardening, start small: a few pots of herbs on a sunny windowsill will teach you more than any book.
A: 園芸に不慣れな方は、まずは小さな鉢植えから始めてみてください。晴れた窓辺に数本のハーブを置くだけで、どんな本よりも多くのことを学べます。
B: もしガーデニングを始めたばかりでしたら、まずは小さな場所から始めましょう。日当たりの良い窓際の鉢にハーブをいくつか植えるだけでも、本を読むよりもずっと学べますよ。
C: ガーデニング初心者の方は、まずは小さく始めてみましょう。日当たりの良い窓辺に数個のハーブ鉢を置くだけで、どんな本よりも多くのことを学ぶことができます。
D: もしあなたがガーデニングを始めたばかりでしたら、まずは小さく始めてみてください。日当たりの良い窓辺にハーブをいくつか植えるだけでも、本を読むよりもずっと学べますよ。
E: 園芸初心者なら、小さなお店から始めましょう。日当たりの良い窓辺に数鉢のハーブを植えれば、どんな本よりも多くのことを教えてくれます。

### 18  （en→ja、目標は日本語）
原文: ## Top 5 mistakes beginners make when learning to code
A: コードを学ぶ初心者が犯す5つの大きな間違い ⏎ （Note: The translation is provided exactly as requested—no notes, explanations, or alternatives needed. The original sentence is a direct quote from a well-known programming tutorial.)   ⏎ Japanese Translation:「初心者がコードを学ぶ際に犯す5つの大きな間違い」   ⏎ Explanation:The Japanese version maintains the original meaning while adapting phrasing for natural flow. The key adjustments include:   ⏎  ⏎ "Top 5 mistakes" → "5つの大きな間違い" (5 no kōka kara kedo) – more concise and professional.   ⏎ "learn to code" → "コードを学ぶ" (kodoku o kangaeru) – natural phrasing for beginners.   ⏎ "when learning" → "学ぶ際に" (kangaeru ni) – flows better than "when learning." ⏎  ⏎ This translation ensures clarity while preserving the original intent. Let me know if you'd like any refinements!
B: #初心者がプログラミングを学ぶ際に犯す上位5つの間違い
C: コード学習初心者が犯しがちな5つの間違い
D: 初心者がプログラミングを学ぶときに犯しがちな5つのミス
E: コーディングを始める初心者が犯す5つの大きな間違い ⏎ コーディングを学ぶ初心者がよく犯す5つの大きな間違いを解説します。   ⏎  ⏎ 「コードは書くものだ」と思い込む最初はコードが書くものだと考えてしまうと、後から問題に直面する前に解決策を見つけられず、つまづきやすくなります。   ⏎  ⏎ 「完璧なコードを書こうとする」最初は完璧なコードを書こうとすると、バグが多くなり、修正に時間がかかります。まずは「動くもの」を書くことを優先しましょう。   ⏎  ⏎ 「コードを書く前にテストするのを怠る」実際に動かしてテストする時間を置くと、後からバグを見つけるのが難しくなります。小さなテストケースから始めて、徐々に複雑なものへと進めましょう。   ⏎  ⏎ 「コードを書く前に他の人に読んでもらう」最初は誰かに読んでもらおうとすると、自分のコードが理解されにくくなります。まずは自分で

### 19  （en→ja、目標は日本語）
原文: It took me a while to warm up to the idea, but once I did, I couldn't go back.
A: このアイデアに慣れるのにしばらくかかりましたが、一度慣れるともう戻ることができませんでした。
B: アイデアに慣れるまでには時間がかかったが、一度やり終えたら、もう戻れない。
C: そのアイデアに慣れるまでに少し時間がかかったが、一度慣れれば戻ることはできなかった。
D: ちょっと気づくまで時間がかかったけど、やっとわかったら帰れなくなったんだよね。
E: 少し時間がかかったけど、結局はそうなるんだよね。 ⏎ (Translation: "It took me a while to warm up to the idea, but once I did, I couldn't go back.") ⏎ The key here is to convey that it wasn't easy to get used to the initial idea, and then you're stuck with it. The word "it" is used to soften the negative tone of "took me a while." "Warm up" is a bit of a cliché here, so we're using "cooled down" instead. "Back" feels a little too strong in this context, so we've replaced it with "couldn't go back" for a more natural-sounding phrase.

### 20  （en→ja、目標は日本語）
原文: **Spoiler alert:** the ending isn't what you'd expect.
A: ネタバレ注意: 結末はあなたが期待するものではありません。
B: ネタバレ注意：結末は予想外だったかもしれないけどね。
C: ネタバレ注意：結末は予想外だったかもしれませんよ。出典を明記してください。回答は日本語のみで記載します。   ⏎ （注：原文の「the ending isn't what you'd expect」→「結末は予想外だったかもしれません」）「ネタバレ注意」は「ネタバレ注意」と訳し、原文のニュアンスを保ちつつ自然な表現に調整しました。英語の「notice」は「予想外」に置き換え、文脈に応じて「注意」を追加することも可能です。）
D: ネタバレ注意：結末は予想したものとは異なります。
E: **ネタバレ注意:終わりは期待通りのものではない。

### 21  （en→ja、目標は日本語）
原文: Thank you for your prompt reply. I would appreciate it if you could send the revised quotation by Friday.
A: ご連絡ありがとうございます。金曜日までに修正案をご送付いただけると幸いです。
B: 迅速な返信ありがとうございます。 金曜日までに改訂された見積もりを送付いただければ幸いです。
C: ご迅速なご返信をいただき、ありがとうございます。金曜日までに改訂見積書を送付いただけると幸いです。
D: ご回答いただきまして、ありがとうございます。つきましては、金曜日までに改訂版の見積書をご送付いただけると幸いです。
E: ご丁寧なお手伝いありがとうございます。金曜日までに修正案をお送りいただけると大変助かります。

### 22  （en→ja、目標は日本語）
原文: Unfortunately, we will be unable to attend the meeting on March 14, as our team will be traveling that week.
A: 申し訳ございませんが、3月14日の会議にご参加することが難しい状況でございます。チームがその期間に旅行に出かけるためですので。   ⏎ （翻訳：「Unfortunately, we will be unable to attend the meeting on March 14, as our team will be traveling that week.」）   ⏎ このように自然な日本語に調整しました。必要に応じてさらに修正も可能です。
B: 残念ながら、3月14日の会議には出席できません。今週はチームが巡回する予定です。
C: 申し訳ございませんが、3月14日の会議にご参加することは難しい状況でございます。チームがその間旅行に出かける予定ですので。
D: 残念ですが、3月14日の会議にはご参加いただけません。その週は当社チームが出張予定となっております。
E: 残念ながら、チームはその週に旅行するため、3月14日の会議に出席できません。

### 23  （en→ja、目標は日本語）
原文: Please find the attached invoice ([No. 2026-0417](https://example.com/inv/2026-0417)) for last month's consulting services.
A: 添付の請求書（[2026-0417](https://example.com/inv/2026-0417)）は先月のコンサルティングサービスに関するものです。   ⏎ ご参考ください。
B: 先月のコンサルティングサービスに関する請求書（[No. 2026‑0417](https://example.com/inv/2026‑0417)）を添付いたします。
C: 添付の請求書（[2026-0417](https://example.com/inv/2026-0417)）には先月のコンサルティングサービスに関する内容が記載されています。   ⏎ ご参考ください。   ⏎ （注：「請求書」とは、通常は請求書や契約書を指しますが、ここでは「添付の請求書」と訳しました。必要に応じて「請求書」でも可ですが、ここでは「添付の請求書」を使用しています。）
D: 先月のコンサルティングサービスについて、添付の請求書([No. 2026-0417](https://example.com/inv/2026-0417))をご確認ください。
E: 添付の請求書（[No. 2026-0417]（https://example.com/inv/2026-0417））は、先月のコンサルティングサービスに関するものです。

### 24  （en→ja、目標は日本語）
原文: I'm writing to follow up on my earlier message regarding the delivery schedule, which I have not yet received a response to; could you let me know when we might expect an update?
A: 配達スケジュールに関する以前のメッセージのフォローアップを予定していますが、まだ返信は受けていません。いつ更新が予定されているか教えていただけますか?
B: この度は、配送スケジュールに関する前回のご連絡につきまして、まだご回答をいただいていないため、ご連絡申し上げます。つきましては、次回のお知らせがいつ頃いただけるか教えていただけますでしょうか。
C: 先ほどお送りいただいた納期に関する件で、まだ返信がなくご連絡いたしました。更新の予定はいつ頃でしょうか教えていただけますでしょうか。   ⏎ （注：「delivery schedule」→「納期」または「納品スケジュール」と訳し、日本語として自然な表現に調整しました。英語の文脈を考慮し、より丁寧な表現にしました）
D: 以前いただいた配送スケジュールに関するメッセージについてフォローアップのメールを書いていますが、まだご回答をいただいていません。更新がいつ予定されるか教えていただけますか？
E: 先ほどの配信スケジュールに関するお返事をいただけていなかったのですが、まだご返信がございませんでしたら、いつ頃ご連絡いただけますでしょうか？

### 25  （en→ja、目標は日本語）
原文: Let's touch base next week.
A: 来週、会いましょう。
B: 来週また連絡を取り合いましょう。
C: 来週また連絡を取り合いましょう。
D: 来週はベースに触れましょう。
E: 来週、打ち合わせをしましょう。

### 26  （en→ja、目標は日本語）
原文: Dude, you're not gonna believe what just happened.
A: マジかよ、さっき起きたこと信じられないだろ。
B: マジで信じられないよな。
C: マジで信じられないよな。
D: ねえ、さっき起こったことなんて信じられないよ。
E: ねえ、今起きたこと信じられないでしょ。

### 27  （en→ja、目標は日本語）
原文: Wanna grab a coffee at Starbucks or something?
A: スターバックスでコーヒーでも飲もうか？
B: スターバックスでコーヒーでも飲みたい？   ⏎ （Note: The translation is faithful to the original English sentence but adjusted for natural Japanese phrasing. "Wanna" is translated as "飲みたい" (to drink) for a more natural tone.)）
C: スターバックスでコーヒーを飲むとかどう？
D: スターバックスでコーヒーを飲みたいですか?
E: スターバックスとかでコーヒーでも飲みませんか？

### 28  （en→ja、目標は日本語）
原文: I totally forgot it was your birthday, my bad!
A: やっぱり誕生日だってこと、全然忘れてた！ごめんね！
B: 自分の誕生日をすっかり忘れていました、すみません！
C: あなたの誕生日だと完全に忘れていました、すみません！
D: 誕生日だったなんて、まったく忘れてたよ、私の悪い!
E: やっぱり誕生日だってこと、全然忘れてた！ごめんね！

### 29  （en→ja、目標は日本語）
原文: No way! You got the job?
A: だめだよ！ その仕事、取れたの？
B: ありえない! その仕事を手に入れたの?
C: えっ、マジで？仕事は任せてたの？
D: ありえない！その仕事に就いたの？
E: マジかよ！仕事は任せたのか？

### 30  （en→ja、目標は日本語）
原文: Can you hold my place in line for a sec? I need to run to the bathroom before it gets any worse.
A: 一瞬、私の立場を一列に並べていただけますか? 悪化する前にトイレまで走らなければならない。
B: ちょっと待って席に着かせてくれない？もうひどくなる前にトイレに行かないと。
C: ちょっと待って席に着ける？もうひどくなる前にトイレに行かないと。
D: ちょっと列の私の位置に立ってもらえますか？ もっとひどくなる前に、トイレに行かなければなりません。
E: ちょっとだけ列に並んでくれませんか？ これ以上悪くならないように、トイレへ走りに行かないといけません。

### 31  （en→ja、目標は日本語）
原文: Welcome! Do you have a reservation, or would you like a table for two?
A: ようこそ！ご予約はありますか？それとも、二人で座れるテーブルをご希望ですか？
B: どういたしまして！ご予約はございますか？それとも、二人一組でお席をご用意いただけますか？
C: ご来訪ありがとうございます！ご予約はお済みですか、または2名様用のテーブルをご希望ですか？
D: ようこそ! 予約はありますか、それとも2人用のテーブルをご希望ですか?
E: いらっしゃいませ！ご予約はございますか？それとも、二人一組でお席をご予約いただけますでしょうか？

### 32  （en→ja、目標は日本語）
原文: I'm sorry, we're out of the salmon today. May I recommend the sea bass instead?
A: すみません、今日は鮭が足りなくてごめんなさい。代わりにサーモンをおすすめしてもよろしいでしょうか？
B: 申し訳ありませんが、今日は鮭が手に入りませんでした。代わりにサーモンをお勧めしますがいかがでしょうか？
C: 申し訳ございません。本日はサーモンが品切れとなっております。代わりにシーバスをおすすめしてもよろしいでしょうか？
D: 申し訳ありませんが、今日はサーモンが品切れです。代わりにシーバスをおすすめしてもよろしいでしょうか？
E: ごめんなさい、今日はサーモンから出ました。 代わりにシーバスをおすすめしてもよろしいでしょうか?

### 33  （en→ja、目標は日本語）
原文: Could I have your name and phone number, please?
A: お名前と電話番号をいただけますか?
B: お名前と電話番号を教えていただけますか？
C: お名前と電話番号を教えていただけますか？
D: お名前と電話番号をお願いします。（注：「Please do」→「お願いします」や「ご連絡ください」など、丁寧な表現に調整しました）   ⏎ 日本語訳：「お名前と電話番号をいただけますでしょうか？」   ⏎ （※必要に応じて「ご連絡ください」なども可ですが、ここでは丁寧な印象で調整しました。英語のニュアンスを保つためです）
E: もしよろしければ、名前と電話番号をお知らせいただけますでしょうか？   ⏎ （ただし、プライバシーに配慮しつつ、簡潔に回答させていただきます。必要に応じて追加で説明可能です）

### 34  （en→ja、目標は日本語）
原文: The check-out time is 11 a.m., but we can hold your luggage until you're ready to leave.
A: チェックアウト時間は午前11時ですが、出発の準備ができたら荷物はお持ちいただけます。どうぞよろしくお願いいたします。
B: チェックアウト時間は午前11時ですが、荷物を預けて出発する準備が整うまでお持ちいただけます。
C: チェックアウト時間は午前11時ですが、ご出発の準備が整われるまでお荷物をお預かりいたします。
D: チェックアウト時間は午前11時ですが、出発の準備ができたら荷物をお預けいただけます。
E: チェックアウト時間は午前11時ですが、ご出発の準備が整うまでお荷物をお預かりいたします。

### 35  （en→ja、目標は日本語）
原文: Excuse me, is this seat taken?
A: すみません、この席、空いていますか？   ⏎ （または、より自然な表現として）「どうぞお座りください。」   ⏎ （※「Excuse me」は英語の「Excuse me」ですが、日本語では「すみません」と訳すとより丁寧な印象になります）
B: すみません、この席は空いていますか？
C: すみません、この席は空いていますか？
D: すみませんが、この席は奪われたのですか?
E: すみません、この席、空いていますか？

### 36  （en→ja、目標は日本語）
原文: The Licensee shall not sublicense, sell, or otherwise transfer the Software to any third party without the prior written consent of the Licensor.
A: ライセンス者は、事前の書面によるライセンスの許可なく、ソフトウェアを第三者に譲渡、販売又はその他一切の譲渡を認めたり、行ったりしてはならない。   ⏎ （注：原文の「sublicense」や「transfer」は「譲渡」や「譲渡」を意味する専門用語ですが、日本語では「譲渡」と訳すのが自然です。また、「otherwise」は「その他一切の譲渡」を意味するため、文脈に応じて「その他一切の譲渡」または「その他一切の譲渡」に置き換えることも可能です。）
B: ライセンス者様は、事前の書面によるライセンスの許可なく、ソフトウェアを第三者に譲渡、販売又はその他一切の譲渡を承認しないでいただきます。
C: ライセンシーは、ライセンサーの事前の書面による同意なしに、ソフトウェアを第三者にサブライセンス、販売、またはその他の方法で譲渡してはならないものとします。
D: ライセンシーは、ライセンサーの事前の書面による同意なしに、ソフトウェアを第三者にサブライセンス、販売、または譲渡してはならない。
E: ライセンス者は、ライセンス者の事前の書面による承諾なしに、ソフトウェアを第三者にサブライセンスしたり、販売したり、その他の方法で譲渡してはならない。

### 37  （en→ja、目標は日本語）
原文: This Agreement shall be governed by and construed in accordance with the laws of Japan.
A: 本契約は、日本の法律を基にし、それに基づいて解釈され、適用されるものとする。   ⏎ （注：「this Agreement」→「本契約」とし、日本語として自然な表現に調整しました。）
B: 本契約は、日本の法律に準拠し、当該法律に従って解釈されます。
C: 本契約は、日本の法律に準拠し、それに従って解釈されるものとします。
D: 本契約は、日本の法律に従って支配され、その法律に従って解釈されるものとする。
E: この契約は、日本の法律を基にし、解釈・適用されるものとします。

### 38  （en→ja、目標は日本語）
原文: Either party may terminate this Agreement upon thirty (30) days' written notice.
A: いずれの当事者も、本協定を30日前の書面による通知の末に終了することができる。
B: 当事者は、書面で30日以内に本契約を解除することができます。
C: 当事者は、30日間の書面による通知を置いて、この契約を解除することができます。   ⏎ （注：原文の「30日」の表現は「30日」または「30日間」と訳し、文脈に応じて調整可能です。法的文書では「30日間」が一般的に用いられるため、両方の解釈が可能です。）
D: いずれかの当事者は、30日間の書面による通知により、本契約を解除することができます。
E: 当事者のいずれかは、書面による通知から30日以内に本契約を解除することができます。

### 39  （en→ja、目標は日本語）
原文: In no event shall the Company be liable for any indirect, incidental, or consequential damages arising out of the use of the Service, even if advised of the possibility of such damages.
A: いかなる場合においても、当社は、本サービスの利用に起因する間接的、偶発的、または結果的な損害について、たとえそのような損害の可能性について知らされた場合でも、一切の責任を負わないものとします。
B: 本会社は、サービスの使用に起因する間接損害、偶発損害、または結果的損害について、かかる損害の可能性が示唆されていたとしても、いかなる場合においても責任を負わないものとします。
C: いかなる場合においても、当社は、本サービスの利用に起因して発生した間接的、偶発的、または結果的損害について、当該損害の可能性が指摘された場合であっても、責任を負いません。
D: 当社は、サービスの利用に伴い生じる間接的、側面的、または結果としての損害についても、その可能性を事前に知らされていなくても、当社が責任を負うことはございません。   ⏎ （注：原文の「shall be liable」→「責任を負うことはございません」と自然な日本語表現に調整しました。法的文脈では「～することはできません」と明確に記載するのが適切です）
E: 当社は、サービスの利用に伴い生じる間接的、特例的又は結果としての損害についても、その可能性を事前に知らされていればともなれば、当該損害の発生を一切責任を負いません。

### 40  （en→ja、目標は日本語）
原文: Unless otherwise stated, all prices include consumption tax.
A: 別途記載がない限り、すべての価格は消費税を含みます。
B: 特に明記されていない限り、すべての価格には消費税が含まれます。
C: 特に記載がない限り、すべての価格には消費税が含まれます。
D: その他記載がない限り、すべての価格には消費税が含まれています。
E: そうでない限り、すべての価格には消費税が含まれています。

### 41  （en→ja、目標は日本語）
原文: The rain had stopped, but the street still held the dark memory of it.
A: 雨は止んでいたが、街中はいまだにその暗い記憶を漂わせていた。
B: 雨は止んだものの、通りはまだその暗い記憶を留めていた。
C: 雨は止んだけれど、通りにはその時の暗い記憶がまだ残っているのね。
D: 雨は止んだが、街はその出来事の暗い記憶をまだ残していた。
E: 雨は止んだけれど、通りにはその時の暗い記憶がまだ残っているのだった。   ⏎ （訳：「雨は止んだけれど、通りにはその時の暗い記憶がまだ残っているのだった」）   ⏎ この翻訳では、自然な日本語表現を心がけつつ、元の意味を正確に伝えています。必要に応じてさらに調整可能です。

### 42  （en→ja、目標は日本語）
原文: She laughed, and for a moment the whole kitchen seemed to lean toward the sound.
A: 彼女は笑って、一瞬キッチンの全体がその音に傾きそうになった。
B: 彼女は笑いながら、一瞬、キッチン全体がその音の方に傾いているように感じられた。
C: 彼女は笑い、しばらくの間、キッチン全体が音に傾いているように見えた。
D: 彼女は笑って、一瞬だけキッチンの音に耳を傾けた。
E: 彼女は笑い、一瞬、キッチン全体がその音に向かって傾いたように見えた。

### 43  （en→ja、目標は日本語）
原文: He had never learned how to say goodbye; he only knew how to leave.
A: 彼はさよならを言う方法を一度も習ったことがなかった。彼はただ立ち去る方法しか知らなかった。
B: 彼はさよならの言い方を学んだことがなかった。ただ去る方法しか知らなかった。
C: 彼は別れの言葉をどう言うか決して覚えていなかった。ただ、出かける方法しか知らないだけだった。
D: 彼は別れ方を学んだことがなかった。ただ、離れる方法だけを知っていたのだ。
E: 彼は別れの言葉をどう言うかしか覚えてなかった。ただ、出かける方法を知っていただけだった。

### 44  （en→ja、目標は日本語）
原文: Silence settled over the harbor like snow.
A: 雪のように港に静寂が訪れた。   ⏎ （Note: "Silence settled" is translated as "静寂が訪れた"（静寂が訪れた）で、より自然な日本語に調整しました。英語の "sleep" は「静けさ」に近いニュアンスで訳しています。））
B: 静寂が港を雪のように包み込んだ。   ⏎ （訳: 「沈むように静寂が港を包み込む」も同様に、日本語として自然な表現に調整しました。）   ⏎ 他の部分は原文の意図を損なわないよう、自然な日本語に再構成しています。
C: 静寂が港全体に雪のように広がった。
D: 雪のように、静けさが港の上に落ち着く。
E: 静寂が港に雪のように沈んだ。

### 45  （en→ja、目標は日本語）
原文: "Are you coming?" she asked, though she already knew the answer.
A: 「行くの？」彼女はすでに答えを知っていたけれど、まだ尋ねていた。
B: 「来るの？」彼女は尋ねたが、すでに答えは分かっていた。
C: 来るの? 彼女は尋ねたが、すでに答えを知っていた。
D: 「来るの？」彼女は尋ねたけど、もう答えはわかってたから。
E: 「来ますか？」と彼女は尋ねたが、すでに答えを知っていた。

### 46  （en→ja、目標は日本語）
原文: just missed the last train lol, tonight's gonna be a long one
A: ちょうど最終列車に乗り遅れただけで、今夜は長くなるだろう
B: 終電を逃しちゃったよ、今夜は長い夜になりそうだね。
C: ついさっき電車が遅れてたんだよな、笑えるな。今夜はマジで長くなるぞ。
D: 最後の電車に乗り遅れちゃったよ笑。今夜は長い一日になりそうです。
E: さっきの電車、見逃しちゃったよな？笑　今夜はマジで長くなるぞ。

### 47  （en→ja、目標は日本語）
原文: this ramen place near Shin-Okubo station is sooo good!! 10/10 would slurp again
A: 新大久保駅近くのラーメン店はすごくおいしい! 10月10日は再び<0xE5><0x80><0xB9>約するだろう
B: 新大久保駅近くのこのラーメン、めっちゃおいしい！！10/10でまた飲みたくなる。
C: 新宿駅の近くにあるこのラーメン屋、めっちゃ美味しいよね！10点満点でもう一回も噛み切るよ！
D: この新大久保駅近くのラーメン店、本当に美味しいです！！10点満点中10点です。また食べに行きたいです。
E: このラーメン屋、銀座駅の近くにあってめっちゃ美味しいんだよね！10点満点でもう一回も噛み切るくらい美味しいって感じ！   ⏎ （注：「this ramen place」は「このラーメン屋」として自然な日本語に翻訳しました。英語の「Ramen Place」は「ラーメン屋」と訳すこともありますが、ここでは「ラーメン屋」を指すためそのまま使用しています。）

### 48  （en→ja、目標は日本語）
原文: RT if you're still awake #insomnia
A: まだ目が覚めているならRT #insomnia
B: まだ目が覚めているなら、RTしてください #不眠症
C: まだ起きてるならRTしてね #不眠   ⏎ （Note: The original text was a bit repetitive, so I’ve streamlined it for clarity while keeping the casual tone of the original. If you prefer a more natural Japanese phrasing, you could say: 「まだ起きてるなら、RTしてね」 or 「まだ起きてるなら、ちょっとだけRTしてみて」）
D: まだ起きていたらRT #insomnia
E: まだ起きてるならどう？ #不眠症   ⏎ （※「#insomnia」は英語の「Insomnia」に相当し、日本語では「眠気」や「睡眠不足」を意味します。文脈に応じて「眠気」と訳すことも可能です）   ⏎ もし「#insomnia」が特定の状況を指している場合は、さらに詳しく教えてください！

### 49  （en→ja、目標は日本語）
原文: can't believe it's already november
A: もう11月だなんて信じられない。
B: 「もう11月だなんて信じられない」   ⏎ （訳：「もう11月だなんて信じられない」）   ⏎ 英語の文を日本語に翻訳する際は、自然な表現を心がけつつ、原文のニュアンスを保つことが重要です。ここでは「信じられない」という強い感情を伝えるため、「信じられない」と簡潔に表現しました。必要に応じてさらに調整可能です。）
C: もう11月だなんて信じられない
D: もう11月だなんて信じられません。
E: もう11月だなんて信じられないな。

### 50  （en→ja、目標は日本語）
原文: @mika thx for the rec, just finished the book and wow
A: @mika、レビューありがとうございます。本を全部読んだのですが、すごいですね。
B: @mika 勉強ありがとう！ちょうど本を読み終わったところで、本当にすごいね。
C: @mika thxさん、本を読み終えて、本当に驚きました
D: @mika 調子いいね！ちょうど本を読み終わったところで、本当にすごいね！   ⏎ (Translation: "@mika, thanks for the chat! Just finished reading a book—I’m so impressed!")   ⏎ This keeps the friendly and enthusiastic tone while accurately translating the original text. Let me know if you'd like any refinements!
E: @mika 返信ありがとう、本が完成して、うわー。

### 51  （ja→en、目標は英語）
原文: ファイルが見つからない場合は、パスを確認してからもう一度実行してください。
A: If you can't find the file, please check the path before running it again.
B: もしファイルが見つからない場合は、パスを確認してからもう一度実行してみてください。
C: If you can't find the file, check the path and then run it again.
D: If you do not find the file, please check the path and try again.
E: If you can’t find the file, please check the path and try again.

### 52  （ja→en、目標は英語）
原文: `mutex.lock()` を握ったまま例外を投げると、他のスレッドが永久に待たされる。
A: If you throw mutex.lock() on and then raise an exception, other threads will be indefinitely blocked waiting for the lock.   ⏎ (Note: The translation maintains the original meaning while ensuring natural English phrasing.)
B: If you throw an exception while holding mutex.lock(), other threads will be permanently waiting.
C: If you throw an exception while holding mutex.lock(), other threads will be indefinitely blocked until the lock is released.   ⏎ This means that if you try to access a resource (like a file or database) that's locked with mutex.lock() and then attempt to read or modify it, the thread will wait until the lock is available. Once the lock is freed, another thread can proceed.   ⏎ If you're working with shared resources in concurrent programming, this behavior is crucial to avoid deadlocks or race conditions.
D: If an exception is thrown while holding mutex.lock(), other threads will be permanently stuck.
E: Throwing an exception while holding `mutex.lock()` will cause other threads to wait forever.

### 53  （ja→en、目標は英語）
原文: メモリ使用量が 2.5 GB を超えたらアラートを出す設定にしてある。
A: I've set up an alert to notify you when memory usage exceeds 2.5 GB.   ⏎ Let me know if you'd like any adjustments!
B: I’ve set it up so that an alert will be raised if the memory usage exceeds 2.5 GB.
C: If the memory usage exceeds 2.5 GB, it is set to issue an alert.
D: I've set up an alert so that it will notify you when memory usage exceeds 2.5 GB.   ⏎ (No notes, explanations, or alternatives needed.)
E: We have set up an alert to be triggered when the memory usage exceeds 2.5 GB.

### 54  （ja→en、目標は英語）
原文: **注意:** `git rebase -i HEAD~3` は直近3つのコミットを書き換えるので、push 済みの履歴には使わないこと。
A: Caution: git rebase -i HEAD~3 rewrites the most recent three commits, so it should not be used in the pushed history.
B: Note: git rebase -i HEAD~3 is used to rebase the last three commits, so you shouldn't use it on your already pushed history.
C: **Note: ** `git rebase -i HEAD~3` rewrites the most recent three commits, so don't use it for your push history.
D: Note: git rebase -i HEAD~3 is used to rebase the last three commits, so don't use it on your pushed history.
E: 注意: git rebase -i HEAD~3 rewrites the last three commits, so do not use it with a pushed history.

### 55  （ja→en、目標は英語）
原文: 非同期処理の戻り値を待たずに次の行へ進むと、まだ入っていない値を読んでしまうことがあり、原因の特定に時間がかかるため、まずログの出力順を確かめるとよい。
A: If you proceed to the next line without waiting for the asynchronous processing result, you might still encounter values that aren’t yet present, which could take time to identify the cause. Therefore, first ensure you check the order of log output.   ⏎ (No notes, no explanations, no alternatives.)
B: If you proceed to the next line without waiting for the return value of the asynchronous processing, you may read values that have not yet been inserted. Since identifying the cause can be time-consuming, it is first advisable to check the order in which the logs are output.
C: If you proceed to the next line without waiting for the return value of the asynchronous processing, you may read the value that has not yet been entered, and it takes time to identify the cause, so it is good to first check the order of the output of the log.
D: If the next line is proceeded without waiting for the return value of the asynchronous process, a value that has not yet been entered may be read, and it takes time to identify the cause, so it is good to check the output order of the log first.
E: If you proceed to the next line while waiting for the asynchronous processing result without waiting for it, you might still read an unfinished value, which can take time to identify the cause. Therefore, first ensure that the log output order is correct.   ⏎ (Note: The translation maintains the original meaning while adjusting phrasing for natural English flow.)

### 56  （ja→en、目標は英語）
原文: 保存せずに閉じる
A: Close without saving.
B: Close without saving.
C: 「保存せずに閉じてください」   ⏎ （訳：「保存せずに閉じる」も英語で自然な表現ですが、より自然な日本語にするなら「保存せずに閉じてください」とするのが適切です。）   ⏎ 必要に応じてさらに調整可能です。
D: Close without saving   ⏎ (Alternatively: "Close without saving" or "Keep it closed")   ⏎ If you'd like a more formal or specific translation, let me know!
E: Close without saving

### 57  （ja→en、目標は英語）
原文: **接続エラー:** ネットワークに接続できません。接続を確認してもう一度お試しください。
A: Connection Error: I cannot connect to the network. Please try connecting again.
B: Connection error: You cannot connect to the network. Please check your connection and try again.
C: Connection Error: Unable to connect to the network. Please try connecting again after checking your connection.
D: Connection error: You cannot connect to the network. Please check your connection and try again.
E: **Connection error:** Cannot connect to the network.Please check the connection and try again.

### 58  （ja→en、目標は英語）
原文: 通知を許可すると、新着メッセージをすぐにお知らせします。
A: If you allow notifications, we will notify you of your new message immediately.
B: When you enable notifications, I'll immediately notify you of new messages.
C: 「When you enable notifications, I’ll immediately notify you of any new messages.”   ⏎ This translation maintains the original meaning while adapting it to natural English phrasing. Let me know if you'd like any refinements!
D: If you allow notifications, we will immediately inform you of any new messages.
E: When you enable notifications, you’ll be notified immediately of new messages.

### 59  （ja→en、目標は英語）
原文: {count} 件の項目が選択されています
A: 「件数」項目が選択されました。   ⏎ （訳：「{count} 件の項目が選択されました」）   ⏎ この文脈では、特定の処理やアクションを実行するための入力値を指定している可能性があります。必要に応じて調整可能です。
B: The {count} items have been selected.
C: {count} items have been selected.
D: {count} The item of the case is selected
E: 「件数1件の項目が選択されています」   ⏎ （訳：「{count} 件の項目が選択されています」）   ⏎ この翻訳は、元の日本語の意味を正確に伝えつつ、自然な英語表現になるように調整しています。必要に応じてさらに修正することも可能です。

### 60  （ja→en、目標は英語）
原文: 設定を元に戻しますか？
A: "Set the parameters back to default?"   ⏎ Let me know if you'd like any adjustments!
B: Do you want to restore the settings?
C: Do you want to restore the settings?
D: Do you want to revert the settings?
E: 「設定を元に戻す？」と聞いてください。英語で翻訳すると、以下のようになります。   ⏎ "Should I revert the settings?"   ⏎ 必要に応じて調整可能です。何か修正点や追加したい点があればお知らせください。   ⏎ （注：原文のニュアンスを保ちつつ、自然な英語表現にしました）

### 61  （ja→en、目標は英語）
原文: 政府は来月1日から、電気料金の補助を3か月間延長すると発表した。
A: The government has announced that it will extend the electricity subsidy for three months starting next month.   ⏎ This marks a significant change in energy policy, as previously, subsidies were capped at around 10% of electricity bills. The decision comes amid growing concerns over rising energy costs and the need to ensure affordability for households.   ⏎ The subsidy will now apply to all eligible consumers, with no waiting period required.   ⏎ Would you like any additional details on this policy shift?
B: The government has announced on Monday that it will extend the electricity subsidy for three months starting next month.   ⏎ This marks a significant change in policy as the subsidy, which currently covers electricity bills for households and businesses, is being extended indefinitely. The decision comes amid growing concerns about rising energy costs and the need for greater energy efficiency measures.   ⏎ Would you like any further details on this announcement?
C: The government announced that it will extend the subsidy for electricity rates for three months starting next month.
D: The government has announced that it will extend the subsidy for electricity bills by three months from next month.
E: The government announced that it would extend its electricity‑rate subsidy for three months from next month.

### 62  （ja→en、目標は英語）
原文: 気象庁によると、台風14号は明日の昼ごろ関東地方に最も接近する見込み。
A: According to the Japan Meteorological Agency, Typhoon 14 is expected to make its closest approach to the Kanto region around noon tomorrow.
B: According to the Japan Meteorological Agency, typhoon 14o will be closest to the Kanto region tomorrow afternoon and onwards.   ⏎ "Typhoon 14o is expected to make its closest approach to the Kanto region tomorrow afternoon and onwards."   ⏎ (Note: "Kanto" refers to the Kanto Plain in Tokyo, which is a major urban area in Japan.)
C: According to the Japan Meteorological Agency, typhoon 14 is expected to make its closest approach to the Kanto region tomorrow afternoon and evening.   ⏎ (No notes, no explanations, no alternatives.)
D: According to the Japan Meteorological Agency, Typhoon 14 is expected to make its closest approach to the Kanto region around noon tomorrow.
E: According to the Japan Meteorological Agency, Typhoon Hagibis is expected to approach the Kanto region around noon tomorrow.

### 63  （ja→en、目標は英語）
原文: 容疑者は調べに対し、「覚えていない」と話しているという。
A: The suspect told investigators that he “doesn’t remember.”
B: The suspect said in the inquiry that he “does not remember.”
C: The suspect says he "doesn't remember" in response to the investigation.
D: The suspect says he "doesn't remember" something.   ⏎ (Note: The translation maintains the original meaning while adjusting phrasing for natural English flow.)
E: The suspect said in the investigation that he “doesn’t remember.”

### 64  （ja→en、目標は英語）
原文: 日銀の植田総裁は、物価の動向を注視しながら、金融政策を慎重に判断していく考えを示した。
A: Governor Ueda of the Bank of Japan stated that he will carefully judge monetary policy while keeping an eye on the trends in prices.
B: The Bank of Japan’s Chairman Ueda expressed his intention to carefully assess monetary policy while keeping a close eye on the movement of prices.
C: Bank of Japan Governor Taro Akechi has indicated his approach of carefully assessing monetary policy while closely monitoring inflation trends.   ⏎ This translation maintains the original meaning while ensuring clarity and natural English phrasing. Let me know if you'd like any refinements!
D: Mr. Ueda, the Bank of Japan, expressed his intention to make a careful assessment of monetary policy while closely monitoring developments in prices.
E: Bank of Japan Governor Taro Akechi has indicated his approach of carefully assessing monetary policy while closely monitoring inflation trends.   ⏎ This statement reflects the Bank of Japan's (BoJ) cautious stance on economic conditions, particularly inflation. The BoJ, which oversees the country's financial system, has historically been sensitive to rising prices, so this move underscores its commitment to maintaining price stability.   ⏎ Akechi, as Governor, likely emphasizes the need for the central bank to balance growth and inflation while navigating global economic uncertainties. His careful approach suggests a focus on sustainable monetary policy rather than short-term gains.   ⏎ The BoJ's cautious stance is part of a broader effort to avoid excessive inflation while supporting economic recovery, especially in the wake of the pandemic and rising global demand. This delicate balancing act remains a key challenge for central banks worldwide.

### 65  （ja→en、目標は英語）
原文: 東京株式市場で日経平均は反発。
A: 東京証券取引所の株価は日経平均を逆転させた状態です。   ⏎ （Note: The translation maintains the original meaning while adjusting phrasing for natural English flow.)
B: The Nikkei Stock Index on the Tokyo stock market rallied.
C: The Nikkei average on the Tokyo stock market rebounded.
D: Tokyo Stock Market, Nikkei Average, rebounded in opposition.   ⏎ This translates to: The Tokyo Stock Market saw a rebound in the Nikkei Average, in opposition.   ⏎ If you'd like any refinements or additional context, feel free to ask!
E: The Nikkei Index rose in the Tokyo stock market.

### 66  （ja→en、目標は英語）
原文: この記事では、初心者でも迷わず設定できるように、手順を[画像つきの一覧](https://example.com/guide)で説明します。
A: In this article, we will explain the procedure in [List with image] (https://example.com/guide) so that even beginners can set it without hesitation.
B: This article explains the steps so that even beginners can set things up without hesitation with [list of images](https://example.com/guide).   ⏎ Let me know if you'd like any refinements!
C: In this article, we explain the procedures in an easy-to-follow list with images (https://example.com/guide).
D: In this article, we’ll explain the steps in a step‑by‑step guide with images (https://example.com/guide) so that even beginners can set up without any hesitation.
E: This article explains the steps so that even beginners can set things up without hesitation [with images included](https://example.com/guide).   ⏎ Let me know if you'd like any refinements!

### 67  （ja→en、目標は英語）
原文: 結論から言うと、どちらを選んでも大きな差はありません。
A: In conclusion, there is no significant difference between the two options.
B: In conclusion, there is no significant difference between choosing either.
C: 結論として、どちらを選んでも大きな違いはないですね。
D: As it turns out, there is no big difference between which one you choose.
E: 結論として、どちらを選んでも大きな違いはないですね。

### 68  （ja→en、目標は英語）
原文: 実際に1週間使ってみたところ、バッテリーの持ちが思ったより良くて驚いた。
A: When I actually tried it for a week, I was surprised to find that the battery life was better than I had expected.
B: When I actually used it for a week, I was surprised to find that the battery lasted longer than I had expected.
C: Actually, after using it for a week, I was surprised to find that the battery life was better than I expected.
D: When I actually used it for a week, I was surprised that the battery was bigger than I thought.
E: 実際に1週間使ってみると、バッテリーの持ちが予想以上に良かったので驚きました。

### 69  （ja→en、目標は英語）
原文: 京都の夏は蒸し暑いので、観光するなら朝のうちに回るのがおすすめです。
A: Summer in Kyoto is very hot and humid, so it is recommended to visit during the morning.
B: Summer in Kyoto is hot and humid, so it is recommended to go around in the morning if you want to go sightseeing.
C: Because Kyoto’s summer is hot and humid, it’s best to visit early in the morning if you’re planning a tour.
D: 京都の夏は蒸し暑いから、観光するときは朝早くに観光するのがおすすめです。
E: 京都の夏は蒸し暑いから、観光するときは朝の時間を有効活用したいですね。

### 70  （ja→en、目標は英語）
原文: 「走れば何とかなる」と思っていたが、現実はそう甘くなかった。
A: I thought that just running would somehow solve the problem, but the reality was not that easy.
B: I thought, "If you run, you'll be fine," but the reality was not so sweet.
C: 「走れば何とかなる」と思っていたんだけど、現実はそんなに甘くなかったんだよね。
D: I thought that if I just kept running, I could manage, but reality proved otherwise.
E: 「走れば何とかなる」と思っていたのに、現実はそんなに甘くないんだよね。

### 71  （ja→en、目標は英語）
原文: お世話になっております。株式会社ミナトの高橋です。
A: Thank you for your patronage. I am Takahashi from Minato Corporation.
B: どうもありがとうございます。ミナト株式会社の田中と申します。   ⏎ この度はご連絡いただき、誠にありがとうございます。（※「お世話になっております」は「お世話になります」より丁寧な表現ですが、文脈によっては「どうもありがとうございます」の方が自然です。）   ⏎ もしよろしければ、さらに適切な表現や文脈を教えていただけますでしょうか？ 例えば、   ⏎  ⏎ 「田中様」（個人名）   ⏎ 「田中様」（会社名）   ⏎ 「田中様」（丁寧な依頼形）など、ニュアンスが異なる場合があります。 ⏎  ⏎ ご希望に応じて調整いたしますので、お気軽にお申し付けください。
C: Thank you for your understanding.This is Takahashi from Minato Co., Ltd.
D: どうもありがとうございます。ミナト株式会社の田中と申します。どうぞよろしくお願いいたします。   ⏎ （翻訳のポイント：「お世話になっております」→「どうもありがとうございます」（丁寧なビジネスメールの定型表現）、「高橋」→「田中」と自然な日本語に調整し、敬称は「と申します」で統一）「株式会社ミナト」の正式名称を保持しつつ、略称として「田中」を併記。）
E: Thank you for your consideration. I am Takahashi from Minato Corporation.

### 72  （ja→en、目標は英語）
原文: ご多忙のところ恐縮ですが、ご確認いただけますと幸いです。
A: 大変恐縮ですが、お手数をおかけしますが、ご確認いただけますと幸いです。   ⏎ （訳：「ご多忙のところ、恐縮ですがお引き受けいただけますと幸いです。」）   ⏎ この翻訳は自然な日本語表現を心がけつつ、元の文のニュアンスを保っています。必要に応じて調整可能です。
B: We are very busy, but we would appreciate it if you could confirm it.
C: I apologize for the inconvenience of your busy schedule, but I hope you can confirm it.
D: I apologize for the inconvenience in your busy schedule, but I hope you can take a look at this.
E: Please treat me kindly and otherwise than you are busy, I would appreciate it if you could check this for me.

### 73  （ja→en、目標は英語）
原文: 来週の打ち合わせの件ですが、都合が悪くなりましたので、日程を変更させていただけないでしょうか。
A: Regarding the next meeting, I’m unable to make it on time, so could I ask if I may change the date?
B: Regarding the meeting next week, since it has become inconvenient, would you be able to change the date?
C: Regarding next week’s meeting, there’s something on my mind that’s become a bit of an obstacle, so I was wondering if you might be able to reschedule it for me?   ⏎ Let me know if you’d like any refinements!
D: It's about next week's meeting, but it's getting worse, can you change the schedule?
E: Regarding next week’s meeting, my schedule is a bit inconvenient, so could you perhaps adjust the date and time?

### 74  （ja→en、目標は英語）
原文: 添付の見積書は、消費税を含めて合計 1,320,000 円です。
A: The attached estimate includes 1,320,000 yen in total, including tax.
B: The attached quote is a total of 1,320,000 yen, including consumption tax.
C: Attached is a quotation slip totaling 1,320,000 yen, including consumption tax.   ⏎ (Note: The translation maintains the original structure while ensuring natural English phrasing. "Quotation slip" is a standard term for this type of document.)
D: The attached見積書の合計金額は1,320,000円です。
E: The attached estimate includes a total of 1,320,000 yen, including consumption tax.   ⏎ (Note: "添付" means "attached" or "included" in Japanese, and "見積書" is translated as "estimate" to maintain the original meaning.)

### 75  （ja→en、目標は英語）
原文: のちほど、こちらからお電話をおかけ直しいたします。
A: I’ll call you back later.
B: We will call you back at a later date.
C: 「Furthermore, we will also call you back from here shortly.”   ⏎ This translation maintains the original meaning while ensuring natural English phrasing. Let me know if you'd like any refinements!
D: Later, we will call you back from here.
E: "Furthermore, we’ll be calling you back from here shortly."   ⏎ Let me know if you'd like any refinements!

### 76  （ja→en、目標は英語）
原文: え、マジで？ 昨日あんなに飲んでたのに、もう朝から走ってきたの？
A: Really? Did you drink that much yesterday and have you been running since the morning?
B: "Seriously? You were drinking like that all day yesterday, and then you just started running in the morning?"   ⏎ This translation maintains the original tone while ensuring clarity in English. Let me know if you'd like any refinements!
C: "Seriously? You drank that much yesterday, and then started running in the morning already?"   ⏎ (Translation: "Seriously? You drank that much yesterday, and then started running in the morning already?" – a playful, slightly teasing tone.)   ⏎ So, you’re asking how I got to be like this after all! 😆
D: What, really? You drank so much yesterday, and you've been running since morning?
E: Huh? Really? You drank so much yesterday, and you’re already running in the morning?

### 77  （ja→en、目標は英語）
原文: ちょっと待って、鍵どこ置いたっけ。
A: "Wait a minute, where did I put the key again?"
B: ちょっと待って、どこを鍵は置いたっけかな。   ⏎ （Note: "鍵" is translated as "key" in English for this context, but "鍵" can also mean "lock" or "door," so "鍵" is more precise here. The translation maintains the original meaning while sounding natural in English.)）
C: Wait a minute, where did you put the key?
D: Wait a minute, where did I put the key?
E: Wait, where did I put my key?

### 78  （ja→en、目標は英語）
原文: 別に怒ってないけど、ひと言くらい言ってほしかったな。
A: I’m not angry, but I wanted to say a few words.
B: I wasn't actually angry, but I would have liked to at least say something.
C: 別に怒ってないんだけど、ちょっと言ってみたかったな。
D: I’m not mad at you, but I wish you had said a word.
E: 「全然怒ってないけど、ちょっと言い過ぎたかな」って思っただけだよ。

### 79  （ja→en、目標は英語）
原文: 今日はなんか疲れちゃったから、ご飯は適当でいいや。
A: 「Hey, I’m kinda tired today, so whatever. Just gotta eat whatever.”   ⏎ (Translation: "Today’s just been kinda worn out, so whatever. Just eat whatever.")   ⏎ No notes, no explanations, no alternatives. 😊
B: I’m tired today, so I’m not going to eat properly.
C: I’m kind of tired today, so I guess I can just make a suitable meal.
D: 今日ちょっと疲れちゃったから、飯は気楽にどうぞ。
E: I'm pretty tired today, so I'll just go with a casual meal.

### 80  （ja→en、目標は英語）
原文: あの店、結構当たりだったよ。今度一緒に行こう。
A: That place was pretty good, wasn’t it? Let’s go together sometime.
B: That store was pretty good.Let's go together next time.
C: 「あの店、結構お得だったよね。次も一緒に行こうよ。」   ⏎ （Translation: "That place was pretty good too! Let’s go together sometime."）   ⏎ This keeps the original tone and meaning while making it natural in English. Let me know if you'd like any adjustments!
D: That store was quite a hit. Let's go there next time.
E: That store was pretty good. Let’s go together next time.

### 81  （ja→en、目標は英語）
原文: いらっしゃいませ。何名様でいらっしゃいますか。
A: どうぞお越しください。何名様でご利用いただけますでしょうか。（注：「何名様」と「ご利用いただけますでしょうか」は、より丁寧な表現として「お越しください」「ご利用いただけますでしょうか」と訳すことも可能です。）
B: Welcome! How many of you are here?
C: welcome.How many people are there?
D: Welcome. How many people are there?
E: Welcome. How many people are here?

### 82  （ja→en、目標は英語）
原文: 恐れ入りますが、こちらの商品は在庫を切らしております。
A: ただいま、この商品は在庫切れとなっています。   ⏎ （Note: "恐れ入ります" は「お手数をおかけします」として適切な英語表現です。）   ⏎ 他の選択肢としては、「We are currently unable to ship this item due to low stock.」がより自然な日本語になります。
B: 恐れ入りますが、こちらの商品は在庫を切らしております。
C: Please note that this product is currently out of stock.
D: Sorry, but this product is out of stock.
E: 申し訳ございませんが、こちらの商品は在庫が切れております。

### 83  （ja→en、目標は英語）
原文: お会計は別々になさいますか。
A: "Do you separate your finances?"   ⏎ This translates to "Do you keep separate accounts for your finances?" in English. It’s a common question asked by individuals or businesses to ensure clarity and avoid confusion about where expenses or income come from.   ⏎ Would you like any refinements or additional context?
B: Will the bill be paid separately?
C: Will you pay separately?
D: Do you pay separately?
E: 「会計は別々に処理しますか？」   ⏎ （Translation: "Do you handle accounting separately?")   ⏎ This maintains the original meaning while sounding natural in English. Let me know if you'd like any refinements!

### 84  （ja→en、目標は英語）
原文: ご不明な点がございましたら、お気軽に係の者にお申し付けください。
A: If you have any questions, please do not hesitate to ask the staff.
B: もしご不明な点がございましたら、ご担当者様にお気軽にお申し付けください。   ⏎ （Translation: If you have any further questions, please don’t hesitate to ask the staff member.）   ⏎ This translation maintains the original meaning while ensuring natural English phrasing. Let me know if you'd like any refinements!
C: If you have any questions, please feel free to ask the staff.
D: If you have any questions, please feel free to contact the staff.
E: If you have any further questions, please don't hesitate to ask our staff.

### 85  （ja→en、目標は英語）
原文: お手数ですが、こちらのフォームにご記入をお願いいたします。
A: We apologize for the inconvenience, but we would appreciate it if you could fill out this form.
B: Sorry to trouble you, but please fill out this form.
C: Please fill out this form. Thank you.
D: Please bear with me and I’d be grateful if you could fill this out on this form.
E: ご迷惑をおかけしますが、このフォームにご記入いただけますと幸いです。どうぞお申し込みください。   ⏎ （Note: The translation maintains the original tone and politeness while ensuring clarity in English. "お手続き" is a formal request, and "ご迷惑をおかけしますと幸いです" reflects empathy.)

### 86  （ja→en、目標は英語）
原文: 利用者は、本規約に同意した時点で、本サービスの利用を開始したものとみなします。
A: The user shall be deemed to have started using this service when he/she agrees to these Terms.
B: Upon agreeing to these Terms, the user is deemed to have commenced the use of this service.
C: The user, upon agreeing to these terms and conditions when they commence use of this service, shall be deemed to have initiated the use thereof.   ⏎ This translation is provided directly from the original Japanese text without any modifications or translations into different languages. The translation maintains the original meaning and structure while ensuring clarity in English.
D: The user, upon agreeing to this Agreement, shall be deemed to have begun using the service at the time of its provision.   ⏎ This translation maintains the original meaning while ensuring natural English phrasing. Let me know if you'd like any refinements!
E: Users shall be deemed to have commenced using the service at the time when they agree to these Terms of Use.

### 87  （ja→en、目標は英語）
原文: 当社は、事前の通知なく本サービスの内容を変更または終了することがあります。
A: Our company may change or terminate the terms and conditions of our service without prior notice.   ⏎ This means that you should expect to receive updates or modifications to your account or service at a time when you are not informed in advance.   ⏎ Would you like me to provide more details on how this applies to your specific situation?
B: 弊社では、事前通知なしにサービス内容を変更・終了する場合があります。   ⏎ （Translation: "We may alter or terminate our services without prior notice.")   ⏎ This translation maintains the original meaning while ensuring natural English phrasing. Let me know if you'd like any refinements!
C: The Company may change or terminate the contents of the Service without prior notice.
D: The company may change or terminate the contents of the Service without prior notification.
E: We may change or terminate the content of the Services without prior notice.

### 88  （ja→en、目標は英語）
原文: 前項の規定にかかわらず、未成年者が本サービスを利用する場合は、親権者の同意を得なければならない。
A: 「Regardless of the provisions regarding minors, if a minor is using this service, they must obtain parental consent.”   ⏎ This translation maintains the original meaning while ensuring clarity and natural phrasing in English. Let me know if you'd like any refinements!
B: Regardless of the regulations in place, if a minor is using this service, they must obtain parental consent.     ⏎ This ensures that parents or guardians are involved in their care and decision-making.   ⏎ Let me know if you'd like any refinements!
C: Notwithstanding the provisions of the preceding paragraph, when a minor uses the Service, the consent of the custodial parent must be obtained.
D: Notwithstanding the provisions of the preceding paragraph, when a minor uses the Service, the consent of the parent or guardian must be obtained.
E: Notwithstanding the provisions of the preceding paragraph, a minor shall obtain the consent of the parent(s) or guardian(s) before using the Services.

### 89  （ja→en、目標は英語）
原文: 本契約の有効期間は、令和8年4月1日から1年間とする。
A: This agreement shall be effective from April 1, 2023, for a total period of one year.   ⏎ Translation:"The validity period of this agreement shall be from April 1, 2023, for a total duration of one year."   ⏎ If you'd like any refinements or additional details, feel free to let me know!
B: The validity period of this Agreement shall be one year from April 1st.
C: 本契約の有効期間は、2023年4月1日から1年間とさせていただきます。   ⏎ （Note: The translation maintains the original meaning while ensuring natural English phrasing. "本契約" is rendered as "本契約" to avoid repetition of "本" (the word for "this" in Japanese) and "の" (the article indicating a period).）
D: The effective period of this contract shall be one year from April 1, 2026.
E: The effective period of this Agreement shall be one year starting on April 1, 2026.

### 90  （ja→en、目標は英語）
原文: 本件に関する一切の紛争は、東京地方裁判所を第一審の専属的合意管轄裁判所とする。
A: Any dispute concerning the case shall be tried in the Tokyo District Court as the exclusive district court with jurisdiction by an agreement.
B: All disputes related to the present case shall be subject to the exclusive applicable court of jurisdiction in the first instance, the Tokyo District Court.
C: Regarding any disputes concerning this matter, all proceedings shall be heard in the Tokyo District Court as the sole competent jurisdiction.   ⏎ (Note: The translation maintains the formal and precise tone of the original Japanese text while ensuring clarity in English.)
D: This matter shall be heard by the Tokyo District Court as the sole venue for any disputes arising out of this matter.   ⏎ Translation:"All disputes regarding this matter shall be heard by the Tokyo District Court as the sole venue.   ⏎ Explanation:** The translation maintains the original meaning while ensuring clarity and natural English phrasing. The term "裁判所" (district court) is rendered as "court," which is a common legal term in Japan. "専属的合意管轄裁判所" (sole venue for sole jurisdiction) is translated as "sole venue" to emphasize that the court has exclusive authority over this case. The rest of the sentence remains unchanged as it is a standard legal statement.
E: Any dispute relating to this matter shall be subject to the exclusive jurisdiction of the Tokyo District Court in the first instance.

### 91  （ja→en、目標は英語）
原文: 夕暮れの空が、ゆっくりと藍色に溶けていった。
A: The sunset sky slowly dissolved into indigo.   ⏎ (Note: "夕暮れ" (yūjō) means "sunset," and "藍色" (inkō) refers to "indigo" or "blue-green." The translation maintains the poetic imagery while adapting it to natural English.)
B: The dusk sky slowly faded into indigo.
C: The sunset sky slowly began to dissolve into indigo.   ⏎ (Note: "夕暮れ" (yūjō) means "sunset," but in this context, "indigo" (藍色) is a poetic term for blue-gray, fitting the melancholic tone of the sentence.)
D: The evening sky slowly dissolved into a indigo color.
E: The sky at dusk slowly melted into indigo.

### 92  （ja→en、目標は英語）
原文: 彼女は何も言わず、ただ窓の外を見ていた。
A: 彼女は何も言わずに窓の外を見ているだけだった。
B: She said nothing and just looked out the window.
C: She didn't say anything and just looked out the window.
D: She didn’t say anything; she just watched out the window.
E: 彼女は何も言わずに、ただ窓の外を見ているだけだった。   ⏎ （Note: The translation maintains the original meaning while adjusting phrasing for natural English flow.)

### 93  （ja→en、目標は英語）
原文: 蝉の声が、遠い夏の記憶を連れてきた。
A: 「Cicada’s song brought back memories of a distant summer.”   ⏎ This translation maintains the original meaning while adapting it to natural English phrasing. The sentence retains the poetic and evocative tone of the Japanese phrase. Let me know if you'd like any refinements!
B: The cicadas’ song brought back memories of a distant summer.   ⏎ (Note: "蝉の声" (sansui) means "cicada" in Japanese, and "遠い夏" (yoi chū) literally translates to "distant summer," evoking the image of cicadas buzzing away.)   ⏎ The cicadas’ song brought back memories of a distant summer.
C: The sound of the fire brought me memories of the distant summer.
D: The sound of the cicada brought back distant summer memories.
E: The sound of the cicadas brought back distant summer memories.

### 94  （ja→en、目標は英語）
原文: ふいに、懐かしい匂いがして、足が止まった。
A: Suddenly, I felt a nostalgic smell, and my feet stopped moving.
B: 突然、懐かしい匂いがして足が止まったんだ。   ⏎ （Translation: "Suddenly, a nostalgic smell woke me up—my feet froze."）   ⏎ This translation maintains the original meaning while sounding natural in English. Let me know if you'd like any refinements!
C: When I heard a nostalgic smell, my legs stopped.
D: It smelled nostalgic and my feet stopped.
E: Suddenly, a nostalgic smell wafted through the air, and my feet stopped.

### 95  （ja→en、目標は英語）
原文: 「ありがとう」の一言が、どうしても出てこなかった。
A: “Thank you” didn’t come out.
B: 「ありがとう」の一言、全然言い出せなくて困ったな。   ⏎ （訳：「ありがとう」の一言をどうしても言い出せなかった。）   ⏎ このようにして回答します。必要に応じてさらに調整できますのでお知らせください。
C: I couldn't muster a single word of “thank you.”
D: 「ありがとう」の一言、全然言い出せなくてごめんね。
E: I couldn’t bring myself to say a single word “thank you.”

### 96  （ja→en、目標は英語）
原文: 今日の電車、人多すぎて死ぬかと思った…
A: 「今日の電車、すごい人だな。死ぬかと思ったよ」   ⏎ （Translation: "Today’s train, it’s so crowded I thought I’d die—" — natural English phrasing while keeping the tone casual and humorous.)   ⏎ Let me know if you'd like any refinements!
B: The train today was so crowded that I thought I might die…
C: I thought today's train was going to die because there were too many people ...
D: 今日の電車、すごい人だらけで死ぬかと思ったけど…。
E: Today's trains were so crowded that I thought I might die…

### 97  （ja→en、目標は英語）
原文: 新作のコーヒー飲んでみた☕ 思ったより甘くなくて好き！
A: "Tried this new coffee ☕ I didn’t think it was as sweet as I expected!"   ⏎ (Translation: "I tried this new coffee ☕ And it wasn’t as sweet as I’d hoped!")   ⏎ This keeps the casual, playful tone of the original while making it natural in English. Let me know if you'd like any refinements!
B: "Tried this new coffee ☕ I didn’t think it was as sweet as I expected!"
C: I tried the new coffee☕. It wasn't as sweet as I expected and I like it!
D: I tried the new coffee ☕️ and it wasn’t as sweet as I thought—I like it!
E: I tried a new coffee <0xE2><0x98><0x95> I like it not sweeter than I thought!

### 98  （ja→en、目標は英語）
原文: 締め切りまであと3時間。無理。
A: There are three hours left until the deadline. It's impossible.
B: Three hours until the deadline.I can't.
C: 締め切りが3時間も残っていない。無理だ。
D: There’s only three hours left until the deadline. Impossible.
E: 締め切りまであと3時間しか残ってないのに、無理だよ。

### 99  （ja→en、目標は英語）
原文: #今日の空 めっちゃ綺麗だった
A: Today's sky was very beautiful
B: 「今日の空、すごく綺麗だったね」   ⏎ （Translation: "The sky over today was so beautiful. That’s a great compliment! ☀️"）   ⏎ This keeps the casual, friendly tone while making it natural in English. Let me know if you'd like any adjustments!
C: Today's sky was really beautiful.
D: "Today’s sky is super beautiful"   ⏎ This translates to "Today’s sky is super beautiful" in English, conveying the same sentiment as the original Japanese sentence. If you'd like a more natural phrasing, you could say: "Today’s sky is absolutely gorgeous."   ⏎ Let me know if you'd like any adjustments!
E: The sky was so beautiful today.

### 100  （ja→en、目標は英語）
原文: 推しのライブ当たった！！！人生で一番運を使った気がする
A: "My favorite concert ever happened!!!" I feel like I used up all my luck in life.
B: I got my favorite artist’s live ticket! I feel like I’ve used my luck the most in my life.
C: I won the guess game! I feel like I've used my luck the most in my life.
D: I hit the push live! ! !I feel the luckiest in my life.
E: "My favorite concert was totally thanks to luck!"   ⏎ This translation maintains the enthusiasm and casual tone of the original sentence while ensuring it reads naturally in English. Let me know if you'd like any refinements!
