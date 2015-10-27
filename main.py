import os
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from pytz import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
import logging
from pymongo.mongo_client import MongoClient
from scraper import Scraper
from special_scraper import SaharaScraper, RadrScraper, venturesScraper, guardScraper, punchScraper, itnScraper, todayScraper, madeScraper, thisdayScraper

logging.basicConfig()
ARTICLE_COLLECTION = "article"
scrapers = []


def define_scrapers(collection):
    


    # Gossip sources
    
    bnaij_gossip = Scraper("Bella Naija Gossip", api_id="5u0c0qoi", region="nigeria", category="Gossip", db_collection=collection,
                     logo="http://www.bellanaija.com/wp-content/themes/diamonds/images/bellanaija-mobile.png")
    print "Adding " + bnaij_gossip.get_name() + " scraper..."
    scrapers.append(bnaij_gossip)
    
    pulse = Scraper("Pulse Gossip", api_id="dnxrp1h6", region="nigeria", category="Gossip", db_collection=collection,
                    logo="http://s20.postimg.org/gg4cv2njd/pulset.png")
    print "Adding " + pulse.get_name() + " scraper..."
    scrapers.append(pulse)
    
    sixty_gossip = Scraper("360 Gossip", api_id="3007ai6g", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://www.360nobs.com/wp-content/uploads/2015/04/360nobs_logo.png")
    print "Adding " + sixty_gossip.get_name() + " scraper..."
    scrapers.append(sixty_gossip)
    

    ynaij_gossip = Scraper("Ynaija Gossip", api_id="acbiv2i8", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://ynaija.com/wp-content/uploads/2015/08/ynaija-logo.png")
    print "Adding " + ynaij_gossip.get_name() + " scraper..."
    scrapers.append(ynaij_gossip)

    ventures_gossip = venturesScraper("Ventures Africa Gossip", api_id="3w6fsfew", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/f4wlmlrxl/Screen_Shot_2015_10_24_at_10.png")
    print "Adding " + ventures_gossip.get_name() + " scraper..."
    scrapers.append(ventures_gossip)
    
    zikoko_gossip = Scraper("Zikoko Gossip", api_id="6tyylw1s", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://zikoko.com/wp-content/uploads/2015/07/logo-300x92.png")
    print "Adding " + zikoko_gossip.get_name() + " scraper..."
    scrapers.append(zikoko_gossip)

    today_gossip = todayScraper("Today Gossip", api_id="98sgndus", region="nigeria", category="Gossip", db_collection=collection,
                            logo="http://s20.postimg.org/mv7z5hjn1/today.png")
    print "Adding " + today_gossip.get_name() + " scraper..."
    scrapers.append(today_gossip)
    


    # Headline sources
    
    today_headlines = Scraper("Today Headlines", api_id="b9lqpkyy", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/mv7z5hjn1/today.png")
    print "Adding " + today_headlines.get_name() + " scraper..."
    scrapers.append(today_headlines)
    
    vanguard_headlines = Scraper("Vanguard Headlines", api_id="abzmopk8", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/lxrwlrcfh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_headlines.get_name() + " scraper..."
    scrapers.append(vanguard_headlines)
    

    y_naija_headlines = Scraper("Y Naija Headlines", api_id="8172f0f2", region="nigeria", category="Headlines", db_collection=collection,
                                logo="http://ynaija.com/wp-content/uploads/2015/08/ynaija-logo.png")
    print "Adding " + y_naija_headlines.get_name() + " scraper..."
    scrapers.append(y_naija_headlines)

    
    sahara = Scraper("Sahara Headlines", api_id="5ih3db3a", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://saharareporters.com/sites/default/themes/sr_theme/images/layout/header/header-logo.png")
    print "Adding " + sahara.get_name() + " scraper..."
    scrapers.append(sahara)
    
    premium = Scraper("Premium Headlines", api_id="4r6sdgjm", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://media.premiumtimesng.com/wp-content/themes/PTN/images/176x64xptn-logo.png.pagespeed.ic.AedNv1evLn.png")
    print "Adding " + premium.get_name() + " scraper..."
    scrapers.append(premium)

    guard_head = guardScraper("Guardian Headlines", api_id="egzuf672", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://newngrguardiannewscom.c.presscdn.com/wp-content/uploads/2015/03/Guardian-Logo4501.jpg")
    print "Adding " + guard_head.get_name() + " scraper..."
    scrapers.append(guard_head)

    thisday_head = thisdayScraper("Thisday Headlines", api_id="4thturvi", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://cdn.akamai.thisdaylive.com/0bef99d6-acf5-4e2c-9779-8fa02ba3fcd4/img/thisday_logo.gif")
    print "Adding " + thisday_head.get_name() + " scraper..."
    scrapers.append(thisday_head)

    


    # Tech

    today_tech = Scraper("Today Tech", api_id="2f7vilp6", region="nigeria", category="Tech", db_collection=collection,
                            logo="http://s20.postimg.org/mv7z5hjn1/today.png")
    print "Adding " + today_tech.get_name() + " scraper..."
    scrapers.append(today_tech)

    tech_cabal = Scraper("Tech Cabal Tech", api_id="4bsxr58e", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/6cfmyx6st/tclogobig.png")
    print "Adding " + tech_cabal.get_name() + " scraper..."
    scrapers.append(tech_cabal)

    vanguard_tech = Scraper("Vanguard Tech", api_id="e9qp7s1a", region="nigeria", category="Tech", db_collection=collection,
                            logo="http://s20.postimg.org/lxrwlrcfh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_tech.get_name() + " scraper..."
    scrapers.append(vanguard_tech)

    techpoint = Scraper("Techpoint Tech", api_id="490y6x36", region="nigeria", category="Tech", db_collection=collection,
                        logo="http://s20.postimg.org/qmhjrsxbh/Techpoint_web_logo.png")
    print "Adding " + techpoint.get_name() + " scraper..."
    scrapers.append(techpoint)

    ventures_tech = Scraper("Ventures Africa Tech", api_id="bu960i24", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://s20.postimg.org/f4wlmlrxl/Screen_Shot_2015_10_24_at_10.png")
    print "Adding " + ventures_tech.get_name() + " scraper..."
    scrapers.append(ventures_tech)
    
    ventures_tech_long = venturesScraper("Ventures Africa Tech Long", api_id="2dlebr7k", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://s20.postimg.org/f4wlmlrxl/Screen_Shot_2015_10_24_at_10.png")
    print "Adding " + ventures_tech_long.get_name() + " scraper..."
    scrapers.append(ventures_tech_long)

    it_news = itnScraper("IT News Africa Tech", api_id="1youwujk", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://www.itnewsafrica.com/wp-content/uploads/2013/08/ITNewsAfrica_logo.gif")
    print "Adding " + it_news.get_name() + " scraper..."
    scrapers.append(it_news)

    ms_techy = Scraper("Miss Techy Tech", api_id="an3p00uy", region="nigeria", category="Tech", db_collection=collection,
                       logo="'http://s20.postimg.org/dnb5b1n71/misstechy_header_logo.png")
    print "Adding " + ms_techy.get_name() + " scraper..."
    scrapers.append(ms_techy)
    
    


    # Business

    ventures = Scraper("Ventures Africa Business", api_id="6vo0hr5a", region="nigeria", category="Business", db_collection=collection,
                       logo="http://s20.postimg.org/f4wlmlrxl/Screen_Shot_2015_10_24_at_10.png")
    print "Adding " + ventures.get_name() + " scraper..."
    scrapers.append(ventures)
    
    ventures_biz_long = venturesScraper("Ventures Africa Business Long", api_id="bbudi886", region="nigeria", category="Business", db_collection=collection,
                       logo="http://s20.postimg.org/f4wlmlrxl/Screen_Shot_2015_10_24_at_10.png")
    print "Adding " + ventures_biz_long.get_name() + " scraper..."
    scrapers.append(ventures_biz_long)
    
    vanguard_business = Scraper("Vanguard Business", api_id="cskj1sxo", region="nigeria", category="Business", db_collection=collection,
                                logo="http://s20.postimg.org/lxrwlrcfh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_business.get_name() + " scraper..."
    scrapers.append(vanguard_business)
    
    punch_biz = punchScraper("Punch Business", api_id="bdid5uka", region="nigeria", category="Business", db_collection=collection,
                        logo="http://punch.cdn.ng/wp-content/themes/punch/images/punch_logo.jpg")
    print "Adding " + punch_biz.get_name() + " scraper..."
    scrapers.append(punch_biz)
    
    premium_biz = Scraper("Premium Business", api_id="8lc0dzni", region="nigeria", category="Business", db_collection=collection,
                           logo="http://media.premiumtimesng.com/wp-content/themes/PTN/images/176x64xptn-logo.png.pagespeed.ic.AedNv1evLn.png")
    print "Adding " + premium_biz.get_name() + " scraper..."
    scrapers.append(premium_biz)

    today_biz = Scraper("Today Business", api_id="ah2kx1zc", region="nigeria", category="Business", db_collection=collection,
                                 logo="http://s20.postimg.org/mv7z5hjn1/today.png")
    print "Adding " + today_biz.get_name() + " scraper..."
    scrapers.append(today_biz)

    guard_biz = guardScraper("Guardian Business", api_id="94g1s2v4", region="nigeria", category="Business", db_collection=collection,
                           logo="http://newngrguardiannewscom.c.presscdn.com/wp-content/uploads/2015/03/Guardian-Logo4501.jpg")
    print "Adding " + guard_biz.get_name() + " scraper..."
    scrapers.append(guard_biz)

    made_it = madeScraper("How We Made it In Africa", api_id="3igwmzsq", region="nigeria", category="Business", db_collection=collection,
                           logo="http://www.howwemadeitinafrica.com/wp-content/uploads/2015/01/HowWeMadeItInAfrica_logo.gif")
    print "Adding " + made_it.get_name() + " scraper..."
    scrapers.append(made_it)

    bizday_biz = Scraper("Businessday Business", api_id="6zzop1eu", region="nigeria", category="Business", db_collection=collection,
                           logo="http://s20.postimg.org/3tow14er1/bd_mast_head_set.png")
    print "Adding " + bizday_biz.get_name() + " scraper..."
    scrapers.append(bizday_biz)



    #Sport
    
    sahara_sport = Scraper("Sahara Sport", api_id="ayzkjxn6", region="nigeria", category="Sports", db_collection=collection,
                           logo="http://saharareporters.com/sites/default/themes/sr_theme/images/layout/header/header-logo.png")
    print "Adding " + sahara_sport.get_name() + " scraper..."
    scrapers.append(sahara_sport)
    

    guard_sport = guardScraper("Guardian Sport", api_id="2x0tlqrm", region="nigeria", category="Sports", db_collection=collection,
                           logo="http://newngrguardiannewscom.c.presscdn.com/wp-content/uploads/2015/03/Guardian-Logo4501.jpg")
    print "Adding " + guard_sport.get_name() + " scraper..."
    scrapers.append(guard_sport)    


    ynaija_sport = Scraper("Y Naija Sport", api_id="61gee0ww", region="nigeria", category="Sports", db_collection=collection,
                                logo="http://ynaija.com/wp-content/uploads/2015/08/ynaija-logo.png")
    print "Adding " + ynaija_sport.get_name() + " scraper..."
    scrapers.append(ynaija_sport)

    
    sixty_sport = Scraper("360 Sport", api_id="82amsk5k", region="nigeria", category="Sports", db_collection=collection,
                             logo="http://www.360nobs.com/wp-content/uploads/2015/04/360nobs_logo.png")
    print "Adding " + sixty_sport.get_name() + " scraper..."
    scrapers.append(sixty_sport)


    premium_sport = Scraper("Premium Sport", api_id="43z2ds64", region="nigeria", category="Sports", db_collection=collection,
                           logo="http://media.premiumtimesng.com/wp-content/themes/PTN/images/176x64xptn-logo.png.pagespeed.ic.AedNv1evLn.png")
    print "Adding " + premium_sport.get_name() + " scraper..."
    scrapers.append(premium_sport)


    today_sport = Scraper("Today Sport", api_id="6230ic18", region="nigeria", category="Sports", db_collection=collection,
                                 logo="http://s20.postimg.org/mv7z5hjn1/today.png")
    print "Adding " + today_sport.get_name() + " scraper..."
    scrapers.append(today_sport)


    vanguard_sport = Scraper("Vanguard Sport", api_id="8h4jou12", region="nigeria", category="Sports", db_collection=collection,
                                logo="http://s20.postimg.org/lxrwlrcfh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_sport.get_name() + " scraper..."
    scrapers.append(vanguard_sport)


    pulse_sport = Scraper("Pulse Sport", api_id="atek2opq", region="nigeria", category="Sports", db_collection=collection,
                    logo="http://s20.postimg.org/gg4cv2njd/pulset.png")
    print "Adding " + pulse_sport.get_name() + " scraper..."
    scrapers.append(pulse_sport)


    #Fashion


    tss_style = Scraper("The September Style", api_id="46qaagqm", region="nigeria", category="Fashion", db_collection=collection,
                                logo="http://theseptemberstandard.com/wp-content/uploads/2015/06/The-September-Standard-Logo.png")
    print "Adding " + tss_style.get_name() + " scraper..."
    scrapers.append(tss_style)


    sixty_fash = Scraper("360 Fashion", api_id="9g7x0tow", region="nigeria", category="Fashion", db_collection=collection,
                             logo="http://www.360nobs.com/wp-content/uploads/2015/04/360nobs_logo.png")
    print "Adding " + sixty_fash.get_name() + " scraper..."
    scrapers.append(sixty_fash)

    
    style_vitae = Scraper("Style Vitae Fashion", api_id="ajm8bq7c", region="nigeria", category="Fashion", db_collection=collection,
                                logo="http://s20.postimg.org/vxruyru0d/Header_Style_Vitae.png")
    print "Adding " + style_vitae.get_name() + " scraper..."
    scrapers.append(style_vitae)
    

    pulse_fash = Scraper("Pulse Fashion", api_id="6iq08fpw", region="nigeria", category="Fashion", db_collection=collection,
                    logo="http://s20.postimg.org/gg4cv2njd/pulset.png")
    print "Adding " + pulse_fash.get_name() + " scraper..."
    scrapers.append(pulse_fash)

    
    bnaij_fash = Scraper("Bella Naija Fashion", api_id="7zpspzcs", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://www.bellanaija.com/wp-content/themes/diamonds/images/bellanaija-mobile.png")
    print "Adding " + bnaij_fash.get_name() + " scraper..."
    scrapers.append(bnaij_fash)

    styleme = Scraper("Style Me Africa", api_id="bdjnldvy", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://www.stylemeafrica.com/wp-content/uploads/2014/09/SMA-Logo.jpg")
    print "Adding " + styleme.get_name() + " scraper..."
    scrapers.append(styleme)

    shirley = Scraper("Shirley's Wardrobe", api_id="3uwqzkjk", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://shirleyswardrobe.com/wp-content/uploads/2014/11/Logo.png")
    print "Adding " + shirley.get_name() + " scraper..."
    scrapers.append(shirley)

    
    #Politics

    sahara_politics = Scraper("Sahara Politics", api_id="adq8oezk", region="nigeria", category="Politics", db_collection=collection,
                           logo="http://saharareporters.com/sites/default/themes/sr_theme/images/layout/header/header-logo.png")
    print "Adding " + sahara_politics.get_name() + " scraper..."
    scrapers.append(sahara_politics)
    

    guard_politics = guardScraper("Guardian Politics", api_id="dafhjgqo", region="nigeria", category="Politics", db_collection=collection,
                           logo="http://newngrguardiannewscom.c.presscdn.com/wp-content/uploads/2015/03/Guardian-Logo4501.jpg")
    print "Adding " + guard_politics.get_name() + " scraper..."
    scrapers.append(guard_politics)    


    ynaija_politics = Scraper("Y Naija Politics", api_id="46p6rxx6", region="nigeria", category="Politics", db_collection=collection,
                                logo="http://ynaija.com/wp-content/uploads/2015/08/ynaija-logo.png")
    print "Adding " + ynaija_politics.get_name() + " scraper..."
    scrapers.append(ynaija_politics)


    today_politics = Scraper("Today Politics", api_id="5o03jioc", region="nigeria", category="Politics", db_collection=collection,
                                 logo="http://s20.postimg.org/mv7z5hjn1/today.png")
    print "Adding " + today_politics.get_name() + " scraper..."
    scrapers.append(today_politics)


    vanguard_politics = Scraper("Vanguard Politics", api_id="415802o6", region="nigeria", category="Politics", db_collection=collection,
                                logo="http://s20.postimg.org/lxrwlrcfh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_politics.get_name() + " scraper..."
    scrapers.append(vanguard_politics)


    punch_politics = punchScraper("Punch Politics", api_id="ei7tbc0y", region="nigeria", category="Politics", db_collection=collection,
                        logo="http://punch.cdn.ng/wp-content/themes/punch/images/punch_logo.jpg")
    print "Adding " + punch_politics.get_name() + " scraper..."
    scrapers.append(punch_politics)
    





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
