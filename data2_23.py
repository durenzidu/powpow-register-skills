# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: Nigerian Pidgin."""
PCM = dict(
    DESC="description: E dey help user complete PowPow (Bubble) registration and one-click login inside di conversation. Di agent dey fill di form for di user (including avatar upload) and dey send di email verification code; di user only need to give basic info and check di verification code once — without comot for di conversation. Di platform dey now inside free testing period: account wey don register fit use every feature at once; subscription payment (Alipay/PayPal) na optional membership upgrade, wey di agent fit still handle am with order creation and money arrival tracking wen e need. E dey trigger wen user talk say \"register for Bubble\", \"create powpow account\", \"how I go register for Bubble\", \"help me create powpow account\", \"sign up powpow\"; e still dey handle registration wahala (verification code no come, username/email don already taken) and activation wahala (login dey talk say \"account no activate\" / pending_payment, how I go subscribe/pay, Bubble free or e dey cost). E need Node ≥ 18; if e no dey, e dey fall back by imself to pure guidance mode. E no cover posting/creating digital human (na powpow-simple work), e no cover code development.",
    INTRO="E dey carry new user from \"I no know wetin Bubble be\" reach \"one-click login, ready to play\" — all inside di conversation. Di user dey comot from di conversation only once: **to check di verification code inside inbox**. Di platform dey now inside free testing period: after you register, every feature dey available, no need to pay; subscription payment na optional membership upgrade (di agent still dey open di cashier and dey track money arrival).",
    VLINE="**Version 2.2.0** · 2026-10-18 (since v2 dis one na agent-helper mode: script contract and full sequence dey for `references/agent-flow.md`; field rules, rate limits and error wahala dey for `references/registration-flow.md`; payment channels dey for `references/payment-and-activation.md`; product screenshot list dey for `references/screenshots.md`. Since v2.1.0 di agent fit still handle PayPal subscription, as option alongside Alipay. Since v2.2.0 di platform don enter free testing period: register and one-click login fit use am at once; payment don turn optional upgrade — if user click di link and land for subscription page, di testing period don end, follow di payment flow from step 7; di flow dey adapt imself, no need to change script)",
    RT_ENV="- **No Node / script error**: e dey fall back by imself to pure guidance mode — give user di registration page https://global.powpow.online/register and guide am along per `references/registration-flow.md` (during free testing period, web registration dey equally instant). No dey keep hammer di script.",
    TRIGGER="- Wahala after registration: \"login dey talk say account no activate\", \"403 pending_payment\", \"how I go pay/subscribe for Bubble\", \"Bubble free or e dey cost\"",
    FLOW6="| 6 One-click login | `login-link(home)` straight into home page; if e land for subscription page, go to step 7 | Click di link and start to play |",
    FLOW7="| 7 Subscription upgrade (optional) | Only wen user want membership / free period don end: handle full payment flow | Pick method, pay |",
    STEP6="""## Step 6: One-Click Login (straight into home page after registration)

1. Right after registration succeed:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Send di link to user: **click am and you land directly for home page, you don already login**. Di platform dey now inside free testing period — after you register, every feature dey usable (feed, map, digital human, check-ins, etc.), **no need to pay**.
3. Ask user to confirm say e don enter; two cases dey:
   - **E land for home page** → go straight to step 8 to wrap up; registration don complete;
   - **E land for subscription page** → di platform free testing period don end; tell di user "di free trial period don end, membership subscription dey needed now", then follow step 7 to complete di subscription, and come back to step 8 after you subscribe.
4. If user by imself want upgrade or support di platform → still go to step 7 (subscribing na voluntary; no dey push).""",
    STEP7="""## Step 7: Subscription Upgrade (optional — only wen step 6 talk am)

1. First send di half-login link so say di payment return page fit correctly show "Payment successful":
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Send di link to user: click am and browser land directly for subscription page, already login.
2. **Tell user make e choose payment method** — show both channels:
   - **Alipay (mainland China / users wey get Alipay)**: one-time purchase of di duration, **no auto-renewal**
     - Monthly **¥6.99** (recommended for trying) / Quarterly **¥19.99** / Yearly **¥69.99**
   - **PayPal (overseas / users wey no get Alipay)**: e dey renew every month, fit cancel anytime
     - Premium Monthly, about **$1/month** (as dem show am for subscription page; e dey renew by imself)
3. Once user pick one:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Di script go return di payment page file path; **open am directly with system command** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Di browser go jump by imself to di official Alipay/PayPal cashier, where di user go complete di payment or di billing authorization.
4. Run `query` every 10–15 seconds until e return `paid` or `ACTIVE` (payment/authorization usually dey land within some seconds to one minute). If user close di payment page for middle → just `create-order` again (old orders / pending subscriptions go close or expire after 2 hours; no mind dem).
5. Di WeChat QR-code channel dey confirm manually and money fit arrive late; Huawei IAP dey only available inside di HarmonyOS App. Di skill no handle those two — after payment, di user dey come back and tell di agent, wey first run `whoami` to confirm arrival, then send di home page link per point 6 below.
6. After arrival don confirm, exchange for login state with di latest subscription claim, then send di link straight to home page:
   ```
   POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Send di link to user: **click am and you land directly for home page with full membership status**.""",
    STEP8="""## Step 8: Wrap-Up

1. `node scripts/powpow-register.mjs cleanup` to clean up local temporary state files (session credentials).
2. Give di user "account card": username, email (di password no dey show again — for generated mode di user bin talk say make e save am when dem generate am; if di user set am by imself, e know am).
3. Membership reminder (talk am once, no dey push): dis one na free testing period and di account dey usable at once; wen di testing period end, accounts wey no subscribe and visit content pages go dey redirect to di subscription page — for long-term use, come back and find di agent to subscribe anytime.
4. Guide di first steps: browse di map, post di first travel journal (→ hand am over to powpow-simple).
5. Recommend extensions: di `@durenzidu/powpow-integration` skill and di `@durenzidu/openclaw-channel-powpow` plugin — connect Bubble into di user own agent; give di install command if e want.
6. End with "next step" block.""",
    WALL="- **Di paywall no be bug**: during di current free testing period all content pages dey open; if user click di home page link but land for subscription page, di testing period don end — guide am to subscribe via step 7. No dey try to bypass di paywall, and no dey explain internal mechanism to di user.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` or `--target home` | E dey generate one-click login link (dual-link design, see below) |",
    AF_LINKSEQ="""## Dual-Link Mechanism (core design)

Di platform login state na HttpOnly cookie, wey di agent no fit plant am for di browser directly; di bridge na di official
`/api/auth/me?token=<JWT>&redirect=<in-site path>` endpoint: verify signature → auto-create
session → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 days) → validate
redirect (must start with single slash, `//` and backslash dem forbid, must be same-origin after parsing) → 307 temporary redirect to di target page.

Two link targets dey, **first generate home, then decide whether to pass through pending based on where di user land**:

- **home link (wey dem dey send by default, `--target home` → land for `/`)**: dem dey generate am and send to di user right after registration succeed.
  During di free testing period di user dey go straight to di home page, fully usable; **if di user click am but land for di subscription page, di free testing period don end** — switch to di payment path (see below); no need to change script and no need to register again.
- **pending link (wey dem dey use for di payment path, `--target pending` → land for `/subscription`)**:
  di user browser dey enter "half-logged-in" state: di subscription page and di payment return page dey visible and dey workable. After payment arrive,
  run `refresh-login` to exchange for new JWT with di ACTIVE claim, then send di home link again for di full membership state.

## Full Sequence

### Fast Path (during di free testing period — di vast majority of cases)

```
1.  status                          # environment self-check
2.  (step 2 conversation to confirm info, password either/or; generated mode: gen-password → tell di user make e save am at once)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → user check di code for inbox (di only time to comot from di conversation)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → send di link to di user; one click and e don dey for home page
7.  (user confirm say e don enter) → wrap up directly: cleanup + account card + guide di first steps
```

### Payment Path (wen di user want membership, or di free testing period don end)

```
1–5. Same as di fast path (di state already get di token after register succeed)
6.  login-link --target pending     # → half-login link, keep di payment return page working
7.  (user pick payment method)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <payment page file>       # Windows; macOS dey use open, Linux dey use xdg-open
    # → di user complete payment/authorization for di Alipay/PayPal cashier (e comot from di conversation)
9.  query (every 10–15s) until paid / ACTIVE
10. refresh-login                   # exchange for new JWT with di ACTIVE claim
11. login-link --target home        # → send di full-membership link to di user
12. whoami                          # confirm subscriptionStatus: ACTIVE (optional)
13. cleanup                         # clear di state file
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Di free testing period don end and payment no arrive; go back to step 9 to keep polling, or confirm whether di user complete di payment |",
    AF_ERR_SUB="| User click di home link but land for di subscription page | Di free testing period don end → switch to di payment path: `login-link --target pending` → pick payment method → `create-order` |",
    AF_FALLBACK="After you fall back: give di registration page https://global.powpow.online/register (during di free testing period, web registration dey equally instant; wen subscription dey needed, still give di subscription page https://global.powpow.online/subscription ), troubleshoot along per di rules for `registration-flow.md`, keep di same tone, and still end every turn with \"next step\" block.",
    PA_NOTE="""> **Free testing period (starting 2026-10-18; di platform real behavior dey prevail)**: during dis period account wey don register fit use every feature directly, and **subscribing na optional upgrade no be requirement** — only follow dis file flow wen di user by imself want membership. Wen di testing period end, accounts wey no subscribe and visit content pages go dey redirect to di subscription page; just complete di subscription per dis file.""",
    RF_STATE="""## Status Flow After Registration Succeed

> **Free testing period (starting 2026-10-18; di platform real behavior dey prevail)**: new account wey don register fit **use every feature directly**
> (feed, map, digital human, check-ins, etc.) with no payment; accounts wey no subscribe no dey wall again from content pages. Di "pending interception"
> wey dem describe for dis section na di regular state after di testing period end — wen dat time come, di real online behavior dey prevail.

1. Di user dey store with `accountStatus: 'pending'` and **3 initial badges** (register route).
2. Di server still dey plant two HttpOnly cookies: di JWT (fit access pages directly) and di pendingUserToken (identity credential for di subscription flow).
3. For di regular state (testing period over / no free period), di registration page dey detect `pending_payment` → redirect to `/subscription`
   (keeping di `next` return parameter); for agent-helper mode, `me?token=…&redirect=/subscription` dey get di same effect.
   **During di free testing period dis step no dey trigger** — after you register, go straight to di home page and start to use am.
4. Payment complete → `accountStatus` turn `active` (**Alipay dey activate automatically server-side via notify**;
   PayPal dey activate via Webhook; WeChat QR code dey confirm manually; Huawei IAP dey pass through `activate-huawei`).
   See `payment-and-activation.md` for details.

For di regular state, inactive (pending) users wey dey call core APIs (feed, map, digital-human chat, check-ins, etc.) dey get 403;
shared post links na di exception (dem dey keep am publicly accessible). During di free testing period dis interception dey suspended and everything dey open.""",
    RF_ROW_403="| Register succeed but login return 403 \"请完成订阅以激活账户\" | Di account still dey pending, and di platform no dey inside free testing period (di expected state before payment) | E no go happen during di free testing period; if e happen, di testing period don end — complete di subscription first; if e still 403 after payment, old JWT dem use — for script mode first run `refresh-login` to exchange for new login state |",
    RF_ROW_LAND="| User click di login link but land for di subscription page (instead of di home page) | Di free testing period don end and di platform paywall don come back | Follow step 7 inside SKILL.md for di subscription payment flow; after you subscribe, run `refresh-login` and then send di home page link |",
    RD_VER="""**Since v2.0.0 dis one na agent-helper mode, and since v2.2.0 e dey adapt to di platform free testing period**: di core script `scripts/powpow-register.mjs` na zero-dependency
(Node ≥ 18); di user dey comot from di conversation only once: to check di verification code for inbox. During di current free testing period, account wey don register fit use every feature at once — subscription payment na optional upgrade; if di testing period end and di user land for di subscription page, di flow dey switch to di payment path by imself. Without Node, or wen di user prefer to do am by imself, e dey fall back by imself to pure guidance mode.""",
    RD_LINK="""3. **One-click login (dual links)**: right after registration succeed, login link dey land di user directly for di home page (during di free testing period, one click and e dey usable);
   if e land for di subscription page (testing period over) or di user want to upgrade, follow di subscription flow — after payment arrive, fresh login state dey exchange and di full-membership link land am for di home page
   (via di platform official `me?token=` bridge, wey dey plant di HttpOnly cookie automatically).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
