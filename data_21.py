# -*- coding: utf-8 -*-
JV = dict(
    DESC=[
        ("aktivasi langganan liwat Alipay", "aktivasi langganan liwat Alipay/PayPal"),
        ("mbayar ing kasir Alipay", "mbayar ing kasir Alipay/PayPal"),
    ],
    INTRO=("**mbayar ing kasir Alipay** (agen bakal mbukak kaca kasir kanthi otomatis).",
           "**mbayar ing kasir bayaran** (Alipay utawa PayPal — agen bakal mbukak kaca kasir kanthi otomatis)."),
    VLINE=[
        ("**Versi 2.0.1** · 2026-10-08", "**Versi 2.1.0** · 2026-10-11"),
        ("Wiwit v2.0.1 tangkapan layar produk dikemas bebarengan skill ing `assets/screenshots/`, ora manunggung layanan gambar njaba)",
         "Wiwit v2.1.0 langganan PayPal uga bisa ditangani agen, dadi pilihan bebarengan Alipay)"),
    ],
    STEP6="""2. **Ajak panganggo milih cara bayar** — tuduhake saluran loro-lorone:
   - **Alipay (ing njero China / panganggo sing duwe Alipay)**: tuku sepisan kanggo durasi sing cocog, **ora langganan otomatis**
     - Wulanan **¥6.99** (disaranake nyoba dhisik) / Kuartalan **¥19.99** / Taunan **¥69.99**
   - **PayPal (luar negeri / panganggo tanpa Alipay)**: langganan otomatis saben wulan, bisa dibatalake kapan wae
     - Premium Monthly, kira-kira **$1/sasi** (kaya sing dituduhake ing kaca langganan; langganan otomatis)
3. Sawise panganggo milih salah siji:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Skrip bali path berkas kaca bayaran, **mbukak langsung nganggo printah sistem** (Windows: `start <berkas>`; macOS: `open <berkas>`; Linux: `xdg-open <berkas>`). Browser otomatis mlumpat menyang kasir resmi Alipay/PayPal, panganggo ngrampungake bayaran utawa ijin tagihan.
4. Saben 10–15 detik jalanke `query` nganti bali `paid` utawa `ACTIVE` (dhuwit/ijin lumebu umume sawetara detik nganti siji menit). Panganggo nutup kaca bayaran ing tengah dalan → langsung jalanke maneh `create-order` (pesanan lawas / langganan PENDING ditutup utawa kadaluwarsa sawise 2 jam, ora usah diatur).
5. Saluran pindai kode WeChat dikonfirmasi manual, tekan dhuwit bisa telat; Huawei IAP mung kasedhiya ing njero app HarmonyOS. Skill ora nangani loro-lorone — sawise mbayar padha bali nglakoni langkah 7.
""",
    BOUNDARY=("akun Alipay/bukti bayaran panganggo", "akun Alipay/PayPal/bukti bayaran panganggo"),
    PA_CONCL="""**Saluran Alipay lan PayPal saiki loro-lorone bisa ditangani agen — kalebu nggawe pesanan lan ngawasi tekan dhuwit.**
Alipay tuku sepisan ora langganan otomatis, kanggo panganggo ing China lan sing duwe Alipay; PayPal langganan otomatis saben wulan lan bisa dibatalake kapan wae,
kanggo panganggo luar negeri lan sing ora duwe Alipay. Pindai kode WeChat (konfirmasi manual) lan Huawei IAP isih ana, nanging ora ditangani skill.""",
    PA_RESP=[
        ("nyentuh akun Alipay", "nyentuh akun Alipay/PayPal"),
        ("Tumindak mbayar tansah ditindakake panganggo dhewe ing kasir resmi Alipay.",
         "Tumindak mbayar tansah ditindakake panganggo dhewe ing kasir resmi."),
    ],
    PA_FRESH=("sawise konfirmasi `paid` dhisik jalanke `refresh-login`",
              "sawise konfirmasi `paid` / PayPal `ACTIVE` dhisik jalanke `refresh-login`"),
    PA_PAYPAL="""## Saluran langganan PayPal (ditangani agen; web, dudu HarmonyOS)

Mung ana siji rencana, Premium Monthly (kira-kira $1/sasi, kaya sing dibalekake `/api/subscription/plans`); **langganan otomatis saben wulan**
lan panganggo bisa mbatalake kapan wae ing akun PayPal-e.

### Kontrak API (wis dibungkus skrip skill; agen aja ngrakit panjalukan dhewe)

| Titik pungkasan | Metode | Cathetan |
|---|---|---|
| `/api/subscription/plans` | GET | Otentikasi Bearer; mbalekake pratelan rencana sing kasedhiya (saiki mung 1) |
| `/api/subscription/create` | POST | Isi `{planId}` → mbalekake `{subscriptionId, approveUrl, status}`; `status` lumrahe `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Otentikasi Bearer; mbalekake `{activeSubscription, allSubscriptions}`; agen mriksa `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | Dicekel kaca sukses kanthi otomatis (karo cookie); ngaktifake liwat API PayPal langsung yen webhook durung tekan |
| `/subscription/success` | Kaca bali browser | Kaca pendaratan sawise ijin PayPal; otomatis polling verify, banjur bali menyang kaca ngarep / kaca asli |
| `/subscription/cancel` | Kaca browser | Kaca pendaratan yen panganggo mbatalake utawa gagal; bisa miwiti pacoban anyar |

### Alur agen

```
create-order --provider paypal   # → mbalekake approveUrl, ditulis menyang berkas HTML lokal
open the HTML file               # → browser mlumpat menyang kaca ijin PayPal
query (saben 10–15 detik)        # → polling nganti ACTIVE
refresh-login                    # → njupuk JWT anyar (klaim langganan ACTIVE)
login-link --target home         # → nggawe tautan mlebu resmi
```

- Langganan PENDING sing ora rampung sajrone 1 jam diresiki backend kanthi otomatis; wiwiti maneh wae.
- Yen panganggo njalanke `create-order` maneh, backend bakal nganggo maneh langganan `APPROVAL_PENDING` sing isih sah, supaya ora 409.
- Padha karo Alipay: tekan dhuwit mung nganyari DB — JWT lawas ora dianyari otomatis, mula **kudu** jalanke `refresh-login` sadurunge ngirim tautan kaca ngarep.""",
    PA_ROWS="""| PayPal `query` tetep PENDING | Panganggo durung ngrampungake ijin ing PayPal; priksa apa tautan ijin wis dibukak ing browser. Yen isih PENDING sawise ijin, webhook bisa telat — ajak panganggo ngenteni sawetara detik ing kaca sukses utawa refresh |
| PayPal `query` mbalekake 409 | Ana langganan PENDING sing durung rampung; enteni 1 jam nganti kadaluwarsa, utawa rampungake ijin tautan lawas ing browser |
| PayPal wis mbayar, tautan 2 isih diblokir | Padha karo Alipay: dhisik `refresh-login` banjur `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (gawan Alipay)<br>`--provider alipay\\|paypal` | Nggawe pesanan bayaran; Alipay mbalekake path berkas kaca bayaran + outTradeNo; PayPal mbalekake path berkas kaca ijin + subscriptionId (otomatis dicathet ing berkas status) |",
    AF_ROW_QUERY="| `query` | —— | Ndeleng status pesanan/langganan. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; polling 10–15 detik |",
    AF_SEQ7="""7.  (panganggo milih cara bayar)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("    # → panganggo mbayar ing kasir Alipay (bagean metu obrolan②)",
             "    # → panganggo ngrampungake bayaran/ijin ing kasir Alipay/PayPal (bagean metu obrolan②)"),
    AF_SEQ9=("9.  query (saben 10–15 detik) nganti paid",
             "9.  query (saben 10–15 detik) nganti paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| Sawise `create-order` panganggo nutup kaca bayaran | Langsung jalanke maneh `create-order` (pesanan lawas otomatis ditutup sawise 2 jam) |",
                  "| Sawise `create-order` panganggo nutup kaca bayaran | Langsung jalanke maneh `create-order` (pesanan lawas otomatis ditutup sawise 2 jam; langganan PayPal PENDING kadaluwarsa sawise 1 jam) |"),
    AF_ERR_409="| `create-order --provider paypal` mbalekake 409 | Ana langganan PayPal sing durung rampung; enteni 1 jam nganti kadaluwarsa, utawa rampungake ijin lawas ing browser |",
    AF_ERR_PEND=("| `query` tansah pending | Panganggo mbokmenawa durung mbayar; takona sepisan. Yen pancen wis mbayar → tindakake tabel diagnostik payment-and-activation.md |",
                 "| `query` tansah pending / PENDING | Panganggo mbokmenawa durung mbayar; takona sepisan. Yen pancen wis mbayar → tindakake tabel diagnostik payment-and-activation.md |"),
    AF_ERR_403=("Bayaran durung tekan,", "Bayaran/ijin durung tekan,"),
    RD=[
        ("pesanan langganan Alipay lan ngawasi tekan dhuwit",
         "pesanan langganan Alipay/PayPal lan ngawasi tekan dhuwit"),
        ("**Wiwit v2.0.0 nganggo mode agen-ditindakake**",
         "**Wiwit v2.0.0 nganggo mode agen-ditindakake, lan wiwit v2.1.0 PayPal uga bisa ditangani**"),
        ("mbayar ing kasir Alipay. Yen ora ana Node", "mbayar ing kasir Alipay/PayPal. Yen ora ana Node"),
        ("4. **Langganan bayaran**: saluran Alipay agen njalukake pesanan (wulan ¥6.99 / kuartal ¥19.99 / taunan ¥69.99, tuku langsung ora langganan otomatis) + polling tekan dhuwit; panganggo luar negeri bali menyang PayPal; pindai kode WeChat / Huawei IAP mung tuduhake dalan.",
         "4. **Langganan bayaran**: Alipay (wulan ¥6.99 / kuartal ¥19.99 / taunan ¥69.99, tuku langsung ora langganan otomatis) lan PayPal (Premium Monthly, kira-kira $1/sasi, langganan otomatis, bisa dibatalake kapan wae) loro-lorone ditangani agen nganggo nggawe pesanan + polling tekan dhuwit; pindai kode WeChat / Huawei IAP mung tuduhake dalan."),
        ("aja tau nyentuh akun Alipay utawa bukti bayaran panganggo, aja tau mbayarke. Bayaran tansah dumadi antarane panganggo lan kasir resmi Alipay.",
         "aja tau nyentuh akun Alipay/PayPal utawa bukti bayaran panganggo, aja tau mbayarke. Bayaran tansah dumadi antarane panganggo lan kasir resmi."),
    ],
)
