import datetime
import requests
from scraper import Scraper
from BeautifulSoup import BeautifulSoup as BS


class SaharaScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        content_div = soup.findAll('div', {'class': 'story-content'})
        content = BS(str(content_div))
        images = content.findAll('img')
        pictures = []
        cover_picture = ""
        for x in range(0, len(images)):
            b = str(images[x])
            b = b.split('src="')
            b = b[1]
            b = b.split('"')
            b = b[0]
            pictures.append(b)
        if len(pictures) > 0:
            cover_picture = pictures[0]
        if len(cover_picture) < 3:
            cover_picture = ""
        return cover_picture

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class RadrScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            cover_picture = str(soup.findAll('div', {'id': 'featured-image'}))
            cover_picture = cover_picture.split('src="')
            cover_picture = cover_picture[1]
            cover_picture = cover_picture.split('"')
            return cover_picture[0]
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class venturesScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            img = soup.findAll('section',{'class':'top-story banner type--post'})
            img = str(img).split('320w')[1].split('640w')[0]
            coverPic = ("http://" + str(img.split('jpg')[0]) + "jpg").split('http://, ')[1]
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class guardScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            img = soup.findAll('div',{'class':'cotent-text'})
            content = BS(str(img))
            images = str(content.findAll('img'))
            coverPic = images.split('src="')
            coverPic = coverPic[1]
            coverPic = coverPic.split('" alt')
            coverPic = coverPic[0]
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class punchScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            div = str(soup.findAll('div',{'class':'td-post-featured-image'}))
            coverPic = div.split('src="')[1].split('" alt=')[0]
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["title"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class itnScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            img = soup.findAll('div',{'id':'content'})
            coverPic = str(img).split('src="')
            coverPic = coverPic[1]
            coverPic = str(coverPic).split('" alt')
            coverPic = coverPic[0]
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class todayScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            img = soup.findAll('div',{'class':'post-featured'})
            coverPic = str(img).split('src="')
            coverPic = coverPic[1]
            coverPic = str(coverPic).split('" class')
            coverPic = coverPic[0]
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class madeScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, count, piece):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            coverPic = str(piece['coverPic']['src'].encode("utf-8"))
            coverPic = coverPic.split("200x240-100x120")
            coverPic = "600x300".join(coverPic)
            return coverPic
        except Exception as e:
            print "Unexpected error:", e, "with Made Scraper "
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, count, piece)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class thisdayScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            img = soup.findAll('div',{'class':'img'})
            coverPic = str(img).split('src="')
            coverPic = coverPic[1]
            coverPic = str(coverPic).split('?max')
            coverPic = coverPic[0]
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class naija_food_Scraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, results):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            div = str(soup.findAll('div',{'class':'portfolio-one-sidebar'}))
            img = str(str(div).split('src="')[2])
            coverPic = str(img.split("?resize")[0])
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, results)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class qzScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, results):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            div = str(soup.findAll('picture'))
            img = str(str(div).split('srcset="')[1])
            coverPic = str(img.split("?quality")[0])
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, results)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class hqScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, results):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            div = str(soup.findAll('div',{'id':'featured-image'}))
            img = str(str(div).split('src="')[1])
            coverPic = str(img.split(".jpg")[0])+".jpg"
            coverPic = str(str(coverPic).split('" />')[0])
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, results)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class beautyScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, results):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            img = soup.findAll('div',{'class':'separator'})
            coverPic = str(img).split('src="')
            coverPic = coverPic[0]
            coverPic = str(coverPic).split('<a href="')
            coverPic = coverPic[1]
            coverPic = str(coverPic).split('" ')[0]
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, results)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class stearsScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, results):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            div = str(soup.findAll('div',{'class':'w-section article-image'}))            
            img = str(str(div).split('src="')[2])
            coverPic = str(img.split('" class=')[0])
            coverPic = "http://www.stearsng.com/"+coverPic
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, results)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class wdigestScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, results):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            div = str(soup.findAll('div',{'class':'post-content entry-content cf'}))
            img =  div.split('<p><img')[1].split('" alt')[0].split('src="')[1]
            coverPic = img
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, results)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class yabaLeftScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, results):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            div = str(soup.findAll('div',{'class':'theiaPostSlider_slides'}))
            snip = div.split(' src="')[1]
            coverPic = snip.split('" alt="')[0]
            return coverPic
        except:
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, results)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1

class styleDocScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, count, piece):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            coverPic = str(piece['coverPic']['src'].encode("utf-8"))
            coverPic = coverPic.split("?resize")
            coverPic = coverPic[0]
            return coverPic
        except Exception as e:
            print "Unexpected error:", e, "with Style Doctor Scraper"
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, count, piece)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class lagosStreetScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, count, piece):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            div = str(soup.findAll('img',{'border':'0'})[4])
            coverPic = div.split('src="')[1].split('"')[0]
            return coverPic
        except Exception as e:
            print "Unexpected error:", e, "with Lagos Street Style"
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, count, piece)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


class nairametricsScraper(Scraper):
    def __init__(self, name, api_id, region, category, db_collection, logo=""):
        Scraper.__init__(self, name, api_id, region, category, db_collection, logo)

    def retrieve_picture(self, source, count, piece):
        r = requests.get(source)
        content = r.content
        soup = BS(content)
        try:
            coverPic = str(piece['coverPic']['src'].encode("utf-8"))
            coverPic = coverPic.split("?resize")
            coverPic = coverPic[0]
            return coverPic
        except Exception as e:
            print "Unexpected error:", e, "with Nairametrics Scraper"
            return ""

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            piece = results["results"]["collection1"][count]
            title = piece["title"]["text"].encode("utf-8")
            source = str(piece["title"]["href"])
            cover_pic = self.retrieve_picture(source, count, piece)
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": title,
                    "source": source,
                    "coverPic": cover_pic,
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1


