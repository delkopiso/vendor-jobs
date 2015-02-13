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
    b_naij = BellaNaijaScraper(collection)
    scrapers.append(b_naij)
    tech_cabal = TechCabalScraper(collection)
    scrapers.append(tech_cabal)


def run_scrapers():
    for scraper in scrapers:
        scraper.run()


def scrape():
    uri = os.environ.get('MONGOLAB_URI')
    db_connection = MongoClient(host=uri) if uri is not None else MongoClient()
    db = db_connection[DB_NAME]
    collection = db[ARTICLE_COLLECTION]
    define_scrapers(collection)
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
    scheduler.add_job(scrape, 'cron', minute=5)#day_of_week='mon-sun', hour=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass