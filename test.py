import urllib2
content = urllib2.urlopen('http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$format=json')
data = content.read()

print(data)
