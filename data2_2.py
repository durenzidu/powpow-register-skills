# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: French, German, Portuguese, Italian."""
FR = dict(
    DESC="description: Aide les utilisateurs à terminer l'inscription à PowPow (Bulle) et la connexion en un clic, entièrement dans la conversation. L'agent remplit le formulaire à leur place (y compris le téléversement de l'avatar) et envoie le code de vérification par e-mail ; l'utilisateur ne fournit que les informations de base et consulte le code une fois, sans quitter la conversation. Pendant la période actuelle d'essai gratuit de la plateforme, un compte inscrit peut utiliser toutes les fonctions immédiatement ; le paiement de l'abonnement (Alipay/PayPal) est une amélioration d'adhésion facultative, que l'agent peut aussi prendre en charge avec création de commande et suivi de l'encaissement si besoin. Se déclenche quand l'utilisateur dit « s'inscrire à Bulle », « créer un compte powpow », « comment s'inscrire à Bulle », « aide-moi à créer un compte powpow », « sign up powpow » ; gère aussi les blocages d'inscription (code de vérification non reçu, nom d'utilisateur/e-mail déjà pris) et les problèmes d'activation (la connexion dit « compte non activé » / pending_payment, comment s'abonner/payer, Bulle est-ce gratuit ?). Nécessite Node ≥ 18 ; replie automatiquement en mode guidage pur si indisponible. Ne couvre pas la publication/la création d'humains numériques (c'est le domaine de powpow-simple), ni le développement code.",
    INTRO="Emmène un nouvel utilisateur de « je ne sais pas ce qu'est Bulle » à « connexion en un clic, prêt à jouer » — entièrement dans la conversation. L'utilisateur ne quitte la conversation qu'une seule fois : **pour consulter le code de vérification dans sa boîte mail**. La plateforme est actuellement en période d'essai gratuit : une fois inscrit, toutes les fonctions sont utilisables, aucun paiement requis ; le paiement de l'abonnement est une amélioration d'adhésion facultative (l'agent ouvre aussi la caisse et suit l'encaissement).",
    VLINE="**Version 2.2.0** · 2026-10-18 (depuis la v2, mode assisté par agent : contrat du script et séquence complète dans `references/agent-flow.md` ; règles de champs, limites de débit et dépannage des erreurs dans `references/registration-flow.md` ; canaux de paiement dans `references/payment-and-activation.md` ; liste des captures produit dans `references/screenshots.md`. Depuis la v2.1.0, les abonnements PayPal peuvent aussi être gérés par l'agent, en option aux côtés d'Alipay. Depuis la v2.2.0, la plateforme entre en période d'essai gratuit : inscris-toi et connecte-toi en un clic pour commencer ; le paiement devient une amélioration facultative — si l'utilisateur ouvre le lien et atterrit sur la page d'abonnement, la période d'essai est terminée, suis alors le flux de paiement de l'étape 7 ; le flux s'adapte tout seul, aucune modification du script)",
    RT_ENV="- **Pas de Node / erreurs du script** : replie automatiquement en mode guidage pur — donne à l'utilisateur la page d'inscription https://global.powpow.online/register et accompagne-le selon `references/registration-flow.md` (pendant la période d'essai gratuit, l'inscription web est tout aussi immédiate). N'insiste pas avec le script.",
    TRIGGER="- Problèmes après inscription : « la connexion dit que le compte n'est pas activé », « 403 pending_payment », « comment payer/s'abonner à Bulle », « Bulle c'est gratuit ou payant ? »",
    FLOW6="| 6 Connexion en un clic | `login-link(home)` directement sur la page d'accueil ; si ça atterrit sur la page d'abonnement, passe à l'étape 7 | Clique le lien et commence à jouer |",
    FLOW7="| 7 Amélioration d'abonnement (facultative) | Seulement si l'utilisateur veut l'adhésion / la période gratuite est terminée : flux de paiement complet géré | Choisis un moyen, paie |",
    STEP6="""## Étape 6 : Connexion en un clic (directement sur la page d'accueil après l'inscription)

1. Juste après l'inscription réussie :
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Envoie le lien à l'utilisateur : **ouvre-le et tu atterris directement sur la page d'accueil, déjà connecté**. La plateforme est actuellement en période d'essai gratuit — après l'inscription, toutes les fonctions sont utilisables (fil, carte, humains numériques, check-ins, etc.), **aucun paiement requis**.
3. Demande à l'utilisateur de confirmer qu'il est bien entré ; il y a deux cas :
   - **Arrivé sur la page d'accueil** → passe directement à l'étape 8 pour conclure ; l'inscription est terminée ;
   - **Arrivé sur la page d'abonnement** → la période d'essai gratuit de la plateforme est terminée ; dis à l'utilisateur « la période d'essai gratuite est terminée, un abonnement d'adhésion est désormais requis », puis suis l'étape 7 pour finaliser l'abonnement, et reviens à l'étape 8 après.
4. Si l'utilisateur veut activement améliorer ou soutenir la plateforme → passe aussi à l'étape 7 (s'abonner est volontaire ; ne pousse pas).""",
    STEP7="""## Étape 7 : Amélioration d'abonnement (facultative — seulement quand l'étape 6 l'exige)

1. Envoie d'abord le lien de demi-connexion pour que la page de retour du paiement affiche correctement « Paiement réussi » :
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Envoie le lien à l'utilisateur : en l'ouvrant, le navigateur atterrit directement sur la page d'abonnement, déjà connecté.
2. **Laisse l'utilisateur choisir le moyen de paiement** — montre les deux canaux :
   - **Alipay (Chine continentale / utilisateurs avec Alipay)** : achat unique de la durée correspondante, **pas de renouvellement automatique**
     - Mensuel **6,99 ¥** (recommandé pour essayer) / Trimestriel **19,99 ¥** / Annuel **69,99 ¥**
   - **PayPal (outre-mer / utilisateurs sans Alipay)** : renouvellement mensuel automatique, annulable à tout moment
     - Premium Monthly, environ **1 $/mois** (selon l'affichage de la page d'abonnement ; renouvellement automatique)
3. Une fois le choix fait :
   - **Alipay** :
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal** :
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Le script renvoie le chemin du fichier de la page de paiement ; **ouvre-le directement avec une commande système** (Windows : `start <fichier>` ; macOS : `open <fichier>` ; Linux : `xdg-open <fichier>`). Le navigateur saute automatiquement à la caisse officielle Alipay/PayPal, où l'utilisateur finalise le paiement ou l'autorisation de facturation.
4. Lance `query` toutes les 10–15 secondes jusqu'à obtenir `paid` ou `ACTIVE` (l'encaissement/l'autorisation arrive généralement en quelques secondes à une minute). Si l'utilisateur ferme la page de paiement en cours de route → relance directement `create-order` (les anciennes commandes / abonnements en attente se ferment ou expirent automatiquement après 2 heures ; ignore-les).
5. Le canal code QR WeChat est confirmé manuellement et l'encaissement peut tarder ; Huawei IAP n'est disponible que dans l'app HarmonyOS. Le skill ne gère pas ces deux canaux — après avoir payé, l'utilisateur revient le dire, et l'agent lance d'abord `whoami` pour confirmer l'encaissement, puis envoie le lien vers la page d'accueil du point 6 ci-dessous.
6. Après confirmation de l'encaissement, échange contre un état de session avec la déclaration d'abonnement la plus récente, puis envoie le lien direct vers la page d'accueil :
   ```
   POWPOW_REGISTER_PASSWORD=<mot de passe> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Envoie le lien à l'utilisateur : **ouvre-le et tu atterris directement sur la page d'accueil avec l'adhésion complète**.""",
    STEP8="""## Étape 8 : Conclusion

1. `node scripts/powpow-register.mjs cleanup` pour nettoyer les fichiers d'état temporaires locaux (identifiants de session).
2. Donne à l'utilisateur une « fiche de compte » : nom d'utilisateur, e-mail (le mot de passe n'est pas réaffiché — en mode généré, l'utilisateur a déjà été invité à le sauvegarder à la génération ; s'il l'a choisi lui-même, il le connaît).
3. Rappel d'adhésion (dis-le une fois, ne pousse pas) : actuellement c'est une période d'essai gratuit et le compte est utilisable immédiatement ; quand la période d'essai se terminera, les comptes non abonnés visitant les pages de contenu seront redirigés vers la page d'abonnement — pour un usage prolongé, reviens demander à l'agent de t'abonner quand tu veux.
4. Guide les premiers pas : parcourir la carte, publier le premier carnet de voyage (→ passe à powpow-simple).
5. Recommande des extensions : le skill `@durenzidu/powpow-integration` et le plugin `@durenzidu/openclaw-channel-powpow` — connecte Bulle à l'agent de l'utilisateur ; donne la commande d'installation s'il le souhaite.
6. Termine par un bloc « prochaine étape ».""",
    WALL="- **Le mur de paiement n'est pas un bug** : pendant la période d'essai gratuit actuelle, toutes les pages de contenu sont ouvertes ; si l'utilisateur ouvre le lien vers la page d'accueil mais atterrit sur la page d'abonnement, la période d'essai est terminée — guide-le vers l'abonnement via l'étape 7. N'essaie pas de contourner le mur de paiement et n'explique pas les mécanismes internes à l'utilisateur.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` ou `--target home` | Génère un lien de connexion en un clic (conception à double lien, voir plus bas) |",
    AF_LINKSEQ="""## Mécanisme à double lien (conception centrale)

L'état de session de la plateforme est un cookie HttpOnly, que l'agent ne peut pas planter directement dans le navigateur ; le pont est l'endpoint officiel
`/api/auth/me?token=<JWT>&redirect=<chemin interne>` : vérifier la signature → créer la session automatiquement
→ `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 jours) → valider
la redirection (doit commencer par une seule barre, `//` et barres obliques inverses interdits, même origine après analyse) → 307 redirection temporaire vers la page cible.

Il y a deux cibles de lien, **génère d'abord home, puis décide s'il faut passer par pending selon où atterrit l'utilisateur** :

- **lien home (envoyé par défaut en premier, `--target home` → atterrit sur `/`)** : généré et envoyé à l'utilisateur immédiatement après l'inscription réussie.
  Pendant la période d'essai gratuit, l'utilisateur entre directement sur la page d'accueil, tout est utilisable ; **si l'utilisateur l'ouvre mais atterrit sur la page d'abonnement, la période d'essai gratuit est terminée** — bascule alors sur le chemin de paiement (voir plus bas) ; aucun changement de script ni réinscription nécessaire.
- **lien pending (utilisé dans le chemin de paiement, `--target pending` → atterrit sur `/subscription`)** :
  le navigateur de l'utilisateur entre en état de « demi-connexion » : la page d'abonnement et la page de retour du paiement sont visibles et utilisables. Après l'encaissement,
  lance `refresh-login` pour échanger contre un nouveau JWT portant la déclaration ACTIVE, puis renvoie le lien home une fois de plus pour l'adhésion complète.

## Séquence complète

### Chemin rapide (pendant la période d'essai gratuit — la grande majorité des cas)

```
1.  status                          # auto-vérification de l'environnement
2.  (étape 2 conversation pour confirmer les infos, mot de passe au choix ; mode généré : gen-password → faire sauvegarder immédiatement par l'utilisateur)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → l'utilisateur consulte le code dans sa boîte mail (seule sortie de la conversation)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → envoie le lien à l'utilisateur ; un clic et il est sur la page d'accueil
7.  (l'utilisateur confirme qu'il est entré) → conclus directement : cleanup + fiche de compte + guide des premiers pas
```

### Chemin de paiement (quand l'utilisateur veut l'adhésion, ou que la période d'essai gratuit est terminée)

```
1–5. Identique au chemin rapide (le state contient déjà le token après un register réussi)
6.  login-link --target pending     # → lien de demi-connexion, garde la page de retour du paiement fonctionnelle
7.  (l'utilisateur choisit le moyen de paiement)
    # Alipay : create-order --package monthly|quarterly|yearly
    # PayPal : create-order --provider paypal
8.  start <fichier de page de paiement>   # Windows ; macOS utilise open, Linux utilise xdg-open
    # → l'utilisateur finalise le paiement/l'autorisation à la caisse Alipay/PayPal (sort de la conversation)
9.  query (toutes les 10–15 s) jusqu'à paid / ACTIVE
10. refresh-login                   # échange contre un nouveau JWT portant la déclaration ACTIVE
11. login-link --target home        # → envoie le lien d'adhésion complète à l'utilisateur
12. whoami                          # confirme subscriptionStatus: ACTIVE (facultatif)
13. cleanup                         # nettoie le fichier d'état
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | La période d'essai gratuit est terminée et le paiement n'est pas encore arrivé ; retourne à l'étape 9 pour continuer à sonder, ou confirme si l'utilisateur a finalisé le paiement |",
    AF_ERR_SUB="| L'utilisateur ouvre le lien home mais atterrit sur la page d'abonnement | La période d'essai gratuit est terminée → bascule sur le chemin de paiement : `login-link --target pending` → choisis un moyen de paiement → `create-order` |",
    AF_FALLBACK="Après repli : donne la page d'inscription https://global.powpow.online/register (pendant la période d'essai gratuit, l'inscription web est tout aussi immédiate ; quand un abonnement est nécessaire, donne aussi la page d'abonnement https://global.powpow.online/subscription ), accompagne le dépannage selon les règles de `registration-flow.md`, garde le même ton et termine chaque tour par un bloc « prochaine étape ».",
    PA_NOTE="""> **Période d'essai gratuit (à partir du 2026-10-18 ; le comportement réel de la plateforme prévaut)** : pendant cette période, un compte inscrit peut utiliser toutes les fonctions directement, et **s'abonner est une amélioration facultative plutôt qu'une exigence** — suis le flux de ce fichier seulement quand l'utilisateur veut activement l'adhésion. Quand la période d'essai se terminera, les comptes non abonnés visitant les pages de contenu seront redirigés vers la page d'abonnement ; il suffit de finaliser l'abonnement selon ce fichier.""",
    RF_STATE="""## Flux d'état après une inscription réussie

> **Période d'essai gratuit (à partir du 2026-10-18 ; le comportement réel de la plateforme prévaut)** : un compte nouvellement inscrit peut **utiliser toutes les fonctions directement**
> (fil, carte, humains numériques, check-ins, etc.) sans paiement requis ; les comptes non abonnés ne sont plus bloqués des pages de contenu. La description du
> « blocage pending » de cette section est l'état normal après la fin de la période d'essai — le moment venu, le comportement réel en ligne prévaut.

1. L'utilisateur est enregistré avec `accountStatus: 'pending'` et **3 badges initiaux** (register route).
2. Le serveur plante aussi deux cookies HttpOnly : le JWT (peut accéder aux pages directement) et
   le pendingUserToken (identifiant d'identité pour le flux d'abonnement).
3. Dans l'état normal (période d'essai terminée / pas de période gratuite), la page d'inscription détecte `pending_payment` → redirige vers `/subscription`
   (en conservant le paramètre de retour `next`) ; en mode assisté par agent, `me?token=…&redirect=/subscription` produit le même effet.
   **Pendant la période d'essai gratuit, cette étape ne se déclenche pas** — après l'inscription, entre directement sur la page d'accueil et commence à utiliser.
