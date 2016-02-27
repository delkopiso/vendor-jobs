import json
import urllib
import urllib2
import requests
from BeautifulSoup import BeautifulSoup as BS
import cStringIO



print "Started Test"

api_id = "149f2867-f608-41c2-9538-61bf0e4c7945"
site = "http%3A%2F%2Fpartyjollof.com%2F&&"
IMPORT_API_KEY = "5a2844a10ccb47deabeaa0417c4f054a89cfae07a6b1dd6a8d5f7b4ce0741e65b28d43c0b0bd992894a60c35c777aaf1ebc51ccd02f2632031353c7f12646e5a6b521fd5862b428bcd1afed2be474fd2"

results = json.load(urllib.urlopen("https://api.import.io/store/connector/"+api_id+"/_query?input=webpage/url:"+site+"_apikey="+IMPORT_API_KEY))

#print len(results['results'])
print "https://api.import.io/store/connector/"+api_id+"/_query?input=webpage/url:"+site+"_apikey="+IMPORT_API_KEY
print results['results'][5]['title/_text'].encode("utf-8")

for x in range(0,12):
	source_url = str(results['results'][x]['title']).encode("utf-8")
	#print source_url
	title = results['results'][x]['title/_text'].encode("utf-8")
	#print title
	#r = requests.get(source_url)
	#content = r.content
	#soup = BS(content)
	
	





	'''
	#Ventures
	
	try:
		div = str(soup.findAll('div',{'class':'td-post-featured-image'}))
		coverPic = div.split('src="')[1].split('" alt=')[0]
		print coverPic
	except:
		print("Goodbye")
	
	
	#WEdding Digest
	
	
	try:
		div = str(soup.findAll('div',{'class':'post-content entry-content cf'}))
		img =  div.split('<p><img')[1].split('" alt')[0].split('src="')[1]
		coverPic = img
		print coverPic
	except:
		print("Goodbye")


	
	#Made
	
	try:
        coverPic = str(results['results']['collection1'][count]['coverPic']['src'].encode("utf-8"))
        coverPic = coverPic.split("200x240-100x120")
        coverPic = "600x300".join(coverPic)
        return coverPic
    except:
        return ""

	#Wedding Digest
	
	try:
		div = str(soup.findAll('div',{'class':'post-entry'}))
		snip = div.split('data-lazy-src="')[1]
		coverPic = snip.split('" alt="')[0]
		print coverPic
	except:
		print("Skipped")


	#YabaLeft
	try:
		div = str(soup.findAll('div',{'class':'theiaPostSlider_slides'}))
		snip = div.split(' src="')[1]
		coverPic = snip.split('" alt="')[0]
		print coverPic
	except:
		print("Skipped")


	#Stears
	try:
		div = str(soup.findAll())
		img = str(str(div).split('src="')[2])
		coverPic = str(img.split('" class=')[0])
		print coverPic
	except:
		print("Skipped")

	#QZ

	try:
		div = str(soup.findAll('picture'))
		img = str(str(div).split('srcset="')[1])
		coverPic = str(img.split("?quality")[0])
		print coverPic
	except:
		print("Skipped")

	#9jaFoodie

	#div = str(soup.findAll('div',{'class':'portfolio-one-sidebar'}))
	#img = str(str(div).split('src="')[2])
	#img = str(img.split("?resize")[0])
	#print img

	#NotJustOK
	div = str(soup.findAll('div',{'class':'entry'}))
	img = str(str(div).split('src="')[1])
	coverPic = str(img.split('" alt')[0])

	#BeautyinLagos
	img = soup.findAll('div',{'class':'separator'})
	coverPic = str(img).split('src="')
	coverPic = coverPic[0]
	coverPic = str(coverPic).split('<a href="')
	coverPic = coverPic[1]
	coverPic = str(coverPic).split('" ')[0]
	print coverPic

	
	#9jaFoodie

	img = str(results['results']['collection2'][x ]['coverPic']['src'].encode("utf-8"))
	coverPic = str(img).split('?resize')
	coverPic = coverPic[0]
	print coverPic


	#Thisday
	img = soup.findAll('div',{'class':'img'})
	coverPic = str(img).split('src="')
	coverPic = coverPic[1]
	coverPic = str(coverPic).split('?max')
	coverPic = coverPic[0]
	print coverPic


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
