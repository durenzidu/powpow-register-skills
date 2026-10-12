# -*- coding: utf-8 -*-
"""Verify a patched package: version, PayPal markers, section order."""
import io, os, re, sys, json

LANGS = sys.argv[1:]
ok = True
for l in LANGS:
    d = 'work/' + l
    sk = io.open(d + '/SKILL.md', encoding='utf-8').read()
    pa = io.open(d + '/references/payment-and-activation.md', encoding='utf-8').read()
    af = io.open(d + '/references/agent-flow.md', encoding='utf-8').read()
    rd = io.open(d + '/README.md', encoding='utf-8').read()
    mv = json.loads(io.open(d + '/_meta.json', encoding='utf-8').read())
    chk = {
        'ver': re.search(r'^version:\s*2\.1\.0$', sk, re.M) is not None,
        'meta': mv['version'] == '2.1.0',
        'no201': '2.0.1' not in sk and '2.0.1' not in pa and '2.0.1' not in af,
        'step6': '--provider paypal' in sk,
        'flow6': '--provider alipay|paypal' in sk,
        'paypal_sec': '\n## ' in pa and len(re.findall(r'^## .*[Pp]ayPal', pa, re.M)) >= 1,
        'af_create': '--provider alipay\\|paypal' in af,
        'af_query': 'ACTIVE / PENDING' in af,
        'rd': '2.1.0' in rd,
        'script': os.path.getsize(d + '/scripts/powpow-register.mjs') == 17286,
    }
    heads = [x for x in pa.split('\n') if x.startswith('## ')]
    bad = [k for k, v in chk.items() if not v]
    print('%-4s %s %s' % (l, 'OK ' if not bad else 'BAD', (' '.join(bad) if bad else '')))
    print('     heads: ' + ' | '.join(h[:32] for h in heads))
    if bad:
        ok = False
print('ALL OK' if ok else 'HAS FAILURES')
