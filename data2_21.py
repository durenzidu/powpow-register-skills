# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: Javanese."""
JV = dict(
    DESC="description: Mbantu pangguna ngrampungake registrasi PowPow (Bubble) lan mlebu siji klik ing sajroning rembugan. Agen ngisi formulir minangka pangguna (kalebu unggah avatar) lan ngirim kode verifikasi email; pangguna mung menehi informasi dhasar lan ndelok kode verifikasi sepisan — tanpa ninggal rembugan. Platform saiki lagi ing wektu coba gratis: akun sing wis didhaftar bisa langsung nggunakake kabeh fitur; pambayaran langganan (Alipay/PayPal) iku peningkatan keanggotaan opsional, sing uga bisa ditangani agen kanthi nggawe pesenan lan nglacak dana mlebu yen perlu. Dipicu nalika pangguna ngomong \"dhaptar Bubble\", \"gawe akun powpow\", \"piye cara dhaptar Bubble\", \"mbantu aku gawe akun powpow\", \"sign up powpow\"; uga nangani masalah registrasi (kode verifikasi ora teka, jeneng pangguna/email wis dijupuk) lan masalah aktivasi (nalika mlebu kandha \"akun durung diaktifake\" / pending_payment, piye cara langganan/mbayar, Bubble gratis utawa mbayar). Mbutuhake Node ≥ 18; yen ora kasedhiya, otomatis bali menyang mode pandhuan murni. Ora kalebu posting/gawe manungsa digital (iku tugas powpow-simple), uga ora kalebu pengembangan kode.",
    INTRO="Nggawa pangguna anyar saka \"aku ora ngerti Bubble kuwi apa\" dadi \"mlebu siji klik, siap dipa\" — kabeh ing sajroning rembugan. Pangguna mung ninggal rembugan sepisan: **kanggo ndelok kode verifikasi ing inbox**. Platform saiki lagi ing wektu coba gratis: sawise dhaptar, kabeh fitur kasedhiya, ora perlu mbayar; pambayaran langganan iku peningkatan keanggotaan opsional (agen uga mbukak kasir lan nglacak dana mlebu).",
    VLINE="**Versi 2.2.0** · 2026-10-18 (wiwit v2 iki mode bantuan agen: kontrak skrip lan urutan lengkap ana ing `references/agent-flow.md`; aturan kolom, wates laju, lan diagnosa kesalahan ana ing `references/registration-flow.md`; saluran pambayaran ana ing `references/payment-and-activation.md`; dhaptar cuplikan produk ana ing `references/screenshots.md`. Wiwit v2.1.0 langganan PayPal uga bisa ditangani agen, minangka pilihan bareng karo Alipay. Wiwit v2.2.0 platform mlebu wektu coba gratis: dhaptar banjur mlebu siji klik langsung bisa dipa; pambayaran dadi peningkatan opsional — yen pangguna mbukak link banjur mandheg ing kaca langganan, wektu coba wis rampung, tindakake alur pambayaran saka langkah 7; alurnya nyetel dhewe, ora perlu ngowahi skrip)",
    RT_ENV="- **Ora ana Node / kesalahan skrip**: otomatis bali menyang mode pandhuan murni — menehi pangguna kaca registrasi https://global.powpow.online/register lan nuntun bebarengan miturut `references/registration-flow.md` (ing wektu coba gratis, registrasi web uga padha cepet). Aja terus nggodhog skrip.",
    TRIGGER="- Masalah sawise registrasi: \"nalika mlebu kandha akun durung diaktifake\", \"403 pending_payment\", \"piye cara mbayar/langganan ing Bubble\", \"Bubble gratis utawa mbayar\"",
    FLOW6="| 6 Mlebu siji klik | `login-link(home)` langsung menyang kaca ngarep; yen mandheg ing kaca langganan, mangkat menyang langkah 7 | Klik link lan miwiti dipa |",
    FLOW7="| 7 Peningkatan langganan (opsional) | Mung nalika pangguna pengin keanggotaan / wektu gratis wis rampung: tangani alur pambayaran lengkap | Pilih cara, mbayar |",
    STEP6="""## Langkah 6: Mlebu siji klik (sawise registrasi langsung menyang kaca ngarep)

1. Sawise registrasi kasil:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Kirim link menyang pangguna: **klik lan kowe langsung menyang kaca ngarep, wis mlebu**. Platform saiki lagi ing wektu coba gratis — sawise dhaptar, kabeh fitur bisa dipa (feed, peta, manungsa digital, check-in, lsp), **ora perlu mbayar**.
3. Takon pangguna konfirmasi wis mlebu; ana rong kahanan:
   - **Manggat menyang kaca ngarep** → langsung mangkat menyang langkah 8 kanggo ngrampungake; registrasi rampung;
   - **Mandheg ing kaca langganan** → wektu coba gratis platform wis rampung; kandha pangguna "wektu coba gratis wis rampung, saiki butuh langganan keanggotaan", banjur tindakake langkah 7 kanggo ngrampungake langganan, lan sawise langganan bali menyang langkah 8.
4. Yen pangguna dewe pengin nambah utawa ndhukung platform → uga tindakake langkah 7 (langganan sukarela; aja meksa).""",
    STEP7="""## Langkah 7: Peningkatan langganan (opsional — mung nalika langkah 6 njaluk)

1. Dhisik kirim link mlebu separo supaya kaca bali sawise pambayaran bisa nuduhake "Pembayaran kasil" kanthi bener:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Kirim link menyang pangguna: klik lan browser langsung menyang kaca langganan, wis mlebu.
2. **Takon pangguna milih cara pambayaran** — tuduhake rong saluran:
   - **Alipay (daratan Cina / pangguna nganggo Alipay)**: tuku sepisan kanggo wektu sing cocog, **ora auto-renewal**
     - Saben wulan **¥6.99** (disaranake kanggo nyoba) / Telung wulan **¥19.99** / Saben taun **¥69.99**
   - **PayPal (maneka negara / tanpa Alipay)**: auto-renewal saben wulan, bisa dibatalake kapan wae
     - Premium Monthly, kira-kira **$1/wulan** (kaya sing katuduhake ing kaca langganan; karo auto-renewal)
3. Sawise pangguna milih siji:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Skrip bakal mbalekake path file kaca pambayaran; **bukak langsung nganggo printah sistem** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Browser bakal otomatis pindhah menyang kasir resmi Alipay/PayPal, panggonan pangguna ngrampungake pambayaran utawa otorisasi tagihan.
4. Lakokake `query` saben 10–15 detik nganti mbalekake `paid` utawa `ACTIVE` (pembayaran/otorisasi biasane mlebu ing sawetara detik nganti sakmenit). Yen pangguna nutup kaca pambayaran ing tengah → mung `create-order` maneh (pesenan lawas / langganan mandheg bakal nutup utawa kadaluwarsa sawise 2 jam; aja digatekake).
5. Saluran kode QR WeChat dikonfirmasi kanthi manual lan dana bisa mlecu; Huawei IAP mung kasedhiya ing sajroning aplikasi HarmonyOS. Skrip ora nangani loro kuwi — sawise mbayar, pangguna bali lan kandha agen, sing dhisik lakokake `whoami` kanggo konfirmasi dana mlebu, banjur kirim link kaca ngarep miturut poin 6 ing ngisor iki.
6. Sawise dana mlebu dikonfirmasi, gentiak kahanan mlebu karo klaim langganan paling anyar, banjur kirim link langsung menyang kaca ngarep:
   ```
   POWPOW_REGISTER_PASSWORD=<sandi> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Kirim link menyang pangguna: **klik lan kowe langsung menyang kaca ngarep karo status keanggotaan lengkap**.""",
    STEP8="""## Langkah 8: Ngrampungake

1. `node scripts/powpow-register.mjs cleanup` kanggo ngresiki file kahanan sementara lokal (kredensial sesi).
2. Menehi pangguna "kartu akun": jeneng pangguna, email (sandi ora dituduhake maneh — ing mode generate pangguna dikon ndelok nalika digawe; yen pangguna nyetel dewe, dheweke ngerti).
3. Pangeling-eling keanggotaan (kandha sepisan, aja meksa): saiki lagi wektu coba gratis lan akun bisa langsung dipa; nalika wektu coba rampung, akun tanpa langganan nalika mlebu kaca isi bakal dialihakake menyang kaca langganan — kanggo dipa suwe, bali lan langganan kapan wae.
4. Tuduhake langkah awal: delok peta, posting jurnal perjalanan pisanan (→ serahake menyang powpow-simple).
5. Rekomendasi ekstensi: skill `@durenzidu/powpow-integration` lan plugin `@durenzidu/openclaw-channel-powpow` — sambungake menyang agen dhewe pangguna; menehi printah instalasi yen dikarepake.
6. Rampungake karo blok "langkah sabanjure".""",
    WALL="- **Paywall dudu bug**: ing wektu coba gratis saiki kabeh kaca isi kabukak; yen pangguna klik link kaca ngarep nanging mandheg ing kaca langganan — wektu coba wis rampung, tuduhake langganan liwat langkah 7. Aja nyoba ngapusi paywall, lan aja nerangake mekanisme internal menyang pangguna.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` utawa `--target home` | Nggawe link mlebu siji klik (desain rong link, delok ngisor) |",
    AF_LINKSEQ="""## Mekanisme rong link (desain inti)

Kahanan mlebu platform iku cookie HttpOnly, sing ora bisa ditancemake agen langsung menyang browser; jembatan iku titik pungkasan resmi
`/api/auth/me?token=<JWT>&redirect=<path ing sajroning situs>`: verifikasi tanda tangan → gawe otomatis
sesi → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 dina) → validasi
redirect (kudu diwiwani karo slash tunggal, `//` lan slash mburi dilarang, kudu same-origin sawise diurai) → 307 redirect sementara menyang kaca target.

Ana rong target link, **dhisik gawe home, banjur mutusake liwat pending utawa ora adhedhasar ngendi pangguna mandheg**:

- **link home (dikirim kanthi default, `--target home` → mandheg ing `/`)**: digawe lan dikirim menyang pangguna sawise registrasi kasil.
  Ing wektu coba gratis pangguna langsung menyang kaca ngarep, kabeh bisa dipa; **yen dheweke klik nanging mandheg ing kaca langganan — wektu coba gratis wis rampung** — pindhah menyang alur pambayaran (delok ngisor); ora perlu ngowahi skrip lan registrasi maneh.
- **link pending (dipakai ing alur pambayaran, `--target pending` → mandheg ing `/subscription`)**:
  browser pangguna mlebu kahanan "mlebu separo": kaca langganan lan kaca bali sawise pambayaran katon lan bisa dioperasikake. Sawise pambayaran mlebu,
  lakokake `refresh-login` kanggo gentiak JWT anyar karo klaim ACTIVE, banjur kirim link home maneh kanggo status keanggotaan lengkap.

## Urutan lengkap

### Alur cepet (ing wektu coba gratis — mayoritas kahanan)

```
1.  status                          # pemeriksaan kahanan lingkungan
2.  (langkah 2 rembugan konfirmasi informasi, sandi bebas; mode generate: gen-password → kon pangguna simen langsung)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → pangguna ndelok kode ing inbox (sasi-sasi ninggal rembugan)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → kirim link menyang pangguna; siji klik langsung ing kaca ngarep
7.  (pangguna konfirmasi wis mlebu) → langsung rampung: cleanup + kartu akun + tuduhake langkah awal
```

### Alur pambayaran (nalika pangguna pengin keanggotaan, utawa wektu coba gratis wis rampung)

```
1–5. Padha karo alur cepet (kahanan wis nduweni token sawise registrasi kasil)
6.  login-link --target pending     # → link mlebu separo, njaga kaca bali pambayaran bisa mlaku
7.  (pangguna milih cara pambayaran)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <file kaca pambayaran>       # Windows; macOS nggunakake open, Linux nggunakake xdg-open
    # → pangguna ngrampungake pambayaran/otorisasi ing kasir Alipay/PayPal (ninggal rembugan)
9.  query (saben 10–15s) nganti paid / ACTIVE
10. refresh-login                   # gentiak JWT anyar karo klaim ACTIVE
11. login-link --target home        # → kirim link keanggotaan lengkap menyang pangguna
12. whoami                          # konfirmasi subscriptionStatus: ACTIVE (opsional)
13. cleanup                         # resikake file kahanan
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Wektu coba gratis wis rampung lan pambayaran durung mlebu; bali menyang langkah 9 terus ngenteni, utawa konfirmasi apa pangguna wis ngrampungake pambayaran |",
    AF_ERR_SUB="| Pangguna klik link home nanging mandheg ing kaca langganan | Wektu coba gratis wis rampung → pindhah menyang alur pambayaran: `login-link --target pending` → pilih cara pambayaran → `create-order` |",
    AF_FALLBACK="Sawise bali: menehi kaca registrasi https://global.powpow.online/register (ing wektu coba gratis, registrasi web uga padha cepet; nalika langganan dibutuhake, menehi kaca langganan uga https://global.powpow.online/subscription ), tangani bebarengan miturut aturan ing `registration-flow.md`, njaga swara padha, lan tansah rampungake saben giliran karo blok \"langkah sabanjure\".",
    PA_NOTE="""> **Wektu coba gratis (wiwit 2026-10-18; tumindak platform nyata sing absah)**: ing wektu iki akun sing wis didhaftar bisa langsung nggunakake kabeh fitur, lan **langganan iku peningkatan opsional dudu syarat** — mung tindakake alur file iki nalika pangguna dewe pengin keanggotaan. Nalika wektu coba rampung, akun tanpa langganan nalika mlebu kaca isi bakal dialihakake menyang kaca langganan; cukup ngrampungake langganan miturut file iki.""",
    RF_STATE="""## Alur kahanan sawise registrasi kasil

> **Wektu coba gratis (wiwit 2026-10-18; tumindak platform nyata sing absah)**: akun anyar sing didhaftar bisa **langsung nggunakake kabeh fitur**
> (feed, peta, manungsa digital, check-in, lsp) tanpa pambayaran; akun tanpa langganan ora dikurung maneh saka kaca isi. "Pencekalan pending"
> sing dijelasake ing bagean iki yaiku kahanan lumrah sawise wektu coba rampung — nalika wektu kuwi teka, tumindak online nyata sing absah.

1. Pangguna disimpen karo `accountStatus: 'pending'` lan **3 lencana awal** (rute register).
2. Server uga nancepake rong cookie HttpOnly: JWT (bisa mlebu kaca langsung) lan pendingUserToken (kredensial identitas kanggo alur langganan).
3. Ing kahanan lumrah (wektu coba rampung / ora ana wektu gratis), kaca registrasi ndeteksi `pending_payment` → dialihakake menyang `/subscription`
   (njaga parameter bali `next`); ing mode bantuan agen, `me?token=…&redirect=/subscription` entuk efek sing padha.
   **Ing wektu coba gratis langkah iki ora dipicu** — sawise dhaptar, langsung menyang kaca ngarep lan miwiti dipa.
4. Pambayaran rampung → `accountStatus` dadi `active` (**Alipay ngaktifake kanthi otomatis sisi server liwat notify**;
   PayPal ngaktifake liwat Webhook; kode QR WeChat dikonfirmasi manual; Huawei IAP liwat `activate-huawei`).
   Delok `payment-and-activation.md` kanggo rincian.

Ing kahanan lumrah, pangguna ora aktif (pending) nimbali API inti (feed, peta, obrolan manungsa digital, check-in, lsp) entuk 403;
link posting sing dibagi dadi pengecualian (tetap bisa diakses publik). Ing wektu coba gratis pencekalan iki disendheksa lan kabeh kabukak.""",
    RF_ROW_403="| Kasil registrasi nanging mlebu mbalekake 403 \"请完成订阅以激活账户\" | Akun isih pending, lan platform ora ing wektu coba gratis (kahanan sing dikarepake sadurunge pambayaran) | Ora bakal kelakon ing wektu coba gratis; yen kelakon, wektu coba wis rampung — rampungake langganan dhisik; yen isih 403 sawise mbayar, JWT lawas sing dipakai — ing mode skrip dhisik lakokake `refresh-login` kanggo gentiak kahanan mlebu anyar |",
    RF_ROW_LAND="| Pangguna klik link mlebu nanging mandheg ing kaca langganan (dudu kaca ngarep) | Wektu coba gratis wis rampung lan paywall platform bali | Tindakake alur pambayaran langganan langkah 7 ing SKILL.md; sawise langganan, lakokake `refresh-login` banjur kirim link kaca ngarep |",
    RD_VER="""**Wiwit v2.0.0 iki mode bantuan agen, lan wiwit v2.2.0 nyetel dhewe karo wektu coba gratis platform**: skrip inti `scripts/powpow-register.mjs` tanpa dependensi
(Node ≥ 18); pangguna mung ninggal rembugan sepisan: kanggo ndelok kode verifikasi ing inbox. Ing wektu coba gratis saiki, akun sing wis didhaftar bisa langsung nggunakake kabeh fitur — pambayaran langganan iku peningkatan opsional; yen wektu coba rampung lan pangguna mandheg ing kaca langganan, alur pindhah menyang alur pambayaran kanthi otomatis. Tanpa Node, utawa nalika pangguna luwih seneng dewe, otomatis bali menyang mode pandhuan murni.""",
    RD_LINK="""3. **Mlebu siji klik (rong link)**: sawise registrasi kasil, link mlebu langsung nggawa pangguna menyang kaca ngarep (ing wektu coba gratis, siji klik langsung bisa dipa);
   yen mandheg ing kaca langganan (wektu coba rampung) utawa pangguna pengin nambah, tindakake alur langganan — sawise pambayaran mlebu, kahanan mleku anyar digentiak lan link keanggotaan lengkap nggawa menyang kaca ngarep
   (liwat jembatan resmi `me?token=` platform, sing nancepake cookie HttpOnly kanthi otomatis).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
