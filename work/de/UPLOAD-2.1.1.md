# powpow-register-de v2.1.1 上传说明

## 压缩包完整路径

```
C:\Users\dongtao\WorkBuddy\2026-10-11-23-20-28\_tmp\powpow-register-de-2.1.1.zip
```

| 项 | 值 |
|---|---|
| 文件名 | `powpow-register-de-2.1.1.zip` |
| 大小 | 946.7 KB |
| 文件数 | 16 |
| SHA256 | `54fcb7cf9767778558756fd892d2b0fc8c8109f2c7f62ebd21e709645e304e19` |
| 包结构 | **平铺**（无顶层目录，`SKILL.md` 直接在根） |
| 基底 | 线上 de 2.1.0 包逐字节复制，仅改版本号 |

---

## ⚠️ 版本号差异说明（重要）

**只有 de 是 2.1.1，其余 38 个变体仍为 2.1.0。**

| 变体 | 版本 |
|---|---|
| `powpow-register-de`（德语） | **2.1.1** ← 本次 |
| 其余 38 个（含中文源 `powpow-register`） | 2.1.0 |

这是**有意设计**：本次只针对 de 单独发一个补丁版，用来覆盖被冻结的商店简介文案（`summary` 字段），其他语言不受影响、内容完全一致。

版本号改动位置（共 3 处，与功能无关）：

| 文件 | 改动 |
|---|---|
| `SKILL.md` L4 | `version: 2.1.0` → `version: 2.1.1` |
| `SKILL.md` L15 | `**Version 2.1.0** · 2026-10-11` → `**Version 2.1.1** · 2026-10-12` |
| `_meta.json` | `"version": "2.1.0"` → `"version": "2.1.1"` |

**功能代码零改动** —— `scripts/powpow-register.mjs` 与线上 2.1.0 逐字节相同（17286 字节，含 PayPal 支持）。

---

## 包内文件清单（16 个）

```
README.md
SKILL.md
_meta.json
clawhub-listing.json
skill-card.md
references/agent-flow.md
references/payment-and-activation.md
references/registration-flow.md
references/screenshots.md
scripts/powpow-register.mjs
assets/screenshots/powpow-01.jpg ~ powpow-06.jpg（6 张）
```

---

## 上传步骤

### 方式一：网页后台上传（推荐）

1. 打开 ClawHub → `powpow-register-de` 技能页
2. 找 **Upload new version / 发布新版本**
3. 选择上面的 zip 文件
4. **版本号填 `2.1.1`**（不要填 2.1.0，会被拒）
5. **Summary / 商店简介字段 —— 粘贴下面这段德文**（这是本次修复的**核心**）
6. Changelog 可写：`v2.1.1: Store-Description (Summary) auf den aktuellen v2.1.0-Stand aktualisiert (PayPal ergänzt).`
7. 上传

### 方式二：我用脚本代传

你只要说一声，我直接用 `.token` 调用 API 发布 + 回环校验。

---

## Summary 字段要粘的内容（德文）

### 完整版（1022 字符，推荐）

```
Hilft Nutzer:innen, PowPow- (Bubble-)Registrierung, Alipay-/PayPal-Abonnement-Aktivierung und Ein-Klick-Login komplett im Chat abzuschließen. Der agent füllt Formulare (inkl. Avatar-Upload), sendet den E-Mail-Verifizierungscode, erstellt den Zahlungsauftrag und verfolgt den Zahlungseingang; die Nutzer:innen geben nur Basisinformationen an, rufen einmal den Verifizierungscode ab und zahlen an der Alipay-/PayPal-Kasse — ohne den Chat zu verlassen. Auslöser: „Bubble registrieren", „PowWow-Konto registrieren", „Wie registriere ich mich bei Bubble?", „Hilf mir, ein powpow-Konto anzulegen", „sign up powpow"; behandelt auch Feststeckendes bei der Registrierung (kein Verifizierungscode, Benutzername/E-Mail vergeben) und Aktivierungsprobleme (Login meldet „Konto nicht aktiviert" / pending_payment, wie abonnieren/bezahlen). Benötigt Node ≥ 18; falls nicht verfügbar, automatischer Rückfall in den reinen Anleitungsmodus. Keine Beiträge/kein Erstellen digitaler Menschen (das macht powpow-simple), keine Code-Entwicklung.
```

### 精简版（330 字符，若输入框有字数限制）

```
Hilft Nutzer:innen, die PowPow-(Bubble-)Registrierung, die Alipay-/PayPal-Abonnement-Aktivierung und den Ein-Klick-Login vollständig im Chat abzuschließen. Auslöser: „Bubble registrieren", „Wie registriere ich mich bei Bubble?", behandelt auch Registrierungs- und Aktivierungsprobleme.
```

**注意**：德文引号用的是 `„…"`（低位双引号 + 直双引号），复制时别被输入法替换成英文引号。

---

## 不要改的字段

| 字段 | 状态 |
|---|---|
| Description / 详细描述 | ✅ 已正确（含 PayPal），**不要动** |
| Display name | ✅ 正确 |
| Name / slug | `powpow-register` / `powpow-register-de`，**不要动** |
| Categories | `communication`, `lifestyle` |

---

## 上传后验证

上传完成后告诉我，我会用 API 回读确认：

1. `latestVersion` == `2.1.1`
2. `summary` 长度从 **142 → 1022**（或 330）
3. `summary` 含 `PayPal` 关键字
4. 下载 `version=2.1.1` 的包与本地 `stage/de/` 逐字节比对

如果 `summary` 仍被服务端忽略（回读还是 142），说明该字段确实是纯派生、无法通过发版覆盖 —— 那就退回"联系官方后台改"这条路，我这边有现成的申请信模板。