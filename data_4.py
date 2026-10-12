# -*- coding: utf-8 -*-
ID = dict(
    DESC=[
        ("mengaktifkan langganan lewat Alipay,", "mengaktifkan langganan lewat Alipay/PayPal,"),
        ("membayar di halaman kasir Alipay ", "membayar di halaman kasir Alipay/PayPal "),
    ],
    INTRO=("**membayar di halaman kasir Alipay** (agent akan membuka halaman pembayarannya sendiri).",
           "**membayar di halaman kasir pembayaran** (Alipay atau PayPal — agent akan membuka halaman pembayarannya sendiri)."),
    VLINE=[
        ("**Versi 2.0.1** · 2026-10-08", "**Versi 2.1.0** · 2026-10-11"),
        ("Sejak v2.0.1 tangkapan layar produk dibundel bersama skill di `assets/screenshots/`, tidak bergantung pada layanan hosting gambar eksternal",
         "Sejak v2.1.0 langganan PayPal juga bisa dikerjakan agent, sebagai pilihan sejajar Alipay"),
    ],
    STEP6="""2. **Minta pengguna memilih metode pembayaran** — tampilkan kedua kanal:
   - **Alipay (daratan Tiongkok / pengguna punya Alipay)**: beli putus sekali untuk masa berlaku yang bersangkutan, **tanpa perpanjangan otomatis**
     - Bulanan **¥6.99** (disarankan saat baru mencoba) / Triwulan **¥19.99** / Tahunan **¥69.99**
   - **PayPal (luar negeri / tanpa Alipay)**: perpanjangan otomatis bulanan, bisa dibatalkan kapan saja
     - Premium Monthly, sekitar **$1/bulan** (sesuai yang tampil di halaman langganan; perpanjangan otomatis)
3. Setelah pengguna memilih salah satu:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Skrip mengembalikan path file halaman pembayaran; **buka langsung dengan perintah sistem** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Browser melompat sendiri ke kasir resmi Alipay/PayPal; pengguna menyelesaikan pembayaran atau otorisasi penagihan di sana.
4. Jalankan `query` setiap 10–15 detik sampai mengembalikan `paid` atau `ACTIVE` (dana/otorisasi masuk biasanya beberapa detik sampai satu menit). Pengguna menutup halaman pembayaran di tengah jalan → langsung jalankan `create-order` lagi (pesanan lama / langganan pending tertutup atau kedaluwarsa otomatis dalam 2 jam, tak perlu dipikirkan).
5. Kanal pindai QR WeChat perlu konfirmasi manual dan dananya bisa masuk lambat; Huawei IAP hanya tersedia di dalam App HarmonyOS. Skill tidak menangani keduanya — setelah pembayaran selesai tetap kembali ke langkah 7 seperti biasa.
""",
    BOUNDARY=("menyentuh akun Alipay/bukti pembayaran", "menyentuh akun Alipay/PayPal/bukti pembayaran"),
    PA_CONCL_N=4,
    PA_CONCL="""**Kanal Alipay dan PayPal sekarang bisa dikerjakan agent — termasuk pembuatan pesanan dan pelacakan dana masuk.**
Alipay beli putus sekali tanpa perpanjangan otomatis, untuk pengguna daratan Tiongkok dan pengguna yang punya Alipay;
PayPal perpanjangan otomatis bulanan dan bisa dibatalkan kapan saja, untuk pengguna luar negeri dan tanpa Alipay.
Pindai QR WeChat (konfirmasi manual) dan Huawei IAP tetap tersedia, tapi tidak dikerjakan skill.""",
    PA_RESP=[
        ("menyentuh akun Alipay/bukti pembayaran pengguna", "menyentuh akun Alipay/PayPal/bukti pembayaran pengguna"),
        ("Aksi membayar selalu diselesaikan oleh pengguna sendiri di kasir resmi Alipay.",
         "Aksi membayar selalu diselesaikan oleh pengguna sendiri di kasir resmi."),
    ],
    PA_FRESH=("Karena itu setelah `paid` terkonfirmasi skill", "Karena itu setelah `paid` / PayPal `ACTIVE` terkonfirmasi skill"),
    PA_PAYPAL="""## Kanal Langganan PayPal (dikerjakan skill; web, non-HarmonyOS)

Hanya ada satu paket, Premium Monthly (sekitar $1/bulan, sesuai yang dikembalikan `/api/subscription/plans`); **perpanjangan otomatis bulanan**
dan pengguna bisa membatalkannya kapan saja di akun PayPal-nya.

### Kontrak API (sudah dibungkus skrip skill; agent tidak pernah merakit request sendiri)

| Endpoint | Metode | Catatan |
|---|---|---|
| `/api/subscription/plans` | GET | Butuh Bearer; mengembalikan daftar paket yang tersedia (saat ini hanya 1) |
| `/api/subscription/create` | POST | body `{planId}` → mengembalikan `{subscriptionId, approveUrl, status}`; `status` biasanya `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Butuh Bearer; mengembalikan `{activeSubscription, allSubscriptions}`; agent mem-poll `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Dipanggil otomatis oleh halaman sukses (membawa cookie); mengaktifkan lewat API PayPal langsung saat webhook belum datang |
| `/subscription/success` | Halaman balik browser | Halaman mendarat setelah otorisasi PayPal; mem-poll verify otomatis, lalu kembali ke beranda / halaman asal |
| `/subscription/cancel` | Halaman browser | Halaman mendarat saat pengguna membatalkan atau gagal; bisa mulai ulang |

### Alur agent

```
create-order --provider paypal   # → mengembalikan approveUrl, ditulis ke file HTML lokal
buka file HTML                   # → browser melompat ke halaman otorisasi PayPal
query (tiap 10–15 dtk)           # → poll sampai ACTIVE
refresh-login                    # → tukar JWT baru (klaim langganan ACTIVE)
login-link --target home         # → hasilkan tautan login resmi
```

- Langganan PENDING yang tidak selesai dalam 1 jam dibersihkan otomatis oleh backend; mulai ulang saja.
- Jika pengguna menjalankan `create-order` lagi, backend memakai ulang langganan `APPROVAL_PENDING` yang masih berlaku, sehingga menghindari 409.
- Sama seperti Alipay: dana masuk hanya memperbarui DB — JWT lama tidak diperbarui otomatis, jadi **wajib** menjalankan `refresh-login` sebelum mengirim tautan beranda.""",
    PA_ROWS="""| `query` PayPal terus PENDING | Pengguna belum menyelesaikan otorisasi di PayPal; pastikan tautan otorisasi sudah terbuka di browser. Bila setelah otorisasi masih PENDING, webhook mungkin tertunda — suruh pengguna menunggu beberapa detik lagi di halaman sukses atau menyegarkannya |
| `query` PayPal mengembalikan 409 | Sudah ada langganan PENDING yang belum selesai; tunggu 1 jam sampai kedaluwarsa, atau selesaikan otorisasi tautan lama di browser |
| PayPal sudah dibayar tapi tautan 2 tetap ditahan | Sama seperti Alipay: jalankan `refresh-login` lebih dulu, baru `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (bawaan Alipay)<br>`--provider alipay\\|paypal` | Membuat pesanan pembayaran; Alipay mengembalikan path file halaman pembayaran + outTradeNo; PayPal mengembalikan path file halaman otorisasi + subscriptionId (otomatis dicatat ke file status) |",
    AF_ROW_QUERY="| `query` | —— | Memeriksa status pesanan/langganan. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; polling tiap 10–15 dtk |",
    AF_SEQ7="""7.  (pengguna memilih metode pembayaran)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("# → pengguna membayar di kasir Alipay (keluar dari percakapan ②)",
             "# → pengguna menyelesaikan pembayaran/otorisasi di kasir Alipay/PayPal (keluar dari percakapan ②)"),
    AF_SEQ9=("9.  query (tiap 10–15 dtk) sampai paid", "9.  query (tiap 10–15 dtk) sampai paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Setelah `create-order` pengguna menutup halaman pembayaran | Langsung `create-order` ulang (pesanan lama tertutup otomatis 2 jam) |",
                  "| Setelah `create-order` pengguna menutup halaman pembayaran | Langsung `create-order` ulang (pesanan lama tertutup otomatis 2 jam; langganan PENDING PayPal kedaluwarsa setelah 1 jam) |"),
    AF_ERR_409="| `create-order --provider paypal` mengembalikan 409 | Sudah ada langganan PayPal yang belum selesai; tunggu 1 jam sampai kedaluwarsa, atau selesaikan otorisasi lama di browser |",
    AF_ERR_PEND=("| `query` terus pending | Pengguna mungkin belum membayar; tanyakan sekali. Kalau sudah bayar → ikuti tabel penelusuran di payment-and-activation.md |",
                 "| `query` terus pending / PENDING | Pengguna mungkin belum membayar; tanyakan sekali. Kalau sudah bayar → ikuti tabel penelusuran di payment-and-activation.md |"),
    AF_ERR_403=("| Dana belum masuk, kembali ke langkah 9 lanjut polling |",
                "| Dana/otorisasi belum masuk, kembali ke langkah 9 lanjut polling |"),
    RD=[
        ("pesanan dan pemantauan langganan\nAlipay, login sekali klik",
         "pesanan dan pemantauan langganan\nAlipay/PayPal, login sekali klik"),
        ("**Sejak v2.0.0 adalah mode agent yang bertindak atas nama**",
         "**Sejak v2.0.0 adalah mode agent yang bertindak atas nama, dan sejak v2.1.0 PayPal juga bisa dikerjakan**"),
        ("membayar di kasir Alipay. Tanpa Node", "membayar di kasir Alipay/PayPal. Tanpa Node"),
        ("4. **Pembayaran langganan**: kanal Alipay dengan pesanan yang dikerjakan agent (bulanan ¥6.99 / triwulan ¥19.99 /\n   tahunan ¥69.99, beli putus sekali tanpa perpanjangan otomatis) + polling dana masuk; pengguna luar negeri\n   mundur ke PayPal; pindai WeChat/Huawei IAP hanya ditunjukkan jalannya.",
         "4. **Pembayaran langganan**: baik Alipay (bulanan ¥6.99 / triwulan ¥19.99 /\n   tahunan ¥69.99, beli putus sekali tanpa perpanjangan otomatis) maupun PayPal (Premium Monthly, sekitar $1/bulan,\n   perpanjangan otomatis, bisa dibatalkan kapan saja) dikerjakan agent dengan pembuatan pesanan + polling dana masuk;\n   pindai QR WeChat/Huawei IAP hanya ditunjukkan jalannya."),
        ("  Alipay atau bukti pembayaran pengguna, tidak pernah membayarkan. Pembayaran selalu terjadi antara pengguna dan\n  kasir resmi Alipay.",
         "  Alipay/PayPal atau bukti pembayaran pengguna, tidak pernah membayarkan. Pembayaran selalu terjadi antara pengguna dan\n  kasir resmi."),
    ],
)
