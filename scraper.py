import json
import os
import urllib
import datetime

KIMONO_API_KEY = os.environ.get('KIMONO_API_KEY')


class Scraper:
    def __init__(self, name, api_id, category, db_collection, logo=""):
        self.mix_index = 0
        self.name = name
        self.api_id = api_id
        self.category = category
        self.logo = logo
        self.db_collection = db_collection

    def get_name(self):
        return self.name

    def load_data(self):
        results = json.load(
            urllib.urlopen("https://www.kimonolabs.com/api/"+self.api_id+"?apikey="+KIMONO_API_KEY)
        )
        return results

    def run(self):
        results = self.load_data()
        count = 0
        while count < results["count"]:
            try:
                piece = results["results"]["collection1"][count]
                source = piece["title"]["href"]
                if self.db_collection.find({"source": source}).count() != 0:
                    return
                else:
                    self.db_collection.insert({
                        "title": piece["title"]["text"],
                        "source": source,
                        "coverPic": piece["coverPic"],
                        "section": self.category,
                        "logo": self.logo,
                        "popularity": 0,
                        "mixIndex": self.mix_index,
                        "dateAdded": datetime.datetime.now()
                    })
                self.mix_index = count % results["count"]
                count += 1
            except Exception as e:
                print e.message, e.args