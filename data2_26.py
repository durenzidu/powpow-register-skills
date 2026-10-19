# -*- coding: utf-8 -*-
# v2.1.0 -> v2.2.0 delta translations: Yoruba (yo)

YO = dict(

DESC="description: Firanran awọn olumulo lati pari iforukọsilẹ PowPop (Bubble) ati iwọle ẹyọkan ni abala iwiregba gbogbo rẹ. Ajanṣan kun fọọmu fun wọn (pẹlu gbigbe aworan) o si fi koodu ifẹsẹmulẹ imeeli ranṣẹ; olumulo kan n pese alaye ipilẹ ati wo koodu ifẹsẹmulẹ lẹẹkan — ko jade kuro ninu iwiregba. Ni akoko idanwo ọfẹ lọwọlọwọ, akanti ti o forukọsilẹ le lo gbogbo ẹya lẹsẹkẹsẹ; owo sập (Alipay/PayPal) jẹ ilọsi ọmọ-ẹyọn aṣayan, ti ajanṣan le tọju pẹlu pipin iwe ati ibẹwo ọwọn pẹlu. O ṣiṣẹ nigbati olumulo ba sọ \"forukọsilẹ fun Bubble\", \"ṣẹda akanti powpow\", \"bawo ni mo ṣe le forukọsilẹ fun Bubble\", \"ran mi lọwọ lati ṣẹda akanti powpow\", \"forukọsilẹ powpow\"; o tun ṣe iṣẹ pẹlu awọn iṣoro iforukọsilẹ (koodu ifẹsẹmulẹ ko gba, orukọ/imeeli ti gba) ati awọn iṣoro imuṣiṣẹ (iwọle sọ \"akanti ko ṣiṣẹ\" / pending_payment, bawo ni o ṣe le sanwọ/sập, Bubble jẹ ọfẹ tabi owo). O nilo Node ≥ 18; pada si ipo itọsọna pipẹ laifọwọyi nigbati ko ba si. Ko ṣe iṣẹ pẹlu ifiweranṣẹ/ṣẹda ẹda oni-nọmba (iṣẹ powpow-simple ni iyẹn), tabi idagbasoke koodu.",

INTRO="O gbe olumulo tuntun lati \"emi ko mọ kini Bubble jẹ\" si \"ti wọle pẹlu ẹyọkan, ṣetan lati ṣere\" — gbogbo rẹ ni abala iwiregba. Olumulo jade kuro ninu iwiregba lẹẹkan kan: **lati wo koodu ifẹsẹmulẹ ninu apoti-ìwé rẹ**. Sajoo ni akoko idanwo ọfẹ: nigbati o forukọsilẹ, gbogbo ẹya wa, ko nilo owo; owo sập jẹ ilọsi ọmọ-ẹyọn aṣayan (ajanṣan tun ṣiṣi ati tọju ọwọn pẹlu).",

VLINE="**Ẹya 2.2.0** · 2026-10-18 (lati v2 eyi jẹ ipo iranlọwọ-ajanṣan: adehun iwe ati gbogbo ilana ni `references/agent-flow.md`; awọn ofin aaye, idinwo iṣẹ ati itọju aṣiṣe ni `references/registration-flow.md`; awọn ọna owo ni `references/payment-and-activation.md`; atokọ aworan ọja ni `references/screenshots.md`. Lati v2.1.0 ajanṣan le tọju sập PayPal pẹlu, gẹgẹbi aṣayan lẹgbẹẹ Alipay. Lati v2.2.0 sajoo wà ninu akoko idanwo ọfẹ: forukọsilẹ ki o wọle pẹlu ẹyọkan lati bẹrẹ lilo; owo di ilọsi aṣayan — ti olumulo ba tẹ ọna asopọ ki o si gbalẹ lori ojú-iwe sập, akoko idanwo ti pari, tẹle ilana owo igba 7; ilana ṣe atunṣa funrarẹ, ko nilo iyipada iwe)",

RT_ENV="- **Ko si Node / aṣiṣe iwe**: pada si ipo itọsọna pipẹ laifọwọyi — fun olumulo ni ojú-iwe iforukọsilẹ https://global.powpow.online/register ki o si ṣe itọsọna pẹlu gẹgẹbi `references/registration-flow.md` (ni akoko idanwo ọfẹ, iforukọsilẹ wẹẹbu jẹ iyara kan). Maṣe tubọ lu iwe.",

TRIGGER="- Awọn iṣoro lẹhin iforukọsilẹ: \"iwọle sọ akanti ko ṣiṣẹ\", \"403 pending_payment\", \"bawo ni mo ṣe sanwọ/sập fun Bubble\", \"Bubble jẹ ọfẹ tabi owo\"",

FLOW6="| 6 Iwọle ẹyọkan | `login-link(home)` taara si ojú-iwe ile; ti o ba gbalẹ lori ojú-iwe sập, lọ si Igba 7 | Tẹ ọna ki o bẹrẹ ṣere |",

FLOW7="| 7 Ilọsi ọmọ-ẹyọn (aṣayan) | Nigbati olumulo fẹ ọmọ-ẹyọn / akoko ọfẹ ti pari: gbogbo ilana owo ni a tọju | Yan ọna, san owo |",

STEP6="""## Igba 6: Iwọle Ẹyọkan (taara si ojú-iwe ile lẹhin iforukọsilẹ)

1. Lẹyin iforukọsilẹ to ṣaṣeyọri:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Fi ọna ranṣẹ si olumulo: **tẹ e ki o si gbalẹ taara lori ojú-iwe ile, ti wọle tẹlẹ**. Sajoo wà ninu akoko idanwo ọfẹ — lẹhin iforukọsilẹ, gbogbo ẹya wa (ifeede, maapu, ẹda oni-nọmba, awọn abẹwo, ati bẹbẹ), **ko nilo owo**.
3. Beere olumulo lati jẹrisi pe o wọle; ipo meji wa:
   - **Gbalẹ lori ojú-iwe ile** → fo taara si Igba 8 lati pari; iforukọsilẹ ti pari;
   - **Gbalẹ lori ojú-iwe sập** → akoko idanwo ọfẹ sajoo ti pari; sọ fun olumulo "akoko idanwo ọfẹ ti pari, sập ọmọ-ẹyọn nilo bayi", lẹhinna tẹle Igba 7 lati pari sập, ki o si pada si Igba 8 lẹhin sập.
4. Ti olumulo ba fẹ ilọsi tabi ṣe atilẹyin sajoo → lọ si Igba 8 pẹlu (sập jẹ ifẹ; maṣe fi ipá).""",

STEP7="""## Igba 7: Ilọsi Ọmọ-ẹyọn (aṣayan — nigbati Igba 6 n beere)

1. Kọọkan fi ọna idaji-iwọle ranṣẹ ki oju-iwe ipadabọ owo le ṣafihan "Owo ṣaṣeyọri" daradara:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Fi ọna ranṣẹ si olumulo: titẹ e jẹ ki aṣawakiri gbalẹ taara lori ojú-iwe sập, ti wọle tẹlẹ.
2. **Jẹ ki olumulo yan ọna owo** — ṣafihan mejeeji:
   - **Alipay (ilẹ China / awọn olumulo pẹlu Alipay)**: rira ẹyọkan ti akoko to baamu, **ko si imudasilẹ adaṣe**
     - Oṣù **¥6.99** (gba niyanju lati danwo) / Kọọkan **¥19.99** / Ọdún **¥69.99**
   - **PayPal (ode ọdún / awọn olumulo laisi Alipay)**: ṣe imudasilẹ adaṣe oṣù kọọkan, le fagilé nigbakigba
     - Alabọde Oṣù, nla **$1/oṣù** (gẹgẹbi a ṣe ṣafihan lori ojú-iwe sập; ṣe imudasilẹ adaṣe)
3. Nigbati olumulo ba yan ọkan:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Iwe na da ọna faili ojú-iwe owo pada; **ṹ ṣíi taara pẹlu aṣẹ eto** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Aṣawakiri fo laifọwọyi si ile-owo Alipay/PayPal ofeefee, nibiti olumulo pari owo tabi aṣẹ ìdíyelé.
4. Ṣiṣe `query` gbogbo iṣẹju 10–15 titi o padà `paid` tabi `ACTIVE` (owo/aṣẹ ni gbogbọn de laarin iṣẹju diẹ si iṣẹju kan). Ti olumulo ba ti ojú-iwe owo ni aarin → ṣẹda `create-order` lẹẹkansi (iwe atijọ / sập n reti ti ipade tabi pari laifọwọyi lẹhin wakati 2; foju wọn).
5. Ọna koodu WeChat QR jẹrisi ni ọwọ ati owo le de pẹlu; Huawei IAP wa ni inu App HarmonyOS nikan. Ìmọ-jáẹẹ yi ko tọju mejeji — lẹhin sanwo, olumulo pada sọ fun ajanṣan, ti n ṣiṣẹ `whoami` kọ lati jẹrisi ọwọn, lẹhinna fi ọna ojú-iwe ile ranṣẹ gẹgẹbi aami 6 ni isalẹ.
6. Lẹhin jẹrisi ọwọn, paṣiparọ fun ipo iwọle pẹlu asẹ sập tuntun, lẹhinna fi ọna ranṣẹ taara si ojú-iwe ile:
   ```
   POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Fi ọna ranṣẹ si olumulo: **tẹ e ki o si gbalẹ taara lori ojú-iwe ile pẹlu ipo ọmọ-ẹyọn kikun**.""",

STEP8="""## Igba 8: Ipari

1. `node scripts/powpow-register.mjs cleanup` lati nu awọn faili ipo akoko agbegbe (ẹri ajọ).
2. Fun olumulo ni "kaadi akanti": orukọ, imeeli (ọrọ igbaniwọle ko han mọ — ni ipo ipilẹṣẹ a beere olumulo lati fipamọ nigbati a ṣe; ti olumulo ba fi silẹ funrarẹ, wọn mọ ọ).
3. Iranti ọmọ-ẹyọn (sọ lẹẹkan, maṣe fi ipá): eleyi jẹ akoko idanwo ọfẹ ati akanti wa lẹsẹkẹsẹ; nigbati akoko idanwo pari, awọn akanti ti ko sập ti n bẹ ojú-iwe akoonu yoo pada si ojú-iwe sập — fun lilo pipẹ, pada wa ajanṣan lati sập nigbakigba.
4. Ṣe itọsọna awọn igba akọkọ: wo maapu, fi akọọlẹ irin-ajo akọkọ posti (→ fi fun powpow-simple).
5. Ṣe igbasilẹ awọn afikun: `@durenzidu/powpow-integration` ìmọ-jáẹẹ ati `@durenzidu/openclaw-channel-powpow` afikun — so Bubble pọ sinu ajanṣan olumulo; fi aṣẹ fi sori ẹrọ fun ti o ba fẹ.
6. Pari pẹlu bulọọki "igba ti o tẹle".""",

WALL="- **Odidi owo kii jẹ aṣiṣe**: ni akoko idanwo ọfẹ lọwọlọw� gbogbo ojú-iwe akoonu ṣi; ti olumulo ba tẹ ọna ojú-iwe ile ṣugbọn gbalẹ lori ojú-iwe sập, akoko idanwo ti pari — ṣe itọsọna wọn lati sập nipasẹ Igba 7. Maṣe gbiyanju lati koju odidi owo, ki o maṣe ṣalaye ilana inu fun olumulo.",

AF_ROW_LOGIN="| `login-link` | `--target pending` tabi `--target home` | Ṣe ẹda ọna iwọle ẹyọkan (apẹẹrẹ ọna meji, wo ni isalẹ) |",

AF_LINKSEQ="""## Ilana Ọna Meji (apẹẹrẹ ipilẹ)

Ipo iwọle sajoo jẹ kuki HttpOnly, ti ajanṣan ko le gbin fun aṣawakiri taara; ọfa ni ofeefee
`/api/auth/me?token=<JWT>&redirect=<ọna inu sajtii>`: jẹrisi ibuwọlu → ṣẹda ajo
adaṣe → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / ọjọ 7) → jẹrisi
itọkasi (gbọdọ bẹrẹ pẹlu kiakia kan, `//` ati kiakia ẹhin ko gba, gbọdọ jẹ orisun kan lẹhin atupale) → 307 itọkasi akoko si ojú-iwe ti a fẹ.

Awọn ọna meji wa, **ṣẹda ile kọọkan, lẹhinna pinnu boya yoo fa nipasẹ pending gẹgẹbi ibiti olumulo gbalẹ**:

- **ọna ile (fi ranṣẹ gẹgẹbi aiyipada, `--target home` → gbalẹ lori `/`)**: ṣẹda ki o fi ranṣẹ si olumulo lẹyin iforukọsilẹ to ṣaṣeyọri.
  Ni akoko idanwo ọfẹ olumulo lọ taara si ojú-iwe ile, gbogbo rẹ wa; **ti olumulo ba tẹ ṣugbọn gbalẹ lori ojú-iwe sập, akoko idanwo ọfẹ ti pari** — pada si ọna owo (wo ni isalẹ); ko nilo iyipada iwe ko si iforukọsilẹ titun.
- **ọna pending (lo ni ọna owo, `--target pending` → gbalẹ lori `/subscription`)**:
  aṣawakiri olumulo wọle ipo "idaji-iwọle": ojú-iwe sập ati ojú-iwe ipadabọ owo han ati ṣiṣẹ. Lẹhin owo de,
  ṣiṣẹ `refresh-login` lati paṣiparọ fun JWT titun pẹlu asẹ ACTIVE, lẹhinna fi ọna ile ranṣẹ lẹẹkansi fun ipo ọmọ-ẹyọn kikun.

## Gbogbo Ilana

### Ọna Kia (ni akoko idanwo ọfẹ — ọpọlọpọ awọn ipo)

```
1.  status                          # ayẹwo ara ẹrọ
2.  (iwiregba Igba 2 lati jẹrisi alaye, ọrọ igbaniwọle eyikeyi; ipo ipilẹṣẹ: gen-password → jẹ ki olumulo fipamọ lẹsẹkẹsẹ)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → olumulo wo koodu ni apoti-ìwé rẹ (igba kan ṣoṣo ti o jade kuro ninu iwiregba)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → fi ọna ranṣẹ si olumulo; ẹyọkan ki o wà lori ojú-iwe ile
7.  (olumulo jẹrisi pe o wọle) → pari taara: cleanup + kaadi akanti + ṣe itọsọna igba akọkọ
```

### Ọna Owo (nigbati olumulo fẹ ọmọ-ẹyọn, tabi akoko idanwo ọfẹ ti pari)

```
1–5. Gẹgẹbi ọna kia (ipo ni tokeni tẹlẹ lẹhin register ṣaṣeyọri)
6.  login-link --target pending     # → ọna idaji-iwọle, jẹ ki ojú-iwe ipadabọ owo ṣiṣẹ
7.  (olumulo yan ọna owo)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <faili ojú-iwe owo>       # Windows; macOS lo open, Linux lo xdg-open
    # → olumulo pari owo/aṣẹ ni ile-owo Alipay/PayPal (o jade kuro ninu iwiregba)
9.  query (gbogbọn 10–15s) titi paid / ACTIVE
10. refresh-login                   # paṣiparọ fun JWT titun pẹlu asẹ ACTIVE
11. login-link --target home        # → fi ọna ọmọ-ẹyọn kikun ranṣẹ si olumulo
12. whoami                          # jẹrisi subscriptionStatus: ACTIVE (aṣayan)
13. cleanup                         # nu faili ipo
```""",

AF_ERR_403="| `refresh-login` 403 `pending_payment` | Akoko idanwo ọfẹ ti pari ati owo ko de; pada si igba 9 lati tẹsiwaju ibi-iṣẹ, tabi jẹrisi boya olumulo pari owo |",

AF_ERR_SUB="| Olumulo tẹ ọna ile ṣugbọn gbalẹ lori ojú-iwe sập | Akoko idanwo ọfẹ ti pari → pada si ọna owo: `login-link --target pending` → yan ọna owo → `create-order` |",

AF_FALLBACK="Lẹhin pada: fi ojú-iwe iforukọsilẹ https://global.powpow.online/register (ni akoko idanwo ọfẹ, iforukọsilẹ wẹẹbu jẹ iyara kan; nigbati sập nilo, fi ojú-iwe sập ranṣẹ pẹlu https://global.powpow.online/subscription ), ṣe itọju pẹlu gẹgẹbi awọn ofin ni `registration-flow.md`, tọju iro kan, ati pari gbogbo iyi pẹlu bulọọki \"igba ti o tẹle\".",

PA_NOTE="""> **Akoko idanwo ọfẹ (bẹrẹ 2026-10-18; ihuwasi sajoo gidi ni o ṣe): ni akoko yii akanti ti o forukọsilẹ le lo gbogbo ẹya taara, ati **sập jẹ ilọsi aṣayan kii jẹ ibeere** — tẹle ilana faili yii nigbati olumulo fẹ ọmọ-ẹyọn nikan. Nigbati akoko idanwo pari, awọn akanti ti ko sập ti n bẹ ojú-iwe akoonu yoo pada si ojú-iwe sập; pari nikan sập gẹgẹbi faili yii.""",

RF_STATE="""## Ilana Ipo Lẹhin Iforukọsilẹ Ṣaṣeyọri

> **Akoko idanwo ọfẹ (bẹrẹ 2026-10-18; ihuwasi sajoo gidi ni o ṣe): akanti tuntun ti o forukọsilẹ le **lo gbogbo ẹya taara**
> (ifeede, maapu, ẹda oni-nọmba, awọn abẹwo, ati bẹbẹ) laisi owo; awọn akanti ti ko sập ko ni idi mọ lori ojú-iwe akoonu. "Idinamọ pending"
> ti a ṣalaye ni abala yii jẹ ipo deede lẹhin akoko idanwo pari — nigbati akoko na de, ihuwasi ori-ayelujara gidi ni o ṣe.

1. Olumulo fi pamọ pẹlu `accountStatus: 'pending'` ati **aami ipilẹ 3** (ọna forukọsilẹ).
2. Olupin gbin kuki HttpOnly meji pẹlu: JWT (le wọle ojú-iwe taara) ati pendingUserToken (ẹri idanimọ fun ilana sập).
3. Ni ipo deede (akoko idanwo pari / ko si akoko ọfẹ), ojú-iwe iforukọsilẹ ri `pending_payment` → pada si `/subscription`
   (ti ipadabọ `next`); ni ipo iranlọwọ-ajanṣan, `me?token=…&redirect=/subscription` gba ipa kan.
   **Ni akoko idanwo ọfẹ igba yii ko ṣiṣẹ** — lẹhin forukọsilẹ, lọ taara si ojú-iwe ile ki o bẹrẹ lilo.
4. Owo pari → `accountStatus` di `active` (**Alipay ṣiṣẹ laifọwọyi ẹgbẹ olupin nipasẹ notify**;
   PayPal ṣiṣẹ nipasẹ Webhook; koodu WeChat QR jẹrisi ni ọwọ; Huawei IAP kọja nipasẹ `activate-huawei`).
   Wo `payment-and-activation.md` fun alaye.

Ni ipo deede, awọn olumulo ti ko ṣiṣẹ (pending) ti n pe API ipilẹ (ifeede, maapu, iwiregba ẹda oni-nọmba, awọn abẹwo, ati bẹbẹ) gba 403;
awọn ọna ifiweranṣẹ pinyẹẹ jẹ aṣẹ (jẹ gbangba). Ni akoko idanwo ọfẹ idinamọ yii duro ati gbogbo rẹ ṣi.""",

RF_ROW_403="| Forukọsilẹ ṣaṣeyọri ṣugbọn iwọle pada 403 \"请完成订阅以激活账户\" | Akanti wa ni pending, ati sajoo ko si ni akoko idanwo ọfẹ (ipo ti a reti ṣaaju owo) | Ko ṣẹlẹ ni akoko idanwo ọfẹ; ti o ba ṣẹlẹ, akoko idanwo ti pari — pari sập kọọkan; ti 504 ba wa lẹhin owo, JWT atijọ lo — ni ipo iwe ṣiṣẹ `refresh-login` kọọkan lati paṣiparọ fun ipo iwọle titun |",

RF_ROW_LAND="| Olumulo tẹ ọna iwọle ṣugbọn gbalẹ lori ojú-iwe sập (dipo ojú-iwe ile) | Akoko idanwo ọfẹ ti pari ati odidi owo sajoo pada | Tẹle Igba 7 ninu SKILL.md fun ilana owo sập; lẹhin sập, ṣiṣẹ `refresh-login` lẹhinna fi ọna ojú-iwe ile ranṣẹ |",

RD_VER="""**Lati v2.0.0 eyi jẹ ipo iranlọwọ-ajanṣan, ati lati v2.2.0 o baamu akoko idanwo ọfẹ sajoo**: iwe ipilẹ `scripts/powpow-register.mjs` jẹ kini-ṣi-ẹrọ-orisun
(Node ≥ 18); olumulo jade kuro ninu iwiregba lẹẹkan kan: lati wo koodu ifẹsẹmulẹ ni apoti-ìwé rẹ. Ni akoko idanwo ọfẹ lọwọlọwọ, akanti ti o forukọsilẹ le lo gbogbo ẹya lẹsẹkẹsẹ — owo sập jẹ ilọsi aṣayan; ti akoko idanwo pari ati olumulo gbalẹ lori ojú-iwe sập, ilana pada si ọna owo laifọwọyi. Laisi Node, tabi nigbati olumulo fẹ ṣe funrarẹ, o pada si ipo itọsọna pipẹ laifọwọyi.""",

RD_LINK="""3. **Iwọle ẹyọkan (awọn ọna meji)**: lẹyin iforukọsilẹ to ṣaṣeyọri, ọna iwọle gbe olumulo taara si ojú-iwe ile (ni akoko idanwo ọfẹ, ẹyọkan ki o wa);
   ti o gbalẹ lori ojú-iwe sập (akoko idanwo pari) tabi olumulo fẹ ilọsi, tẹle ilana sập — lẹhin owo de, ipo iwọle tuntun paṣiparọ ati ọna ọmọ-ẹyọn kikun gbe wọn si ojú-iwe ile
   (nipasẹ ọfa `me?token=` ofeefee sajoo, ti o gbin kuki HttpOnly laifọwọyi).""",

LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
