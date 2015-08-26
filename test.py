import json
import urllib
import urllib2
import requests
from BeautifulSoup import BeautifulSoup as BS
import html2text
import cStringIO



print "Started Test"
results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/4thturvi?apikey=b08304e70880d8872c8732a6c32985df"))

for x in range(0,5):
	source_url = str(results['results']['collection1'][x ]['title']['href'])
	title = str(results['results']['collection1'][x ]['title']['text'])
	r = requests.get(source_url)
	content = r.content
	soup = BS(content)
	
	
	#Thisday
	img = soup.findAll('div',{'class':'img'})
	coverPic = str(img).split('src="')
	coverPic = coverPic[1]
	coverPic = str(coverPic).split('?max')
	coverPic = coverPic[0]
	print coverPic
	


	'''
	#Punch
	img = soup.findAll('div',{'class':'story-featured-image'})
	coverPic = str(img).split('src="')
	coverPic = coverPic[1]
	coverPic = str(coverPic).split('" class')
	coverPic = coverPic[0]
	print coverPic
	'''

	'''
	content = BS(str(img))
	images = str(content.findAll('img'))
	coverPic = str(images.split(' 3072w')[0])
	coverPic = str(coverPic.split(', ')[len(images.split(' 3072w'))+2])
	print coverPic
	'''
	'''
	#guardian 
	img = soup.findAll('div',{'class':'cotent-text'})
	content = BS(str(img))
	images = str(content.findAll('img'))
	coverPic = images.split('src="')
	coverPic = coverPic[1]
	coverPic = coverPic.split('" alt')
	coverPic = coverPic[0]
	'''

	'''
	#New_ventures
	img = soup.findAll('section',{'class':'top-story banner type--post'})
	content = BS(str(img))
	images = str(content.findAll('img'))
	coverPic = str(images.split(' 3072w')[0])
	coverPic = str(coverPic.split(', ')[len(images.split(' 3072w'))+2])
	'''
