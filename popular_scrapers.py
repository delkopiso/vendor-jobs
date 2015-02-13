from base_scraper import BaseScraper
from BeautifulSoup import BeautifulSoup as BS
import html2text


class BellaNaijaScraper(BaseScraper):
    def __init__(self, db_collection):
        BaseScraper.__init__(self, api_id="arepnqw8", category="Popular", db_collection=db_collection,
                             logo="http://www.bellanaija.com/wp-content/themes/diamonds/images/bellanaija-mobile.png")

    def parse_title(self, piece):
        self.title = piece["title"]["text"].encode("utf-8")

    def parse_text_body(self, piece):
        entry_div = self.soup.findAll('div', {'class': 'entry-content'})
        entry_div_string = str(entry_div)
        entry_div_soup = BS(entry_div_string)
        entry_div_text = entry_div_soup.findAll('p')

        handler = html2text.HTML2Text()
        handler.ignore_links = True
        handler.ignore_images = True

        text_final = []

        for i in range(0, len(entry_div_text)):
            text = str(entry_div_text[i]).decode('utf-8')
            text_final.append(text)
        text = str(handler.handle("\n\n".join(text_final)).encode('utf-8'))

        #Cleaning Text
        text = text.split('\n\n')
        text = "".join(text)
        text = text.split('\n')
        text = "".join(text)
        text = text.split('**')
        self.body_text = "".join(text)

    def parse_cover_picture(self, piece):
        self.cover_picture = piece['coverPic']['src'].encode('utf-8')


class NdaniTVScraper(BaseScraper):
    def __init__(self, db_collection):
        BaseScraper.__init__(self, api_id="8ms0cfmi", category="Popular", db_collection=db_collection,
                             logo="http://ndani.tv/images/logo.png")

    def parse_title(self, piece):
        title = str(self.soup.findAll('h2', {'class': 'post-title'}))
        title = title.split('[')
        title = "".join(title)
        title = title.split(']')
        title = "".join(title)
        handler = html2text.HTML2Text()
        handler.ignore_links = True

        try:
            title.decode('utf-8')
            title = handler.handle(title)
        except:
            return

        title = title.split('##  ')
        title = "".join(title)
        title = title.split('\n')
        self.title = "".join(title)

    def parse_text_body(self, piece):
        entry_div = self.soup.findAll('div', {'class': 'copy clearfix'})
        entry_string = str(entry_div)
        content = BS(entry_string)
        p = content.findAll('p')
        p = str(p)
        p = p.split("/p>,")
        p = "/p>".join(p)
        p = p.split('[')
        p = "".join(p)
        p = p.split(']')
        p = "".join(p)
        handler = html2text.HTML2Text()
        handler.ignore_links = True
        try:
            p = p.decode('utf-8')
            p = handler.handle(p)
        except:
            return

        result = p.split('\n\n')

        text_list = []
        for i in range(0, len(result)):
            x = result[i].split('\n')
            x = " ".join(x)
            text_list.append(x)
        result = "".join(text_list)
        result = result.strip()
        self.body_text = result + self.cover_picture

    def parse_cover_picture(self, piece):
        vid = self.soup.findAll('li', {'class': 'post-image'})
        content = BS(str(vid))
        vid = str(content.findAll('iframe'))
        vid = vid.split('[')
        vid = "".join(vid)
        vid = vid.split(']')
        vid = "".join(vid)
        vid = vid.split('src="')
        vid = vid[1]
        vid = vid.split('" frameborder')
        vid = vid[0]
        vid = "![]http:" + vid
        self.cover_picture = vid


class RadarNGScraper(BaseScraper):
    def __init__(self, db_collection):
        BaseScraper.__init__(self, api_id="6g898ewm", category="Popular", db_collection=db_collection,
                             logo="http://static.radar.ng/wp-content/uploads/2014/05/logo-small2.png")

    def parse_title(self, piece):
        self.title = piece['title']['text'].encode('utf-8')

    def parse_text_body(self, piece):
        self.body_text = piece['text']['text'].encode('utf-8')

    def parse_cover_picture(self, piece):
        try:
            coverPic = str(self.soup.findAll('div', {'id': 'featured-image'}))
            coverPic = coverPic.split('src="')
            coverPic = coverPic[1]
            coverPic = coverPic.split('"')
            self.cover_picture = coverPic[0]
        except:
            return


class LindaIkejiScraper(BaseScraper):
    def __init__(self, db_collection):
        BaseScraper.__init__(self, api_id="3urqe5fa", category="Popular", db_collection=db_collection,
                             logo="")

    def parse_title(self, piece):
        self.title = piece['title']['text'].encode('utf-8')

    def parse_text_body(self, piece):
        text_div = str(self.soup.findAll('div', {'class': 'post-body entry-content'}))
        text_div = text_div.split("</div>")
        text_div = text_div[1]
        text_div = text_div.split('<')
        text = text_div[0]
        text = text.split('\n')
        self.body_text = "".join(text)

    def parse_cover_picture(self, piece):
        img_div = str(self.soup.findAll('div', {'class': 'post-body entry-content'}))
        img_div = BS(img_div)
        coverPic = str(img_div.findAll('img'))
        link = coverPic.split('src="')
        link = link[1]
        link = link.split('"')
        self.cover_picture = link[0]


class Y_NaijaScraper(BaseScraper):
    def __init__(self, db_collection):
        BaseScraper.__init__(self, api_id="2nf95wdg", category="Popular", db_collection=db_collection,
                             logo="http://ynaija.com/wp-content/uploads/2014/09/xynlogo.png")

    def parse_title(self, piece):
        self.title = piece['title']['text'].encode('utf-8')

    def parse_text_body(self, piece):
        self.body_text = piece['text'].encode('utf-8')

    def parse_cover_picture(self, piece):
        try:
            self.cover_picture = piece['coverPic']['src']
        except:
            return