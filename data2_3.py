# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: Russian, Polish, Turkish, Vietnamese."""
RU = dict(
    DESC="description: Помогает пользователю полностью завершить регистрацию в PowPow (Bubble) и вход в один клик прямо в диалоге. Агент заполняет форму за пользователя (включая загрузку аватара) и отправляет код подтверждения на email; пользователю достаточно дать базовую информацию и один раз проверить код подтверждения в почте — не покидая диалог. Сейчас платформа находится в бесплатном тестовом периоде: зарегистрированный аккаунт сразу может использовать все функции; оплата подписки (Alipay/PayPal) — необязательное расширение членства, и при необходимости агент тоже может провести создание заказа и отслеживание зачисления. Запускается фразами вроде «зарегистрироваться в Bubble», «создать аккаунт powpow», «как зарегистрироваться в Bubble», «помоги зарегистрировать аккаунт powpow», «sign up powpow»; также разбирается с проблемами регистрации (код подтверждения не пришёл, имя пользователя/email уже заняты) и активации (при входе говорит «аккаунт не активирован» / pending_payment, как подписаться/оплатить, Bubble бесплатный или платный). Требует Node ≥ 18; если недоступен — автоматический откат в режим чистых указаний. Не покрывает публикации и создание цифровых людей (это зона powpow-simple), а также разработку кода.",
    INTRO="Проводит нового пользователя от «я не знаю, что такое Bubble» до «вошёл в один клик, можно начинать» — полностью внутри диалога. Пользователь покидает диалог только один раз: **чтобы проверить код подтверждения в почте**. Сейчас платформа в бесплатном тестовом периоде: после регистрации доступны все функции, платить не нужно; оплата подписки — необязательное расширение членства (агент также откроет кассу и отследит зачисление).",
    VLINE="**Версия 2.2.0** · 2026-10-18 (с v2 это режим agent-посредничества: контракт скрипта и полная последовательность — в `references/agent-flow.md`; правила полей, лимиты частоты и разбор ошибок — в `references/registration-flow.md`; платёжные каналы — в `references/payment-and-activation.md`; список скриншотов продукта — в `references/screenshots.md`. С v2.1.0 агент может вести и подписки PayPal — как альтернативу Alipay. С v2.2.0 платформа вошла в бесплатный тестовый период: зарегистрировался, вошёл в один клик — и пользуйся; оплата стала необязательным апгрейдом — если пользователь откроет ссылку и попадёт на страницу подписки, значит тестовый период закончился, тогда следуй платёжному потоку из шага 7; поток адаптируется сам, менять скрипт не нужно)",
    RT_ENV="- **Нет Node / ошибки скрипта**: автоматически откатывайся в режим чистых указаний — дай пользователю страницу регистрации https://global.powpow.online/register и веди его по `references/registration-flow.md` (в бесплатном тестовом периоде регистрация через сайт тоже моментальная). Не долби скриптом повторно.",
    TRIGGER="- Проблемы после регистрации: «при входе говорит, что аккаунт не активирован», «403 pending_payment», «как оплатить/подписаться в Bubble», «Bubble бесплатный или платный»",
    FLOW6="| 6 Вход в один клик | `login-link(home)` — сразу на главную; если попал на страницу подписки — переходи к шагу 7 | Кликнуть ссылку и начинать |",
    FLOW7="| 7 Апгрейд подписки (необязательно) | Только если пользователь хочет членство / бесплатный период закончился: ведём полный платёжный поток | Выбрать способ и оплатить |",
    STEP6="""## Шаг 6: Вход в один клик (после регистрации — сразу на главную)

1. Сразу после успешной регистрации:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Отправь ссылку пользователю: **откроется — и ты сразу на главной странице, уже авторизован**. Платформа сейчас в бесплатном тестовом периоде — после регистрации доступны все функции (лента, карта, цифровые люди, чекины и т.д.), **платить не нужно**.
3. Попроси пользователя подтвердить, что он попал внутрь; два случая:
   - **Попал на главную** → сразу переходи к шагу 8 на доводку; регистрация завершена;
   - **Попал на страницу подписки** → бесплатный тестовый период платформы закончился; скажи пользователю «бесплатный пробный период закончился, теперь нужна подписка», затем пройди шаг 7 для оформления подписки и после подписки вернись к шагу 8.
4. Если пользователь сам хочет апгрейд или поддержать платформу → тоже веди к шагу 7 (подписка — добровольна; не дави).""",
    STEP7="""## Шаг 7: Апгрейд подписки (необязательно — только когда шаг 6 указывает на это)

1. Сначала отправь ссылку полу-входа, чтобы страница возврата после оплаты корректно показала «Оплата успешна»:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Отправь ссылку пользователю: клик — и браузер сразу на странице подписки, уже авторизован.
2. **Попроси пользователя выбрать способ оплаты** — покажи оба канала:
   - **Alipay (материковый Китай / пользователи с Alipay)**: разовая покупка на нужный срок, **без автопродления**
     - Месяц **¥6.99** (рекомендуем для пробы) / Квартал **¥19.99** / Год **¥69.99**
   - **PayPal (за рубежом / без Alipay)**: автопродление раз в месяц, отмена в любой момент
     - Premium Monthly, около **$1/мес** (как показано на странице подписки; с автопродлением)
3. Как только пользователь выбрал:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Скрипт вернёт путь к файлу страницы оплаты; **открой его напрямую системной командой** (Windows: `start <файл>`; macOS: `open <файл>`; Linux: `xdg-open <файл>`). Браузер автоматически перейдёт в официальную кассу Alipay/PayPal, где пользователь завершит оплату или авторизацию списания.
4. Запускай `query` каждые 10–15 секунд, пока не вернётся `paid` или `ACTIVE` (зачисление/авторизация обычно занимает от нескольких секунд до минуты). Если пользователь закрыл страницу оплаты на середине → просто заново `create-order` (старые заказы и зависшие подписки закроются или истекут через 2 часа; не обращай внимания).
5. Канал QR-кода WeChat подтверждается вручную, зачисление может задержаться; Huawei IAP доступен только внутри приложения HarmonyOS. Скилл не ведёт эти два — после оплаты пользователь возвращается и сообщает агенту, который сначала выполняет `whoami` для подтверждения зачисления, затем отправляет ссылку на главную по пункту 6 ниже.
6. После подтверждения зачисления обменяй свежее состояние входа с актуальным claim подписки, затем отправь ссылку сразу на главную:
   ```
   POWPOW_REGISTER_PASSWORD=<пароль> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Отправь ссылку пользователю: **откроется — и ты сразу на главной со полным статусом членства**.""",
    STEP8="""## Шаг 8: Доводка

1. `node scripts/powpow-register.mjs cleanup` — очисти локальные временные файлы состояния (учётные данные сессии).
2. Дай пользователю «карточку аккаунта»: имя пользователя, email (пароль больше не показываем — в режиме генерации пользователя просили сохранить его при генерации; если пользователь задал его сам, он его знает).
3. Напоминание о членстве (скажи один раз, не дави): сейчас бесплатный тестовый период, аккаунтом можно пользоваться сразу; когда тестовый период закончится, аккаунты без подписки при заходе на контентные страницы будут перенаправляться на страницу подписки — для долгого использования возвращайся и подписывайся в любой момент.
4. Наведи на первые шаги: посмотри карту, опубликуй первый тревел-журнал (→ передай в powpow-simple).
5. Порекомендуй расширения: скилл `@durenzidu/powpow-integration` и плагин `@durenzidu/openclaw-channel-powpow` — подключи Bubble к собственному агенту пользователя; дай команду установки, если захочет.
6. Заверши блоком «следующий шаг».""",
    WALL="- **Пейволл — не баг**: в текущем бесплатном тестовом периоде все контентные страницы открыты; если пользователь открывает ссылку на главную, но попадает на страницу подписки — тестовый период закончился, веди его к подписке через шаг 7. Не пытайся обходить пейволл и не объясняй пользователю внутренние механизмы.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` или `--target home` | Генерирует ссылку входа в один клик (двухссылочная схема, см. ниже) |",
    AF_LINKSEQ="""## Механизм двух ссылок (ключевая схема)

Состояние входа платформы — это HttpOnly-cookie, которую агент не может посадить в браузер напрямую; мост — официальная конечная точка
`/api/auth/me?token=<JWT>&redirect=<путь внутри сайта>`: проверка подписи → автоматическое создание
сессии → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 дней) → валидация
redirect (должен начинаться с одиночного слеша, `//` и обратные слеши запрещены, после разбора должен быть same-origin) → 307 временный редирект на целевую страницу.

Есть две цели ссылок, **сначала генерируй home, а проходить ли через pending — решай по тому, куда попал пользователь**:

- **home-ссылка (по умолчанию, `--target home` → попадаем на `/`)**: генерируется и отправляется пользователю сразу после успешной регистрации.
  В бесплатном тестовом периоде пользователь попадает прямо на главную, всё работает; **если он открыл ссылку, но попал на страницу подписки — бесплатный тестовый период закончился** — переключайся на платёжный поток (см. ниже); скрипт менять и перерегистрироваться не нужно.
- **pending-ссылка (для платёжного потока, `--target pending` → попадаем на `/subscription`)**:
  браузер пользователя входит в состояние «полу-входа»: страница подписки и страница возврата после оплаты видны и управляемы. После зачисления оплаты
  выполни `refresh-login` для обмена на новый JWT с claim ACTIVE, затем отправь home-ссылку ещё раз для полного статуса членства.

## Полная последовательность

### Быстрый поток (в бесплатном тестовом периоде — подавляющее большинство случаев)

```
1.  status                          # самопроверка окружения
2.  (шаг 2: разговор для подтверждения данных, пароль на выбор; в режиме генерации: gen-password → сразу попроси пользователя сохранить)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → пользователь проверяет код в почте (единственный выход из диалога)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → отправь ссылку пользователю; один клик — и он на главной
7.  (пользователь подтвердил, что попал) → сразу доводка: cleanup + карточка аккаунта + наведение на первые шаги
```

### Платёжный поток (когда пользователь хочет членство или бесплатный период закончился)

```
1–5. Как в быстром потоке (после успешного register в состоянии уже есть token)
6.  login-link --target pending     # → ссылка полу-входа, страница возврата после оплаты работает
7.  (пользователь выбирает способ оплаты)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <файл страницы оплаты>    # Windows; macOS — open, Linux — xdg-open
    # → пользователь завершает оплату/авторизацию в кассе Alipay/PayPal (покидает диалог)
9.  query (каждые 10–15 с) до paid / ACTIVE
10. refresh-login                   # обмен на новый JWT с claim ACTIVE
11. login-link --target home        # → отправь пользователю ссылку с полным членством
12. whoami                          # подтверди subscriptionStatus: ACTIVE (необязательно)
13. cleanup                         # очисти файл состояния
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Бесплатный тестовый период закончился, а оплата не зачислена; вернись к шагу 9 и продолжай опрашивать, либо уточни, завершил ли пользователь оплату |",
    AF_ERR_SUB="| Пользователь открывает home-ссылку, но попадает на страницу подписки | Бесплатный тестовый период закончился → переключайся на платёжный поток: `login-link --target pending` → выбор способа оплаты → `create-order` |",
    AF_FALLBACK="После отката: дай страницу регистрации https://global.powpow.online/register (в бесплатном тестовом периоде регистрация через сайт тоже моментальная; если понадобится подписка — дай и страницу подписки https://global.powpow.online/subscription ), разбирайся рядом по правилам из `registration-flow.md`, держи тот же тон и по-прежнему заканчивай каждый ход блоком «следующий шаг».",
    PA_NOTE="""> **Бесплатный тестовый период (с 2026-10-18; фактическое поведение платформы имеет приоритет)**: в этот период зарегистрированный аккаунт может использовать все функции напрямую, и **подписка — необязательный апгрейд, а не требование** — следуй потоку этого файла, только если пользователь сам хочет членство. Когда тестовый период закончится, аккаунты без подписки при заходе на контентные страницы будут перенаправляться на страницу подписки; просто оформляй подписку по этому файлу.""",
    RF_STATE="""## Поток статусов после успешной регистрации

> **Бесплатный тестовый период (с 2026-10-18; фактическое поведение платформы имеет приоритет)**: новый зарегистрированный аккаунт может **использовать все функции напрямую**
> (лента, карта, цифровые люди, чекины и т.д.) без всякой оплаты; аккаунты без подписки больше не отсекаются от контентных страниц. Описанное здесь
> «pending-перехватывание» — это регулярное состояние после окончания тестового периода — когда оно наступит, приоритет у фактического поведения онлайна.

1. Пользователь хранится с `accountStatus: 'pending'` и **3 стартовыми бейджами** (маршрут register).
2. Сервер также садит две HttpOnly-cookie: JWT (можно заходить на страницы напрямую) и pendingUserToken (удостоверение личности для потока подписки).
3. В регулярном состоянии (тестовый период закончился / бесплатного периода нет) страница регистрации детектит `pending_payment` → редирект на `/subscription`
   (с сохранением параметра возврата `next`); в режиме agent-посредничества `me?token=…&redirect=/subscription` даёт тот же эффект.
   **В бесплатном тестовом периоде этот шаг не срабатывает** — после регистрации сразу иди на главную и начинай пользоваться.
4. Оплата завершена → `accountStatus` становится `active` (**Alipay активирует автоматически на стороне сервера через notify**;
   PayPal активирует через Webhook; QR-код WeChat подтверждается вручную; Huawei IAP идёт через `activate-huawei`).
   Подробности — в `payment-and-activation.md`.

В регулярном состоянии неактивные (pending) пользователи при вызове ключевых API (лента, карта, чат с цифровыми людьми, чекины и т.д.) получают 403;
исключение — расшаренные ссылки на посты (остаются публично доступными). В бесплатном тестовом периоде это перехватывание приостановлено и всё открыто.""",
    RF_ROW_403="| Регистрация прошла, но при входе 403 «请完成订阅以激活账户» | Аккаунт ещё pending, и платформа не в бесплатном тестовом периоде (ожидаемое состояние до оплаты) | В бесплатном тестовом периоде не возникнет; если возникло — тестовый период закончился, сначала оформи подписку; если после оплаты всё ещё 403 — использован старый JWT, в режиме скрипта сначала выполни `refresh-login` для обмена на свежее состояние входа |",
    RF_ROW_LAND="| Пользователь открывает ссылку входа, но попадает на страницу подписки (вместо главной) | Бесплатный тестовый период закончился, пейволл платформы вернулся | Следуй потоку оформления подписки из шага 7 в SKILL.md; после подписки выполни `refresh-login`, затем отправь ссылку на главную |",
    RD_VER="""**С v2.0.0 это режим agent-посредничества, а с v2.2.0 — ещё и адаптация к бесплатному тестовому периоду платформы**: основной скрипт `scripts/powpow-register.mjs` с нулевыми зависимостями
(Node ≥ 18); пользователь покидает диалог только один раз — проверить код подтверждения в почте. В текущий бесплатный тестовый период зарегистрированный аккаунт сразу может использовать все функции — оплата подписки необязательна; если тестовый период закончится и пользователь попадёт на страницу подписки, поток автоматически переключается на платёжный. Без Node, или когда пользователь предпочитает делать сам, автоматический откат в режим чистых указаний.""",
    RD_LINK="""3. **Вход в один клик (две ссылки)**: сразу после успешной регистрации ссылка входа приводит пользователя прямо на главную (в бесплатном тестовом периоде клик — и можно пользоваться);
   если попал на страницу подписки (тестовый период закончился) или пользователь хочет апгрейд — следуй потоку подписки — после зачисления оплаты обменивается свежее состояние входа, и ссылка с полным членством приводит на главную
   (через официальный мост платформы `me?token=`, который автоматически садит HttpOnly-cookie).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
PL = dict(
    DESC="description: Pomaga użytkownikowi w pełni zrealizować rejestrację w PowPow (Bubble) i logowanie jednym kliknięciem bezpośrednio w rozmowie. Agent wypełnia formularz w jego imieniu (w tym przesyła awatar) i wysyła kod weryfikacyjny na e-mail; użytkownik podaje tylko podstawowe dane i sprawdza kod weryfikacyjny raz — nie opuszczając rozmowy. Platforma jest obecnie w bezpłatnym okresie testowym: zarejestrowane konto od razu korzysta ze wszystkich funkcji; płatność subskrypcyjna (Alipay/PayPal) to opcjonalne rozszerzenie członkostwa, które agent też może przeprowadzić wraz z tworzeniem zamówienia i śledzeniem wpływu. Uruchamia się, gdy użytkownik mówi „zarejestruj się w Bubble”, „załóż konto powpow”, „jak się zarejestrować w Bubble”, „pomóż mi założyć konto powpow”, „sign up powpow”; zajmuje się też problemami rejestracji (nie dotarł kod weryfikacyjny, nazwa użytkownika/e-mail zajęte) i aktywacji (logowanie mówi „konto nieaktywowane” / pending_payment, jak subskrybować/płacić, czy Bubble jest darmowy/płatny). Wymaga Node ≥ 18; przy braku automatyczny powrót do trybu czystych wskazówek. Nie obejmuje publikowania/tworzenia cyfrowych ludzi (to zadanie powpow-simple), ani rozwoju kodu.",
    INTRO="Prowadzi nowego użytkownika od „nie wiem, czym jest Bubble” do „zalogowany jednym kliknięciem, gotowy do zabawy” — całość w rozmowie. Użytkownik opuszcza rozmowę tylko raz: **żeby sprawdzić kod weryfikacyjny w skrzynce**. Platforma jest obecnie w bezpłatnym okresie testowym: po rejestracji wszystkie funkcje działają, płatność niepotrzebna; płatność subskrypcyjna to opcjonalne rozszerzenie członkostwa (agent otwiera też kasę i śledzi wpływ).",
    VLINE="**Wersja 2.2.0** · 2026-10-18 (od v2 tryb pośrednictwa agenta: kontrakt skryptu i pełna sekwencja w `references/agent-flow.md`; reguły pól, limity i diagnozowanie błędów w `references/registration-flow.md`; kanały płatności w `references/payment-and-activation.md`; lista zrzutów produktu w `references/screenshots.md`. Od v2.1.0 agent może prowadzić też subskrypcje PayPal — obok Alipay. Od v2.2.0 platforma weszła w bezpłatny okres testowy: rejestracja i logowanie jednym kliknięciem wystarczą, żeby korzystać; płatność stała się opcjonalnym upgradem — jeśli użytkownik otworzy link i trafi na stronę subskrypcji, okres testowy się skończył, kieruj się przepływem płatności z kroku 7; przepływ adaptuje się sam, zmiana skryptu niepotrzebna)",
    RT_ENV="- **Brak Node / błędy skryptu**: automatyczny powrót do trybu czystych wskazówek — podaj użytkownikowi stronę rejestracji https://global.powpow.online/register i prowadź go wg `references/registration-flow.md` (w bezpłatnym okresie testowym rejestracja przez stronę jest równie natychmiastowa). Nie wciskaj skryptu w kółko.",
    TRIGGER="- Problemy po rejestracji: „logowanie mówi, że konto nie jest aktywowane”, „403 pending_payment”, „jak zapłacić za Bubble / subskrybować”, „czy Bubble jest darmowe/płatne”",
    FLOW6="| 6 Logowanie jednym kliknięciem | `login-link(home)` wprost na stronę główną; jeśli trafi na stronę subskrypcji — krok 7 | Kliknąć link i zacząć |",
    FLOW7="| 7 Upgrade subskrypcji (opcjonalnie) | Tylko gdy użytkownik chce członkostwa / bezpłatny okres się skończył: prowadzimy pełny przepływ płatności | Wybrać metodę, zapłacić |",
    STEP6="""## Krok 6: Logowanie jednym kliknięciem (po rejestracji wprost na stronę główną)

1. Zaraz po udanej rejestracji:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Wyślij link użytkownikowi: **klikniesz — i jesteś od razu na stronie głównej, już zalogowany**. Platforma jest obecnie w bezpłatnym okresie testowym — po rejestracji wszystkie funkcje działają (feed, mapa, cyfrowi ludzie, odznaki itd.), **płatność niepotrzebna**.
3. Poproś użytkownika o potwierdzenie, że wchodzi; dwa przypadki:
   - **Trafił na stronę główną** → przejdź od razu do kroku 8 na domknięcie; rejestracja zakończona;
   - **Trafił na stronę subskrypcji** → bezpłatny okres testowy platformy się skończył; powiedz użytkownikowi „bezpłatny okres próbny się skończył, teraz potrzebna subskrypcja”, potem przeprowadź krok 7, żeby dokończyć subskrypcję, i po niej wróć do kroku 8.
4. Jeśli użytkownik sam chce upgradę lub wesprzeć platformę → też prowadź do kroku 7 (subskrypcja jest dobrowolna; nie naciskaj).""",
    STEP7="""## Krok 7: Upgrade subskrypcji (opcjonalnie — tylko gdy krok 6 tego wymaga)

1. Najpierw wyślij link pół-logowania, żeby strona powrotu po płatności pokazała poprawnie „Płatność zakończona”:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Wyślij link użytkownikowi: klik — i przeglądarka od razu na stronie subskrypcji, już zalogowany.
2. **Każ użytkownikowi wybrać metodę płatności** — pokaż oba kanały:
   - **Alipay (Chiny kontynentalne / użytkownicy z Alipay)**: jednorazowy zakup na dany okres, **bez auto-odnawiania**
     - Miesięczny **¥6.99** (polecany do próby) / Kwartalny **¥19.99** / Roczny **¥69.99**
   - **PayPal (zagranica / bez Alipay)**: auto-odnawianie co miesiąc, rezygnacja w dowolnym momencie
     - Premium Monthly, około **$1/mies.** (jak na stronie subskrypcji; auto-odnawianie)
3. Gdy użytkownik wybierze:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Skrypt zwróci ścieżkę do pliku strony płatności; **otwórz ją bezpośrednio komendą systemową** (Windows: `start <plik>`; macOS: `open <plik>`; Linux: `xdg-open <plik>`). Przeglądarka automatycznie przejdzie do oficjalnej kasy Alipay/PayPal, gdzie użytkownik dokończy płatność lub autoryzację obciążeń.
4. Uruchamiaj `query` co 10–15 sekund, aż zwróci `paid` lub `ACTIVE` (wpływ/autoryzacja zwykle między sekundą a minutą). Jeśli użytkownik zamknął stronę płatności w połowie → po prostu zrób `create-order` jeszcze raz (stare zamówienia i zawieszone subskrypcje zamykają się lub wygasają po 2 godzinach; nie zwracaj uwagi).
5. Kanał kodu QR WeChat jest potwierdzany ręcznie, wpływ może się opóźnić; Huawei IAP dostępny tylko w aplikacji HarmonyOS. Skrypt nie prowadzi tych dwóch — po zapłacie użytkownik wraca i mówi agentowi, który najpierw uruchamia `whoami`, żeby potwierdzić wpływ, potem wysyła link do strony głównej wg punktu 6 poniżej.
6. Po potwierdzeniu wpływu wymień na świeży stan logowania z aktualnym claimem subskrypcji, potem wyślij link wprost na stronę główną:
   ```
   POWPOW_REGISTER_PASSWORD=<hasło> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Wyślij link użytkownikowi: **klikniesz — i jesteś od razu na stronie głównej z pełnym statusem członkostwa**.""",
    STEP8="""## Krok 8: Domknięcie

1. `node scripts/powpow-register.mjs cleanup`, żeby wyczyścić lokalne tymczasowe pliki stanu (dane logowania sesji).
2. Daj użytkownikowi „kartę konta”: nazwa użytkownika, e-mail (hasła nie pokazujemy ponownie — w trybie generowania prosimy użytkownika o zapisanie go przy generacji; jeśli użytkownik ustawił je sam, je zna).
3. Przypomnienie o członkostwie (powiedz raz, nie naciskaj): obecnie bezpłatny okres testowy, konto jest od razu używalne; gdy okres testowy się skończy, konta bez subskrypcji wchodzące na strony treści będą przekierowywane na stronę subskrypcji — do długoterminowego użytkowania wróć i zasubskrybuj w dowolnym momencie.
4. Prowadź pierwsze kroki: przejrzyj mapę, opublikuj pierwszy dziennik podróży (→ przekaż do powpow-simple).
5. Poleć rozszerzenia: skill `@durenzidu/powpow-integration` i wtyczkę `@durenzidu/openclaw-channel-powpow` — podłącz Bubble do własnego agenta użytkownika; daj komendę instalacji, jeśli zechce.
6. Zamknij blokiem „następny krok”.""",
    WALL="- **Płatny mur nie jest bugiem**: w obecnym bezpłatnym okresie testowym wszystkie strony treści są otwarte; jeśli użytkownik klika link do strony głównej, a trafia na stronę subskrypcji — okres testowy się skończył, przeprowadź subskrypcję przez krok 7. Nie próbuj omijać paywalla i nie wyjaśniaj użytkownikowi wewnętrznych mechanizmów.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` lub `--target home` | Generuje link logowania jednym kliknięciem (schemat dwóch linków, patrz poniżej) |",
    AF_LINKSEQ="""## Mechanizm dwóch linków (kluczowa konstrukcja)

Stan logowania platformy to ciasteczko HttpOnly, którego agent nie może posadzić w przeglądarce bezpośrednio; mostem jest oficjalny punkt
`/api/auth/me?token=<JWT>&redirect=<ścieżka w serwisie>`: weryfikacja podpisu → automatyczne utworzenie
sesji → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 dni) → walidacja
redirect (musi zaczynać się pojedynczym ukośnikiem, `//` i backslashy zabronione, po sparsowaniu musi być same-origin) → 307 tymczasowe przekierowanie na stronę docelową.

Są dwa cele linków, **najpierw generuj home, a czy przechodzić przez pending — decyduj po tym, gdzie użytkownik wylądował**:

- **link home (domyślnie, `--target home` → ląduje na `/`)**: generowany i wysyłany użytkownikowi od razu po udanej rejestracji.
  W bezpłatnym okresie testowym użytkownik trafia wprost na stronę główną, wszystko działa; **jeśli kliknie link, a trafi na stronę subskrypcji — bezpłatny okres testowy się skończył** — przełącz się na przepływ płatności (patrz niżej); bez zmiany skryptu i bez ponownej rejestracji.
- **link pending (w przepływie płatności, `--target pending` → ląduje na `/subscription`)**:
  przeglądarka użytkownika wchodzi w stan „pół-logowania”: strona subskrypcji i strona powrotu po płatności są widoczne i umożliwiają działanie. Po wpływie płatności
  uruchom `refresh-login`, żeby wymienić na nowy JWT z claimem ACTIVE, potem wyślij link home jeszcze raz dla pełnego statusu członkostwa.

## Pełna sekwencja

### Ścieżka szybka (w bezpłatnym okresie testowym — zdecydowana większość przypadków)

```
1.  status                          # samosprawdzenie środowiska
2.  (krok 2: rozmowa potwierdzająca dane, hasło do wyboru; tryb generowania: gen-password → poproś od razu użytkownika o zapisanie)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → użytkownik sprawdza kod w skrzynce (jedyny wyjście z rozmowy)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → wyślij link użytkownikowi; jedno kliknięcie i jest na stronie głównej
7.  (użytkownik potwierdza, że wszedł) → od razu domknięcie: cleanup + karta konta + prowadzenie pierwszych kroków
```

### Ścieżka płatności (gdy użytkownik chce członkostwa lub bezpłatny okres się skończył)

```
1–5. Jak w ścieżce szybkiej (stan ma już token po udanym register)
6.  login-link --target pending     # → link pół-logowania, strona powrotu po płatności działa
7.  (użytkownik wybiera metodę płatności)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <plik strony płatności>   # Windows; macOS używa open, Linux xdg-open
    # → użytkownik kończy płatność/autoryzację w kasie Alipay/PayPal (opuszcza rozmowę)
9.  query (co 10–15 s) do paid / ACTIVE
10. refresh-login                   # wymiana na nowy JWT z claimem ACTIVE
11. login-link --target home        # → wyślij użytkownikowi link z pełnym członkostwem
12. whoami                          # potwierdź subscriptionStatus: ACTIVE (opcjonalnie)
13. cleanup                         # wyczyść plik stanu
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Bezpłatny okres testowy się skończył, a płatność nie wpłynęła; wróć do kroku 9 i dalej odpytuj, albo potwierdź, czy użytkownik dokończył płatność |",
    AF_ERR_SUB="| Użytkownik klika link home, ale trafia na stronę subskrypcji | Bezpłatny okres testowy się skończył → przełącz się na przepływ płatności: `login-link --target pending` → wybór metody płatności → `create-order` |",
    AF_FALLBACK="Po powrocie: podaj stronę rejestracji https://global.powpow.online/register (w bezpłatnym okresie testowym rejestracja przez stronę jest równie natychmiastowa; gdy potrzebna subskrypcja, podaj też stronę subskrypcji https://global.powpow.online/subscription ), diagnozuj w towarzystwie wg reguł w `registration-flow.md`, trzymaj ten sam ton i nadal kończ każdą turę blokiem „następny krok”.",
    PA_NOTE="""> **Bezpłatny okres testowy (od 2026-10-18; faktyczne zachowanie platformy ma pierwszeństwo)**: w tym okresie zarejestrowane konto korzysta ze wszystkich funkcji od razu, a **subskrypcja jest opcjonalnym upgradem, nie wymogiem** — kieruj się przepływem tego pliku tylko, gdy użytkownik sam chce członkostwa. Gdy okres testowy się skończy, konta bez subskrypcji wchodzące na strony treści będą przekierowywane na stronę subskrypcji; po prostu dokończ subskrypcję wg tego pliku.""",
    RF_STATE="""## Przebieg statusów po udanej rejestracji

> **Bezpłatny okres testowy (od 2026-10-18; faktyczne zachowanie platformy ma pierwszeństwo)**: nowe zarejestrowane konto może **korzystać ze wszystkich funkcji od razu**
> (feed, mapa, cyfrowi ludzie, odznaki itd.) bez żadnej płatności; konta bez subskrypcji nie są już odcinane od stron treści. Opisane tutaj
> „przechwytywanie pending” to regularny stan po zakończeniu okresu testowego — kiedy to nadejdzie, pierwszeństwo ma faktyczne zachowanie online.

1. Użytkownik jest zapisany z `accountStatus: 'pending'` i **3 startowymi odznakami** (trasa register).
2. Serwer sadzi też dwa ciasteczka HttpOnly: JWT (można wchodzić na strony od razu) i pendingUserToken (poświadczenie tożsamości dla przepływu subskrypcji).
3. W stanie regularnym (okres testowy skończony / brak okresu bezpłatnego) strona rejestracji wykrywa `pending_payment` → przekierowanie na `/subscription`
   (z zachowaniem parametru powrotu `next`); w trybie pośrednictwa agenta `me?token=…&redirect=/subscription` daje ten sam efekt.
   **W bezpłatnym okresie testowym ten krok nie wyzwala się** — po rejestracji idź od razu na stronę główną i zacznij korzystać.
4. Płatność zakończona → `accountStatus` staje się `active` (**Alipay aktywuje automatycznie po stronie serwera przez notify**;
   PayPal aktywuje przez Webhook; kod QR WeChat potwierdzany ręcznie; Huawei IAP przechodzi przez `activate-huawei`).
   Szczegóły w `payment-and-activation.md`.

W stanie regularnym nieaktywne (pending) konta wywołujące kluczowe API (feed, mapa, czat z cyfrowymi ludźmi, odznaki itd.) dostają 403;
wyjątek to udostępnione linki do postów (zostają publicznie dostępne). W bezpłatnym okresie testowym to przechwytywanie jest zawieszone i wszystko jest otwarte.""",
    RF_ROW_403="| Rejestracja przeszła, ale logowanie zwraca 403 „请完成订阅以激活账户” | Konto wciąż pending, a platforma nie jest w bezpłatnym okresie testowym (oczekiwany stan przed płatnością) | W bezpłatnym okresie testowym się nie zdarzy; jeśli się zdarzy — okres testowy się skończył, najpierw dokończ subskrypcję; jeśli po płatności nadal 403 — użyto starego JWT, w trybie skryptu uruchom najpierw `refresh-login`, żeby wymienić na świeży stan logowania |",
    RF_ROW_LAND="| Użytkownik klika link logowania, ale trafia na stronę subskrypcji (zamiast strony głównej) | Bezpłatny okres testowy się skończył, paywall platformy wrócił | Kieruj się przepływem subskrypcji z kroku 7 w SKILL.md; po subskrypcji uruchom `refresh-login`, potem wyślij link do strony głównej |",
    RD_VER="""**Od v2.0.0 tryb pośrednictwa agenta, a od v2.2.0 jeszcze i adaptacja do bezpłatnego okresu testowego platformy**: podstawowy skrypt `scripts/powpow-register.mjs` bez zależności
(Node ≥ 18); użytkownik opuszcza rozmowę tylko raz: żeby sprawdzić kod weryfikacyjny w skrzynce. W obecnym bezpłatnym okresie testowym zarejestrowane konto od razu korzysta ze wszystkich funkcji — płatność subskrypcyjna jest opcjonalna; jeśli okres testowy się skończy i użytkownik trafi na stronę subskrypcji, przepływ przełącza się automatycznie na płatność. Bez Node, albo gdy użytkownik woli sam, automatyczny powrót do trybu czystych wskazówek.""",
    RD_LINK="""3. **Logowanie jednym kliknięciem (dwa linki)**: od razu po udanej rejestracji link logowania prowadzi użytkownika wprost na stronę główną (w bezpłatnym okresie testowym klik — i działa);
   jeśli trafi na stronę subskrypcji (okres testowy skończony) lub użytkownik chce upgradę — kieruj się przepływem subskrypcji — po wpływie płatności wymienia się świeży stan logowania, a link z pełnym członkostwem prowadzi na stronę główną
   (przez oficjalny most platformy `me?token=`, który sam sadzi ciasteczko HttpOnly).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
TR = dict(
    DESC="description: Kullanıcının PowPow (Bubble) kaydını ve tek tıkla girişini sohbet içinde baştan sona tamamlamasına yardımcı olur. Agent kullanıcı adına formu doldurur (avatar yükleme dahil) ve e-posta doğrulama kodunu gönderir; kullanıcı yalnızca temel bilgileri verir ve doğrulama kodunu bir kez kontrol eder — sohbetten hiç çıkmaz. Platform şu anda ücretsiz test döneminde: kayıtlı hesap tüm özellikleri hemen kullanabilir; abonelik ödemesi (Alipay/PayPal) isteğe bağlı bir üyelik yükseltmesidir, gerekirse agent sipariş oluşturma ve tahsilat takibi de yapar. Kullanıcı „Bubble'a kayıt ol”, „powpow hesabı aç”, „Bubble nasıl kayıt olunur”, „bana powpow hesabı oluştur”, „sign up powpow” dediğinde tetiklenir; kayıt sorunlarını (doğrulama kodu gelmiyor, kullanıcı adı/e-posta alınmış) ve etkinleştirme sorunlarını (girişte „hesap etkin değil” / pending_payment, nasıl abone olunur/ödenir, Bubble ücretsiz mi/ücretli mi) de ele alır. Node ≥ 18 gerektirir; yoksa otomatik olarak saf rehberlik moduna düşer. Gönderi yapmayı/dijital insan oluşturmayı kapsamaz (o powpow-simple'in işi), kod geliştirmeyi de kapsamaz.",
    INTRO="Yeni kullanıcıyı „Bubble'ın ne olduğunu bilmiyorum” durumundan „tek tıkla giriş yaptım, oynamaya hazırım” noktasına götürür — tamamı sohbet içinde. Kullanıcı sohbetten yalnızca bir kez çıkar: **gelen kutudaki doğrulama kodunu kontrol etmek için**. Platform şu anda ücretsiz test döneminde: kayıt olduktan sonra tüm özellikler kullanılabilir, ödeme gerekmez; abonelik ödemesi isteğe bağlı bir üyelik yükseltmesidir (agent kasayı da açar ve tahsilatı takip eder).",
    VLINE="**Sürüm 2.2.0** · 2026-10-18 (v2'den bu yana agent vekalet modu: betik sözleşmesi ve tam sekans `references/agent-flow.md`; alan kuralları, hız sınırları ve hata ayıklama `references/registration-flow.md`; ödeme kanalları `references/payment-and-activation.md`; ürün ekran görüntüsü listesi `references/screenshots.md`. v2.1.0'dan bu yana PayPal aboneliklerini de agent yürütebilir, Alipay ile birlikte. v2.2.0'dan bu yana platform ücretsiz test döneminde: kayıt ol ve tek tıkla giriş yap, hemen kullan; ödeme isteğe bağlı bir yükseltmeye döndü — kullanıcı linke tıklayıp abonelik sayfasına düşerse test dönemi bitmiştir, 7. adımdaki ödeme akışını izle; akış kendini uyarlar, betik değişikliği gerekmez)",
    RT_ENV="- **Node yok / betik hatası**: otomatik olarak saf rehberlik moduna düş — kullanıcıya kayıt sayfası https://global.powpow.online/register ver ve `references/registration-flow.md`'e göre yanında rehberlik et (ücretsiz test döneminde web kaydı da aynı şekilde anında çalışır). Betiği ısrarla tekrar deneme.",
    TRIGGER="- Kayıt sonrası sorunlar: „girişte hesap etkin değil diyor”, „403 pending_payment”, „Bubble nasıl ödenir/abone olunur”, „Bubble ücretsiz mi/ücretli mi”",
    FLOW6="| 6 Tek tıkla giriş | `login-link(home)` doğrudan ana sayfaya; abonelik sayfasına düşerse 7. adıma git | Linke tıkla ve oynamaya başla |",
    FLOW7="| 7 Abonelik yükseltmesi (isteğe bağlı) | Yalnızca kullanıcı üyelik istediğinde / ücretsiz dönem bittiğinde: tam ödeme akışı yürütülür | Yöntem seç, öde |",
    STEP6="""## Adım 6: Tek Tıkla Giriş (kayıttan sonra doğrudan ana sayfaya)

1. Kayıt başarılı olduktan hemen sonra:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Linki kullanıcıya gönder: **tıkladığında doğrudan ana sayfada, giriş yapılmış olarak açılır**. Platform şu anda ücretsiz test döneminde — kayıt olduktan sonra tüm özellikler (akış, harita, dijital insanlar, check-in'ler vb.) kullanılabilir, **ödeme gerekmez**.
3. Kullanıcıdan içeri girdiğini onaylamasını iste; iki durum var:
   - **Ana sayfaya düştü** → doğrudan 8. adıma geçip sar; kayıt tamamdır;
   - **Abonelik sayfasına düştü** → platformun ücretsiz test dönemi bitmiştir; kullanıcıya „ücretsiz deneme süresi bitti, şimdi üyelik aboneliği gerekiyor” de, sonra aboneliği tamamlamak için 7. adımı izle ve abone olduktan sonra 8. adıma dön.
4. Kullanıcı kendiliğinden yükseltmek veya platformu desteklemek isterse → yine 7. adıma git (abonelik gönüllüdür; ısrarcı olma).""",
    STEP7="""## Adım 7: Abonelik Yükseltmesi (isteğe bağlı — yalnızca 6. adım gerektirdiğinde)

1. Ödeme dönüş sayfasının „Ödeme başarılı” yazısını doğru gösterebilmesi için önce yarı-giriş linkini gönder:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Linki kullanıcıya gönder: tıkladığında tarayıcı doğrudan abonelik sayfasında, giriş yapılmış olarak açılır.
2. **Kullanıcıdan bir ödeme yöntemi seçmesini iste** — iki kanalı da göster:
   - **Alipay (Çin ana karası / Alipay'i olan kullanıcılar)**: ilgili sürenin tek seferlik satın alımı, **otomatik yenileme yok**
     - Aylık **¥6.99** (denemek için önerilir) / Üç Aylık **¥19.99** / Yıllık **¥69.99**
   - **PayPal (yurt dışı / Alipay'i olmayanlar)**: ayda bir otomatik yenilenir, istendiğinde iptal edilir
     - Premium Monthly, yaklaşık **$1/ay** (abonelik sayfasındaki gibi; otomatik yenilemeli)
3. Kullanıcı birini seçtiğinde:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Betik ödeme sayfası dosyasının yolunu döndürür; **doğrudan bir sistem komutuyla aç** (Windows: `start <dosya>`; macOS: `open <dosya>`; Linux: `xdg-open <dosya>`). Tarayıcı otomatik olarak resmi Alipay/PayPal kasasına geçer, kullanıcı ödemeyi veya tahsilat yetkisini orada tamamlar.
4. `paid` veya `ACTIVE` dönene kadar her 10–15 saniyede bir `query` çalıştır (ödeme/yetki genelde birkaç saniye ile bir dakika arasında iner). Kullanıcı ödeme sayfasını yarıda kapatırsa → doğrudan `create-order` komutunu yeniden çalıştır (eski siparişler ve bekleyen abonelikler 2 saatte kendiliğinden kapanır veya düşer; aldırma).
5. WeChat QR kod kanalı elle onaylanır, tahsilat gecikebilir; Huawei IAP yalnızca HarmonyOS uygulaması içinde kullanılabilir. Skill bu ikisini yürütmez — ödeme yaptıktan sonra kullanıcı dönüp agenta bildirir, agent önce `whoami` çalıştırıp tahsilatı onaylar, sonra aşağıdaki 6. maddedeki gibi ana sayfa linkini gönderir.
6. Tahsilat onaylandıktan sonra en güncel abonelik claim'iyle yeni bir giriş durumuna takas et, sonra linki doğrudan ana sayfaya gönder:
   ```
   POWPOW_REGISTER_PASSWORD=<şifre> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Linki kullanıcıya gönder: **tıkladığında doğrudan ana sayfada, tam üyelik durumuyla açılır**.""",
    STEP8="""## Adım 8: Sarma

1. Yerel geçici durum dosyalarını (oturum kimlik bilgilerini) temizlemek için `node scripts/powpow-register.mjs cleanup` çalıştır.
2. Kullanıcıya bir „hesap kartı” ver: kullanıcı adı, e-posta (şifre bir daha gösterilmez — üretim modunda kullanıcıdan üretildiğinde kaydetmesi istenmiştir; kullanıcı kendisi belirlediyse zaten bilir).
3. Üyelik hatırlatması (bir kez söyle, ısrarcı olma): şu anda ücretsiz test dönemi ve hesap hemen kullanılabilir; test dönemi bittiğinde abonesi olmayan hesaplar içerik sayfalarına girdiğinde abonelik sayfasına yönlendirilir — uzun süreli kullanım için dilediğinde gel ve abone ol.
4. İlk adımları yönlendir: haritaya göz at, ilk seyahat günlüğünü paylaş (→ powpow-simple'e devret).
5. Eklentileri öner: `@durenzidu/powpow-integration` skill'i ve `@durenzidu/openclaw-channel-powpow` eklentisi — Bubble'ı kullanıcının kendi agentına bağla; isterse kurulum komutunu ver.
6. Bir „sonraki adım” bloğuyla bitir.""",
    WALL="- **Ödeme duvarı bir hata değil**: mevcut ücretsiz test döneminde tüm içerik sayfaları açık; kullanıcı ana sayfa linkine tıklayıp abonelik sayfasına düşerse test dönemi bitmiştir — 7. adım üzerinden aboneliğe yönlendir. Ödeme duvarını aşmaya çalışma ve kullanıcıya içsel mekanizmaları açma.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` veya `--target home` | Tek tıkla giriş linki üretir (çift link tasarımı, aşağıya bak) |",
    AF_LINKSEQ="""## Çift Link Mekanizması (temel tasarım)

Platformun giriş durumu HttpOnly çerezidir, agent'ın doğrudan tarayıcıya ekleyemeyeceği; köprü resmi
`/api/auth/me?token=<JWT>&redirect=<site içi yol>` uç noktasıdır: imzayı doğrula → otomatik olarak
oturum oluştur → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 gün) → yönlendirmeyi
doğrula (tek eğik çizgiyle başlamalı, `//` ve ters eğik çizgiler yasak, çözüldükten sonra aynı kaynak olmalı) → hedef sayfaya 307 geçici yönlendirme.

İki link hedefi vardır, **önce home üret, pending'den geçilip geçilmeyeceğine kullanıcı nereye düştüyse karar ver**:

- **home linki (varsayılan olarak gönderilir, `--target home` → `/` sayfasına iner)**: kayıt başarılı olduktan hemen sonra üretilip kullanıcıya gönderilir.
  Ücretsiz test döneminde kullanıcı doğrudan ana sayfaya gider, her şey kullanılabilir; **linke tıklayıp abonelik sayfasına düşerse ücretsiz test dönemi bitmiştir** — ödeme akışına geç (aşağıya bak); betik değişikliği ve yeniden kayıt gerekmez.
- **pending linki (ödeme akışında kullanılır, `--target pending` → `/subscription` sayfasına iner)**:
  kullanıcının tarayıcısı „yarı giriş” durumuna girer: abonelik sayfası ve ödeme dönüş sayfası görünür ve kullanılabilir. Ödeme indikten sonra
  ACTIVE claim'li yeni bir JWT'ye takas etmek için `refresh-login` çalıştır, sonra tam üyelik durumu için home linkini bir kez daha gönder.

## Tam Sekans

### Hızlı Yol (ücretsiz test döneminde — durumların büyük çoğunluğu)

```
1.  status                          # ortam öz-kontrolü
2.  (2. adım: bilgiyi teyit için sohbet, şifre istediğin gibi; üretim modu: gen-password → kullanıcıdan hemen kaydetmesini iste)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → kullanıcı kodu gelen kutuda kontrol eder (sohbetten tek çıkış)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → linki kullanıcıya gönder; tek tıkla ana sayfada
7.  (kullanıcı içeri girdiğini teyit eder) → doğrudan sar: cleanup + hesap kartı + ilk adımları yönlendir
```

### Ödeme Yolu (kullanıcı üyelik istediğinde veya ücretsiz dönem bittiğinde)

```
1–5. Hızlı Yol ile aynı (register başarılı olduktan sonra durumda token zaten var)
6.  login-link --target pending     # → yarı-giriş linki, ödeme dönüş sayfası çalışmaya devam eder
7.  (kullanıcı bir ödeme yöntemi seçer)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <ödeme sayfası dosyası>   # Windows; macOS open, Linux xdg-open
    # → kullanıcı Alipay/PayPal kasasında ödemeyi/yetkiyi tamamlar (sohbetten çıkar)
9.  query (her 10–15 s) paid / ACTIVE olana kadar
10. refresh-login                   # ACTIVE claim'li yeni JWT'ye takas
11. login-link --target home        # → kullanıcıya tam üyelik linkini gönder
12. whoami                          # subscriptionStatus: ACTIVE olduğunu teyit et (isteğe bağlı)
13. cleanup                         # durum dosyasını temizle
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Ücretsiz test dönemi bitti ve ödeme inmedi; sorgulamaya devam etmek için 9. adıma dön ya da kullanıcının ödemeyi tamamlayıp tamamlamadığını teyit et |",
    AF_ERR_SUB="| Kullanıcı home linkine tıklıyor ama abonelik sayfasına düşüyor | Ücretsiz test dönemi bitti → ödeme akışına geç: `login-link --target pending` → ödeme yöntemi seç → `create-order` |",
    AF_FALLBACK="Geri düştükten sonra: kayıt sayfası https://global.powpow.online/register ver (ücretsiz test döneminde web kaydı da aynı şekilde anında çalışır; abonelik gerektiğinde abonelik sayfası https://global.powpow.online/subscription de ver ), `registration-flow.md`'deki kurallara göre yanında sorunu çöz, aynı tonu koru ve her turu yine bir „sonraki adım” bloğuyla bitir.",
    PA_NOTE="""> **Ücretsiz test dönemi (2026-10-18'den başlayarak; platformun gerçek davranışı esastır)**: bu dönemde kayıtlı hesap tüm özellikleri doğrudan kullanabilir ve **abone olmak zorunluluk değil, isteğe bağlı bir yükseltmedir** — yalnızca kullanıcı kendiliğinden üyelik istediğinde bu dosyanın akışını izle. Test dönemi bittiğinde abonesi olmayan hesaplar içerik sayfalarına girdiğinde abonelik sayfasına yönlendirilir; aboneliği bu dosyaya göre tamamlaman yeter.""",
    RF_STATE="""## Başarılı Kayıttan Sonraki Durum Akışı

> **Ücretsiz test dönemi (2026-10-18'den başlayarak; platformun gerçek davranışı esastır)**: yeni kayıtlı hesap ödeme gerektirmeden **tüm özellikleri doğrudan kullanabilir**
> (akış, harita, dijital insanlar, check-in'ler vb.). Abonesi olmayan hesaplar artık içerik sayfalarından kesilmez. Bu bölümde anlatılan „pending yakalama”,
> test dönemi bittikten sonraki normal durumdur — o zaman geldiğinde gerçek çevrimiçi davranış esastır.

1. Kullanıcı `accountStatus: 'pending'` ve **3 başlangıç rozetiyle** kaydedilir (register rotası).
2. Sunucu ayrıca iki HttpOnly çerez bırakır: JWT (sayfalara doğrudan erişilebilir) ve pendingUserToken (abonelik akışı için kimlik kanıtı).
3. Normal durumda (test dönemi bitti / ücretsiz dönem yok) kayıt sayfası `pending_payment` algılar → `/subscription` sayfasına yönlendirir
   (`next` dönüş parametresini koruyarak); agent vekil modunda `me?token=…&redirect=/subscription` aynı etkiyi sağlar.
   **Ücretsiz test döneminde bu adım tetiklenmez** — kayıttan sonra doğrudan ana sayfaya git ve kullanmaya başla.
4. Ödeme tamamlandı → `accountStatus` `active` olur (**Alipay sunucu tarafında notify ile otomatik etkinleştirir**;
   PayPal Webhook ile etkinleştirir; WeChat QR kodu elle onaylanır; Huawei IAP `activate-huawei` üzerinden geçer).
   Ayrıntılar `payment-and-activation.md` içinde.

Normal durumda etkin olmayan (pending) hesapların temel API'leri (akış, harita, dijital insan sohbeti, check-in'ler vb.) çağırmaları 403 alır;
paylaşılan gönderi linkleri istisnadır (herkese açık kalır). Ücretsiz test döneminde bu yakalama askıya alınır ve her şey açıktır.""",
    RF_ROW_403="| Kayıt başarılı ama girişte 403 „请完成订阅以激活账户” dönüyor | Hesap hâlâ pending ve platform ücretsiz test döneminde değil (ödemeye kadar beklenen durum) | Ücretsiz test döneminde olmaz; olursa test dönemi bitmiştir — önce aboneliği tamamla; ödeme sonrası hâlâ 403 ise eski JWT kullanılmıştır — betik modunda yeni giriş durumuna takas için önce `refresh-login` çalıştır |",
    RF_ROW_LAND="| Kullanıcı giriş linkine tıklıyor ama abonelik sayfasına düşüyor (ana sayfa yerine) | Ücretsiz test dönemi bitti ve platformun ödeme duvarı geri geldi | SKILL.md'deki 7. adımdaki abonelik ödeme akışını izle; abone olduktan sonra `refresh-login` çalıştır, sonra ana sayfa linkini gönder |",
    RD_VER="""**v2.0.0'dan bu yana agent vekil modu, v2.2.0'dan bu yana ayrıca platformun ücretsiz test dönemine uyum sağlıyor**: çekirdek betik `scripts/powpow-register.mjs` bağımlılıksızdır
(Node ≥ 18); kullanıcı sohbetten yalnızca bir kez çıkar: gelen kutudaki doğrulama kodunu kontrol etmek için. Mevcut ücretsiz test döneminde kayıtlı hesap tüm özellikleri hemen kullanabilir — abonelik ödemesi isteğe bağlıdır; test dönemi bitip kullanıcı abonelik sayfasına düşerse akış kendiliğinden ödeme yoluna geçer. Node olmadan veya kullanıcı kendisi yapmayı tercih ettiğinde otomatik olarak saf rehberlik moduna düşer.""",
    RD_LINK="""3. **Tek tıkla giriş (çift link)**: kayıt başarılı olduktan hemen sonra giriş linki kullanıcıyı doğrudan ana sayfaya indirir (ücretsiz test döneminde tek tık ve kullanıma hazır);
   abonelik sayfasına düşerse (test dönemi bitti) veya kullanıcı yükseltmek isterse abonelik akışını izle — ödeme indikten sonra yeni giriş durumuna takas edilir ve tam üyelik linki ana sayfaya indirir
   (HttpOnly çerezi otomatik bırakan platformun resmi `me?token=` köprüsü üzerinden).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
VI = dict(
    DESC="description: Giúp người dùng hoàn tất đăng ký PowPow (Bubble) và đăng nhập một cú click ngay trong cuộc hội thoại. Agent điền form thay người dùng (kể cả tải ảnh đại diện) và gửi mã xác minh email; người dùng chỉ cần cung cấp thông tin cơ bản và kiểm tra mã xác minh một lần — không rời cuộc hội thoại. Nền tảng hiện đang trong giai đoạn dùng thử miễn phí: tài khoản đã đăng ký có thể dùng ngay mọi tính năng; thanh toán gói hội viên (Alipay/PayPal) là nâng cấp tùy chọn, khi cần agent cũng lo việc tạo đơn và theo dõi tiền về. Kích hoạt khi người dùng nói \"đăng ký Bubble\", \"tạo tài khoản powpow\", \"đăng ký Bubble thế nào\", \"giúp tôi tạo tài khoản powpow\", \"sign up powpow\"; cũng xử lý các vấn đề đăng ký (không nhận được mã xác minh, tên người dùng/email đã dùng) và kích hoạt (đăng nhập báo \"tài khoản chưa kích hoạt\" / pending_payment, làm sao đăng ký gói/thanh toán, Bubble miễn phí hay trả phí). Yêu cầu Node ≥ 18; nếu không có sẽ tự động chuyển sang chế độ hướng dẫn thuần túy. Không lo việc đăng bài/tạo nhân vật số (đó là nhiệm vụ của powpow-simple), cũng như phát triển mã.",
    INTRO="Dẫn dắt người dùng mới từ \"chưa biết Bubble là gì\" đến \"đăng nhập một cú click, chơi được ngay\" — toàn bộ trong cuộc hội thoại. Người dùng chỉ rời cuộc hội thoại đúng một lần: **để kiểm tra mã xác minh trong hộp thư**. Nền tảng hiện đang trong giai đoạn dùng thử miễn phí: sau khi đăng ký, mọi tính năng đều dùng được, không cần trả tiền; thanh toán gói hội viên là nâng cấp tùy chọn (agent cũng lo mở quầy thu ngân và theo dõi tiền về).",
    VLINE="**Phiên bản 2.2.0** · 2026-10-18 (từ v2 trở đi là chế độ agent đại diện: hợp đồng script và toàn bộ trình tự ở `references/agent-flow.md`; quy tắc trường, giới hạn tần suất và xử lý lỗi ở `references/registration-flow.md`; kênh thanh toán ở `references/payment-and-activation.md`; danh sách ảnh chụp sản phẩm ở `references/screenshots.md`. Từ v2.1.0 agent cũng lo được gói PayPal, song song với Alipay. Từ v2.2.0 nền tảng bước vào giai đoạn dùng thử miễn phí: đăng ký xong đăng nhập một cú click là dùng được ngay; thanh toán trở thành nâng cấp tùy chọn — nếu người dùng mở link lại rơi vào trang gói hội viên, nghĩa là giai đoạn dùng thử đã kết thúc, hãy theo luồng thanh toán ở bước 7; luồng tự thích ứng, không cần sửa script)",
    RT_ENV="- **Không có Node / script lỗi**: tự động chuyển sang chế độ hướng dẫn thuần túy — đưa cho người dùng trang đăng ký https://global.powpow.online/register và đồng hành hướng dẫn theo `references/registration-flow.md` (trong giai đoạn dùng thử miễn phí, đăng ký trên web cũng dùng được ngay như nhau). Đừng cố gắng chạy script mãi.",
    TRIGGER="- Vấn đề sau đăng ký: \"đăng nhập báo tài khoản chưa kích hoạt\", \"403 pending_payment\", \"trả tiền/đăng ký gói Bubble thế nào\", \"Bubble miễn phí hay trả phí\"",
    FLOW6="| 6 Đăng nhập một cú click | `login-link(home)` vào thẳng trang chủ; nếu rơi vào trang gói hội viên thì sang bước 7 | Bấm link và bắt đầu dùng |",
    FLOW7="| 7 Nâng cấp gói hội viên (tùy chọn) | Chỉ khi người dùng muốn làm hội viên / giai đoạn miễn phí đã kết thúc: lo trọn luồng thanh toán | Chọn phương thức, trả tiền |",
    STEP6="""## Bước 6: Đăng Nhập Một Cú Click (sau đăng ký vào thẳng trang chủ)

1. Ngay sau khi đăng ký thành công:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Gửi link cho người dùng: **bấm vào là vào thẳng trang chủ, đã đăng nhập sẵn**. Nền tảng hiện đang trong giai đoạn dùng thử miễn phí — sau khi đăng ký, mọi tính năng (bảng tin, bản đồ, nhân vật số, điểm danh, v.v.) đều dùng được, **không cần trả tiền**.
3. Nhờ người dùng xác nhận đã vào được; có hai trường hợp:
   - **Vào được trang chủ** → nhảy thẳng sang bước 8 để khép lại; quy trình đăng ký hoàn tất;
   - **Rơi vào trang gói hội viên** → giai đoạn dùng thử miễn phí của nền tảng đã kết thúc; nói với người dùng \"giai đoạn dùng thử miễn phí đã hết, giờ cần đăng ký gói hội viên\", sau đó theo bước 7 hoàn tất đăng ký gói, xong quay lại bước 8.
4. Nếu người dùng tự nguyện muốn nâng cấp hoặc ủng hộ nền tảng → cũng sang bước 7 (đăng ký gói là tự nguyện; đừng mời mọc).""",
    STEP7="""## Bước 7: Nâng Cấp Gói Hội Viên (tùy chọn — chỉ khi bước 6 yêu cầu)

1. Trước tiên gửi link đăng nhập nửa vời để trang trả về sau thanh toán hiển thị đúng \"Thanh toán thành công":
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Gửi link cho người dùng: bấm vào là trình duyệt mở thẳng trang gói hội viên, đã đăng nhập sẵn.
2. **Nhờ người dùng chọn phương thức thanh toán** — hiển thị cả hai kênh:
   - **Alipay (Trung Quốc đại lục / người dùng có Alipay)**: mua một lần theo thời hạn tương ứng, **không tự động gia hạn**
     - Tháng **¥6.99** (khuyên dùng để thử) / Quý **¥19.99** / Năm **¥69.99**
   - **PayPal (hải ngoại / người dùng không có Alipay)**: tự động gia hạn hàng tháng, hủy bất cứ lúc nào
     - Premium Monthly, khoảng **$1/tháng** (theo hiển thị trên trang gói hội viên; tự động gia hạn)
3. Khi người dùng đã chọn:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Script trả về đường dẫn file trang thanh toán; **mở trực tiếp bằng lệnh hệ thống** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Trình duyệt tự động nhảy sang quầy thu ngân chính thức Alipay/PayPal, nơi người dùng hoàn tất thanh toán hoặc uỷ quyền trừ tiền.
4. Chạy `query` mỗi 10–15 giây cho đến khi trả về `paid` hoặc `ACTIVE` (tiền về/uỷ quyền thường trong vài giây đến một phút). Nếu người dùng đóng trang thanh toán giữa chừng → chỉ cần `create-order` lại (đơn cũ / gói đang chờ tự đóng hoặc hết hạn sau 2 giờ; bỏ qua).
5. Kênh mã QR WeChat xác nhận thủ công, tiền về có thể chậm; Huawei IAP chỉ dùng được trong ứng dụng HarmonyOS. Skill không lo hai kênh này — sau khi trả tiền, người dùng quay lại báo agent, agent chạy `whoami` xác nhận tiền về trước, rồi gửi link trang chủ theo điểm 6 bên dưới.
6. Sau khi xác nhận tiền về, đổi lấy trạng thái đăng nhập mới nhất kèm quyền lợi gói hội viên, rồi gửi link vào thẳng trang chủ:
   ```
   POWPOW_REGISTER_PASSWORD=<mật khẩu> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Gửi link cho người dùng: **bấm vào là vào thẳng trang chủ với trạng thái hội viên đầy đủ**.""",
    STEP8="""## Bước 8: Khép Lại

1. `node scripts/powpow-register.mjs cleanup` để dọn các file trạng thái tạm trên máy (thông tin đăng nhập phiên).
2. Đưa cho người dùng một \"thẻ tài khoản\": tên người dùng, email (mật khẩu không hiển thị lại — ở chế độ sinh mật khẩu, người dùng đã được nhờ lưu lại lúc sinh; nếu người dùng tự đặt thì họ tự biết).
3. Nhắc nhở về hội viên (nói một lần, đừng mời mọc): hiện đang trong giai đoạn dùng thử miễn phí, dùng được ngay; khi giai đoạn dùng thử kết thúc, tài khoản chưa đăng ký gói khi vào các trang nội dung sẽ bị chuyển hướng về trang gói hội viên — để dùng lâu dài, quay lại tìm agent đăng ký bất cứ lúc nào.
4. Hướng dẫn bước đầu: xem bản đồ, đăng nhật ký du lịch đầu tiên (→ chuyển giao cho powpow-simple).
5. Giới thiệu tiện ích mở rộng: skill `@durenzidu/powpow-integration` và plugin `@durenzidu/openclaw-channel-powpow` — kết nối Bubble vào agent của chính người dùng; đưa lệnh cài nếu muốn.
6. Kết thúc bằng khối \"bước tiếp theo\".""",
    WALL="- **Tường phí không phải lỗi**: trong giai đoạn dùng thử miễn phí hiện tại, mọi trang nội dung đều mở; nếu người dùng bấm link trang chủ lại rơi vào trang gói hội viên, nghĩa là giai đoạn dùng thử đã kết thúc — hướng dẫn đăng ký gói qua bước 7. Đừng tìm cách vượt tường phí, và đừng giải thích cơ chế nội bộ cho người dùng.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` hoặc `--target home` | Tạo link đăng nhập một cú click (thiết kế hai link, xem bên dưới) |",
    AF_LINKSEQ="""## Cơ Chế Hai Link (thiết kế cốt lõi)

Trạng thái đăng nhập của nền tảng là cookie HttpOnly, agent không thể tự gắn vào trình duyệt; cầu nối là endpoint chính thức
`/api/auth/me?token=<JWT>&redirect=<đường dẫn trong site>`: xác minh chữ ký → tự động tạo
phiên → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 ngày) → kiểm tra
redirect (phải bắt đầu bằng dấu gạch chéo đơn, cấm `//` và dấu gạch chéo ngược, sau khi parse phải cùng origin) → 307 chuyển hướng tạm sang trang đích.

Có hai đích link, **ưu tiên sinh home trước, rồi quyết định có đi qua pending không dựa vào chỗ người dùng rơi vào**:

- **link home (mặc định, `--target home` → rơi vào `/`)**: sinh và gửi cho người dùng ngay sau khi đăng ký thành công.
  Trong giai đoạn dùng thử miễn phí, người dùng vào thẳng trang chủ, dùng được hết; **nếu bấm link lại rơi vào trang gói hội viên, nghĩa là giai đoạn dùng thử miễn phí đã kết thúc** — chuyển sang luồng thanh toán (xem bên dưới); không cần sửa script và không cần đăng ký lại.
- **link pending (dùng trong luồng thanh toán, `--target pending` → rơi vào `/subscription`)**:
  trình duyệt của người dùng vào trạng thái \"đăng nhập nửa vời\": trang gói hội viên và trang trả về sau thanh toán đều thấy và thao tác được. Sau khi tiền về,
  chạy `refresh-login` để đổi lấy JWT mới kèm quyền lợi ACTIVE, rồi gửi link home thêm lần nữa để có trạng thái hội viên đầy đủ.

## Trình Tự Đầy Đủ

### Luồng Nhanh (trong giai đoạn dùng thử miễn phí — đa số trường hợp)

```
1.  status                          # tự kiểm tra môi trường
2.  (bước 2: hội thoại xác nhận thông tin, mật khẩu tùy chọn; chế độ sinh: gen-password → nhờ người dùng lưu ngay)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → người dùng kiểm tra mã trong hộp thư (lần duy nhất rời hội thoại)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → gửi link cho người dùng; một cú click là vào trang chủ
7.  (người dùng xác nhận đã vào) → khép lại luôn: cleanup + thẻ tài khoản + hướng dẫn bước đầu
```

### Luồng Thanh Toán (khi người dùng muốn làm hội viên, hoặc giai đoạn miễn phí đã kết thúc)

```
1–5. Giống Luồng Nhanh (trạng thái đã có token sau khi register thành công)
6.  login-link --target pending     # → link đăng nhập nửa vời, trang trả về sau thanh toán vẫn hoạt động
7.  (người dùng chọn phương thức thanh toán)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <file trang thanh toán>   # Windows; macOS dùng open, Linux dùng xdg-open
    # → người dùng hoàn tất thanh toán/uỷ quyền tại quầy Alipay/PayPal (rời hội thoại)
9.  query (mỗi 10–15 giây) đến khi paid / ACTIVE
10. refresh-login                   # đổi lấy JWT mới kèm quyền lợi ACTIVE
11. login-link --target home        # → gửi link hội viên đầy đủ cho người dùng
12. whoami                          # xác nhận subscriptionStatus: ACTIVE (tùy chọn)
13. cleanup                         # dọn file trạng thái
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Giai đoạn dùng thử miễn phí đã kết thúc mà tiền chưa về; quay lại bước 9 tiếp tục poll, hoặc xác nhận người dùng đã hoàn tất thanh toán chưa |",
    AF_ERR_SUB="| Người dùng bấm link home nhưng rơi vào trang gói hội viên | Giai đoạn dùng thử miễn phí đã kết thúc → chuyển sang luồng thanh toán: `login-link --target pending` → chọn phương thức thanh toán → `create-order` |",
    AF_FALLBACK="Sau khi chuyển về: đưa trang đăng ký https://global.powpow.online/register (trong giai đoạn dùng thử miễn phí, đăng ký trên web cũng dùng được ngay như nhau; khi cần đăng ký gói, đưa thêm trang gói hội viên https://global.powpow.online/subscription ), xử lý sự cố song song theo quy tắc trong `registration-flow.md`, giữ cùng giọng điệu, và vẫn kết thúc mỗi lượt bằng khối \"bước tiếp theo\".",
    PA_NOTE="""> **Giai đoạn dùng thử miễn phí (bắt đầu từ 2026-10-18; hành vi thực tế của nền tảng là chuẩn)**: trong giai đoạn này tài khoản đã đăng ký dùng được mọi tính năng trực tiếp, và **đăng ký gói là nâng cấp tùy chọn chứ không phải yêu cầu** — chỉ theo luồng trong file này khi người dùng chủ động muốn làm hội viên. Khi giai đoạn dùng thử kết thúc, tài khoản chưa đăng ký gói khi vào các trang nội dung sẽ bị chuyển hướng về trang gói hội viên; chỉ cần hoàn tất đăng ký gói theo file này.""",
    RF_STATE="""## Luồng Trạng Thái Sau Khi Đăng Ký Thành Công

> **Giai đoạn dùng thử miễn phí (bắt đầu từ 2026-10-18; hành vi thực tế của nền tảng là chuẩn)**: tài khoản mới đăng ký có thể **dùng mọi tính năng trực tiếp**
> (bảng tin, bản đồ, nhân vật số, điểm danh, v.v.) không cần trả tiền; tài khoản chưa đăng ký gói không còn bị chặn khỏi các trang nội dung. Việc \"chặn pending\"
> mô tả trong mục này là trạng thái thông thường sau khi giai đoạn dùng thử kết thúc — khi đến lúc đó, hành vi thực tế trên mạng là chuẩn.

1. Người dùng được lưu với `accountStatus: 'pending'` và **3 huy hiệu khởi tạo** (route register).
2. Máy chủ cũng gắn hai cookie HttpOnly: JWT (vào trang trực tiếp được) và pendingUserToken (chứng thực danh tính cho luồng đăng ký gói).
3. Ở trạng thái thông thường (giai đoạn dùng thử kết thúc / không có giai đoạn miễn phí), trang đăng ký phát hiện `pending_payment` → chuyển hướng sang `/subscription`
   (giữ tham số trả về `next`); ở chế độ agent đại diện, `me?token=…&redirect=/subscription` cho hiệu ứng tương đương.
   **Trong giai đoạn dùng thử miễn phí, bước này không kích hoạt** — sau khi đăng ký, vào thẳng trang chủ và bắt đầu dùng.
4. Thanh toán xong → `accountStatus` thành `active` (**Alipay tự kích hoạt phía máy chủ qua notify**;
   PayPal kích hoạt qua Webhook; mã QR WeChat xác nhận thủ công; Huawei IAP đi qua `activate-huawei`).
   Chi tiết ở `payment-and-activation.md`.

Ở trạng thái thông thường, tài khoản chưa kích hoạt (pending) gọi các API lõi (bảng tin, bản đồ, chat nhân vật số, điểm danh, v.v.) sẽ bị 403;
link bài đăng chia sẻ là ngoại lệ (vẫn mở công khai). Trong giai đoạn dùng thử miễn phí, việc chặn này tạm ngưng và mọi thứ đều mở.""",
    RF_ROW_403="| Đăng ký thành công nhưng đăng nhập trả về 403 \"请完成订阅以激活账户\" | Tài khoản vẫn pending, và nền tảng không trong giai đoạn dùng thử miễn phí (trạng thái mong đợi trước khi trả tiền) | Trong giai đoạn dùng thử miễn phí sẽ không xảy ra; nếu xảy ra nghĩa là giai đoạn dùng thử đã kết thúc — hoàn tất đăng ký gói trước; nếu trả tiền rồi vẫn 403 thì đã dùng JWT cũ — ở chế độ script chạy `refresh-login` trước để đổi lấy trạng thái đăng nhập mới |",
    RF_ROW_LAND="| Người dùng bấm link đăng nhập nhưng rơi vào trang gói hội viên (thay vì trang chủ) | Giai đoạn dùng thử miễn phí đã kết thúc, tường phí của nền tảng đã trở lại | Theo luồng thanh toán đăng ký gói ở bước 7 trong SKILL.md; sau khi đăng ký gói, chạy `refresh-login` rồi gửi link trang chủ |",
    RD_VER="""**Từ v2.0.0 là chế độ agent đại diện, từ v2.2.0 còn thích ứng với giai đoạn dùng thử miễn phí của nền tảng**: script cốt lõi `scripts/powpow-register.mjs` không phụ thuộc thư viện
(Node ≥ 18); người dùng chỉ rời hội thoại đúng một lần: để kiểm tra mã xác minh trong hộp thư. Trong giai đoạn dùng thử miễn phí hiện tại, tài khoản đã đăng ký dùng được mọi tính năng ngay — thanh toán gói hội viên là tùy chọn; nếu giai đoạn dùng thử kết thúc và người dùng rơi vào trang gói hội viên, luồng tự chuyển sang đường thanh toán. Không có Node, hoặc khi người dùng muốn tự làm, tự động chuyển sang chế độ hướng dẫn thuần túy.""",
    RD_LINK="""3. **Đăng nhập một cú click (hai link)**: ngay sau khi đăng ký thành công, link đăng nhập đưa người dùng vào thẳng trang chủ (trong giai đoạn dùng thử miễn phí, một cú click là dùng được);
   nếu rơi vào trang gói hội viên (giai đoạn dùng thử kết thúc) hoặc người dùng muốn nâng cấp thì theo luồng đăng ký gói — sau khi tiền về, đổi lấy trạng thái đăng nhập mới và link hội viên đầy đủ đưa vào trang chủ
   (qua cầu nối chính thức `me?token=` của nền tảng, tự gắn cookie HttpOnly).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
