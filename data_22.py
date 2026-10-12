# -*- coding: utf-8 -*-
LN = dict(
    DESC=[
        ("activation ya abonnement na Alipay", "activation ya abonnement na Alipay/PayPal"),
        ("afuti na caisse ya Alipay", "afuti na caisse ya Alipay/PayPal"),
    ],
    INTRO=("**kofuta na caisse ya Alipay** (agent efungolaka lokasa ya caisse automatiquement).",
           "**kofuta na caisse ya kofuta** (Alipay to PayPal — agent efungolaka lokasa ya caisse automatiquement)."),
    VLINE=[
        ("**Version 2.0.1** · 2026-10-08", "**Version 2.1.0** · 2026-10-11"),
        ("Uta v2.0.1 lilinzo ya produit ezali na pack na `assets/screenshots/`, esali kotekemelela image host ya libanda te)",
         "Uta v2.1.0 abonnement ya PayPal ekoki pe kosalema na agent, lokola choix pembeni ya Alipay)"),
    ],
    STEP6="""2. **Tika mosaleli apona nzela ya kofuta** — lakisa nzela nyonso mibale:
   - **Alipay (na kati ya Chine / ba mosaleli bazali na Alipay)**: achat mbala moko ya duree ekokani, **e-renouveler automatiquement te**
     - Mois **¥6.99** (proposer ya meka liboso) / Trimestre **¥19.99** / Annee **¥69.99**
   - **PayPal (mboka mosusu / ba mosaleli bazali na Alipay te)**: e-renouveler automatiquement chaque mois, ko-annuler ntango nionso
     - Premium Monthly, soki **$1/mois** (ndenge lokasa ya abonnement elakisi; e-renouveler automatiquement)
3. Mosaleli aponi moko:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Script ezongisa chemin ya fichier ya lokasa ya kofuta, **fungola directement na commande ya systeme** (Windows: `start <fichier>`; macOS: `open <fichier>`; Linux: `xdg-open <fichier>`). Navigateur eko zwa nzela directement na caisse officielle ya Alipay/PayPal, mosaleli asilisa kofuta to ndingisa ya facturation.
4. Mbala na secondes 10–15 sala `query` kino ezongisa `paid` to `ACTIVE` (mbongo/ndingisa mingi ekota na secondes moke kino minute moko). Mosaleli afunga lokasa ya kofuta na katikati → directement sala lisusu `create-order` (ba commandes ya kala / ba abonnements PENDING efungwama to esila nsima heures 2, tika yango).
5. Nzela ya scan WeChat ezali confirmation ya moto, mbongo ekoki kochelewa; Huawei IAP ezali kaka na kati ya app HarmonyOS. Skill esala yango mibale te — nsima ya kofuta zonga na Etape 7 ndenge moko.
""",
    BOUNDARY=("compte ya Alipay ya mosaleli / identite ya kofuta",
              "compte ya Alipay/PayPal ya mosaleli / identite ya kofuta"),
    PA_CONCL="""**Nzela ya Alipay na PayPal nyonso mibale sikoyo ekoki kosalema na agent — kosala commande na kolandela mbongo ekota.**
Alipay ezali achat mbala moko, e-renouveler automatiquement te, mpo na ba mosaleli ya Chine na ba oyo bazali na Alipay; PayPal e-renouveler automatiquement chaque mois mpe ekoki ko-annuler ntango nionso,
mpo na ba mosaleli ya mboka mosusu na ba oyo bazali na Alipay te. Scan WeChat (confirmation ya moto) na Huawei IAP ezali naino, kasi skill esala yango te.""",
    PA_RESP=[
        ("compte ya Alipay ya mosaleli / identite ya kofuta",
         "compte ya Alipay/PayPal ya mosaleli / identite ya kofuta"),
        ("Action ya kofuta mbala nionso esalaka na mosaleli moko moko na caisse officielle ya Alipay.",
         "Action ya kofuta mbala nionso esalaka na mosaleli moko moko na caisse officielle."),
    ],
    PA_FRESH=("nsima ya confirmation `paid` liboso esala `refresh-login`",
              "nsima ya confirmation `paid` / PayPal `ACTIVE` liboso esala `refresh-login`"),
    PA_PAYPAL="""## Nzela ya abonnement PayPal (agent esalaka yango; web, HarmonyOS te)

Plan moko kaka ezali, Premium Monthly (soki $1/mois, ndenge `/api/subscription/plans` ezongisaka); **e-renouveler automatiquement chaque mois**
mpo mosaleli akoki ko-annuler ntango nionso na compte na ye ya PayPal.

### Contract ya API (esili ko-emballer na script ya skill; agent asangisaka requête moko moko te)

| Endpoint | Methode | Note |
|---|---|---|
| `/api/subscription/plans` | GET | Auth Bearer; ezongisaka liste ya ba plans ezali (sikoyo moko kaka) |
| `/api/subscription/create` | POST | Corps `{planId}` → ezongisaka `{subscriptionId, approveUrl, status}`; `status` mingi ezali `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Auth Bearer; ezongisaka `{activeSubscription, allSubscriptions}`; agent atunaka `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Lokasa ya succès ebengaka yango automatiquement (na cookie); e-activer na API ya PayPal directement soki webhook ekomi naino te |
| `/subscription/success` | Lokasa ya retour ya navigateur | Lokasa ya kokita nsima ya ndingisa PayPal; e-poller verify automatiquement, nsima ezonga na lokasa ya ndako / lokasa ya kala |
| `/subscription/cancel` | Lokasa ya navigateur | Lokasa ya kokita ntango mosaleli a-annuler to esali échec; essai ya sika ekoki kobanda |

### Molongo ya agent

```
create-order --provider paypal   # → ezongisaka approveUrl, ekomama na fichier HTML local
open the HTML file               # → navigateur ezo zwa nzela na lokasa ya ndingisa PayPal
query (chaque secondes 10–15)    # → poller kino ACTIVE
refresh-login                    # → echanger JWT sika (declaration ya abonnement ACTIVE)
login-link --target home         # → sala lien officiel ya koneksione
```

- Ba abonnements PENDING oyo esilama te na kati ya heure 1, backend epetolaka yango automatiquement; banda lisusu.
- Soki mosaleli asali lisusu `create-order`, backend esalelaka lisusu abonnement `APPROVAL_PENDING` oyo ezali naino valide, eboya 409.
- Ndenge moko na Alipay: mbongo ekota ebongisaka kaka DB — JWT ya kala e-renouveler automatiquement te, yango wana **esengeli** osala `refresh-login` liboso ya kotinda lien ya lokasa ya ndako.""",
    PA_ROWS="""| PayPal `query` etikali PENDING | Mosaleli asilisi ndingisa na PayPal te; tala soki lien ya ndingisa efungwama na navigateur. Soki ezali naino PENDING nsima ya ndingisa, webhook ekoki kochelewa — tika mosaleli azela secondes moke na lokasa ya succès to a-refresh |
| PayPal `query` ezongisi 409 | Abonnement PENDING moko esilama naino te; zela heure 1 esila, to silisa ndingisa ya lien ya kala na navigateur |
| PayPal nsima ya kofuta, lien 2 ekota naino ebombama | Ndenge moko na Alipay: liboso `refresh-login` nsima `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (défaut Alipay)<br>`--provider alipay\\|paypal` | Sala commande ya kofuta; Alipay ezongisa chemin ya fichier ya lokasa ya kofuta + outTradeNo; PayPal ezongisa chemin ya fichier ya lokasa ya ndingisa + subscriptionId (ekanda automatiquement na fichier etat) |",
    AF_ROW_QUERY="| `query` | —— | Tuna etat ya commande/abonnement. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; poller chaque secondes 10–15 |",
    AF_SEQ7="""7.  (Mosaleli aponi nzela ya kofuta)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("    # → mosaleli afuta na caisse ya Alipay (sehemu ya kobima na lisolola②)",
             "    # → mosaleli asilisa kofuta/ndingisa na caisse ya Alipay/PayPal (sehemu ya kobima na lisolola②)"),
    AF_SEQ9=("9.  query (chaque secondes 10–15) kino paid",
             "9.  query (chaque secondes 10–15) kino paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Nsima ya `create-order` mosaleli afunga lokasa ya kofuta | Sala directement lisusu `create-order` (commande ya kala efungwama automatiquement nsima heures 2) |",
                  "| Nsima ya `create-order` mosaleli afunga lokasa ya kofuta | Sala directement lisusu `create-order` (commande ya kala efungwama automatiquement nsima heures 2; ba abonnements PENDING ya PayPal esila nsima heure 1) |"),
    AF_ERR_409="| `create-order --provider paypal` ezongisi 409 | Abonnement PayPal moko esilama naino te; zela heure 1 esila, to silisa ndingisa ya kala na navigateur |",
    AF_ERR_PEND=("| `query` ezali kofanda pending | Ekoki kozala mosaleli afuti te; tuna moko. Asili afuti → landa table ya kotunga ya payment-and-activation.md |",
                 "| `query` ezali kofanda pending / PENDING | Ekoki kozala mosaleli afuti te; tuna moko. Asili afuti → landa table ya kotunga ya payment-and-activation.md |"),
    AF_ERR_403=("Kofuta naino ekomi te,", "Kofuta/ndingisa naino ekomi te,"),
    RD=[
        ("commande ya abonnement Alipay na kolandela mbongo ekota",
         "commande ya abonnement Alipay/PayPal na kolandela mbongo ekota"),
        ("**Uta v2.0.0 ezali mode ya agent-esalaka**",
         "**Uta v2.0.0 ezali mode ya agent-esalaka, mpe uta v2.1.0 PayPal ekoki pe kosalema**"),
        ("na caisse ya Alipay afuta. Soki Node ezali te", "na caisse ya Alipay/PayPal afuta. Soki Node ezali te"),
        ("4. **Abonnement na kofuta**: nzela ya Alipay agent esala commande (mois ¥6.99 / trimestre ¥19.99 / annee ¥69.99, achat mbala moko ko-renouveler automatiquement te) + kolandela mbongo ekota; mosaleli ya mboka mosusu ezonga na PayPal; scan WeChat / Huawei IAP lakisa nzela.",
         "4. **Abonnement na kofuta**: Alipay (mois ¥6.99 / trimestre ¥19.99 / annee ¥69.99, achat mbala moko ko-renouveler automatiquement te) na PayPal (Premium Monthly, soki $1/mois, e-renouveler automatiquement, ko-annuler ntango nionso) nyonso mibale agent esala commande + kolandela mbongo ekota; scan WeChat / Huawei IAP lakisa nzela."),
        ("jamais ekanga compte ya Alipay ya mosaleli to identite ya kofuta, jamais efuta na esika ya mosaleli. Kofuta esalaka mbala nionso na kati ya mosaleli na caisse officielle ya Alipay.",
         "jamais ekanga compte ya Alipay/PayPal ya mosaleli to identite ya kofuta, jamais efuta na esika ya mosaleli. Kofuta esalaka mbala nionso na kati ya mosaleli na caisse officielle."),
    ],
)
