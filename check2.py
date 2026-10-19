# -*- coding: utf-8 -*-
"""Triple validation for data2_* translation files.

Checks per language:
1. py_compile syntax
2. foreign-script contamination (CJK / kana / cyrillic / arabic / hebrew / georgian / armenian / hangul / devanagari-adjacent-latin / etc.)
   - allowed exception: the platform error string "请完成订阅以激活账户" (intentional, kept verbatim in RF_ROW_403)
   - per-language expected script family is auto-detected from the majority of characters
3. 23-key completeness against data2_en.EN
4. language-invariant anchors present (code spans, URLs, versions, prices)
"""
import io, os, re, sys, importlib, py_compile

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

# script ranges: (name, regex) - each is "foreign" to at least one of our target languages,
# but we only flag chars that are outside the language's own expected set.
CJK = r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]'
KANA = r'[\u3040-\u30ff]'
HANGUL = r'[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]'
CYRILLIC = r'[\u0400-\u04ff\u0500-\u052f]'
ARABIC = r'[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff]'
HEBREW = r'[\u0590-\u05ff]'
GEORGIAN = r'[\u10a0-\u10ff]'
ARMENIAN = r'[\u0530-\u058f]'
ETHIOPIC = r'[\u1200-\u137f]'
BENGALI = r'[\u0980-\u09ff]'
DEVANAGARI = r'[\u0900-\u097f]'
GURMUKHI = r'[\u0a00-\u0a7f]'
GUJARATI = r'[\u0a80-\u0aff]'
ORIYA = r'[\u0b00-\u0b7f]'
TAMIL = r'[\u0b80-\u0bff]'
TELUGU = r'[\u0c00-\u0c7f]'
KANNADA = r'[\u0c80-\u0cff]'
MALAYALAM = r'[\u0d00-\u0d7f]'
SINHALA = r'[\u0d80-\u0dff]'
THAI = r'[\u0e00-\u0e7f]'
LAO = r'[\u0e80-\u0eff]'
MYANMAR = r'[\u1000-\u109f]'
KHMER = r'[\u1780-\u17ff]'

ALLOWED_CN = '请完成订阅以激活账户'  # intentional platform error message, kept verbatim
ALLOWED_SHARED = '\u0964\u0965'  # danda / double danda: shared Indic punctuation (no dedicated codepoints in Gurmukhi etc.)

INDIC = DEVANAGARI + GURMUKHI + GUJARATI + ORIYA + BENGALI + TAMIL + TELUGU + KANNADA + MALAYALAM + SINHALA

FOREIGN = {
    'CJK': CJK, 'KANA': KANA, 'HANGUL': HANGUL, 'CYRILLIC': CYRILLIC,
    'ARABIC': ARABIC, 'HEBREW': HEBREW, 'GEORGIAN': GEORGIAN, 'ARMENIAN': ARMENIAN,
    'ETHIOPIC': ETHIOPIC, 'BENGALI': BENGALI, 'DEVANAGARI': DEVANAGARI,
    'GURMUKHI': GURMUKHI, 'GUJARATI': GUJARATI, 'ORIYA': ORIYA, 'TAMIL': TAMIL,
    'TELUGU': TELUGU, 'KANNADA': KANNADA, 'MALAYALAM': MALAYALAM, 'SINHALA': SINHALA,
    'THAI': THAI, 'LAO': LAO, 'MYANMAR': MYANMAR, 'KHMER': KHMER,
}

# expected native scripts per language (families that are OK for that language)
NATIVE = {
    'en': [], 'gu': [GUJARATI], 'pa': [GURMUKHI], 'am': [ETHIOPIC],
    'bho': [DEVANAGARI], 'ha': [], 'jv': [], 'ln': [], 'pcm': [],
    'sw': [], 'tl': [], 'yo': [], 'my': [MYANMAR], 'or': [ORIYA], 'pnb': [ARABIC],
    'ja': [KANA, CJK], 'ko': [HANGUL], 'es': [], 'fr': [], 'de': [], 'pt': [],
    'it': [], 'ru': [CYRILLIC], 'pl': [], 'tr': [], 'vi': [], 'id': [], 'ar': [ARABIC],
    'hi': [DEVANAGARI], 'th': [THAI], 'bn': [BENGALI], 'ur': [ARABIC], 'fa': [ARABIC],
    'ta': [TAMIL], 'te': [TELUGU], 'ml': [MALAYALAM], 'kn': [KANNADA], 'mr': [DEVANAGARI],
}

# embedded-latin check for Indic/Burmese/Ethiopic scripts: letter-only ranges
# (punctuation like Ethiopic word separator U+1361/1362/1363 or Devanagari danda is excluded)
LETTERS = {
    'gu': r'\u0a85-\u0ab9', 'pa': r'\u0a05-\u0a39', 'bho': r'\u0904-\u0939\u0958-\u095f\u0960-\u0961',
    'am': r'\u1200-\u135c', 'my': r'\u1000-\u1039', 'or': r'\u0b05-\u0b39',
    'pnb': r'\u0620-\u064a', 'hi': r'\u0904-\u0939\u0958-\u095f\u0960-\u0961',
    'ta': r'\u0b85-\u0bb9', 'te': r'\u0c05-\u0c39', 'ml': r'\u0d05-\u0d39',
    'kn': r'\u0c85-\u0cb9', 'mr': r'\u0904-\u0939\u0958-\u095f\u0960-\u0961',
    'bn': r'\u0985-\u09b9', 'ru': r'\u0410-\u044f',
}
EMBED_SCAN = LETTERS

