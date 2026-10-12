# -*- coding: utf-8 -*-
SW = dict(
    DESC=[
        ("uwezeshaji wa usajili kupitia Alipay", "uwezeshaji wa usajili kupitia Alipay/PayPal"),
        ("na kulipa kwenye cashier ya Alipay, bila kuondoka mazungumzoni", "na kulipa kwenye cashier ya Alipay/PayPal, bila kuondoka mazungumzoni"),
    ],
    INTRO=("**kulipa kwenye cashier ya Alipay** (agent itafungua ukurasa wa cashier kiotomatiki)",
           "**kulipa kwenye cashier ya malipo** (Alipay au PayPal — agent itafungua ukurasa wa cashier kiotomatiki)"),
    VLINE=[
        ("**Toleo 2.0.1** · 2026-10-08", "**Toleo 2.1.0** · 2026-10-11"),
        ("Tangu v2.0.1 picha za bidhaa zimefungwa pamoja na skill katika `assets/screenshots/`, hazitegemei tena hifadhi ya picha ya nje",
         "Tangu v2.1.0 usajili wa PayPal pia unaweza kushughulikiwa na agent, kama chaguo kando ya Alipay"),
    ],
    STEP6="""2. **Mfanye mtumiaji achague njia ya malipo** — onyesha njia zote mbili:
   - **Alipay (China bara / watumiaji wenye Alipay)**: ununuzi wa mara moja wa muda unaolingana, **hakuna ushamiri otomatiki**
     - Mwezi **¥6.99** (inashauriwa kujaribu kwanza) / Robo mwaka **¥19.99** / Mwaka **¥69.99**
   - **PayPal (nje / watumiaji wasio na Alipay)**: inashamiri otomatiki kila mwezi, batilisha wakati wowote
     - Premium Monthly, takriban **$1/mwezi** (kama inavyooneshwa kwenye ukurasa wa usajili; inashamiri otomatiki)
3. Mtumiaji amepochagua:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Hati inarudisha njia ya faili ya ukurasa wa malipo; **ifungue moja kwa moja kwa amri ya mfumo** (Windows: `start <faili>`; macOS: `open <faili>`; Linux: `xdg-open <faili>`). Kivinjari kitaelekea moja kwa moja kwenye cashier rasmi ya Alipay/PayPal, ambapo mtumiaji anamiliki malipo au uidhinishaji wa bili.
4. Endesha `query` kila sekunde 10–15 hadi irudishe `paid` au `ACTIVE` (malipo/uidhinishaji kwa kawaida hufika ndani ya sekunde chache hadi dakika moja). Mtumiaji akifunga ukurasa wa malipo katikati → endesha tu tena `create-order` (agizo la zamani / usajili wa PENDING hufungwa au mwisho baada ya saa 2; usijali).
5. Njia ya usome msimbo wa WeChat ni ya uthibitisho wa mtu na pesa zinaweza kuchelewa; Huawei IAP inapatikana tu ndani ya App ya HarmonyOS. Skill haishughuliki hizo mbili — baada ya malipo, hurudi kwenye Hatua ya 7 kwa namna hiyo hiyo.
""",
    BOUNDARY=("akaunti ya Alipay ya mtumiaji / kitambulisho cha malipo", "akaunti ya Alipay/PayPal ya mtumiaji / kitambulisho cha malipo"),
    PA_CONCL="""**Sasa njia zote mbili za Alipay na PayPal zinaweza kushughulikiwa na agent — kuunda agizo na kufuatilia ufikiaji wa malipo.**
Alipay ni ununuzi wa mara moja bila ushamiri otomatiki, kwa watumiaji wa China bara na watumiaji wenye Alipay; PayPal inashamiri otomatiki kila mwezi na inaweza kubatilishwa wakati wowote, kwa watumiaji wa nje na watumiaji wasio na Alipay. Usome msimbo wa WeChat (uthibitisho wa mtu) na Huawei IAP bado zipo, lakini hazimsimamiwi na skill.""",
    PA_RESP=[
        ("**kamwe** haigusi akaunti ya Alipay ya mtumiaji / kitambulisho cha malipo", "**kamwe** haigusi akaunti ya Alipay/PayPal ya mtumiaji / kitambulisho cha malipo"),
        ("Kitendo cha kulipa kila wakati kinafanywa na mtumiaji mwenyewe kwenye cashier rasmi ya Alipay.",
         "Kitendo cha kulipa kila wakati kinafanywa na mtumiaji mwenyewe kwenye cashier rasmi."),
    ],
    PA_FRESH=("Kwa hiyo skill baada ya kuthibitisha `paid` kwanza inaendesha `refresh-login`",
              "Kwa hiyo skill baada ya kuthibitisha `paid` / PayPal `ACTIVE` kwanza inaendesha `refresh-login`"),
    PA_PAYPAL="""## Njia ya Usajili wa PayPal (inashughulikiwa na agent; wavuti, sio HarmonyOS)

Kuna mpango mmoja tu, Premium Monthly (takriban $1/mwezi, kama inavyorudishwa na `GET /api/subscription/plans`); **inashamiri otomatiki kila mwezi**
na mtumiaji anaweza kubatilisha wakati wowote katika akaunti yake ya PayPal.

### Mkataba wa API (umeshikwa tayari na hati ya skill; agent haijengi maombi moja kwa moja)

| Endpoint | Method | Maelezo |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer auth; inarudisha orodha ya mipango inayopatikana (kwa sasa 1 tu) |
| `/api/subscription/create` | POST | Mwili `{planId}` → inarudisha `{subscriptionId, approveUrl, status}`; `status` kwa kawaida ni `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Bearer auth; inarudisha `{activeSubscription, allSubscriptions}`; agent hupima `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Ukurasa wa mafanikio unaita kiotomatiki (kwa cookie); inawezesha moja kwa moja kupitia API ya PayPal wakati webhook haijafika |
| `/subscription/success` | Ukurasa wa kurudi wa kivinjari | Ukurasa wa kutua baada ya uidhinishaji wa PayPal; hupima verify kiotomatiki, kisha inarudi kwenye ukurasa wa nyumbani / ukurasa wa awali |
| `/subscription/cancel` | Ukurasa wa kivinjari | Ukurasa wa kutua mtumiaji anapobatilisha au itashindwa; jaribio jipya linaweza kuanza |

### Mtiririko wa Agent

```
create-order --provider paypal   # → inarudisha approveUrl, huandikwa kwenye faili ya HTML ya ndani
open faili ya HTML               # → kivinjari kinaelekea ukurasa wa uidhinishaji wa PayPal
query (kila sekunde 10–15)        # → pima hadi ACTIVE
refresh-login                    # → badilisha JWT mpya (madai ya usajili ACTIVE)
login-link --target home         # → tengeneza kiungo rasmi cha kuingia
```

- Usajili wa PENDING ambao haujamalizika ndani ya saa 1, hufutwa kiotomatiki na backend; anza tu tena.
- Ikiwa mtumiaji anaendesha `create-order` tena, backend hutumia tena usajili uliopo wa `APPROVAL_PENDING`, huzuia 409.
- Sawa na Alipay: ufikiaji huwashesha tu DB — JWT ya zamani haibadilishwi kiotomatiki, kwa hiyo **lazima** uendeshe `refresh-login` kabla ya kutuma kiungo cha ukurasa wa nyumbani.""",
    PA_ROWS="""| PayPal `query` inabaki PENDING | Mtumiaji labda hajakamilisha uidhinishaji kwenye PayPal; hakikisha kiungo cha uidhinishaji kimefunguliwa kwenye kivinjari. Ikiwa bado ni PENDING baada ya uidhinishaji, webhook inaweza kuchelewa — mwongo mtumiaji asubiri sekunde chache kwenye ukurasa wa mafanikio au arekebishe |
| PayPal `query` inarudisha 409 | Tayari kuna usajili wa PayPal usio malizika; subiri saa 1 upite, au kamilisha uidhinishaji wa zamani kwenye kivinjari |
| PayPal imeilipa lakini Link 2 bado inazuiliwa | Sawa na Alipay: kwanza `refresh-login`, kisha `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (chaguomsingi Alipay)<br>`--provider alipay\\|paypal` | Unda agizo la malipo; Alipay inarudisha njia ya faili ya ukurasa wa malipo + outTradeNo; PayPal inarudisha njia ya faili ya ukurasa wa uidhinishaji + subscriptionId (huhifadhiwa kiotomatiki kwenye faili ya hali) |",
    AF_ROW_QUERY="| `query` | —— | Angalia hali ya agizo/usajili. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; hoji kila sekunde 10–15 |",
    AF_SEQ7="""7.  (Mtumiaji achagua njia ya malipo)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → mtumiaji alipe kwenye cashier ya Alipay (sehemu ya kuondoka mazungumzoni②)",
             "# → mtumiaji alipe/uidhinishe kwenye cashier ya Alipay/PayPal (sehemu ya kuondoka mazungumzoni②)"),
    AF_SEQ9=("9.  query (kila sekunde 10–15) hadi paid", "9.  query (kila sekunde 10–15) hadi paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Baada ya `create-order` mtumiaji amefunga ukurasa wa malipo | Endesha tu tena `create-order` (agizo la zamani hufungwa kiotomatiki baada ya saa 2) |",
                  "| Baada ya `create-order` mtumiaji amefunga ukurasa wa malipo | Endesha tu tena `create-order` (agizo la zamani hufungwa kiotomatiki baada ya saa 2; usajili wa PENDING wa PayPal hufungwa baada ya saa 1) |"),
    AF_ERR_409="| `create-order --provider paypal` inarudisha 409 | Tayari kuna usajili wa PayPal usio malizika; subiri saa 1 upite, au maliza uidhinishaji wa zamani kwenye kivinjari |",
    AF_ERR_PEND=("| `query` inabaki pending | Labda mtumiaji hajali; uliza. Amekweli kulipa → fuata jedwali la utatuzi wa payment-and-activation.md |",
                 "| `query` inabaki pending / PENDING | Labda mtumiaji hajali; uliza. Amekweli kulipa → fuata jedwali la utatuzi wa payment-and-activation.md |"),
    AF_ERR_403=("Malipo bado hayajafika, rudi Hatua ya 9", "Malipo/uidhinishaji bado hayajafika, rudi Hatua ya 9"),
    RD=[
        ("agizo la usajili wa Alipay na ufuatiliaji wa malipo", "agizo la usajili wa Alipay/PayPal na ufuatiliaji wa malipo"),
        ("agent-kusaidia**: hati kuu `scripts/powpow-register.mjs` haina tegemezi (Node >= 18)", "agent-kusaidia, na tangu v2.1.0 PayPal pia inaweza kushughulikiwa**: hati kuu `scripts/powpow-register.mjs` haina tegemezi (Node >= 18)"),
        ("kwenye cashier ya Alipay kulipa", "kwenye cashier ya Alipay/PayPal kulipa"),
        ("4. **Usajili wa malipo**: njia ya Alipay agent inasaidia kuunda agizo (mwezi ¥6.99 / robo mwaka ¥19.99 / mwaka ¥69.99, ununuzi wa mara moja hauna ushamiri otomatiki) + ufuatiliaji wa malipo; mtumiaji wa nje anarudi PayPal; mwongozo wa usome msimbo wa WeChat / Huawei IAP.",
         "4. **Usajili wa malipo**: njia zote mbili za Alipay (mwezi ¥6.99 / robo mwaka ¥19.99 / mwaka ¥69.99, ununuzi wa mara moja hauna ushamiri otomatiki) na PayPal (Premium Monthly, takriban $1/mwezi, inashamiri otomatiki, batilisha wakati wowote) zinashughulikiwa na agent kwa kuunda agizo + ufuatiliaji wa malipo; mtumiaji wa nje anarudi PayPal; mwongozo wa usome msimbo wa WeChat / Huawei IAP."),
        ("kamwe haigusi akaunti ya Alipay ya mtumiaji au kitambulisho cha malipo, kamwe hailipi badala yake. Malipo yanafanyika kila wakati kati ya mtumiaji na cashier rasmi ya Alipay.",
         "kamwe haigusi akaunti ya Alipay/PayPal ya mtumiaji au kitambulisho cha malipo, kamwe hailipi badala yake. Malipo yanafanyika kila wakati kati ya mtumiaji na cashier rasmi."),
    ],
)
