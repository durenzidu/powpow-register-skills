# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: Lingala."""
LN = dict(
    DESC="description: Esungisaka motaleli mpé kosilisa enregistrement na PowPow (Bubble) pe kokota na clic moko na kati ya masolo. Agent akopisaka formula na esika ya motaleli (na kotya avatar) pe atindaka email ya code de vérification; motaleli abongisi sé kopesa ba informations de base pe komona code de vérification mbala moko — koleka te na masolo. Plateforme lelo ezali na période d'essai gratuit: compte enregistré akoki kosalisa ba fonctionnalités nionso mbala moko; paiement ya abonnement (Alipay/PayPal) ezali amélioration ya membre ya option, oyo agent akoki kosala na création de commande pe suivi ya argent naino soki esengeli. Etambuli tango motaleli alobi \"enregistrer na Bubble\", \"sala compte powpow\", \"ndenge nini kosala enregistrement na Bubble\", \"salisa ngai na kosala compte powpow\", \"sign up powpow\"; pe esalisi na ba problèmes ya enregistrement (code de vérification eyaki te, nom ya motaleli/email ezuami déjà) pe ba problèmes ya activation (kokota elobi \"compte eactivé te\" / pending_payment, ndenge nini kosala abonnement/paiement, Bubble est gratuit to ezali paiement). Esengeli Node ≥ 18; soki ezali te, ezali koleka na mode ya guide pur. Ezali te kobimisa/créer ba humains numériques (mosala ya powpow-simple), ezali te développement ya code.",
    INTRO="Ememaka motaleli ya sika uta \"nayebi te Bubble nini\" tii \"nakoti na clic moko, pronto kosala\" — nionso na kati ya masolo. Motaleli atikaka masolo mbala moko sé: **mpo na komona code de vérification na boîte de réception**. Plateforme lelo ezali na période d'essai gratuit: nsima ya enregistrement, ba fonctionnalités nionso ezali, bosenga ya paiement te; paiement ya abonnement ezali amélioration ya membre ya option (agent afungukaka caisse pe alandaka argent naino).",
    VLINE="**Version 2.2.0** · 2026-10-18 (kobanda na v2 oyo ezali mode ya aide ya agent: contrat ya script pe ordre mobimba ezali na `references/agent-flow.md`; ba règles ya champ, ba limites ya débit pe diagnostic d'erreur na `references/registration-flow.md`; ba canaux ya paiement na `references/payment-and-activation.md`; liste ya captures d'écran ya produit na `references/screenshots.md`. Kobanda na v2.1.0 abonnement PayPal akoki kosalama na agent, lokola option na côté ya Alipay. Kobanda na v2.2.0 plateforme ekoti na période d'essai gratuit: enregistrer pe kokota na clic moko mpo na kosala mbala moko; paiement ekomi amélioration ya option — soki motaleli abendi lien pe akwei na page d'abonnement, période d'essai esili, landa flux ya paiement uta na étape 7; flux esengeli komibongisa yango moko, bosenga te ya kobongola script)",
    RT_ENV="- **Node te / ba erreurs ya script**: koleka automatique na mode ya guide pur — pesa motaleli page d'enregistrement https://global.powpow.online/register pe lakisa ye na côté selon `references/registration-flow.md` (na période d'essai gratuit, enregistrement na web ezali mbala moko rapide). Kobundela script mbala na mbala te.",
    TRIGGER="- Ba problèmes nsima ya enregistrement: \"kokota elobi compte eactivé te\", \"403 pending_payment\", \"ndenge nini kosala paiement/abonnement na Bubble\", \"Bubble est gratuit to ezali paiement\"",
    FLOW6="| 6 Kokota na clic moko | `login-link(home)` directement na page d'accueil; soki akwei na page d'abonnement, kende na étape 7 | Benda lien pe banda kosala |",
    FLOW7="| 7 Amélioration d'abonnement (option) | Sé tango motaleli alingi membre / période gratuite esili: flux ya paiement mobimba | Pona méthode, futa |",
    STEP6="""## Étape 6: Kokota na clic moko (nsima ya enregistrement directement na page d'accueil)

1. Mbala moko nsima ya enregistrement elongi:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Tinda lien na motaleli: **benda pe okozala directement na page d'accueil, okoti déjà**. Plateforme lelo ezali na période d'essai gratuit — nsima ya enregistrement ba fonctionnalités nionso ezali (feed, carte, humains numériques, check-ins, etc.), **bosenga ya paiement te**.
3. Lakesa motaleli andimisa akoti; ba cas mibale ezali:
   - **Akwei na page d'accueil** → kokende directement na étape 8 mpo na kosilisa; enregistrement esili;
   - **Akwei na page d'abonnement** → période d'essai gratuit ya plateforme esili; láta na motaleli \"période d'essai gratuit esili, soki membre abonnement esengeli sikoyo\", nsima landa étape 7 mpo na kosilisa abonnement, pe nsima ya abonnement zonga na étape 8.
4. Soki motaleli moko alingi amélioration to soutenir plateforme → kokende na étape 7 (abonnement volontaire; kobenda nguya te).""",
    STEP7="""## Étape 7: Amélioration d'abonnement (option — sé tango étape 6 elobi)

1. Liboso tinda lien ya demi-kokota mpo na page ya retour nsima ya paiement emonisa \"Paiement elongi\" lolenge:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Tinda lien na motaleli: benda pe navigateur directement na page d'abonnement, okoti déjà.
2. **Lakesa motaleli apona méthode ya paiement** — monisa ba canaux mibale:
   - **Alipay (Chine continentale / ba utilisateurs na Alipay)**: achat moko ya durée, **auto-renouvellement te**
     - Sanza **¥6.99** (pona essai) / Misato **¥19.99** / Mobu **¥69.99**
   - **PayPal (internasyonal / ba utilisateurs sans Alipay)**: auto-renouvellement sanza na sanza, annuler na ntiná nionso
     - Premium Monthly, penza **$1/sanza** (lokola emonisi na page d'abonnement; na auto-renouvellement)
3. Soki motaleli apona moko:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Script azongisi chemin ya fichier ya page ya paiement; **fungula ye directement na commande système** (Windows: `start <fichier>`; macOS: `open <fichier>`; Linux: `xdg-open <fichier>`). Navigateur akende automatique na caisse officiel Alipay/PayPal, epai motaleli asilisaka paiement to autorisation ya facturation.
4. Salisa `query` na 10–15 secondes tii azongisi `paid` to `ACTIVE` (paiement/autorisation ekweaka na ba secondes tii na minute moko). Soki motaleli afongwaki page ya paiement na katikati → sé `create-order` lisusu (ba commandes anciens / abonnements en attente bakofungama to bakosila nsima ya ba heures 2; koyeba te).
5. Canal ya code QR WeChat endimisaka na loboko pe argent akoki koyoka; Huawei IAP ezali sé na kati ya application HarmonyOS. Skill esalaka yango mibale te — nsima ya paiement, motaleli azongi pe alobaka na agent, oyo liboso asalaka `whoami` mpo na koyeba soki argent ekwei, nsima atindaka lien ya page d'accueil selon point 6 oyo ezali awa na se.
6. Nsima ya koyeba soki argent ekwei, bongola état ya kokota na affirmation ya abonnement ya sika, nsima tinda lien directement na page d'accueil:
   ```
   POWPOW_REGISTER_PASSWORD=<mot de passe> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Tinda lien na motaleli: **benda pe okozala directement na page d'accueil na état ya membre mobimba**.""",
    STEP8="""## Étape 8: Kosilisa

1. `node scripts/powpow-register.mjs cleanup` mpo na kopetola ba fichiers temporaires locaux (identifiants ya session).
2. Pesa motaleli "carte de compte": nom d'utilisateur, email (mot de passe emonanisaka lisusu te — na mode généré motaleli alobelaki kobomba tango egenerami; soki motaleli atieki yango moko, ayebi yango).
3. Lembisi ya membre (loba mbala moko, kobenda nguya te): lelo ezali période d'essai gratuit pe compte esalaka mbala moko; tango période d'essai esili, ba comptes sans abonnement tango bakokota na ba pages ya contenu bakozwa redirection na page d'abonnement — mpo na utilisation ya temps molai, zonga pe sala abonnement na ntiná nionso.
4. Lakisa ba étapes ya liboso: tala carte, publike journal ya voyage ya liboso (→ kopesa na powpow-simple).
5. Recommander ba extensions: skill `@durenzidu/powpow-integration` pe plugin `@durenzidu/openclaw-channel-powpow` — connecter Bubble na agent ya motaleli moko; pesa commande d'installation soki alingi.
6. Silisa na bloc "étape oyo elandi".""",
    WALL="- **Paywall ezali bug te**: na période d'essai gratuit lelo ba pages ya contenu nionso bazali ouvert; soki motaleli abendi lien ya page d'accueil pe akwei na page d'abonnement — période d'essai esili, lakisa ye asala abonnement na étape 7. Komeka kopikola paywall te, pe koyebisa ba mécanismes internes na motaleli te.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` to `--target home` | Esalaka lien ya kokota na clic moko (design ya ba liens mibale, tala awa na se) |",
    AF_LINKSEQ="""## Mécanisme ya ba liens mibale (design central)

État ya kokota ya plateforme ezali cookie HttpOnly, oyo agent akoki kotya yango directement na navigateur te; pont ezali endpoint officiel
`/api/auth/me?token=<JWT>&redirect=<chemin na kati ya site>`: vérifier signature → création automatique
session → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 jours) → valider
redirect (esengeli abanda na slash moko, `//` pe ba slash ya nsima epekisami, esengeli ezala same-origin nsima ya analyse) → 307 redirection temporaire na page cible.

Ba cibles ya lien mibale ezali, **liboso créer home, nsima décider passer par to te selon epai motaleli akwei**:

- **lien home (etindami par défaut, `--target home` → akwei na `/`)**: ecreami pe etindami na motaleli mbala moko nsima ya enregistrement elongi.
  Na période d'essai gratuit motaleli akende directement na page d'accueil, utilisation mobimba; **soki abendi lien pe akwei na page d'abonnement — période d'essai gratuit esili** — bongola na flux ya paiement (tala awa na se); bosenga te ya kobongola script pe enregistrement lisusu.
- **lien pending (esalemi na flux ya paiement, `--target pending` → akwei na `/subscription`)**:
  navigateur ya motaleli ekoti na état "demi-kokota": page d'abonnement pe page ya retour nsima ya paiement emonani pe esalaka. Nsima ya argent ekwei,
  salisa `refresh-login` mpo na bongola JWT ya sika na affirmation ACTIVE, nsima tinda lien home lisusu mpo na état ya membre mobimba.

## Ordre mobimba

### Chemin rapide (na période d'essai gratuit — majorité ya ba cas)

```
1.  status                          # auto-vérification d'environnement
2.  (étape 2 masolo mpo na confirmer informations, mot de passe nionso; mode généré: gen-password → láta motaleli abomba mbala moko)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → motaleli atala code na boîte de réception (tangoko ya kokabola masolo)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → tinda lien na motaleli; clic moko pe na page d'accueil
7.  (motaleli andimisi akoti) → silisa directement: cleanup + carte de compte + lakisa ba étapes ya liboso
```

### Chemin ya paiement (tango motaleli alingi membre, to période d'essai gratuit esili)

```
1–5. Lokola chemin rapide (état ezali na token nsima ya enregistrement elongi)
6.  login-link --target pending     # → lien demi-kokota, ebombaka page ya retour ya paiement esala
7.  (motaleli apona méthode ya paiement)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <fichier ya page ya paiement>       # Windows; macOS esaleli open, Linux esaleli xdg-open
    # → motaleli asilisaka paiement/autorisation na caisse Alipay/PayPal (akabwaka masolo)
9.  query (na 10–15s) tii paid / ACTIVE
10. refresh-login                   # bongola JWT ya sika na affirmation ACTIVE
11. login-link --target home        # → tinda lien membre mobimba na motaleli
12. whoami                          # confirmer subscriptionStatus: ACTIVE (option)
13. cleanup                         # petola fichier ya état
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Période d'essai gratuit esili pe paiement ekwei te; zonga na étape 9 kokoba interroger, to confirmer soki motaleli asilisaki paiement |",
    AF_ERR_SUB="| Motaleli abendi lien home pe akwei na page d'abonnement | Période d'essai gratuit esili → bongola na flux ya paiement: `login-link --target pending` → pona méthode ya paiement → `create-order` |",
    AF_FALLBACK="Nsima ya kozonga: pesa page d'enregistrement https://global.powpow.online/register (na période d'essai gratuit, enregistrement na web ezali mbala moko rapide; tango abonnement esengeli, pesa page d'abonnement pe https://global.powpow.online/subscription ), silisa problème na côté selon ba règles na `registration-flow.md`, bombaka ton moko, pe silisa na tour nionso na bloc \"étape oyo elandi\".",
    PA_NOTE="""> **Période d'essai gratuit (kobanda 2026-10-18; comportement réel ya plateforme ezali oyo eleki)**: na période oyo compte enregistré akoki kosalisa ba fonctionnalités nionso directement, pe **sala abonnement ezali amélioration ya option te exigence** — landa flux ya fichier oyo sé tango motaleli moko alingi membre. Tango période d'essai esili, ba comptes sans abonnement tango bakokota na ba pages ya contenu bakozwa redirection na page d'abonnement; silisa abonnement selon fichier oyo.""",
    RF_STATE="""## Flux ya état nsima ya enregistrement elongi

> **Période d'essai gratuit (kobanda 2026-10-18; comportement réel ya plateforme ezali oyo eleki)**: compte ya sika enregistré akoki **kosalisa ba fonctionnalités nionso directement**
> (feed, carte, humains numériques, check-ins, etc.) paiement te; ba comptes sans abonnement bazali sé na ba pages ya contenu lisusu te. "Blocage pending"
> oyo edescriptami na section oyo ezali état normal nsima ya période d'essai — tango tango wana ekoya, comportement réel en ligne ezali oyo eleki.

1. Motaleli abombami na `accountStatus: 'pending'` pe **3 badges ya liboso** (route register).
2. Serveur atiaka pe cookies mibale HttpOnly: JWT (akoki kokota na ba pages directement) pe pendingUserToken (identifiant ya flux ya abonnement).
3. Na état normal (période d'essai esili / période gratuite te), page d'enregistrement edetecte `pending_payment` → redirection na `/subscription`
   (ebombaka paramètre ya retour `next`); na mode ya aide ya agent, `me?token=…&redirect=/subscription` esalaka effet moko.
   **Na période d'essai gratuit étape oyo etambulaka te** — nsima ya enregistrement, kende directement na page d'accueil pe banda kosala.
4. Paiement esili → `accountStatus` ekomi `active` (**Alipay eactive automatique côté serveur via notify**;
   PayPal eactive via Webhook; code QR WeChat endimisaka na loboko; Huawei IAP epusi via `activate-huawei`).
   Tala `payment-and-activation.md` mpo na détails.

Na état normal, ba utilisateurs inactifs (pending) bakobenga API central (feed, carte, discussion ya humain numérique, check-ins, etc.) bazwaka 403;
ba liens ya publication partagés bazali exception (ebombami accessibles publiquement). Na période d'essai gratuit blocage oyo esalemaka te pe nionso ezali ouvert.""",
    RF_ROW_403="| Enregistrement elongi mais kokota azongisi 403 \"请完成订阅以激活账户\" | Compte azali pending, pe plateforme ezali na période d'essai gratuit te (état attendu avant paiement) | Ekosalema te na période d'essai gratuit; soki esalemi, période d'essai esili — silisa abonnement liboso; soki 403 kaka nsima ya paiement, JWT ya kala esalemaki — na mode script liboso salisa `refresh-login` mpo na bongola état ya kokota ya sika |",
    RF_ROW_LAND="| Motaleli abendi lien ya kokota pe akwei na page d'abonnement (esika ya page d'accueil) | Période d'essai gratuit esili pe paywall ya plateforme azongi | Landa flux ya paiement d'abonnement étape 7 na SKILL.md; nsima ya abonnement, salisa `refresh-login` nsima tinda lien ya page d'accueil |",
    RD_VER="""**Kobanda na v2.0.0 oyo ezali mode ya aide ya agent, pe kobanda na v2.2.0 ebongisami na période d'essai gratuit ya plateforme**: script central `scripts/powpow-register.mjs` azali na dépendances zéro
(Node ≥ 18); motaleli atikaka masolo mbala moko sé: mpo na komona code de vérification na boîte de réception. Na période d'essai gratuit lelo, compte enregistré akoki kosalisa ba fonctionnalités nionso mbala moko — paiement ya abonnement ezali amélioration ya option; soki période d'essai esili pe motaleli akwei na page d'abonnement, flux ebongolaka yango moko na chemin ya paiement. Soki Node te, to tango motaleli alingi kosala yango moko, ezali koleka automatique na mode ya guide pur.""",
    RD_LINK="""3. **Kokota na clic moko (ba liens mibale)**: mbala moko nsima ya enregistrement elongi, lien ya kokota ememaka motaleli directement na page d'accueil (na période d'essai gratuit, clic moko pe esalaka);
   soki akwei na page d'abonnement (période d'essai esili) to motaleli alingi amélioration, landa flux d'abonnement — nsima ya argent ekwei, état ya kokota ya sika ebongolami pe lien ya membre mobimba ememaka ye na page d'accueil
   (via pont officiel `me?token=` ya plateforme, oyo atiaka cookie HttpOnly automatique).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
