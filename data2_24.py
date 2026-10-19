# -*- coding: utf-8 -*-
# v2.1.0 -> v2.2.0 delta translations: Swahili (sw)

SW = dict(

DESC="description: Husaidia watumiaji kukamilisha usajili wa PowPow (Bubble) na kuingia kwa bonyezo moja ndani ya mazungumzo yote. Wakala hujaza fomu kwa niaba yao (ikiwa ni pamoja na kupakia picha ya wasifu) na hutuma msimbo wa uthibitishaji wa barua pepe; mtumiaji hutoa tu taarifa za msingi na kukagua msimbo wa uthibitishaji mara moja — haachi mazungumzo kabisa. Katika kipindi cha sasa cha majaribio bila malipo cha jukwaa, akaunti iliyosajiliwa inaweza kutumia kila kipengele mara moja; malipo ya sasiri (Alipay/PayPal) ni uboreshaji wa hiari wa uanachama, ambao wakala anaweza pia kuyashughulikia kwa kuunda oda na kufuatilia mapato inapohitajika. Huchochea wakati mtumiaji anasema \"jiandikishe kwa Bubble\", \"fungua akaunti ya powpow\", \"nawezaje kujiandikisha kwa Bubble\", \"nisaidie kufungua akaunti ya powpow\", \"jiandikishe powpow\"; pia hushughulikia matatizo ya usajili (msimbo wa uthibitishaji haujapokelewa, jina la mtumiaji/barua pepe tayari yamechukuliwa) na matatizo ya uamshaji (kuingia kunasema \"akaunti haijawashwa\" / pending_payment, nawezaje kusajili/kulipa, Bubble ni bila malipo au inagharimu). Inahitaji Node ≥ 18; hurejea kiotomatiki kwenye hali ya mwongozo safi inapopatikana. Haifanyi kazi za kuchapisha/kuunda binadamu wa digitali (ni kazi ya powpow-simple), wala maendeleo ya msimbo.",

INTRO="Inachukua mtumiaji mpya kutoka \"sijui Bubble ni nini\" hadi \"nimeingia kwa bonyezo moja, niko tayari kucheza\" — yote ndani ya mazungumzo. Mtumiaji anaacha mazungumzo mara moja tu: **kukagua msimbo wa uthibitishaji kwenye kikasha chake**. Jukwaa kwa sasa liko katika kipindi cha majaribio bila malipo: mara baada ya kujiandikisha, kila kipengele kinapatikana, hakuna malipo yanayohitajika; malipo ya sasiri ni uboreshaji wa hiari wa uanachama (wakala pia hushughulikia kufungua kasha na kufuatilia mapato).",

VLINE="**Toleo 2.2.0** · 2026-10-18 (tangu v2 hii ni hali ya wakala-msaidizi: mkataba wa hati na mpangilio kamili kwenye `references/agent-flow.md`; kanuni za uwanja, vikomo za kiwango na utatuzi wa makosa kwenye `references/registration-flow.md`; njia za malipo kwenye `references/payment-and-activation.md`; orodha ya picha za bidhaa kwenye `references/screenshots.md`. Tangu v2.1.0 sasiri za PayPal pia zinaweza kushughulikiwa na wakala, kama chaguo pamoja na Alipay. Tangu v2.2.0 jukwaa limeingia katika kipindi cha majaribio bila malipo: jiandikishe na kuingia kwa bonyezo moja ili kuanza kutumia; malipo yamekuwa uboreshaji wa hiari — ikiwa mtumiaji anabonyeza kiungo na kutua kwenye ukurasa wa sasiri, kipindi cha majaribio kimekamilika, fuata mtiririko wa malipo wa Hatua 7; mtiririko unajirekebisha yenyewe, hakuna mabadiliko ya hati yanayohitajika)",

RT_ENV="- **Hakuna Node / makosa ya hati**: hurejea kiotomatiki kwenye hali ya mwongozo safi — mpe mtumiaji ukurasa wa usajili https://global.powpow.online/register na umwongoze kando kulingana na `references/registration-flow.md` (katika kipindi cha majaribio bila malipo, usajili wa wavuti ni wa haraka sawa). Usizidi kubisha hati.",

TRIGGER="- Matatizo baada ya usajili: \"kuingia kunasema akaunti haijawashwa\", \"403 pending_payment\", \"nawezaje kulipa/kusajili kwa Bubble\", \"Bubble ni bila malipo au inagharimu\"",

FLOW6="| 6 Kuingia kwa bonyezo moja | `login-link(home)` moja kwa moja kwenye ukurasa wa nyumbani; ikiwa kinatua kwenye ukurasa wa sasiri, nenda Hatua 7 | Bonyeza kiungo na uanze kucheza |",

FLOW7="| 7 Uboreshaji wa sasiri (wa hiari) | Tu wakati mtumiaji anataka uanachama / kipindi cha bila malipo kimekamilika: mtiririko kamili wa malipo unashughulikiwa | Chagua njia, lipa |",

STEP6="""## Hatua 6: Kuingia kwa Bonyezo Moja (moja kwa moja kwenye ukurasa wa nyumbani baada ya usajili)

1. Mara baada ya usajili kufanikiwa:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Tuma kiungo kwa mtumiaji: **bonyeza na wewe unatua moja kwa moja kwenye ukurasa wa nyumbani, tayari umeingia**. Jukwaa kwa sasa liko katika kipindi cha majaribio bila malipo — baada ya kujiandikisha, kila kipengele kinapatikana (mlipuko, ramani, binadamu wa digitali, viingilio, n.k.), **hakuna malipo yanayohitajika**.
3. Mwombe mtumiaji athibitishe kuwa ameingia; kuna hali mbili:
   - **Ametua kwenye ukurasa wa nyumbani** → rukia moja kwa moja Hatua 8 kufunga kazi; usajili umekamilika;
   - **Ametua kwenye ukurasa wa sasiri** → kipindi cha majaribio bila malipo cha jukwaa kimekamilika; mwambie mtumiaji "kipindi cha majaribio bila malipo kimeisha, sasiri ya uanachama inahitajika sasa", kisha fuata Hatua 7 kukamilisha sasiri, na urudi Hatua 8 baada ya kusajili.
4. Kama mtumiaji mwenyewe anataka kuboresha au kusaidia jukwaa → pia nenda Hatua 7 (kusajiri ni kwa hiari; usisukume).""",

STEP7="""## Hatua 7: Uboreshaji wa Sasiri (wa hiari — tu wakati Hatua 6 inaita)

1. Kwanza tuma kiungo cha nusu-kuingia ili ukurasa wa kurudi kwa malipo uweze kuonyesha "Malipo yamefanikiwa" kwa usahihi:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Tuma kiungo kwa mtumiaji: kubonyeza kunamwacha kivinjari moja kwa moja kwenye ukurasa wa sasiri, tayari ameingia.
2. **Mwombe mtumiaji achague njia ya malipo** — onyesha njia zote mbili:
   - **Alipay (China bara / watumiaji wenye Alipay)**: ununuzi wa mara moja wa muda unaolingana, **hakuna kujirudia kiotomatiki**
     - Kila mwezi **¥6.99** (inapendekezwa kwa majaribio) / Kila robo **¥19.99** / Kila mwaka **¥69.99**
   - **PayPal (nje ya nchi / watumiaji wasio na Alipay)**: hujirudia kiotomatiki kila mwezi, ghairi wakati wowote
     - Premium Kila mwezi, karibu **$1/mwezi** (kama inavyoonyeshwa kwenye ukurasa wa sasiri; hujirudia kiotomatiki)
3. Mara mtumiaji anapochagua moja:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Hiti inarudisha njia ya faili ya ukurasa wa malipo; **ifungue moja kwa moja kwa amri ya mfumo** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Kivinjari hurukia kiotomatiki kwenye kasha rasmi ya Alipay/PayPal, ambapo mtumiaji hukamilisha malipo au idhini ya bili.
4. Endesha `query` kila sekunde 10–15 hadi irudishe `paid` au `ACTIVE` (malipo/idhini kwa kawaida hufika ndani ya sekunde chache hadi dakika moja). Kama mtumiaji anafunga ukurasa wa malipo katikati → fanya `create-order` tena (oda za zamani / sasiri zinazosubiri hufungwa au kwisha kiotomatiki baada ya masaa 2; ziondoe).
5. Njia ya msimbo wa QR ya WeChat huthibitishwa kwa mikono na fedha zinaweza kufika marehemu; Huawei IAP inapatikana tu ndani ya Programu ya HarmonyOS. Hiti hii haiwezi kushughulikia hizi mbili — baada ya kulipa, mtumiaji anarudi na kumwambia wakala, ambaye kwanza anaendesha `whoami` kuthibitisha mapato, kisha anatuma kiungo cha ukurasa wa nyumbani kwa punto 6 hapa chini.
6. Baada ya mapato kuthibitishwa, badilishana hali ya kuingia yenye dai la sasa la sasiri, kisha tuma kiungo moja kwa moja kwenye ukurasa wa nyumbani:
   ```
   POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Tuma kiungo kwa mtumiaji: **bonyeza na wewe unatua moja kwa moja kwenye ukurasa wa nyumbani wenye hali kamili ya uanachama**.""",

STEP8="""## Hatua 8: Kufunga Kazi

1. `node scripts/powpow-register.mjs cleanup` kusafisha faili za hali za muda za ndani (vitambulisho vya kipindi).
2. Mpe mtumiaji "kadi ya akaunti": jina la mtumiaji, barua pepe (nywila haionyeshwi tena — katika hali ya kuzalisha mtumiaji aliombwa kuhifadhi wakati ilizalishwa; kama mtumiaji aliweka mwenyewe, anaijua).
3. Ukumbusho wa uanachama (sema mara moja, usisukume): hii kwa sasa ni kipindi cha majaribio bila malipo na akaunti inapatikana mara moja; kipindi cha majaribio kinapokamilika, akaunti zisizo na sasiri zinazotembelea kurasa za maudhui zitaelekezwa kwenye ukurasa wa sasiri — kwa matumizi ya muda mrefu, rudi na umtafute wakala kusajiri wakati wowote.
4. Ongoza hatua za kwanza: vinjari ramani, chapisha jarida la kwanza la safari (→ peleka kwa powpow-simple).
5. Pendekeza viendelezi: hati ya `@durenzidu/powpow-integration` na programu-jalizi ya `@durenzidu/openclaw-channel-powpow` — unganisha Bubble kwenye wakala mwenyewe wa mtumiaji; mpe amri ya usakinishaji akitaka.
6. Maliza na bloku ya "hatua inayofuata".""",

WALL="- **Ukuta wa malipo si hitilafu**: katika kipindi cha sasa cha majaribio bila malipo kurasa zote za maudhui zimefunguliwa; kama mtumiaji anabonyeza kiungo cha ukurasa wa nyumbani lakini anatua kwenye ukurasa wa sasiri, kipindi cha majaribio kimekamilika — mwongoze kusajili kupitia Hatua 7. Usijaribu kupita ukuta wa malipo, na usieleze mifumo ya ndani kwa mtumiaji.",

AF_ROW_LOGIN="| `login-link` | `--target pending` au `--target home` | Huzalisha kiungo cha kuingia kwa bonyezo moja (muundo wa viungo viwili, ona hapa chini) |",

AF_LINKSEQ="""## Mfumo wa Viungo Viwili (muundo wa msingi)

Hali ya kuingia ya jukwaa ni kuki ya HttpOnly, ambayo wakala hawezi kuzalisha kwa kivinjari moja kwa moja; daraja ni rasmi
`/api/auth/me?token=<JWT>&redirect=<njia ya ndani ya tovuti>`: thibitisha saini → unda kipindi
kiotomatiki → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / siku 7) → thibitisha
kuelekeza (lazima ianze na mkwaju mmoja, `//` na mikwaju ya nyuma imekatazwa, lazima iwe chanzo sawa baada ya kuchanganua) → 307 kuelekeza kwa muda hadi ukurasa lengwa.

Kuna malengo mawili ya viungo, **zalisha nyumbani kwanza, kisha amua kama utapitia pending kulingana na mahali mtumiaji anapotua**:

- **kiungo cha nyumbani (kinatumwa kwa chaguo-msingi, `--target home` → kinatua kwenye `/`)**: kinazalishwa na kutumwa kwa mtumiaji mara baada ya usajili kufanikiwa.
  Katika kipindi cha majaribio bila malipo mtumiaji huenda moja kwa moja kwenye ukurasa wa nyumbani, kinapatikana kikamilifu; **kama mtumiaji anabonyeza lakini anatua kwenye ukurasa wa sasiri, kipindi cha majaribio bila malipo kimekamilika** — badilisha kwenye njia ya malipo (ona hapa chini); hakuna mabadiliko ya hati na hakuna usajili upya unaohitajika.
- **kiungo cha pending (kinatumika katika njia ya malipo, `--target pending` → kinatua kwenye `/subscription`)**:
  kivinjari cha mtumiaji huingia katika hali ya "nusu-kuingia": ukurasa wa sasiri na ukurasa wa kurudi kwa malipo ni vinara na vinafanya kazi. Baada ya malipo kufika,
  endesha `refresh-login` kubadilishana JWT mpya yenye dai la ACTIVE, kisha tuma kiungo cha nyumbani tena kwa hali kamili ya uanachama.

## Mpangilio Kamili

### Njia ya Haraka (katika kipindi cha majaribio bila malipo — wingi mkubwa wa matukio)

```
1.  status                          # ukaguzi wa mazingira
2.  (mazungumzo ya Hatua 2 kuthibitisha taarifa, nywila mojawapo; hali ya kuzalisha: gen-password → mwombe mtumiaji ahifadhi mara moja)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → mtumiaji hukagua msimbo kwenye kikasha chake (wakati pekee wa kuacha mazungumzo)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → tuma kiungo kwa mtumiaji; bonyezo moja na yuko kwenye ukurasa wa nyumbani
7.  (mtumiaji athibitishe ameingia) → funga moja kwa moja: cleanup + kadi ya akaunti + ongoza hatua za kwanza
```

### Njia ya Malipo (wakati mtumiaji anataka uanachama, au kipindi cha majaribio bila malipo kimekamilika)

```
1–5. Sawa na njia ya haraka (hali tayari ina tokeni baada ya register kufanikiwa)
6.  login-link --target pending     # → kiungo cha nusu-kuingia, huweka ukurasa wa kurudi kwa malipo ukifanya kazi
7.  (mtumiaji achague njia ya malipo)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <faili ya ukurasa wa malipo>       # Windows; macOS hutumia open, Linux hutumia xdg-open
    # → mtumiaji hukamilisha malipo/idhini kwenye kasha cha Alipay/PayPal (anaacha mazungumzo)
9.  query (kila 10–15s) hadi paid / ACTIVE
10. refresh-login                   # badilishana JWT mpya yenye dai la ACTIVE
11. login-link --target home        # → tuma kiungo cha uanachama kamili kwa mtumiaji
12. whoami                          # thibitisha subscriptionStatus: ACTIVE (hiari)
13. cleanup                         # safisha faili ya hali
```""",

AF_ERR_403="| `refresh-login` 403 `pending_payment` | Kipindi cha majaribio bila malipo kimekamilika na malipo hayajafika; rudi hatua 9 kuendelea kuchunguza, au thibitisha kama mtumiaji alikamilisha malipo |",

AF_ERR_SUB="| Mtumiaji anabonyeza kiungo cha nyumbani lakini anatua kwenye ukurasa wa sasiri | Kipindi cha majaribio bila malipo kimekamilika → badilisha kwenye njia ya malipo: `login-link --target pending` → chagua njia ya malipo → `create-order` |",

AF_FALLBACK="Baada ya kurejea: mpe ukurasa wa usajili https://global.powpow.online/register (katika kipindi cha majaribio bila malipo, usajili wa wavuti ni wa haraka sawa; wakati sasiri inahitajika, pia mpe ukurasa wa sasiri https://global.powpow.online/subscription ), tatua kando kulingana na kanuni za `registration-flow.md`, weka sauti sawa, na bado maliza kila zamu na bloku ya \"hatua inayofuata\".",

PA_NOTE="""> **Kipindi cha majaribio bila malipo (kuanzia 2026-10-18; tabia halisi ya jukwaa ndiyo inayotawala)**: katika kipindi hiki akaunti iliyosajiliwa inaweza kutumia kila kipengele moja kwa moja, na **kusajiri ni uboreshaji wa hiari sio sharti** — fuata mtiririko wa faili hili tu wakati mtumiaji mwenyewe anataka uanachama. Kipindi cha majaribio kinapokamilika, akaunti zisizo na sasiri zinazotembelea kurasa za maudhui zitaelekezwa kwenye ukurasa wa sasiri; kamilisha tu sasiri kulingana na faili hili.""",

RF_STATE="""## Mtiririko wa Hali Baada ya Usajili Kufanikiwa

> **Kipindi cha majaribio bila malipo (kuanzia 2026-10-18; tabia halisi ya jukwaa ndiyo inayotawala)**: akaunti mpya iliyosajiliwa inaweza **kutumia kila kipengele moja kwa moja**
> (mlipuko, ramani, binadamu wa digitali, viingilio, n.k.) bila malipo yanayohitajika; akaunti zisizo na sasiri hazifungwi tena kwenye kurasa za maudhui. "Kuzuia kwa pending"
> kunaelezewa katika sehemu hii ni hali ya kawaida baada ya kipindi cha majaribio kukamilika — wakati huo unapofika, tabia halisi ya mtandaoni ndiyo inayotawala.

1. Mtumiaji huhifadhiwa na `accountStatus: 'pending'` na **beji 3 za mwanzo** (njia ya register).
2. Seva pia huzalisha vuki viwili vya HttpOnly: JWT (inaweza kufikia kurasa moja kwa moja) na pendingUserToken (cheti cha utambulisho cha mtiririko wa sasiri).
3. Katika hali ya kawaida (kipindi cha majaribio kimeisha / hakuna kipindi cha bila malipo), ukurasa wa usajili hugundua `pending_payment` → inaelekeza kwenye `/subscription`
   (ikihifadhi kigezo cha kurudi `next`); katika hali ya wakala-msaidizi, `me?token=…&redirect=/subscription` hupata athari sawa.
   **Katika kipindi cha majaribio bila malipo hatua hii haichochei** — baada ya kujiandikisha, nenda moja kwa moja kwenye ukurasa wa nyumbani na uanze kutumia.
4. Malipo yamekamilika → `accountStatus` inakuwa `active` (**Alipay huwasha kiotomatiki upande wa seva kupitia notify**;
   PayPal huwasha kupitia Webhook; msimbo wa QR ya WeChat huthibitishwa kwa mikono; Huawei IAP hupitia `activate-huawei`).
   Ona `payment-and-activation.md` kwa maelezo.

Katika hali ya kawaida, watumiaji wasio na shughuli (pending) wanaoitia API za msingi (mlipuko, ramani, mazungumzo ya binadamu wa digitali, viingilio, n.k.) hupata 403;
viungo vya machapisho yaliyogawanywa ni ubaguzi (vinahifadhiwa kupatikana hadharani). Katika kipindi cha majaribio bila malipo kuzuia hii kunasimamishwa na kila kitu kimefunguliwa.""",

RF_ROW_403="| Usajili umefanikiwa lakini kuingia inarudisha 403 \"请完成订阅以激活账户\" | Akaunti bado iko pending, na jukwaa haliko katika kipindi cha majaribio bila malipo (hali inayotarajiwa kabla ya malipo) | Haitatokea katika kipindi cha majaribio bila malipo; ikitokea, kipindi cha majaribio kimekamilika — kamilisha sasiri kwanza; kama bado 403 baada ya malipo, JWT ya zamani ilitumika — katika hali ya hati endesha `refresh-login` kwanza kubadilishana hali mpya ya kuingia |",

RF_ROW_LAND="| Mtumiaji anabonyeza kiungo cha kuingia lakini anatua kwenye ukurasa wa sasiri (badala ya ukurasa wa nyumbani) | Kipindi cha majaribio bila malipo kimekamilika na ukuta wa malipo wa jukwaa umerudi | Fuata Hatua 7 ndani ya SKILL.md kwa mtiririko wa malipo ya sasiri; baada ya kusajiri, endesha `refresh-login` kisha tuma kiungo cha ukurasa wa nyumbani |",

RD_VER="""**Tangu v2.0.0 hii ni hali ya wakala-msaidizi, na tangu v2.2.0 inajirekebisha kwa kipindi cha majaribio bila malipo cha jukwaa**: hati kuu `scripts/powpow-register.mjs` ni zero-dependency
(Node ≥ 18); mtumiaji anaacha mazungumzo mara moja tu: kukagua msimbo wa uthibitishaji kwenye kikasha chake. Katika kipindi cha sasa cha majaribio bila malipo, akaunti iliyosajiliwa inaweza kutumia kila kipengele mara moja — malipo ya sasiri ni uboreshaji wa hiari; kama kipindi cha majaribio kinaisha na mtumiaji anatua kwenye ukurasa wa sasiri, mtiririko unabadilika kwenye njia ya malipo kiotomatiki. Bila Node, au wakati mtumiaji anaenda kufanya mwenyewe, hurejea kiotomatiki kwenye hali ya mwongozo safi.""",

RD_LINK="""3. **Kuingia kwa bonyezo moja (viungo viwili)**: mara baada ya usajili kufanikiwa, kiungo cha kuingia kinamweka mtumiaji moja kwa moja kwenye ukurasa wa nyumbani (katika kipindi cha majaribio bila malipo, bonyezo moja na kinapatikana);
   kama kinatua kwenye ukurasa wa sasiri (kipindi cha majaribio kimeisha) au mtumiaji anataka kuboresha, fuata mtiririko wa sasiri — baada ya malipo kufika, hali mpya ya kuingia inabadilishwa na kiungo cha uanachama kamili kinamweka kwenye ukurasa wa nyumbani
   (kupitia daraja rasmi la `me?token=` la jukwaa, linalozalisha kuki ya HttpOnly kiotomatiki).""",

LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