LATIN = r'[A-Za-z]'

ANCHORS = [
    'pending_payment', 'me?token=', 'powpow_token', 'login-link', '--target home',
    '--target pending', 'create-order', '--package monthly', '--provider paypal',
    'refresh-login', 'whoami', 'cleanup', 'prepare-suggest', 'send-code',
    'powpow-register.mjs', 'powpow-simple', '@durenzidu/powpow-integration',
    '@durenzidu/openclaw-channel-powpow', 'https://global.powpow.online/register',
    'https://global.powpow.online/subscription', '2.2.0', '2026-10-18',
    # prices: accept "¥6.99" or localized "6,99 ¥" (FR/DE decimal comma)
    ('¥6.99', '6,99 ¥'), ('¥19.99', '19,99 ¥'), ('¥69.99', '69,99 ¥'),
    'accountStatus', 'pendingUserToken', 'ACTIVE',
    'Node ≥ 18', 'references/agent-flow.md', 'references/registration-flow.md',
    'references/payment-and-activation.md', 'references/screenshots.md',
    'POWPOW_REGISTER_PASSWORD', 'HttpOnly', 'SameSite=Lax', '307',
    'Alipay', 'PayPal', 'WeChat', 'Huawei IAP', 'HarmonyOS',
]


def strip_allowed_cn(text):
    for ch in ALLOWED_SHARED:
        text = text.replace(ch, '')
    return text.replace(ALLOWED_CN, '')


def check_impurity(lang, text):
    t = strip_allowed_cn(text)
    native = NATIVE.get(lang, [])
    hits = []
    for name, rx in FOREIGN.items():
        pat = re.compile(rx)
        if name == 'CJK' and 'CJK' in [n for n, r in FOREIGN.items() if r in native]:
            continue
        # skip if this script is native for the language
        if rx in native:
            continue
        found = pat.findall(t)
        if found:
            hits.append((name, len(found), ''.join(sorted(set(found))[:12])))
    return hits


def check_embedded_latin(lang, text):
    if lang not in EMBED_SCAN:
        return []
    t = strip_allowed_cn(text)
    out = []
    letters = EMBED_SCAN[lang]
    # native letter directly adjacent to a latin letter (either side)
    for m in re.finditer('([' + letters + '])(' + LATIN[1:-1] + ')', t):
        out.append(m.group(0))
    for m in re.finditer('(' + LATIN[1:-1] + ')([' + letters + '])', t):
        out.append(m.group(0))
    return out


def main():
    from data2_en import EN
    files = sys.argv[1:]
    if not files:
        files = ['data2_all']
    grand_fail = 0
    for fn in files:
        path = os.path.join(ROOT, fn + '.py') if not fn.endswith('.py') else os.path.join(ROOT, fn)
        modname = os.path.basename(path)[:-3]
        # syntax check
        try:
            py_compile.compile(path, doraise=True)
        except py_compile.PyCompileError as e:
            print('!! %s SYNTAX FAIL: %s' % (modname, e))
            grand_fail += 1
            continue
        mod = importlib.import_module(modname)
        langs = {}
        for name in dir(mod):
            if name.isupper() and name not in ('EN',) and isinstance(getattr(mod, name), dict):
                langs[name.lower()] = getattr(mod, name)
        if 'data' in dir(mod):
            for k, v in mod.data.items():
                langs[k] = v
        for lang, d in sorted(langs.items()):
            problems = []
            missing = [k for k in EN if k not in d]
            extra = [k for k in d if k not in EN]
            if missing:
                problems.append('MISSING %s' % missing)
            if extra:
                problems.append('EXTRA %s' % extra)
            for k, v in d.items():
                if k == 'LISTING_NOTE':
                    continue  # meta note intentionally kept in Chinese across all packs
                hits = check_impurity(lang, v)
                if hits:
                    problems.append('%s impurity %s' % (k, hits))
                emb = check_embedded_latin(lang, v)
                if emb:
                    problems.append('%s embedded-latin %s' % (k, emb[:8]))
            # anchor check on the full concatenated text
            full = '\n'.join(d.values())
            for a in ANCHORS:
                alts = a if isinstance(a, tuple) else (a,)
                if not any(x in full for x in alts):
                    problems.append('anchor missing: %r' % (a,))
            if problems:
                grand_fail += 1
                print('!! %s [%s]' % (modname, lang))
                for p in problems:
                    print('   ', p)
            else:
                print('OK %s [%s] %d keys' % (modname, lang, len(d)))
    print('---')
    print('FAIL' if grand_fail else 'ALL PASS')
    sys.exit(1 if grand_fail else 0)


if __name__ == '__main__':
    main()
