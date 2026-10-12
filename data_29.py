# -*- coding: utf-8 -*-
PNB = dict(
    DESC=[
        ("Alipay سبسکرپشن نال ایکٹویٹ کرنا", "Alipay/PayPal سبسکرپشن نال ایکٹویٹ کرنا"),
        ("Alipay کیشیئر تے ادا کردا اے", "Alipay/PayPal کیشیئر تے ادا کردا اے"),
    ],
    INTRO=("**Alipay کیشیئر تے پیسے ادا کرنا** (ایجنٹ کیشیئر دا صفہہ خود کھولھ دیندا اے)",
           "**پیمنٹ کیشیئر تے پیسے ادا کرنا** (Alipay یا PayPal — ایجنٹ کیشیئر دا صفہہ خود کھولھ دیندا اے)"),
    VLINE=[
        ("**Version 2.0.1** · 2026-10-08", "**Version 2.1.0** · 2026-10-11"),
        ("v2.0.1 توں مصنوعات دیاں سکرین شاٹاں skill نال `assets/screenshots/` وچ پیک نیں، باہری تصویر ہوسٹنگ تے انحصار نہیں",
         "v2.1.0 توں PayPal سبسکرپشن وی agent کر سکدا اے، Alipay نال متوازی چوائس"),
    ],
    STEP6="""2. **صارف نوں ادائیگی دا طریقہ چنن دیو**، دوواں چینلاں دا مظاہرہ کرو:
   - **Alipay (مینلینڈ/Alipay والے صارف)**: اک واری ادائیگی نال متعلقہ مدت کھلدی اے، **خودکار تجدید نہیں**
     - مہینہ **¥6.99** (پہلے ایہ آزماؤن دی سفارش) / سہ ماہی **¥19.99** / سالانہ **¥69.99**
   - **PayPal (بیرون ملک/Alipay نہ والے صارف)**: مہینہ وار خودکار تجدید، کسی وی ویلے منسوخ
     - Premium Monthly، تقریباً **$1/مہینہ** (سبسکرپشن صفحے تے دکھائے مطابق، خودکار تجدید)
3. صارف چون لے تاں:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   سکرپٹ پیمنٹ صفحے دا فائل راہ دیندا اے، **سسٹم کمانڈ نال سدھا کھولھو** (Windows: `start <فائل>`; macOS: `open <فائل>`; Linux: `xdg-open <فائل>`)۔ براؤزر خود Alipay/PayPal دے سرکاری کیشیئر تے لنگھدا اے، صارف ادا کردا اے یا اجازت دیندا اے۔
4. ہر 10–15 سیکنڈ `query` چلاؤ جدوں تک `paid` یا `ACTIVE` نہ آوے (آمدنی/اجازت عام طور تے چند سیکنڈ توں اک منٹ وچ آ جاندی اے)۔ صارف وچکار پیمنٹ صفہہ بند کر دے → سدھا دوبارہ `create-order` (پرانا آرڈر/باقی PayPal سبسکرپشن 2 گھنٹے وچ خود بند/میاڈ، فکر نہ کرو)۔
5. WeChat QR چینل دستی تصدیق اے، آمدنی دیر نال آندی اے؛ Huawei IAP صرف ہارمونی App وچ۔ ایہ دوویں skill خود نہیں کردا — ادا کرن تے وی قدم 7 تے واپس آؤ۔
""",
    BOUNDARY=("صارف دے Alipay اکاؤنٹ/پیمنٹ کریڈینشل نوں", "صارف دے Alipay/PayPal اکاؤنٹ/پیمنٹ کریڈینشل نوں"),
    PA_CONCL="""**Alipay تے PayPal دوواں سبسکرپشناں دا agent آرڈر تے ٹریکنگ کر سکدا اے۔**
Alipay اک واری ادائیگی، خودکار تجدید نہیں، مینلینڈ/Alipay والے صارفاں لئی موزوں؛ PayPal مہینہ وار خودکار تجدید، کسی وی ویلے منسوخ، بیرون ملک/Alipay نہ والے صارفاں لئی موزوں۔ WeChat QR (دستی تصدیق) تے Huawei IAP وی نیں، پر skill خود نہیں کردا۔""",
    PA_RESP=[
        ("صارف دے Alipay", "صارف دے Alipay/PayPal"),
        ("صارف خود Alipay سرکاری کیشیئر", "صارف خود سرکاری کیشیئر"),
    ],
    PA_FRESH=("skill `paid` دی تصدیق توں بعد", "skill `paid` / PayPal `ACTIVE` دی تصدیق توں بعد"),
    PA_PAYPAL="""## PayPal سبسکرپشن چینل (skill کردا اے، ویب ہارمونی نہیں)

صرف اک Premium Monthly پلان اے (تقریباً $1/مہینہ، `/api/subscription/plans` دے جواب مطابق)، **مہینہ وار خودکار تجدید**، صارف کسی وی ویلے PayPal بیک اینڈ تے منسوخ کر سکدا اے۔

### انٹرفیس معاہدہ (skill سکرپٹ وچ بنھیا گیا اے، agent سدھا درخواست نہیں بناؤندا)

| انٹرفیس | طریقہ | وضاحت |
|---|---|---|
| `/api/subscription/plans` | GET | Bearer جانچ، دستیاب پلاناں دی لسٹ دیندا اے (ہن صرف 1) |
| `/api/subscription/create` | POST | body `{planId}` → دیندا اے `{subscriptionId, approveUrl, status}`؛ status عام طور تے `APPROVAL_PENDING` |
| `/api/subscription/create` | GET | Bearer جانچ، دیندا اے `{activeSubscription, allSubscriptions}`؛ agent پولنگ کردا اے `activeSubscription.subscription.status === 'ACTIVE'` |
| `/api/subscription/verify` | POST | کامیابی صفہہ خود کال کردا اے (cookie نال)، webhook نہ آن تے PayPal API نوں خود کال کے ایکٹویٹ کردا اے |
| `/subscription/success` | براؤزر واپسی صفہہ | PayPal اجازت توں بعد اتردا اے، خود verify پولنگ کردا اے؛ ایکٹویٹ ہون تے ہوم/اصل صفحے تے واپس |
| `/subscription/cancel` | براؤزر صفہہ | صارف منسوخ کرے یا فیل ہووے تاں اتردا اے، دوبارہ شروع کر سکدا اے |

### agent عمل

```
create-order --provider paypal  # → approveUrl دیندا اے تے لوکل HTML فائل وچ لکھدا اے
HTML فائل کھولھو                  # → براؤزر PayPal اجازت صفحے تے لنگھدا اے
query (ہر 10–15s)               # → ACTIVE تک پولنگ
refresh-login                   # → نواں JWT (سبسکرپشن دعویٰ ACTIVE)
login-link --target home        # → اصل لاگ ان لنک بناؤندا اے
```

- 1 گھنٹے وچ نہ مکمل ہووے والی PENDING سبسکرپشن بیک اینڈ خود صاف کردا اے، دوبارہ شروع کر سکدے او۔
- جے صارف دوبارہ `create-order` چلاؤے، بیک اینڈ اجے وی چالو `APPROVAL_PENDING` سبسکرپشن دوبارہ ورتدا اے، 409 توں بچن لئی۔
- Alipay وانگوں: ادائیگی آؤن تے صرف DB اپڈیٹ ہوندا اے، پرانا JWT خود ریفریش نہیں ہوندا، **ضرور** پہلے `refresh-login` فیر ہوم لنک بھیجو۔""",
    PA_ROWS="""| PayPal `query` ہمیشہ PENDING | صارف نے اجے PayPal تے اجازت نہیں دتی؛ براؤزر وچ اجازت دا لنک کھلیا ہووے یقینی کرو۔ اجازت دے دتی ہووے تاں وی PENDING رہے تاں شاید webhook دیری اے — صارف نوں کامیابی صفحے تے چند سیکنڈ انتظار یا ریفریش کرن لئی کہو |
| PayPal `query` توں 409 آوے | نامکمل PayPal سبسکرپشن اے؛ 1 گھنٹے انتظار کرو خودکار میاڈ لئی، یا براؤزر وچ پرانی اجازت مکمل کرو |
| PayPal ادائیگی ہو گئی، لنک 2 وچ وی رکدا اے | Alipay وانگوں: پہلے `refresh-login` فیر `login-link` |
""",
    AF_ROW_CREATE="| `create-order` | `--package monthly\\|quarterly\\|yearly` (Alipay ڈیفالٹ) <br>`--provider alipay\\|paypal` | پیمنٹ آرڈر بناوے؛ Alipay پیمنٹ صفہہ فائل راہ + outTradeNo دیندا اے؛ PayPal اجازت صفہہ فائل راہ + subscriptionId دیندا اے (خود سٹیٹ فائل وچ لکھیا جاندا اے) |",
    AF_ROW_QUERY="| `query` | —— | آرڈر/سبسکرپشن حالت پچھو۔ Alipay: `paid / pending / closed / unknown`؛ PayPal: `ACTIVE / PENDING`, 10–15s پولنگ |",
    AF_SEQ7="""7.  (صارف ادائیگی دا طریقہ چوندا اے)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal""",
    AF_SEQ8=("    # → صارف Alipay کیشیئر تے ادا کردا اے (گفتگو چھوڑن دا دوجا قدم②)",
             "    # → صارف Alipay/PayPal کیشیئر تے ادا کردا اے یا اجازت دیندا اے (گفتگو چھوڑن دا دوجا قدم②)"),
    AF_SEQ9=("9.  query (ہر 10–15s) جدوں تک paid", "9.  query (ہر 10–15s) جدوں تک paid / ACTIVE"),
    AF_API_CREATE="| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |",
    AF_API_QUERY="| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |",
    AF_ERR_CLOSE=("| `create-order` توں بعد صارف نے پیمنٹ صفہہ بند کیتا | سدھا دوبارہ `create-order` (پرانا آرڈر 2h وچ خود بند) |",
                  "| `create-order` توں بعد صارف نے پیمنٹ صفہہ بند کیتا | سدھا دوبارہ `create-order` (پرانا آرڈر 2h وچ خود بند؛ PayPal PENDING سبسکرپشن 1h بعد خودکار میاڈ) |"),
    AF_ERR_409="| `create-order --provider paypal` توں 409 آوے | نامکمل PayPal سبسکرپشن اے؛ 1 گھنٹے انتظار کرو خودکار میاڈ لئی، یا براؤزر وچ پرانی اجازت مکمل کرو |",
    AF_ERR_PEND=("| `query` ہمیشہ pending | شاید صارف نے ادا نہیں کیتا؛ اک سوال پچھو۔ واقعی ادا کیتا اے → payment-and-activation.md جانچ جدول مطابق جاؤ |",
                 "| `query` ہمیشہ pending / PENDING | شاید صارف نے ادا نہیں کیتا؛ اک سوال پچھو۔ واقعی ادا کیتا اے → payment-and-activation.md جانچ جدول مطابق جاؤ |"),
    AF_ERR_403=("پیمنٹ اجے آئی نہیں، قدم 9 تے واپس پولنگ جاری رکھو", "پیمنٹ/اجازت اجے آئی نہیں، قدم 9 تے واپس پولنگ جاری رکھو"),
    RD=[
        ("Alipay سبسکرپشن آرڈر تے آمدنی ٹریکنگ", "Alipay/PayPal سبسکرپشن آرڈر تے آمدنی ٹریکنگ"),
        ("**v2.0.0 توں ایجنٹ-معاون موڈ اے**:", "**v2.0.0 توں ایجنٹ-معاون موڈ اے، v2.1.0 توں PayPal وی agent کر سکدا اے**:"),
        ("Alipay چینل وچ ایجنٹ آرڈر بناؤندا اے (مہینہ ¥6.99 / سہ ماہی ¥19.99 / سال ¥69.99، اک واری ادائیگی، خودکار تجدید نہیں) + آمدنی پولنگ؛ بیرونی صارف PayPal تے واپس؛ WeChat QR/ہوآوی IAP لئی راہ دساؤ۔",
         "Alipay (مہینہ ¥6.99 / سہ ماہی ¥19.99 / سال ¥69.99، اک واری ادائیگی، خودکار تجدید نہیں) تے PayPal (Premium Monthly، تقریباً $1/مہینہ، خودکار تجدید، کسی وی ویلے منسوخ) دوواں وچ ایجنٹ آرڈر بناؤندا اے + آمدنی پولنگ؛ بیرونی صارف PayPal تے واپس؛ WeChat QR/ہوآوی IAP لئی راہ دساؤ۔"),
        ("صارف دے Alipay اکاؤنٹ یا پیمنٹ کریڈینشل نوں کدے نہیں چھوندا", "صارف دے Alipay/PayPal اکاؤنٹ یا پیمنٹ کریڈینشل نوں کدے نہیں چھوندا"),
        ("ادائیگی ہمیشہ صارف تے Alipay سرکاری کیشیئر دے وچکار ہوندی اے۔", "ادائیگی ہمیشہ صارف تے سرکاری کیشیئر دے وچکار ہوندی اے۔"),
    ],
)
