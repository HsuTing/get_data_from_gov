import urllib2
import time

def get_data(url):
	for i in range(0, len(url)):
		temptime = time.localtime(time.time())
		output = str(temptime.tm_year) + '_' + str(temptime.tm_mon) + '_' + str(temptime.tm_mday) + '_' + str(temptime.tm_hour) + '_' + str(temptime.tm_min) + '_' + str(temptime.tm_sec)
		temp = 'http://opendata.epa.gov.tw/ws/Data/' + url[i] + '/?$format=json'
		content = urllib2.urlopen(temp)
		data = content.read()
		fout = open(output + '_' + url[i] + '.json', 'w+')
		fout.write(data)
