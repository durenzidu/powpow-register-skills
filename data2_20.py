# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: Hausa."""
HA = dict(
    DESC="description: Yana taimaka wa mai amfani kammala rajistar PowPow (Bubble) da shiga da danna daya cikin hirar. Magidiman yana cika fom madadin mai amfani (har da dora hoton bayan gida) kuma yana aika da lambar tabbatar da imel; mai amfani kawai yana bayar da bayanan asali da kuma duban lambar tabbatar da sau daya — ba tare da ya bar tattaunawar ba. Yanar gizo a yanzu yana cikin lokacin gwaji kyauta: asusu da aka yi rajista zai iya amfani da dukkan fannoni nan take; biyan kudi na biya (Alipay/PayPal) karin mamba ne na zabi, wanda magidiman zai iya sarrafawa da kirkirar oda da bin diddigin kudin shiga in da akace. Yana kunna sa'oi da masu amfani na cewa \"yi rajista a Bubble\", \"kirkiro asusu powpow\", \"yaya zan yi rajista a Bubble\", \"taimaka mini kirkirar asusu powpow\", \"sign up powpow\"; kuma yana sarrafa matsalolin rajista (lambar tabbatar da bata zo, sunan mai amfani/imel an riga an rike) da matsalolin kunna (shiga yana cewa \"ba a kunna asusu ba\" / pending_payment, yaya zan biya/yi rajista, Bubble kyauta ne ko kudi). Yana bukatar Node ≥ 18; idan babu shi, ya koma da kansa zuwa yanayin jagorar tsantsa. Ba ya hada buga/kirkirar mutum na dijital (aikin powpow-simple ne), kuma ba ya hada habaka lamba.",
    INTRO="Yana daukar sabon mai amfani daga \"ban san menene Bubble ba\" zuwa \"na shiga da danna daya, a shirye don fara\" — duka a cikin tattaunawar. Mai amfani yana barin tattaunawa sau daya kawai: **don duban lambar tabbatar da a akwatin sakonni**. Yanar gizo a yanzu yana cikin lokacin gwaji kyauta: bayan rajista, dukkan fannoni suna samuwa, babu bukatar biya; biyan kudi na biya karin mamba ne na zabi (magidiman yana bude karfat kudi kuma yana bin diddigin kudin shiga).",
    VLINE="**Sigar 2.2.0** · 2026-10-18 (tun daga v2 wannan yanayin magidiman ne: kwangilar rubutu da cikakken jeri suna a `references/agent-flow.md`; ka'idodin fili, iyakar kima da warware matsala a `references/registration-flow.md`; hanyoyin biya a `references/payment-and-activation.md`; jerin hotunan samfur a `references/screenshots.md`. Tun daga v2.1.0 magidiman zai iya sarrafa rajistar PayPal, azaman zabi tare da Alipay. Tun daga v2.2.0 yanar gizo ya shiga lokacin gwaji kyauta: yi rajista kuma shiga da danna daya don fara amfani; biya ya zama kari na zabi — in mai amfani ya danna hanyar hadi kuma ya sauka a shafin biya, lokacin gwaji ya kare, bi bin jawardar biya daga mataki 7; jawardar tana daidaita kanta, babu bukatar canza rubutu)",
    RT_ENV="- **Babu Node / kuskuren rubutu**: koma da kanka zuwa yanayin jagorar tsantsa — ba mai amfani shafin rajista https://global.powpow.online/register kuma ka bi shi bisa ka'idodin `references/registration-flow.md` (a lokacin gwaji kyauta, rajistar yanar gizo ita ce nan take). Kada ka ci gaba da dukan rubutu.",
    TRIGGER="- Matsalolin bayan rajista: \"shiga yana cewa ba a kunna asusu ba\", \"403 pending_payment\", \"yaya zan biya/yi rajista a Bubble\", \"Bubble kyauta ne ko kudi\"",
    FLOW6="| 6 Shiga da danna daya | `login-link(home)` kai tsaye zuwa shafin gida; in ya sauka a shafin biya, je zuwa mataki 7 | Danna hanyar hadi kuma fara amfani |",
    FLOW7="| 7 Karin rajista (na zabi) | Kawai in mai amfani ya so mamba / lokacin kyauta ya kare: cikakken jawardar biya a sarrafa | Zabi hanya, biya |",
    STEP6="""## Mataki 6: Shiga da danna daya (bayan rajista kai tsaye zuwa shafin gida)

1. Nan take bayan rajista ta samu nasara:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Aika hanyar hadi zuwa ga mai amfani: **danna shi kuma ka sauka kai tsaye a shafin gida, tare da shiga**. Yanar gizo a yanzu yana cikin lokacin gwaji kyauta — bayan rajista dukkan fannoni suna amfani (beam, taswira, mutum na dijital, shaidar ziyara da sauransu), **babu bukatar biya**.
3. Tambayi mai amfani ya tabbatar da shigarsa; akwai halaye biyu:
   - **Ya sauka a shafin gida** → je kai tsaye zuwa mataki 8 don kammala; rajista ta kammala;
   - **Ya sauka a shafin biya** → lokacin gwaji kyauta na yanar gizo ya kare; faɗa wa mai amfani "lokacin gwaji kyauta ya kare, yanzu ana bukatar rajistar mamba", sannan bi mataki 7 don kammala rajista, kuma bayan rajista koma zuwa mataki 8.
4. In mai amfani da kansa ya so kari ko tallafa yanar gizo → je zuwa mataki 7 (rajista son zuciya ne; kada ka tilasta).""",
    STEP7="""## Mataki 7: Karin rajista (na zabi — kawai sa'adda mataki 6 ya nuna)

1. Da fari aika hanyar shiga ta rabi don shafin dawowa bayan biya ya iya nuna "Biya ta samu nasara" daidai:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Aika hanyar hadi zuwa ga mai amfani: danna shi kuma burauza ya sauka kai tsaye a shafin biya, tare da shiga.
2. **Tambayi mai amfani ya zabi hanyar biya** — nuna dukkan hanyoyin biyu:
   - **Alipay (ƙasar Sin / masu amfani da Alipay)**: siyan daya ta wani lokaci, **ba ta sake kanta ba**
     - Na wata **¥6.99** (an shawarata don gwaji) / Na watanni uku **¥19.99** / Na shekara **¥69.99**
   - **PayPal (ketare / marasa Alipay)**: sake kanta kowane wata, soke a kowane lokaci
     - Premium Monthly, kusan **$1/wata** (kamar yadda aka nuna a shafin biya; tare da sake kanta)
3. Da zarar mai amfani ya zabi daya:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Rubutun zai dawo da hanyar fayil din shafin biya; **buɗe shi kai tsaye da umarnin tsarin** (Windows: `start <fayil>`; macOS: `open <fayil>`; Linux: `xdg-open <fayil>`). Burauza zai sake kansa zuwa karfat kudin Alipay/PayPal na hukuma, inda mai amfani zai kammala biya ko izinin cajin kudi.
4. Gudanar da `query` kowane 10–15 dakika har ya dawo da `paid` ko `ACTIVE` (biya/izini yana sauka a cikin yan dakika zuwa minti daya). In mai amfani ya rufe shafin biya a tsakiya → kawai `create-order` sake (tsofaffin oda / rajistar da ta tsaya suna rufe ko karewa bayan awa 2; kauce musu).
5. Hanyar kodin QR ta WeChat ana tabbatar da ita da hannu kuma kudi na iya jinkirta; Huawei IAP yana samuwa kawai a cikin manhajar HarmonyOS. Fasahar ba ta sarrafa waɗannan biyu — bayan biya, mai amfani yana komawa kuma ya faɗa wa magidiman, wanda ya fara gudanar da `whoami` don tabbatar da saukar kudi, sannan ya aika hanyar shafin gida bisa ka'ida 6 a kasa.
6. Bayan tabbatar da saukar kudi, musanya yanayin shiga da kimar rajista ta yanzu, sannan aika hanyar hadi kai tsaye zuwa shafin gida:
   ```
   POWPOW_REGISTER_PASSWORD=<kalmar sirri> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Aika hanyar hadi zuwa ga mai amfani: **danna shi kuma ka sauka kai tsaye a shafin gida tare da cikakken matsayin mamba**.""",
    STEP8="""## Mataki 8: Kammalawa

1. `node scripts/powpow-register.mjs cleanup` don share fayilolin yanayin na wancan lokaci (takaddun zama).
2. Ba mai amfani "katin asusu": sunan mai amfani, imel (ba a sake nuna kalmar sirri — a yanayin kirkira an ce wa mai amfani ya ajiye ta sa'adda aka kirkira; in mai amfani ya saita ta da kansa, ya santa).
3. Tunatarwar mamba (faɗa sau daya, kada ka tilasta): a yanzu lokacin gwaji kyauta ne kuma asusu yana amfani nan take; sa'adda lokacin gwaji ya kare, asusun da ba su yi rajista ba za a mayar da su zuwa shafin biya sa'adda suka shiga shafukan abun ciki — don amfani na dogon lokaci, koyo kuma yi rajista a kowane lokaci.
4. Nuna matakan farko: duba taswira, buga rubutun tafiya na farko (→ mika zuwa powpow-simple).
5. Shawarar fadada: fasahar `@durenzidu/powpow-integration` da plugin din `@durenzidu/openclaw-channel-powpow` — hada Bubble zuwa magidiman mai amfani da kansa; ba da umarnin shigar da in ya so.
6. Kammala da sashin "mataki na gaba".""",
    WALL="- **Katanga ba laifi ba ne**: a cikin lokacin gwaji kyauta na yanzu dukkan shafukan abun ciki suna buɗe; in mai amfani ya danna hanyar shafin gida amma ya sauka a shafin biya — lokacin gwaji ya kare, bishe shi ya yi rajista ta mataki 7. Kada ka kokari wuce katanga, kuma kada ka bayar da ginshikan cikin gida ga mai amfani.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` ko `--target home` | Yana kirkirar hanyar shiga da danna daya (tsarin hanyoyi biyu, duba a kasa) |",
    AF_LINKSEQ="""## Tsarin hanyoyi biyu (tsarin asali)

Yanayin shiga na yanar gizo kuki ne na HttpOnly, wanda magidiman ba zai iya dasa shi kai tsaye a burauza; gada shi ne iyakar
`/api/auth/me?token=<JWT>&redirect=<hanya a cikin gidan yanar gizo>`: tabbatar da sa hannu → kirkira kai tsaye
zama → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / kwanaki 7) → tabbatar da
maye gurbin (dole ya fara da salo daya, `//` da salo masu baya an hana, dole ya zama same-origin bayan warware) → 307 maye gurbin na wancan lokaci zuwa shafin manufa.

Akwai manufofi biyu na hanyoyi, **fara kirkirar home, sannan ka yanke shawarar wucewa pending bisa inda mai amfani ya sauka**:

- **hanyar home (ana aika ta by default, `--target home` → sauka a `/`)**: ana kirkirar ta kuma aika wa mai amfani nan take bayan rajista ta samu nasara.
  A lokacin gwaji kyauta mai amfani yana zuwa shafin gida kai tsaye, cikakken amfani; **in ya danna hanyar amma ya sauka a shafin biya — lokacin gwaji kyauta ya kare** — sauya zuwa jawardar biya (duba a kasa); babu bukatar canza rubutu ko sake yin rajista.
- **hanyar pending (ana amfani da ita a jawardar biya, `--target pending` → sauka a `/subscription`)**:
  burauza mai amfani yana shiga yanayin "rabin shiga": shafin biya da shafin dawowa bayan biya suna bayyana kuma suna aiki. Bayan saukar kudi,
  gudanar da `refresh-login` don musanya sabon JWT tare da kimar ACTIVE, sannan aika hanyar home sake daya don cikakken matsayin mamba.

## Cikakken jeri

### Hanya mai sauri (a lokacin gwaji kyauta — yawancin lokuta)

```
1.  status                          # tabbatar da yanayin kansa
2.  (mataki 2 tattaunawa don tabbatar da bayani, kalmar sirri ko kaza; yanayin kirkira: gen-password → ce wa mai amfani ya ajiye nan take)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → mai amfani yana duba lambar a akwatin sakonni (lokacin barin tattaunawa)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → aika hanyar ga mai amfani; danna daya kuma a shafin gida
7.  (mai amfani ya tabbatar da shigarsa) → kammala nan take: cleanup + katin asusu + nuna matakan farko
```

### Hanyar biya (sa'adda mai amfani ya so mamba, ko lokacin gwaji kyauta ya kare)

```
1–5. Kamar hanya mai sauri (yanayi yana da token bayan rajista ta samu nasara)
6.  login-link --target pending     # → hanyar rabin shiga, tana rike shafin dawowa bayan biya yana aiki
7.  (mai amfani ya zabi hanyar biya)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <fayil din shafin biya>       # Windows; macOS yana amfani da open, Linux yana amfani da xdg-open
    # → mai amfani yana kammala biya/izini a karfat kudin Alipay/PayPal (yana barin tattaunawa)
9.  query (kowane 10–15s) har paid / ACTIVE
10. refresh-login                   # musanya sabon JWT tare da kimar ACTIVE
11. login-link --target home        # → aika hanyar cikakken mamba ga mai amfani
12. whoami                          # tabbatar da subscriptionStatus: ACTIVE (na zabi)
13. cleanup                         # share fayil din yanayi
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Lokacin gwaji kyauta ya kare kuma biya bata sauka ba; koma zuwa mataki 9 don ci gaba da nema, ko tabbatar da cewa mai amfani ya kammala biya |",
    AF_ERR_SUB="| Mai amfani ya danna hanyar gida amma ya sauka a shafin biya | Lokacin gwaji kyauta ya kare → sauya zuwa jawardar biya: `login-link --target pending` → zabi hanyar biya → `create-order` |",
    AF_FALLBACK="Bayan koma: ba shafin rajista https://global.powpow.online/register (a lokacin gwaji kyauta, rajistar yanar gizo ita ce nan take; sa'adda ana bukatar rajista, ba shafin biya kuma https://global.powpow.online/subscription ), warware matsala tare bisa ka'idodin `registration-flow.md`, riƙe kalar magana daya, kuma kammala kowane juyi da sashin \"mataki na gaba\".",
    PA_NOTE="""> **Lokacin gwaji kyauta (tun daga 2026-10-18; halayen yanar gizo na gaske ya fi)**: a wannan lokaci asusu da aka yi rajista zai iya amfani da dukkan fannoni kai tsaye, kuma **yi rajista kari ne na zabi ba wajibi ba** — bi jawardar wannan fayil kawai sa'adda mai amfani da kansa ya so mamba. Sa'adda lokacin gwaji ya kare, asusun da ba su yi rajista ba za a mayar da su zuwa shafin biya sa'adda suka shiga shafukan abun ciki; kammala rajista bisa wannan fayil.""",
    RF_STATE="""## Jawardar yanayi bayan rajista ta samu nasara

> **Lokacin gwaji kyauta (tun daga 2026-10-18; halayen yanar gizo na gaske ya fi)**: sabon asusu da aka yi rajista **zai iya amfani da dukkan fannoni kai tsaye**
> (beam, taswira, mutum na dijital, shaidar ziyara da sauransu) babu bukatar biya; ba a ƙara katanga ga asusun da ba su yi rajista ba daga shafukan abun ciki. "Ajiyen pending"
> da aka bayyana a wannan sashe yanayi na al'ada ne bayan ƙarewar lokacin gwaji — sa'adda lokacin ya zo, halayen yanar gizo na gaske ya fi.

1. Ana adana mai amfani tare da `accountStatus: 'pending'` da **badge 3 na farko** (hanyar rajista).
2. Sabar kuma tana dasa kuki biyu na HttpOnly: JWT (zai iya shiga shafuna kai tsaye) da pendingUserToken (takaddar shaida don jawardar biya).
3. A yanayi na al'ada (lokacin gwaji ya kare / babu lokacin kyauta), shafin rajista yana gano `pending_payment` → mayar da shi zuwa `/subscription`
   (tare da riƙe parameter din dawowa `next`); a yanayin magidiman, `me?token=…&redirect=/subscription` yana samun sakamaron daya.
   **A lokacin gwaji kyauta wannan mataki baya kunna** — bayan rajista, je kai tsaye zuwa shafin gida kuma fara amfani.
4. Biya ta kammala → `accountStatus` ya zama `active` (**Alipay yana kunna shi kai tsaye ta wajen sabar ta notify**;
   PayPal yana kunna shi ta Webhook; lambar QR ta WeChat ana tabbatar da ita da hannu; Huawei IAP yana wucewa ta `activate-huawei`).
   Duba `payment-and-activation.md` don cikakkun bayani.

A yanayi na al'ada, masu amfani marasa kunna (pending) suna kiran API din asali (beam, taswira, hiran mutum na dijital, shaidar ziyara da sauransu) suna samun 403;
hanyoyin hadin rubuta da aka raba suna bambanta (ana riƙe su a buɗe). A lokacin gwaji kyauta an dakatar da wannan ajiye kuma dukkan suna buɗe.""",
    RF_ROW_403="| An yi rajista da nasara amma shiga ya dawo da 403 \"请完成订阅以激活账户\" | Asusu har yanzu pending ne kuma yanar gizo ba shi cikin lokacin gwaji kyauta (yanayin da ake tsammani kafin biya) | Ba zai faru a lokacin gwaji kyauta ba; in ya faru, lokacin gwaji ya kare — kammala rajista da fari; in har yana 403 bayan biya, an yi amfani da JWT na tsohuwa — a yanayin rubutu fara gudanar da `refresh-login` don musanya sabon yanayin shiga |",
    RF_ROW_LAND="| Mai amfani ya danna hanyar shiga amma ya sauka a shafin biya (maimakon shafin gida) | Lokacin gwaji kyauta ya kare kuma katanga biya na yanar gizo ya dawo | Bi jawardar biyan rajista ta mataki 7 a SKILL.md; bayan rajista, gudanar da `refresh-login` sannan aika hanyar shafin gida |",
    RD_VER="""**Tun daga v2.0.0 wannan yanayin magidiman ne, kuma tun daga v2.2.0 yana daidaita da lokacin gwaji kyauta na yanar gizo**: rubutu na asali `scripts/powpow-register.mjs` ba shi da bukatar abun biya
(Node ≥ 18); mai amfani yana barin tattaunawa sau daya kawai: don duban lambar tabbatar da a akwatin sakonni. A cikin lokacin gwaji kyauta na yanzu, asusu da aka yi rajista zai iya amfani da dukkan fannoni nan take — biyan kudi na biya kari ne na zabi; in lokacin gwaji ya kare kuma mai amfani ya sauka a shafin biya, jawardar tana sauya kanta zuwa hanyar biya. Ba tare da Node, ko sa'adda mai amfani ya fi son yin shi da kansa, yana koma kai tsaye zuwa yanayin jagorar tsantsa.""",
    RD_LINK="""3. **Shiga da danna daya (hanyoyi biyu)**: nan take bayan rajista ta samu nasara, hanyar shiga tana kai mai amfani kai tsaye zuwa shafin gida (a lokacin gwaji kyauta, danna daya kuma yana amfani);
   in ya sauka a shafin biya (lokacin gwaji ya kare) ko mai amfani ya so kari, bi jawardar rajista — bayan saukar kudi, ana musanya sabon yanayin shiga kuma hanyar cikakken mamba tana kai shi zuwa shafin gida
   (ta hanyar gada `me?token=` na yanar gizo na hukuma, wanda ke dasa kuki na HttpOnly kai tsaye).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
