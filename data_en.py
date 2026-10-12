# -*- coding: utf-8 -*-
EN = dict(
    DESC=[
        ("Alipay subscription activation and one-click login",
         "Alipay/PayPal subscription activation and one-click login"),
        ("and pays at the Alipay cashier", "and pays at the Alipay/PayPal cashier"),
    ],
    INTRO=("**to pay at the Alipay cashier** (the agent opens the cashier page for them automatically).",
           "**to pay at the payment cashier** (Alipay or PayPal — the agent opens the cashier page for them automatically)."),
    VLINE=[
        ("**Version 2.0.1** · 2026-10-08", "**Version 2.1.0** · 2026-10-11"),
        ("Since v2.0.1 the screenshots are bundled inside the skill at `assets/screenshots/`, so no external image hosting is needed",
         "Since v2.1.0 PayPal subscriptions can also be handled by the agent, as an option alongside Alipay"),
    ],
    STEP6="""2. **Have the user choose a payment method** — show both channels:
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
5. The WeChat QR-code channel is manually confirmed and funds may arrive late; Huawei IAP is only available inside the HarmonyOS App. The skill doesn't handle those two — once paid, they come back to Step 7 all the same.
""",
    BOUNDARY=("the user's Alipay account/payment credentials",
              "the user's Alipay/PayPal account/payment credentials"),
    PA_CONCL="""**Both Alipay and PayPal subscriptions can now be handled by the agent — order creation and arrival tracking included.**
Alipay is a one-time purchase with no auto-renewal, for mainland-China users and users with Alipay; PayPal auto-renews monthly and can be cancelled anytime,
for overseas users and users without Alipay. WeChat QR code (manual confirmation) and Huawei IAP remain available, but the skill doesn't handle them.""",
    PA_RESP=[
        ("it **never** touches the user's Alipay", "it **never** touches the user's Alipay/PayPal"),
        ("The payment action is always completed by the user in person at the official Alipay cashier.",
         "The payment action is always completed by the user in person at the official cashier."),
    ],
    PA_FRESH=("So after confirming `paid`, the skill first runs `refresh-login`",
              "So after confirming `paid` / PayPal `ACTIVE`, the skill first runs `refresh-login`"),
    PA_PAYPAL="""## PayPal Subscription Channel (handled by the agent; web, non-HarmonyOS)

There is only one plan, Premium Monthly (about $1/month, as returned by `/api/subscription/plans`); it **auto-renews monthly**
and the user can cancel anytime in their PayPal account.

### API Contract (already wrapped by the skill script; the agent never assembles requests directly)

| Endpoint | Method | Notes |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer auth; returns the list of available plans (currently only 1) |
| `/api/subscription/create` | POST | Body `{planId}` → returns `{subscriptionId, approveUrl, status}`; `status` is usually `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Bearer auth; returns `{activeSubscription, allSubscriptions}`; the agent polls `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Called automatically by the success page (with the cookie); activates through the PayPal API directly when the webhook hasn't arrived |
| `/subscription/success` | Browser return page | Landing page after PayPal authorization; polls verify automatically, then returns to the home page / original page |
| `/subscription/cancel` | Browser page | Landing page when the user cancels or it fails; a new attempt can be started |

### Agent Flow

```
create-order --provider paypal   # → returns approveUrl, written into a local HTML file
open the HTML file               # → the browser jumps to the PayPal authorization page
query (every 10–15s)             # → poll until ACTIVE
refresh-login                    # → exchange for a new JWT (subscription claim ACTIVE)
login-link --target home         # → generate the formal login link
```

- PENDING subscriptions that aren't finished within 1 hour are cleaned up automatically by the backend; just start over.
- If the user runs `create-order` again, the backend reuses the still-valid `APPROVAL_PENDING` subscription, avoiding a 409.
- Same as Alipay: arrival only updates the DB — an old JWT is not refreshed automatically, so you **must** run `refresh-login` before sending the home-page link.""",
    PA_ROWS="""| PayPal `query` stays PENDING | The user hasn't finished authorization in PayPal; confirm the authorization link was opened in the browser. If it's still PENDING after authorizing, the webhook may be delayed — have the user wait a few more seconds on the success page or refresh |
| PayPal `query` returns 409 | There is already an unfinished PENDING subscription; wait 1 hour for it to expire, or complete the authorization of the old link in the browser |
| PayPal paid, but Link 2 still gets walled | Same as Alipay: run `refresh-login` first, then `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay default)<br>`--provider alipay\\|paypal` | Creates the payment order; Alipay returns the payment page file path + outTradeNo; PayPal returns the authorization page file path + subscriptionId (recorded into the state file automatically) |",
    AF_ROW_QUERY="| `query` | —— | Checks the order/subscription status. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; poll every 10–15s |",
    AF_SEQ7="""7.  (user picks a payment method)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → user pays at the Alipay cashier (leave-the-conversation moment ②)",
             "# → user completes payment/authorization at the Alipay/PayPal cashier (leave-the-conversation moment ②)"),
    AF_SEQ9=("9.  query (every 10–15s) until paid", "9.  query (every 10–15s) until paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| User closed the payment page after `create-order` | Just `create-order` again (the old order auto-closes after 2h) |",
                  "| User closed the payment page after `create-order` | Just `create-order` again (the old order auto-closes after 2h; PayPal PENDING subscriptions expire after 1h) |"),
    AF_ERR_409="| `create-order --provider paypal` returns 409 | There is already an unfinished PayPal subscription; wait 1h for it to expire, or complete the old authorization in the browser |",
    AF_ERR_PEND=("| `query` stays pending | The user may not have paid; ask. If they really paid → follow the troubleshooting table in payment-and-activation.md |",
                 "| `query` stays pending / PENDING | The user may not have paid; ask. If they really paid → follow the troubleshooting table in payment-and-activation.md |"),
    AF_ERR_403=("Payment hasn't arrived yet; go back to step 9",
                "Payment/authorization hasn't arrived yet; go back to step 9"),
    RD=[
        ("Alipay subscription order creation with arrival tracking",
         "Alipay/PayPal subscription order creation with arrival tracking"),
        ("**Since v2.0.0 this is agent-assisted mode**: the core script",
         "**Since v2.0.0 this is agent-assisted mode, and since v2.1.0 PayPal can be handled too**: the core script"),
        ("at the Alipay cashier. Without Node",
         "at the Alipay/PayPal cashier. Without Node"),
        ("4. **Subscription payment**: the agent handles Alipay order creation (monthly ¥6.99 / quarterly ¥19.99 / yearly ¥69.99,\n   one-time purchase, no auto-renewal) + polls for arrival; overseas users fall back to PayPal; WeChat QR code / Huawei IAP are pointed to.",
         "4. **Subscription payment**: both Alipay (monthly ¥6.99 / quarterly ¥19.99 / yearly ¥69.99,\n   one-time purchase, no auto-renewal) and PayPal (Premium Monthly, about $1/month, auto-renews, cancel anytime) are handled by the agent with order creation + arrival polling; WeChat QR code / Huawei IAP are pointed to."),
        ("it never touches the user's Alipay account\n  or payment credentials, and never pays on their behalf. Payment always happens between the user and the official Alipay cashier.",
         "it never touches the user's Alipay/PayPal account\n  or payment credentials, and never pays on their behalf. Payment always happens between the user and the official cashier."),
    ],
)
