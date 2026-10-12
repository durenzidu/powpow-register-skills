# -*- coding: utf-8 -*-
"""Apply the v2.0.1 -> v2.1.0 delta to one localized skill package."""
import io, os, re, sys, json, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'base210')
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


def find_line(ls, exact, where):
    for i, l in enumerate(ls):
        if l == exact:
            return i
    raise SystemExit('!! exact line not found [%s]: %r' % (where, exact[:80]))


def g(lang, key):
    return DATA[lang][key]


def patch_skill(d, lang):
    p = os.path.join(d, 'SKILL.md')
    ls = lines(p)
    for old, new in g(lang, 'DESC'):
        ls[2] = must_sub(ls[2], old, new, lang + ' SKILL desc')
    ls[3] = ls[3].replace('2.0.1', '2.1.0')
    assert ls[3].strip().startswith('version: 2.1.0'), ls[3]
    old, new = g(lang, 'INTRO')
    i = find_idx(ls, lambda l: old in l, lang + ' SKILL intro')
    ls[i] = must_sub(ls[i], old, new, lang + ' SKILL intro')
    i = find_idx(ls, lambda l: l.startswith('**') and '2.0.1' in l, lang + ' SKILL banner')
    for old, new in g(lang, 'VLINE'):
        ls[i] = must_sub(ls[i], old, new, lang + ' SKILL banner')
    pat = DATA[lang].get('FLOW6_RE', r'^\|\s*6\s')
    i = find_idx(ls, lambda l: re.match(pat, l), lang + ' SKILL flow row')
    ls[i] = must_sub(ls[i], '`create-order`', '`create-order --provider alipay|paypal`', lang + ' SKILL flow row')
    i = find_idx(ls, lambda l: 'login-link --target pending' in l, lang + ' SKILL step6 anchor')
    k = find_idx(ls, lambda l: re.match(r'^\s*2[.．、]\s', l), lang + ' SKILL item2', start=i)
    j = find_idx(ls, lambda l: l.startswith('## '), lang + ' SKILL next heading', start=i)
    ls[k:j] = g(lang, 'STEP6').split('\n')
    old, new = g(lang, 'BOUNDARY')
    i = find_idx(ls, lambda l: old in l, lang + ' SKILL boundary')
    ls[i] = must_sub(ls[i], old, new, lang + ' SKILL boundary')
    save(p, ls)


def patch_pa(d, lang):
    p = os.path.join(d, 'references/payment-and-activation.md')
    ls = lines(p)
    n = g(lang, 'PA_CONCL_N') if 'PA_CONCL_N' in DATA[lang] else 2
    ls[4:4 + n] = g(lang, 'PA_CONCL').split('\n')
    for old, new in g(lang, 'PA_RESP'):
        hit = False
        for i in range(4, 20):
            if old in ls[i]:
                ls[i] = must_sub(ls[i], old, new, lang + ' PA resp')
                hit = True
                break
        if not hit:
            raise SystemExit('!! PA resp not found: %r' % old[:60])
    old, new = g(lang, 'PA_FRESH')
    i = find_idx(ls, lambda l: old in l, lang + ' PA fresh')
    ls[i] = must_sub(ls[i], old, new, lang + ' PA fresh')
    h2 = [i for i, l in enumerate(ls) if l.startswith('## ')]
    # insert right before the "four channels / subscription page" section:
    #   6-heading packages (zh-like): h2[2];  7-heading packages: h2[3]
    at = h2[len(h2) - 4]
    ls[at:at] = g(lang, 'PA_PAYPAL').split('\n') + ['']
    h2 = [i for i, l in enumerate(ls) if l.startswith('## ')]
    i = find_idx(ls, lambda l: l.startswith('|') and '`refresh-login`' in l and '`login-link`' in l,
                 lang + ' PA trouble anchor', start=h2[len(h2) - 2])
    ls[i + 1:i + 1] = g(lang, 'PA_ROWS').split('\n')
    save(p, ls)


def patch_af(d, lang):
    p = os.path.join(d, 'references/agent-flow.md')
    ls = lines(p)
    i = find_idx(ls, lambda l: l.startswith('| `create-order` | `--package'), lang + ' AF create row')
    ls[i] = g(lang, 'AF_ROW_CREATE')
    i = find_idx(ls, lambda l: l.startswith('| `query` |'), lang + ' AF query row')
    ls[i] = g(lang, 'AF_ROW_QUERY')
    i = find_idx(ls, lambda l: 'create-order --package monthly' in l, lang + ' AF seq7')
    ls[i:i + 1] = g(lang, 'AF_SEQ7').split('\n')
    old, new = g(lang, 'AF_SEQ8')
    i = find_idx(ls, lambda l: old in l, lang + ' AF seq8')
    ls[i] = must_sub(ls[i], old, new, lang + ' AF seq8')
    old, new = g(lang, 'AF_SEQ9')
    i = find_line(ls, old, lang + ' AF seq9')
    ls[i] = new
    i = find_idx(ls, lambda l: l.startswith('| `create-order` | `POST /api/payment/alipay/create-order'), lang + ' AF api create')
    ls[i] = g(lang, 'AF_API_CREATE')
    i = find_idx(ls, lambda l: l.startswith('| `query` | `GET /api/payment/alipay/query'), lang + ' AF api query')
    ls[i] = g(lang, 'AF_API_QUERY')
    old, new = g(lang, 'AF_ERR_CLOSE')
    i = find_line(ls, old, lang + ' AF err close')
    ls[i] = new
    ls[i + 1:i + 1] = [g(lang, 'AF_ERR_409')]
    old, new = g(lang, 'AF_ERR_PEND')
    i = find_line(ls, old, lang + ' AF err pend')
    ls[i] = new
    old, new = g(lang, 'AF_ERR_403')
    i = find_idx(ls, lambda l: old in l, lang + ' AF err 403')
    ls[i] = must_sub(ls[i], old, new, lang + ' AF err 403')
    save(p, ls)


def patch_readme(d, lang):
    p = os.path.join(d, 'README.md')
    t = rd(p)
    for old, new in g(lang, 'RD'):
        t = must_sub(t, old, new, lang + ' README')
    wr(p, t)


def patch_meta(d, lang):
    shutil.copyfile(os.path.join(SRC, 'scripts/powpow-register.mjs'),
                    os.path.join(d, 'scripts/powpow-register.mjs'))
    shutil.copyfile(os.path.join(SRC, 'skill-card.md'), os.path.join(d, 'skill-card.md'))
    p = os.path.join(d, '_meta.json')
    j = json.loads(rd(p))
    j['version'] = '2.1.0'
    wr(p, json.dumps(j, ensure_ascii=False, indent=2) + '\n')


def apply(lang):
    d = os.path.join(ROOT, 'work', lang)
    patch_skill(d, lang)
    patch_pa(d, lang)
    patch_af(d, lang)
    patch_readme(d, lang)
    patch_meta(d, lang)
    print('patched', lang)


if __name__ == '__main__':
    import data_all
    DATA.update(data_all.DATA)
    for lang in sys.argv[1:]:
        apply(lang)
