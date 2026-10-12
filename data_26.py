# -*- coding: utf-8 -*-
YO = dict(
    DESC=[
        ("imuyipada ṣiṣẹ ti Alipay", "imuyipada ṣiṣẹ ti Alipay/PayPal"),
        ("sanwo ni alagbata Alipay", "sanwo ni alagbata Alipay/PayPal"),
    ],
    INTRO=("**sanwo ni alagbata Alipay** (agent yoo ṣii oju-iwe alagbata naa laifọwọyi)",
           "**sanwo ni alagbata isanwo** (Alipay tabi PayPal — agent yoo ṣii oju-iwe alagbata naa laifọwọyi)"),
    VLINE=[
        ("**Ẹ̀dà 2.0.1** · 2026-10-08", "**Ẹ̀dà 2.1.0** · 2026-10-11"),
        ("Lati v2.0.1 awọn aworan ọja ti dahun pọ pẹlu skill ninu `assets/screenshots/`, ko tun gbẹkẹle ibi ipamọ aworan ita mọ",
         "Lati v2.1.0 ṣiṣe alaisanfarasin PayPal tun le ṣe itọsọna nipasẹ agent, gẹgẹ bi yiyan lẹgbẹẹ Alipay"),
    ],
    STEP6="""2. **Jẹ ki olumulo yan ọna isanwo**, ṣafihan awọn ọna meji:
   - **Alipay (Ilu China / olumulo ti o ni Alipay)**: rira-lẹẹkan fun akoko deede, **ko ṣe isọdọtun laifọwọyi**
     - Oṣu **¥6.99** (daba lati gbiyanju kọkọ) / mẹẹdogun **¥19.99** / ọdun **¥69.99**
   - **PayPal (okeere / olumulo laisi Alipay)**: isọdọtun oṣu laifọwọyi, a le fagilee nigbakugba
     - Premium Monthly, bii **$1/oṣu** (gẹgẹbi oju-iwe ṣiṣe alaisanfarasin ṣe fihan, isọdọtun laifọwọyi)
3. Nigbati olumulo ba yan:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Iwe naa da ọna faili oju-iwe isanwo pada, **ṣii taara pẹlu aṣẹ eto** (Windows: `start <faili>`; macOS: `open <faili>`; Linux: `xdg-open <faili>`). Aṣawakiri yoo lọ taara si alagbata Alipay/PayPal osise, olumulo ṣe isanwo tabi fowo si aṣẹ.
4. Ṣiṣẹ `query` ni iṣẹmu 10–15 kọọkan titi yoo fi da `paid` tabi `ACTIVE` pada (owo/ifọwọsi deede laarin iṣẹmu diẹ si iṣẹmu kan). Ti olumulo ba ti pa oju-iwe isanwo ni aarin → tun ṣiṣẹ `create-order` taara (aṣẹ atijọ / ṣiṣe alaisanfarasin PENDING ti pa laifọwọyi lẹhin wakati 2, maṣe yọnu).
5. Ọna iwo-koodu WeChat jẹ timo-ọkọnrin, isanwo n ṣe idaduro; Huawei IAP wa nikan ninu App HarmonyOS. Skill ko ṣe iranlọwọ awọn mejeeji — lẹhin isanwo pada si Ipe 7.
""",
    BOUNDARY=("fọwọkan akọọlẹ Alipay olumulo / ẹri isanwo", "fọwọkan akọọlẹ Alipay/PayPal olumulo / ẹri isanwo"),
    PA_CONCL="""**Awọn ọna isanwo Alipay ati PayPal mejeeji le ṣe itọsọna nipasẹ agent lati ṣẹda aṣẹ ati tọpa isanwo.**
Alipay jẹ rira-lẹẹkan laisi isọdọtun laifọwọyi, fun olumulo Ilu China/ti o ni Alipay; PayPal jẹ isọdọtun oṣu laifọwọyi ti a le fagilee nigbakugba, fun olumulo okeere/laisi Alipay. Iwo-koodu WeChat (timọ-ọkọnrin) ati Huawei IAP tun wa, ṣugbọn skill ko ṣe iranlọwọ wọn.""",
    PA_RESP=[
        ("fọwọkan akọọlẹ Alipay olumulo", "fọwọkan akọọlẹ Alipay/PayPal olumulo"),
        ("Iṣe isanwo nigbagbogbo jẹ ti olumulo funrarẹ ni alagbata Alipay osise.",
         "Iṣe isanwo nigbagbogbo jẹ ti olumulo funrarẹ ni alagbata osise."),
    ],
    PA_FRESH=("Nitorina skill lẹhin imudaniloju `paid` kọkọ ṣiṣẹ `refresh-login`",
              "Nitorina skill lẹhin imudaniloju `paid` / PayPal `ACTIVE` kọkọ ṣiṣẹ `refresh-login`"),
    PA_PAYPAL="""## Ọna isanwo alaisanfarasin PayPal (agent n ṣe iranlọwọ; oju-iwe wẹẹbu, kii ṣe HarmonyOS)

Eto Premium Monthly kan ṣoṣo ni o wa (bii $1/oṣu, gẹgẹbi `/api/subscription/plans` ṣe da pada), **isọdọtun oṣu laifọwọyi**,
olumulo le fagilee nigbakugba ninu akọọlẹ PayPal rẹ.

### Adrhun aaye (iwe skill ti fi pamọ, agent ko ṣe akopọ ibeere)

| Aaye | Ọna | Apejuwe |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer auth; da atokọ awọn ẹgbẹ to wulo pada (lọwọlọwọ 1 nikan) |
| `/api/subscription/create` | POST | body `{planId}` → da `{subscriptionId, approveUrl, status}` pada; `status` jẹ `APPROVAL_PENDING` nigbagbogbo |
| `/api/subscription/create` | GET | Bearer auth; da `{activeSubscription, allSubscriptions}` pada; agent ṣe ibeere `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Oju-iwe aṣeyọri n pe laifọwọyi (pẹlu kukisi); nigbati webhook ko ba de, pe API PayPal taara lati mu ṣiṣẹ |
| `/subscription/success` | Oju-iwe ipadabọ aṣawakiri | Ibugbe lẹhin ifọwọsi PayPal; ṣe ibeere verify laifọwọyi, lẹhinna pada si oju-iwe ile / oju-iwe atilẹba |
| `/subscription/cancel` | Oju-iwe aṣawakiri | Ibugbe nigbati olumulo ba fagilee tabi kuna; a le tun bẹrẹ |

### Ṣiṣan agent

```
create-order --provider paypal   # → da approveUrl pada, kọ sinu faili HTML agbegbe
ṣii faili HTML                   # → aṣawakiri lọ si oju-iwe ifọwọsi PayPal
query (ni iṣẹmu 10–15)           # → ṣe ibeere titi yoo fi ACTIVE
refresh-login                    # → gba JWT tuntun (ikede ṣiṣe alaisanfarasin ACTIVE)
login-link --target home         # → ṣe ipilẹṣẹ ọna asopọ wiwọle osise
```

- Ṣiṣe alaisanfarasin PENDING ti ko pari laarin wakati 1 yoo nu laifọwọyi nipasẹ backend; tun bẹrẹ nikan.
- Ti olumulo ba tun ṣiṣẹ `create-order`, backend yoo lo ṣiṣe alaisanfarasin `APPROVAL_PENDING` ti o wulo tẹlẹ, lati yago fun 409.
- Gẹgẹbi Alipay: isanwo ti de ṣe imudojuiwọn DB nikan — JWT atijọ ko ṣe imudojuiwọn laifọwọyi, nitorina **gbọdọ** ṣiṣẹ `refresh-login` ṣaaju ki o to ṣe ipilẹṣẹ ọna asopọ oju-iwe ile.""",
    PA_ROWS="""| PayPal `query` duro PENDING | Olumulo le ma ti pari ifọwọsi ni PayPal; rii daju pe ọna asopọ ifọwọsi ti ṣii ninu aṣawakiri. Ti o ba tun jẹ PENDING lẹhin ifọwọsi, webhook le ṣe idaduro — jẹ ki olumulo duro iṣẹmu diẹ lori oju-iwe aṣeyọri tabi ṣe imudojuiwọn |
| PayPal `query` da 409 pada | Ṣiṣe alaisanfarasin PENDING PayPal ti ko pari wa; duro wakati 1 ki o to di ofo, tabi pari ifọwọsi atijọ ninu aṣawakiri |
| Sanwo PayPal pari ṣugbọn ọna asopọ 2 tun di didena | Gẹgẹbi Alipay: kọkọ `refresh-login`, lẹhinna `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay aiyipada)<br>`--provider alipay\\|paypal` | Ṣẹda aṣẹ isanwo; Alipay da ọna faili oju-iwe isanwo + outTradeNo pada; PayPal da ọna faili oju-iwe ifọwọsi + subscriptionId pada (fi sinu faili ipo laifọwọyi) |",
    AF_ROW_QUERY="| `query` | —— | Ṣe ibeere ipo aṣẹ/ṣiṣe alaisanfarasin. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; ṣe ibeere ni iṣẹmu 10–15 |",
    AF_SEQ7="""7.  (olumulo yan ọna isanwo)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("    # → olumulo sanwo ni alagbata Alipay",
             "    # → olumulo sanwo/fọwọsi ni alagbata Alipay/PayPal"),
    AF_SEQ9=("9.  query (ni iṣẹmu 10–15) titi yoo fi paid",
             "9.  query (ni iṣẹmu 10–15) titi yoo fi paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Lẹhin `create-order` olumulo ti pa oju-iwe isanwo | Tun ṣiṣẹ `create-order` taara (aṣẹ atijọ laipẹ pa laifọwọyi ni wakati 2) |",
                  "| Lẹhin `create-order` olumulo ti pa oju-iwe isanwo | Tun ṣiṣẹ `create-order` taara (aṣẹ atijọ laipẹ pa laifọwọyi ni wakati 2; ṣiṣe alaisanfarasin PayPal PENDING yoo di ofo lẹhin wakati 1) |"),
    AF_ERR_409="| `create-order --provider paypal` da 409 pada | Ṣiṣe alaisanfarasin PENDING PayPal ti ko pari wa; duro wakati 1 ki o to di ofo, tabi pari ifọwọsi atijọ ninu aṣawakiri |",
    AF_ERR_PEND=("| `query` wa pending nigbagbogbo | Olumulo le ma sanwo; beere ọrọ kan. Ti o ba sanwo gangan → tẹle tabili ṣiṣayẹwo `payment-and-activation.md` |",
                 "| `query` wa pending / PENDING nigbagbogbo | Olumulo le ma sanwo; beere ọrọ kan. Ti o ba sanwo gangan → tẹle tabili ṣiṣayẹwo `payment-and-activation.md` |"),
    AF_ERR_403=("Isanwo ko tii de, pada si Ipe 9 tẹsiwaju ibeere",
                "Isanwo/ifọwọsi ko tii de, pada si Ipe 9 tẹsiwaju ibeere"),
    RD=[
        ("ṣiṣe aṣẹ ṣiṣe alaisanfarasin Alipay ati tọpa isanwo",
         "ṣiṣe aṣẹ ṣiṣe alaisanfarasin Alipay/PayPal ati tọpa isanwo"),
        ("**Lati v2.0.0 jẹ ipo agent-oluranlọwọ**",
         "**Lati v2.0.0 jẹ ipo agent-oluranlọwọ, ati lati v2.1.0 PayPal tun le ṣe itọsọna**"),
        ("sanwo ni alagbata Alipay.", "sanwo ni alagbata Alipay/PayPal."),
        ("4. **Ṣiṣe alaisanfarasin**: ọna Alipay agent ṣe iranlọwọ ṣẹda aṣẹ (osu ¥6.99 / mẹẹdogun ¥19.99 / ọdun ¥69.99, rira lẹẹkan laisi isọdọtun laifọwọyi) + tọpa isanwo; olumulo okeere pada si PayPal; itọsọna iwo-koodu WeChat / Huawei IAP.",
         "4. **Ṣiṣe alaisanfarasin**: ọna Alipay (osu ¥6.99 / mẹẹdogun ¥19.99 / ọdun ¥69.99, rira lẹẹkan laisi isọdọtun laifọwọyi) ati PayPal (Premium Monthly, bii $1/oṣu, isọdọtun laifọwọyi, a le fagilee nigbakugba) mejeeji jẹ ti agent ṣe iranlọwọ lati ṣẹda aṣẹ + tọpa isanwo; olumulo okeere pada si PayPal; itọsọna iwo-koodu WeChat / Huawei IAP."),
        ("rara fọwọkan akọọlẹ Alipay olumulo tabi ẹri isanwo, rara sanwo ni ipo rẹ. Isanwo n ṣẹlẹ nigbagbogbo laarin olumulo ati alagbata Alipay osise.",
         "rara fọwọkan akọọlẹ Alipay/PayPal olumulo tabi ẹri isanwo, rara sanwo ni ipo rẹ. Isanwo n ṣẹlẹ nigbagbogbo laarin olumulo ati alagbata osise."),
    ],
)
