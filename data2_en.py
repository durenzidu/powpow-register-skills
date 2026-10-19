# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: English (template for all other languages)."""
EN = dict(
    DESC="description: Helps users complete PowPow (Bubble) registration and one-click login entirely inside the conversation. The agent fills in the form on their behalf (including avatar upload) and sends the email verification code; the user only provides basic information and checks the verification code once — never leaving the conversation. During the platform's current free testing period, a registered account can use every feature right away; subscription payment (Alipay/PayPal) is an optional membership upgrade, which the agent can also handle with order creation and arrival tracking when needed. Triggers when the user says \"register for Bubble\", \"sign up for a powpow account\", \"how do I register for Bubble\", \"help me create a powpow account\", \"sign up powpow\"; also handles registration issues (verification code not received, username/email already taken) and activation issues (login says \"account not activated\" / pending_payment, how to subscribe/pay, is Bubble free/paid). Requires Node ≥ 18; automatically falls back to pure guidance mode when unavailable. Does not cover posting/creating digital humans (that's powpow-simple's job), nor code development.",
    INTRO="Takes a new user from \"I don't know what Bubble is\" to \"one-click logged in, ready to play\" — entirely inside the conversation. The user leaves the conversation only once: **to check the verification code in their inbox**. The platform is currently in a free testing period: once registered, every feature is usable, no payment needed; subscription payment is an optional membership upgrade (the agent also handles opening the cashier and tracking arrival).",
    VLINE="**Version 2.2.0** · 2026-10-18 (since v2 this is agent-assisted mode: script contract and full sequence in `references/agent-flow.md`; field rules, rate limits and error troubleshooting in `references/registration-flow.md`; payment channels in `references/payment-and-activation.md`; product screenshot list in `references/screenshots.md`. Since v2.1.0 PayPal subscriptions can also be handled by the agent, as an option alongside Alipay. Since v2.2.0 the platform is in a free testing period: register and one-click login to start using; payment becomes an optional upgrade — if the user clicks the link and lands on the subscription page, the testing period has ended, so follow the Step 7 payment flow; the flow adapts itself, no script changes needed)",
    RT_ENV="- **No Node / script errors**: automatically fall back to pure guidance mode — give the user the registration page https://global.powpow.online/register and guide them alongside per `references/registration-flow.md` (during the free testing period, web registration is equally instant). Don't keep hammering the script.",
    TRIGGER="- Post-registration issues: \"login says the account is not activated\", \"403 pending_payment\", \"how do I pay for/subscribe to Bubble\", \"is Bubble free/paid\"",
    FLOW6="| 6 One-click login | `login-link(home)` straight into the home page; if it lands on the subscription page, go to Step 7 | Click the link and start playing |",
    FLOW7="| 7 Subscription upgrade (optional) | Only when the user wants membership / the free period has ended: full payment flow handled | Pick a method, pay |",
    STEP6="""## Step 6: One-Click Login (straight into the home page after registration)

1. Right after successful registration:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Send the link to the user: **click it and you land directly on the home page, already logged in**. The platform is currently in a free testing period — after registering, every feature is usable (feed, map, digital humans, check-ins, etc.), **no payment needed**.
3. Ask the user to confirm they got in; there are two cases:
   - **Landed on the home page** → jump straight to Step 8 to wrap up; registration is complete;
   - **Landed on the subscription page** → the platform's free testing period has ended; tell the user "the free trial period is over, a membership subscription is required now", then follow Step 7 to complete the subscription, and come back to Step 8 after subscribing.
4. If the user actively wants to upgrade or support the platform → also go to Step 7 (subscribing is voluntary; don't push).""",
    STEP7="""## Step 7: Subscription Upgrade (optional — only when Step 6 calls for it)

1. First send the half-login link so the payment return page can correctly show "Payment successful":
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Send the link to the user: clicking it lands the browser directly on the subscription page, already logged in.
2. **Have the user choose a payment method** — show both channels:
   - **Alipay (mainland China / users with Alipay)**: one-time purchase of the corresponding duration, **no auto-renewal**
     - Monthly **¥6.99** (recommended for trying) / Quarterly **¥19.99** / Yearly **¥69.99**
   - **PayPal (overseas / users without Alipay)**: auto-renews monthly, cancel anytime
     - Premium Monthly, about **$1/month** (as shown on the subscription page; auto-renews)
3. Once the user picks one:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   The script returns the payment page file path; **open it directly with a system command** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). The browser automatically jumps to the official Alipay/PayPal cashier, where the user completes the payment or the billing authorization.
4. Run `query` every 10–15 seconds until it returns `paid` or `ACTIVE` (payment/authorization usually lands within a few seconds to a minute). If the user closes the payment page midway → just `create-order` again (old orders / pending subscriptions auto-close or expire after 2 hours; ignore them).
5. The WeChat QR-code channel is manually confirmed and funds may arrive late; Huawei IAP is only available inside the HarmonyOS App. The skill doesn't handle those two — after paying, the user comes back and tells the agent, who first runs `whoami` to confirm arrival, then sends the home-page link per point 6 below.
6. After arrival is confirmed, exchange for a login state with the latest subscription claim, then send the link straight to the home page:
   ```
   POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Send the link to the user: **click it and you land directly on the home page with full membership status**.""",
    STEP8="""## Step 8: Wrap-Up

1. `node scripts/powpow-register.mjs cleanup` to clean up local temporary state files (session credentials).
2. Give the user an "account card": username, email (the password is not shown again — in generated mode the user was asked to save it when it was generated; if the user set it themselves, they know it).
3. Membership reminder (say it once, don't push): this is currently a free testing period and the account is usable right away; when the testing period ends, unsubscribed accounts visiting content pages will be redirected to the subscription page — for long-term use, come back and find the agent to subscribe anytime.
4. Guide the first steps: browse the map, post the first travel journal (→ hand off to powpow-simple).
5. Recommend extensions: the `@durenzidu/powpow-integration` skill and the `@durenzidu/openclaw-channel-powpow` plugin — connect Bubble into the user's own agent; give the install command if wanted.
6. End with a "next step" block.""",
    WALL="- **The paywall is not a bug**: during the current free testing period all content pages are open; if the user clicks the home-page link but lands on the subscription page, the testing period has ended — guide them to subscribe via Step 7. Don't try to bypass the paywall, and don't explain internal mechanisms to the user.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` or `--target home` | Generates a one-click login link (dual-link design, see below) |",
    AF_LINKSEQ="""## Dual-Link Mechanism (core design)

The platform's login state is an HttpOnly cookie, which the agent cannot plant for the browser directly; the bridge is the official
`/api/auth/me?token=<JWT>&redirect=<in-site path>` endpoint: verify signature → auto-create
session → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 days) → validate
redirect (must start with a single slash, `//` and backslashes forbidden, must be same-origin after parsing) → 307 temporary redirect to the target page.

There are two link targets, **generate home first, then decide whether to go through pending based on where the user lands**:

- **home link (sent by default, `--target home` → lands on `/`)**: generated and sent to the user immediately after successful registration.
  During the free testing period the user goes straight to the home page, fully usable; **if the user clicks it but lands on the subscription page, the free testing period has ended** — switch to the payment path (see below); no script changes and no re-registration needed.
- **pending link (used in the payment path, `--target pending` → lands on `/subscription`)**:
  the user's browser enters a "half-logged-in" state: the subscription page and payment return page are visible and operable. After payment arrives,
  run `refresh-login` to exchange for a new JWT with the ACTIVE claim, then send the home link once more for the full membership state.

## Full Sequence

### Fast Path (during the free testing period — the vast majority of cases)

```
1.  status                          # environment self-check
2.  (Step 2 conversation to confirm info, password either/or; generated mode: gen-password → have the user save it immediately)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → user checks the code in their inbox (the only time leaving the conversation)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → send the link to the user; one click and they're on the home page
7.  (user confirms they're in) → wrap up directly: cleanup + account card + guide first steps
```

### Payment Path (when the user wants membership, or the free testing period has ended)

```
1–5. Same as the fast path (the state already has the token after register succeeds)
6.  login-link --target pending     # → half-login link, keeps the payment return page working
7.  (user picks a payment method)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <payment page file>       # Windows; macOS uses open, Linux uses xdg-open
    # → the user completes payment/authorization at the Alipay/PayPal cashier (leaves the conversation)
9.  query (every 10–15s) until paid / ACTIVE
10. refresh-login                   # exchange for a new JWT with the ACTIVE claim
11. login-link --target home        # → send the full-membership link to the user
12. whoami                          # confirm subscriptionStatus: ACTIVE (optional)
13. cleanup                         # clear the state file
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | The free testing period has ended and payment hasn't arrived; go back to step 9 to keep polling, or confirm whether the user completed the payment |",
    AF_ERR_SUB="| User clicks the home link but lands on the subscription page | The free testing period has ended → switch to the payment path: `login-link --target pending` → pick a payment method → `create-order` |",
    AF_FALLBACK="After falling back: give the registration page https://global.powpow.online/register (during the free testing period, web registration is equally instant; when a subscription is needed, also give the subscription page https://global.powpow.online/subscription ), troubleshoot alongside per the rules in `registration-flow.md`, keep the same tone, and still end every turn with a \"next step\" block.",
    PA_NOTE="""> **Free testing period (starting 2026-10-18; actual platform behavior prevails)**: during this period a registered account can use every feature directly, and **subscribing is an optional upgrade rather than a requirement** — only follow this file's flow when the user actively wants membership. When the testing period ends, unsubscribed accounts visiting content pages will be redirected to the subscription page; just complete the subscription per this file.""",
    RF_STATE="""## Status Flow After Successful Registration

> **Free testing period (starting 2026-10-18; actual platform behavior prevails)**: a newly registered account can **use every feature directly**
> (feed, map, digital humans, check-ins, etc.) with no payment required; unsubscribed accounts are no longer walled off from content pages. The "pending interception"
> described in this section is the regular state after the testing period ends — when that time comes, actual online behavior prevails.

1. The user is stored with `accountStatus: 'pending'` and **3 initial badges** (register route).
2. The server also plants two HttpOnly cookies: the JWT (can access pages directly) and the pendingUserToken (identity credential for the subscription flow).
3. In the regular state (testing period over / no free period), the registration page detects `pending_payment` → redirects to `/subscription`
   (keeping the `next` return parameter); in agent-assisted mode, `me?token=…&redirect=/subscription` achieves the same effect.
   **During the free testing period this step doesn't trigger** — after registering, go straight to the home page and start using.
4. Payment complete → `accountStatus` becomes `active` (**Alipay activates automatically server-side via notify**;
   PayPal activates via Webhook; WeChat QR code is manually confirmed; Huawei IAP goes through `activate-huawei`).
   See `payment-and-activation.md` for details.

In the regular state, inactive (pending) users calling core APIs (feed, map, digital-human chat, check-ins, etc.) get 403;
shared post links are the exception (kept publicly accessible). During the free testing period this interception is suspended and everything is open.""",
    RF_ROW_403="| Registered successfully but login returns 403 \"请完成订阅以激活账户\" | The account is still pending, and the platform is not in a free testing period (the expected state before payment) | Won't happen during the free testing period; if it does, the testing period has ended — complete the subscription first; if still 403 after payment, an old JWT was used — in script mode run `refresh-login` first to exchange for a new login state |",
    RF_ROW_LAND="| User clicks the login link but lands on the subscription page (instead of the home page) | The free testing period has ended and the platform paywall is back | Follow Step 7 in SKILL.md for the subscription payment flow; after subscribing, run `refresh-login` and then send the home-page link |",
    RD_VER="""**Since v2.0.0 this is agent-assisted mode, and since v2.2.0 it adapts to the platform's free testing period**: the core script `scripts/powpow-register.mjs` is zero-dependency
(Node ≥ 18); the user leaves the conversation only once: to check the verification code in their inbox. During the current free testing period, a registered account can use every feature right away — subscription payment is an optional upgrade; if the testing period ends and the user lands on the subscription page, the flow switches to the payment path automatically. Without Node, or when the user prefers to do it themselves, it automatically falls back to pure guidance mode.""",
    RD_LINK="""3. **One-click login (dual links)**: right after successful registration, a login link lands the user directly on the home page (during the free testing period, one click and it's usable);
   if it lands on the subscription page (testing period over) or the user wants to upgrade, follow the subscription flow — after payment arrives, a fresh login state is exchanged and the full-membership link lands them on the home page
   (via the platform's official `me?token=` bridge, which plants the HttpOnly cookie automatically).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
