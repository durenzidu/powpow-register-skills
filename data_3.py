# -*- coding: utf-8 -*-
RU = dict(
    PA_CONCL_N=3,
    DESC=[
        ("активацию подписки через Alipay", "активацию подписки через Alipay или PayPal"),
        ("оплатить в кассе Alipay", "оплатить в кассе Alipay или PayPal"),
    ],
    INTRO=("**оплатить в кассе Alipay** (agent сам откроет страницу оплаты)",
           "**оплатить в кассе** (Alipay или PayPal — agent сам откроет страницу оплаты)"),
    VLINE=[
        ("**Версия 2.0.1** · 2026-10-08", "**Версия 2.1.0** · 2026-10-11"),
        ("С v2.0.1 скриншоты продукта едут вместе со скиллом в `assets/screenshots/`, без зависимости от внешнего хостинга картинок",
         "С v2.1.0 подписки PayPal тоже может вести agent — наравне с Alipay"),
    ],
    STEP6="""2. **Попроси пользователя выбрать способ оплаты** — покажи оба канала:
   - **Alipay (Китай / пользователи с Alipay)**: разовая покупка соответствующего периода, **без автопродления**
     - Месячный **¥6.99** (рекомендуем для пробы) / Квартальный **¥19.99** / Годовой **¥69.99**
   - **PayPal (за рубежом / без Alipay)**: ежемесячное автопродление, отмена в любой момент
     - Premium Monthly, около **$1/мес** (как показано на странице подписки; автопродление)
3. Когда пользователь выберет:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Скрипт вернёт путь к файлу страницы оплаты; **откройте его напрямую системной командой** (Windows: `start <файл>`; macOS: `open <файл>`; Linux: `xdg-open <файл>`). Браузер автоматически перейдёт в официальную кассу Alipay или PayPal, где пользователь завершит оплату или авторизацию списания.
4. Запускайте `query` каждые 10–15 секунд, пока не вернётся `paid` или `ACTIVE` (зачисление/авторизация обычно занимает от нескольких секунд до минуты). Если пользователь закрыл страницу оплаты на середине → просто заново `create-order` (старые заказы и зависшие подписки закроются или истекут через 2 часа; не обращайте внимания).
5. Канал QR-кода WeChat подтверждается вручную, зачисление может задержаться; Huawei IAP доступен только внутри приложения HarmonyOS. Эти два скилл не ведёт — после оплаты они так же возвращаются к шагу 7.
""",
    BOUNDARY=("**никогда** не касается аккаунта Alipay пользователя и его платёжных инструментов",
              "**никогда** не касается аккаунта Alipay/PayPal пользователя и его платёжных инструментов"),
    PA_CONCL="""**И Alipay-, и PayPal-подписки теперь может вести agent — создание заказа и отслеживание зачисления включены.**
Alipay — разовая покупка без автопродления, для пользователей из Китая и с Alipay; PayPal продлевается автоматически каждый месяц и отменяется в любой момент,
для пользователей за рубежом и без Alipay. QR-код WeChat (ручное подтверждение) и Huawei IAP остаются доступными, но скилл их не ведёт.""",
    PA_RESP=[
        ("аккаунта Alipay пользователя", "аккаунта Alipay/PayPal пользователя"),
        ("в официальной кассе Alipay.", "в официальной кассе."),
    ],
    PA_FRESH=("Поэтому скилл после подтверждения `paid` сначала",
              "Поэтому скилл после подтверждения `paid` / PayPal `ACTIVE` сначала"),
    PA_PAYPAL="""## Канал подписки PayPal (ведёт скилл; веб, не HarmonyOS)

Есть только один план — Premium Monthly (около $1/мес, по данным `/api/subscription/plans`); он **продлевается автоматически каждый месяц**,
и пользователь может отменить его в любой момент в своём аккаунте PayPal.

### Контракт интерфейсов (уже обёрнут скриптом скилла; agent не собирает запросы вручную)

| Интерфейс | Метод | Описание |
|---|---|---|
| `/api/subscription/plans` | GET | Авторизация Bearer; возвращает список доступных планов (сейчас только 1) |
| `/api/subscription/create` | POST | body `{planId}` → возвращает `{subscriptionId, approveUrl, status}`; `status` обычно `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Авторизация Bearer; возвращает `{activeSubscription, allSubscriptions}`; agent опрашивает `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Вызывается страницей успеха автоматически (с cookie); активирует напрямую через API PayPal, если webhook ещё не пришёл |
| `/subscription/success` | Страница возврата в браузере | Сюда попадают после авторизации в PayPal; автоматически опрашивает verify и потом возвращает на главную / исходную страницу |
| `/subscription/cancel` | Страница в браузере | Сюда попадают при отмене или ошибке; можно начать заново |

### Поток в режиме делегирования

```
create-order --provider paypal  # → возвращает approveUrl, записанный в локальный HTML-файл
открыть HTML-файл               # → браузер переходит на страницу авторизации PayPal
query (каждые 10–15с)           # → опрашивать до ACTIVE
refresh-login                   # → обменять на новый JWT (декларация подписки ACTIVE)
login-link --target home        # → сгенерировать окончательную ссылку входа
```

- Подписки PENDING, не завершённые в течение часа, бэкенд очищает автоматически; просто начните заново.
- Если пользователь повторит `create-order`, бэкенд переиспользует ещё действительную подписку `APPROVAL_PENDING`, избегая 409.
- Как и с Alipay: зачисление обновляет только базу, старый JWT сам не обновляется — перед отправкой ссылки на главную **обязательно** запустите `refresh-login`.""",
    PA_ROWS="""| `query` PayPal всё время PENDING | Пользователь не завершил авторизацию в PayPal; проверьте, что ссылка авторизации открыта в браузере. Если после авторизации всё ещё PENDING, возможна задержка webhook — попросите пользователя подождать ещё несколько секунд на странице успеха или обновить её |
| `query` PayPal возвращает 409 | Уже есть незавершённая подписка PENDING; подождите 1 час, пока она истечёт, или завершите авторизацию по старой ссылке в браузере |
| PayPal оплачен, но по ссылке 2 всё ещё закрыто | Как с Alipay: сначала `refresh-login`, потом `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (по умолчанию Alipay)<br>`--provider alipay\\|paypal` | Создаёт платёжный заказ; Alipay возвращает путь к файлу страницы оплаты + outTradeNo; PayPal возвращает путь к файлу страницы авторизации + subscriptionId (автоматически записывается в файл состояния) |",
    AF_ROW_QUERY="| `query` | —— | Проверяет статус заказа/подписки. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; опрос каждые 10–15с |",
    AF_SEQ7="""7.  (пользователь выбирает способ оплаты)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → пользователь платит в кассе Alipay (выход из диалога, момент ②)",
             "# → пользователь завершает оплату/авторизацию в кассе Alipay/PayPal (выход из диалога, момент ②)"),
    AF_SEQ9=("9.  query (каждые 10–15с) до paid", "9.  query (каждые 10–15с) до paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Пользователь закрыл страницу оплаты после `create-order` | Просто заново `create-order` (старый заказ сам закроется через 2ч) |",
                  "| Пользователь закрыл страницу оплаты после `create-order` | Просто заново `create-order` (старый заказ сам закроется через 2ч; подписки PayPal в статусе PENDING истекают через 1ч) |"),
    AF_ERR_409="| `create-order --provider paypal` возвращает 409 | Уже есть незавершённая подписка PayPal; подождите 1ч, пока она истечёт, или завершите старую авторизацию в браузере |",
    AF_ERR_PEND=("| `query` всё время pending | Возможно, пользователь не заплатил; спросите. Если точно заплатил → идти по таблице разбора payment-and-activation.md |",
                 "| `query` всё время pending / PENDING | Возможно, пользователь не заплатил; спросите. Если точно заплатил → идти по таблице разбора payment-and-activation.md |"),
    AF_ERR_403=("Оплата ещё не зачислилась;", "Оплата/авторизация ещё не зачислилась;"),
    RD=[
        ("через Alipay и отслеживание зачисления", "через Alipay или PayPal и отслеживание зачисления"),
        ("**С v2.0.0 — режим делегированного выполнения agent'ом**",
         "**С v2.0.0 — режим делегированного выполнения agent'ом, с v2.1.0 и PayPal**"),
        ("сходить в почту за кодом и оплатить в кассе Alipay.", "сходить в почту за кодом и оплатить в кассе Alipay или PayPal."),
        ("4. **Оплата подписки**: канал Alipay — заказ делегирован agent'у (месяц ¥6.99 / квартал ¥19.99 / год",
         "4. **Оплата подписки**: и Alipay (месяц ¥6.99 / квартал ¥19.99 / год"),
        ("¥69.99, разовая покупка без автопродления) + опрос зачисления; пользователи за рубежом откатываются на",
         "¥69.99, разовая покупка без автопродления), и PayPal (Premium Monthly, около $1/мес, автопродление, отмена в любой момент) — заказ делегирован agent'у + опрос зачисления;"),
        ("PayPal; QR-код WeChat / Huawei IAP — только показать дорогу.", "QR-код WeChat / Huawei IAP — только показать дорогу."),
        ("аккаунта Alipay пользователя или его платёжных инструментов", "аккаунта Alipay/PayPal пользователя или его платёжных инструментов"),
        ("официальной кассой Alipay.", "официальной кассой."),
    ],
)

