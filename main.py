import os
from pytz import utc
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ProcessPoolExecutor

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
    # 'coalesce': True
}


# from pymongo.mongo_client import MongoClient
# from popular_scrapers import BellaNaijaScraper
# from tech_scrapers import TechCabalScraper
#
# DB_NAME = "vendor"
# ARTICLE_COLLECTION = "article"
# scrapers = []
#
#
# def define_scrapers(collection):
#     b_naij = BellaNaijaScraper(collection)
#     scrapers.append(b_naij)
#     tech_cabal = TechCabalScraper(collection)
#     scrapers.append(tech_cabal)
#
#
# def run_scrapers():
#     for scraper in scrapers:
#         scraper.run()
#
#
# @scheduler.scheduled_job('cron', day_of_week='mon-sun', hour=23, id='main_scrape_job')
# def main_job():
#     uri = os.environ.get('MONGOLAB_URI')
#     db_connection = MongoClient(host=uri) if uri is not None else MongoClient()
#     db = db_connection[DB_NAME]
#     collection = db[ARTICLE_COLLECTION]
#     define_scrapers(collection)
#     run_scrapers()


@scheduler.interval_schedule(seconds=3, id='test_timer')
def timed_job():
    print 'This job is run every three minutes.'


scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
scheduler.start()
print "Scheduler started"

while __name__ == '__main__':
    pass