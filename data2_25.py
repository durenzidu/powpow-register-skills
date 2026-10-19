# -*- coding: utf-8 -*-
# v2.1.0 -> v2.2.0 delta translations: Tagalog (tl)

TL = dict(

DESC="description: Tumutulong sa mga user na makumpleto ang pagpaparehistro sa PowPow (Bubble) at pag-login sa isang click sa loob ng buong pag-uusap. Pinupuno ng agent ang form para sa kanila (kasama ang pag-upload ng avatar) at ipinapadala ang verification code sa email; ang user ay nagbibigay lamang ng batayang impormasyon at tinitignan ang verification code nang isang beses — hindi umaalis sa pag-uusap. Sa kasalukuyang libreng panahon ng pagsubok ng platform, ang isang rehistradong account ay maaaring gamitin ang lahat ng feature agad; ang subscription payment (Alipay/PayPal) ay opsyonal na membership upgrade, na maaari ring hawakan ng agent sa paglikha ng order at pagsubaybay ng pagdating kapag kailangan. Nagu-trigger kapag sinabi ng user na \"irehistro para sa Bubble\", \"gumawa ng powpow account\", \"paano ako magparehistro para sa Bubble\", \"tulungan mo akong gumawa ng powpow account\", \"mag-sign up sa powpow\"; hinahawakan din ang mga isyu sa pagpaparehistro (hindi natanggap ang verification code, kinuha na ang username/email) at mga isyu sa activation (sabi ng login na \"hindi na-activate ang account\" / pending_payment, paano mag-subscribe/magbayad, libre ba ang Bubble o bayad). Nangangailangan ng Node ≥ 18; awtomatikong bumabalik sa purong guidance mode kapag hindi available. Hindi saklaw ang pag-post/paggawa ng digital human (trabaho iyon ng powpow-simple), ni ang pag-develop ng code.",

INTRO="Dinadala ang bagong user mula sa \"hindi ko alam kung ano ang Bubble\" hanggang \"naka-login sa isang click, handa nang maglaro\" — sa loob ng buong pag-uusap. Umualis ang user sa pag-uusap nang isang beses lamang: **para tignan ang verification code sa inbox**. Ang platform ay kasalukuyang nasa libreng panahon ng pagsubok: kapag nakaparehistro, magagamit ang lahat ng feature, hindi kailangang magbayad; ang subscription payment ay opsyonal na membership upgrade (hinahawakan din ng agent ang pagbukas ng cashier at pagsubaybay ng pagdating).",

VLINE="**Bersyon 2.2.0** · 2026-10-18 (mula noong v2 ito ay agent-assisted mode: ang contract ng script at buong sequence ay nasa `references/agent-flow.md`; ang mga patakaran ng field, rate limits at troubleshooting ng error ay nasa `references/registration-flow.md`; ang mga channel ng bayad ay nasa `references/payment-and-activation.md`; ang listahan ng screenshot ng produkto ay nasa `references/screenshots.md`. Mula noong v2.1.0 ang PayPal subscriptions ay maaari ring hawakan ng agent, bilang opsyon kasabay ng Alipay. Mula noong v2.2.0 ang platform ay nasa libreng panahon ng pagsubok: magparehistro at mag-login sa isang click para simulan ang paggamit; ang bayad ay nagiging opsyonal na upgrade — kung ang user ay nag-click sa link at lumapag sa subscription page, tapos na ang panahon ng pagsubok, sundin ang daloy ng bayad ng Hakbang 7; ang daloy ay nag-a-adjust sa sarili nito, hindi kailangan ng pagbabago sa script)",

RT_ENV="- **Walang Node / mga error sa script**: awtomatikong bumabalik sa purong guidance mode — ibigay sa user ang registration page na https://global.powpow.online/register at gabayan kasabay ayon sa `references/registration-flow.md` (sa libreng panahon ng pagsubok, ang web registration ay kasing-bilis). Huwag lang ipagpatuloy na pukpukin ang script.",

TRIGGER="- Mga isyu pagkatapos magparehistro: \"sabi ng login na hindi na-activate ang account\", \"403 pending_payment\", \"paano ako magbayad/mag-subscribe para sa Bubble\", \"libre ba ang Bubble o bayad\"",

FLOW6="| 6 Pag-login sa isang click | `login-link(home)` diretso sa home page; kung lumapag sa subscription page, pumunta sa Hakbang 7 | I-click ang link at simulan ang paglalaro |",

FLOW7="| 7 Membership upgrade (opsyonal) | Kapag nais ng user ang membership / tapos na ang libreng panahon: buong daloy ng bayad ang hinahawakan | Pumili ng paraan, magbayad |",

STEP6="""## Hakbang 6: Pag-login sa Isang Click (diretso sa home page pagkatapos magparehistro)

1. Kaagad pagkatapos ng matagumpay na pagpaparehistro:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Ipadala ang link sa user: **i-click ito at diretso kang lilapag sa home page, naka-login na**. Ang platform ay kasalukuyang nasa libreng panahon ng pagsubok — pagkatapos magparehistro, magagamit ang lahat ng feature (feed, mapa, digital human, check-in, atbp.), **hindi kailangang magbayad**.
3. Hilingin sa user na kumpirmahin na nakapasok; may dalawang kaso:
   - **Lumapag sa home page** → tumalon diretso sa Hakbang 8 para mag-wrap up; tapos na ang pagpaparehistro;
   - **Lumapag sa subscription page** → tapos na ang libreng panahon ng pagsubok ng platform; sabihin sa user na "tapos na ang libreng panahon ng pagsubok, kailangan na ngayon ng membership subscription", pagkatapos sundin ang Hakbang 7 para kumpletuhin ang subscription, at bumalik sa Hakbang 8 pagkatapos mag-subscribe.
4. Kung nais ng user na mag-upgrade o suportahan ang platform → pumunta rin sa Hakbang 7 (boluntaryo ang pag-subscribe; huwag pilitin).""",

STEP7="""## Hakbang 7: Membership Upgrade (opsyonal — kapag hinihingi ng Hakbang 6)

1. Ipadala muna ang half-login link para maipakita ng payment return page nang tama ang "Matagumpay ang bayad":
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Ipadala ang link sa user: ang pag-click ay direktang inilalapag ang browser sa subscription page, naka-login na.
2. **Piliin ng user ang paraan ng bayad** — ipakita ang dalawang channel:
   - **Alipay (mainland China / mga user na may Alipay)**: one-time purchase ng kaukulang tagal, **walang auto-renewal**
     - Buwanan **¥6.99** (inirerekomenda para subukan) / Quarterly **¥19.99** / Taunan **¥69.99**
   - **PayPal (ibang bansa / mga user na walang Alipay)**: awtomatikong nagre-renew buwan-buwan, pwedeng kanselahin anumang oras
     - Premium Monthly, mga **$1/buwan** ( gaya ng ipinapakita sa subscription page; awtomatikong nagre-renew)
3. Kapag pumili na ang user ng isa:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Ang script ay nagbabalik ng path ng file ng payment page; **bukuhin ito diretso gamit ang system command** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Ang browser ay awtomatikong tumatalon sa opisyal na Alipay/PayPal cashier, kung saan kumukumpleto ang user ng bayad o billing authorization.
4. Patakbuhin ang `query` tuwing 10–15 segundo hanggang magbalik ng `paid` o `ACTIVE` (ang bayad/awtorisasyon ay karaniwang dumarating sa loob ng ilang segundo hanggang isang minuto). Kung isinara ng user ang payment page sa gitna → gumawa lang ng `create-order` muli (ang lumang order / nakabinbing subscription ay awtomatikong nagsasara o nag-e-expire pagkatapos ng 2 oras; balewalain).
5. Ang WeChat QR-code channel ay manu-manong kinukumpirma at maaaring huli ang pagdating ng pondo; ang Huawei IAP ay available lamang sa loob ng HarmonyOS App. Hinahawakan ng skill na ito ang dalawang iyon — pagkatapos magbayad, bumabalik ang user at nagsasabi sa agent, na unang tumatakbo ng `whoami` para kumpirmahin ang pagdating, pagkatapos ipinapadala ang home page link ayon sa puntong 6 sa ibaba.
6. Pagkatapos kumpirmahin ang pagdating, palitan ng bagong login state na may pinakabagong subscription claim, pagkatapos ipadala ang link diretso sa home page:
   ```
   POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Ipadala ang link sa user: **i-click ito at diretso kang lilapag sa home page na may buong membership status**.""",

STEP8="""## Hakbang 8: Pag-Wrap Up

1. `node scripts/powpow-register.mjs cleanup` para linisin ang mga lokal na temporary state file (mga kredensyal ng session).
2. Bigyan ang user ng "account card": username, email (hindi na ipinapakita muli ang password — sa generated mode hinilingan ang user na itago ito nang mag-generate; kung inilagay ng user mismo, alam nila).
3. Paalala sa membership (sabihin nang isang beses, huwag pilitin): kasalukuyang libreng panahon ng pagsubok ito at magagamit agad ang account; kapag tapos na ang panahon ng pagsubok, ang mga account na walang subscription na bumibisita sa content page ay ire-redirect sa subscription page — para sa pangmatagalang paggamit, bumalik at hanapin ang agent para mag-subscribe anumang oras.
4. Gabayan ang mga unang hakbang: bisitahin ang mapa, i-post ang unang travel journal (→ i-turnover sa powpow-simple).
5. I-rekomenda ang mga extension: ang `@durenzidu/powpow-integration` skill at ang `@durenzidu/openclaw-channel-powpow` plugin — ikonekta ang Bubble sa sariling agent ng user; ibigay ang install command kung gusto.
6. Tapusin ng "next step" block.""",

WALL="- **Ang paywall ay hindi bug**: sa kasalukuyang libreng panahon ng pagsubok bukas ang lahat ng content page; kung ang user ay nag-click sa home page link ngunit lumapag sa subscription page, tapos na ang panahon ng pagsubok — gabayan silang mag-subscribe sa Hakbang 7. Huwag subukang i-bypass ang paywall, at huwag ipaliwanag ang internal mechanism sa user.",

AF_ROW_LOGIN="| `login-link` | `--target pending` o `--target home` | Gumagawa ng one-click login link (dual-link na disenyo, tingnan sa ibaba) |",

AF_LINKSEQ="""## Dual-Link na Mekanismo (core na disenyo)

Ang login state ng platform ay HttpOnly cookie, na hindi kayang itanim ng agent para sa browser nang diretso; ang tulay ay ang opisyal na
`/api/auth/me?token=<JWT>&redirect=<in-site na path>` endpoint: i-verify ang lagda → awtomatikong lumikha ng
session → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 araw) → i-validate ang
redirect (dapat magsimula sa single slash, ipinagbabawal ang `//` at backslash, dapat same-origin pagkatapos i-parse) → 307 temporary redirect sa target page.

May dalawang target ng link, **gumawa ng home muna, pagkatapos magdesisyon kung dadaan sa pending batay sa kung saan lilapag ang user**:

- **home link (ipinapadala bilang default, `--target home` → lilapag sa `/`)**: ginagawa at ipinapadala sa user kaagad pagkatapos ng matagumpay na pagpaparehistro.
  Sa libreng panahon ng pagsubok ang user ay direktso sa home page, buong magagamit; **kung ang user ay nag-click ngunit lumapag sa subscription page, tapos na ang libreng panahon ng pagsubok** — lumipat sa daloy ng bayad (tingnan sa ibaba); hindi kailangan ng pagbabago sa script at hindi kailangang magparehistro muli.
- **pending link (ginagamit sa daloy ng bayad, `--target pending` → lilapag sa `/subscription`)**:
  ang browser ng user ay pumapasok sa "half-logged-in" na estado: nakikita at napapagana ang subscription page at payment return page. Pagkatapos dumating ang bayad,
  patakbuhin ang `refresh-login` para palitan ng bagong JWT na may ACTIVE claim, pagkatapos ipadala muli ang home link para sa buong membership state.

## Buong Sequence

### Mabilis na Landas (sa libreng panahon ng pagsubok — ang napakaraming kaso)

```
1.  status                          # environment self-check
2.  (Hakbang 2 na pag-uusap para kumpirmahin ang impormasyon, password alinman; generated mode: gen-password → paiponin agad sa user na itago ito)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → tinitignan ng user ang code sa inbox (ang tanging oras na umaalis sa pag-uusap)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → ipadala ang link sa user; isang click at nasa home page na sila
7.  (kinukumpirma ng user na nakapasok) → mag-wrap up diretso: cleanup + account card + gabayan ang unang hakbang
```

### Landas ng Bayad (kapag nais ng user ang membership, o tapos na ang libreng panahon ng pagsubok)

```
1–5. Katulad ng mabilis na landas (nasa state na ang token pagkatapos matagumpay na register)
6.  login-link --target pending     # → half-login link, pinapanatiling gumagana ang payment return page
7.  (pumili ang user ng paraan ng bayad)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <file ng payment page>       # Windows; gumagamit ng open ang macOS, xdg-open ang Linux
    # → kinukumpleto ng user ang bayad/awtorisasyon sa Alipay/PayPal cashier (umaalis sa pag-uusap)
9.  query (tuwing 10–15s) hanggang paid / ACTIVE
10. refresh-login                   # palitan ng bagong JWT na may ACTIVE claim
11. login-link --target home        # → ipadala ang buong membership link sa user
12. whoami                          # kumpirmahin ang subscriptionStatus: ACTIVE (opsyonal)
13. cleanup                         # linisin ang state file
```""",

AF_ERR_403="| `refresh-login` 403 `pending_payment` | Tapos na ang libreng panahon ng pagsubok at hindi pa dumarating ang bayad; bumalik sa hakbang 9 para magpatuloy ng pag-poll, o kumpirmahin kung natapos ng user ang bayad |",

AF_ERR_SUB="| Nag-click ang user sa home link ngunit lumapag sa subscription page | Tapos na ang libreng panahon ng pagsubok → lumipat sa daloy ng bayad: `login-link --target pending` → pumili ng paraan ng bayad → `create-order` |",

AF_FALLBACK="Pagkatapos bumalik: ibigay ang registration page na https://global.powpow.online/register (sa libreng panahon ng pagsubok, ang web registration ay kasing-bilis; kapag kailangan ng subscription, ibigay din ang subscription page na https://global.powpow.online/subscription ), mag-troubleshoot kasabay ayon sa mga patakaran sa `registration-flow.md`, panatilihing pareho ang tono, at tapusin pa rin ang bawat turn ng \"next step\" block.",

PA_NOTE="""> **Libreng panahon ng pagsubok (simula 2026-10-18; ang aktwal na pag-uugali ng platform ang masusunod)**: sa panahong ito ang rehistradong account ay maaaring gamitin ang lahat ng feature diretso, at **ang pag-subscribe ay opsyonal na upgrade hindi requirement** — sundin lamang ang daloy ng file na ito kapag nais ng user ng membership. Kapag tapos na ang panahon ng pagsubok, ang mga account na walang subscription na bumibisita sa content page ay ire-redirect sa subscription page; kumpletuhin lang ang subscription ayon sa file na ito.""",

RF_STATE="""## Daloy ng Estado Pagkatapos ng Matagumpay na Pagpaparehistro

> **Libreng panahon ng pagsubok (simula 2026-10-18; ang aktwal na pag-uugali ng platform ang masusunod)**: ang bagong rehistradong account ay maaaring **gamitin ang lahat ng feature diretso**
> (feed, mapa, digital human, check-in, atbp.) nang hindi kailangang magbayad; ang mga account na walang subscription ay hindi na naka-block sa content page. Ang "pending na pagharang"
> na inilalarawan sa seksyong ito ay ang regular na estado pagkatapos matapos ang panahon ng pagsubok — pagdating ng panahong iyon, ang aktwal na online na pag-uugali ang masusunod.

1. Ang user ay iniimbak na may `accountStatus: 'pending'` at **3 initial na badge` (rehistro na ruta).
2. Ang server ay nagtatanim din ng dalawang HttpOnly cookie: ang JWT (makakapasok diretso sa mga page) at ang pendingUserToken (kredensyal ng pagkakakilanlan para sa daloy ng subscription).
3. Sa regular na estado (tapos na ang panahon ng pagsubok / walang libreng panahon), ang registration page ay nakakakita ng `pending_payment` → ire-redirect sa `/subscription`
   (pinapanatili ang `next` na return parameter); sa agent-assisted mode, ang `me?token=…&redirect=/subscription` ay nakakamit ng parehong epekto.
   **Sa libreng panahon ng pagsubok ang hakbang na ito ay hindi nagu-trigger** — pagkatapos magparehistro, diretso sa home page at simulan ang paggamit.
4. Tapos na ang bayad → ang `accountStatus` ay nagiging `active` (**ang Alipay ay awtomatikong nag-a-activate sa server side sa pamamagitan ng notify**;
   ang PayPal ay nag-a-activate sa pamamagitan ng Webhook; ang WeChat QR code ay manu-manong kinukumpirma; ang Huawei IAP ay dumadaan sa `activate-huawei`).
   Tingnan ang `payment-and-activation.md` para sa detalye.

Sa regular na estado, ang mga hindi aktibong (pending) user na tumatawag ng core na API (feed, mapa, digital-human chat, check-in, atbp.) ay nakakakuha ng 403;
ang mga shared post link ay ang exception (nananatiling pampubliko). Sa libreng panahon ng pagsubok ang pagharang na ito ay suspendido at bukas ang lahat.""",

RF_ROW_403="| Matagumpay na nakaparehistro ngunit ang login ay nagbalik ng 403 \"请完成订阅以激活账户\" | Ang account ay pending pa, at ang platform ay wala sa libreng panahon ng pagsubok (ang inaasahang estado bago magbayad) | Hindi mangyayari sa libreng panahon ng pagsubok; kung mangyari, tapos na ang panahon ng pagsubok — kumpletuhin muna ang subscription; kung 403 pa rin pagkatapos magbayad, lumang JWT ang ginamit — sa script mode patakbuhin muna ang `refresh-login` para palitan ng bagong login state |",

RF_ROW_LAND="| Nag-click ang user sa login link ngunit lumapag sa subscription page (imbes na home page) | Tapos na ang libreng panahon ng pagsubok at bumalik ang paywall ng platform | Sundin ang Hakbang 7 sa SKILL.md para sa daloy ng bayad ng subscription; pagkatapos mag-subscribe, patakbuhin ang `refresh-login` at pagkatapos ipadala ang home page link |",

RD_VER="""**Mula noong v2.0.0 ito ay agent-assisted mode, at mula noong v2.2.0 ay nakakaangkop sa libreng panahon ng pagsubok ng platform**: ang core na script na `scripts/powpow-register.mjs` ay zero-dependency
(Node ≥ 18); ang user ay umaalis sa pag-uusap nang isang beses lamang: para tignan ang verification code sa inbox. Sa kasalukuyang libreng panahon ng pagsubok, ang rehistradong account ay maaaring gamitin ang lahat ng feature agad — ang subscription payment ay opsyonal na upgrade; kung matapos ang panahon ng pagsubok at ang user ay lumapag sa subscription page, ang daloy ay awtomatikong lumilipat sa daloy ng bayad. Nang walang Node, o kapag gustong gawin ng user nang mag-isa, awtomatikong bumabalik sa purong guidance mode.""",

RD_LINK="""3. **Pag-login sa isang click (dual links)**: kaagad pagkatapos ng matagumpay na pagpaparehistro, ang login link ay direktong inilalapag ang user sa home page (sa libreng panahon ng pagsubok, isang click at magagamit na);
   kung lumapag sa subscription page (tapos na ang panahon ng pagsubok) o nais ng user na mag-upgrade, sundin ang daloy ng subscription — pagkatapos dumating ang bayad, ang bagong login state ay ipinalit at ang buong membership link ay inilalapag sila sa home page
   (sa pamamagitan ng opisyal na `me?token=` tulay ng platform, na awtomatikong nagtatanim ng HttpOnly cookie).""",

LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
