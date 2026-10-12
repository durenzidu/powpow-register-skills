# -*- coding: utf-8 -*-
FR = dict(
    PA_CONCL_N=4,
    DESC=[
        ("l'activation de l'abonnement via Alipay", "l'activation de l'abonnement via Alipay ou PayPal"),
        ("paie à la caisse Alipay", "paie à la caisse Alipay ou PayPal"),
    ],
    INTRO=("**payer à la caisse Alipay** (l'agent ouvre automatiquement la page de paiement)",
           "**payer à la caisse de paiement** (Alipay ou PayPal — l'agent ouvre automatiquement la page de paiement)"),
    VLINE=[
        ("**Version 2.0.1** · 2026-10-08", "**Version 2.1.0** · 2026-10-11"),
        ("Depuis la v2.0.1, les captures du produit sont embarquées avec la compétence dans `assets/screenshots/`, sans dépendre d'un hébergeur d'images externe",
         "Depuis la v2.1.0, les abonnements PayPal peuvent aussi être pris en charge par l'agent, au même titre qu'Alipay"),
    ],
    STEP6="""2. **Fais choisir à l'utilisateur son moyen de paiement** ; présente les deux canaux :
   - **Alipay (Chine continentale / utilisateurs avec Alipay)** : achat unique de la durée correspondante, **sans renouvellement automatique**
     - Mensuel **¥6.99** (recommandé pour essayer) / Trimestriel **¥19.99** / Annuel **¥69.99**
   - **PayPal (étranger / utilisateurs sans Alipay)** : renouvellement automatique mensuel, annulable à tout moment
     - Premium Monthly, environ **$1/mois** (selon l'affichage de la page d'abonnement ; renouvellement automatique)
3. Une fois le choix fait :
   - **Alipay** :
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal** :
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Le script renvoie le chemin du fichier de la page de paiement ; **ouvre-le directement avec une commande système** (Windows : `start <fichier>` ; macOS : `open <fichier>` ; Linux : `xdg-open <fichier>`). Le navigateur saute automatiquement à la caisse officielle Alipay ou PayPal, où l'utilisateur finalise le paiement ou l'autorisation de prélèvement.
4. Lance `query` toutes les 10–15 secondes jusqu'à ce qu'il renvoie `paid` ou `ACTIVE` (l'encaissement / l'autorisation prend en général de quelques secondes à une minute). Si l'utilisateur ferme la page de paiement en cours de route → relance simplement `create-order` (les anciennes commandes se ferment et les abonnements en attente expirent au bout de 2 heures ; on ne s'en occupe pas).
5. Le canal QR code WeChat demande une confirmation manuelle et l'encaissement peut traîner ; Huawei IAP n'est disponible que dans l'app HarmonyOS. La compétence ne gère pas ces deux-là : une fois payé, on revient pareil à l'étape 7.
""",
    BOUNDARY=("au compte Alipay de l'utilisateur ni à ses moyens de paiement",
              "au compte Alipay/PayPal de l'utilisateur ni à ses moyens de paiement"),
    PA_CONCL="""**Les abonnements par Alipay comme par PayPal peuvent désormais être pris en charge par l'agent — création de la commande et suivi de l'encaissement compris.**
Alipay est un achat unique sans renouvellement automatique, pour les utilisateurs en Chine continentale et ceux qui ont Alipay ; PayPal se renouvelle automatiquement chaque mois et s'annule à tout moment,
pour les utilisateurs à l'étranger et sans Alipay. Le QR code WeChat (confirmation manuelle) et Huawei IAP restent disponibles, mais la compétence ne les prend pas en charge.""",
    PA_RESP=[
        ("au compte Alipay de l'utilisateur", "au compte Alipay/PayPal de l'utilisateur"),
        ("l'utilisateur lui-même à la caisse officielle Alipay.", "l'utilisateur lui-même à la caisse officielle."),
    ],
    PA_FRESH=("après confirmation du `paid`, lance d'abord `refresh-login`",
              "après confirmation du `paid` / du `ACTIVE` PayPal, lance d'abord `refresh-login`"),
    PA_PAYPAL="""## Canal d'abonnement PayPal (pris en charge par la compétence ; web, hors HarmonyOS)

Il n'existe qu'une seule formule, Premium Monthly (environ $1/mois, selon ce que renvoie `/api/subscription/plans`) ; **elle se renouvelle automatiquement chaque mois**
et l'utilisateur peut l'annuler quand il veut depuis son compte PayPal.

### Contrat d'interface (déjà encapsulé par le script de la compétence ; l'agent n'assemble pas les requêtes à la main)

| Interface | Méthode | Description |
|---|---|---|
| `/api/subscription/plans` | GET | Auth Bearer ; renvoie la liste des formules disponibles (actuellement une seule) |
| `/api/subscription/create` | POST | body `{planId}` → renvoie `{subscriptionId, approveUrl, status}` ; `status` vaut généralement `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Auth Bearer ; renvoie `{activeSubscription, allSubscriptions}` ; l'agent sonde `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Appelée automatiquement par la page de succès (avec le cookie) ; active directement via l'API PayPal si le webhook n'est pas arrivé |
| `/subscription/success` | Page de retour navigateur | Page d'atterrissage après l'autorisation PayPal ; sonde verify automatiquement, puis revient à l'accueil / à la page d'origine |
| `/subscription/cancel` | Page navigateur | Page d'atterrissage en cas d'annulation ou d'échec ; on peut relancer |

### Déroulé délégué

```
create-order --provider paypal  # → renvoie approveUrl, écrit dans un fichier HTML local
ouvrir le fichier HTML          # → le navigateur saute vers la page d'autorisation PayPal
query (toutes les 10–15 s)      # → sonder jusqu'à ACTIVE
refresh-login                   # → échanger contre un JWT neuf (déclaration d'abonnement ACTIVE)
login-link --target home        # → générer le lien de connexion définitif
```

- Les abonnements PENDING non finalisés dans l'heure sont nettoyés automatiquement par le backend ; il suffit de relancer.
- Si l'utilisateur relance `create-order`, le backend réutilise l'abonnement `APPROVAL_PENDING` encore valide, ce qui évite un 409.
- Comme avec Alipay : l'encaissement ne met à jour que la base de données, un ancien JWT ne se rafraîchit pas tout seul — il **faut** lancer `refresh-login` avant d'envoyer le lien vers l'accueil.""",
    PA_ROWS="""| Le `query` PayPal reste PENDING | L'utilisateur n'a pas finalisé l'autorisation dans PayPal ; vérifie que le lien d'autorisation a bien été ouvert dans le navigateur. Si c'est toujours PENDING après autorisation, le webhook a peut-être du retard : demande à l'utilisateur d'attendre quelques secondes de plus sur la page de succès ou de la recharger |
| Le `query` PayPal renvoie 409 | Il existe déjà un abonnement PENDING non terminé ; attends 1 heure qu'il expire, ou finalise l'autorisation de l'ancien lien dans le navigateur |
| PayPal payé, mais l'accès via le lien 2 reste bloqué | Comme avec Alipay : d'abord `refresh-login`, ensuite `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay par défaut)<br>`--provider alipay\\|paypal` | Crée la commande de paiement ; Alipay renvoie le chemin du fichier de la page de paiement + outTradeNo ; PayPal renvoie le chemin du fichier de la page d'autorisation + subscriptionId (noté automatiquement dans le fichier d'état) |",
    AF_ROW_QUERY="| `query` | —— | Consulte l'état de la commande / de l'abonnement. Alipay : `paid / pending / closed / unknown` ; PayPal : `ACTIVE / PENDING` ; interrogation toutes les 10–15s |",
    AF_SEQ7="""7.  (l'utilisateur choisit son moyen de paiement)
    # Alipay : create-order --package monthly|quarterly|yearly
    # PayPal : create-order --provider paypal""",
    AF_SEQ8=("# → l'utilisateur paie à la caisse Alipay (sortie de la conversation, moment ②)",
             "# → l'utilisateur finalise le paiement/l'autorisation à la caisse Alipay/PayPal (sortie de la conversation, moment ②)"),
    AF_SEQ9=("9.  query (toutes les 10–15s) jusqu'à paid", "9.  query (toutes les 10–15s) jusqu'à paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| L'utilisateur a fermé la page de paiement après `create-order` | Relance directement `create-order` (l'ancienne commande se ferme seule au bout de 2h) |",
                  "| L'utilisateur a fermé la page de paiement après `create-order` | Relance directement `create-order` (l'ancienne commande se ferme seule au bout de 2h ; les abonnements PENDING PayPal expirent au bout de 1h) |"),
    AF_ERR_409="| `create-order --provider paypal` renvoie 409 | Il existe déjà un abonnement PayPal non finalisé ; attends 1h qu'il expire, ou finalise l'ancienne autorisation dans le navigateur |",
    AF_ERR_PEND=("| `query` reste en pending | L'utilisateur n'a peut-être pas payé ; pose la question. S'il a vraiment payé → suis le tableau de diagnostic de payment-and-activation.md |",
                 "| `query` reste en pending / PENDING | L'utilisateur n'a peut-être pas payé ; pose la question. S'il a vraiment payé → suis le tableau de diagnostic de payment-and-activation.md |"),
    AF_ERR_403=("Le paiement n'est pas encore encaissé ;", "Le paiement/l'autorisation n'est pas encore encaissé ;"),
    RD=[
        ("d'abonnement Alipay et suivi de l'encaissement", "d'abonnement Alipay/PayPal et suivi de l'encaissement"),
        ("**Depuis la v2.0.0, mode prise en charge déléguée par l'agent** : le script principal",
         "**Depuis la v2.0.0, mode prise en charge déléguée par l'agent, et depuis la v2.1.0 PayPal aussi** : le script principal"),
        ("payer à la caisse Alipay.", "payer à la caisse Alipay/PayPal."),
        ("4. **Paiement de l'abonnement** : canal Alipay, commande déléguée à l'agent (mensuel ¥6.99 / trimestriel",
         "4. **Paiement de l'abonnement** : Alipay (mensuel ¥6.99 / trimestriel"),
        ("¥19.99 / annuel ¥69.99, achat unique sans renouvellement automatique) + interrogation en boucle jusqu'à",
         "¥19.99 / annuel ¥69.99, achat unique sans renouvellement automatique) comme PayPal (Premium Monthly, environ $1/mois, renouvellement automatique, annulable à tout moment) sont gérés par l'agent : commande + interrogation en boucle jusqu'à"),
        ("l'encaissement ; repli vers PayPal pour les utilisateurs à l'étranger ; QR code WeChat / Huawei IAP : on montre le chemin.",
         "l'encaissement ; QR code WeChat / Huawei IAP : on montre le chemin."),
        ("au compte Alipay de l'utilisateur ni à ses moyens de paiement", "au compte Alipay/PayPal de l'utilisateur ni à ses moyens de paiement"),
        ("la caisse officielle Alipay.", "la caisse officielle."),
    ],
)

DE = dict(
    PA_CONCL_N=2,
    DESC=[
        ("Alipay-Abonnement-Aktivierung", "Alipay-/PayPal-Abonnement-Aktivierung"),
        ("zahlen an der Alipay-Kasse", "zahlen an der Alipay-/PayPal-Kasse"),
    ],
    INTRO=("**um an der Alipay-Kasse zu zahlen** (der agent öffnet die Kassenseite automatisch)",
           "**um an der Kasse zu zahlen** (Alipay oder PayPal — der agent öffnet die Kassenseite automatisch)"),
    VLINE=[
        ("**Version 2.0.1** · 2026-10-08", "**Version 2.1.0** · 2026-10-11"),
        ("Ab v2.0.1 werden die Produkt-Screenshots mit dem Skill unter `assets/screenshots/` ausgeliefert — keine Abhängigkeit von externen Bild-Hostings mehr",
         "Ab v2.1.0 kann der agent auch PayPal-Abos übernehmen, als Option neben Alipay"),
    ],
    STEP6="""2. **Lass den Nutzer die Zahlungsart wählen** — zeig beide Kanäle:
   - **Alipay (China / Nutzer:innen mit Alipay)**: Einmalkauf der entsprechenden Laufzeit, **keine automatische Verlängerung**
     - Monatlich **¥6.99** (zum Ausprobieren empfohlen) / Quartal **¥19.99** / Jahr **¥69.99**
   - **PayPal (Ausland / ohne Alipay)**: monatliche automatische Verlängerung, jederzeit kündbar
     - Premium Monthly, ca. **$1/Monat** (gemäß Anzeige auf der Abo-Seite; automatische Verlängerung)
3. Sobald gewählt wurde:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Das Skript liefert den Dateipfad der Zahlungsseite — **direkt per Systembefehl öffnen** (Windows: `start <Datei>`; macOS: `open <Datei>`; Linux: `xdg-open <Datei>`). Der Browser springt automatisch zur offiziellen Kasse von Alipay oder PayPal; der Nutzer schließt dort die Zahlung oder die Einzugsermächtigung ab.
4. Alle 10–15 Sekunden `query` ausführen, bis `paid` oder `ACTIVE` zurückkommt (Zahlung/Autorisierung meist in wenigen Sekunden bis einer Minute). Schließt der Nutzer die Zahlungsseite zwischendurch → einfach erneut `create-order` (alte Bestellungen bzw. offene Abos schließen bzw. laufen nach 2 Stunden automatisch ab; nicht darum kümmern).
5. Der WeChat-QR-Kanal wird manuell bestätigt, der Zahlungseingang kann sich verzögern; Huawei IAP gibt es nur in der HarmonyOS-App. Diese beiden macht der Skill nicht — nach der Zahlung geht es ganz normal mit Schritt 7 weiter.
""",
    BOUNDARY=("das Alipay-Konto/Zahlungs-Credentials des Nutzers", "das Alipay-/PayPal-Konto/Zahlungs-Credentials des Nutzers"),
    PA_CONCL="""**Sowohl Alipay- als auch PayPal-Abos kann der agent übernehmen — Bestellung anlegen und Zahlungseingang verfolgen inklusive.**
Alipay ist ein Einmalkauf ohne automatische Verlängerung, für Nutzer:innen in China und mit Alipay; PayPal verlängert sich monatlich automatisch und ist jederzeit kündbar,
für Nutzer:innen im Ausland und ohne Alipay. WeChat-QR (manuelle Bestätigung) und Huawei IAP gibt es weiterhin, sie werden vom Skill aber nicht übernommen.""",
    PA_RESP=[
        ("mit dem Alipay-Konto /", "mit dem Alipay-/PayPal-Konto /"),
        ("an der offiziellen Alipay-Kasse aus.", "an der offiziellen Kasse aus."),
    ],
    PA_FRESH=("nach Bestätigung von `paid` zuerst `refresh-login` aus",
              "nach Bestätigung von `paid` / PayPal `ACTIVE` zuerst `refresh-login` aus"),
    PA_PAYPAL="""## PayPal-Abo-Kanal (vom Skill übernommen; Web, nicht HarmonyOS)

Es gibt nur einen Plan, Premium Monthly (ca. $1/Monat, laut Rückgabe von `/api/subscription/plans`); er **verlängert sich monatlich automatisch**
und der Nutzer kann ihn jederzeit in seinem PayPal-Konto kündigen.

### Endpunkt-Vertrag (vom Skill-Skript gekapselt; der agent baut keine Anfragen selbst)

| Endpunkt | Methode | Beschreibung |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer-Auth; liefert die Liste der verfügbaren Pläne (aktuell nur 1) |
| `/api/subscription/create` | POST | Body `{planId}` → liefert `{subscriptionId, approveUrl, status}`; `status` ist meist `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Bearer-Auth; liefert `{activeSubscription, allSubscriptions}`; der agent pollt `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Wird von der Erfolgsseite automatisch aufgerufen (mit Cookie); aktiviert direkt über die PayPal-API, wenn der Webhook noch nicht da ist |
| `/subscription/success` | Browser-Rückkehrseite | Landet nach der PayPal-Autorisierung, pollt verify automatisch und springt danach zur Startseite / Ursprungsseite zurück |
| `/subscription/cancel` | Browser-Seite | Landet bei Abbruch oder Fehler; ein neuer Versuch ist möglich |

### Ablauf in Vertretung

```
create-order --provider paypal  # → liefert approveUrl, in lokale HTML-Datei geschrieben
HTML-Datei öffnen               # → der Browser springt zur PayPal-Autorisierungsseite
query (alle 10–15 s)            # → pollen bis ACTIVE
refresh-login                   # → neues JWT holen (Abo-Anspruch ACTIVE)
login-link --target home        # → den endgültigen Login-Link erzeugen
```

- PENDING-Abos, die innerhalb einer Stunde nicht abgeschlossen werden, räumt das Backend automatisch auf; einfach neu starten.
- Wiederholt der Nutzer `create-order`, nutzt das Backend das noch gültige `APPROVAL_PENDING`-Abo wieder und vermeidet so einen 409.
- Wie bei Alipay: Der Zahlungseingang aktualisiert nur die Datenbank, ein altes JWT wird nicht automatisch erneuert — vor dem Senden des Startseiten-Links **muss** `refresh-login` laufen.""",
    PA_ROWS="""| PayPal-`query` bleibt PENDING | Der Nutzer hat die Autorisierung bei PayPal nicht abgeschlossen; prüfen, ob der Autorisierungslink im Browser geöffnet wurde. Wenn trotz Autorisierung weiter PENDING, kann der Webhook verzögert sein — den Nutzer auf der Erfolgsseite noch einige Sekunden warten oder neu laden lassen |
| PayPal-`query` meldet 409 | Es gibt schon ein unfertiges PENDING-Abo; 1 Stunde warten, bis es abläuft, oder die Autorisierung des alten Links im Browser abschließen |
| PayPal bezahlt, aber mit Link 2 weiterhin blockiert | Wie bei Alipay: zuerst `refresh-login`, dann `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Standard: Alipay)<br>`--provider alipay\\|paypal` | Legt die Zahlungsbestellung an; Alipay liefert den Dateipfad der Zahlungsseite + outTradeNo, PayPal den Dateipfad der Autorisierungsseite + subscriptionId (automatisch in die Statusdatei eingetragen) |",
    AF_ROW_QUERY="| `query` | —— | Fragt den Status von Bestellung/Abo ab. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; alle 10–15 s pollen |",
    AF_SEQ7="""7.  (der Nutzer wählt die Zahlungsart)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → der Nutzer zahlt an der Alipay-Kasse (Verlassen des Chats, Stelle ②)",
             "# → der Nutzer schließt Zahlung/Autorisierung an der Alipay-/PayPal-Kasse ab (Verlassen des Chats, Stelle ②)"),
    AF_SEQ9=("9.  query (alle 10–15 s) bis paid", "9.  query (alle 10–15 s) bis paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Nach `create-order` hat der Nutzer die Zahlungsseite geschlossen | Einfach erneut `create-order` (die alte Bestellung schließt sich nach 2 h automatisch) |",
                  "| Nach `create-order` hat der Nutzer die Zahlungsseite geschlossen | Einfach erneut `create-order` (die alte Bestellung schließt sich nach 2 h automatisch; PayPal-PENDING-Abos laufen nach 1 h ab) |"),
    AF_ERR_409="| `create-order --provider paypal` meldet 409 | Es gibt schon ein unfertiges PayPal-Abo; 1 h warten, bis es abläuft, oder die alte Autorisierung im Browser abschließen |",
    AF_ERR_PEND=("| `query` bleibt dauerhaft pending | Der Nutzer hat eventuell nicht bezahlt; kurz nachfragen. Wirklich bezahlt → nach der Troubleshooting-Tabelle in payment-and-activation.md vorgehen |",
                 "| `query` bleibt dauerhaft pending / PENDING | Der Nutzer hat eventuell nicht bezahlt; kurz nachfragen. Wirklich bezahlt → nach der Troubleshooting-Tabelle in payment-and-activation.md vorgehen |"),
    AF_ERR_403=("Die Zahlung ist noch nicht eingegangen;", "Die Zahlung/Autorisierung ist noch nicht eingegangen;"),
    RD=[
        ("Alipay-Abo-Bestellung mit Eingangsverfolgung", "Alipay-/PayPal-Abo-Bestellung mit Eingangsverfolgung"),
        ("**Ab v2.0.0 agent-gestützter Modus**: Das Kernskript", "**Ab v2.0.0 agent-gestützter Modus, ab v2.1.0 auch PayPal**: Das Kernskript"),
        ("Zahlung an der Alipay-Kasse.", "Zahlung an der Alipay-/PayPal-Kasse."),
        ("4. **Abo-Zahlung**: Im Alipay-Kanal bestellt der agent (Monat ¥6.99 / Quartal ¥19.99 / Jahr ¥69.99, Einmalkauf ohne automatische Verlängerung) und pollt den Eingang; Übersee-Nutzer:innen fallen auf PayPal zurück; WeChat-QR/Huawei IAP nur den Weg weisen.",
         "4. **Abo-Zahlung**: Sowohl Alipay (Monat ¥6.99 / Quartal ¥19.99 / Jahr ¥69.99, Einmalkauf ohne automatische Verlängerung) als auch PayPal (Premium Monthly, ca. $1/Monat, automatische Verlängerung, jederzeit kündbar) bestellt der agent und pollt den Eingang; WeChat-QR/Huawei IAP nur den Weg weisen."),
        ("das Alipay-Konto oder Zahlungs-Credentials", "das Alipay-/PayPal-Konto oder Zahlungs-Credentials"),
        ("der offiziellen Alipay-Kasse.", "der offiziellen Kasse."),
    ],
)

