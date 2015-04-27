import urllib2

def get_data(url):
	for i in range(0, len(url)):
		temp = 'http://opendata.epa.gov.tw/ws/Data/' + url[i] + '/?$format=json'
		content = urllib2.urlopen(temp)
		data = content.read()
		fout = open(url[i] + '.json', 'w+')
		fout.write(data)
