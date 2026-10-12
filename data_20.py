# -*- coding: utf-8 -*-
HA = dict(
    DESC=[
        ("kunna membanci ta hanyar Alipay", "kunna membanci ta hanyar Alipay/PayPal"),
        ("yana biya a cashier na Alipay", "yana biya a cashier na Alipay/PayPal"),
    ],
    INTRO=("**biya a cashier na Alipay** (agent za ta buɗe shafin cashier da kai).",
           "**biya a cashier na biya** (Alipay ko PayPal — agent za ta buɗe shafin cashier da kai)."),
    VLINE=[
        ("**Sigar 2.0.1** · 2026-10-08", "**Sigar 2.1.0** · 2026-10-11"),
        ("Tun daga v2.0.1 hotunan samfur an haɗe su tare da skill a cikin `assets/screenshots/`, ba sa dogara ga mashigar hoto ta waje)",
         "Tun daga v2.1.0 membanci ta PayPal ma agent za ta iya kula da ita, a matsayin zaɓi tare da Alipay)"),
    ],
    STEP6="""2. **Ka bar mai amfani ya zaɓi hanyar biya** — ka nuna hanyoyi biyu:
   - **Alipay (cikin China / masu amfani da ke da Alipay)**: saya sau ɗaya na lokacin da ya dace, **ba ya sabunta kansa da kai**
     - Na wata **¥6.99** (an ba da shawarar a fara gwada) / Na kwata **¥19.99** / Na shekara **¥69.99**
   - **PayPal (ƙasashen waje / waɗanda ba su da Alipay)**: yana sabunta kansa kowace wata, ana iya soke shi kowane lokaci
     - Premium Monthly, kusan **$1/wata** (kamar yadda shafin membanci ya nuna; yana sabunta kansa)
3. Mai amfani ya zaɓi ɗaya:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Script ɗin yana dawo da hanyar fayil ɗin shafin biya, **ka buɗe ta da umarnin tsarin kai tsaye** (Windows: `start <fayil>`; macOS: `open <fayil>`; Linux: `xdg-open <fayil>`). Burauza za ta koma kai tsaye ga cashier na Alipay/PayPal na hukuma, mai amfani ya kammala biya ko izinin biya.
4. A kowace daƙiƙa 10–15 ka gudanar da `query` har sai ta dawo da `paid` ko `ACTIVE` (kuɗin/izinin yawanci yana shiga a cikin daƙiƙa kaɗan zuwa minti ɗaya). Mai amfani ya rufe shafin biya a tsakanin → ka sake `create-order` kai tsaye (tsoffin oda / membancin da ke jiran an rufe su ko sun ƙare bayan sa'o'i 2, ka yi watsi da su).
5. Hanyar siffanta lambar QR ta WeChat tabbatarwa ce ta hannu, kuɗin na iya yin jinkiri; Huawei IAP yana samuwa ne kawai cikin app na HarmonyOS. Skill ba ta kula da waɗannan biyun — bayan biya a dawo a mataki na 7 kamar yadda yake.
""",
    BOUNDARY=("asusun Alipay na mai amfani/takaddun biya",
              "asusun Alipay/PayPal na mai amfani/takaddun biya"),
    PA_CONCL="""**Hanyoyin Alipay da PayPal duka yanzu agent za ta iya kula da su — ƙirƙirar oda da bin diddigin shigar kuɗi sun haɗa.**
Alipay biya sau ɗaya ne ba ya sabunta kansa, ga masu amfani na China da waɗanda ke da Alipay; PayPal na sabunta kansa kowace wata kuma ana iya soke shi kowane lokaci,
ga mai amfani na ƙasashen waje da waɗanda ba su da Alipay. Siffanta lambar QR ta WeChat (tabbatarwa ta hannu) da Huawei IAP har yanzu suna nan, amma skill ba ta aikatawa ba.""",
    PA_RESP=[
        ("asusun Alipay na mai amfani/takaddun biya",
         "asusun Alipay/PayPal na mai amfani/takaddun biya"),
        ("Aikin biya koyaushe mai amfani da kansa yana yi a cashier na Alipay na hukuma.",
         "Aikin biya koyaushe mai amfani da kansa yana yi a cashier na hukuma."),
    ],
    PA_FRESH=("bayan tabbatar da `paid` da farko na gudanar da `refresh-login`",
              "bayan tabbatar da `paid` / PayPal `ACTIVE` da farko na gudanar da `refresh-login`"),
    PA_PAYPAL="""## Hanyar membanci ta PayPal (agent tana kula da ita; yanar gizo, ba HarmonyOS ba)

Shiri ɗaya ne kawai, Premium Monthly (kusan $1/wata, kamar yadda `/api/subscription/plans` ya dawo); **yana sabunta kansa kowace wata**
kuma mai amfani na iya soke shi kowane lokaci a cikin asusun PayPal ɗinsa.

### Kwangilar API (an riga an naɗe ta a cikin script ɗin skill; agent kada ta haɗa buƙatu da kanta)

| Ƙarshen hanya | Hanya | Bayani |
|---|---|---|
| `/api/subscription/plans` | GET | Tabbatar da Bearer; yana dawo da jerin shirye-shirye da ake da su (yanzu 1 kawai) |
| `/api/subscription/create` | POST | Jiki `{planId}` → yana dawo da `{subscriptionId, approveUrl, status}`; `status` yawanci `APPROVAL_PENDING` ne |
| `/api/subscription/create` | GET | Tabbatar da Bearer; yana dawo da `{activeSubscription, allSubscriptions}`; agent na duba `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Shafin nasara na kira shi da kai (tare da cookie); yana kunnawa ta API na PayPal kai tsaye idan webhook bai iso ba |
| `/subscription/success` | Shafin dawowar burauza | Shafin sauka bayan izinin PayPal; yana duba verify da kai, sannan ya koma shafin gida / shafin asali |
| `/subscription/cancel` | Shafin burauza | Shafin sauka idan mai amfani ya soke ko ya gaza; ana iya fara sabon yunƙuri |

### Tsarin agent

```
create-order --provider paypal   # → yana dawo da approveUrl, an rubuta shi cikin fayil HTML na gida
open the HTML file               # → burauza ta koma shafin izinin PayPal
query (kowace daƙiƙa 10–15)      # → duba har sai ACTIVE
refresh-login                    # → musanya JWT sabuwa (da'awar membanci ACTIVE)
login-link --target home         # → ƙirƙiri mahaɗin shiga na hukuma
```

- Membancin PENDING da ba a kammala shi cikin sa'a 1 ba, ɓangaren baya na share shi da kai; ka sake farawa.
- Idan mai amfani ya sake gudanar da `create-order`, ɓangaren baya na sake amfani da membancin `APPROVAL_PENDING` da ke nan daram, yana guje wa 409.
- Kamar Alipay: shigar kuɗi yana sabunta DB ne kawai — tsohon JWT ba ya sabunta da kai, saboda haka **dole** ka gudanar da `refresh-login` kafin ka aika mahaɗin shafin gida.""",
    PA_ROWS="""| PayPal `query` ya ci gaba da PENDING | Mai amfani bai kammala izini a PayPal ba; ka tabbatar an buɗe mahaɗin izini a burauza. Idan har yanzu PENDING bayan izini, webhook na iya yin jinkiri — ka bar mai amfani ya jira ƴan daƙiƙu a shafin nasara ko ya sabunta |
| PayPal `query` ya dawo da 409 | Akwai membancin PENDING da ba a kammala ba; ka jira sa'a 1 ya ƙare, ko ka kammala izinin tsohon mahaɗi a burauza |
| An biya ta PayPal, amma mahaɗi na 2 har yanzu ana toshi | Kamar Alipay: ka fara `refresh-login` sannan `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (tsoho na Alipay)<br>`--provider alipay\\|paypal` | Ƙirƙiri oda biya; Alipay yana dawo da hanyar fayil ɗin shafin biya + outTradeNo; PayPal yana dawo da hanyar fayil ɗin shafin izini + subscriptionId (ana adanawa cikin fayil ɗin hali ta kai) |",
    AF_ROW_QUERY="| `query` | —— | Duba halin oda/membanci. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; sake duba kowace daƙiƙa 10–15 |",
    AF_SEQ7="""7.  (Mai amfani ya zaɓi hanyar biya)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("    # → mai amfani ya biya a cashier na Alipay (matakin barin tattaunawa na ②)",
             "    # → mai amfani ya kammala biya/izini a cashier na Alipay/PayPal (matakin barin tattaunawa na ②)"),
    AF_SEQ9=("9.  query (kowace daƙiƙa 10–15) har sai paid",
             "9.  query (kowace daƙiƙa 10–15) har sai paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Bayan `create-order` mai amfani ya rufe shafin biya | Ka sake `create-order` kai tsaye (tsohon oda yana rufewa da kai bayan sa'o'i 2) |",
                  "| Bayan `create-order` mai amfani ya rufe shafin biya | Ka sake `create-order` kai tsaye (tsohon oda yana rufewa da kai bayan sa'o'i 2; membancin PayPal PENDING yana ƙarewa bayan sa'a 1) |"),
    AF_ERR_409="| `create-order --provider paypal` ya dawo da 409 | Akwai membancin PayPal da ba a kammala ba; ka jira sa'a 1 ya ƙare, ko ka kammala tsohon izini a burauza |",
    AF_ERR_PEND=("| `query` na ci gaba da pending | Mai amfani mai yiwuwa ba ya biya; ka tambaya. Hakika ya biya → ka bi teburin bincike na payment-and-activation.md |",
                 "| `query` na ci gaba da pending / PENDING | Mai amfani mai yiwuwa ba ya biya; ka tambaya. Hakika ya biya → ka bi teburin bincike na payment-and-activation.md |"),
    AF_ERR_403=("Kuɗin ba shiga tukuna ba,", "Kuɗin/izinin ba shiga tukuna ba,"),
    RD=[
        ("oda membanci ta Alipay da bin diddigin shigar kuɗi",
         "oda membanci ta Alipay/PayPal da bin diddigin shigar kuɗi"),
        ("**Tun daga v2.0.0 yanayin agent-yana-taimakawa ne**",
         "**Tun daga v2.0.0 yanayin agent-yana-taimakawa ne, kuma tun daga v2.1.0 PayPal ma za a iya kula da ita**"),
        ("a cashier na Alipay biya. Idan ba a sami Node",
         "a cashier na Alipay/PayPal biya. Idan ba a sami Node"),
        ("4. **Membanci da biya**: hanyar Alipay agent tana taimakawa ƙirƙirar oda (wata ¥6.99 / kwata ¥19.99 / shekara ¥69.99, biya sau ɗaya ba ya sabunta kansa) + bin diddigin shigar kuɗi; mai amfani na waje ya koma PayPal; nuna hanyar siffanta lambar QR ta WeChat / Huawei IAP.",
         "4. **Membanci da biya**: Alipay (wata ¥6.99 / kwata ¥19.99 / shekara ¥69.99, biya sau ɗaya ba ya sabunta kansa) da PayPal (Premium Monthly, kusan $1/wata, yana sabunta kansa, ana iya soke shi kowane lokaci) duka agent tana taimakawa ƙirƙirar oda + bin diddigin shigar kuɗi; nuna hanyar siffanta lambar QR ta WeChat / Huawei IAP."),
        ("kada ta taba asusun Alipay na mai amfani ko takaddun biya, kada ta biya a madadinsa. Biya koyaushe yana faruwa tsakanin mai amfani da cashier na Alipay na hukuma.",
         "kada ta taba asusun Alipay/PayPal na mai amfani ko takaddun biya, kada ta biya a madadinsa. Biya koyaushe yana faruwa tsakanin mai amfani da cashier na hukuma."),
    ],
)
