# -*- coding: utf-8 -*-
"""Package work/<lang> into upload/ as powpow-register-<lang>-2.1.0.zip (flat root)."""
import os, zipfile, io, json
langs = 'en ja ko es fr de pt it ru pl tr vi'.split()
os.makedirs('upload', exist_ok=True)
for l in langs:
    src = os.path.join('work', l)
    out = os.path.join('upload', 'powpow-register-%s-2.1.0.zip' % l)
    n = 0
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(src):
            dirs.sort()
            for f in sorted(files):
                p = os.path.join(root, f)
                z.write(p, os.path.relpath(p, src).replace('\\', '/'))
                n += 1
    print('%-3s %6d B  %2d files  %s' % (l, os.path.getsize(out), n, os.path.basename(out)))