PL = dict(
    PA_CONCL_N=4,
    DESC=[
        ("aktywację subskrypcji Alipay", "aktywację subskrypcji Alipay lub PayPal"),
        ("płaci w kasie Alipay", "płaci w kasie Alipay lub PayPal"),
    ],
    INTRO=("**zapłacić w kasie Alipay** (agent sam otworzy stronę kasy)",
           "**zapłacić w kasie** (Alipay lub PayPal — agent sam otworzy stronę kasy)"),
    VLINE=[
        ("**Wersja 2.0.1** · 2026-10-08", "**Wersja 2.1.0** · 2026-10-11"),
        ("Od v2.0.1 zrzuty ekranu produktu są pakowane razem ze skillem w `assets/screenshots/` i nie zależą od zewnętrznego hostingu obrazków",
         "Od v2.1.0 subskrypcje PayPal też może obsługiwać agent, jako opcję obok Alipay"),
    ],
    STEP6="""2. **Poproś użytkownika o wybór metody płatności** — pokaż oba kanały:
   - **Alipay (Chiny / użytkownicy z Alipay)**: jednorazowy zakup odpowiedniego okresu, **bez automatycznego odnawiania**
     - Miesięcznie **¥6.99** (polecany na start) / Kwartalnie **¥19.99** / Rocznie **¥69.99**
   - **PayPal (zagranica / bez Alipay)**: automatyczne odnawianie co miesiąc, rezygnacja w każdej chwili
     - Premium Monthly, ok. **$1/mies.** (zgodnie z tym, co pokazuje strona subskrypcji; automatyczne odnawianie)
3. Gdy użytkownik wybierze:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Skrypt zwróci ścieżkę pliku strony płatności; **otwórz ją bezpośrednio poleceniem systemowym** (Windows: `start <plik>`; macOS: `open <plik>`; Linux: `xdg-open <plik>`). Przeglądarka sama przejdzie do oficjalnej kasy Alipay lub PayPal, gdzie użytkownik sfinalizuje płatność albo autoryzację obciążenia.
4. Co 10–15 sekund uruchamiaj `query`, aż zwróci `paid` lub `ACTIVE` (księgowanie/autoryzacja zwykle trwa od kilku sekund do minuty). Jeśli użytkownik zamknie stronę płatności w trakcie → po prostu ponów `create-order` (stare zamówienia i wiszące subskrypcje zamykają się lub wygasają po 2 godzinach; nie przejmuj się nimi).
5. Kanał skanowania WeChat wymaga ręcznego potwierdzenia i księgowanie może się opóźnić; Huawei IAP działa tylko w aplikacji HarmonyOS. Tych dwóch skill nie załatwia — po zapłacie i tak wracają do kroku 7.
""",
    BOUNDARY=("**nigdy** nie dotyka konta Alipay/dowodów płatności użytkownika",
              "**nigdy** nie dotyka konta Alipay/PayPal/dowodów płatności użytkownika"),
    PA_CONCL="""**Zarówno subskrypcje przez Alipay, jak i przez PayPal może obsługiwać agent — składanie zamówienia i śledzenie księgowania włącznie.**
Alipay to jednorazowy zakup bez automatycznego odnawiania, dla użytkowników z Chin i tych z Alipay; PayPal odnawia się automatycznie co miesiąc i można zrezygnować w każdej chwili,
dla użytkowników spoza Chin i bez Alipay. Skanowanie WeChat (potwierdzenie ręczne) i Huawei IAP dalej istnieją, ale skill ich nie załatwia.""",
    PA_RESP=[
        ("konta Alipay/dowodów płatności", "konta Alipay/PayPal/dowodów płatności"),
        ("w oficjalnej kasie Alipay.", "w oficjalnej kasie."),
    ],
    PA_FRESH=("Dlatego po potwierdzeniu `paid` skill najpierw odpala `refresh-login`",
              "Dlatego po potwierdzeniu `paid` / PayPal `ACTIVE` skill najpierw odpala `refresh-login`"),
    PA_PAYPAL="""## Kanał subskrypcji PayPal (obsługiwany przez skill; web, nie HarmonyOS)

Istnieje tylko jeden plan — Premium Monthly (ok. $1/mies., zgodnie z `/api/subscription/plans`); **odnawia się automatycznie co miesiąc**,
a użytkownik może zrezygnować w każdej chwili w swoim koncie PayPal.

### Kontrakt interfejsów (już opakowany przez skrypt skilla; agent nie składa requestów samodzielnie)

| Interfejs | Metoda | Opis |
|---|---|---|
| `/api/subscription/plans` | GET | Autoryzacja Bearer; zwraca listę dostępnych planów (obecnie tylko 1) |
| `/api/subscription/create` | POST | body `{planId}` → zwraca `{subscriptionId, approveUrl, status}`; `status` to zwykle `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Autoryzacja Bearer; zwraca `{activeSubscription, allSubscriptions}`; agent odpytuje `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Wywoływana automatycznie przez stronę sukcesu (z ciasteczkiem); aktywuje bezpośrednio przez API PayPal, gdy webhook jeszcze nie dotarł |
| `/subscription/success` | Strona powrotu w przeglądarce | Tu ląduje się po autoryzacji w PayPal; automatycznie odpytuje verify i wraca na stronę główną / pierwotną stronę |
| `/subscription/cancel` | Strona w przeglądarce | Tu ląduje się przy anulowaniu lub błędzie; można zacząć od nowa |

### Przebieg w trybie agenta

```
create-order --provider paypal  # → zwraca approveUrl zapisany w lokalnym pliku HTML
otworzyć plik HTML              # → przeglądarka przechodzi na stronę autoryzacji PayPal
query (co 10–15 s)              # → odpytywać do ACTIVE
refresh-login                   # → wymiana na nowy JWT (claim subskrypcji ACTIVE)
login-link --target home        # → wygenerować właściwy link logowania
```

- Subskrypcje PENDING nieukończone w ciągu godziny backend czyści automatycznie; po prostu zacznij od nowa.
- Jeśli użytkownik powtórzy `create-order`, backend wykorzysta ponownie wciąż ważną subskrypcję `APPROVAL_PENDING`, unikając 409.
- Tak jak przy Alipay: księgowanie aktualizuje tylko bazę, stary JWT nie odświeża się sam — przed wysłaniem linku na stronę główną **trzeba** uruchomić `refresh-login`.""",
    PA_ROWS="""| `query` PayPal ciągle PENDING | Użytkownik nie dokończył autoryzacji w PayPal; sprawdź, czy link autoryzacyjny został otwarty w przeglądarce. Jeśli po autoryzacji nadal PENDING, możliwe opóźnienie webhooka — poproś użytkownika, by odczekał jeszcze kilka sekund na stronie sukcesu lub ją odświeżył |
| `query` PayPal zwraca 409 | Istnieje już niedokończona subskrypcja PENDING; odczekaj 1 godzinę, aż wygaśnie, albo dokończ autoryzację starego linku w przeglądarce |
| PayPal opłacony, ale z linkiem 2 nadal blokada | Tak jak przy Alipay: najpierw `refresh-login`, potem `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (domyślnie Alipay)<br>`--provider alipay\\|paypal` | Tworzy zamówienie płatności; Alipay zwraca ścieżkę pliku strony płatności + outTradeNo, PayPal zwraca ścieżkę pliku strony autoryzacji + subscriptionId (automatycznie wpisywane do pliku stanu) |",
    AF_ROW_QUERY="| `query` | —— | Sprawdza status zamówienia/subskrypcji. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; odpytywanie co 10–15 s |",
    AF_SEQ7="""7.  (użytkownik wybiera metodę płatności)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → użytkownik płaci w kasie Alipay (punkt wyjścia z rozmowy ②)",
             "# → użytkownik finalizuje płatność/autoryzację w kasie Alipay/PayPal (punkt wyjścia z rozmowy ②)"),
    AF_SEQ9=("9.  query (co 10–15 s) aż do paid", "9.  query (co 10–15 s) aż do paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Po `create-order` użytkownik zamknął stronę płatności | Po prostu ponów `create-order` (stare zamówienie zamknie się samo po 2 h) |",
                  "| Po `create-order` użytkownik zamknął stronę płatności | Po prostu ponów `create-order` (stare zamówienie zamknie się samo po 2 h; subskrypcje PayPal w statusie PENDING wygasają po 1 h) |"),
    AF_ERR_409="| `create-order --provider paypal` zwraca 409 | Istnieje już niedokończona subskrypcja PayPal; odczekaj 1 h, aż wygaśnie, albo dokończ starą autoryzację w przeglądarce |",
    AF_ERR_PEND=("| `query` wciąż pending | Użytkownik mógł nie zapłacić; zapytaj jednym zdaniem. Jeśli zapłacił → idź wg tabeli w payment-and-activation.md |",
                 "| `query` wciąż pending / PENDING | Użytkownik mógł nie zapłacić; zapytaj jednym zdaniem. Jeśli zapłacił → idź wg tabeli w payment-and-activation.md |"),
    AF_ERR_403=("Płatność jeszcze nie zaksięgowana;", "Płatność/autoryzacja jeszcze nie zaksięgowana;"),
    RD=[
        ("zamówienie subskrypcji Alipay", "zamówienie subskrypcji Alipay/PayPal"),
        ("**Od v2.0.0 tryb agenta działającego w imieniu użytkownika**",
         "**Od v2.0.0 tryb agenta działającego w imieniu użytkownika, od v2.1.0 także PayPal**"),
        ("skrzynki e-mail i na płatność w kasie Alipay.", "skrzynki e-mail i na płatność w kasie Alipay lub PayPal."),
        ("4. **Płatność subskrypcji**: kanał Alipay z zamówieniem załatwianym przez agenta (miesięcznie ¥6.99 / kwartalnie",
         "4. **Płatność subskrypcji**: zarówno Alipay (miesięcznie ¥6.99 / kwartalnie"),
        ("¥19.99 / rocznie ¥69.99, jednorazowy zakup bez automatycznego odnawiania) + odpytywanie o księgowanie;",
         "¥19.99 / rocznie ¥69.99, jednorazowy zakup bez automatycznego odnawiania), jak i PayPal (Premium Monthly, ok. $1/mies., automatyczne odnawianie, rezygnacja w każdej chwili) załatwia agent + odpytywanie o księgowanie;"),
        ("użytkownicy spoza Chin cofają się do PayPal; skanowanie WeChat/Huawei IAP tylko ze wskazaniem drogi.",
         "skanowanie WeChat/Huawei IAP tylko ze wskazaniem drogi."),
        ("Alipay ani dowodów płatności użytkownika", "Alipay/PayPal ani dowodów płatności użytkownika"),
        ("oficjalną kasą Alipay.", "oficjalną kasą."),
    ],
)

