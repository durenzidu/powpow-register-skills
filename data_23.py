# -*- coding: utf-8 -*-
PCM = dict(
    DESC=[
        ("Alipay subscription activation", "Alipay/PayPal subscription activation"),
        ("pay for Alipay cashier", "pay for Alipay/PayPal cashier"),
    ],
    INTRO=("**pay for Alipay cashier** (agent go open di cashier page by imsef)",
           "**pay for di payment cashier** (Alipay or PayPal — agent go open di cashier page by imsef)"),
    VLINE=[
        ("**Version 2.0.1** · 2026-10-08", "**Version 2.1.0** · 2026-10-11"),
        ("From v2.0.1 di product screenshots dey pack inside di skill for `assets/screenshots/`, e no dey depend on external image host again",
         "From v2.1.0 PayPal subscription fit also dey handle by di agent, as option side by side with Alipay"),
    ],
    STEP6="""2. **Make di user choose one payment method** — show both channel dem:
   - **Alipay (mainland China / users wey get Alipay)**: buy once for di corresponding time, **e no dey auto-renew**
     - Monthly **¥6.99** (recommend make e try am first) / Quarterly **¥19.99** / Yearly **¥69.99**
   - **PayPal (overseas / users wey no get Alipay)**: e dey auto-renew every month, cancel any time
     - Premium Monthly, about **$1/month** (as e dey show for di subscription page; e dey auto-renew)
3. After di user don choose one:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Di script go return di payment page file path; **open am direct with system command** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Di browser go jump to di official Alipay/PayPal cashier by imsef, where di user go complete di payment or di billing authorization.
4. Run `query` every 10–15 seconds until e return `paid` or `ACTIVE` (payment/authorization dey land normally from few seconds to one minute). If di user close di payment page for middle → just run `create-order` again (old order / pending subscription go close or expire by imsef after 2 hours; no mind dem).
5. Di WeChat scan-code channel na manual confirm, money fit land late; Huawei IAP dey available only inside di HarmonyOS App. Di skill no dey handle dis two — after payment, dem go come back to Step 7 same way.
""",
    BOUNDARY=("user Alipay account/payment credential", "user Alipay/PayPal account/payment credential"),
    PA_CONCL="""**Both Alipay and PayPal subscription fit now dey handle by di agent — order creation and money-landing tracking included.**
Alipay na one-time buy with no auto-renew, for mainland-China users and users wey get Alipay; PayPal dey auto-renew monthly and fit cancel any time, for overseas users and users wey no get Alipay. WeChat scan code (manual confirm) and Huawei IAP still dey available, but di skill no dey handle dem.""",
    PA_RESP=[
        ("**never** touch di user Alipay account/payment credential", "**never** touch di user Alipay/PayPal account/payment credential"),
        ("Di payment action always na di user imsef go do am for di Alipay official cashier.",
         "Di payment action always na di user imsef go do am for di official cashier."),
    ],
    PA_FRESH=("di skill after e confirm `paid` first run `refresh-login`",
              "di skill after e confirm `paid` / PayPal `ACTIVE` first run `refresh-login`"),
    PA_PAYPAL="""## PayPal Subscription Channel (agent dey handle am; web, no be HarmonyOS)

Na only one plan dey, Premium Monthly (about $1/month, as `GET /api/subscription/plans` go return am); it **dey auto-renew every month**
and di user fit cancel any time for im PayPal account.

### API Contract (di skill script done wrap am already; di agent no dey assemble request direct)

| Endpoint | Method | Notes |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer auth; e return di list of available plans (right now na only 1) |
| `/api/subscription/create` | POST | Body `{planId}` → e return `{subscriptionId, approveUrl, status}`; `status` most times na `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Bearer auth; e return `{activeSubscription, allSubscriptions}`; di agent dey poll `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Di success page dey call am automatic (with di cookie); e activate direct through PayPal API when di webhook never reach |
| `/subscription/success` | Browser return page | Landing page after PayPal authorization; e dey poll verify automatic, then e go return to home page / original page |
| `/subscription/cancel` | Browser page | Landing page when di user cancel or e fail; new attempt fit start |

### Agent Flow

```
create-order --provider paypal   # → e return approveUrl, dem write am into local HTML file
open di HTML file                # → di browser go jump to PayPal authorization page
query (every 10–15s)             # → poll until ACTIVE
refresh-login                    # → exchange for new JWT (subscription claim ACTIVE)
login-link --target home         # → generate di formal login link
```

- PENDING subscriptions wey dem no finish within 1 hour, di backend go clean dem automatically; just start over.
- If di user run `create-order` again, di backend go reuse di still-valid `APPROVAL_PENDING` subscription, e avoid 409.
- Same as Alipay: arrival only update di DB — old JWT no dey refresh automatic, so you **must** run `refresh-login` before you send di home-page link.""",
    PA_ROWS="""| PayPal `query` stay PENDING | Di user never finish authorization for PayPal; confirm say di authorization link open for browser. If e still dey PENDING after authorization, di webhook fit delay — make di user wait some seconds for di success page or refresh |
| PayPal `query` return 409 | Dem get unfinished PENDING subscription already; wait 1 hour for am to expire, or complete di old authorization for browser |
| PayPal pay finish but Link 2 still get wall | Same as Alipay: first run `refresh-login`, then `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay default)<br>`--provider alipay\\|paypal` | Create di payment order; Alipay return di payment page file path + outTradeNo; PayPal return di authorization page file path + subscriptionId (e dey write into di state file automatic) |",
    AF_ROW_QUERY="| `query` | —— | Check di order/subscription status. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; poll every 10–15s |",
    AF_SEQ7="""7.  (di user choose payment method)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → di user pay for Alipay cashier (comot from chat part ②)",
             "# → di user complete payment/authorization for Alipay/PayPal cashier (comot from chat part ②)"),
    AF_SEQ9=("9.  query (every 10–15s) until paid", "9.  query (every 10–15s) until paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| After `create-order` di user close di payment page | Just run `create-order` again (old order go close automatic after 2h) |",
                  "| After `create-order` di user close di payment page | Just run `create-order` again (old order go close automatic after 2h; PayPal PENDING subscription expire after 1h) |"),
    AF_ERR_409="| `create-order --provider paypal` returns 409 | There is already an unfinished PayPal subscription; wait 1h for it to expire, or complete the old authorization in the browser |",
    AF_ERR_PEND=("| `query` dey pending anyhow | Di user fit be say e no pay yet; ask am one question. If e truly pay → follow di troubleshooting table for payment-and-activation.md |",
                 "| `query` dey pending anyhow / PENDING | Di user fit be say e no pay yet; ask am one question. If e truly pay → follow di troubleshooting table for payment-and-activation.md |"),
    AF_ERR_403=("Payment no land yet, go back to Step 9", "Payment/authorization no land yet, go back to Step 9"),
    RD=[
        ("Alipay subscription order and money-landing tracking", "Alipay/PayPal subscription order and money-landing tracking"),
        ("**From v2.0.0 na agent-do-am mode**: di main script", "**From v2.0.0 na agent-do-am mode, and from v2.1.0 PayPal fit also dey handle**: di main script"),
        ("pay for di Alipay cashier", "pay for di Alipay/PayPal cashier"),
        ("4. **Subscription payment**: Alipay channel, agent go create order (monthly ¥6.99 / quarterly ¥19.99 / yearly ¥69.99, one-time buy no auto-renew) + poll money landing; overseas users fall back to PayPal; WeChat scan code/Huawei IAP just point di way.",
         "4. **Subscription payment**: both Alipay (monthly ¥6.99 / quarterly ¥19.99 / yearly ¥69.99, one-time buy no auto-renew) and PayPal (Premium Monthly, about $1/month, auto-renew, cancel anytime) na di agent go create order + poll money landing; overseas users fall back to PayPal; WeChat scan code/Huawei IAP just point di way."),
        ("never touch di user Alipay account or payment credential, never pay for am. Payment always happen between di user and di Alipay official cashier.",
         "never touch di user Alipay/PayPal account or payment credential, never pay for am. Payment always happen between di user and di official cashier."),
    ],
)
