# -*- coding: utf-8 -*-
"""Download the just-published 2.1.0 package and diff it against work/<lang>."""
import io, os, sys, json, zipfile, urllib.request, shutil, hashlib

TOK = open('.token', encoding='utf-8').read().strip()
langs = sys.argv[1:] or 'en ja ko es fr de pt it ru pl tr vi'.split()

os.makedirs('dl', exist_ok=True)
for l in langs:
    slug = 'powpow-register-' + l
    url = 'https://clawhub.ai/api/v1/download?slug=%s&version=2.1.0' % slug
    req = urllib.request.Request(url)
    req.add_header('Authorization', 'Bearer ' + TOK)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    zp = os.path.join('dl', l + '.zip')
    open(zp, 'wb').write(data)
    d = os.path.join('dl', l)
    if os.path.isdir(d):
        shutil.rmtree(d)
    with zipfile.ZipFile(zp) as z:
        z.extractall(d)
    bad = []
    for root, _, fs in os.walk(os.path.join('work', l)):
        for f in fs:
            rel = os.path.relpath(os.path.join(root, f), os.path.join('work', l)).replace('\\', '/')
            if rel in ('_meta.json', 'skill-card.md'):
                continue
            a = open(os.path.join('work', l, rel), 'rb').read()
            b = open(os.path.join(d, rel), 'rb').read()
            if a != b:
                bad.append(rel)
    names = sorted(os.path.relpath(os.path.join(r, f), d).replace('\\', '/')
                   for r, _, fs in os.walk(d) for f in fs)
    print('%-3s %7d B  files=%d  %s' % (l, len(data), len(names),
                                        'OK' if not bad else 'MISMATCH ' + ','.join(bad)))
