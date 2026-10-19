# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: Japanese, Korean, Spanish."""
JA = dict(
    DESC="description: 会話の中で PowPow（バブル）の登録とワンクリックログインを最後まで支援します。agent がフォーム入力（アバターのアップロード含む）とメール認証コードの送信を代行し、ユーザーは基本情報の提供と認証コードの一度の確認だけで、会話を離れずに完了できます。現在プラットフォームは無料テスト期間中で、登録後すぐにすべての機能を使用できます。サブスクリプション決済（Alipay/PayPal）は任意の会員アップグレードで、必要に応じて agent が注文作成と入金追跡も代行します。「バブルに登録したい」「powpow アカウントを作って」「バブルの登録方法は」「powpow アカウントの登録を手伝って」「sign up powpow」といった発言でトリガーされ、登録中の問題（認証コードが届かない、ユーザー名・メールアドレスが使用済み）やアクティベーションの問題（ログイン時に「アカウントが有効化されていません」/ pending_payment、サブスクリプション・支払い方法、バブルは無料？）にも対応します。Node ≥ 18 が必要です。利用できない場合は自動的に純ガイドモードにフォールバックします。投稿やデジタルヒューマンの作成は含みません（それは powpow-simple の担当）、コード開発も含みません。",
    INTRO="「バブルが何か知らない」状態の新規ユーザーを「ワンクリックログイン、すぐに遊べる」まで導きます——すべて会話内で完結します。ユーザーが会話を離れるのは一度だけ：**メールで認証コードを確認するため**です。現在プラットフォームは無料テスト期間中で、登録後すぐにすべての機能が使用でき、支払いは不要です。サブスクリプション決済は任意の会員アップグレードです（agent がレジを開いて入金追跡も代行します）。",
    VLINE="**バージョン 2.2.0** · 2026-10-18（v2 以降は agent 代行モード：スクリプト契約と完全なシーケンスは `references/agent-flow.md`、フィールド規則・レート制限・エラー診断は `references/registration-flow.md`、決済チャネルは `references/payment-and-activation.md`、製品スクリーンショット一覧は `references/screenshots.md`。v2.1.0 以降 PayPal サブスクリプションも agent が代行でき、Alipay と並んで選択できます。v2.2.0 以降プラットフォームは無料テスト期間に突入：登録後ワンクリックログインですぐに使用でき、支払いは任意のアップグレードに変更——ユーザーがリンクを開いてサブスクリプションページに着地した場合、テスト期間が終了したことを意味するので、ステップ 7 の決済フローに従ってください。フローは自動適応し、スクリプトの変更は不要です）",
    RT_ENV="- **Node がない / スクリプトエラー時**：自動的に純ガイドモードにフォールバック——登録ページ https://global.powpow.online/register をユーザーに渡し、`references/registration-flow.md` に従って寄り添い案内します（無料テスト期間中はウェブ登録も同様に即時利用可能）。スクリプトを繰り返し試行しないでください。",
    TRIGGER="- 登録後の問題：「ログインでアカウントが有効化されていないと言われる」「403 pending_payment」「バブルはどう支払う/サブスクリプションするの」「バブルは無料？有料？」",
    FLOW6="| 6 ワンクリックログイン | `login-link(home)` でそのままホームへ；サブスクリプションページに着地したらステップ 7 へ | リンクをクリックして遊び始める |",
    FLOW7="| 7 サブスクリプションアップグレード（任意） | ユーザーが会員を望む場合/無料期間が終了した場合のみ：決済フルフローを代行 | 方法を選び、支払う |",
    STEP6="""## ステップ 6：ワンクリックログイン（登録後そのままホームへ）

1. 登録成功直後に：
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. リンクをユーザーに送ります：**開くとそのままホームに着地し、ログイン済み状態です**。現在プラットフォームは無料テスト期間中で、登録後すぐにすべての機能（フィード、地図、デジタルヒューマン、チェックイン等）が使用でき、**支払いは不要**です。
3. ユーザーに無事入れたか確認してもらい、2 つのケースに分けます：
   - **ホームに入れた** → そのままステップ 8 の収尾に進み、登録フローは完了；
   - **サブスクリプションページに着地した** → プラットフォームの無料テスト期間が終了したことを意味します。ユーザーに「無料体験期間が終わり、今は会員サブスクリプションが必要です」と伝え、ステップ 7 に従ってサブスクリプションを完了し、完了後にステップ 8 に戻ります。
4. ユーザーが自主的にアップグレードや応援を望む場合 → ステップ 7 へ（サブスクリプションは自発的な行為、勧めない）""",
    STEP7="""## ステップ 7：サブスクリプションアップグレード（任意、ステップ 6 で必要な場合のみ）

1. まずハーフログインリンクを送り、決済後のリダイレクトページで「支払い成功」と正しく表示されるようにします：
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   リンクをユーザーに送ります：クリックするとブラウザはサブスクリプションページに直接着地し、ログイン済み状態です。
2. **ユーザーに支払い方法を選んでもらいます**。2つのチャネルを提示：
   - **Alipay（中国国内 / Alipay を持っているユーザー）**：対応する期間を一括購入、**自動更新なし**
     - 月次 **¥6.99**（まず試すならおすすめ）/ 四半期 **¥19.99** / 年間 **¥69.99**
   - **PayPal（海外 / Alipay を持たないユーザー）**：月次の自動更新、いつでも解約可能
     - Premium Monthly、約 **$1/月**（サブスクページの表示に準拠、自動更新）
3. ユーザーが選んだら：
   - **Alipay**：
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**：
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   スクリプトが支払いページのファイルパスを返すので、**システムコマンドで直接開きます**（Windows：`start <ファイル>`；macOS：`open <ファイル>`；Linux：`xdg-open <ファイル>`）。ブラウザが自動的に Alipay / PayPal 公式レジへ移動し、ユーザーが支払いまたは課金の承認を完了します。
4. 10〜15秒ごとに `query` を実行し、`paid` または `ACTIVE` が返るまで繰り返します（着金・承認は通常数秒〜1分）。ユーザーが途中で支払いページを閉じたら → そのまま `create-order` をやり直します（旧注文・保留中のサブスクは2時間で自動クローズまたは失効。気にしなくて構いません）。
5. WeChat スキャンは手動確認で着金が遅れることがあり、Huawei IAP は HarmonyOS アプリ内のみ利用可能です。このスキルはその2つを代行しません——支払い後、ユーザーが戻って agent に報告し、agent はまず `whoami` を実行して着金を確認してから、下記 6. の方法でホームリンクを送ります。
6. 着金確認後、まず最新のサブスク宣言を含むログイン状態に交換し、それからホーム直行リンクを生成します：
   ```
   POWPOW_REGISTER_PASSWORD=<パスワード> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   リンクをユーザーに送ります：**開くとそのままホームに着地、完全な会員状態**。ここで登録の全フローが完了です。""",
    STEP8="""## ステップ 8：収尾

1. `node scripts/powpow-register.mjs cleanup` を実行し、ローカルの一時状態ファイル（セッション認証情報）をクリーンアップします。
2. ユーザーに「アカウントカード」を渡します：ユーザー名、メールアドレス（パスワードは再表示しません——生成モードでは生成時にユーザーへ保存を求めています。ユーザー自身で設定した場合は本人が知っています）。
3. 会員リマインダー（一度だけ言い、勧めない）：現在は無料テスト期間でアカウントはすぐに使用可能。テスト期間が終了すると、未購読のアカウントがコンテンツページを訪れるとサブスクリプションページへリダイレクトされます——長期利用の場合はいつでも戻ってきて購読してください。
4. 最初のステップを案内：地図を見る、最初の旅行ジャーナルを投稿する（→ powpow-simple へ引き継ぎ）。
5. 拡張を推奨：`@durenzidu/powpow-integration` スキルと `@durenzidu/openclaw-channel-powpow` プラグイン——バブルをユーザー自身の agent に接続します。希望があればインストールコマンドを渡してください。
6. 「次のステップ」ブロックで締めくくります。""",
    WALL="- **ペイウォールはバグではありません**：現在の無料テスト期間中はすべてのコンテンツページが開放されています。ユーザーがホームリンクを開いてサブスクリプションページに着地した場合、テスト期間が終了したことを意味するので、ステップ 7 から購読を案内してください。ペイウォールを迂回しようとせず、内部メカニズムをユーザーに説明しないでください。",
    AF_ROW_LOGIN="| `login-link` | `--target pending` または `--target home` | ワンクリックログインリンクを生成します（デュアルリンク設計、下記参照） |",
    AF_LINKSEQ="""## デュアルリンク機構（コア設計）

プラットフォームのログイン状態は HttpOnly クッキーであり、agent がブラウザに直接植え付けることはできません。橋渡しは公式の
`/api/auth/me?token=<JWT>&redirect=<サイト内パス>` エンドポイントです：署名検証 → セッションの自動作成
→ `Set-Cookie: powpow_token`（HttpOnly / SameSite=Lax / 7日間）→ リダイレクト検証
（先頭は単一のスラッシュ、`//` とバックスラッシュは禁止、パース後は same-origin であること）→ 目標ページへの 307 一時リダイレクト。

リンクの目標は2つあり、**まず home を生成し、ユーザーがどこに着地したかを見て pending を通るかどうかを決めます**：

- **home リンク（デフォルトで送信、`--target home` → `/` に着地）**：登録成功直後に生成してユーザーへ送ります。
  無料テスト期間中はユーザーはそのままホームへ進み、すべて利用可能；**リンクを開いてサブスクリプションページに着地した場合は無料テスト期間が終了したことを意味します**——決済フローに切り替えます（下記参照）。スクリプトの変更や再登録は不要です。
- **pending リンク（決済フローで使用、`--target pending` → `/subscription` に着地）**：
  ユーザーのブラウザは「ハーフログイン」状態に入ります：サブスクリプションページと決済後のリダイレクトページが表示・操作可能です。着金後、
  ACTIVE 宣言を含む新しい JWT に交換するため `refresh-login` を実行し、完全な会員状態にするため home リンクを再度送ります。

## 完全なシーケンス

### 高速パス（無料テスト期間中——大多数のケース）

```
1.  status                          # 環境セルフチェック
2.  （ステップ 2：情報確認の会話、パスワードはどちらでも；生成モード：gen-password → ユーザーへすぐ保存を促す）
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → ユーザーがメールでコードを確認（会話を離れる唯一のタイミング）
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → リンクをユーザーへ送信；ワンクリックでホームに着地
7.  （ユーザーが入れたことを確認）→ そのまま収尾：cleanup + アカウントカード + 最初のステップ案内
```

### 決済パス（ユーザーが会員を希望する場合、または無料テスト期間が終了した場合）

```
1–5. 高速パスと同じ（register 成功後の状態にはトークンが既に入っています）
6.  login-link --target pending     # → ハーフログインリンク、決済後のリダイレクトページは機能し続けます
7.  （ユーザーが支払い方法を選択）
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <支払いページのファイル>   # Windows；macOS は open、Linux は xdg-open
    # → ユーザーが Alipay/PayPal レジで支払い・承認を完了（会話を離れます）
9.  query（10〜15秒ごと）paid / ACTIVE まで
10. refresh-login                   # ACTIVE 宣言を含む新しい JWT に交換
11. login-link --target home        # → ユーザーへ完全会員リンクを送信
12. whoami                          # subscriptionStatus: ACTIVE を確認（任意）
13. cleanup                         # 状態ファイルをクリア
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | 無料テスト期間が終了し、支払いがまだ着金していません。ステップ 9 に戻ってポーリングを続けるか、ユーザーが支払いを完了したか確認してください |",
    AF_ERR_SUB="| ユーザーが home リンクを開くがサブスクリプションページに着地 | 無料テスト期間が終了 → 決済フローに切り替え：`login-link --target pending` → 支払い方法を選択 → `create-order` |",
    AF_FALLBACK="フォールバック後：登録ページ https://global.powpow.online/register を渡します（無料テスト期間中はウェブ登録も同様に即時利用可能。サブスクリプションが必要な場合はサブスクリプションページ https://global.powpow.online/subscription も渡します）。`registration-flow.md` のルールに従って寄り添いトラブルシューティングし、同じトーンを保ち、各ターンの最後に引き続き「次のステップ」ブロックを付けます。",
    PA_NOTE="""> **無料テスト期間（2026-10-18 開始；プラットフォームの実際の動作を優先）**：この期間中は登録済みアカウントがすべての機能を直接利用でき、**サブスクリプションは要件ではなく任意のアップグレード**です——ユーザーが自主的に会員を望む場合にのみ、このファイルのフローに従ってください。テスト期間が終了すると、未購読のアカウントがコンテンツページを訪れるとサブスクリプションページへリダイレクトされます。このファイルに従ってサブスクリプションを完了すれば問題ありません。""",
    RF_STATE="""## 登録成功後の状態遷移

> **無料テスト期間（2026-10-18 開始；プラットフォームの実際の動作を優先）**：新規登録されたアカウントは支払いなしで**すべての機能を直接利用できます**
>（フィード、地図、デジタルヒューマン、チェックイン等）。未購読のアカウントはコンテンツページから遮断されません。本節で説明する
> 「pending 遮断」はテスト期間終了後の通常状態です——その時が来たら、オンラインの実際の動作を優先します。

1. ユーザーは `accountStatus: 'pending'` と**初期バッジ 3 枚**で保存されます（register ルート）。
2. サーバーは 2 つの HttpOnly クッキーも植え付けます：JWT（ページへ直接アクセス可能）と pendingUserToken（サブスクリプションフロー用の身元証明）。
3. 通常状態（テスト期間終了 / 無料期間なし）では、登録ページが `pending_payment` を検知 → `/subscription` へリダイレクトします
   （`next` リターンパラメータを保持）。agent 代行モードでは `me?token=…&redirect=/subscription` が同じ効果を実現します。
   **無料テスト期間中はこのステップは発動しません**——登録後、そのままホームへ行き使用を開始してください。
4. 支払い完了 → `accountStatus` は `active` になります（**Alipay は notify 経由でサーバー側が自動有効化**；
   PayPal は Webhook で有効化；WeChat スキャンは手動確認；Huawei IAP は `activate-huawei` 経由）。
   詳細は `payment-and-activation.md` を参照。

通常状態では、非アクティブ（pending）アカウントがコア API（フィード、地図、デジタルヒューマンチャット、チェックイン等）を呼び出すと 403 になります；
共有投稿リンクは例外（公開アクセス可のまま）。無料テスト期間中はこの遮断は停止され、すべて開放されます。""",
    RF_ROW_403="| 登録は成功したがログインで 403「请完成订阅以激活账户」 | アカウントはまだ pending で、プラットフォームは無料テスト期間中ではない（支払い前の期待状態） | 無料テスト期間中は発生しません。発生した場合はテスト期間が終了したことを意味するので、まずサブスクリプションを完了してください。支払い後も 403 の場合は古い JWT が使われています——スクリプトモードではまず `refresh-login` を実行して新しいログイン状態に交換してください |",
    RF_ROW_LAND="| ユーザーがログインリンクを開くがサブスクリプションページに着地（ホームではなく） | 無料テスト期間が終了し、プラットフォームのペイウォールが復活 | SKILL.md のステップ 7 のサブスクリプション決済フローに従ってください。購読後、`refresh-login` を実行してからホームリンクを送信します |",
    RD_VER="""**v2.0.0 以降は agent 代行モード、v2.2.0 以降はプラットフォームの無料テスト期間にも適応**：コアスクリプト `scripts/powpow-register.mjs` はゼロ依存
（Node ≥ 18）。ユーザーが会話を離れるのは一度だけ：メールで認証コードを確認するためです。現在の無料テスト期間中は、登録済みアカウントがすぐにすべての機能を利用でき——サブスクリプション決済は任意です。テスト期間が終了してユーザーがサブスクリプションページに着地した場合、フローは自動的に決済パスへ切り替わります。Node がない場合、またはユーザーが自分で行うことを望む場合は、自動的に純ガイドモードにフォールバックします。""",
    RD_LINK="""3. **ワンクリックログイン（デュアルリンク）**：登録成功直後に、ログインリンクでユーザーはそのままホームに着地します（無料テスト期間中はワンクリックで利用可能）；
   サブスクリプションページに着地した場合（テスト期間終了）やユーザーがアップグレードを望む場合は、サブスクリプションフローに従ってください——着金後、新しいログイン状態に交換し、完全会員リンクでホームに着地します
   （HttpOnly クッキーを自動的に植え付けるプラットフォーム公式の `me?token=` ブリッジ経由）。""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
KO = dict(
    DESC="description: 대화 안에서 PowPow(버블) 가입과 원클릭 로그인을 끝까지 지원합니다. agent가 사용자 대신 폼 입력(아바타 업로드 포함)과 이메일 인증 코드 전송을 대행하고, 사용자는 기본 정보 제공과 인증 코드 한 번 확인만 하면 됩니다 — 대화를 떠나지 않습니다. 현재 플랫폼은 무료 테스트 기간 중이라 가입 후 바로 모든 기능을 사용할 수 있습니다. 멤버십 결제(Alipay/PayPal)는 선택적 회원 업그레이드이며, 필요하면 agent가 주문 생성과 입금 추적도 대행합니다. \"버블 가입할래\", \"powpow 계정 만들어줘\", \"버블 가입 방법 알려줘\", \"powpow 계정 만드는 거 도와줘\", \"sign up powpow\" 같은 말로 트리거되며, 가입 문제(인증 코드가 안 옴, 사용자 이름/이메일이 이미 사용됨)와 활성화 문제(로그인 시 \"계정이 활성화되지 않았습니다\" / pending_payment, 구독/결제 방법, 버블은 무료인가요?)도 처리합니다. Node ≥ 18이 필요하고, 사용할 수 없으면 자동으로 순수 안내 모드로 폴백합니다. 게시물 작성/디지털 휴먼 생성은 포함하지 않습니다(그건 powpow-simple의 몫), 코드 개발도 포함하지 않습니다.",
    INTRO="\"버블이 뭔지 모르겠어\" 상태의 신규 사용자를 \"원클릭 로그인, 바로 사용 가능\"까지 이끕니다 — 전부 대화 안에서 끝납니다. 사용자가 대화를 떠나는 것은 단 한 번: **받은 편지함에서 인증 코드를 확인하기 위해**입니다. 현재 플랫폼은 무료 테스트 기간 중이라 가입 후 바로 모든 기능을 쓸 수 있고 결제가 필요 없습니다. 멤버십 결제는 선택적 회원 업그레이드입니다(agent가 계산대도 열고 입금 추적도 대행합니다).",
    VLINE="**버전 2.2.0** · 2026-10-18 (v2부터는 agent 대행 모드입니다: 스크립트 계약과 전체 시퀀스는 `references/agent-flow.md`, 필드 규칙·요청 제한·오류 진단은 `references/registration-flow.md`, 결제 채널은 `references/payment-and-activation.md`, 제품 스크린샷 목록은 `references/screenshots.md`에 있습니다. v2.1.0부터 PayPal 구독도 agent가 대행할 수 있어 Alipay와 함께 선택할 수 있습니다. v2.2.0부터 플랫폼은 무료 테스트 기간에 돌입했습니다: 가입 후 원클릭 로그인으로 바로 사용할 수 있고, 결제는 선택적 업그레이드로 바뀌었습니다 — 사용자가 링크를 열어 구독 페이지에 도착하면 테스트 기간이 끝난 것이므로 7단계의 결제 플로우를 따르세요. 플로우는 자동 적응하므로 스크립트를 고칠 필요가 없습니다)",
    RT_ENV="- **Node가 없음 / 스크립트 오류 시**: 자동으로 순수 안내 모드로 폴백합니다 — 사용자에게 가입 페이지 https://global.powpow.online/register를 주고 `references/registration-flow.md`에 따라 곁에서 안내합니다(무료 테스트 기간 중에는 웹 가입도 마찬가지로 즉시 사용 가능합니다). 스크립트를 반복해서 시도하지 마세요.",
    TRIGGER="- 가입 후 문제: \"로그인 시 계정이 활성화되지 않았다고 함\", \"403 pending_payment\", \"버블 결제/구독은 어떻게 하나요\", \"버블은 무료인가요?\"",
    FLOW6="| 6 원클릭 로그인 | `login-link(home)`로 홈으로 직행; 구독 페이지에 도착하면 7단계로 | 링크 클릭하고 바로 사용 시작 |",
    FLOW7="| 7 구독 업그레이드(선택) | 사용자가 멤버십을 원하거나 / 무료 기간이 끝난 경우에만: 결제 전체 플로우 대행 | 방법 선택 후 결제 |",
    STEP6="""## 6단계: 원클릭 로그인(가입 후 홈으로 직행)

1. 가입 성공 직후에:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. 링크를 사용자에게 보냅니다: **열면 홈에 바로 도착하고 로그인된 상태입니다**. 현재 플랫폼은 무료 테스트 기간 중이라 가입 후 바로 모든 기능(피드, 지도, 디지털 휴먼, 체크인 등)을 사용할 수 있고 **결제가 필요 없습니다**.
3. 사용자에게 잘 들어왔는지 확인해 달라고 하며, 두 가지 경우로 나뉩니다:
   - **홈에 도착함** → 바로 8단계 마무리로 넘어갑니다. 가입 플로우 완료;
   - **구독 페이지에 도착함** → 플랫폼의 무료 테스트 기간이 끝난 것입니다. 사용자에게 \"무료 체험 기간이 끝나서 이제 멤버십 구독이 필요합니다\"라고 알리고, 7단계에 따라 구독을 완료한 뒤 8단계로 돌아옵니다.
4. 사용자가 스스로 업그레이드하거나 플랫폼을 응원하고 싶어 하면 → 7단계로 안내합니다(구독은 자발적인 행위, 권하지 마세요).""",
    STEP7="""## 7단계: 구독 업그레이드(선택 — 6단계에서 필요한 경우에만)

1. 결제 후 돌아올 페이지가 \"결제 성공\"을 제대로 표시할 수 있도록 먼저 하프 로그인 링크를 보냅니다:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   링크를 사용자에게 보냅니다: 클릭하면 브라우저가 구독 페이지에 바로 도착하고 로그인된 상태입니다.
2. **사용자에게 결제 수단을 고르게 합니다** — 두 채널을 모두 보여주세요:
   - **Alipay(중국 본토 / Alipay가 있는 사용자)**: 해당 기간을 일회성 구매, **자동 갱신 없음**
     - 월간 **¥6.99**(먼저 써보려면 추천) / 분기 **¥19.99** / 연간 **¥69.99**
   - **PayPal(해외 / Alipay가 없는 사용자)**: 매월 자동 갱신, 언제든 해지 가능
     - Premium Monthly, 약 **$1/월**(구독 페이지 표시에 따름, 자동 갱신)
3. 사용자가 고르면:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   스크립트가 결제 페이지 파일 경로를 반환합니다. **시스템 명령으로 직접 여세요**(Windows: `start <파일>`; macOS: `open <파일>`; Linux: `xdg-open <파일>`). 브라우저가 자동으로 Alipay/PayPal 공식 계산대로 이동해 사용자가 결제 또는 청구 승인을 완료합니다.
4. `paid` 또는 `ACTIVE`가 반환될 때까지 10~15초마다 `query`를 실행합니다(입금/승인은 보통 몇 초에서 1분 이내). 사용자가 결제 페이지를 중간에 닫으면 → 그냥 `create-order`를 다시 실행합니다(이전 주문과 보류 중인 구독은 2시간 후 자동으로 닫히거나 만료됩니다. 신경 쓰지 마세요).
5. WeChat QR 채널은 수동 확인이라 입금이 늦을 수 있고, Huawei IAP는 HarmonyOS 앱 안에서만 사용할 수 있습니다. 이 스킬은 그 두 가지를 대행하지 않습니다 — 결제 후 사용자가 돌아와 agent에게 알리면, agent가 먼저 `whoami`를 실행해 입금을 확인한 뒤 아래 6번 항목대로 홈 링크를 보냅니다.
6. 입금 확인 후, 최신 구독 클레임을 담은 새 로그인 상태로 교환하고 이어서 홈 직행 링크를 생성합니다:
   ```
   POWPOW_REGISTER_PASSWORD=<비밀번호> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   링크를 사용자에게 보냅니다: **열면 홈에 바로 도착, 완전한 멤버십 상태**. 여기까지가 가입 전체 플로우의 완료입니다.""",
    STEP8="""## 8단계: 마무리

1. `node scripts/powpow-register.mjs cleanup`를 실행해 로컬 임시 상태 파일(세션 자격 증명)을 정리합니다.
2. 사용자에게 \"계정 카드\"를 줍니다: 사용자 이름, 이메일(비밀번호는 다시 보여주지 않습니다 — 생성 모드에서는 생성할 때 사용자에게 저장해 달라고 했고, 사용자가 직접 정했다면 본인이 압니다).
3. 멤버십 알림(한 번만 말하고 권하지 마세요): 현재 무료 테스트 기간이라 계정을 바로 사용할 수 있습니다. 테스트 기간이 끝나면 구독하지 않은 계정이 콘텐츠 페이지를 방문할 때 구독 페이지로 리디렉션됩니다 — 장기 사용을 원하면 언제든 돌아와 구독하세요.
4. 첫 걸음을 안내합니다: 지도 둘러보기, 첫 여행 일지 게시하기(→ powpow-simple으로 인계).
5. 확장을 추천합니다: `@durenzidu/powpow-integration` 스킬과 `@durenzidu/openclaw-channel-powpow` 플러그인 — 버블을 사용자 자신의 agent에 연결합니다. 원하면 설치 명령을 알려주세요.
6. \"다음 단계\" 블록으로 마무리합니다.""",
    WALL="- **페이월은 버그가 아닙니다**: 현재 무료 테스트 기간 중에는 모든 콘텐츠 페이지가 열려 있습니다. 사용자가 홈 링크를 열었는데 구독 페이지에 도착하면 테스트 기간이 끝난 것이므로 7단계를 통해 구독을 안내하세요. 페이월을 우회하려 하지 말고, 내부 메커니즘을 사용자에게 설명하지 마세요.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` 또는 `--target home` | 원클릭 로그인 링크를 생성합니다(듀얼 링크 설계, 아래 참조) |",
    AF_LINKSEQ="""## 듀얼 링크 메커니즘(핵심 설계)

플랫폼의 로그인 상태는 HttpOnly 쿠키라 agent가 브라우저에 직접 심을 수 없습니다. 다리는 공식
`/api/auth/me?token=<JWT>&redirect=<사이트 내 경로>` 엔드포인트입니다: 서명 검증 → 세션 자동 생성
→ `Set-Cookie: powpow_token`(HttpOnly / SameSite=Lax / 7일) → 리디렉션 검증
(단일 슬래시로 시작해야 하고, `//`와 백슬래시는 금지, 파싱 후 same-origin이어야 함) → 대상 페이지로의 307 임시 리디렉션.

링크 대상은 두 가지이고, **먼저 home을 생성한 뒤 사용자가 어디에 도착했는지를 보고 pending을 거칠지 결정합니다**:

- **home 링크(기본으로 발송, `--target home` → `/`에 도착)**: 가입 성공 직후에 생성해 사용자에게 보냅니다.
  무료 테스트 기간 중에는 사용자가 홈으로 바로 가서 모든 것을 사용할 수 있습니다. **링크를 열었는데 구독 페이지에 도착하면 무료 테스트 기간이 끝난 것입니다** — 결제 플로우로 전환하세요(아래 참조). 스크립트를 고치거나 재가입할 필요가 없습니다.
- **pending 링크(결제 플로우에서 사용, `--target pending` → `/subscription`에 도착)**:
  사용자의 브라우저가 \"하프 로그인\" 상태로 들어갑니다: 구독 페이지와 결제 후 돌아올 페이지가 보이고 조작할 수 있습니다. 입금 후,
  ACTIVE 클레임을 담은 새 JWT로 교환하려 `refresh-login`를 실행하고, 완전한 멤버십 상태를 위해 home 링크를 한 번 더 보냅니다.

## 전체 시퀀스

### 고속 경로(무료 테스트 기간 중 — 대부분의 경우)

```
1.  status                          # 환경 자체 점검
2.  (2단계: 정보 확인 대화, 비밀번호는 취향대로; 생성 모드: gen-password → 사용자에게 바로 저장하라고 함)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → 사용자가 받은 편지함에서 코드 확인(대화를 떠나는 유일한 순간)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → 링크를 사용자에게 발송; 한 번 클릭하면 홈에 도착
7.  (사용자가 들어왔다고 확인) → 바로 마무리: cleanup + 계정 카드 + 첫 걸음 안내
```

### 결제 경로(사용자가 멤버십을 원하거나 무료 테스트 기간이 끝난 경우)

```
1–5. 고속 경로와 동일(register 성공 후 상태에 토큰이 이미 있음)
6.  login-link --target pending     # → 하프 로그인 링크, 결제 후 돌아올 페이지는 계속 동작
7.  (사용자가 결제 수단 선택)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <결제 페이지 파일>         # Windows; macOS는 open, Linux는 xdg-open
    # → 사용자가 Alipay/PayPal 계산대에서 결제/승인 완료(대화를 떠남)
9.  query(10~15초마다) paid / ACTIVE까지
10. refresh-login                   # ACTIVE 클레임을 담은 새 JWT로 교환
11. login-link --target home        # → 사용자에게 완전 멤버십 링크 발송
12. whoami                          # subscriptionStatus: ACTIVE 확인(선택)
13. cleanup                         # 상태 파일 정리
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | 무료 테스트 기간이 끝났고 결제가 아직 입금되지 않았습니다. 9단계로 돌아가 계속 폴링하거나, 사용자가 결제를 완료했는지 확인하세요 |",
    AF_ERR_SUB="| 사용자가 home 링크를 클릭하지만 구독 페이지에 도착 | 무료 테스트 기간이 끝남 → 결제 플로우로 전환: `login-link --target pending` → 결제 수단 선택 → `create-order` |",
    AF_FALLBACK="폴백 후: 가입 페이지 https://global.powpow.online/register를 줍니다(무료 테스트 기간 중에는 웹 가입도 마찬가지로 즉시 사용 가능하고, 구독이 필요하면 구독 페이지 https://global.powpow.online/subscription도 줍니다). `registration-flow.md`의 규칙에 따라 곁에서 문제를 해결하고, 같은 어조를 유지하며, 매 턴을 계속 \"다음 단계\" 블록으로 끝냅니다.",
    PA_NOTE="""> **무료 테스트 기간(2026-10-18 시작; 플랫폼의 실제 동작이 우선합니다)**: 이 기간에는 가입한 계정이 모든 기능을 바로 사용할 수 있고 **구독은 요구사항이 아니라 선택적 업그레이드**입니다 — 사용자가 스스로 멤버십을 원할 때만 이 파일의 플로우를 따르세요. 테스트 기간이 끝나면 구독하지 않은 계정이 콘텐츠 페이지를 방문할 때 구독 페이지로 리디렉션됩니다. 이 파일에 따라 구독을 완료하면 됩니다.""",
    RF_STATE="""## 가입 성공 후 상태 흐름

> **무료 테스트 기간(2026-10-18 시작; 플랫폼의 실제 동작이 우선합니다)**: 새로 가입한 계정은 결제 없이 **모든 기능을 바로 사용할 수 있습니다**
> (피드, 지도, 디지털 휴먼, 체크인 등). 구독하지 않은 계정은 더 이상 콘텐츠 페이지에서 차단되지 않습니다. 이 섹션에서 설명하는
> \"pending 차단\"은 테스트 기간이 끝난 뒤의 일반 상태입니다 — 그때가 되면 온라인의 실제 동작이 우선합니다.

1. 사용자는 `accountStatus: 'pending'`와 **시작 배지 3개**로 저장됩니다(register 경로).
2. 서버는 HttpOnly 쿠키 두 개도 심습니다: JWT(페이지에 바로 접근 가능)와 pendingUserToken(구독 플로우용 신원 증명).
3. 일반 상태(테스트 기간 종료 / 무료 기간 없음)에서는 가입 페이지가 `pending_payment`를 감지 → `/subscription`으로 리디렉트합니다
   (`next` 반환 파라미터를 유지하며). agent 대행 모드에서는 `me?token=…&redirect=/subscription`가 같은 효과를 냅니다.
   **무료 테스트 기간 중에는 이 단계가 발동하지 않습니다** — 가입 후 바로 홈으로 가서 사용을 시작하세요.
4. 결제 완료 → `accountStatus`가 `active`가 됩니다(**Alipay는 notify를 통해 서버 측에서 자동 활성화**;
   PayPal은 Webhook으로 활성화; WeChat QR 코드는 수동 확인; Huawei IAP는 `activate-huawei`를 통해 진행).
   자세한 내용은 `payment-and-activation.md`에 있습니다.

일반 상태에서 비활성(pending) 계정이 핵심 API(피드, 지도, 디지털 휴먼 채팅, 체크인 등)를 호출하면 403을 받습니다;
공유된 게시물 링크는 예외입니다(공개 접근을 유지함). 무료 테스트 기간 중에는 이 차단이 중단되고 모두 열려 있습니다.""",
    RF_ROW_403="| 가입은 성공했지만 로그인 시 403 \"请完成订阅以激活账户\" 반환 | 계정이 아직 pending이고 플랫폼이 무료 테스트 기간 중이 아닙니다(결제 전 예상 상태) | 무료 테스트 기간 중에는 발생하지 않습니다. 발생하면 테스트 기간이 끝난 것이므로 먼저 구독을 완료하세요. 결제 후에도 403이면 오래된 JWT를 사용한 것입니다 — 스크립트 모드에서 먼저 `refresh-login`를 실행해 새 로그인 상태로 교환하세요 |",
    RF_ROW_LAND="| 사용자가 로그인 링크를 클릭하지만 구독 페이지에 도착(홈이 아닌) | 무료 테스트 기간이 끝나고 플랫폼 페이월이 돌아왔습니다 | SKILL.md의 7단계 구독 결제 플로우를 따르세요. 구독 후 `refresh-login`를 실행한 뒤 홈 링크를 보냅니다 |",
    RD_VER="""**v2.0.0부터 agent 대행 모드이고, v2.2.0부터는 플랫폼의 무료 테스트 기간에도 적응합니다**: 핵심 스크립트 `scripts/powpow-register.mjs`는 무의존
(Node ≥ 18)입니다. 사용자가 대화를 떠나는 것은 단 한 번: 받은 편지함에서 인증 코드를 확인하기 위해서입니다. 현재 무료 테스트 기간 중에는 가입한 계정이 모든 기능을 바로 사용할 수 있고 — 멤버십 결제는 선택입니다. 테스트 기간이 끝나 사용자가 구독 페이지에 도착하면 플로우가 자동으로 결제 경로로 전환됩니다. Node가 없거나 사용자가 직접 하기를 원하면 자동으로 순수 안내 모드로 폴백합니다.""",
    RD_LINK="""3. **원클릭 로그인(듀얼 링크)**: 가입 성공 직후 로그인 링크로 사용자를 홈으로 바로 데려갑니다(무료 테스트 기간 중에는 한 번 클릭하면 사용 가능);
   구독 페이지에 도착하면(테스트 기간 종료) 또는 사용자가 업그레이드를 원하면 구독 플로우를 따릅니다 — 입금 후 새 로그인 상태로 교환하고, 완전 멤버십 링크로 홈에 도착합니다
   (HttpOnly 쿠키를 자동으로 심어주는 플랫폼 공식 `me?token=` 브리지를 통해).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
ES = dict(
    DESC="description: Ayuda a los usuarios a completar el registro de PowPow (Burbuja) y el inicio de sesión con un clic dentro de la conversación. El agent rellena el formulario en su nombre (incluida la subida de avatar) y envía el código de verificación por correo; el usuario solo aporta información básica y comprueba el código una vez, sin salir de la conversación. Durante el periodo actual de prueba gratuita de la plataforma, una cuenta registrada puede usar todas las funciones de inmediato; el pago de suscripción (Alipay/PayPal) es una mejora de membresía opcional, que el agent también puede gestionar con creación de pedidos y seguimiento del cobro cuando se necesite. Se activa cuando el usuario dice «registrarme en Burbuja», «crear una cuenta powpow», «cómo me registro en Burbuja», «ayúdame a crear una cuenta powpow», «sign up powpow»; también gestiona problemas de registro (código de verificación no recibido, nombre de usuario/correo ya ocupados) y problemas de activación (el login dice «cuenta no activada» / pending_payment, cómo suscribirse/pagar, ¿Burbuja es gratis o de pago?). Requiere Node ≥ 18; si no está disponible, vuelve automáticamente al modo de guía pura. No incluye publicar/crear humanos digitales (eso es cosa de powpow-simple) ni desarrollo de código.",
    INTRO="Lleva a un usuario nuevo desde «no sé qué es Burbuja» hasta «inicio de sesión con un clic, listo para jugar» — todo dentro de la conversación. El usuario solo sale de la conversación una vez: **para consultar el código de verificación en su correo**. La plataforma está actualmente en un periodo de prueba gratuita: una vez registrado, todas las funciones están disponibles, sin necesidad de pagar; el pago de suscripción es una mejora de membresía opcional (el agent también se encarga de abrir la caja y seguir el cobro).",
    VLINE="**Versión 2.2.0** · 2026-10-18 (desde v2 este es el modo asistido por agent: el contrato del script y la secuencia completa están en `references/agent-flow.md`; las reglas de campos, los límites de tasa y la resolución de errores en `references/registration-flow.md`; los canales de pago en `references/payment-and-activation.md`; la lista de capturas de producto en `references/screenshots.md`. Desde v2.1.0 las suscripciones de PayPal también pueden ser gestionadas por el agent, como opción junto a Alipay. Desde v2.2.0 la plataforma entra en un periodo de prueba gratuita: regístrate y entra con un clic para empezar a usar; el pago pasa a ser una mejora opcional — si el usuario abre el enlace y aterriza en la página de suscripción, el periodo de prueba ha terminado, así que sigue el flujo de pago del Paso 7; el flujo se adapta solo, sin necesidad de cambiar el script)",
    RT_ENV="- **Sin Node / errores del script**: vuelve automáticamente al modo de guía pura — dale al usuario la página de registro https://global.powpow.online/register y acompáñalo según `references/registration-flow.md` (durante el periodo de prueba gratuita, el registro web es igual de inmediato). No insistas con el script.",
    TRIGGER="- Problemas tras el registro: «el login dice que la cuenta no está activada», «403 pending_payment», «cómo pago/suscribo Burbuja», «¿Burbuja es gratis o de pago?»",
    FLOW6="| 6 Inicio de sesión con un clic | `login-link(home)` directo a la página de inicio; si aterriza en la página de suscripción, ve al Paso 7 | Haz clic en el enlace y empieza a jugar |",
    FLOW7="| 7 Mejora de suscripción (opcional) | Solo cuando el usuario quiere membresía / el periodo gratuito ha terminado: flujo de pago completo gestionado | Elige un método, paga |",
    STEP6="""## Paso 6: Inicio de sesión con un clic (directo a la página de inicio tras el registro)

1. Justo después de registrarte con éxito:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Envía el enlace al usuario: **ábrelo y aterrizarás directamente en la página de inicio, ya con la sesión iniciada**. La plataforma está actualmente en un periodo de prueba gratuita: tras registrarte, todas las funciones están disponibles (feed, mapa, humanos digitales, check-ins, etc.), **sin necesidad de pagar**.
3. Pide al usuario que confirme si ha entrado; hay dos casos:
   - **Aterrizó en la página de inicio** → pasa directamente al Paso 8 para cerrar; el registro está completo;
   - **Aterrizó en la página de suscripción** → el periodo de prueba gratuita de la plataforma ha terminado; dile al usuario «el periodo de prueba gratuito ha terminado, ahora se requiere una suscripción de membresía», luego sigue el Paso 7 para completar la suscripción y vuelve al Paso 8 cuando termines.
4. Si el usuario quiere activamente mejorar o apoyar la plataforma → ve también al Paso 7 (suscribirse es voluntario; no insistas).""",
    STEP7="""## Paso 7: Mejora de suscripción (opcional — solo cuando el Paso 6 lo requiera)

1. Primero envía el enlace de semi-sesión para que la página de retorno del pago muestre correctamente «Pago realizado»:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Envía el enlace al usuario: al abrirlo, el navegador aterriza directamente en la página de suscripción, ya con la sesión iniciada.
2. **Deja que el usuario elija el método de pago** — muestra ambos canales:
   - **Alipay (China continental / usuarios con Alipay)**: compra única de la duración correspondiente, **sin renovación automática**
     - Mensual **¥6.99** (recomendado para probar) / Trimestral **¥19.99** / Anual **¥69.99**
   - **PayPal (ultramar / usuarios sin Alipay)**: se renueva mensualmente, cancela cuando quieras
     - Premium Monthly, unos **$1/mes** (según lo mostrado en la página de suscripción; renovación automática)
3. Una vez que el usuario elige:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   El script devuelve la ruta del archivo de la página de pago; **ábrelo directamente con un comando del sistema** (Windows: `start <archivo>`; macOS: `open <archivo>`; Linux: `xdg-open <archivo>`). El navegador saltará automáticamente a la caja oficial de Alipay/PayPal, donde el usuario completa el pago o la autorización de facturación.
4. Ejecuta `query` cada 10–15 segundos hasta que devuelva `paid` o `ACTIVE` (el cobro/autorización suele llegar en unos segundos o un minuto). Si el usuario cierra la página de pago a mitad → vuelve a ejecutar `create-order` directamente (los pedidos antiguos / suscripciones pendientes se cierran o caducan automáticamente tras 2 horas; ignóralos).
5. El canal de código QR de WeChat se confirma manualmente y el cobro puede tardar; Huawei IAP solo está disponible dentro de la app HarmonyOS. El skill no gestiona esos dos — tras pagar, el usuario vuelve y lo cuenta, y el agent ejecuta primero `whoami` para confirmar el cobro y luego envía el enlace a la página de inicio del punto 6 siguiente.
6. Tras confirmar el cobro, cambia a un estado de sesión con la declaración de suscripción más reciente y envía el enlace directo a la página de inicio:
   ```
   POWPOW_REGISTER_PASSWORD=<contraseña> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Envía el enlace al usuario: **ábrelo y aterrizarás directamente en la página de inicio con la membresía completa**.""",
    STEP8="""## Paso 8: Cierre

1. `node scripts/powpow-register.mjs cleanup` para limpiar los archivos de estado temporales locales (credenciales de sesión).
2. Dale al usuario una «ficha de cuenta»: nombre de usuario, correo (la contraseña no se muestra de nuevo — en el modo generado ya se pidió al usuario que la guardara al generarla; si el usuario la puso él mismo, él la sabe).
3. Recordatorio de membresía (dilo una vez, no insistas): actualmente es un periodo de prueba gratuita y la cuenta se puede usar de inmediato; cuando el periodo de prueba termine, las cuentas sin suscripción que visiten páginas de contenido serán redirigidas a la página de suscripción — para un uso prolongado, vuelve y pide al agent que te suscriba cuando quieras.
4. Guía los primeros pasos: mirar el mapa, publicar el primer diario de viaje (→ pasa a powpow-simple).
5. Recomienda extensiones: el skill `@durenzidu/powpow-integration` y el plugin `@durenzidu/openclaw-channel-powpow` — conecta Burbuja con el agent del propio usuario; da el comando de instalación si lo quiere.
6. Cierra con un bloque de «siguiente paso».""",
    WALL="- **El muro de pago no es un bug**: durante el periodo actual de prueba gratuita todas las páginas de contenido están abiertas; si el usuario abre el enlace a la página de inicio pero aterriza en la página de suscripción, el periodo de prueba ha terminado — guíalo a suscribirse mediante el Paso 7. No intentes saltarte el muro de pago ni expliques mecanismos internos al usuario.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` o `--target home` | Genera un enlace de inicio de sesión con un clic (diseño de doble enlace, ver abajo) |",
    AF_LINKSEQ="""## Mecanismo de doble enlace (diseño central)

El estado de sesión de la plataforma es una cookie HttpOnly, que el agent no puede plantar directamente en el navegador; el puente es el endpoint oficial
`/api/auth/me?token=<JWT>&redirect=<ruta interna>`: verificar firma → crear sesión automáticamente
→ `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 días) → validar
redirect (debe empezar con una sola barra, prohibidos `//` y barras invertidas, debe ser del mismo origen tras el análisis) → 307 redirección temporal a la página de destino.

Hay dos destinos de enlace, **genera primero home y decide si pasar por pending según dónde aterrice el usuario**:

- **enlace home (enviado por defecto el primero, `--target home` → aterriza en `/`)**: se genera y envía al usuario inmediatamente después de registrarse con éxito.
  Durante el periodo de prueba gratuita el usuario entra directamente a la página de inicio y puede usar todo; **si el usuario lo abre pero aterriza en la página de suscripción, el periodo de prueba gratuita ha terminado** — cambia a la ruta de pago (ver abajo); no hacen falta cambios de script ni volver a registrarse.
- **enlace pending (usado en la ruta de pago, `--target pending` → aterriza en `/subscription`)**:
  el navegador del usuario entra en estado de «semi-sesión»: la página de suscripción y la página de retorno del pago son visibles y operables. Tras recibir el cobro,
  ejecuta `refresh-login` para cambiar a un nuevo JWT con la declaración ACTIVE y envía el enlace home una vez más para tener la membresía completa.

## Secuencia completa

### Ruta rápida (durante el periodo de prueba gratuita — la gran mayoría de los casos)

```
1.  status                          # autocomprobación del entorno
2.  (Paso 2 conversación para confirmar la info, contraseña a elegir; modo generado: gen-password → que el usuario la guarde de inmediato)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → el usuario consulta el código en su correo (la única vez que sale de la conversación)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → envía el enlace al usuario; un clic y está en la página de inicio
7.  (el usuario confirma que ha entrado) → cierra directamente: cleanup + ficha de cuenta + guía de primeros pasos
```

### Ruta de pago (cuando el usuario quiere membresía, o el periodo de prueba gratuita ha terminado)

```
1–5. Igual que la ruta rápida (el state ya tiene el token tras registrarse con éxito)
6.  login-link --target pending     # → enlace de semi-sesión, mantiene la página de retorno del pago funcionando
7.  (el usuario elige el método de pago)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <archivo de página de pago>   # Windows; macOS usa open, Linux usa xdg-open
    # → el usuario completa el pago/autorización en la caja de Alipay/PayPal (sale de la conversación)
9.  query (cada 10–15 s) hasta paid / ACTIVE
10. refresh-login                   # cambiar a un nuevo JWT con la declaración ACTIVE
11. login-link --target home        # → envía el enlace de membresía completa al usuario
12. whoami                          # confirmar subscriptionStatus: ACTIVE (opcional)
13. cleanup                         # limpiar el archivo de estado
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | El periodo de prueba gratuita ha terminado y el pago aún no ha llegado; vuelve al paso 9 para seguir sondeando, o confirma si el usuario completó el pago |",
    AF_ERR_SUB="| El usuario abre el enlace home pero aterriza en la página de suscripción | El periodo de prueba gratuita ha terminado → cambia a la ruta de pago: `login-link --target pending` → elige un método de pago → `create-order` |",
    AF_FALLBACK="Tras volver al modo guía: da la página de registro https://global.powpow.online/register (durante el periodo de prueba gratuita, el registro web es igual de inmediato; cuando se necesite suscripción, da también la página de suscripción https://global.powpow.online/subscription ), acompaña la resolución según las reglas de `registration-flow.md`, mantén el mismo tono y cierra cada turno con un bloque de «siguiente paso».",
    PA_NOTE="""> **Periodo de prueba gratuita (a partir del 2026-10-18; manda el comportamiento real de la plataforma)**: durante este periodo una cuenta registrada puede usar todas las funciones directamente, y **suscribirse es una mejora opcional, no un requisito** — sigue el flujo de este archivo solo cuando el usuario quiera activamente la membresía. Cuando el periodo de prueba termine, las cuentas sin suscripción que visiten páginas de contenido serán redirigidas a la página de suscripción; basta con completar la suscripción según este archivo.""",
    RF_STATE="""## Flujo de estado tras el registro exitoso

> **Periodo de prueba gratuita (a partir del 2026-10-18; manda el comportamiento real de la plataforma)**: una cuenta recién registrada puede **usar todas las funciones directamente**
> (feed, mapa, humanos digitales, check-ins, etc.) sin necesidad de pagar; las cuentas sin suscripción ya no son bloqueadas en las páginas de contenido. La descripción del
> «bloqueo pending» de esta sección es el estado normal tras el fin del periodo de prueba — cuando llegue ese momento, manda el comportamiento real en línea.

1. El usuario se guarda con `accountStatus: 'pending'` y **3 insignias iniciales** (register route).
2. El servidor planta además dos cookies HttpOnly: el JWT (puede acceder a las páginas directamente) y
   el pendingUserToken (credencial de identidad para el flujo de suscripción).
3. En el estado normal (periodo de prueba terminado / sin periodo gratuito), la página de registro detecta `pending_payment` → redirige a `/subscription`
   (conservando el parámetro de retorno `next`); en el modo asistido por agent, `me?token=…&redirect=/subscription` consigue el mismo efecto.
   **Durante el periodo de prueba gratuita este paso no se dispara** — tras registrarte, entra directamente a la página de inicio y empieza a usar.
4. Pago completado → `accountStatus` pasa a `active` (**Alipay activa automáticamente en el servidor vía notify**;
   PayPal activa vía Webhook; el código QR de WeChat se confirma manualmente; Huawei IAP pasa por `activate-huawei`).
   Ver detalles en `payment-and-activation.md`.

En el estado normal, los usuarios inactivos (pending) que llamen a las API núcleo (feed, mapa, chat de humanos digitales, check-ins, etc.) reciben 403;
los enlaces de posts compartidos son la excepción (se mantienen accesibles públicamente). Durante el periodo de prueba gratuita este bloqueo queda suspendido y todo está abierto.""",
    RF_ROW_403="| Registrado con éxito pero el login devuelve 403 «请完成订阅以激活账户» | La cuenta sigue pending, y la plataforma no está en un periodo de prueba gratuita (estado esperado antes de pagar) | No ocurre durante el periodo de prueba gratuita; si ocurre, el periodo de prueba ha terminado — completa primero la suscripción; si sigue dando 403 tras pagar, se usó un JWT antiguo — en el modo script ejecuta primero `refresh-login` para cambiar a un nuevo estado de sesión |",
    RF_ROW_LAND="| El usuario abre el enlace de login pero aterriza en la página de suscripción (en vez de la de inicio) | El periodo de prueba gratuita ha terminado y el muro de pago de la plataforma ha vuelto | Sigue el flujo de pago por suscripción del Paso 7 de SKILL.md; tras suscribirte, ejecuta `refresh-login` y luego envía el enlace a la página de inicio |",
    RD_VER="""**Desde v2.0.0 este es el modo asistido por agent, y desde v2.2.0 se adapta al periodo de prueba gratuita de la plataforma**: el script núcleo `scripts/powpow-register.mjs` es de cero dependencias
(Node ≥ 18); el usuario sale de la conversación solo una vez: para consultar el código de verificación en su correo. Durante el periodo actual de prueba gratuita, una cuenta registrada puede usar todas las funciones de inmediato — el pago de suscripción es una mejora opcional; si el periodo de prueba termina y el usuario aterriza en la página de suscripción, el flujo cambia automáticamente a la ruta de pago. Sin Node, o cuando el usuario prefiera hacerlo él mismo, vuelve automáticamente al modo de guía pura.""",
    RD_LINK="""3. **Inicio de sesión con un clic (doble enlace)**: justo tras registrarte con éxito, un enlace de login hace aterrizar al usuario directamente en la página de inicio (durante el periodo de prueba gratuita, un clic y listo);
   si aterriza en la página de suscripción (periodo de prueba terminado) o el usuario quiere mejorar, sigue el flujo de suscripción — tras recibir el cobro, se cambia a un nuevo estado de sesión y el enlace de membresía completa lo lleva a la página de inicio
   (a través del puente oficial `me?token=` de la plataforma, que planta la cookie HttpOnly automáticamente).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
