import os
from pytz import timezone
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
import logging
from pymongo.mongo_client import MongoClient
from popular_scrapers import BellaNaijaScraper
from tech_scrapers import TechCabalScraper

logging.basicConfig()
DB_NAME = "vendor"
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
    print "Starting scraper..."
    print "Fetching MONGOLAB_URI..."
    uri = os.environ.get('MONGOLAB_URI')
    print "Acquired {0} from the system as the connection string".format(uri)
    db_connection = MongoClient(host=uri) if uri is not None else MongoClient()
    print "Database connection established"
    db = db_connection[DB_NAME]
    collection = db[ARTICLE_COLLECTION]
    print "Defining scrapers..."
    define_scrapers(collection)
    print "Running each scraper..."
    run_scrapers()


# def tick():
#     print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    url = os.environ.get('DATABASE_URL')
    jobstores = {}
    if url != None:
        jobstores = {
            'default': SQLAlchemyJobStore(url=url)
        }
    else:
        jobstores = {
            'default': MemoryJobStore()
        }
    executors = {
        'processpool': ProcessPoolExecutor(max_workers=1)
    }
    job_defaults = {
        'coalesce': True
    }
    scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=timezone('US/Eastern'))
    # scheduler.add_job(tick, 'interval', seconds=3, id='test_timer_tick')
    scheduler.add_job(scrape, 'interval', minutes=3, start_date='2015-2-13 03:58')#day_of_week='mon-sun', hour=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass