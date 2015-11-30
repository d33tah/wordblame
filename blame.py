#!/usr/bin/env python

import sys
import subprocess
from functools32 import lru_cache

skip = '84b3b2ad (Jacek Wielemborek 2015-11-30 11:33:20 +0100   87) '

@lru_cache()
def commit_to_url(commit):
    return subprocess.check_output("git log '%s^..%s' --format=oneline" % (commit, commit), shell=True).split()[-1].replace('&action=edit','&diff=prev').replace('_', '/')

z = ""
for line in sys.stdin:
    commit = line.split()[0]
    url = commit_to_url(commit)
    text = line[len(skip):].rstrip()
    if text.endswith('28cacf72-e312-43db-9c4a-ca8024b8ef05'):
        add = text[:-len('28cacf72-e312-43db-9c4a-ca8024b8ef05')] + ' '
    else:
        add = text + '\n<br />'
    z += '<a href="%s" style="color: %s">%s</a>' % (url, commit[:6], add)
print(z)
