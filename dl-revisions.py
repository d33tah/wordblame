#!/usr/bin/env python

"""
Usage:

./dl-revisions.py Nmap > urls.txt
"""

from lxml import html
import urllib
import uuid

E = str(uuid.uuid4())
def get_hexed(url):
    print(url)
    h = urllib.urlopen(url).read()
    t = html.fromstring(h)
    open('/tmp/meh/' + url.replace('/', '_'), "w").write(h)
    z = t.xpath('//textarea')[0].text
    ret = z.replace(' ', E+'\n')
    open('/tmp/meh2/' + url.replace('/', '_'), "w").write(ret.encode('utf-8'))
    return ret

inurl = 'https://en.wikipedia.org/w/index.php?title=%s&limit=500&action=history' % sys.argv[1]
while True:
    t = html.parse(urllib.urlopen(inurl))
    for a in t.xpath('//a [@class="mw-changeslist-date"]'):
        url = 'https://en.wikipedia.org' + a.get('href') + '&action=edit'
        e = get_hexed(url)
    n = t.xpath('//a [contains(.,"older 500")]')
    if n:
        inurl = 'https://en.wikipedia.org/' + n[0].get('href')
    else:
        break
