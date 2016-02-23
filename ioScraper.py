import json
import os
import urllib
import datetime
import ssl

IMPORT_API_KEY = "5a2844a10ccb47deabeaa0417c4f054a89cfae07a6b1dd6a8d5f7b4ce0741e65b28d43c0b0bd992894a60c35c777aaf1ebc51ccd02f2632031353c7f12646e5a6b521fd5862b428bcd1afed2be474fd2"
limit = "5"


class ioScraper:
    def __init__(self, name, site, api_id, region, category, db_collection, logo=""):
        self.mix_index = 0
        self.name = name
        self.site = site
        self.api_id = api_id
        self.region = region
        self.category = category
        self.logo = logo
        self.db_collection = db_collection

    def get_name(self):
        return self.name

    def load_data(self):
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        results = json.load(
            urllib.urlopen("https://api.import.io/store/connector/"+self.api_id+"/_query?input=webpage/url:"+self.site+"_apikey="+IMPORT_API_KEY, context=gcontext)
        )
        
        return results

    def run(self):
        results = self.load_data()
        count = 0
        while count < limit:
            piece = results["results"][count]
            source = piece["title"]
            if self.db_collection.find({"source": source}).count() != 0:
                return
            else:
                self.db_collection.insert({
                    "title": piece["title/_text"],
                    "source": source,
                    "coverPic": piece["coverpic"],
                    "region": self.region,
                    "section": self.category,
                    "logo": self.logo,
                    "popularity": 0,
                    "mixIndex": self.mix_index,
                    "dateAdded": datetime.datetime.now()
                })
            self.mix_index = count % results["count"]
            count += 1
