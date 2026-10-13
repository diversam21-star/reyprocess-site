#!/usr/bin/env python3
"""Rebuild index.html from template.html by embedding assets as data URIs."""
import base64,re,os
d=os.path.dirname(os.path.abspath(__file__))
m={'cross':'rooted-cross-white.png','crosssm':'rooted-cross-white-sm.png','hero':'hero.jpg','home':'app-home.jpg','kids':'app-kids.jpg','fellow':'app-fellow.jpg','teefront':'tee-front.jpg','teeback':'tee-back.jpg'}
t=open(f'{d}/template.html').read()
def uri(f):
    mt='image/png' if f.endswith('png') else 'image/jpeg'
    return f'data:{mt};base64,'+base64.b64encode(open(f'{d}/assets/{f}','rb').read()).decode()
t=re.sub(r'\{\{(\w+)\}\}',lambda x:uri(m[x.group(1)]),t)
open(f'{d}/index.html','w').write(t); print('ok',len(t))
