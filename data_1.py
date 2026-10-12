# -*- coding: utf-8 -*-
JA = dict(
    PA_CONCL_N=2,
    DESC=[
        ("Alipay サブスクリプションによるアクティベーション", "Alipay / PayPal サブスクリプションによるアクティベーション"),
        ("Alipay のレジで支払うこと", "Alipay / PayPal のレジで支払うこと"),
    ],
    INTRO=("**Alipay のレジで支払う**こと（agent がレジページを自動で開きます）",
           "**決済レジで支払う**こと（Alipay / PayPal。agent がレジページを自動で開きます）"),
    VLINE=[
        ("**バージョン 2.0.1** · 2026-10-08", "**バージョン 2.1.0** · 2026-10-11"),
        ("v2.0.1 より製品スクリーンショットは `assets/screenshots/` としてスキル本体に同梱され、外部画像ホスティングに依存しません",
         "v2.1.0 より PayPal サブスクも agent が代行でき、Alipay と並んで選べます"),
    ],
    STEP6="""2. **ユーザーに支払い方法を選んでもらいます**。2つのチャネルを提示：
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
5. WeChat スキャンは手動確認で着金が遅れることがあり、華為 IAP は HarmonyOS アプリ内のみ利用可能です。この2つは skill が代行しません。支払いが済んだら同じく第7ステップへ進みます。
""",
    BOUNDARY=("ユーザーの Alipay アカウント/決済証憑", "ユーザーの Alipay / PayPal アカウント/決済証憑"),
    PA_CONCL="""**Alipay と PayPal のサブスクはどちらも、agent が発注と着金トラッキングを代行できます。**
Alipay は一括買い切りで自動更新なし。中国国内 / Alipay を持っているユーザー向け。PayPal は月次の自動更新でいつでも解約可能、
海外 / Alipay を持たないユーザー向けです。WeChat スキャン（手動確認）と華為 IAP も残っていますが、skill は代行しません。""",
    PA_RESP=[
        ("**絶対に**ユーザーの Alipay", "**絶対に**ユーザーの Alipay / PayPal"),
        ("支払いの動作は常にユーザー本人が Alipay 公式レジで行います。", "支払いの動作は常にユーザー本人が公式レジで行います。"),
    ],
    PA_FRESH=("そこで skill は `paid` を確認した後、まず `refresh-login` を実行し",
              "そこで skill は `paid` / PayPal の `ACTIVE` を確認した後、まず `refresh-login` を実行し"),
    PA_PAYPAL="""## PayPal サブスクチャネル（skill が代行、Web 版かつ非 HarmonyOS）

プランは Premium Monthly の1つのみ（約 $1/月、`/api/subscription/plans` の返り値に準拠）。**月次の自動更新**で、
ユーザーはいつでも PayPal 側で解約できます。

### インターフェース契約（skill スクリプトがラップ済み。agent が直接リクエストを組み立てることはない）

| インターフェース | メソッド | 説明 |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer 認証。利用可能なプラン一覧を返す（現在は1つのみ） |
| `/api/subscription/create` | POST | body `{planId}` → `{subscriptionId, approveUrl, status}` を返す。`status` は通常 `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Bearer 認証。`{activeSubscription, allSubscriptions}` を返す。agent は `activeSubscription.subscription.status === 'ACTIVE'` をポーリング |
| `/api/subscription/verify` | POST | 成功ページが自動呼び出し（cookie 付き）。webhook 未着時に PayPal API で直接アクティベート |
| `/subscription/success` | ブラウザの戻りページ | PayPal 承認後の着地ページ。verify を自動ポーリングし、アクティベート後にホーム/元のページへ戻る |
| `/subscription/cancel` | ブラウザページ | ユーザーがキャンセルまたは失敗した場合の着地ページ。やり直し可能 |

### 代行フロー

```
create-order --provider paypal  # → approveUrl を返し、ローカル HTML ファイルに書き込む
HTML ファイルを開く             # → ブラウザが PayPal 承認ページへ遷移
query（10〜15秒ごと）            # → ACTIVE になるまでポーリング
refresh-login                   # → 新しい JWT に交換（サブスク宣言が ACTIVE）
login-link --target home        # → 正式なログインリンクを生成
```

- 1時間以内に完了しなかった PENDING サブスクはバックエンドが自動クリーンアップします。やり直せばOK。
- ユーザーが `create-order` を繰り返した場合、バックエンドは仍有効な `APPROVAL_PENDING` サブスクを再利用し、409 を回避します。
- Alipay と同じく：支払いの着金は DB を更新するだけで、古い JWT は自動的に更新されません。ホームページのリンクを送る前に**必ず** `refresh-login` を実行してください。""",
    PA_ROWS="""| PayPal の `query` がずっと PENDING | ユーザーが PayPal での承認を完了していません。ブラウザで承認リンクが開かれたか確認を。承認済みなのに PENDING なら webhook 遅延の可能性あり。成功ページで数秒待つか再読み込みしてもらう |
| PayPal の `query` が 409 を返す | 未完了の PENDING サブスクが既に存在します。1時間待てば自動失効。またはブラウザで旧リンクの承認を完了 |
| PayPal で支払ったのに、リンク2で入ってもまだ弾かれる | Alipay と同じ：先に `refresh-login`、それから `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly`（Alipay がデフォルト）<br>`--provider alipay\\|paypal` | 決済注文を作成。Alipay は支払いページのファイルパス + outTradeNo、PayPal は承認ページのファイルパス + subscriptionId を返す（自動で状態ファイルに記録） |",
    AF_ROW_QUERY="| `query` | —— | 注文/サブスクの状態を照会。Alipay：`paid / pending / closed / unknown`；PayPal：`ACTIVE / PENDING`。10〜15秒間隔でポーリング |",
    AF_SEQ7="""7.  （ユーザーが支払い方法を選択）
    # Alipay：create-order --package monthly|quarterly|yearly
    # PayPal：create-order --provider paypal""",
    AF_SEQ8=("# → ユーザーが Alipay のレジで支払い（会話離脱②）",
             "# → ユーザーが Alipay / PayPal のレジで支払い/承認を完了（会話離脱②）"),
    AF_SEQ9=("9.  query（10〜15秒ごと）paid になるまで", "9.  query（10〜15秒ごと）paid / ACTIVE になるまで"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order`（Bearer、Alipay）<br>`GET /api/subscription/plans` + `POST /api/subscription/create`（Bearer、PayPal） |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…`（Bearer、Alipay）<br>`GET /api/subscription/create`（Bearer、PayPal） |",
    AF_ERR_CLOSE=("| `create-order` 後にユーザーが支払いページを閉じた | そのまま `create-order` をやり直す（旧注文は2時間で自動クローズ） |",
                  "| `create-order` 後にユーザーが支払いページを閉じた | そのまま `create-order` をやり直す（旧注文は2時間で自動クローズ。PayPal の PENDING サブスクは1時間で失効） |"),
    AF_ERR_409="| `create-order --provider paypal` が 409 を返す | 未完了の PayPal サブスクが既に存在します。1時間待って失効させるか、ブラウザで旧承認を完了 |",
    AF_ERR_PEND=("| `query` がずっと pending | ユーザーが支払っていない可能性。一言尋ねる。本当に払っていたら → payment-and-activation.md の調査表へ |",
                 "| `query` がずっと pending / PENDING | ユーザーが支払っていない可能性。一言尋ねる。本当に払っていたら → payment-and-activation.md の調査表へ |"),
    AF_ERR_403=("支払いがまだ着金していない。", "支払い/承認がまだ着金していない。"),
    RD=[
        ("Alipay サブスクの発注と着金トラッキング", "Alipay / PayPal サブスクの発注と着金トラッキング"),
        ("**v2.0.0 以降は agent 代行モード**：コアスクリプト", "**v2.0.0 以降は agent 代行モード、v2.1.0 以降は PayPal も代行可能**：コアスクリプト"),
        ("メールボックスで認証コードを確認すること、Alipay のレジで支払うこと。",
         "メールボックスで認証コードを確認すること、Alipay / PayPal のレジで支払うこと。"),
        ("4. **サブスク決済**：Alipay チャネルは agent が発注を代行（月 ¥6.99 / 四半期 ¥19.99 /",
         "4. **サブスク決済**：Alipay（月 ¥6.99 / 四半期 ¥19.99 /"),
        ("年 ¥69.99、一括購入で自動更新なし）+ 着金ポーリング。海外ユーザーは PayPal へ",
         "年 ¥69.99、一括購入で自動更新なし）も PayPal（Premium Monthly、約 $1/月、自動更新、いつでも解約可）も agent が発注と着金ポーリングを代行。"),
        ("フォールバック。WeChat スキャン/華為 IAP は道案内のみ。", "WeChat スキャン/華為 IAP は道案内のみ。"),
        ("ユーザーの Alipay アカウント", "ユーザーの Alipay / PayPal アカウント"),
        ("Alipay 公式レジの間で完結します。", "公式レジの間で完結します。"),
    ],
)

KO = dict(
    PA_CONCL_N=2,
    DESC=[
        ("Alipay 구독 활성화", "Alipay/PayPal 구독 활성화"),
        ("Alipay 계산대에서 결제", "Alipay/PayPal 계산대에서 결제"),
    ],
    INTRO=("**Alipay 계산대에서 결제**(agent가 계산대 페이지를 자동으로 엽니다)",
           "**결제 계산대에서 결제**(Alipay/PayPal. agent가 계산대 페이지를 자동으로 엽니다)"),
    VLINE=[
        ("**버전 2.0.1** · 2026-10-08", "**버전 2.1.0** · 2026-10-11"),
        ("v2.0.1부터 제품 스크린샷이 `assets/screenshots/`로 스킬에 동봉되어 외부 이미지 호스팅에 의존하지 않습니다",
         "v2.1.0부터 PayPal 구독도 agent가 대행할 수 있어 Alipay와 나란히 선택 가능합니다"),
    ],
    STEP6="""2. **사용자에게 결제 수단을 고르게 합니다**. 두 채널을 모두 보여주세요:
   - **Alipay(중국 본토 / Alipay가 있는 사용자)**: 해당 기간을 일회성 구매, **자동 갱신 없음**
     - 월간 **¥6.99**(먼저 체험 추천)/ 분기 **¥19.99** / 연간 **¥69.99**
   - **PayPal(해외 / Alipay가 없는 사용자)**: 월간 자동 갱신, 언제든 해지 가능
     - Premium Monthly, 약 **$1/월**(구독 페이지 표시 기준, 자동 갱신)
3. 사용자가 고르면:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   스크립트가 결제 페이지 파일 경로를 반환하면, **시스템 명령으로 바로 엽니다**(Windows: `start <파일>`; macOS: `open <파일>`; Linux: `xdg-open <파일>`). 브라우저가 자동으로 Alipay/PayPal 공식 계산대로 이동하고, 사용자가 결제 또는 결제 승인을 완료합니다.
4. 10~15초마다 `query`를 실행해 `paid` 또는 `ACTIVE`가 반환될 때까지 반복합니다(입금/승인은 보통 수 초~1분). 사용자가 도중에 결제 페이지를 닫으면 → 그냥 `create-order`를 다시 실행합니다(이전 주문/대기 중 구독은 2시간 후 자동 종료 또는 만료, 신경 쓰지 않아도 됩니다).
5. WeChat 스캔 채널은 수동 확인이라 입금이 지연될 수 있고, 화웨이 IAP는 HarmonyOS 앱 안에서만 쓸 수 있습니다. 이 둘은 skill이 대행하지 않습니다. 결제가 끝나면 동일하게 7단계로 진행합니다.
""",
    BOUNDARY=("사용자의 Alipay 계정/결제 자격증명", "사용자의 Alipay/PayPal 계정/결제 자격증명"),
    PA_CONCL="""**Alipay 구독과 PayPal 구독 모두 agent가 발주와 입금 추적을 대행할 수 있습니다.**
Alipay는 일회성 구매로 자동 갱신이 없어 중국 본토/Alipay가 있는 사용자에게 맞고, PayPal은 월간 자동 갱신으로 언제든 해지 가능해
해외/Alipay가 없는 사용자에게 맞습니다. WeChat 스캔(수동 확인)과 화웨이 IAP도 남아 있지만 skill이 대행하지는 않습니다.""",
    PA_RESP=[
        ("사용자의 Alipay", "사용자의 Alipay/PayPal"),
        ("결제 행위는 항상 사용자 본인이 Alipay 공식 계산대에서 수행합니다.", "결제 행위는 항상 사용자 본인이 공식 계산대에서 수행합니다."),
    ],
    PA_FRESH=("그래서 skill은 `paid` 확인 후 먼저 `refresh-login`을 실행하고",
              "그래서 skill은 `paid` / PayPal `ACTIVE` 확인 후 먼저 `refresh-login`을 실행하고"),
    PA_PAYPAL="""## PayPal 구독 채널(skill 대행, 웹 버전이며 비(非) HarmonyOS)

플랜은 Premium Monthly 하나뿐입니다(약 $1/월, `/api/subscription/plans` 반환값 기준). **월간 자동 갱신**이며,
사용자는 언제든 PayPal에서 해지할 수 있습니다.

### 인터페이스 계약(skill 스크립트가 이미 래핑. agent가 직접 요청을 조립하지 않음)

| 인터페이스 | 메서드 | 설명 |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer 인증. 사용 가능한 플랜 목록 반환(현재 1개) |
| `/api/subscription/create` | POST | body `{planId}` → `{subscriptionId, approveUrl, status}` 반환. `status`는 보통 `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Bearer 인증. `{activeSubscription, allSubscriptions}` 반환. agent는 `activeSubscription.subscription.status === 'ACTIVE'`를 폴링 |
| `/api/subscription/verify` | POST | 성공 페이지가 자동 호출(cookie 포함). webhook이 안 왔을 때 PayPal API로 직접 활성화 |
| `/subscription/success` | 브라우저 리턴 페이지 | PayPal 승인 후 착지 페이지. verify를 자동 폴링하고 활성화 후 홈/원래 페이지로 복귀 |
| `/subscription/cancel` | 브라우저 페이지 | 사용자가 취소하거나 실패했을 때 착지 페이지. 다시 시작 가능 |

### 대행 흐름

```
create-order --provider paypal  # → approveUrl 반환, 로컬 HTML 파일로 기록
HTML 파일 열기                   # → 브라우저가 PayPal 승인 페이지로 이동
query(10~15초마다)               # → ACTIVE까지 폴링
refresh-login                   # → 새 JWT로 교체(구독 클레임 ACTIVE)
login-link --target home        # → 정식 로그인 링크 생성
```

- 1시간 안에 완료되지 않은 PENDING 구독은 백엔드가 자동 정리합니다. 다시 시작하면 됩니다.
- 사용자가 `create-order`를 반복하면 백엔드가 유효한 `APPROVAL_PENDING` 구독을 재사용해 409를 피합니다.
- Alipay와 동일: 입금은 DB만 갱신하고 기존 JWT는 자동 갱신되지 않으므로, 홈 링크를 보내기 전에 **반드시** `refresh-login`을 실행하세요.""",
    PA_ROWS="""| PayPal `query`가 계속 PENDING | 사용자가 PayPal에서 승인을 완료하지 않았습니다. 브라우저에서 승인 링크가 열렸는지 확인. 승인했는데도 PENDING이면 webhook 지연일 수 있으니 성공 페이지에서 몇 초 더 기다리거나 새로고침 |
| PayPal `query`가 409 반환 | 미완료 PENDING 구독이 이미 있습니다. 1시간 기다려 만료시키거나, 브라우저에서 이전 링크 승인을 완료 |
| PayPal 결제했는데 링크 2로 들어가도 계속 막힘 | Alipay와 동일: 먼저 `refresh-login`, 그다음 `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly`(Alipay 기본값)<br>`--provider alipay\\|paypal` | 결제 주문 생성. Alipay는 결제 페이지 파일 경로 + outTradeNo, PayPal은 승인 페이지 파일 경로 + subscriptionId 반환(자동으로 상태 파일에 기록) |",
    AF_ROW_QUERY="| `query` | —— | 주문/구독 상태 조회. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`. 10~15초 간격 폴링 |",
    AF_SEQ7="""7.  (사용자가 결제 수단 선택)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → 사용자가 Alipay 계산대에서 결제(대화 이탈 ②)",
             "# → 사용자가 Alipay/PayPal 계산대에서 결제/승인 완료(대화 이탈 ②)"),
    AF_SEQ9=("9.  query(10~15초마다) paid가 될 때까지", "9.  query(10~15초마다) paid / ACTIVE가 될 때까지"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order`(Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create`(Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…`(Bearer, Alipay)<br>`GET /api/subscription/create`(Bearer, PayPal) |",
    AF_ERR_CLOSE=("| `create-order` 후 사용자가 결제 페이지를 닫음 | 그냥 `create-order` 다시 실행(이전 주문은 2시간 후 자동 종료) |",
                  "| `create-order` 후 사용자가 결제 페이지를 닫음 | 그냥 `create-order` 다시 실행(이전 주문은 2시간 후 자동 종료. PayPal PENDING 구독은 1시간 후 만료) |"),
    AF_ERR_409="| `create-order --provider paypal`이 409 반환 | 미완료 PayPal 구독이 이미 있습니다. 1시간 기다려 만료시키거나 브라우저에서 이전 승인을 완료 |",
    AF_ERR_PEND=("| `query`가 계속 pending | 사용자가 결제하지 않았을 가능성. 한마디 물어보세요. 실제로 결제했다면 → payment-and-activation.md 해결 표대로 |",
                 "| `query`가 계속 pending / PENDING | 사용자가 결제하지 않았을 가능성. 한마디 물어보세요. 실제로 결제했다면 → payment-and-activation.md 해결 표대로 |"),
    AF_ERR_403=("결제가 아직 입금되지 않음.", "결제/승인이 아직 입금되지 않음."),
    RD=[
        ("Alipay 구독 주문 및 입금 추적", "Alipay/PayPal 구독 주문 및 입금 추적"),
        ("**v2.0.0부터 agent 대행 모드**: 핵심 스크립트", "**v2.0.0부터 agent 대행 모드, v2.1.0부터는 PayPal도 대행**: 핵심 스크립트"),
        ("메일함에서 인증번호 확인, Alipay 계산대에서 결제.", "메일함에서 인증번호 확인, Alipay/PayPal 계산대에서 결제."),
        ("4. **구독 결제**: Alipay 채널은 agent가 주문 대행(월 ¥6.99 / 분기 ¥19.99 / 연 ¥69.99,",
         "4. **구독 결제**: Alipay(월 ¥6.99 / 분기 ¥19.99 / 연 ¥69.99,"),
        ("일회성 구매로 자동 갱신 없음) + 입금 폴링. 해외 사용자는 PayPal로 폴백. WeChat",
         "일회성 구매로 자동 갱신 없음)와 PayPal(Premium Monthly, 약 $1/월, 자동 갱신, 언제든 해지) 모두 agent가 주문과 입금 폴링을 대행. WeChat"),
        ("사용자의 Alipay 계정이나", "사용자의 Alipay/PayPal 계정이나"),
        ("사용자와 Alipay 공식 계산대 사이에서 완료됩니다.", "사용자와 공식 계산대 사이에서 완료됩니다."),
    ],
)

ES = dict(
    PA_CONCL_N=2,
    DESC=[
        ("la activación de la suscripción con Alipay", "la activación de la suscripción con Alipay o PayPal"),
        ("paga en la caja de Alipay", "paga en la caja de Alipay o PayPal"),
    ],
    INTRO=("**pagar en la caja de Alipay** (el agent abre automáticamente la página de pago)",
           "**pagar en la caja de pago** (Alipay o PayPal — el agent abre automáticamente la página de pago)"),
    VLINE=[
        ("**Versión 2.0.1** · 2026-10-08", "**Versión 2.1.0** · 2026-10-11"),
        ("Desde v2.0.1 las capturas del producto viajan con la habilidad en `assets/screenshots/`, sin depender de un hospedaje externo de imágenes",
         "Desde v2.1.0 el agent también puede gestionar las suscripciones PayPal, como opción junto a Alipay"),
    ],
    STEP6="""2. **Haz que el usuario elija un método de pago**; muéstrale los dos canales:
   - **Alipay (China continental / usuarios con Alipay)**: compra única del periodo correspondiente, **sin renovación automática**
     - Mensual **¥6.99** (recomendado para empezar a probar) / Trimestral **¥19.99** / Anual **¥69.99**
   - **PayPal (extranjero / usuarios sin Alipay)**: renovación automática mensual, se puede cancelar cuando se quiera
     - Premium Monthly, unos **$1/mes** (según lo que muestre la página de suscripción; con renovación automática)
3. Cuando el usuario elija:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   El script devuelve la ruta del archivo de la página de pago; **ábrela directamente con un comando del sistema** (Windows: `start <archivo>`; macOS: `open <archivo>`; Linux: `xdg-open <archivo>`). El navegador salta automáticamente a la caja oficial de Alipay o PayPal, donde el usuario completa el pago o la autorización de cargo.
4. Ejecuta `query` cada 10–15 segundos hasta que devuelva `paid` o `ACTIVE` (el cobro o la autorización suelen tardar de unos segundos a un minuto). Si el usuario cierra la página de pago a medias → vuelve a ejecutar `create-order` sin más (los pedidos viejos caducan y las suscripciones pendientes expiran solas a las 2 horas; no hay que ocuparse de ellos).
5. El canal de código QR de WeChat es de confirmación manual y el cobro puede retrasarse; Huawei IAP solo está disponible dentro de la app de HarmonyOS. La habilidad no gestiona esos dos: una vez pagado, se vuelve igualmente al paso 7.
""",
    BOUNDARY=("la cuenta Alipay del usuario ni sus credenciales de pago", "la cuenta Alipay/PayPal del usuario ni sus credenciales de pago"),
    PA_CONCL="""**Tanto las suscripciones por Alipay como por PayPal las puede gestionar el agent: creación del pedido y seguimiento del cobro incluidos.**
Alipay es una compra única sin renovación automática, para usuarios de China continental y usuarios con Alipay; PayPal se renueva automáticamente cada mes y se puede cancelar en cualquier momento,
para usuarios en el extranjero y sin Alipay. El código QR de WeChat (confirmación manual) y Huawei IAP siguen existiendo, pero la habilidad no los gestiona.""",
    PA_RESP=[
        ("**jamás** toca la cuenta Alipay", "**jamás** toca la cuenta Alipay/PayPal"),
        ("La acción de pagar la realiza siempre el propio usuario en la caja oficial de Alipay.",
         "La acción de pagar la realiza siempre el propio usuario en la caja oficial."),
    ],
    PA_FRESH=("Por eso la habilidad, tras confirmar el `paid`, ejecuta primero `refresh-login`",
              "Por eso la habilidad, tras confirmar el `paid` / el `ACTIVE` de PayPal, ejecuta primero `refresh-login`"),
    PA_PAYPAL="""## Canal de suscripción PayPal (lo gestiona la habilidad; web no HarmonyOS)

Solo hay un plan, Premium Monthly (unos $1/mes, según lo que devuelva `/api/subscription/plans`); **se renueva automáticamente cada mes**
y el usuario puede cancelarlo cuando quiera desde su cuenta de PayPal.

### Contrato de API (ya encapsulado por el script de la habilidad; el agent nunca arma las peticiones directamente)

| Endpoint | Método | Notas |
|---|---|---|
| `/api/subscription/plans` | GET | Auth Bearer; devuelve la lista de planes disponibles (ahora mismo solo 1) |
| `/api/subscription/create` | POST | Cuerpo `{planId}` → devuelve `{subscriptionId, approveUrl, status}`; `status` suele ser `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Auth Bearer; devuelve `{activeSubscription, allSubscriptions}`; el agente sondea `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | La llama automáticamente la página de éxito (con la cookie); activa directamente vía la API de PayPal si el webhook no ha llegado |
| `/subscription/success` | Página de retorno del navegador | Aterriza tras la autorización de PayPal; sondea verify automáticamente y vuelve al inicio / a la página original |
| `/subscription/cancel` | Página del navegador | Aterriza si el usuario cancela o algo falla; se puede reintentar |

### Flujo delegado

```
create-order --provider paypal  # → devuelve approveUrl, escrito en un archivo HTML local
abrir el archivo HTML           # → el navegador salta a la página de autorización de PayPal
query (cada 10–15 s)            # → sondear hasta ACTIVE
refresh-login                   # → cambiar a un JWT nuevo (declaración de suscripción ACTIVE)
login-link --target home        # → generar el enlace de inicio de sesión definitivo
```

- Las suscripciones PENDING que no se completan en 1 hora las limpia el backend automáticamente; basta con empezar de nuevo.
- Si el usuario repite `create-order`, el backend reutiliza la suscripción `APPROVAL_PENDING` aún válida, evitando un 409.
- Igual que con Alipay: el cobro solo actualiza la base de datos, el JWT viejo no se refresca solo, así que **hay que** ejecutar `refresh-login` antes de enviar el enlace al inicio.""",
    PA_ROWS="""| El `query` de PayPal sigue en PENDING | El usuario no ha terminado la autorización en PayPal; confirma que el enlace de autorización se abrió en el navegador. Si sigue PENDING tras autorizar, puede ser un retraso del webhook: pide al usuario que espere unos segundos más en la página de éxito o que la recargue |
| El `query` de PayPal devuelve 409 | Ya existe una suscripción PENDING sin terminar; espera 1 hora a que expire o completa la autorización del enlace antiguo en el navegador |
| PayPal pagado, pero al entrar con el enlace 2 sigue bloqueado | Igual que con Alipay: primero `refresh-login` y luego `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay por defecto)<br>`--provider alipay\\|paypal` | Crea el pedido de pago; Alipay devuelve la ruta del archivo de la página de pago + outTradeNo; PayPal devuelve la ruta del archivo de la página de autorización + subscriptionId (anotado automáticamente en el archivo de estado) |",
    AF_ROW_QUERY="| `query` | —— | Consulta el estado del pedido/suscripción. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; sondeo cada 10–15s |",
    AF_SEQ7="""7.  (el usuario elige método de pago)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → el usuario paga en la caja de Alipay (salida de la conversación, momento ②)",
             "# → el usuario completa el pago/autorización en la caja de Alipay/PayPal (salida de la conversación, momento ②)"),
    AF_SEQ9=("9.  query (cada 10–15s) hasta paid", "9.  query (cada 10–15s) hasta paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| El usuario cerró la página de pago tras `create-order` | Vuelve a ejecutar `create-order` directamente (el pedido viejo se cierra solo a las 2h) |",
                  "| El usuario cerró la página de pago tras `create-order` | Vuelve a ejecutar `create-order` directamente (el pedido viejo se cierra solo a las 2h; las suscripciones PENDING de PayPal expiran a la 1h) |"),
    AF_ERR_409="| `create-order --provider paypal` devuelve 409 | Ya hay una suscripción de PayPal sin terminar; espera 1h a que expire o completa la autorización antigua en el navegador |",
    AF_ERR_PEND=("| `query` sigue en pending | Puede que el usuario no haya pagado; pregunta. Si de verdad pagó → sigue la tabla de diagnóstico de payment-and-activation.md |",
                 "| `query` sigue en pending / PENDING | Puede que el usuario no haya pagado; pregunta. Si de verdad pagó → sigue la tabla de diagnóstico de payment-and-activation.md |"),
    AF_ERR_403=("El cobro aún no ha llegado;", "El cobro o la autorización aún no ha llegado;"),
    RD=[
        ("creación del pedido de suscripción en Alipay con seguimiento del cobro",
         "creación del pedido de suscripción en Alipay o PayPal con seguimiento del cobro"),
        ("**Desde v2.0.0 el modo es de gestión delegada en el agent**",
         "**Desde v2.0.0 el modo es de gestión delegada en el agent, y desde v2.1.0 también se gestiona PayPal**"),
        ("para mirar el código en su correo y para pagar en la caja de Alipay.",
         "para mirar el código en su correo y para pagar en la caja de Alipay o PayPal."),
        ("4. **Suscripción y pago**: por el canal de Alipay el agent gestiona el pedido (mensual ¥6.99 / trimestral ¥19.99 / anual ¥69.99, compra única sin renovación automática) + sondeo del cobro; los usuarios en el extranjero retroceden a PayPal; el código QR de WeChat y el IAP de Huawei solo se indican.",
         "4. **Suscripción y pago**: tanto Alipay (mensual ¥6.99 / trimestral ¥19.99 / anual ¥69.99, compra única sin renovación automática) como PayPal (Premium Monthly, unos $1/mes, con renovación automática y cancelación en cualquier momento) los gestiona el agent con creación del pedido + sondeo del cobro; el código QR de WeChat y el IAP de Huawei solo se indican."),
        ("jamás toca la cuenta Alipay del usuario ni sus credenciales de pago, jamás paga por él. El pago ocurre siempre entre el usuario y la caja oficial de Alipay.",
         "jamás toca la cuenta Alipay/PayPal del usuario ni sus credenciales de pago, jamás paga por él. El pago ocurre siempre entre el usuario y la caja oficial."),
    ],
)
