import time

def Time():
  t = time.localtime()
  output = time.mktime(t)
  return '(' + time.strftime("%Y-%b-%d_%H:%M:%S", time.gmtime(output)) + ')'