TR = dict(
    PA_CONCL_N=3,
    DESC=[
        ("Alipay üzerinden aboneliği etkinleştirmesine", "Alipay veya PayPal üzerinden aboneliği etkinleştirmesine"),
        ("Alipay kasa sayfasında ödemeyi yapmak", "Alipay/PayPal kasa sayfasında ödemeyi yapmak"),
    ],
    INTRO=("**Alipay kasa sayfasında ödemek** (agent ödeme sayfasını kendiliğinden açar)",
           "**kasa sayfasında ödemek** (Alipay veya PayPal — agent ödeme sayfasını kendiliğinden açar)"),
    VLINE=[
        ("**Sürüm 2.0.1** · 2026-10-08", "**Sürüm 2.1.0** · 2026-10-11"),
        ("v2.0.1'den itibaren ürün ekran görüntüleri `assets/screenshots/` altında paketle birlikte gelir, harici görsel servisine bağlı değildir",
         "v2.1.0'dan itibaren PayPal aboneliklerini de agent vekâleten yürütebilir, Alipay'in yanında bir seçenek olarak"),
    ],
    STEP6="""2. **Kullanıcıya ödeme yöntemini seçtirin** — iki kanalı da gösterin:
   - **Alipay (Çin / Alipay'i olan kullanıcılar)**: karşılık gelen sürenin tek seferlik satın alımı, **otomatik yenileme yok**
     - Aylık **¥6.99** (ilk denemede önerilir) / Üç aylık **¥19.99** / Yıllık **¥69.99**
   - **PayPal (yurt dışı / Alipay'i olmayan kullanıcılar)**: aylık otomatik yenileme, istenildiği anda iptal
     - Premium Monthly, yaklaşık **$1/ay** (abonelik sayfasında gösterildiği şekilde; otomatik yenileme)
3. Kullanıcı seçtikten sonra:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Script ödeme sayfası dosyasının yolunu döndürür; **sistem komutuyla doğrudan açın** (Windows: `start <dosya>`; macOS: `open <dosya>`; Linux: `xdg-open <dosya>`). Tarayıcı kendiliğinden Alipay ya da PayPal'ın resmî kasa sayfasına gider; kullanıcı ödemeyi veya ödeme talimatını orada tamamlar.
4. `paid` ya da `ACTIVE` dönene dek 10–15 saniyede bir `query` çalıştırın (hesaba geçiş/autorizasyon genelde birkaç saniye ile bir dakika arası sürer). Kullanıcı ödeme sayfasını yarıda kapatırsa → hemen `create-order`'ı tekrar çalıştırın (eski siparişler ve bekleyen abonelikler 2 saatte kendiliğinden kapanır ya da sona erer; dert etmeyin).
5. WeChat QR kanalı elle onay gerektirir, hesaba geçiş gecikebilir; Huawei IAP yalnızca HarmonyOS uygulaması içinde kullanılabilir. Bu ikisini skill vekâleten yürütmez — ödeme bittikten sonra yine Adım 7'ye dönülür.
""",
    BOUNDARY=("kullanıcının Alipay hesabına/ödeme belgelerine **asla** dokunmaz",
              "kullanıcının Alipay/PayPal hesabına/ödeme belgelerine **asla** dokunmaz"),
    PA_CONCL="""**Hem Alipay hem de PayPal aboneliklerini artık vekâleten agent yürütebilir — sipariş açma ve hesaba geçiş takibi dahil.**
Alipay otomatik yenilemesi olmayan tek seferlik satın alımdır; Çin'deki ve Alipay'i olan kullanıcılara uygundur. PayPal her ay otomatik yenilenir ve istenildiği anda iptal edilebilir,
yurt dışındaki ve Alipay'i olmayan kullanıcılara uygundur. WeChat QR (elle onay) ve Huawei IAP duruyor, ancak skill bunları vekâleten yürütmez.""",
    PA_RESP=[
        ("kullanıcının Alipay", "kullanıcının Alipay/PayPal"),
        ("kullanıcı tarafından Alipay'in resmî kasasında yapılır.", "kullanıcı tarafından resmî kasada yapılır."),
    ],
    PA_FRESH=("`paid` doğrulandıktan sonra önce `refresh-login` çalıştırır",
              "`paid` / PayPal `ACTIVE` doğrulandıktan sonra önce `refresh-login` çalıştırır"),
    PA_PAYPAL="""## PayPal abonelik kanalı (skill vekâleten yürütür; web, HarmonyOS değil)

Tek bir plan var: Premium Monthly (yaklaşık $1/ay, `/api/subscription/plans` dönüşüne göre). **Her ay otomatik yenilenir**
ve kullanıcı bunu PayPal hesabından istediği zaman iptal edebilir.

### Arayüz sözleşmesi (skill scripti tarafından sarmalandı; agent istekleri kendisi kurmaz)

| Arayüz | Metot | Açıklama |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer doğrulama; kullanılabilir planların listesini döner (şu anda yalnızca 1) |
| `/api/subscription/create` | POST | body `{planId}` → `{subscriptionId, approveUrl, status}` döner; `status` genelde `APPROVAL_PENDING` olur |
| `/api/subscription/create` | GET | Bearer doğrulama; `{activeSubscription, allSubscriptions}` döner; agent `activeSubscription.subscription.status === 'ACTIVE'` değerini yoklar |
| `/api/subscription/verify` | POST | Başarı sayfası tarafından otomatik çağrılır (cookie ile); webhook gelmediyse PayPal API üzerinden doğrudan etkinleştirir |
| `/subscription/success` | Tarayıcı dönüş sayfası | PayPal onayından sonra buraya düşülür; verify'yi otomatik yoklar, sonra ana sayfaya / ilk sayfaya döner |
| `/subscription/cancel` | Tarayıcı sayfası | Kullanıcı iptal ederse ya da hata olursa buraya düşülür; yeniden denenebilir |

### Vekâlet akışı

```
create-order --provider paypal  # → approveUrl döner, yerel HTML dosyasına yazılır
HTML dosyasını aç               # → tarayıcı PayPal onay sayfasına geçer
query (her 10–15s)              # → ACTIVE olana dek yokla
refresh-login                   # → yeni JWT ile değiştir (abonelik beyanı ACTIVE)
login-link --target home        # → kesin giriş bağlantısını üret
```

- 1 saat içinde tamamlanmayan PENDING abonelikleri backend otomatik temizler; baştan başlamak yeterlidir.
- Kullanıcı `create-order`'ı tekrarlarsa backend hâlâ geçerli olan `APPROVAL_PENDING` aboneliği yeniden kullanır ve 409'u önler.
- Alipay'deki gibi: hesaba geçiş yalnızca veritabanını günceller, eski JWT kendiliğinden yenilenmez — ana sayfa bağlantısını göndermeden önce **mutlaka** `refresh-login` çalıştırılmalıdır.""",
    PA_ROWS="""| PayPal `query` sürekli PENDING | Kullanıcı PayPal'da onayı tamamlamadı; onay bağlantısının tarayıcıda açıldığını doğrulayın. Onaya rağmen hâlâ PENDING ise webhook gecikmesi olabilir — kullanıcıdan başarı sayfasında birkaç saniye daha beklemesini veya sayfayı yenilemesini isteyin |
| PayPal `query` 409 döndürüyor | Hâlihazırda tamamlanmamış bir PENDING abonelik var; 1 saat bekleyip sona ermesini bekleyin ya da eski bağlantının onayını tarayıcıda tamamlayın |
| PayPal ödendi ama bağlantı 2 ile giriş hâlâ engelli | Alipay'deki gibi: önce `refresh-login`, sonra `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (varsayılan Alipay)<br>`--provider alipay\\|paypal` | Ödeme siparişini oluşturur; Alipay ödeme sayfası dosya yolunu + outTradeNo döndürür, PayPal onay sayfası dosya yolunu + subscriptionId döndürür (otomatik olarak durum dosyasına yazılır) |",
    AF_ROW_QUERY="| `query` | —— | Sipariş/abonelik durumunu sorar. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; 10–15s arayla yoklanır |",
    AF_SEQ7="""7.  (kullanıcı ödeme yöntemini seçer)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → kullanıcı Alipay kasasında öder (sohbetten ayrılış ②)",
             "# → kullanıcı Alipay/PayPal kasasında ödemeyi/onayı tamamlar (sohbetten ayrılış ②)"),
    AF_SEQ9=("9.  query (her 10–15s) paid olana dek", "9.  query (her 10–15s) paid / ACTIVE olana dek"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| `create-order`'dan sonra kullanıcı ödeme sayfasını kapattı | Doğrudan `create-order` yeniden (eski sipariş 2 saatte otomatik kapanır) |",
                  "| `create-order`'dan sonra kullanıcı ödeme sayfasını kapattı | Doğrudan `create-order` yeniden (eski sipariş 2 saatte otomatik kapanır; PayPal PENDING abonelikler 1 saatte sona erer) |"),
    AF_ERR_409="| `create-order --provider paypal` 409 döndürüyor | Hâlihazırda tamamlanmamış bir PayPal aboneliği var; 1 saat bekleyip sona ermesini bekleyin ya da eski onayı tarayıcıda tamamlayın |",
    AF_ERR_PEND=("| `query` sürekli pending | Kullanıcı ödememiş olabilir; bir cümle sorun. Gerçekten ödediyse → payment-and-activation.md'deki teşhis tablosunu izleyin |",
                 "| `query` sürekli pending / PENDING | Kullanıcı ödememiş olabilir; bir cümle sorun. Gerçekten ödediyse → payment-and-activation.md'deki teşhis tablosunu izleyin |"),
    AF_ERR_403=("Ödeme henüz hesaba geçmedi,", "Ödeme/onay henüz hesaba geçmedi,"),
    RD=[
        ("Alipay abonelik siparişi ve hesaba", "Alipay/PayPal abonelik siparişi ve hesaba"),
        ("**v2.0.0'dan itibaren agent vekâlet modudur**", "**v2.0.0'dan itibaren agent vekâlet modudur, v2.1.0'dan itibaren PayPal dahil**"),
        ("doğrulama kodunu okumak ve Alipay kasasında ödemek.", "doğrulama kodunu okumak ve Alipay/PayPal kasasında ödemek."),
        ("4. **Abonelik ödemesi**: Alipay kanalında agent siparişi vekâleten açar (aylık ¥6.99 / üç aylık ¥19.99 / yıllık",
         "4. **Abonelik ödemesi**: hem Alipay (aylık ¥6.99 / üç aylık ¥19.99 / yıllık"),
        ("¥69.99, tek seferlik satın alma, otomatik yenileme yok) + hesaba geçiş yoklaması; yurt dışındaki kullanıcılar",
         "¥69.99, tek seferlik satın alma, otomatik yenileme yok) hem de PayPal (Premium Monthly, yaklaşık $1/ay, otomatik yenileme, istenince iptal) için siparişi agent vekâleten açar + hesaba geçiş yoklaması;"),
        ("PayPal'e döner; WeChat QR/Huawei IAP için yol gösterilir.", "WeChat QR/Huawei IAP için yol gösterilir."),
        ("kullanıcının Alipay hesabına ya", "kullanıcının Alipay/PayPal hesabına ya"),
        ("kullanıcı ile Alipay'in resmî\n  kasası arasında gerçekleşir.", "kullanıcı ile resmî\n  kasa arasında gerçekleşir."),
    ],
)