PT = dict(
    PA_CONCL_N=4,
    DESC=[
        ("a ativação da assinatura via Alipay", "a ativação da assinatura via Alipay ou PayPal"),
        ("paga no caixa do Alipay", "paga no caixa do Alipay ou PayPal"),
    ],
    INTRO=("**pagar no caixa do Alipay** (o agent abre automaticamente a página de pagamento)",
           "**pagar no caixa de pagamento** (Alipay ou PayPal — o agent abre automaticamente a página de pagamento)"),
    VLINE=[
        ("**Versão 2.0.1** · 2026-10-08", "**Versão 2.1.0** · 2026-10-11"),
        ("Desde a v2.0.1 as capturas do produto acompanham a skill em `assets/screenshots/`, sem depender de hospedagem externa de imagens",
         "Desde a v2.1.0 as assinaturas PayPal também podem ser gerenciadas pelo agent, como opção ao lado do Alipay"),
    ],
    STEP6="""2. **Peça ao usuário para escolher a forma de pagamento**; mostre os dois canais:
   - **Alipay (China continental / usuários com Alipay)**: compra única do período correspondente, **sem renovação automática**
     - Mensal **¥6.99** (recomendado para começar testando) / Trimestral **¥19.99** / Anual **¥69.99**
   - **PayPal (exterior / usuários sem Alipay)**: renovação automática mensal, cancele quando quiser
     - Premium Monthly, cerca de **$1/mês** (conforme a exibição na página de assinatura; renovação automática)
3. Depois que o usuário escolher:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   O script devolve o caminho do arquivo da página de pagamento; **abra-o diretamente com um comando do sistema** (Windows: `start <arquivo>`; macOS: `open <arquivo>`; Linux: `xdg-open <arquivo>`). O navegador salta automaticamente para o caixa oficial do Alipay ou PayPal, onde o usuário conclui o pagamento ou a autorização de cobrança.
4. Rode `query` a cada 10–15 segundos até devolver `paid` ou `ACTIVE` (o pagamento/autorização costuma cair de alguns segundos a um minuto). Se o usuário fechar a página de pagamento no meio → rode `create-order` de novo direto (pedidos antigos/assinaturas pendentes fecham ou expiram sozinhos em 2 horas; não é preciso se ocupar deles).
5. O canal de QR code do WeChat tem confirmação manual e o pagamento pode demorar a cair; o Huawei IAP só está disponível dentro do app HarmonyOS. A skill não gerencia esses dois: depois de pagar, segue-se igualmente para a etapa 7.
""",
    BOUNDARY=("na conta Alipay do usuário ou nas suas credenciais de pagamento",
              "na conta Alipay/PayPal do usuário ou nas suas credenciais de pagamento"),
    PA_CONCL="""**Tanto a assinatura por Alipay como a por PayPal podem ser gerenciadas pelo agent — criação do pedido e acompanhamento do pagamento inclusos.**
O Alipay é compra única sem renovação automática, para usuários da China continental e com Alipay; o PayPal renova automaticamente todo mês e pode ser cancelado a qualquer momento,
para usuários no exterior e sem Alipay. O QR code do WeChat (confirmação manual) e o Huawei IAP continuam existindo, mas não são gerenciados pela skill.""",
    PA_RESP=[
        ("na conta Alipay do usuário", "na conta Alipay/PayPal do usuário"),
        ("no caixa oficial do Alipay.", "no caixa oficial."),
    ],
    PA_FRESH=("`paid`, roda primeiro `refresh-login`", "`paid` / PayPal `ACTIVE`, roda primeiro `refresh-login`"),
    PA_PAYPAL="""## Canal de assinatura PayPal (gerenciado pela skill; web, fora do HarmonyOS)

Existe apenas um plano, o Premium Monthly (cerca de $1/mês, conforme o retorno de `/api/subscription/plans`); **renova automaticamente todo mês**
e o usuário pode cancelar quando quiser na sua conta PayPal.

### Contrato das interfaces (já encapsuladas pelo script da skill; o agent não monta as requisições à mão)

| Interface | Método | Descrição |
|---|---|---|
| `/api/subscription/plans` | GET | Auth Bearer; devolve a lista de planos disponíveis (atualmente só 1) |
| `/api/subscription/create` | POST | body `{planId}` → devolve `{subscriptionId, approveUrl, status}`; `status` costuma ser `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Auth Bearer; devolve `{activeSubscription, allSubscriptions}`; o agent faz polling de `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Chamada automaticamente pela página de sucesso (com o cookie); ativa direto pela API do PayPal se o webhook não chegou |
| `/subscription/success` | Página de retorno do navegador | Onde o usuário cai após a autorização do PayPal; faz polling de verify automaticamente e depois volta para a home/página original |
| `/subscription/cancel` | Página do navegador | Onde o usuário cai se cancelar ou falhar; dá para recomeçar |

### Fluxo delegado

```
create-order --provider paypal  # → devolve approveUrl, gravado num arquivo HTML local
abrir o arquivo HTML            # → o navegador salta para a página de autorização do PayPal
query (a cada 10–15s)           # → fazer polling até ACTIVE
refresh-login                   # → trocar por um JWT novo (declaração de assinatura ACTIVE)
login-link --target home        # → gerar o link de login definitivo
```

- Assinaturas PENDING que não forem concluídas em 1 hora são limpas automaticamente pelo backend; basta recomeçar.
- Se o usuário repetir `create-order`, o backend reaproveita a assinatura `APPROVAL_PENDING` ainda válida, evitando um 409.
- Igual ao Alipay: o pagamento só atualiza o banco, um JWT antigo não se renova sozinho — **é obrigatório** rodar `refresh-login` antes de mandar o link da home.""",
    PA_ROWS="""| O `query` do PayPal fica em PENDING | O usuário não concluiu a autorização no PayPal; confirme se o link de autorização foi aberto no navegador. Se mesmo autorizado continuar PENDING, pode ser atraso do webhook: peça ao usuário para esperar mais alguns segundos na página de sucesso ou recarregá-la |
| O `query` do PayPal devolve 409 | Já existe uma assinatura PENDING não concluída; espere 1 hora para expirar ou conclua a autorização do link antigo no navegador |
| PayPal pago, mas com o link 2 continua bloqueado | Igual ao Alipay: primeiro `refresh-login`, depois `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay é o padrão)<br>`--provider alipay\\|paypal` | Cria o pedido de pagamento; o Alipay devolve o caminho do arquivo da página de pagamento + outTradeNo; o PayPal devolve o caminho do arquivo da página de autorização + subscriptionId (gravado automaticamente no arquivo de estado) |",
    AF_ROW_QUERY="| `query` | —— | Consulta o estado do pedido/assinatura. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; consulta a cada 10–15s |",
    AF_SEQ7="""7.  (o usuário escolhe a forma de pagamento)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → o usuário paga no caixa do Alipay (saída da conversa, momento ②)",
             "# → o usuário conclui o pagamento/autorização no caixa do Alipay/PayPal (saída da conversa, momento ②)"),
    AF_SEQ9=("9.  query (a cada 10–15s) até paid", "9.  query (a cada 10–15s) até paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| O usuário fechou a página de pagamento depois do `create-order` | Rode `create-order` de novo direto (o pedido antigo fecha sozinho em 2h) |",
                  "| O usuário fechou a página de pagamento depois do `create-order` | Rode `create-order` de novo direto (o pedido antigo fecha sozinho em 2h; assinaturas PENDING do PayPal expiram em 1h) |"),
    AF_ERR_409="| `create-order --provider paypal` devolve 409 | Já existe uma assinatura PayPal não concluída; espere 1h para expirar ou conclua a autorização antiga no navegador |",
    AF_ERR_PEND=("| `query` fica em pending | O usuário talvez não tenha pago; pergunte. Se pagou mesmo → siga a tabela de diagnóstico do payment-and-activation.md |",
                 "| `query` fica em pending / PENDING | O usuário talvez não tenha pago; pergunte. Se pagou mesmo → siga a tabela de diagnóstico do payment-and-activation.md |"),
    AF_ERR_403=("O pagamento ainda não caiu;", "O pagamento/autorização ainda não caiu;"),
    RD=[
        ("pedido de assinatura via Alipay e acompanhamento", "pedido de assinatura via Alipay/PayPal e acompanhamento"),
        ("**Desde a v2.0.0 o modo é de gestão delegada pelo agent**: o script principal",
         "**Desde a v2.0.0 o modo é de gestão delegada pelo agent, e desde a v2.1.0 o PayPal também**: o script principal"),
        ("pagar no caixa do Alipay.", "pagar no caixa do Alipay/PayPal."),
        ("4. **Pagamento da assinatura**: no canal Alipay o agent faz o pedido por delegação (mensal ¥6.99 /",
         "4. **Pagamento da assinatura**: tanto no Alipay (mensal ¥6.99 /"),
        ("trimestral ¥19.99 / anual ¥69.99, compra única sem renovação automática) + consulta em loop até cair;",
         "trimestral ¥19.99 / anual ¥69.99, compra única sem renovação automática) como no PayPal (Premium Monthly, cerca de $1/mês, renovação automática, cancele quando quiser) o agent faz o pedido e a consulta em loop até cair;"),
        ("usuários no exterior recuam para o PayPal; QR code WeChat / Huawei IAP apenas indica-se o caminho.",
         "QR code WeChat / Huawei IAP apenas indica-se o caminho."),
        ("Alipay do usuário ou nas suas credenciais", "Alipay/PayPal do usuário ou nas suas credenciais"),
        ("o caixa oficial do Alipay.", "o caixa oficial."),
    ],
)

