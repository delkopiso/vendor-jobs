import os
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from apscheduler.jobstores.memory import MemoryJobStore
import logging
from pymongo.mongo_client import MongoClient
from popular_scrapers import BellaNaijaScraper
from tech_scrapers import TechCabalScraper

logging.basicConfig()
ARTICLE_COLLECTION = "article"
scrapers = []


def define_scrapers(collection):
    print "Defining Bella Naija scraper..."
    b_naij = BellaNaijaScraper(collection)
    scrapers.append(b_naij)
    print "Defining Tech Cabal scraper..."
    tech_cabal = TechCabalScraper(collection)
    scrapers.append(tech_cabal)


def run_scrapers():
    for scraper in scrapers:
        scraper.run()


def scrape():
    uri = os.environ.get('MONGOLAB_URI')
    db_connection = MongoClient(host=uri) if uri is not None else MongoClient()
    db = db_connection.get_default_database()
    collection = db[ARTICLE_COLLECTION]
    define_scrapers(collection)
    print "Running scrapers..."
    run_scrapers()


if __name__ == '__main__':
    # url = os.environ.get('DATABASE_URL')
    jobstores = {'default': MemoryJobStore()}
    # if url != None:
    #     jobstores = {
    #         'default': SQLAlchemyJobStore(url=url)
    #     }
    # else:
    #     jobstores = {
    #         'default': MemoryJobStore()
    #     }
    executors = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    scheduler = BackgroundScheduler()
    scheduler.configure(jobstores=jobstores, executors=executors, timezone=timezone('US/Eastern'))
    scheduler.add_job(scrape, trigger='cron', hour='*', day='*', month='*')
    print 'Scrape job has been scheduled'

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass