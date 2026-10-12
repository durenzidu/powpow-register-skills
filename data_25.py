# -*- coding: utf-8 -*-
TL = dict(
    DESC=[
        ("pag-activate ng subscription sa Alipay", "pag-activate ng subscription sa Alipay/PayPal"),
        ("nagbabayad sa Alipay cashier", "nagbabayad sa Alipay/PayPal cashier"),
    ],
    INTRO=("**magbayad sa Alipay cashier** (awtomatikong bubuksan ng agent ang cashier page)",
           "**magbayad sa cashier ng bayad** (Alipay o PayPal — awtomatikong bubuksan ng agent ang cashier page)"),
    VLINE=[
        ("**Bersyon 2.0.1** · 2026-10-08", "**Bersyon 2.1.0** · 2026-10-11"),
        ("Mula v2.0.1, ang mga product screenshot ay nakapaketeng kasama ng skill sa `assets/screenshots/`, hindi na umaasa sa external image host",
         "Mula v2.1.0, ang PayPal subscription ay maaari na ring hawakan ng agent, bilang opsyon kasama ng Alipay"),
    ],
    STEP6="""2. **Hayaan ang gumagamit na pumili ng paraan ng bayad**, ipakita ang dalawang channel:
   - **Alipay (mainland / may Alipay na gumagamit)**: one-time purchase para sa kaukulang tagal, **hindi auto-renew**
     - Buwanan **¥6.99** (imungkahing subukan muna) / Tatlong-buwan **¥19.99** / Taunang **¥69.99**
   - **PayPal (ibang bansa / walang Alipay)**: buwanang auto-renew, maaaring kanselahin anumang oras
     - Premium Monthly, humigit-kumulang **$1/buwan** (ayon sa ipinapakitang subscription page, auto-renew)
3. Matapos piliin ng gumagamit:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Nagbabalik ang script ng file path ng payment page, **buksan nang direkta gamit ang system command** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Awtomatikong dadako ang browser sa opisyal na Alipay/PayPal cashier, kung saan magre-scan ang gumagamit ng QR code o mag-log in para magbayad/o mag-authorize ng subscription.
4. Patakbuhin ang `query` kada 10–15 segundo hanggang magbalik ng `paid` o `ACTIVE` (karaniwang ilang segundo hanggang isang minuto ang pagdating ng bayad/authorization). Kung isinara ng gumagamit ang payment page sa gitna → muling patakbuhin lang ang `create-order` (awtomatikong magsasara/expire ang lumang order / PENDING subscription pagkatapos ng 2 oras, huwag intindihin).
5. Ang WeChat QR channel ay may manual na kumpirmasyon at maaaring ma-delay ang pagdating ng bayad; ang Huawei IAP ay available lang sa loob ng HarmonyOS app. Hindi ina-asikaso ng skill ang dalawang ito — pagkatapos magbayad, bumalik pa rin sa Hakbang 7.
""",
    BOUNDARY=("hawakan ang Alipay account/payment credentials ng gumagamit", "hawakan ang Alipay/PayPal account/payment credentials ng gumagamit"),
    PA_CONCL="""**Ang Alipay at PayPal subscription ay parehong kayang hawakan ng agent para sa paggawa ng order at pagsubaybay sa pagdating ng bayad.**
Ang Alipay ay one-time purchase na hindi auto-renew, para sa mainland/may Alipay na gumagamit; ang PayPal ay buwanang auto-renew na maaaring kanselahin anumang oras, para sa ibang bansa/walang Alipay. Ang WeChat QR (manual confirmation) at Huawei IAP ay nananatili, ngunit hindi ina-asikaso ng skill.""",
    PA_RESP=[
        ("hawakan ang Alipay", "hawakan ang Alipay/PayPal"),
        ("Ang pagbabayad ay palaging ginagawa mismo ng gumagamit sa opisyal na Alipay cashier.",
         "Ang pagbabayad ay palaging ginagawa mismo ng gumagamit sa opisyal na cashier."),
    ],
    PA_FRESH=("Kaya ang skill, pagkatapos makumpirma ang `paid`, ay patakbuhin muna ang `refresh-login`",
              "Kaya ang skill, pagkatapos makumpirma ang `paid` / PayPal `ACTIVE`, ay patakbuhin muna ang `refresh-login`"),
    PA_PAYPAL="""## PayPal subscription channel (agent-assisted; web, hindi HarmonyOS)

May iisang Premium Monthly plan lang (humigit-kumulang $1/buwan, ayon sa `/api/subscription/plans`), **buwanang auto-renew**,
maaaring kanselahin ng gumagamit anumang oras sa kanyang PayPal account.

### API contract (naka-encapsulate na sa skill script, hindi direktang nagbubuo ng request ang agent)

| Endpoint | Method | Paglalarawan |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer auth; nagbabalik ng listahan ng available plans (kasalukuyang 1 lang) |
| `/api/subscription/create` | POST | body `{planId}` → nagbabalik ng `{subscriptionId, approveUrl, status}`; karaniwang `APPROVAL_PENDING` ang `status` |
| `/api/subscription/create` | GET | Bearer auth; nagbabalik ng `{activeSubscription, allSubscriptions}`; pine-poll ng agent ang `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | awtomatikong tinatawag ng success page (kasama ang cookie); kapag hindi pa dumating ang webhook, direktang tinatawag ang PayPal API para i-activate |
| `/subscription/success` | Browser return page | landing page pagkatapos ng PayPal authorization; awtomatikong nire-poll ang verify; pagkatapos ay babalik sa home page / orihinal na page |
| `/subscription/cancel` | Browser page | landing page kapag kanselado o nabigo ang gumagamit; maaaring muling simulan |

### Daloy ng agent

```
create-order --provider paypal   # → nagbabalik ng approveUrl, isinusulat sa lokal na HTML file
buksan ang HTML file              # → dadako ang browser sa PayPal authorization page
query (kada 10–15s)               # → poll hanggang ACTIVE
refresh-login                     # → kumuha ng bagong JWT (ACTIVE subscription claim)
login-link --target home          # → gumawa ng opisyal na login link
```

- Ang PENDING subscription na hindi natapos sa loob ng 1 oras ay awtomatikong lilinisin ng backend; simulan lang muli.
- Kung muling patatakbuhin ng gumagamit ang `create-order`, gagamitin muli ng backend ang valid na `APPROVAL_PENDING` subscription, para iwas 409.
- Katulad ng Alipay: ang pagdating ng bayad ay nag-a-update lang sa DB — hindi awtomatikong nare-refresh ang lumang JWT, kaya **kailangang** patakbuhin muna ang `refresh-login` bago gumawa ng home page link.""",
    PA_ROWS="""| PayPal `query` laging PENDING | Hindi pa natatapos ng gumagamit ang authorization sa PayPal; siguraduhing nabuksan ang authorization link sa browser. Kung PENDING pa rin pagkatapos mag-authorize, baka na-delay ang webhook — hayaang maghintay ang gumagamit ng ilang segundo sa success page o i-refresh |
| PayPal `query` nagbabalik ng 409 | May hindi pa natatapos na PENDING PayPal subscription; maghintay ng 1 oras para mag-expire, o tapusin ang lumang authorization sa browser |
| Nakabayad na sa PayPal ngunit hinarang pa rin ang Link 2 | Katulad ng Alipay: muna `refresh-login`, pagkatapos `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (default ng Alipay)<br>`--provider alipay\\|paypal` | Gumawa ng payment order; ibinabalik ng Alipay ang payment page file path + outTradeNo; ibinabalik ng PayPal ang authorization page file path + subscriptionId (awtomatikong nakatala sa state file) |",
    AF_ROW_QUERY="| `query` | —— | Tingnan ang status ng order/subscription. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; poll kada 10–15s |",
    AF_SEQ7="""7.  (Pipiliin ng gumagamit ang paraan ng bayad)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("    # → magbayad ang gumagamit sa Alipay cashier (pag-alis sa usapan ②)",
             "    # → magbabayad/mag-aauthorize ang gumagamit sa Alipay/PayPal cashier (pag-alis sa usapan ②)"),
    AF_SEQ9=("9.  query (kada 10–15s) hanggang paid",
             "9.  query (kada 10–15s) hanggang paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Pagkatapos ng `create-order`, isinara ng gumagamit ang payment page | Muling patakbuhin lang ang `create-order` (awtomatikong magsasara ang lumang order pagkatapos ng 2 oras) |",
                  "| Pagkatapos ng `create-order`, isinara ng gumagamit ang payment page | Muling patakbuhin lang ang `create-order` (awtomatikong magsasara ang lumang order pagkatapos ng 2 oras; ang PayPal PENDING subscription ay mag-e-expire pagkatapos ng 1 oras) |"),
    AF_ERR_409="| `create-order --provider paypal` nagbabalik ng 409 | May hindi pa natatapos na PayPal subscription; maghintay ng 1 oras para mag-expire, o tapusin ang lumang authorization sa browser |",
    AF_ERR_PEND=("| `query` ay laging pending | Maaaring hindi pa nagbayad ang gumagamit; magtanong. Kung talagang nagbayad → sundan ang troubleshooting table ng payment-and-activation.md |",
                 "| `query` ay laging pending / PENDING | Maaaring hindi pa nagbayad ang gumagamit; magtanong. Kung talagang nagbayad → sundan ang troubleshooting table ng payment-and-activation.md |"),
    AF_ERR_403=("Hindi pa dumarating ang bayad, bumalik sa Hakbang 9 at mag-poll muli",
                "Hindi pa dumarating ang bayad/authorization, bumalik sa Hakbang 9 at mag-poll muli"),
    RD=[
        ("Alipay subscription ordering at pagsubaybay sa pagdating ng bayad",
         "Alipay/PayPal subscription ordering at pagsubaybay sa pagdating ng bayad"),
        ("**Mula v2.0.0 ay agent-assisted mode**",
         "**Mula v2.0.0 ay agent-assisted mode, at mula v2.1.0 ang PayPal ay kayang hawakan din**"),
        ("magbayad sa Alipay cashier.", "magbayad sa Alipay/PayPal cashier."),
        ("4. **Subscription payment**: sa Alipay channel, ang agent ang gumagawa ng order (buwanan ¥6.99 / tatlong buwan ¥19.99 / taunan ¥69.99, one-time na bayad na hindi auto-renew) + pagsubaybay sa pagdating ng bayad; para sa mga gumagamit sa ibang bansa, bumabalik sa PayPal; itinuturo ang daan para sa WeChat QR/Huawei IAP.",
         "4. **Subscription payment**: ang Alipay (buwanan ¥6.99 / tatlong buwan ¥19.99 / taunan ¥69.99, one-time na bayad na hindi auto-renew) at PayPal (Premium Monthly, humigit-kumulang $1/buwan, auto-renew, maaaring kanselahin anumang oras) ay parehong hinahawakan ng agent sa paggawa ng order + pagsubaybay sa pagdating ng bayad; para sa mga gumagamit sa ibang bansa, bumabalik sa PayPal; itinuturo ang daan para sa WeChat QR/Huawei IAP."),
        ("huwag kailanman hahawakan ang Alipay account o payment credentials ng gumagamit, huwag kailanman magbabayad para sa kanya. Ang pagbabayad ay palaging nagaganap sa pagitan ng gumagamit at ng opisyal na Alipay cashier.",
         "huwag kailanman hahawakan ang Alipay/PayPal account o payment credentials ng gumagamit, huwag kailanman magbabayad para sa kanya. Ang pagbabayad ay palaging nagaganap sa pagitan ng gumagamit at ng opisyal na cashier."),
    ],
)
