# -*- coding: utf-8 -*-
"""Apply the v2.1.0 -> v2.2.0 delta (free testing period: register -> direct login) to one localized pack.

Anchor strategy (all language-invariant):
- code spans (`login-link`, `pending_payment`, `me?token=`), URLs, version strings, step digits
- structural positions (H1 intro line, banner line, Nth "## " heading)
Every patch is strict: a mismatch raises SystemExit with the language and anchor.
"""
import io, os, re, sys, json, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = {}


def rd(p):
    with io.open(p, encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)


def lines(p):
    return rd(p).split('\n')


def save(p, ls):
    wr(p, '\n'.join(ls))


def must_sub(text, old, new, where):
    n = text.count(old)
    if n != 1:
        raise SystemExit('!! %s: expected 1 occurrence of %r, got %d' % (where, old[:70], n))
    return text.replace(old, new)


def find_idx(ls, pred, where, start=0):
    for i in range(start, len(ls)):
        if pred(ls[i]):
            return i
    raise SystemExit('!! not found: ' + where)


def g(lang, key):
    return DATA[lang][key]


# localized digits -> ASCII (Arabic-Indic U+0660-69; Extended Arabic-Indic/Persian U+06F0-F9;
# Devanagari U+0966; Bengali U+09E6; Gurmukhi U+0A66; Gujarati U+0AE6; Oriya U+0B66; Tamil U+0BE6;
# Telugu U+0C66; Kannada U+0CE6; Malayalam U+0D66; Thai U+0E50; Myanmar U+1040)
DIGIT_MAP = {}
for _base in (0x0660, 0x06F0, 0x0966, 0x09E6, 0x0A66, 0x0AE6, 0x0B66, 0x0BE6, 0x0C66, 0x0CE6, 0x0D66, 0x0E50, 0x1040):
    for _k in range(10):
        DIGIT_MAP[chr(_base + _k)] = str(_k)


def norm_digits(s):
    return ''.join(DIGIT_MAP.get(c, c) for c in s)


def headings(ls):
    return [i for i, l in enumerate(ls) if l.startswith('## ')]


# ---------------- SKILL.md ----------------

def patch_skill(d, lang):
    p = os.path.join(d, 'SKILL.md')
    ls = lines(p)
    w = lang + ' SKILL'

    # 1. frontmatter description (line index 2) + version line
    ls[2] = g(lang, 'DESC')
    vi = find_idx(ls, lambda l: l.startswith('version:'), w + ' ver line')
    ls[vi] = 'version: 2.2.0'

    # 2. intro paragraph: first non-blank line after the H1
    h1 = find_idx(ls, lambda l: l.startswith('# ') and not l.startswith('## '), w + ' h1')
    i = find_idx(ls, lambda l: l.strip() != '', w + ' intro', start=h1 + 1)
    ls[i] = g(lang, 'INTRO')

    # 3. version banner: the "**...2.1.0..." line
    i = find_idx(ls, lambda l: l.startswith('**') and '2.1.0' in l, w + ' banner')
    ls[i] = g(lang, 'VLINE')

    # 4. runtime-env fallback line (the only /subscription URL line before the flow table)
    tbl = find_idx(ls, lambda l: norm_digits(l).startswith('| 1 ') or norm_digits(l).startswith('| 1\u3000'), w + ' flow tbl')
    i = find_idx(ls, lambda l: 'global.powpow.online/subscription' in l, w + ' rtenv', start=0)
    if i > tbl:
        raise SystemExit('!! %s: rtenv anchor after flow table' % w)
    ls[i] = g(lang, 'RT_ENV')

    # 5. trigger line (contains pending_payment; skip the frontmatter block)
    fm_end = find_idx(ls, lambda l: l.strip() == '---', w + ' fm end', start=1)
    i = find_idx(ls, lambda l: 'pending_payment' in l, w + ' trigger', start=fm_end + 1)
    ls[i] = g(lang, 'TRIGGER')

    # 6. flow table rows 6 / 7 (digits may be localized: bn Bengali, fa/ur Persian)
    i = find_idx(ls, lambda l: re.match(r'^\|\s*6\s', norm_digits(l)), w + ' flow6')
    ls[i] = g(lang, 'FLOW6')
    i = find_idx(ls, lambda l: re.match(r'^\|\s*7\s', norm_digits(l)), w + ' flow7')
    ls[i] = g(lang, 'FLOW7')

    # 7. step 6+7 sections: from the "## ...6..." heading to the "## ...8..." heading
    h = headings(ls)
    i6 = find_idx(ls, lambda l: l.startswith('## ') and re.search(r'6', norm_digits(l)), w + ' step6 head', start=tbl)
    i8 = find_idx(ls, lambda l: l.startswith('## ') and re.search(r'8', norm_digits(l)), w + ' step8 head', start=i6 + 1)
    new67 = (g(lang, 'STEP6') + '\n' + g(lang, 'STEP7')).split('\n')
    ls[i6:i8] = new67
    # step 8 section now starts right after the inserted block
    i8 = i6 + len(new67)
    if not ls[i8].startswith('## '):
        raise SystemExit('!! %s: step8 heading not where expected: %r' % (w, ls[i8][:60]))
    nxt = [x for x in headings(ls) if x > i8]
    end = nxt[0] if nxt else len(ls)
    ls[i8:end] = g(lang, 'STEP8').split('\n')

    # 8. paywall hard rule: 4th "- **" bullet in the last section
    h = headings(ls)
    last = h[-1]
    bullets = [i for i in range(last, len(ls)) if ls[i].startswith('- **')]
    if len(bullets) < 4:
        raise SystemExit('!! %s: hard-rule bullets < 4' % w)
    ls[bullets[3]] = g(lang, 'WALL')

    save(p, ls)


