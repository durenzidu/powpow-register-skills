# -*- coding: utf-8 -*-
BHO = dict(
    DESC=[
        ("Alipay से सदस्यता चालू करावे आ एक क्लिक लॉगिन करावे",
         "Alipay/PayPal से सदस्यता चालू करावे आ एक क्लिक लॉगिन करावे"),
        ("Alipay कैशियर पर पैसा देला", "Alipay/PayPal कैशियर पर पैसा देला"),
    ],
    INTRO=("**Alipay कैशियर पर पैसा देवे** (agent खुदे कैशियर के पेज खोल देला)।",
           "**पेमेंट कैशियर पर पैसा देवे** (Alipay या PayPal — agent खुदे कैशियर के पेज खोल देला)।"),
    VLINE=[
        ("**वर्जन 2.0.1** · 2026-10-08", "**वर्जन 2.1.0** · 2026-10-11"),
        ("v2.0.1 से प्रोडक्ट स्क्रीनशॉट skill के साथे `assets/screenshots/` में बंदल बा, बाहरी इमेज-होस्ट पर निर्भर नईखे)",
         "v2.1.0 से PayPal सदस्यता भी agent संभाल सकत बा, Alipay के साथे विकल्प के रूप में)"),
    ],
    STEP6="""2. **यूज़र से पेमेंट के तरीका चुनवाईं** — दुनो रास्ता देखाईं:
   - **Alipay (चीन के भीतर / Alipay वाला यूज़र)**: मिलत-जुलत अवधि खातिर एक बेर के खरीद, **अपने-आप रिन्यू नई होला**
     - मासिक **¥6.99** (आजमावे लायक सुझाव) / त्रैमासिक **¥19.99** / वार्षिक **¥69.99**
   - **PayPal (विदेश / Alipay ना होखे वाला यूज़र)**: हर महीना अपने-आप रिन्यू, कबो भी रद्द कइल जा सकत बा
     - Premium Monthly, करीब **$1/महीना** (सदस्यता पेज पर जइसन देखाई; अपने-आप रिन्यू होला)
3. यूज़र एक गो चुन लिहला पर:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   स्क्रिप्ट पेमेंट पेज फाइल के पाथ देला, **सिस्टम कमांड से सीधे खोलीं** (Windows: `start <फाइल>`; macOS: `open <फाइल>`; Linux: `xdg-open <फाइल>`)। ब्राउज़र अपने-आप Alipay/PayPal के आधिकारिक कैशियर पर चल जाई, यूज़र पैसा देला या बिलिंग के अनुमति दिहलस।
4. हर 10–15 सेकंड में `query` चलाईं जब ले `paid` या `ACTIVE` लवटे (पैसा/अनुमति आमतौर पर कुछ सेकंड से एक मिनट में जमा हो जाला)। बीच में यूज़र पेमेंट पेज बंद कइ दिहलस → सीधे फेर `create-order` (पुरान ऑर्डर / PENDING सदस्यता 2 घंटा में अपने-आप बंद या खतम हो जाई, ओके छोड़ दीं)।
5. WeChat QR रास्ता मैनुअल पुष्टि वाला बा, पैसा जमा होए में देरी लग सकत बा; Huawei IAP खाली HarmonyOS ऐप के भीतर मिलेला। skill ई दुनो ना संभाली — पैसा दिहला के बाद ओही तरह कदम 7 पर आईं।
""",
    BOUNDARY=("Alipay खाता/पेमेंट क्रेडेंशियल", "Alipay/PayPal खाता/पेमेंट क्रेडेंशियल"),
    PA_CONCL="""**Alipay आ PayPal दुनो सदस्यता अब agent संभाल सकत बा — ऑर्डर बनावल आ पैसा जमा देखरेख सहित।**
Alipay एक बेर के खरीद बा, अपने-आप रिन्यू नई होला, चीन के यूज़र आ Alipay वाला यूज़र खातिर; PayPal हर महीना अपने-आप रिन्यू होला आ कबो भी रद्द कइल जा सकत बा,
विदेशी यूज़र आ Alipay ना होखे वाला यूज़र खातिर। WeChat QR (मैनुअल पुष्टि) आ Huawei IAP भी बाने, पर skill ई ना संभाली।""",
    PA_RESP=[
        ("यूज़र के Alipay", "यूज़र के Alipay/PayPal"),
        ("पैसा देवे के काम सदा यूज़र खुदे Alipay आधिकारिक कैशियर पर करेला।",
         "पैसा देवे के काम सदा यूज़र खुदे आधिकारिक कैशियर पर करेला।"),
    ],
    PA_FRESH=("`paid` पक्का भइला पर पहिले `refresh-login`",
              "`paid` / PayPal `ACTIVE` पक्का भइला पर पहिले `refresh-login`"),
    PA_PAYPAL="""## PayPal सदस्यता रास्ता (agent संभालेला; वेब, HarmonyOS ना)

एके गो प्लान बा, Premium Monthly (करीब $1/महीना, `/api/subscription/plans` जइसन लवटावेला); ई **हर महीना अपने-आप रिन्यू होला**
आ यूज़र अपना PayPal खाता में कबो भी एके रद्द कर सकत बा।

### API कॉन्ट्रैक्ट (skill स्क्रिप्ट में पहिले से बंदल बा; agent कबो खुद रिक्वेस्ट ना जोड़े)

| एंडपॉइंट | तरीका | टिप्पणी |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer auth; उपलब्ध प्लान के लिस्ट लवटावेला (अभी खाली 1 गो) |
| `/api/subscription/create` | POST | बॉडी `{planId}` → `{subscriptionId, approveUrl, status}` लवटावेला; `status` आमतौर पर `APPROVAL_PENDING` होला |
| `/api/subscription/create` | GET | Bearer auth; `{activeSubscription, allSubscriptions}` लवटावेला; agent `activeSubscription.subscription.status === 'ACTIVE'` पूछेला |
| `/api/subscription/verify` | POST | सक्सेस पेज (कुकी सहित) अपने-आप बोलावेला; webhook ना पहुँचला पर PayPal API से सीधे एक्टिवेट कर देला |
| `/subscription/success` | ब्राउज़र वापसी पेज | PayPal अनुमति के बाद के लैंडिंग पेज; verify अपने-आप पूछेला, फिर होमपेज / मूल पेज पर लौटावेला |
| `/subscription/cancel` | ब्राउज़र पेज | यूज़र रद्द करे या फेल होए पर के लैंडिंग पेज; नया कोशिश कइल जा सकत बा |

### Agent के फ्लो

```
create-order --provider paypal   # → approveUrl लवटावेला, लोकल HTML फाइल में लिखल जाला
open the HTML file               # → ब्राउज़र PayPal अनुमति पेज पर जाला
query (हर 10–15s)                # → ACTIVE होए ले पूछीं
refresh-login                    # → नवा JWT बदलीं (सदस्यता के वादा ACTIVE)
login-link --target home         # → पक्का लॉगिन लिंक बनावेला
```

- 1 घंटा में ना पूरा भइल PENDING सदस्यता बैकएंड अपने-आप साफ कर देला; फेर से शुरू करीं।
- यूज़र फेर `create-order` चलावे त, बैकएंड अबहीं चलत `APPROVAL_PENDING` सदस्यता दोबारा इस्तेमाल करेला, 409 से बचावेला।
- Alipay जइसन: पैसा जमा होए से खाली DB अपडेट होला — पुरान JWT अपने-आप ताजा नई होला, एही से होमपेज लिंक भेजे से पहिले `refresh-login` चलावे के **पड़ी**।""",
    PA_ROWS="""| PayPal `query` PENDING रह गइल | यूज़र PayPal में अनुमति पूरा नईखे कइलस; जाँचीं अनुमति लिंक ब्राउज़र में खुलल रहे। अनुमति के बाद भी PENDING रहे त webhook देरी भइल हो सकत बा — यूज़र के सक्सेस पेज पर कुछ सेकंड रुके या ताजा करे दीं |
| PayPal `query` 409 लवटावेला | एक गो अधूरा PENDING सदस्यता बा; 1 घंटा रुकीं जब ले खतम हो जाय, या पुरान लिंक के अनुमति ब्राउज़र में पूरा करीं |
| PayPal से पैसा दिहल, लिंक 2 पर अबहीं रोकल जात बा | Alipay जइसन: पहिले `refresh-login` फिर `login-link` |""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay डिफ़ॉल्ट)<br>`--provider alipay\\|paypal` | पेमेंट ऑर्डर बनावे; Alipay पेमेंट पेज फाइल पाथ + outTradeNo लवटावे; PayPal अनुमति पेज फाइल पाथ + subscriptionId लवटावे (अपने-आप स्टेट फाइल में दर्ज) |",
    AF_ROW_QUERY="| `query` | —— | ऑर्डर/सदस्यता हालत पूछे। Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; 10–15s में पूछीं |",
    AF_SEQ7="""7.  (यूज़र पेमेंट के तरीका चुने)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("    # → यूज़र Alipay कैशियर पर पैसा देवे (गप्पा छोड़े के जगह②)",
             "    # → यूज़र Alipay/PayPal कैशियर पर पैसा/अनुमति पूरा करे (गप्पा छोड़े के जगह②)"),
    AF_SEQ9=("9.  query (हर 10–15s) जब ले paid", "9.  query (हर 10–15s) जब ले paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| `create-order` के बाद यूज़र पेमेंट पेज बंद कइ दिहलस | सीधे फेर `create-order` (पुरान ऑर्डर 2 घंटा में अपने-आप बंद हो जाई) |",
                  "| `create-order` के बाद यूज़र पेमेंट पेज बंद कइ दिहलस | सीधे फेर `create-order` (पुरान ऑर्डर 2 घंटा में अपने-आप बंद हो जाई; PayPal PENDING सदस्यता 1 घंटा में खतम) |"),
    AF_ERR_409="| `create-order --provider paypal` 409 लवटावेला | एक गो अधूरा PayPal सदस्यता बा; 1 घंटा रुकीं जब ले खतम हो जाय, या पुरान अनुमति ब्राउज़र में पूरा करीं |",
    AF_ERR_PEND=("| `query` लगातार pending | शायद यूज़र पैसा ना दिहलस; एक शब्द पूछीं। असल में दिहलस → payment-and-activation.md के पड़ताल टेबल अपनाईं |",
                 "| `query` लगातार pending / PENDING | शायद यूज़र पैसा ना दिहलस; एक शब्द पूछीं। असल में दिहलस → payment-and-activation.md के पड़ताल टेबल अपनाईं |"),
    AF_ERR_403=("पैसा अभी जमा ना भइल,", "पैसा/अनुमति अभी जमा ना भइल,"),
    RD=[
        ("Alipay सदस्यता ऑर्डर बनावल आ पैसा जमा देखरेख",
         "Alipay/PayPal सदस्यता ऑर्डर बनावल आ पैसा जमा देखरेख"),
        ("**v2.0.0 से ई agent-सहायता मोड बा**",
         "**v2.0.0 से ई agent-सहायता मोड बा, आ v2.1.0 से PayPal भी संभालल जा सकत बा**"),
        ("Alipay कैशियर पर पैसा देवे। Node ना बा", "Alipay/PayPal कैशियर पर पैसा देवे। Node ना बा"),
        ("4. **सदस्यता पेमेंट**: Alipay रास्ता में agent ऑर्डर बनावेला (मासिक ¥6.99 / त्रैमासिक ¥19.99 / वार्षिक ¥69.99, एक बेर के खरीद, अपने-आप रिन्यू नई) + जमा देखरेख; विदेशी यूज़र खातिर PayPal; WeChat QR/Huawei IAP खातिर रास्ता दिखावल।",
         "4. **सदस्यता पेमेंट**: Alipay (मासिक ¥6.99 / त्रैमासिक ¥19.99 / वार्षिक ¥69.99, एक बेर के खरीद, अपने-आप रिन्यू नई) आ PayPal (Premium Monthly, करीब $1/महीना, अपने-आप रिन्यू, कबो भी रद्द) दुनो में agent ऑर्डर बनावेला + जमा देखरेख; WeChat QR/Huawei IAP खातिर रास्ता दिखावल।"),
        ("यूज़र के Alipay खाता या पेमेंट क्रेडेंशियल कभो ना छुवे, कभो ऊसर से पैसा ना देवे। पैसा सदा यूज़र आ Alipay आधिकारिक कैशियर के बीचे दिहल जाला।",
         "यूज़र के Alipay/PayPal खाता या पेमेंट क्रेडेंशियल कभो ना छुवे, कभो ऊसर से पैसा ना देवे। पैसा सदा यूज़र आ आधिकारिक कैशियर के बीचे दिहल जाला।"),
    ],
)
