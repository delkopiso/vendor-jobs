from pymongo import Connection
from popular_scrapers import BellaNaijaScraper
from tech_scrapers import TechCabalScraper

DB_NAME = "vendor"
ARTICLE_COLLECTION = "article"

scrapers = []


def define_scrapers():
    b_naij = BellaNaijaScraper(collection)
    scrapers.append(b_naij)
    tech_cabal = TechCabalScraper(collection)
    scrapers.append(tech_cabal)


def run_scrapers():
    for scraper in scrapers:
        scraper.run()


if __name__ == "__main__":
    db_connection = Connection()
    db = db_connection[DB_NAME]
    collection = db[ARTICLE_COLLECTION]
    define_scrapers()
    run_scrapers()
