from base_scraper import BaseScraper


class TodayNGScraper(BaseScraper):
    def __init__(self, db_collection):
        BaseScraper.__init__(self, api_id="2yio1io4", category="Tech", db_collection=db_collection,
                             logo="http://static.today.ng/wp-content/uploads/2014/09/logo.jpg")

    def parse_title(self, piece):
        self.title = piece["title"]["text"].encode("utf-8")

    def parse_text_body(self, piece):
        self.body_text = piece['text']

    def parse_cover_picture(self, piece):
        self.cover_picture = piece['coverPic']['src']


class TechCabalScraper(BaseScraper):
    def __init__(self, db_collection):
        BaseScraper.__init__(self, api_id="3lfnkuxu", category="Tech", db_collection=db_collection,
                             logo="http://www.techcabal.com/wp-content/uploads/2013/09/tclogobig.png")

    def parse_title(self, piece):
        self.title = piece['title']['text'].encode('utf-8')

    def parse_text_body(self, piece):
        print piece['text']
        self.body_text = piece['text']

    def parse_cover_picture(self, piece):
        self.cover_picture = piece['pic']['src'].encode('utf-8')