VI = dict(
    PA_CONCL_N=3,
    DESC=[
        ("kích hoạt gói thành viên qua Alipay", "kích hoạt gói thành viên qua Alipay hoặc PayPal"),
        ("thanh toán tại trang thu ngân Alipay", "thanh toán tại trang thu ngân Alipay hoặc PayPal"),
    ],
    INTRO=("**thanh toán tại trang thu ngân Alipay** (agent sẽ tự mở trang thanh toán)",
           "**thanh toán tại trang thu ngân** (Alipay hoặc PayPal — agent sẽ tự mở trang thanh toán)"),
    VLINE=[
        ("**Phiên bản 2.0.1** · 2026-10-08", "**Phiên bản 2.1.0** · 2026-10-11"),
        ("Từ v2.0.1 ảnh chụp sản phẩm đi kèm skill trong `assets/screenshots/`, không phụ thuộc dịch vụ lưu ảnh bên ngoài",
         "Từ v2.1.0 gói PayPal cũng do agent thao tác hộ được, thành một lựa chọn ngang hàng với Alipay"),
    ],
    STEP6="""2. **Bảo người dùng chọn phương thức thanh toán** — đưa ra cả hai kênh:
   - **Alipay (Trung Quốc đại lục / người dùng có Alipay)**: mua đứt thời gian tương ứng một lần, **không tự động gia hạn**
     - Tháng **¥6.99** (khuyên dùng khi mới thử) / Quý **¥19.99** / Năm **¥69.99**
   - **PayPal (nước ngoài / người dùng không có Alipay)**: tự động gia hạn theo tháng, hủy bất cứ lúc nào
     - Premium Monthly, khoảng **$1/tháng** (theo hiển thị trên trang gói; tự động gia hạn)
3. Khi người dùng chọn xong:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Script trả về đường dẫn file trang thanh toán; **dùng lệnh hệ thống mở thẳng** (Windows: `start <tệp>`; macOS: `open <tệp>`; Linux: `xdg-open <tệp>`). Trình duyệt tự nhảy sang trang thu ngân chính thức của Alipay hoặc PayPal, nơi người dùng hoàn tất thanh toán hoặc ủy quyền trừ tiền.
4. Cứ 10–15 giây chạy `query` một lần cho đến khi trả về `paid` hoặc `ACTIVE` (tiền về/ủy quyền thường mất vài giây đến một phút). Người dùng đóng trang thanh toán giữa chừng → chạy lại `create-order` luôn (đơn cũ hoặc gói đang chờ sẽ tự đóng/hết hạn sau 2 tiếng; khỏi bận tâm).
5. Kênh quét mã WeChat cần xác nhận thủ công, tiền về có thể trễ; Huawei IAP chỉ dùng được trong app HarmonyOS. Hai kênh này skill không thao tác hộ — thanh toán xong vẫn quay về bước 7 như thường.
""",
    BOUNDARY=("**tuyệt đối không** đụng vào tài khoản Alipay/chứng từ thanh toán của người dùng",
              "**tuyệt đối không** đụng vào tài khoản Alipay/PayPal/chứng từ thanh toán của người dùng"),
    PA_CONCL="""**Cả gói qua Alipay lẫn gói qua PayPal đều do agent thao tác hộ được — gồm đặt đơn và theo dõi tiền về.**
Alipay là mua đứt một lần, không tự động gia hạn, hợp với người dùng ở Trung Quốc đại lục và người có Alipay; PayPal tự động gia hạn theo tháng, hủy bất cứ lúc nào,
hợp với người dùng ở nước ngoài và không có Alipay. Quét mã WeChat (xác nhận thủ công) và Huawei IAP vẫn còn, nhưng skill không thao tác hộ.""",
    PA_RESP=[
        ("tài khoản Alipay / chứng từ thanh toán", "tài khoản Alipay / PayPal / chứng từ thanh toán"),
        ("trang thu ngân chính thức của Alipay.", "trang thu ngân chính thức."),
    ],
    PA_FRESH=("Vì vậy khi xác nhận `paid`, skill trước tiên chạy `refresh-login`",
              "Vì vậy khi xác nhận `paid` / PayPal `ACTIVE`, skill trước tiên chạy `refresh-login`"),
    PA_PAYPAL="""## Kênh gói PayPal (skill thao tác hộ; web, không phải HarmonyOS)

Chỉ có một gói duy nhất, Premium Monthly (khoảng $1/tháng, theo kết quả trả về của `/api/subscription/plans`); **tự động gia hạn theo tháng**
và người dùng có thể hủy bất cứ lúc nào trong tài khoản PayPal của họ.

### Hợp đồng interface (script của skill đã gói sẵn; agent không tự ráp request)

| Interface | Phương thức | Mô tả |
|---|---|---|
| `/api/subscription/plans` | GET | Xác thực Bearer; trả về danh sách gói khả dụng (hiện chỉ có 1) |
| `/api/subscription/create` | POST | body `{planId}` → trả về `{subscriptionId, approveUrl, status}`; `status` thường là `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Xác thực Bearer; trả về `{activeSubscription, allSubscriptions}`; agent luân phiên kiểm tra `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Trang thành công tự gọi (kèm cookie); kích hoạt trực tiếp qua API PayPal khi webhook chưa tới |
| `/subscription/success` | Trang quay về trên trình duyệt | Nơi người dùng rơi vào sau khi ủy quyền PayPal; tự luân phiên verify rồi quay về trang chủ/trang ban đầu |
| `/subscription/cancel` | Trang trên trình duyệt | Nơi rơi vào khi người dùng hủy hoặc lỗi; có thể làm lại |

### Luồng thao tác hộ

```
create-order --provider paypal  # → trả về approveUrl, ghi vào file HTML local
mở file HTML                    # → trình duyệt nhảy sang trang ủy quyền PayPal
query (cứ 10–15s)               # → luân phiên đến khi ACTIVE
refresh-login                   # → đổi JWT mới (tuyên bố gói ACTIVE)
login-link --target home        # → sinh link đăng nhập chính thức
```

- Gói PENDING không hoàn tất trong 1 giờ sẽ được backend tự dọn; cứ làm lại từ đầu.
- Nếu người dùng lặp lại `create-order`, backend sẽ dùng lại gói `APPROVAL_PENDING` còn hiệu lực, tránh bị 409.
- Giống Alipay: tiền về chỉ cập nhật DB, JWT cũ không tự làm mới — trước khi gửi link trang chủ **bắt buộc** phải chạy `refresh-login`.""",
    PA_ROWS="""| `query` PayPal mãi PENDING | Người dùng chưa hoàn tất ủy quyền trên PayPal; kiểm tra xem link ủy quyền đã được mở trong trình duyệt chưa. Nếu đã ủy quyền mà vẫn PENDING thì có thể webhook bị trễ — bảo người dùng đợi thêm vài giây trên trang thành công hoặc tải lại trang |
| `query` PayPal báo 409 | Đã có một gói PENDING chưa hoàn tất; đợi 1 tiếng cho hết hạn, hoặc hoàn tất ủy quyền của link cũ trong trình duyệt |
| Đã trả qua PayPal nhưng vào bằng link 2 vẫn bị chặn | Giống Alipay: chạy `refresh-login` trước, rồi `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (mặc định là Alipay)<br>`--provider alipay\\|paypal` | Tạo đơn thanh toán; Alipay trả về đường dẫn file trang thanh toán + outTradeNo; PayPal trả về đường dẫn file trang ủy quyền + subscriptionId (tự ghi vào file trạng thái) |",
    AF_ROW_QUERY="| `query` | —— | Tra trạng thái đơn/gói. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; luân phiên 10–15s |",
    AF_SEQ7="""7.  (Người dùng chọn phương thức thanh toán)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → Người dùng trả tiền tại trang thu ngân Alipay (khúc rời hội thoại ②)",
             "# → Người dùng hoàn tất thanh toán/ủy quyền tại trang thu ngân Alipay/PayPal (khúc rời hội thoại ②)"),
    AF_SEQ9=("9.  query (cứ 10–15s) cho đến khi paid", "9.  query (cứ 10–15s) cho đến khi paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Sau `create-order` người dùng đóng trang thanh toán | Chạy lại `create-order` thẳng (đơn cũ 2h tự đóng) |",
                  "| Sau `create-order` người dùng đóng trang thanh toán | Chạy lại `create-order` thẳng (đơn cũ 2h tự đóng; gói PENDING của PayPal hết hạn sau 1h) |"),
    AF_ERR_409="| `create-order --provider paypal` báo 409 | Đã có một gói PayPal chưa hoàn tất; đợi 1h cho hết hạn, hoặc hoàn tất ủy quyền cũ trong trình duyệt |",
    AF_ERR_PEND=("| `query` mãi pending | Người dùng có thể chưa trả; hỏi một câu. Thật sự đã trả → đi theo bảng xử lý trong payment-and-activation.md |",
                 "| `query` mãi pending / PENDING | Người dùng có thể chưa trả; hỏi một câu. Thật sự đã trả → đi theo bảng xử lý trong payment-and-activation.md |"),
    AF_ERR_403=("Tiền chưa về,", "Tiền/ủy quyền chưa về,"),
    RD=[
        ("đặt đơn gói thành viên qua Alipay và theo dõi tiền về", "đặt đơn gói thành viên qua Alipay hoặc PayPal và theo dõi tiền về"),
        ("**Từ v2.0.0 là chế độ agent thao tác hộ**", "**Từ v2.0.0 là chế độ agent thao tác hộ, từ v2.1.0 gồm cả PayPal**"),
        ("thanh toán tại trang thu ngân Alipay.", "thanh toán tại trang thu ngân Alipay hoặc PayPal."),
        ("4. **Thanh toán gói**: kênh Alipay agent thao tác hộ đặt đơn (tháng ¥6.99 / quý ¥19.99 / năm ¥69.99,",
         "4. **Thanh toán gói**: cả Alipay (tháng ¥6.99 / quý ¥19.99 / năm ¥69.99,"),
        ("mua đứt một lần không tự động gia hạn) + luân phiên tra tiền về; người dùng ở nước ngoài lùi về PayPal;",
         "mua đứt một lần không tự động gia hạn) lẫn PayPal (Premium Monthly, khoảng $1/tháng, tự động gia hạn, hủy bất cứ lúc nào) đều do agent thao tác hộ đặt đơn + luân phiên tra tiền về;"),
        ("tài khoản Alipay", "tài khoản Alipay / PayPal"),
        ("trang thu ngân chính thức của Alipay.", "trang thu ngân chính thức."),
    ],
)
