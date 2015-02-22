import os
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from pytz import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
#from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
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


def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    url = os.environ.get('DATABASE_URL')
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
        'processpool': ProcessPoolExecutor(max_workers=1)
    }
    scheduler.configure(jobstores=jobstores, executors=executors, timezone=timezone('US/Eastern'))
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()

    print 'Scheduler has been started'
    scheduler.add_job(scrape, trigger='cron', minute='*')
    print 'Scrape job has been added'
