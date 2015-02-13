import json
import urllib
import requests
from BeautifulSoup import BeautifulSoup as BS

KIMONO_API_KEY = "b08304e70880d8872c8732a6c32985df"


class BaseScraper:
    def __init__(self, api_id, category, db_collection, logo=""):
        self.api_id = api_id
        self.category = category
        self.logo = logo
        self.results = None
        self.soup = None
        self.title = ""
        self.body_text = ""
        self.source_url = ""
        self.cover_picture = ""
        self.db_collection = db_collection

    def load_data(self):
        self.results = json.load(
            urllib.urlopen("https://www.kimonolabs.com/api/"+self.api_id+"?apikey="+KIMONO_API_KEY)
        )

    def parse_source_url(self, piece):
        self.source_url = str(piece["title"]["href"]).encode('utf-8')

    def parse_title(self, piece):
        raise NotImplementedError

    def parse_text_body(self, piece):
        raise NotImplementedError

    def parse_cover_picture(self, piece):
        raise NotImplementedError

    def load_soup_object(self):
        request = requests.get(self.source_url)
        content = request.content
        self.soup = BS(content)

    def push_to_database(self):
        self.db_collection.insert({
            "title": self.title,
            "text": self.body_text,
            "source": self.source_url,
            "coverPic": self.cover_picture,
            "section": self.category,
            "logo": self.logo,
            "popularity": 0
        })

    def run(self):
        self.load_data()
        count = 0
        while count < self.results["count"]:
            piece = self.results["results"]["collection1"][count]
            self.parse_source_url(piece)
            self.load_soup_object()
            self.parse_title(piece)
            self.parse_cover_picture(piece)
            self.parse_text_body(piece)
            self.push_to_database()
            count += 1
