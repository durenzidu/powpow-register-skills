# -*- coding: utf-8 -*-
"""Verify a v2.2.0-patched package: version markers, new-flow markers, no stale content.

All checks use language-invariant anchors only (dates, code tokens, version strings,
digit-normalized table rows) so they work identically across all 38 localized packs.
"""
import io, os, re, sys, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apply2 import norm_digits

LANGS = sys.argv[1:]
ok = True
for l in LANGS:
    d = 'work/' + l
    sk = io.open(d + '/SKILL.md', encoding='utf-8').read()
    pa = io.open(d + '/references/payment-and-activation.md', encoding='utf-8').read()
    af = io.open(d + '/references/agent-flow.md', encoding='utf-8').read()
    rf = io.open(d + '/references/registration-flow.md', encoding='utf-8').read()
    rd = io.open(d + '/README.md', encoding='utf-8').read()
    sc = io.open(d + '/scripts/powpow-register.mjs', encoding='utf-8').read()
    mv = json.loads(io.open(d + '/_meta.json', encoding='utf-8').read())
    sk_n = norm_digits(sk)
    chk = {
        'ver': re.search(r'^version:\s*2\.2\.0$', sk, re.M) is not None,
        'meta': mv['version'] == '2.2.0',
        # no stale version *declaration*; VLINE history mentions of v2.1.0 are legitimate
        'no211': ('version: 2.1.0' not in sk and '2.1.0' not in pa
                  and '2.1.0' not in af and '2.1.0' not in rf and '2.1.0' not in rd),
        'homefirst': '--target home' in sk and 'login-link --target home' in af,
        'flow6': (re.search(r'^\|\s*6\s', sk_n, re.M) is not None
                  and '--provider alipay|paypal' not in sk),
        'step8': re.search(r'^## .*8', sk_n, re.M) is not None,
        # free-period date anchor present in the version banner (every language)
        'freeperiod': '2026-10-18' in sk,
        # Full Sequence block markers (code tokens, language-invariant)
        'af_fast': 'prepare-suggest' in af and 'query' in af and 'whoami' in af,
        # subscription-landing error row carries the pending-link command
        'af_errsub': 'login-link --target pending' in af,
        'pa_note': '2026-10-18' in pa,
        'rf_state': 'accountStatus' in rf and '2026-10-18' in rf,
        'rd': '2.2.0' in rd,
        'script_new': 'target=home' in sc,
        'no_twice_depart': 'twice' not in sk.lower() or 'only once' in sk.lower(),
    }
    bad = [k for k, v in chk.items() if not v]
    print('%-4s %s %s' % (l, 'OK ' if not bad else 'BAD', (' '.join(bad) if bad else '')))
    if bad:
        ok = False
print('ALL OK' if ok else 'HAS FAILURES')
