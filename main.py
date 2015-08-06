import os
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from pytz import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
import logging
from pymongo.mongo_client import MongoClient
from scraper import Scraper
from special_scraper import SaharaScraper, RadrScraper, venturesScraper, guardScraper, punchScraper, itnScraper, todayScraper

logging.basicConfig()
ARTICLE_COLLECTION = "article"
scrapers = []


def define_scrapers(collection):
    


    # Gossip sources
    bnaij_gossip = Scraper("Bella Naija", api_id="5u0c0qoi", region="nigeria", category="Gossip", db_collection=collection,
                     logo="http://www.bellanaija.com/wp-content/themes/diamonds/images/bellanaija-mobile.png")
    print "Adding " + bnaij_gossip.get_name() + " scraper..."
    scrapers.append(bnaij_gossip)
    
    pulse = Scraper("Pulse.ng", api_id="dnxrp1h6", region="nigeria", category="Gossip", db_collection=collection,
                    logo="http://static.pulse.ng/resources/20150218-3ng/ver1-0/img/logo_print.gif")
    print "Adding " + pulse.get_name() + " scraper..."
    scrapers.append(pulse)
    
    sixty_gossip = Scraper("360 Gossip", api_id="3007ai6g", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://www.360nobs.com/wp-content/uploads/2015/04/360nobs_logo.png")
    print "Adding " + sixty_gossip.get_name() + " scraper..."
    scrapers.append(sixty_gossip)
    
    ynaij_gossip = Scraper("Ynaija Gossip", api_id="6pma1t9s", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://ynaija.com/wp-content/uploads/2014/05/logo.png")
    print "Adding " + ynaij_gossip.get_name() + " scraper..."
    scrapers.append(ynaij_gossip)

    ventures_gossip = venturesScraper("Ventures Africa", api_id="3w6fsfew", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://www.ventures-africa.com/wp-content/uploads/2013/12/logo_web.png")
    print "Adding " + ventures_gossip.get_name() + " scraper..."
    scrapers.append(ventures_gossip)
    
    zikoko_gossip = Scraper("Zikoko", api_id="6tyylw1s", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://zikoko.com/wp-content/uploads/2015/07/logo-300x92.png")
    print "Adding " + zikoko_gossip.get_name() + " scraper..."
    scrapers.append(zikoko_gossip)

    today_gossip = todayScraper("Today", api_id="98sgndus", region="nigeria", category="Gossip", db_collection=collection,
                            logo="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTjEw9FCJP0MgaACcs95m9HDYx4IHxm7bjkGWtkJgohhiO6yuitGKDiIIo")
    print "Adding " + today_gossip.get_name() + " scraper..."
    scrapers.append(today_gossip)
    


    # Headline sources
    
    today_headlines = Scraper("Today", api_id="b9lqpkyy", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTjEw9FCJP0MgaACcs95m9HDYx4IHxm7bjkGWtkJgohhiO6yuitGKDiIIo")
    print "Adding " + today_headlines.get_name() + " scraper..."
    scrapers.append(today_headlines)
    
    vanguard_headlines = Scraper("Vanguard", api_id="abzmopk8", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://cdn1.vanguardngr.com/wp-content/uploads/2013/12/250x55xvanguardlogo.png.pagespeed.ic.WF70w5uJ9P.png")
    print "Adding " + vanguard_headlines.get_name() + " scraper..."
    scrapers.append(vanguard_headlines)
    y_naija_headlines = Scraper("Y Naija", api_id="e6jhynpm", region="nigeria", category="Headlines", db_collection=collection,
                                logo="http://ynaija.com/wp-content/uploads/2014/05/logo.png")
    print "Adding " + y_naija_headlines.get_name() + " scraper..."
    scrapers.append(y_naija_headlines)
    sahara = Scraper("Sahara Reporters", api_id="5ih3db3a", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://saharareporters.com/sites/default/themes/sr_theme/images/layout/header/header-logo.png")
    print "Adding " + sahara.get_name() + " scraper..."
    scrapers.append(sahara)
    
    premium = Scraper("Premium Times", api_id="4r6sdgjm", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://media.premiumtimesng.com/wp-content/themes/PTN/images/176x64xptn-logo.png.pagespeed.ic.AedNv1evLn.png")
    print "Adding " + premium.get_name() + " scraper..."
    scrapers.append(premium)

    guard_head = guardScraper("Guardian Headlines", api_id="egzuf672", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://newngrguardiannewscom.c.presscdn.com/wp-content/uploads/2015/03/Guardian-Logo4501.jpg")
    print "Adding " + guard_head.get_name() + " scraper..."
    scrapers.append(guard_head)

    


    # Tech
    today_tech = Scraper("Today", api_id="2f7vilp6", region="nigeria", category="Tech", db_collection=collection,
                            logo="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTjEw9FCJP0MgaACcs95m9HDYx4IHxm7bjkGWtkJgohhiO6yuitGKDiIIo")
    print "Adding " + today_tech.get_name() + " scraper..."
    scrapers.append(today_tech)

    tech_cabal = Scraper("Tech Cabal", api_id="4bsxr58e", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://www.techcabal.com/wp-content/uploads/2013/09/tclogobig.png")
    print "Adding " + tech_cabal.get_name() + " scraper..."
    scrapers.append(tech_cabal)

    vanguard_tech = Scraper("Vanguard", api_id="e9qp7s1a", region="nigeria", category="Tech", db_collection=collection,
                            logo="http://cdn1.vanguardngr.com/wp-content/uploads/2013/12/250x55xvanguardlogo.png.pagespeed.ic.WF70w5uJ9P.png")
    print "Adding " + vanguard_tech.get_name() + " scraper..."
    scrapers.append(vanguard_tech)

    techpoint = Scraper("Techpoint", api_id="490y6x36", region="nigeria", category="Tech", db_collection=collection,
                        logo="http://techpoint.ng/wp-content/uploads/2014/05/Techpoint_web_logo.png")
    print "Adding " + techpoint.get_name() + " scraper..."
    scrapers.append(techpoint)

    ventures_tech = Scraper("Ventures Africa", api_id="bu960i24", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://www.ventures-africa.com/wp-content/uploads/2013/12/logo_web.png")
    print "Adding " + ventures_tech.get_name() + " scraper..."
    scrapers.append(ventures_tech)
    
    ventures_tech_long = venturesScraper("Ventures Africa", api_id="2dlebr7k", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://www.ventures-africa.com/wp-content/uploads/2013/12/logo_web.png")
    print "Adding " + ventures_tech_long.get_name() + " scraper..."
    scrapers.append(ventures_tech_long)

    it_news = itnScraper("IT News Africa", api_id="1youwujk", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://www.itnewsafrica.com/wp-content/uploads/2013/08/ITNewsAfrica_logo.gif")
    print "Adding " + it_news.get_name() + " scraper..."
    scrapers.append(it_news)

    ms_techy = Scraper("Miss Techy", api_id="an3p00uy", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://misstechy.com/wp-content/uploads/2015/05/misstechy-header-logo.jpg")
    print "Adding " + ms_techy.get_name() + " scraper..."
    scrapers.append(ms_techy)
    
    


    # Business
    ventures = Scraper("Ventures Africa", api_id="6vo0hr5a", region="nigeria", category="Business", db_collection=collection,
                       logo="http://www.ventures-africa.com/wp-content/uploads/2013/12/logo_web.png")
    print "Adding " + ventures.get_name() + " scraper..."
    scrapers.append(ventures)
    
    ventures_biz_long = venturesScraper("Ventures Africa", api_id="bbudi886", region="nigeria", category="Business", db_collection=collection,
                       logo="http://www.ventures-africa.com/wp-content/uploads/2013/12/logo_web.png")
    print "Adding " + ventures_biz_long.get_name() + " scraper..."
    scrapers.append(ventures_biz_long)
    
    vanguard_business = Scraper("Vanguard", api_id="cskj1sxo", region="nigeria", category="Business", db_collection=collection,
                                logo="http://cdn1.vanguardngr.com/wp-content/uploads/2013/12/250x55xvanguardlogo.png.pagespeed.ic.WF70w5uJ9P.png")
    print "Adding " + vanguard_business.get_name() + " scraper..."
    scrapers.append(vanguard_business)
    
    punch_biz = punchScraper("Punch", api_id="bdid5uka", region="nigeria", category="Business", db_collection=collection,
                        logo="http://punch.cdn.ng/wp-content/themes/punch/images/punch_logo.jpg")
    print "Adding " + punch_biz.get_name() + " scraper..."
    scrapers.append(punch_biz)
    
    premium_biz = Scraper("Premium Times", api_id="8lc0dzni", region="nigeria", category="Business", db_collection=collection,
                           logo="http://media.premiumtimesng.com/wp-content/themes/PTN/images/176x64xptn-logo.png.pagespeed.ic.AedNv1evLn.png")
    print "Adding " + premium_biz.get_name() + " scraper..."
    scrapers.append(premium_biz)

    today_biz = Scraper("Today", api_id="ah2kx1zc", region="nigeria", category="Business", db_collection=collection,
                                 logo="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTjEw9FCJP0MgaACcs95m9HDYx4IHxm7bjkGWtkJgohhiO6yuitGKDiIIo")
    print "Adding " + today_biz.get_name() + " scraper..."
    scrapers.append(today_biz)

    guard_biz = guardScraper("Guardian Headlines", api_id="egzuf672", region="nigeria", category="Business", db_collection=collection,
                           logo="http://newngrguardiannewscom.c.presscdn.com/wp-content/uploads/2015/03/Guardian-Logo4501.jpg")
    print "Adding " + guard_biz.get_name() + " scraper..."
    scrapers.append(guard_biz)
    


def run_scrapers():
    for scraper in scrapers:
        try:
            scraper.run()
        except Exception as e:
            print "Unexpected error:", e, "with ", scraper.get_name()


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
    scheduler.add_job(scrape, trigger='cron', hour='*')
    print 'Scrape job has been added'
    scheduler.start()
    print 'Scheduler has been started'
