# -*- coding: utf-8 -*-
"""Check registry version for each language pack (version is embedded in the
skill.description field as the frontmatter of the current published SKILL.md)."""
import json, sys, time, urllib.request

TOK = open('.token', encoding='utf-8').read().strip()


def api_get(path):
    req = urllib.request.Request('https://clawhub.ai/api/v1/' + path)
    req.add_header('Authorization', 'Bearer ' + TOK)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode('utf-8'))


for l in sys.argv[1:]:
    slug = 'powpow-register-' + l if l != 'zh' else 'powpow-register'
    try:
        j = api_get('skills/' + slug)
        desc = j['skill'].get('description') or ''
        ver = None
        for line in desc.split('\n'):
            if line.startswith('version:'):
                ver = line.split(':', 1)[1].strip()
                break
        has_date = '2026-10-18' in desc
        print('%-4s registry version=%-8s free-period-date=%s' % (l, ver, has_date))
    except Exception as e:
        print('%-4s ERR %s' % (l, str(e)[:100]))
    time.sleep(0.25)