# ---------------- references/agent-flow.md ----------------

def patch_af(d, lang):
    p = os.path.join(d, 'references/agent-flow.md')
    ls = lines(p)
    w = lang + ' AF'

    # 1. login-link command row
    i = find_idx(ls, lambda l: l.startswith('| `login-link` |'), w + ' row login')
    ls[i] = g(lang, 'AF_ROW_LOGIN')

    # 2. Dual-Link + Full Sequence sections: heading #3 .. heading #5 (0-based 2..4)
    h = headings(ls)
    if len(h) < 5:
        raise SystemExit('!! %s: AF headings < 5' % w)
    ls[h[2]:h[4]] = g(lang, 'AF_LINKSEQ').split('\n')

    # 3. error table: replace the pending_payment row, insert the subscription-landing row before it
    i = find_idx(ls, lambda l: 'pending_payment' in l and l.lstrip().startswith('|'), w + ' err 403')
    ls[i] = g(lang, 'AF_ERR_403')
    ls[i:i] = [g(lang, 'AF_ERR_SUB')]

    # 4. fallback line (register URL line in the last section)
    i = find_idx(ls, lambda l: 'global.powpow.online/register' in l, w + ' fallback')
    ls[i] = g(lang, 'AF_FALLBACK')

    save(p, ls)


# ---------------- references/payment-and-activation.md ----------------

def patch_pa(d, lang):
    p = os.path.join(d, 'references/payment-and-activation.md')
    ls = lines(p)
    w = lang + ' PA'
    # insert the free-period note right after the first "## " heading (the Conclusion heading)
    i = find_idx(ls, lambda l: l.startswith('## '), w + ' concl head')
    ls[i + 1:i + 1] = g(lang, 'PA_NOTE').split('\n') + ['']
    save(p, ls)


# ---------------- references/registration-flow.md ----------------

def patch_rf(d, lang):
    p = os.path.join(d, 'references/registration-flow.md')
    ls = lines(p)
    w = lang + ' RF'
    # state-flow section: walk back from the accountStatus line to its "## " heading
    i = find_idx(ls, lambda l: "accountStatus: 'pending'" in l, w + ' state anchor')
    start = max(x for x in headings(ls) if x < i)
    nxt = [x for x in headings(ls) if x > start]
    end = nxt[0] if nxt else len(ls)
    ls[start:end] = g(lang, 'RF_STATE').split('\n')
    # error table rows (platform error text stays Chinese in every pack)
    i = find_idx(ls, lambda l: '请完成订阅以激活账户' in l, w + ' err 403')
    ls[i] = g(lang, 'RF_ROW_403')
    ls[i:i] = [g(lang, 'RF_ROW_LAND')]
    save(p, ls)


# ---------------- README.md / listing / meta / card / script ----------------

def patch_readme(d, lang):
    p = os.path.join(d, 'README.md')
    ls = lines(p)
    w = lang + ' README'
    # version paragraph: expand from the 'v2.1.0' line to the whole paragraph, replace
    i = find_idx(ls, lambda l: 'v2.1.0' in l, w + ' ver')
    start = i
    while start > 0 and ls[start - 1].strip() != '':
        start -= 1
    end = i
    while end < len(ls) - 1 and ls[end].strip() != '':
        end += 1
    ls[start:end] = g(lang, 'RD_VER').split('\n')
    # feature item 3: from the '3. ' line through the me?token= line
    fi = find_idx(ls, lambda l: l.startswith('3. '), w + ' feat3')
    mi = find_idx(ls, lambda l: 'me?token=' in l, w + ' feat3 end', start=fi)
    ls[fi:mi + 1] = g(lang, 'RD_LINK').split('\n')
    save(p, ls)


def patch_meta(d, lang):
    # new script (logic unchanged; two hint messages made flow-neutral)
    shutil.copyfile(os.path.join(ROOT, '..', 'powpow-register', 'scripts', 'powpow-register.mjs'),
                    os.path.join(d, 'scripts', 'powpow-register.mjs'))
    p = os.path.join(d, '_meta.json')
    if os.path.exists(p):
        j = json.loads(rd(p))
        j['version'] = '2.2.0'
        wr(p, json.dumps(j, ensure_ascii=False, indent=2) + '\n')
    # listing notes (Chinese meta-note, same for every pack)
    p = os.path.join(d, 'clawhub-listing.json')
    if os.path.exists(p):
        j = json.loads(rd(p))
        j['notes'] = g(lang, 'LISTING_NOTE')
        wr(p, json.dumps(j, ensure_ascii=False, indent=2) + '\n')
    # skill-card version line
    p = os.path.join(d, 'skill-card.md')
    if os.path.exists(p):
        t = rd(p)
        t = t.replace('2.1.0', '2.2.0')
        wr(p, t)


def apply(lang):
    d = os.path.join(ROOT, 'work', lang)
    patch_skill(d, lang)
    patch_af(d, lang)
    patch_pa(d, lang)
    patch_rf(d, lang)
    patch_readme(d, lang)
    patch_meta(d, lang)
    print('patched', lang)


if __name__ == '__main__':
    import data2_all
    DATA.update(data2_all.DATA)
    for lang in sys.argv[1:]:
        apply(lang)