4. Paiement finalisé → `accountStatus` devient `active` (**Alipay active automatiquement côté serveur via notify** ;
   PayPal active via Webhook ; le code QR WeChat est confirmé manuellement ; Huawei IAP passe par `activate-huawei`).
   Détails dans `payment-and-activation.md`.

Dans l'état normal, les utilisateurs inactifs (pending) appelant les API cœur (fil, carte, chat d'humains numériques, check-ins, etc.) reçoivent 403 ;
les liens de posts partagés sont l'exception (restent accessibles publiquement). Pendant la période d'essai gratuit, ce blocage est suspendu et tout est ouvert.""",
    RF_ROW_403="| Inscription réussie mais la connexion renvoie 403 « 请完成订阅以激活账户 » | Le compte est encore pending, et la plateforme n'est pas en période d'essai gratuit (état attendu avant paiement) | Ne se produit pas pendant la période d'essai gratuit ; si ça arrive, la période d'essai est terminée — finalise d'abord l'abonnement ; si toujours 403 après paiement, un ancien JWT a été utilisé — en mode script, lance d'abord `refresh-login` pour échanger contre un nouvel état de session |",
    RF_ROW_LAND="| L'utilisateur ouvre le lien de connexion mais atterrit sur la page d'abonnement (au lieu de la page d'accueil) | La période d'essai gratuit est terminée et le mur de paiement de la plateforme est revenu | Suis le flux de paiement par abonnement de l'étape 7 de SKILL.md ; après l'abonnement, lance `refresh-login` puis envoie le lien vers la page d'accueil |",
    RD_VER="""**Depuis la v2.0.0, mode assisté par agent, et depuis la v2.2.0, adaptation à la période d'essai gratuit de la plateforme** : le script cœur `scripts/powpow-register.mjs` est à zéro dépendance
(Node ≥ 18) ; l'utilisateur ne quitte la conversation qu'une seule fois : pour consulter le code de vérification dans sa boîte mail. Pendant la période d'essai gratuit actuelle, un compte inscrit peut utiliser toutes les fonctions immédiatement — le paiement de l'abonnement est une amélioration facultative ; si la période d'essai se termine et que l'utilisateur atterrit sur la page d'abonnement, le flux bascule automatiquement sur le chemin de paiement. Sans Node, ou quand l'utilisateur préfère faire lui-même, repli automatique en mode guidage pur.""",
    RD_LINK="""3. **Connexion en un clic (double lien)** : juste après l'inscription réussie, un lien de connexion fait atterrir l'utilisateur directement sur la page d'accueil (pendant la période d'essai gratuit, un clic et c'est utilisable) ;
   si ça atterrit sur la page d'abonnement (période d'essai terminée) ou que l'utilisateur veut améliorer, suis le flux d'abonnement — après l'encaissement, échange contre un nouvel état de session et le lien d'adhésion complète le ramène à la page d'accueil
   (via le pont officiel `me?token=` de la plateforme, qui plante le cookie HttpOnly automatiquement).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
