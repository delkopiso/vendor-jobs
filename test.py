import json
import urllib
import urllib2
import requests
from BeautifulSoup import BeautifulSoup as BS
import cStringIO



print "Started Test"
results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/5zucxtg0?apikey=b08304e70880d8872c8732a6c32985df&kimlimit=5"))

for x in range(0,5):
	source_url = str(results['results']['collection1'][x ]['title']['href'])
	title = str(results['results']['collection1'][x ]['title']['text'].encode("utf-8"))
	print title
	r = requests.get(source_url)
	content = r.content
	soup = BS(content)
	
	
	#Ventures
	
	try:
		img = soup.findAll('a',{'class':'post_image page_margin_top prettyPhoto'})
		if len(img) == 0:
			img = soup.findAll('a',{'class':'post_image prettyPhoto'})
		
		img = str(img).split('href="')[1].split('" title')[0]
		coverPic = img
		print coverPic
		
	except:
		print("Goodbye")
		


	
	


	'''

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
