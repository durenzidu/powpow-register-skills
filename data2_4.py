# -*- coding: utf-8 -*-
"""v2.1.0 -> v2.2.0 delta translations: Indonesian."""
ID = dict(
    DESC="description: Membantu pengguna menyelesaikan pendaftaran PowPow (Bubble) dan login sekali klik sepenuhnya di dalam percakapan. Agent mengisi formulir atas nama pengguna (termasuk unggah avatar) dan mengirim kode verifikasi email; pengguna hanya perlu memberikan informasi dasar dan memeriksa kode verifikasi sekali — tanpa pernah meninggalkan percakapan. Platform saat ini sedang dalam masa uji coba gratis: akun yang sudah terdaftar langsung bisa memakai semua fitur; pembayaran langganan (Alipay/PayPal) adalah peningkatan keanggotaan opsional, yang juga bisa ditangani agent dengan pembuatan pesanan dan pelacakan dana masuk bila diperlukan. Terpicu ketika pengguna mengatakan \"daftar Bubble\", \"buat akun powpow\", \"cara daftar Bubble\", \"bantu saya buat akun powpow\", \"sign up powpow\"; juga menangani masalah pendaftaran (kode verifikasi tidak masuk, nama pengguna/email sudah dipakai) dan masalah aktivasi (saat login bilang \"akun belum diaktivasi\" / pending_payment, cara langganan/bayar, Bubble gratis atau berbayar). Membutuhkan Node ≥ 18; bila tidak tersedia, otomatis beralih ke mode panduan murni. Tidak mencakup posting/membuat manusia digital (itu tugas powpow-simple), maupun pengembangan kode.",
    INTRO="Membawa pengguna baru dari \"tidak tahu Bubble itu apa\" menjadi \"login sekali klik, siap dimainkan\" — seluruhnya di dalam percakapan. Pengguna hanya meninggalkan percakapan satu kali: **untuk memeriksa kode verifikasi di kotak masuk**. Platform saat ini sedang dalam masa uji coba gratis: setelah mendaftar, semua fitur bisa dipakai, tidak perlu bayar; pembayaran langganan adalah peningkatan keanggotaan opsional (agent juga membuka kasir dan melacak dana masuk).",
    VLINE="**Versi 2.2.0** · 2026-10-18 (sejak v2 ini mode perantara agent: kontrak skrip dan urutan lengkap ada di `references/agent-flow.md`; aturan field, batas laju, dan diagnosa error di `references/registration-flow.md`; kanal pembayaran di `references/payment-and-activation.md`; daftar tangkapan layar produk di `references/screenshots.md`. Sejak v2.1.0 langganan PayPal juga bisa ditangani agent, sebagai pilihan bersama Alipay. Sejak v2.2.0 platform memasuki masa uji coba gratis: daftar lalu login sekali klik langsung bisa dipakai; pembayaran berubah menjadi peningkatan opsional — jika pengguna membuka link dan mendarat di halaman langganan, berarti masa uji coba telah berakhir, ikuti alur pembayaran dari langkah 7; alurnya menyesuaikan sendiri, tidak perlu ubah skrip)",
    RT_ENV="- **Node tidak ada / skrip error**: otomatis beralih ke mode panduan murni — beri pengguna halaman pendaftaran https://global.powpow.online/register dan dampingi sesuai `references/registration-flow.md` (selama masa uji coba gratis, pendaftaran lewat web sama-sama langsung bisa dipakai). Jangan memaksa skrip berulang kali.",
    TRIGGER="- Masalah setelah daftar: \"login bilang akun belum diaktivasi\", \"403 pending_payment\", \"cara bayar/langganan Bubble\", \"Bubble gratis atau berbayar\"",
    FLOW6="| 6 Login sekali klik | `login-link(home)` langsung ke beranda; jika mendarat di halaman langganan, lanjut ke langkah 7 | Klik link dan mulai main |",
    FLOW7="| 7 Peningkatan langganan (opsional) | Hanya bila pengguna mau keanggotaan / masa gratis telah berakhir: tangani seluruh alur pembayaran | Pilih metode, bayar |",
    STEP6="""## Langkah 6: Login Sekali Klik (setelah daftar langsung ke beranda)

1. Tepat setelah pendaftaran berhasil:
   ```
   node scripts/powpow-register.mjs login-link --target home
   ```
2. Kirim linknya ke pengguna: **diklik dan langsung berada di beranda, sudah login**. Platform saat ini sedang dalam masa uji coba gratis — setelah mendaftar, semua fitur (feed, peta, manusia digital, check-in, dll.) bisa dipakai, **tidak perlu bayar**.
3. Minta pengguna mengonfirmasi bahwa dia berhasil masuk; ada dua kemungkinan:
   - **Mendarat di beranda** → langsung lompat ke langkah 8 untuk menutup; pendaftaran selesai;
   - **Mendarat di halaman langganan** → masa uji coba gratis platform telah berakhir; katakan kepada pengguna \"masa uji coba gratis sudah selesai, sekarang perlu langganan keanggotaan\", lalu ikuti langkah 7 untuk menyelesaikan langganan, dan kembali ke langkah 8 setelah berlangganan.
4. Jika pengguna sendiri ingin meningkatkan atau mendukung platform → juga arahkan ke langkah 7 (berlangganan itu sukarela; jangan mendesak).""",
    STEP7="""## Langkah 7: Peningkatan Langganan (opsional — hanya bila langkah 6 memintanya)

1. Pertama kirim link login-setengah agar halaman kembali setelah pembayaran bisa menampilkan \"Pembayaran berhasil\" dengan benar:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Kirim linknya ke pengguna: diklik dan browser langsung berada di halaman langganan, sudah login.
2. **Minta pengguna memilih metode pembayaran** — tampilkan kedua kanal:
   - **Alipay (Tiongkok daratan / pengguna punya Alipay)**: pembelian sekali jalan untuk durasi yang dipilih, **tanpa perpanjangan otomatis**
     - Bulanan **¥6.99** (disarankan untuk mencoba) / Triwulanan **¥19.99** / Tahunan **¥69.99**
   - **PayPal (luar negeri / pengguna tanpa Alipay)**: perpanjangan otomatis tiap bulan, batalkan kapan saja
     - Premium Monthly, sekitar **$1/bulan** (sesuai tampilan di halaman langganan; perpanjangan otomatis)
3. Setelah pengguna memilih:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Skrip mengembalikan path file halaman pembayaran; **buka langsung dengan perintah sistem** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Browser otomatis melompat ke kasir resmi Alipay/PayPal, tempat pengguna menyelesaikan pembayaran atau otorisasi penagihan.
4. Jalankan `query` setiap 10–15 detik sampai mengembalikan `paid` atau `ACTIVE` (dana masuk/otorisasi biasanya mendarat dalam beberapa detik sampai satu menit). Jika pengguna menutup halaman pembayaran di tengah jalan → cukup `create-order` lagi (pesanan lama / langganan menggantung otomatis tutup atau kedaluwarsa setelah 2 jam; abaikan).
5. Kanal kode QR WeChat dikonfirmasi manual, dana masuk bisa terlambat; Huawei IAP hanya tersedia di dalam aplikasi HarmonyOS. Skill tidak menangani keduanya — setelah membayar, pengguna kembali dan memberi tahu agent, yang lebih dulu menjalankan `whoami` untuk mengonfirmasi dana masuk, lalu mengirim link beranda sesuai poin 6 di bawah.
6. Setelah dana masuk dikonfirmasi, tukar dengan status login terbaru yang membawa claim langganan terkini, lalu kirim link langsung ke beranda:
   ```
   POWPOW_REGISTER_PASSWORD=<kata sandi> node scripts/powpow-register.mjs refresh-login
   node scripts/powpow-register.mjs login-link --target home
   ```
   Kirim linknya ke pengguna: **diklik dan langsung berada di beranda dengan status keanggotaan penuh**.""",
    STEP8="""## Langkah 8: Menutup

1. `node scripts/powpow-register.mjs cleanup` untuk membersihkan file status sementara lokal (kredensial sesi).
2. Beri pengguna sebuah \"kartu akun\": nama pengguna, email (kata sandi tidak ditampilkan lagi — di mode generasi, pengguna diminta menyimpannya saat dibuat; jika pengguna menyetel sendiri, dia sudah tahu).
3. Pengingat keanggotaan (katakan sekali, jangan mendesak): saat ini masa uji coba gratis dan akun langsung bisa dipakai; ketika masa uji coba berakhir, akun tanpa langganan yang mengunjungi halaman konten akan dialihkan ke halaman langganan — untuk pemakaian jangka panjang, kembali lagi dan berlangganan kapan saja.
4. Pandu langkah pertama: jelajahi peta, unggah jurnal perjalanan pertama (→ serahkan ke powpow-simple).
5. Rekomendasikan ekstensi: skill `@durenzidu/powpow-integration` dan plugin `@durenzidu/openclaw-channel-powpow` — hubungkan Bubble ke agent milik pengguna sendiri; beri perintah instalasi bila mau.
6. Akhiri dengan blok \"langkah selanjutnya".""",
    WALL="- **Paywall bukan bug**: selama masa uji coba gratis saat ini semua halaman konten terbuka; jika pengguna mengklik link beranda tetapi mendarat di halaman langganan, masa uji coba telah berakhir — bimbing mereka berlangganan lewat langkah 7. Jangan mencoba mengakali paywall, dan jangan menjelaskan mekanisme internal kepada pengguna.",
    AF_ROW_LOGIN="| `login-link` | `--target pending` atau `--target home` | Membuat link login sekali klik (desain dua link, lihat di bawah) |",
    AF_LINKSEQ="""## Mekanisme Dua Link (desain inti)

Status login platform adalah cookie HttpOnly, yang tidak bisa ditanam agent langsung ke browser; jembatannya adalah endpoint resmi
`/api/auth/me?token=<JWT>&redirect=<path dalam situs>`: verifikasi tanda tangan → otomatis membuat
sesi → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 hari) → validasi
redirect (harus dimulai dengan satu garis miring, `//` dan garis miring terbalik dilarang, setelah diparse harus same-origin) → 307 redirect sementara ke halaman target.

Ada dua target link, **utamakan membuat home lebih dulu, lalu putuskan apakah lewat pending berdasarkan di mana pengguna mendarat**:

- **link home (dikirim secara default, `--target home` → mendarat di `/`)**: dibuat dan dikirim ke pengguna tepat setelah pendaftaran berhasil.
  Selama masa uji coba gratis pengguna langsung menuju beranda dan semuanya bisa dipakai; **jika ia mengkliknya tetapi mendarat di halaman langganan, masa uji coba gratis telah berakhir** — beralih ke alur pembayaran (lihat di bawah); tanpa ubah skrip dan tanpa daftar ulang.
- **link pending (dipakai di alur pembayaran, `--target pending` → mendarat di `/subscription`)**:
  browser pengguna masuk ke status \"login setengah\": halaman langganan dan halaman kembali setelah pembayaran terlihat dan bisa dioperasikan. Setelah dana masuk,
  jalankan `refresh-login` untuk menukar JWT baru dengan claim ACTIVE, lalu kirim link home sekali lagi untuk status keanggotaan penuh.

## Urutan Lengkap

### Jalur Cepat (selama masa uji coba gratis — mayoritas kasus)

```
1.  status                          # self-check lingkungan
2.  (langkah 2: percakapan konfirmasi info, kata sandi terserah; mode generasi: gen-password → minta pengguna segera menyimpan)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → pengguna periksa kode di kotak masuk (satu-satunya keluar dari percakapan)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target home        # → kirim link ke pengguna; sekali klik langsung di beranda
7.  (pengguna konfirmasi sudah masuk) → langsung tutup: cleanup + kartu akun + panduan langkah pertama
```

### Jalur Pembayaran (bila pengguna ingin keanggotaan, atau masa uji coba gratis telah berakhir)

```
1–5. Sama dengan Jalur Cepat (status sudah punya token setelah register berhasil)
6.  login-link --target pending     # → link login setengah, halaman kembali setelah pembayaran tetap bekerja
7.  (pengguna memilih metode pembayaran)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <file halaman pembayaran> # Windows; macOS pakai open, Linux pakai xdg-open
    # → pengguna menyelesaikan pembayaran/otorisasi di kasir Alipay/PayPal (keluar dari percakapan)
9.  query (setiap 10–15 s) sampai paid / ACTIVE
10. refresh-login                   # tukar ke JWT baru dengan claim ACTIVE
11. login-link --target home        # → kirim link keanggotaan penuh ke pengguna
12. whoami                          # konfirmasi subscriptionStatus: ACTIVE (opsional)
13. cleanup                         # bersihkan file status
```""",
    AF_ERR_403="| `refresh-login` 403 `pending_payment` | Masa uji coba gratis telah berakhir dan pembayaran belum masuk; kembali ke langkah 9 untuk terus polling, atau konfirmasi apakah pengguna sudah menyelesaikan pembayaran |",
    AF_ERR_SUB="| Pengguna mengklik link home tetapi mendarat di halaman langganan | Masa uji coba gratis telah berakhir → beralih ke alur pembayaran: `login-link --target pending` → pilih metode pembayaran → `create-order` |",
    AF_FALLBACK="Setelah beralih: beri halaman pendaftaran https://global.powpow.online/register (selama masa uji coba gratis, pendaftaran lewat web sama-sama langsung bisa dipakai; bila langganan diperlukan, beri juga halaman langganan https://global.powpow.online/subscription ), tangani masalah sambil mendampingi sesuai aturan di `registration-flow.md`, jaga nada yang sama, dan tetap akhiri setiap giliran dengan blok \"langkah selanjutnya\".",
    PA_NOTE="""> **Masa uji coba gratis (mulai 2026-10-18; perilaku aktual platform yang berlaku)**: selama periode ini akun yang sudah terdaftar bisa langsung memakai semua fitur, dan **berlangganan adalah peningkatan opsional, bukan keharusan** — ikuti alur di file ini hanya bila pengguna sendiri ingin keanggotaan. Ketika masa uji coba berakhir, akun tanpa langganan yang mengunjungi halaman konten akan dialihkan ke halaman langganan; cukup selesaikan langganannya sesuai file ini.""",
    RF_STATE="""## Alur Status Setelah Pendaftaran Berhasil

> **Masa uji coba gratis (mulai 2026-10-18; perilaku aktual platform yang berlaku)**: akun yang baru terdaftar bisa **langsung memakai semua fitur**
> (feed, peta, manusia digital, check-in, dll.) tanpa perlu bayar; akun tanpa langganan tidak lagi dipisahkan dari halaman konten. \"Pencegahan pending\"
> yang dijelaskan di bagian ini adalah status normal setelah masa uji coba berakhir — saat itu tiba, perilaku aktual daring yang berlaku.

1. Pengguna disimpan dengan `accountStatus: 'pending'` dan **3 lencana awal** (rute register).
2. Server juga menanam dua cookie HttpOnly: JWT (bisa langsung mengakses halaman) dan pendingUserToken (kredensial identitas untuk alur langganan).
3. Pada status normal (masa uji coba berakhir / tidak ada masa gratis), halaman pendaftaran mendeteksi `pending_payment` → dialihkan ke `/subscription`
   (dengan mempertahankan parameter kembali `next`); pada mode perantara agent, `me?token=…&redirect=/subscription` memberi efek yang sama.
   **Selama masa uji coba gratis langkah ini tidak terpicu** — setelah mendaftar, langsung menuju beranda dan mulai pakai.
4. Pembayaran selesai → `accountStatus` menjadi `active` (**Alipay mengaktifkan otomatis di sisi server melalui notify**;
   PayPal mengaktifkan melalui Webhook; kode QR WeChat dikonfirmasi manual; Huawei IAP lewat `activate-huawei`).
   Detailnya ada di `payment-and-activation.md`.

Pada status normal, akun tidak aktif (pending) yang memanggil API inti (feed, peta, chat manusia digital, check-in, dll.) mendapat 403;
pengecualiannya link posting yang dibagikan (tetap bisa diakses publik). Selama masa uji coba gratis pencegahan ini ditangguhkan dan semuanya terbuka.""",
    RF_ROW_403="| Terdaftar berhasil tapi login mengembalikan 403 \"请完成订阅以激活账户\" | Akun masih pending, dan platform tidak sedang dalam masa uji coba gratis (status yang diharapkan sebelum bayar) | Selama masa uji coba gratis tidak akan terjadi; jika terjadi berarti masa uji coba telah berakhir — selesaikan langganan dulu; jika setelah bayar masih 403 berarti memakai JWT lama — pada mode skrip jalankan `refresh-login` dulu untuk menukar dengan status login terbaru |",
    RF_ROW_LAND="| Pengguna mengklik link login tapi mendarat di halaman langganan (bukan beranda) | Masa uji coba gratis telah berakhir dan paywall platform kembali | Ikuti alur langganan dari langkah 7 di SKILL.md; setelah berlangganan, jalankan `refresh-login` lalu kirim link beranda |",
    RD_VER="""**Sejak v2.0.0 ini mode perantara agent, dan sejak v2.2.0 juga menyesuaikan diri dengan masa uji coba gratis platform**: skrip inti `scripts/powpow-register.mjs` tanpa dependensi
(Node ≥ 18); pengguna hanya meninggalkan percakapan satu kali: untuk memeriksa kode verifikasi di kotak masuk. Selama masa uji coba gratis saat ini, akun yang sudah terdaftar langsung bisa memakai semua fitur — pembayaran langganan opsional; jika masa uji coba berakhir dan pengguna mendarat di halaman langganan, alur otomatis beralih ke jalur pembayaran. Tanpa Node, atau bila pengguna lebih suka melakukannya sendiri, otomatis beralih ke mode panduan murni.""",
    RD_LINK="""3. **Login sekali klik (dua link)**: tepat setelah pendaftaran berhasil, link login membawa pengguna langsung ke beranda (selama masa uji coba gratis, sekali klik langsung bisa dipakai);
   jika mendarat di halaman langganan (masa uji coba berakhir) atau pengguna ingin meningkatkan, ikuti alur langganan — setelah dana masuk, status login terbaru ditukar dan link keanggotaan penuh membawa ke beranda
   (melalui jembatan resmi platform `me?token=`, yang otomatis menanam cookie HttpOnly).""",
    LISTING_NOTE="ClawHub 上架表单填写用。v2.0.0 起为 agent 代办型：脚本代办发码/注册/下单（零依赖 Node>=18），用户只需收一次验证码；无 Node 环境自动回退纯指引模式。v2.2.0（2026-10-18）起适配平台免费测试期：注册后一键登录即可使用，订阅支付改为可选升级，用户落地订阅页时流程自动转支付路径。",
)
