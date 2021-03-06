import urllib2
import json
import sys
import os

import argument
from argument import Time

extend = ""
argu = {
  '-t': Time()
}

for i in range(1, len(sys.argv)):
###check argument
  if sys.argv[i] in argu.keys(): 
    extend = extend + argu[sys.argv[i]]
    i = i + 1

  with open(sys.argv[i]) as fin:
    urls = json.load(fin)
    for name, url in urls.iteritems():
      content = urllib2.urlopen(url)
      data = content.read()
      with open(os.path.join('output', extend + name + '.json'), 'w+') as fout:
        fout.write(data.decode('utf-8').encode('utf-8'))
      fout.close()

  fin.close()