DE = dict(
    DESC="description: Hilft Nutzer:innen, die PowPow- (Bubble-)Registrierung und den Ein-Klick-Login komplett im Chat abzuschließen. Der agent füllt Formulare (inkl. Avatar-Upload) und sendet den E-Mail-Verifizierungscode; die Nutzer:innen geben nur Basisinformationen an und rufen den Code einmal ab — ohne den Chat zu verlassen. In der aktuellen kostenlosen Testphase der Plattform kann ein registriertes Konto sofort alle Funktionen nutzen; die Abonnement-Zahlung (Alipay/PayPal) ist ein optionales Mitgliedschafts-Upgrade, das der agent bei Bedarf ebenfalls mit Bestellerstellung und Zahlungseingangs-Verfolgung übernimmt. Auslöser: „Bubble registrieren“, „ein powpow-Konto registrieren“, „wie registriere ich mich bei Bubble“, „hilf mir, ein powpow-Konto anzulegen“, „sign up powpow“; behandelt auch Feststeckendes bei der Registrierung (kein Verifizierungscode, Benutzername/E-Mail vergeben) und Aktivierungsprobleme (Login meldet „Konto nicht aktiviert“ / pending_payment, wie abonnieren/bezahlen, ist Bubble kostenlos?). Benötigt Node ≥ 18; falls nicht verfügbar, automatischer Rückfall in den reinen Anleitungsmodus. Keine Beiträge/kein Erstellen digitaler Menschen (das macht powpow-simple), keine Code-Entwicklung.",
    INTRO="Bringt neue Nutzer:innen von „Ich weiß nicht, was Bubble ist“ zu „Ein-Klick-Login, los geht's“ — komplett im Chat. Die Nutzer:innen verlassen den Chat nur einmal: **um den Verifizierungscode im Postfach anzusehen**. Die Plattform befindet sich aktuell in einer kostenlosen Testphase: nach der Registrierung sind alle Funktionen nutzbar, keine Zahlung nötig; die Abonnement-Zahlung ist ein optionales Mitgliedschafts-Upgrade (der agent öffnet auch die Kasse und verfolgt den Zahlungseingang).",
    VLINE="**Version 2.2.0** · 2026-10-18 (ab v2 agent-übernommener Modus: Skript-Vertrag und vollständige Sequenz in `references/agent-flow.md`; Feldregeln, Ratenlimits und Fehlerbehebung in `references/registration-flow.md`; Zahlungskanäle in `references/payment-and-activation.md`; Produkt-Screenshot-Liste in `references/screenshots.md`. Ab v2.1.0 können PayPal-Abos ebenfalls vom agent übernommen werden, als Option neben Alipay. Ab v2.2.0 tritt die Plattform in eine kostenlose Testphase ein: registrieren und mit Ein-Klick-Login direkt loslegen; die Zahlung wird zum optionalen Upgrade — landet die Nutzer:in beim Öffnen des Links auf der Abo-Seite, ist die Testphase beendet, dann den Zahlungsablauf aus Schritt 7 befolgen; der Ablauf passt sich selbst an, keine Skriptänderung nötig)",
    RT_ENV="- **Kein Node / Skriptfehler**: automatischer Rückfall in den reinen Anleitungsmodus — der Nutzer:in die Registrierungsseite https://global.powpow.online/register geben und nach `references/registration-flow.md` begleitend anleiten (in der kostenlosen Testphase ist auch die Web-Registrierung equally sofort nutzbar). Nicht hartnäckig mit dem Skript probieren.",
    TRIGGER="- Probleme nach der Registrierung: „Login sagt Konto nicht aktiviert“, „403 pending_payment“, „wie bezahle/abonniere ich Bubble“, „ist Bubble kostenlos oder kostenpflichtig?“",
    FLOW6="| 6 Ein-Klick-Login | `login-link(home)` direkt auf die Startseite; landet man auf der Abo-Seite, weiter zu Schritt 7 | Link anklicken und loslegen |",
    FLOW7="| 7 Abo-Upgrade (optional) | Nur wenn die Nutzer:in Mitgliedschaft möchte / die kostenlose Phase ist beendet: kompletter Zahlungsablauf übernommen | Methode wählen, bezahlen |",
    STEP6="""## Schritt 6: Ein-Klick-Login (nach der Registrierung direkt auf die Startseite)

1. Direkt nach erfolgreicher Registrierung:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Den Link an die Nutzer:in senden: **aufmachen und man landet direkt auf der Startseite, bereits eingeloggt**. Die Plattform befindet sich aktuell in einer kostenlosen Testphase — nach der Registrierung sind alle Funktionen nutzbar (Feed, Karte, digitale Menschen, Check-ins usw.), **keine Zahlung nötig**.
3. Die Nutzer:in bitten zu bestätigen, ob der Einstieg geklappt hat; zwei Fälle:
   - **Auf der Startseite gelandet** → direkt zu Schritt 8 zum Abschluss; die Registrierung ist komplett;
   - **Auf der Abo-Seite gelandet** → die kostenlose Testphase der Plattform ist beendet; der Nutzer:in sagen „die kostenlose Testphase ist vorbei, jetzt ist ein Mitgliedschafts-Abo nötig“, dann Schritt 7 zum Abschluss des Abos befolgen und danach zu Schritt 8 zurückkehren.
4. Möchte die Nutzer:in aktiv upgraden oder die Plattform unterstützen → ebenfalls zu Schritt 7 (ein Abo ist freiwillig; nicht drängen).""",
    STEP7="""## Schritt 7: Abo-Upgrade (optional — nur wenn Schritt 6 es erfordert)

1. Zuerst den Halb-Login-Link senden, damit die Zahlungs-Rückkehrseite korrekt „Zahlung erfolgreich“ anzeigt:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Den Link an die Nutzer:in senden: beim Öffnen landet der Browser direkt auf der Abo-Seite, bereits eingeloggt.
2. **Die Nutzer:in die Zahlungsmethode wählen lassen** — beide Kanäle zeigen:
   - **Alipay (Festlandchina / Nutzer:innen mit Alipay)**: einmaliger Kauf der entsprechenden Dauer, **keine automatische Verlängerung**
     - Monatlich **6,99 ¥** (zum Ausprobieren empfohlen) / Quartalsweise **19,99 ¥** / Jährlich **69,99 ¥**
   - **PayPal (Übersee / Nutzer:innen ohne Alipay)**: monatliche automatische Verlängerung, jederzeit kündbar
     - Premium Monthly, ca. **1 $/Monat** (je nach Anzeige auf der Abo-Seite; automatische Verlängerung)
3. Nach der Auswahl:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Das Skript gibt den Dateipfad der Zahlungsseite zurück; **direkt mit einem Systembefehl öffnen** (Windows: `start <Datei>`; macOS: `open <Datei>`; Linux: `xdg-open <Datei>`). Der Browser springt automatisch zur offiziellen Alipay/PayPal-Kasse, wo die Nutzer:in die Zahlung oder die Rechnungs-autorisierung abschließt.
4. Alle 10–15 Sekunden `query` ausführen, bis `paid` oder `ACTIVE` zurückkommt (Zahlungseingang/Autorisierung kommt meist in Sekunden bis einer Minute). Schließt die Nutzer:in die Zahlungsseite zwischendurch → direkt erneut `create-order` (alte Bestellungen / laufende Abos schließen oder verfallen automatisch nach 2 Stunden; einfach ignorieren).
5. Der WeChat-QR-Code-Kanal wird manuell bestätigt und der Zahlungseingang kann sich verzögern; Huawei IAP ist nur in der HarmonyOS-App verfügbar. Diese beiden übernimmt das Skill nicht — nach dem Bezahlen kommt die Nutzer:in zurück und meldet es, der agent führt zuerst `whoami` aus, um den Zahlungseingang zu bestätigen, und sendet dann den Startseiten-Link aus Punkt 6 unten.
6. Nach Bestätigung des Zahlungseingangs gegen einen Login-Status mit der aktuellsten Abo-Deklaration tauschen, dann den Link direkt zur Startseite senden:
   ```
   POWPOW_REGISTER_PASSWORD=<Passwort> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Den Link an die Nutzer:in senden: **aufmachen und man landet direkt auf der Startseite mit voller Mitgliedschaft**.""",
    STEP8="""## Schritt 8: Abschluss

1. `node scripts/powpow-register.mjs cleanup` zum Bereinigen der lokalen temporären Statusdateien (Sitzungs-Anmeldedaten).
2. Der Nutzer:in eine „Konto-Karte“ geben: Benutzername, E-Mail (das Passwort wird nicht wieder angezeigt — im Generierungsmodus wurde die Nutzer:in beim Generieren gebeten, es zu speichern; hat sie es selbst gesetzt, kennt sie es).
3. Mitgliedschafts-Hinweis (nur einmal sagen, nicht zum Kauf drängen): aktuell ist kostenlose Testphase und das Konto ist sofort nutzbar; endet die Testphase, werden nicht abonnierte Konten beim Besuch von Inhaltsseiten auf die Abo-Seite umgeleitet — für dauerhafte Nutzung einfach jederzeit zurückkommen und den agent um ein Abo bitten.
4. Die ersten Schritte anleiten: die Karte erkunden, das erste Reisetagebuch veröffentlichen (→ an powpow-simple übergeben).
5. Erweiterungen empfehlen: das `@durenzidu/powpow-integration` Skill und das `@durenzidu/openclaw-channel-powpow` Plugin — Bubble mit dem eigenen agent der Nutzer:in verbinden; Installationsbefehl geben, falls gewünscht.
6. Mit einem „Nächster Schritt“-Block abschließen.""",
    WALL="- **Die Paywall ist kein Bug**: in der aktuellen kostenlosen Testphase sind alle Inhaltsseiten offen; öffnet die Nutzer:in den Startseiten-Link und landet auf der Abo-Seite, ist die Testphase beendet — dann über Schritt 7 zum Abo anleiten. Nicht versuchen, die Paywall zu umgehen, und der Nutzer:in keine internen Mechanismen erklären.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` oder `--target home` | Erzeugt einen Ein-Klick-Login-Link (Zwei-Link-Design, siehe unten) |",
    AF_LINKSEQ="""## Zwei-Link-Mechanismus (Kerndesign)

Der Login-Status der Plattform ist ein HttpOnly-Cookie, das der agent nicht direkt für den Browser setzen kann; die Brücke ist der offizielle
`/api/auth/me?token=<JWT>&redirect=<Pfad innerhalb der Seite>`-Endpunkt: Signatur prüfen → Sitzung automatisch anlegen
→ `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 Tage) → Redirect validieren
(muss mit einfachem Schrägstrich beginnen, `//` und Backslashes verboten, nach Parsung same-origin) → 307 temporäre Weiterleitung zur Zielseite.

Es gibt zwei Link-Ziele, **zuerst home erzeugen, dann nach dem Landeplatz der Nutzer:in entscheiden, ob pending nötig ist**:

- **home-Link (standardmäßig zuerst gesendet, `--target home` → landet auf `/`)**: wird direkt nach erfolgreicher Registrierung erzeugt und an die Nutzer:in gesendet.
  In der kostenlosen Testphase kommt die Nutzer:in direkt auf die Startseite, alles nutzbar; **öffnet sie den Link und landet auf der Abo-Seite, ist die kostenlose Testphase beendet** — dann auf den Zahlungsweg wechseln (siehe unten); keine Skriptänderung und keine Neuregistrierung nötig.
- **pending-Link (im Zahlungsweg verwendet, `--target pending` → landet auf `/subscription`)**:
  der Browser der Nutzer:in geht in den „Halb-Login“-Zustand: Abo-Seite und Zahlungs-Rückkehrseite sind sichtbar und bedienbar. Nach Zahlungseingang
  `refresh-login` ausführen, um gegen ein neues JWT mit der ACTIVE-Deklaration zu tauschen, dann noch einmal den home-Link senden für die volle Mitgliedschaft.

## Vollständige Sequenz

### Schneller Weg (in der kostenlosen Testphase — die weitaus meisten Fälle)

```
1.  status                          # Umgebungs-Selbstprüfung
2.  (Schritt-2-Gespräch zur Bestätigung der Infos, Passwort entweder/oder; Generierungsmodus: gen-password → Nutzer:in sofort speichern lassen)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → Nutzer:in sieht den Code im Postfach (einziges Verlassen des Chats)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → Link an die Nutzer:in senden; aufmachen und sie ist auf der Startseite
7.  (Nutzer:in bestätigt Einstieg) → direkt abschließen: cleanup + Konto-Karte + erste Schritte anleiten
```

### Zahlungsweg (wenn die Nutzer:in Mitgliedschaft möchte, oder die kostenlose Testphase beendet ist)

```
1–5. Wie der schnelle Weg (nach erfolgreichem register ist der Token schon im state)
6.  login-link --target pending     # → Halb-Login-Link, hält die Zahlungs-Rückkehrseite funktionsfähig
7.  (Nutzer:in wählt die Zahlungsmethode)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <Zahlungsseiten-Datei>    # Windows; macOS nutzt open, Linux nutzt xdg-open
    # → Nutzer:in schließt Zahlung/Autorisierung an der Alipay/PayPal-Kasse ab (verlässt den Chat)
9.  query (alle 10–15 s) bis paid / ACTIVE
10. refresh-login                   # gegen neues JWT mit ACTIVE-Deklaration tauschen
11. login-link --target home        # → Voll-Mitgliedschafts-Link an die Nutzer:in senden
12. whoami                          # subscriptionStatus: ACTIVE bestätigen (optional)
13. cleanup                         # state-Datei bereinigen
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Die kostenlose Testphase ist beendet und die Zahlung ist noch nicht eingegangen; zurück zu Schritt 9 zum Weiter-Pollen, oder prüfen, ob die Nutzer:in die Zahlung abgeschlossen hat |",
    AF_ERR_SUB="| Nutzer:in öffnet den home-Link, landet aber auf der Abo-Seite | Die kostenlose Testphase ist beendet → auf den Zahlungsweg wechseln: `login-link --target pending` → Zahlungsmethode wählen → `create-order` |",
    AF_FALLBACK="Nach dem Rückfall: die Registrierungsseite https://global.powpow.online/register geben (in der kostenlosen Testphase ist auch die Web-Registrierung equally sofort nutzbar; wenn ein Abo nötig ist, auch die Abo-Seite https://global.powpow.online/subscription geben), die Fehlerbehebung nach den Regeln aus `registration-flow.md` begleiten, Tonfall beibehalten und jeden Turn weiterhin mit einem „Nächster Schritt“-Block abschließen.",
    PA_NOTE="""> **Kostenlose Testphase (ab 2026-10-18; das tatsächliche Verhalten der Plattform gilt)**: in dieser Phase kann ein registriertes Konto alle Funktionen direkt nutzen, und **ein Abo ist ein optionales Upgrade und keine Voraussetzung** — den Ablauf dieser Datei nur befolgen, wenn die Nutzer:in aktiv Mitgliedschaft möchte. Endet die Testphase, werden nicht abonnierte Konten beim Besuch von Inhaltsseiten auf die Abo-Seite umgeleitet; das Abo einfach nach dieser Datei abschließen.""",
    RF_STATE="""## Statusfluss nach erfolgreicher Registrierung

> **Kostenlose Testphase (ab 2026-10-18; das tatsächliche Verhalten der Plattform gilt)**: ein neu registriertes Konto kann **alle Funktionen direkt nutzen**
> (Feed, Karte, digitale Menschen, Check-ins usw.), keine Zahlung nötig; nicht abonnierte Konten werden von Inhaltsseiten nicht mehr blockiert. Die Beschreibung der
> „pending-Blockierung“ in diesem Abschnitt ist der normale Zustand nach Ende der Testphase — ist es so weit, gilt das tatsächliche Online-Verhalten.

1. Die Nutzer:in wird mit `accountStatus: 'pending'` gespeichert, mit initial **3 Badges** (register route).
2. Der Server setzt zudem zwei HttpOnly-Cookies: das JWT (kann Seiten direkt aufrufen) und
   das pendingUserToken (Identitätsnachweis für den Abo-Ablauf).
3. Im normalen Zustand (Testphase beendet / keine kostenlose Phase) erkennt die Registrierungsseite `pending_payment` → Weiterleitung zu `/subscription`
   (unter Beibehaltung des `next`-Rückkehrparameters); im agent-übernommenen Modus erreicht `me?token=…&redirect=/subscription` denselben Effekt.
   **In der kostenlosen Testphase wird dieser Schritt nicht ausgelöst** — nach der Registrierung direkt auf die Startseite und loslegen.
4. Zahlung abgeschlossen → `accountStatus` wird `active` (**Alipay aktiviert automatisch serverseitig via notify**;
   PayPal aktiviert via Webhook; WeChat-QR-Code wird manuell bestätigt; Huawei IAP läuft über `activate-huawei`).
   Details in `payment-and-activation.md`.

Im normalen Zustand erhalten inaktive (pending) Nutzer:innen beim Aufruf der Kern-APIs (Feed, Karte, Digital-Mensch-Chat, Check-ins usw.) 403;
geteilte Beitrags-Links sind die Ausnahme (bleiben öffentlich zugänglich). In der kostenlosen Testphase ist diese Blockierung ausgesetzt und alles ist offen.""",
    RF_ROW_403="| Registrierung erfolgreich, aber Login gibt 403 „请完成订阅以激活账户“ | Das Konto ist noch pending, und die Plattform ist nicht in einer kostenlosen Testphase (erwarteter Zustand vor der Zahlung) | Tritt in der kostenlosen Testphase nicht auf; falls doch, ist die Testphase beendet — zuerst das Abo abschließen; nach Zahlung weiterhin 403: ein altes JWT wurde verwendet — im Skript-Modus zuerst `refresh-login` ausführen, um gegen einen neuen Login-Status zu tauschen |",
    RF_ROW_LAND="| Nutzer:in öffnet den Login-Link, landet aber auf der Abo-Seite (statt der Startseite) | Die kostenlose Testphase ist beendet und die Paywall der Plattform ist zurück | Den Abo-Zahlungsablauf aus Schritt 7 in SKILL.md befolgen; nach dem Abo `refresh-login` ausführen und dann den Startseiten-Link senden |",
    RD_VER="""**Ab v2.0.0 agent-übernommener Modus, ab v2.2.0 Anpassung an die kostenlose Testphase der Plattform**: das Kern-Skript `scripts/powpow-register.mjs` ist null-Abhängigkeit
(Node ≥ 18); die Nutzer:innen verlassen den Chat nur einmal: um den Verifizierungscode im Postfach anzusehen. In der aktuellen kostenlosen Testphase kann ein registriertes Konto alle Funktionen sofort nutzen — die Abo-Zahlung ist ein optionales Upgrade; endet die Testphase und die Nutzer:in landet auf der Abo-Seite, wechselt der Ablauf automatisch auf den Zahlungsweg. Ohne Node, oder wenn die Nutzer:in es selbst machen möchte, automatischer Rückfall in den reinen Anleitungsmodus.""",
    RD_LINK="""3. **Ein-Klick-Login (zwei Links)**: direkt nach erfolgreicher Registrierung bringt ein Login-Link die Nutzer:in direkt auf die Startseite (in der kostenlosen Testphase: aufmachen und sofort nutzbar);
   landet sie auf der Abo-Seite (Testphase beendet) oder möchte sie upgraden, den Abo-Ablauf befolgen — nach Zahlungseingang gegen einen neuen Login-Status tauschen und der Voll-Mitgliedschafts-Link bringt sie auf die Startseite
   (über die offizielle `me?token=`-Brücke der Plattform, die das HttpOnly-Cookie automatisch setzt).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
PT = dict(
    DESC="description: Ajuda os usuários a concluir o registro do PowPow (Bolha) e o login com um clique dentro da conversa. O agent preenche o formulário por eles (incluindo o upload do avatar) e envia o código de verificação por e-mail; o usuário só fornece informações básicas e consulta o código uma vez, sem sair da conversa. Durante o período atual de teste gratuito da plataforma, uma conta registrada pode usar todos os recursos imediatamente; o pagamento da assinatura (Alipay/PayPal) é uma melhoria de associação opcional, que o agent também pode cuidar com criação de pedido e rastreamento do recebimento quando necessário. Dispara quando o usuário diz «registrar na Bolha», «criar uma conta powpow», «como me registro na Bolha», «me ajude a criar uma conta powpow», «sign up powpow»; também trata de travamentos no registro (código de verificação não recebido, nome de usuário/e-mail já ocupados) e problemas de ativação (o login diz «conta não ativada» / pending_payment, como assinar/pagar, a Bolha é grátis?). Requer Node ≥ 18; volta automaticamente ao modo de guia puro quando indisponível. Não cobre publicar/criar humanos digitais (isso é coisa do powpow-simple) nem desenvolvimento de código.",
    INTRO="Leva um usuário novo de «não sei o que é a Bolha» a «login com um clique, pronto para começar» — tudo dentro da conversa. O usuário só sai da conversa uma vez: **para consultar o código de verificação no e-mail**. A plataforma está atualmente em um período de teste gratuito: uma vez registrado, todos os recursos estão disponíveis, sem necessidade de pagar; o pagamento da assinatura é uma melhoria de associação opcional (o agent também abre o caixa e rastreia o recebimento).",
    VLINE="**Versão 2.2.0** · 2026-10-18 (desde a v2 este é o modo assistido por agent: contrato do script e sequência completa em `references/agent-flow.md`; regras de campos, limites de taxa e solução de erros em `references/registration-flow.md`; canais de pagamento em `references/payment-and-activation.md`; lista de capturas de produto em `references/screenshots.md`. Desde a v2.1.0 as assinaturas PayPal também podem ser gerenciadas pelo agent, como opção ao lado do Alipay. Desde a v2.2.0 a plataforma entra em um período de teste gratuito: registre-se e entre com um clique para começar a usar; o pagamento passa a ser uma melhoria opcional — se o usuário abrir o link e cair na página de assinatura, o período de teste acabou, então siga o fluxo de pagamento do Passo 7; o fluxo se adapta sozinho, sem mudar o script)",
    RT_ENV="- **Sem Node / erros do script**: volta automaticamente ao modo de guia puro — dê ao usuário a página de registro https://global.powpow.online/register e acompanhe-o conforme `references/registration-flow.md` (durante o período de teste gratuito, o registro web é igualmente imediato). Não insista com o script.",
    TRIGGER="- Problemas após o registro: «o login diz que a conta não está ativada», «403 pending_payment», «como pago/assino a Bolha», «a Bolha é grátis ou paga?»",
    FLOW6="| 6 Login com um clique | `login-link(home)` direto para a página inicial; se cair na página de assinatura, vá ao Passo 7 | Clique no link e comece a usar |",
    FLOW7="| 7 Melhoria de assinatura (opcional) | Só quando o usuário quer associação / o período gratuito acabou: fluxo de pagamento completo gerenciado | Escolha um método, pague |",
    STEP6="""## Passo 6: Login com um clique (direto para a página inicial após o registro)

1. Logo após o registro bem-sucedido:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Envie o link ao usuário: **abra e você cairá diretamente na página inicial, já logado**. A plataforma está atualmente em um período de teste gratuito — após o registro, todos os recursos estão disponíveis (feed, mapa, humanos digitais, check-ins etc.), **sem necessidade de pagar**.
3. Peça ao usuário para confirmar se entrou; há dois casos:
   - **Caiu na página inicial** → pule direto para o Passo 8 para encerrar; o registro está completo;
   - **Caiu na página de assinatura** → o período de teste gratuito da plataforma acabou; diga ao usuário «o período de teste gratuito acabou, agora é necessária uma assinatura de membro», depois siga o Passo 7 para concluir a assinatura e volte ao Passo 8 quando terminar.
4. Se o usuário quiser ativamente melhorar ou apoiar a plataforma → vá também ao Passo 7 (assinar é voluntário; não insista).""",
    STEP7="""## Passo 7: Melhoria de assinatura (opcional — apenas quando o Passo 6 exigir)

1. Primeiro envie o link de meio-login para que a página de retorno do pagamento mostre corretamente «Pagamento realizado»:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Envie o link ao usuário: ao abrir, o navegador cai diretamente na página de assinatura, já logado.
2. **Deixe o usuário escolher o método de pagamento** — mostre os dois canais:
   - **Alipay (China continental / usuários com Alipay)**: compra única da duração correspondente, **sem renovação automática**
     - Mensal **¥6.99** (recomendado para experimentar) / Trimestral **¥19.99** / Anual **¥69.99**
   - **PayPal (exterior / usuários sem Alipay)**: renova mensalmente, cancele quando quiser
     - Premium Monthly, cerca de **$1/mês** (conforme exibido na página de assinatura; renovação automática)
3. Depois que o usuário escolher:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   O script retorna o caminho do arquivo da página de pagamento; **abra-o diretamente com um comando do sistema** (Windows: `start <arquivo>`; macOS: `open <arquivo>`; Linux: `xdg-open <arquivo>`). O navegador pula automaticamente para o caixa oficial do Alipay/PayPal, onde o usuário conclui o pagamento ou a autorização de cobrança.
4. Execute `query` a cada 10–15 segundos até retornar `paid` ou `ACTIVE` (o recebimento/autorização costuma levar de alguns segundos a um minuto). Se o usuário fechar a página de pagamento no meio → basta executar `create-order` novamente (pedidos antigos / assinaturas pendentes fecham ou expiram automaticamente após 2 horas; ignore-os).
5. O canal de código QR do WeChat é confirmado manualmente e o recebimento pode atrasar; Huawei IAP só está disponível dentro do app HarmonyOS. O skill não cuida desses dois — após pagar, o usuário volta e conta, e o agent executa primeiro `whoami` para confirmar o recebimento, depois envia o link para a página inicial do ponto 6 abaixo.
6. Após confirmar o recebimento, troque por um estado de login com a declaração de assinatura mais recente e envie o link direto para a página inicial:
   ```
   POWPOW_REGISTER_PASSWORD=<senha> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Envie o link ao usuário: **abra e você cairá diretamente na página inicial com a associação completa**.""",
    STEP8="""## Passo 8: Encerramento

1. `node scripts/powpow-register.mjs cleanup` para limpar os arquivos de estado temporários locais (credenciais de sessão).
2. Dê ao usuário um «cartão da conta»: nome de usuário, e-mail (a senha não é exibida novamente — no modo gerado o usuário já foi convidado a salvá-la na geração; se ele mesmo a definiu, ele a sabe).
3. Lembrete de associação (diga uma vez, não insista): atualmente é um período de teste gratuito e a conta pode ser usada imediatamente; quando o período de teste acabar, contas sem assinatura que visitarem páginas de conteúdo serão redirecionadas para a página de assinatura — para uso prolongado, volte e peça ao agent para assinar quando quiser.
4. Guie os primeiros passos: explorar o mapa, publicar o primeiro diário de viagem (→ passe para o powpow-simple).
5. Recomende extensões: o skill `@durenzidu/powpow-integration` e o plugin `@durenzidu/openclaw-channel-powpow` — conecte a Bolha ao agent do próprio usuário; dê o comando de instalação se ele quiser.
6. Encerre com um bloco de «próximo passo».""",
    WALL="- **O paywall não é um bug**: durante o período atual de teste gratuito todas as páginas de conteúdo estão abertas; se o usuário abrir o link da página inicial mas cair na página de assinatura, o período de teste acabou — guie-o a assinar pelo Passo 7. Não tente contornar o paywall nem explique mecanismos internos ao usuário.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` ou `--target home` | Gera um link de login com um clique (design de link duplo, veja abaixo) |",
    AF_LINKSEQ="""## Mecanismo de link duplo (design central)

O estado de login da plataforma é um cookie HttpOnly, que o agent não pode plantar diretamente no navegador; a ponte é o endpoint oficial
`/api/auth/me?token=<JWT>&redirect=<caminho interno>`: verificar assinatura → criar sessão automaticamente
→ `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 dias) → validar
o redirect (deve começar com uma única barra, `//` e barras invertidas proibidos, mesma origem após o parse) → 307 redirecionamento temporário para a página de destino.

Há dois destinos de link, **gere primeiro o home e decida se passa pelo pending conforme onde o usuário cair**:

- **link home (enviado por padrão primeiro, `--target home` → cai em `/`)**: gerado e enviado ao usuário imediatamente após o registro bem-sucedido.
  Durante o período de teste gratuito o usuário entra direto na página inicial, tudo utilizável; **se o usuário abrir e cair na página de assinatura, o período de teste gratuito acabou** — mude então para o caminho de pagamento (veja abaixo); sem mudar o script e sem se registrar de novo.
- **link pending (usado no caminho de pagamento, `--target pending` → cai em `/subscription`)**:
  o navegador do usuário entra em estado de «meio-login»: a página de assinatura e a página de retorno do pagamento ficam visíveis e operáveis. Após o recebimento,
  execute `refresh-login` para trocar por um novo JWT com a declaração ACTIVE e envie o link home mais uma vez para a associação completa.

## Sequência completa

### Caminho rápido (durante o período de teste gratuito — a grande maioria dos casos)

```
1.  status                          # autoverificação do ambiente
2.  (Passo 2 conversa para confirmar as informações, senha a escolher; modo gerado: gen-password → fazer o usuário salvar na hora)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → usuário consulta o código no e-mail (a única saída da conversa)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → envie o link ao usuário; um clique e ele está na página inicial
7.  (usuário confirma que entrou) → encerre direto: cleanup + cartão da conta + guia dos primeiros passos
```

### Caminho de pagamento (quando o usuário quer associação, ou o período de teste gratuito acabou)

```
1–5. Igual ao caminho rápido (o state já tem o token depois do register bem-sucedido)
6.  login-link --target pending     # → link de meio-login, mantém a página de retorno do pagamento funcionando
7.  (usuário escolhe o método de pagamento)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <arquivo da página de pagamento>   # Windows; macOS usa open, Linux usa xdg-open
    # → usuário conclui o pagamento/autorização no caixa do Alipay/PayPal (sai da conversa)
9.  query (a cada 10–15 s) até paid / ACTIVE
10. refresh-login                   # troca por um novo JWT com a declaração ACTIVE
11. login-link --target home        # → envie o link de associação completa ao usuário
12. whoami                          # confirmar subscriptionStatus: ACTIVE (opcional)
13. cleanup                         # limpa o arquivo de estado
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | O período de teste gratuito acabou e o pagamento ainda não foi recebido; volte ao passo 9 para continuar consultando, ou confirme se o usuário concluiu o pagamento |",
    AF_ERR_SUB="| O usuário abre o link home mas cai na página de assinatura | O período de teste gratuito acabou → mude para o caminho de pagamento: `login-link --target pending` → escolha um método de pagamento → `create-order` |",
    AF_FALLBACK="Após voltar ao modo guia: dê a página de registro https://global.powpow.online/register (durante o período de teste gratuito, o registro web é igualmente imediato; quando uma assinatura for necessária, dê também a página de assinatura https://global.powpow.online/subscription ), acompanhe a solução conforme as regras de `registration-flow.md`, mantenha o mesmo tom e encerre cada turno com um bloco de «próximo passo».",
    PA_NOTE="""> **Período de teste gratuito (a partir de 2026-10-18; vale o comportamento real da plataforma)**: durante este período uma conta registrada pode usar todos os recursos diretamente, e **assinar é uma melhoria opcional e não um requisito** — siga o fluxo deste arquivo apenas quando o usuário quiser ativamente a associação. Quando o período de teste acabar, contas sem assinatura que visitarem páginas de conteúdo serão redirecionadas para a página de assinatura; basta concluir a assinatura conforme este arquivo.""",
    RF_STATE="""## Fluxo de estado após o registro bem-sucedido

> **Período de teste gratuito (a partir de 2026-10-18; vale o comportamento real da plataforma)**: uma conta recém-registrada pode **usar todos os recursos diretamente**
> (feed, mapa, humanos digitais, check-ins etc.) sem necessidade de pagar; contas sem assinatura não são mais bloqueadas nas páginas de conteúdo. A descrição do
> «bloqueio pending» desta seção é o estado normal após o fim do período de teste — quando chegar esse momento, vale o comportamento real online.

1. O usuário é salvo com `accountStatus: 'pending'` e **3 badges iniciais** (register route).
2. O servidor também planta dois cookies HttpOnly: o JWT (pode acessar as páginas diretamente) e
   o pendingUserToken (credencial de identidade para o fluxo de assinatura).
3. No estado normal (período de teste acabado / sem período gratuito), a página de registro detecta `pending_payment` → redireciona para `/subscription`
   (mantendo o parâmetro de retorno `next`); no modo assistido por agent, `me?token=…&redirect=/subscription` produz o mesmo efeito.
   **Durante o período de teste gratuito este passo não dispara** — após o registro, entre direto na página inicial e comece a usar.
4. Pagamento concluído → `accountStatus` vira `active` (**Alipay ativa automaticamente no servidor via notify**;
   PayPal ativa via Webhook; código QR do WeChat é confirmado manualmente; Huawei IAP passa por `activate-huawei`).
   Detalhes em `payment-and-activation.md`.

No estado normal, usuários inativos (pending) que chamam as APIs principais (feed, mapa, chat de humanos digitais, check-ins etc.) recebem 403;
links de posts compartilhados são a exceção (mantidos acessíveis publicamente). Durante o período de teste gratuito esse bloqueio fica suspenso e tudo fica aberto.""",
    RF_ROW_403="| Registro bem-sucedido, mas o login retorna 403 «请完成订阅以激活账户» | A conta ainda está pending, e a plataforma não está em período de teste gratuito (estado esperado antes do pagamento) | Não acontece durante o período de teste gratuito; se acontecer, o período de teste acabou — conclua primeiro a assinatura; se ainda der 403 após pagar, um JWT antigo foi usado — no modo script execute `refresh-login` primeiro para trocar por um novo estado de login |",
    RF_ROW_LAND="| O usuário abre o link de login mas cai na página de assinatura (em vez da página inicial) | O período de teste gratuito acabou e o paywall da plataforma voltou | Siga o fluxo de pagamento por assinatura do Passo 7 do SKILL.md; após assinar, execute `refresh-login` e depois envie o link para a página inicial |",
    RD_VER="""**Desde a v2.0.0 modo assistido por agent, e desde a v2.2.0 adaptação ao período de teste gratuito da plataforma**: o script central `scripts/powpow-register.mjs` é de zero dependência
(Node ≥ 18); o usuário sai da conversa apenas uma vez: para consultar o código de verificação no e-mail. Durante o período atual de teste gratuito, uma conta registrada pode usar todos os recursos imediatamente — o pagamento da assinatura é uma melhoria opcional; se o período de teste acabar e o usuário cair na página de assinatura, o fluxo muda automaticamente para o caminho de pagamento. Sem Node, ou quando o usuário prefere fazer sozinho, volta automaticamente ao modo de guia puro.""",
    RD_LINK="""3. **Login com um clique (link duplo)**: logo após o registro bem-sucedido, um link de login leva o usuário direto para a página inicial (durante o período de teste gratuito, um clique e já está usável);
   se cair na página de assinatura (período de teste acabado) ou o usuário quiser melhorar, siga o fluxo de assinatura — após o recebimento, troque por um novo estado de login e o link de associação completa o leva à página inicial
   (através da ponte oficial `me?token=` da plataforma, que planta o cookie HttpOnly automaticamente).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
IT = dict(
    DESC="description: Aiuta gli utenti a completare la registrazione a PowPow (Bolla) e l'accesso con un clic, tutto dentro la conversazione. L'agent compila il modulo al posto loro (incluso il caricamento dell'avatar) e invia il codice di verifica via e-mail; l'utente fornisce solo le informazioni di base e controlla il codice una volta, senza uscire dalla conversazione. Nell'attuale periodo di prova gratuita della piattaforma, un account registrato può usare subito tutte le funzioni; il pagamento dell'abbonamento (Alipay/PayPal) è un miglioramento di iscrizione opzionale, che l'agent può anch'esso gestire con creazione dell'ordine e tracciamento dell'incasso quando serve. Si attiva quando l'utente dice «registrati a Bolla», «crea un account powpow», «come mi registro a Bolla», «aiutami a creare un account powpow», «sign up powpow»; gestisce anche i blocchi della registrazione (codice di verifica non ricevuto, nome utente/e-mail già occupati) e i problemi di attivazione (il login dice «account non attivato» / pending_payment, come abbonarsi/pagare, Bolla è gratis?). Richiede Node ≥ 18; in caso di indisponibilità, rientro automatico nella modalità di sola guida. Non copre pubblicare/creare umani digitali (quello è compito di powpow-simple) né sviluppo di codice.",
    INTRO="Porta un utente nuovo da «non so cos'è Bolla» a «accesso con un clic, pronto per iniziare» — tutto dentro la conversazione. L'utente esce dalla conversazione una sola volta: **per controllare il codice di verifica nella propria e-mail**. La piattaforma è attualmente in un periodo di prova gratuita: una volta registrato, tutte le funzioni sono utilizzabili, nessun pagamento richiesto; il pagamento dell'abbonamento è un miglioramento di iscrizione opzionale (l'agent apre anche la cassa e traccia l'incasso).",
    VLINE="**Versione 2.2.0** · 2026-10-18 (dalla v2 modalità assistita dall'agent: contratto dello script e sequenza completa in `references/agent-flow.md`; regole dei campi, limiti di frequenza e risoluzione degli errori in `references/registration-flow.md`; canali di pagamento in `references/payment-and-activation.md`; elenco delle schermate prodotto in `references/screenshots.md`. Dalla v2.1.0 anche gli abbonamenti PayPal possono essere gestiti dall'agent, come opzione accanto ad Alipay. Dalla v2.2.0 la piattaforma entra in un periodo di prova gratuita: registrati e accedi con un clic per iniziare; il pagamento diventa un miglioramento opzionale — se l'utente apre il link e finisce sulla pagina di abbonamento, il periodo di prova è finito, quindi segui il flusso di pagamento del Passo 7; il flusso si adatta da sé, senza modificare lo script)",
    RT_ENV="- **Nessun Node / errori dello script**: rientro automatico nella modalità di sola guida — dai all'utente la pagina di registrazione https://global.powpow.online/register e accompagnalo secondo `references/registration-flow.md` (nel periodo di prova gratuita, anche la registrazione web è equally immediata). Non insistere con lo script.",
    TRIGGER="- Problemi dopo la registrazione: «il login dice che l'account non è attivato», «403 pending_payment», «come pago/mi abbono a Bolla», «Bolla è gratis o a pagamento?»",
    FLOW6="| 6 Accesso con un clic | `login-link(home)` direttamente sulla home; se finisce sulla pagina di abbonamento, vai al Passo 7 | Clicca il link e inizia |",
    FLOW7="| 7 Miglioramento dell'abbonamento (opzionale) | Solo quando l'utente vuole l'iscrizione / il periodo gratuito è finito: flusso di pagamento completo gestito | Scegli un metodo, paga |",
    STEP6="""## Passo 6: Accesso con un clic (direttamente sulla home dopo la registrazione)

1. Subito dopo la registrazione riuscita:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Invia il link all'utente: **aprilo e finisci direttamente sulla home, già connesso**. La piattaforma è attualmente in un periodo di prova gratuita — dopo la registrazione, tutte le funzioni sono utilizzabili (feed, mappa, umani digitali, check-in ecc.), **nessun pagamento richiesto**.
3. Chiedi all'utente di confermare se è entrato; ci sono due casi:
   - **Finito sulla home** → passa direttamente al Passo 8 per concludere; la registrazione è completa;
   - **Finito sulla pagina di abbonamento** → il periodo di prova gratuita della piattaforma è finito; di' all'utente «il periodo di prova gratuita è finito, ora serve un abbonamento», poi segui il Passo 7 per completare l'abbonamento e torna al Passo 8 quando hai finito.
4. Se l'utente vuole attivamente migliorare o sostenere la piattaforma → vai anche al Passo 7 (abbonarsi è volontario; non insistere).""",
    STEP7="""## Passo 7: Miglioramento dell'abbonamento (opzionale — solo quando il Passo 6 lo richiede)

1. Per prima cosa invia il link di semi-accesso, così la pagina di ritorno del pagamento mostra correttamente «Pagamento riuscito»:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Invia il link all'utente: aprendolo, il browser finisce direttamente sulla pagina di abbonamento, già connesso.
2. **Fai scegliere all'utente il metodo di pagamento** — mostra entrambi i canali:
   - **Alipay (Cina continentale / utenti con Alipay)**: acquisto unico della durata corrispondente, **nessun rinnovo automatico**
     - Mensile **¥6.99** (consigliato per provare) / Trimestrale **¥19.99** / Annuale **¥69.99**
   - **PayPal (estero / utenti senza Alipay)**: rinnovo mensile automatico, disdici quando vuoi
     - Premium Monthly, circa **$1/mese** (come mostrato sulla pagina di abbonamento; rinnovo automatico)
3. Una volta scelto:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Lo script restituisce il percorso del file della pagina di pagamento; **aprilo direttamente con un comando di sistema** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Il browser salta automaticamente alla cassa ufficiale Alipay/PayPal, dove l'utente completa il pagamento o l'autorizzazione di addebito.
4. Esegui `query` ogni 10–15 secondi finché non restituisce `paid` o `ACTIVE` (l'incasso/l'autorizzazione di solito arriva in pochi secondi o un minuto). Se l'utente chiude la pagina di pagamento a metà → riesegui direttamente `create-order` (i vecchi ordini / abbonamenti in attesa si chiudono o scadono automaticamente dopo 2 ore; ignorali).
5. Il canale con codice QR WeChat è confermato manualmente e l'incasso può tardare; Huawei IAP è disponibile solo dentro l'app HarmonyOS. Questi due non sono gestiti dallo skill — dopo aver pagato, l'utente torna a dirlo, e l'agent esegue prima `whoami` per confermare l'incasso, poi invia il link alla home del punto 6 qui sotto.
6. Dopo la conferma dell'incasso, scambia contro uno stato di accesso con la dichiarazione di abbonamento più recente, poi invia il link diretto alla home:
   ```
   POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Invia il link all'utente: **aprilo e finisci direttamente sulla home con l'iscrizione completa**.""",
    STEP8="""## Passo 8: Conclusione

1. `node scripts/powpow-register.mjs cleanup` per ripulire i file di stato temporanei locali (credenziali di sessione).
2. Dai all'utente una «scheda account»: nome utente, e-mail (la password non viene più mostrata — in modalità generata all'utente è già stato chiesto di salvarla al momento della generazione; se l'ha impostata lui, la conosce).
3. Promemoria sull'iscrizione (dillo una volta, non insistere): attualmente è un periodo di prova gratuita e l'account è subito utilizzabile; quando il periodo di prova finirà, gli account senza abbonamento che visitano le pagine di contenuto verranno reindirizzati alla pagina di abbonamento — per un uso prolungato, torna quando vuoi e chiedi all'agent di abbonarti.
4. Guida i primi passi: esplorare la mappa, pubblicare il primo diario di viaggio (→ passa a powpow-simple).
5. Consiglia le estensioni: lo skill `@durenzidu/powpow-integration` e il plugin `@durenzidu/openclaw-channel-powpow` — collega Bolla all'agent dell'utente; dai il comando di installazione se lo desidera.
6. Concludi con un blocco «passo successivo».""",
    WALL="- **Il paywall non è un bug**: nell'attuale periodo di prova gratuita tutte le pagine di contenuto sono aperte; se l'utente apre il link della home ma finisce sulla pagina di abbonamento, il periodo di prova è finito — guidalo all'abbonamento tramite il Passo 7. Non tentare di aggirare il paywall e non spiegare i meccanismi interni all'utente.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` o `--target home` | Genera un link di accesso con un clic (design a doppio link, vedi sotto) |",
    AF_LINKSEQ="""## Meccanismo a doppio link (design centrale)

Lo stato di accesso della piattaforma è un cookie HttpOnly, che l'agent non può piantare direttamente nel browser; il ponte è l'endpoint ufficiale
`/api/auth/me?token=<JWT>&redirect=<percorso interno>`: verifica la firma → crea la sessione automaticamente
→ `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 giorni) → valida
il redirect (deve iniziare con una sola barra, `//` e barre rovesciate vietati, stessa origine dopo il parsing) → 307 reindirizzamento temporaneo alla pagina di destinazione.

Ci sono due destinazioni di link, **genera prima home, poi decidi se passare da pending in base a dove finisce l'utente**:

- **link home (inviato per primo per impostazione predefinita, `--target home` → finisce su `/`)**: generato e inviato all'utente subito dopo la registrazione riuscita.
  Nel periodo di prova gratuita l'utente entra direttamente sulla home, tutto utilizzabile; **se l'utente lo apre ma finisce sulla pagina di abbonamento, il periodo di prova gratuita è finito** — passa allora al percorso di pagamento (vedi sotto); nessuna modifica allo script e nessuna nuova registrazione necessaria.
- **link pending (usato nel percorso di pagamento, `--target pending` → finisce su `/subscription`)**:
  il browser dell'utente entra nello stato di «semi-accesso»: la pagina di abbonamento e la pagina di ritorno del pagamento sono visibili e utilizzabili. Dopo l'incasso,
  esegui `refresh-login` per scambiare contro un nuovo JWT con la dichiarazione ACTIVE, poi invia di nuovo il link home per l'iscrizione completa.

## Sequenza completa

### Percorso rapido (nel periodo di prova gratuita — la stragrande maggioranza dei casi)

```
1.  status                          # auto-verifica dell'ambiente
2.  (Passo 2 conversazione per confermare le info, password a scelta; modalità generata: gen-password → fai salvare subito all'utente)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → l'utente controlla il codice nella e-mail (unica uscita dalla conversazione)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → invia il link all'utente; un clic ed è sulla home
7.  (l'utente conferma di essere entrato) → concludi direttamente: cleanup + scheda account + guida dei primi passi
```

### Percorso di pagamento (quando l'utente vuole l'iscrizione, o il periodo di prova gratuita è finito)

```
1–5. Come il percorso rapido (dopo il register riuscito il token è già nello state)
6.  login-link --target pending     # → link di semi-accesso, mantiene funzionante la pagina di ritorno del pagamento
7.  (l'utente sceglie il metodo di pagamento)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <file della pagina di pagamento>   # Windows; macOS usa open, Linux usa xdg-open
    # → l'utente completa il pagamento/l'autorizzazione alla cassa Alipay/PayPal (esce dalla conversazione)
9.  query (ogni 10–15 s) fino a paid / ACTIVE
10. refresh-login                   # scambia contro un nuovo JWT con la dichiarazione ACTIVE
11. login-link --target home        # → invia il link di iscrizione completa all'utente
12. whoami                          # conferma subscriptionStatus: ACTIVE (opzionale)
13. cleanup                         # ripulisci il file di stato
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Il periodo di prova gratuita è finito e il pagamento non è ancora arrivato; torna al passo 9 per continuare a sondare, o conferma se l'utente ha completato il pagamento |",
    AF_ERR_SUB="| L'utente apre il link home ma finisce sulla pagina di abbonamento | Il periodo di prova gratuita è finito → passa al percorso di pagamento: `login-link --target pending` → scegli un metodo di pagamento → `create-order` |",
    AF_FALLBACK="Dopo il rientro nella modalità guida: dai la pagina di registrazione https://global.powpow.online/register (nel periodo di prova gratuita, anche la registrazione web è equally immediata; quando serve un abbonamento, dai anche la pagina di abbonamento https://global.powpow.online/subscription ), accompagna la risoluzione secondo le regole di `registration-flow.md`, mantieni lo stesso tono e concludi ogni turno con un blocco «passo successivo».",
    PA_NOTE="""> **Periodo di prova gratuita (a partire dal 2026-10-18; vale il comportamento reale della piattaforma)**: in questo periodo un account registrato può usare direttamente tutte le funzioni, e **abbonarsi è un miglioramento opzionale e non un requisito** — segui il flusso di questo file solo quando l'utente vuole attivamente l'iscrizione. Quando il periodo di prova finirà, gli account senza abbonamento che visitano le pagine di contenuto verranno reindirizzati alla pagina di abbonamento; basta completare l'abbonamento secondo questo file.""",
    RF_STATE="""## Flusso di stato dopo la registrazione riuscita

> **Periodo di prova gratuita (a partire dal 2026-10-18; vale il comportamento reale della piattaforma)**: un account appena registrato può **usare direttamente tutte le funzioni**
> (feed, mappa, umani digitali, check-in ecc.) senza pagare; gli account senza abbonamento non sono più bloccati dalle pagine di contenuto. La descrizione del
> «blocco pending» in questa sezione è lo stato normale dopo la fine del periodo di prova — quando arriva quel momento, vale il comportamento reale online.

1. L'utente viene salvato con `accountStatus: 'pending'` e **3 badge iniziali** (register route).
2. Il server pianta anche due cookie HttpOnly: il JWT (può accedere direttamente alle pagine) e
   il pendingUserToken (credenziale di identità per il flusso di abbonamento).
3. Nello stato normale (periodo di prova finito / nessun periodo gratuito), la pagina di registrazione rileva `pending_payment` → reindirizza a `/subscription`
   (mantenendo il parametro di ritorno `next`); in modalità assistita dall'agent, `me?token=…&redirect=/subscription` ottiene lo stesso effetto.
   **Nel periodo di prova gratuita questo passaggio non scatta** — dopo la registrazione, entra direttamente sulla home e inizia a usare.
4. Pagamento completato → `accountStatus` diventa `active` (**Alipay attiva automaticamente lato server via notify**;
   PayPal attiva via Webhook; il codice QR WeChat è confermato manualmente; Huawei IAP passa da `activate-huawei`).
   Dettagli in `payment-and-activation.md`.

Nello stato normale, gli utenti inattivi (pending) che chiamano le API core (feed, mappa, chat con umani digitali, check-in ecc.) ricevono 403;
i link dei post condivisi sono l'eccezione (restano accessibili pubblicamente). Nel periodo di prova gratuita questo blocco è sospeso e tutto è aperto.""",
    RF_ROW_403="| Registrazione riuscita ma il login restituisce 403 «请完成订阅以激活账户» | L'account è ancora pending, e la piattaforma non è in un periodo di prova gratuita (stato atteso prima del pagamento) | Non succede nel periodo di prova gratuita; se succede, il periodo di prova è finito — completa prima l'abbonamento; se dopo il pagamento dà ancora 403, è stato usato un vecchio JWT — in modalità script esegui prima `refresh-login` per scambiare contro un nuovo stato di accesso |",
    RF_ROW_LAND="| L'utente apre il link di accesso ma finisce sulla pagina di abbonamento (invece che sulla home) | Il periodo di prova gratuita è finito e il paywall della piattaforma è tornato | Segui il flusso di pagamento per abbonamento del Passo 7 in SKILL.md; dopo l'abbonamento, esegui `refresh-login` e poi invia il link alla home |",
    RD_VER="""**Dalla v2.0.0 modalità assistita dall'agent, e dalla v2.2.0 adattamento al periodo di prova gratuita della piattaforma**: lo script centrale `scripts/powpow-register.mjs` è a zero dipendenze
(Node ≥ 18); l'utente esce dalla conversazione una sola volta: per controllare il codice di verifica nella propria e-mail. Nell'attuale periodo di prova gratuita, un account registrato può usare subito tutte le funzioni — il pagamento dell'abbonamento è un miglioramento opzionale; se il periodo di prova finisce e l'utente finisce sulla pagina di abbonamento, il flusso passa automaticamente al percorso di pagamento. Senza Node, o quando l'utente preferisce fare da sé, rientro automatico nella modalità di sola guida.""",
    RD_LINK="""3. **Accesso con un clic (doppio link)**: subito dopo la registrazione riuscita, un link di accesso porta l'utente direttamente sulla home (nel periodo di prova gratuita, un clic ed è utilizzabile);
   se finisce sulla pagina di abbonamento (periodo di prova finito) o l'utente vuole migliorare, segui il flusso di abbonamento — dopo l'incasso, scambia contro un nuovo stato di accesso e il link di iscrizione completa lo porta sulla home
   (attraverso il ponte ufficiale `me?token=` della piattaforma, che pianta il cookie HttpOnly automaticamente).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
