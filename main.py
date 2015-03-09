import os
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from pytz import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
import logging
from pymongo.mongo_client import MongoClient
from scraper import Scraper
from special_scraper import SaharaScraper, RadrScraper

logging.basicConfig()
ARTICLE_COLLECTION = "article"
scrapers = []


def define_scrapers(collection):
    # Gossip sources
    b_naij = Scraper("Bella Naija", api_id="arepnqw8", category="Gossip", db_collection=collection,
                     logo="http://www.bellanaija.com/wp-content/themes/diamonds/images/bellanaija-mobile.png")
    print "Adding " + b_naij.get_name() + " scraper..."
    scrapers.append(b_naij)
    # ndani = Scraper("Ndani TV", api_id="8ms0cfmi", category="Gossip", db_collection=collection,
    # logo="http://ndani.tv/images/logo.png")
    # print "Adding " + ndani.get_name() + " scraper..."
    # scrapers.append(ndani)
    y_naija_gossip = Scraper("Y Naija", api_id="2nf95wdg", category="Gossip", db_collection=collection,
                             logo="http://ynaija.com/wp-content/uploads/2014/05/logo.png")
    print "Adding " + y_naija_gossip.get_name() + " scraper..."
    scrapers.append(y_naija_gossip)
    pulse = Scraper("Pulse.ng", api_id="dnxrp1h6", category="Gossip", db_collection=collection,
                    logo="http://static.pulse.ng/resources/20150218-3ng/ver1-0/img/pulse_red.png")
    print "Adding " + pulse.get_name() + " scraper..."
    scrapers.append(pulse)
    radr_ng = RadrScraper("Radr.ng", api_id="6g898ewm", category="Gossip", db_collection=collection,
                           logo="http://www.radar.ng/wp-content/uploads/2014/05/logo.png")
    print "Adding " + radr_ng.get_name() + " scraper..."
    scrapers.append(radr_ng)

    # Headline sources
    today_ng_headlines = Scraper("Today NG", api_id="68dq8a2w", category="Headlines", db_collection=collection,
                                 logo="http://static.today.ng/wp-content/uploads/2015/01/logo.jpg")
    print "Adding " + today_ng_headlines.get_name() + " scraper..."
    scrapers.append(today_ng_headlines)
    vanguard_headlines = Scraper("Vanguard", api_id="abzmopk8", category="Headlines", db_collection=collection,
                                 logo="http://cdn1.vanguardngr.com/wp-content/uploads/2013/12/250x55xvanguardlogo.png.pagespeed.ic.WF70w5uJ9P.png")
    print "Adding " + vanguard_headlines.get_name() + " scraper..."
    scrapers.append(vanguard_headlines)
    y_naija_headlines = Scraper("Y Naija", api_id="e6jhynpm", category="Headlines", db_collection=collection,
                                logo="http://ynaija.com/wp-content/uploads/2014/05/logo.png")
    print "Adding " + y_naija_headlines.get_name() + " scraper..."
    scrapers.append(y_naija_headlines)
    sahara = SaharaScraper("Sahara Reporters", api_id="8wd4g63i", category="Headlines", db_collection=collection,
                           logo="http://saharareporters.com/sites/default/themes/sr_theme/images/layout/header/header-logo.png")
    print "Adding " + sahara.get_name() + " scraper..."
    scrapers.append(sahara)

    # Tech
    today_ng_tech = Scraper("Today NG", api_id="747byvlu", category="Tech", db_collection=collection,
                            logo="http://static.today.ng/wp-content/uploads/2014/09/logo.jpg")
    print "Adding " + today_ng_tech.get_name() + " scraper..."
    scrapers.append(today_ng_tech)
    tech_cabal = Scraper("Tech Cabal", api_id="3lfnkuxu", category="Tech", db_collection=collection,
                         logo="http://www.techcabal.com/wp-content/uploads/2013/09/tclogobig.png")
    print "Adding " + tech_cabal.get_name() + " scraper..."
    scrapers.append(tech_cabal)
    vanguard_tech = Scraper("Vanguard", api_id="e9qp7s1a", category="Tech", db_collection=collection,
                            logo="http://cdn1.vanguardngr.com/wp-content/uploads/2013/12/250x55xvanguardlogo.png.pagespeed.ic.WF70w5uJ9P.png")
    print "Adding " + vanguard_tech.get_name() + " scraper..."
    scrapers.append(vanguard_tech)

    # Business
    ventures = Scraper("Ventures Africa", api_id="7l5zbtl6", category="Business", db_collection=collection,
                       logo="http://www.ventures-africa.com/wp-content/uploads/2013/12/logo_web.png")
    print "Adding " + ventures.get_name() + " scraper..."
    scrapers.append(ventures)
    vanguard_business = Scraper("Vanguard", api_id="cskj1sxo", category="Business", db_collection=collection,
                                logo="http://cdn1.vanguardngr.com/wp-content/uploads/2013/12/250x55xvanguardlogo.png.pagespeed.ic.WF70w5uJ9P.png")
    print "Adding " + vanguard_business.get_name() + " scraper..."
    scrapers.append(vanguard_business)
    punch_biz = Scraper("Punch", api_id="bdid5uka", category="Business", db_collection=collection,
                        logo="http://punch.cdn.ng/wp-content/themes/punch/images/punch_logo.jpg")
    print "Adding " + punch_biz.get_name() + " scraper..."
    scrapers.append(punch_biz)


def run_scrapers():
    for scraper in scrapers:
        try:
            scraper.run()
        except Exception as e:
            print "Unexpected error:", e


def scrape():
    uri = os.environ.get('MONGOLAB_URI')
    db_connection = MongoClient(host=uri) if uri is not None else MongoClient()
    db = db_connection.get_default_database() if uri is not None else db_connection['vendor']
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
    executors = {'processpool': ProcessPoolExecutor(max_workers=1)}
    scheduler.configure(jobstores=jobstores, executors=executors, timezone=timezone('US/Eastern'))
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.add_job(scrape, trigger='cron', minute='*/2')
    print 'Scrape job has been added'
    scheduler.start()
    print 'Scheduler has been started'