IT = dict(
    PA_CONCL_N=4,
    DESC=[
        ("attivare l'abbonamento via Alipay", "attivare l'abbonamento via Alipay o PayPal"),
        ("pagare alla cassa Alipay", "pagare alla cassa Alipay o PayPal"),
    ],
    INTRO=("**pagare alla cassa Alipay** (l'agent apre automaticamente la pagina di pagamento)",
           "**pagare alla cassa di pagamento** (Alipay o PayPal — l'agent apre automaticamente la pagina di pagamento)"),
    VLINE=[
        ("**Versione 2.0.1** · 2026-10-08", "**Versione 2.1.0** · 2026-10-11"),
        ("Dalla v2.0.1 gli screenshot di prodotto sono inclusi nel pacchetto in `assets/screenshots/`, senza dipendere da servizi di hosting esterni",
         "Dalla v2.1.0 anche gli abbonamenti PayPal possono essere gestiti dall'agent, come opzione accanto ad Alipay"),
    ],
    STEP6="""2. **Fai scegliere all'utente il metodo di pagamento**; mostra entrambi i canali:
   - **Alipay (Cina continentale / utenti con Alipay)**: acquisto una tantum del periodo corrispondente, **senza rinnovo automatico**
     - Mese **¥6.99** (consigliato per provare) / Trimestre **¥19.99** / Anno **¥69.99**
   - **PayPal (estero / utenti senza Alipay)**: rinnovo automatico mensile, disdici quando vuoi
     - Premium Monthly, circa **$1/mese** (come mostrato nella pagina abbonamento; rinnovo automatico)
3. Una volta scelto:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Lo script restituisce il percorso del file della pagina di pagamento; **aprilo direttamente con un comando di sistema** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Il browser salta da solo alla cassa ufficiale di Alipay o PayPal, dove l'utente completa il pagamento o l'autorizzazione all'addebito.
4. Esegui `query` ogni 10–15 secondi finché non restituisce `paid` o `ACTIVE` (pagamento/autorizzazione di solito arriva in pochi secondi o in un minuto). Se l'utente chiude la pagina di pagamento a metà → esegui subito di nuovo `create-order` (i vecchi ordini e gli abbonamenti in sospeso si chiudono o scadono da soli dopo 2 ore; non pensarci).
5. Il canale QR WeChat richiede conferma manuale e l'accredito può ritardare; Huawei IAP è disponibile solo dentro l'app HarmonyOS. La skill non gestisce questi due: finito il pagamento si torna comunque al passo 7.
""",
    BOUNDARY=("l'account Alipay o le credenziali di pagamento dell'utente",
              "l'account Alipay/PayPal o le credenziali di pagamento dell'utente"),
    PA_CONCL="""**Sia gli abbonamenti con Alipay sia quelli con PayPal possono essere gestiti dall'agent — creazione dell'ordine e tracciamento dell'accredito inclusi.**
Alipay è un acquisto una tantum senza rinnovo automatico, per gli utenti in Cina continentale e chi ha Alipay; PayPal si rinnova automaticamente ogni mese e si può disdire in qualsiasi momento,
per gli utenti all'estero e senza Alipay. Il QR WeChat (conferma manuale) e Huawei IAP restano disponibili, ma la skill non li gestisce.""",
    PA_RESP=[
        ("l'account Alipay o le credenziali", "l'account Alipay/PayPal o le credenziali"),
        ("la cassa ufficiale Alipay.", "la cassa ufficiale."),
    ],
    PA_FRESH=("il `paid`, la skill esegue prima `refresh-login`",
              "il `paid` o lo `ACTIVE` di PayPal, la skill esegue prima `refresh-login`"),
    PA_PAYPAL="""## Canale di abbonamento PayPal (gestito dalla skill; web, non HarmonyOS)

Esiste un solo piano, Premium Monthly (circa $1/mese, secondo quanto restituito da `/api/subscription/plans`); **si rinnova automaticamente ogni mese**
e l'utente può disdirlo quando vuole dal proprio account PayPal.

### Contratto delle interfacce (già incapsulato nello script della skill; l'agent non costruisce richieste per conto proprio)

| Interfaccia | Metodo | Descrizione |
|---|---|---|
| `/api/subscription/plans` | GET | Auth Bearer; restituisce l'elenco dei piani disponibili (al momento solo 1) |
| `/api/subscription/create` | POST | body `{planId}` → restituisce `{subscriptionId, approveUrl, status}`; `status` di solito è `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Auth Bearer; restituisce `{activeSubscription, allSubscriptions}`; l'agent fa polling di `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | La chiama automaticamente la pagina di successo (con il cookie); attiva direttamente tramite l'API PayPal se il webhook non è arrivato |
| `/subscription/success` | Pagina di ritorno del browser | Dove si atterra dopo l'autorizzazione PayPal; fa polling di verify automaticamente e poi torna alla home / pagina originale |
| `/subscription/cancel` | Pagina del browser | Dove si atterra se l'utente annulla o qualcosa fallisce; si può riprovare |

### Flusso delegato

```
create-order --provider paypal  # → restituisce approveUrl, scritto in un file HTML locale
aprire il file HTML             # → il browser salta alla pagina di autorizzazione PayPal
query (ogni 10–15s)             # → fare polling fino ad ACTIVE
refresh-login                   # → scambiare con un JWT nuovo (dichiarazione di abbonamento ACTIVE)
login-link --target home        # → generare il link di accesso definitivo
```

- Gli abbonamenti PENDING non completati entro 1 ora vengono ripuliti automaticamente dal backend; basta ricominciare.
- Se l'utente ripete `create-order`, il backend riutilizza l'abbonamento `APPROVAL_PENDING` ancora valido, evitando un 409.
- Come con Alipay: l'accredito aggiorna solo il database, un JWT vecchio non si rinnova da sé — **bisogna** eseguire `refresh-login` prima di inviare il link alla home.""",
    PA_ROWS="""| Il `query` di PayPal resta PENDING | L'utente non ha completato l'autorizzazione su PayPal; verifica che il link di autorizzazione sia stato aperto nel browser. Se dopo l'autorizzazione resta PENDING, può essere un ritardo del webhook: chiedi all'utente di attendere qualche secondo in più sulla pagina di successo o di ricaricarla |
| Il `query` di PayPal restituisce 409 | Esiste già un abbonamento PENDING non completato; attendi 1 ora perché scada, oppure completa l'autorizzazione del vecchio link nel browser |
| PayPal pagato, ma con il link 2 si viene comunque respinti | Come con Alipay: prima `refresh-login`, poi `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay predefinito)<br>`--provider alipay\\|paypal` | Crea l'ordine di pagamento; Alipay restituisce il percorso del file della pagina di pagamento + outTradeNo; PayPal restituisce il percorso del file della pagina di autorizzazione + subscriptionId (registrato automaticamente nel file di stato) |",
    AF_ROW_QUERY="| `query` | —— | Interroga lo stato dell'ordine/abbonamento. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; polling ogni 10–15s |",
    AF_SEQ7="""7.  (l'utente sceglie il metodo di pagamento)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → l'utente paga alla cassa Alipay (uscita dalla conversazione ②)",
             "# → l'utente completa pagamento/autorizzazione alla cassa Alipay/PayPal (uscita dalla conversazione ②)"),
    AF_SEQ9=("9.  query (ogni 10–15s) finché non è paid", "9.  query (ogni 10–15s) finché non è paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| L'utente chiude la pagina di pagamento dopo `create-order` | Eseguire subito di nuovo `create-order` (il vecchio ordine si chiude da solo dopo 2h) |",
                  "| L'utente chiude la pagina di pagamento dopo `create-order` | Eseguire subito di nuovo `create-order` (il vecchio ordine si chiude da solo dopo 2h; gli abbonamenti PENDING PayPal scadono dopo 1h) |"),
    AF_ERR_409="| `create-order --provider paypal` restituisce 409 | Esiste già un abbonamento PayPal non completato; attendi 1h perché scada o completa la vecchia autorizzazione nel browser |",
    AF_ERR_PEND=("| `query` resta sempre pending | Forse l'utente non ha pagato; chiedere. Se ha pagato davvero → seguire la tabella in payment-and-activation.md |",
                 "| `query` resta sempre pending / PENDING | Forse l'utente non ha pagato; chiedere. Se ha pagato davvero → seguire la tabella in payment-and-activation.md |"),
    AF_ERR_403=("Il pagamento non è ancora accreditato,", "Il pagamento o l'autorizzazione non è ancora accreditato,"),
    RD=[
        ("dell'abbonamento Alipay, accesso con un clic a doppio link", "dell'abbonamento Alipay/PayPal, accesso con un clic a doppio link"),
        ("**Dalla v2.0.0 è la modalità a operazione delegata dell'agent**: lo script principale",
         "**Dalla v2.0.0 è la modalità a operazione delegata dell'agent, e dalla v2.1.0 anche PayPal**: lo script principale"),
        ("pagare alla cassa Alipay.", "pagare alla cassa Alipay/PayPal."),
        ("4. **Pagamento dell'abbonamento**: canale Alipay con ordine delegato all'agent (mese ¥6.99 / trimestre ¥19.99 /",
         "4. **Pagamento dell'abbonamento**: sia Alipay (mese ¥6.99 / trimestre ¥19.99 /"),
        ("anno ¥69.99, acquisto una tantum senza rinnovo automatico) + interrogazione dell'accredito; per gli utenti",
         "anno ¥69.99, acquisto una tantum senza rinnovo automatico) sia PayPal (Premium Monthly, circa $1/mese, rinnovo automatico, disdica quando vuoi) sono gestiti dall'agent: ordine + interrogazione dell'accredito;"),
        ("all'estero ripiego su PayPal; per QR WeChat/Huawei IAP solo indicazioni.", "per QR WeChat/Huawei IAP solo indicazioni."),
        ("non tocca mai l'account Alipay o", "non tocca mai l'account Alipay/PayPal o"),
        ("e la cassa ufficiale Alipay.", "e la cassa ufficiale."),
    ],
)
