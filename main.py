import os
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from pytz import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
import logging
from pymongo.mongo_client import MongoClient
from scraper import Scraper
from special_scraper import SaharaScraper, RadrScraper, venturesScraper, guardScraper, punchScraper, itnScraper, todayScraper, madeScraper, thisdayScraper, naija_food_Scraper, qzScraper, hqScraper, beautyScraper, stearsScraper, wdigestScraper, yabaLeftScraper

logging.basicConfig()
ARTICLE_COLLECTION = "article"
scrapers = []


def define_scrapers(collection):
    


    # Gossip sources
    
    bnaij_gossip = Scraper("Bella Naija Gossip", api_id="5u0c0qoi", region="nigeria", category="Gossip", db_collection=collection,
                     logo="http://s20.postimg.org/lb78ku0ml/bellanaija_mobile.png")
    print "Adding " + bnaij_gossip.get_name() + " scraper..."
    scrapers.append(bnaij_gossip)
    
    pulse = Scraper("Pulse Gossip", api_id="dnxrp1h6", region="nigeria", category="Gossip", db_collection=collection,
                    logo="http://s20.postimg.org/po5s399d5/pulset.png")
    print "Adding " + pulse.get_name() + " scraper..."
    scrapers.append(pulse)
    
    sixty_gossip = Scraper("360 Gossip", api_id="3007ai6g", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/bpdo4j9gp/360nobs_logo.png")
    print "Adding " + sixty_gossip.get_name() + " scraper..."
    scrapers.append(sixty_gossip)
    

    ynaij_gossip = Scraper("Ynaija Gossip", api_id="acbiv2i8", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/k57tzs1pp/ynaija_logo.png")
    print "Adding " + ynaij_gossip.get_name() + " scraper..."
    scrapers.append(ynaij_gossip)

    ventures_gossip = venturesScraper("Ventures Africa Gossip", api_id="3w6fsfew", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/vf0juq6qx/Ventures.png")
    print "Adding " + ventures_gossip.get_name() + " scraper..."
    scrapers.append(ventures_gossip)
    
    today_gossip = todayScraper("Today Gossip", api_id="5zucxtg0", region="nigeria", category="Gossip", db_collection=collection,
                            logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_gossip.get_name() + " scraper..."
    scrapers.append(today_gossip)
    


    # Headline sources
    
    today_headlines = Scraper("Today Headlines", api_id="b9lqpkyy", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_headlines.get_name() + " scraper..."
    scrapers.append(today_headlines)
    
    vanguard_headlines = Scraper("Vanguard Headlines", api_id="abzmopk8", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_headlines.get_name() + " scraper..."
    scrapers.append(vanguard_headlines)
    

    y_naija_headlines = Scraper("Y Naija Headlines", api_id="8172f0f2", region="nigeria", category="Headlines", db_collection=collection,
                                logo="http://s20.postimg.org/k57tzs1pp/ynaija_logo.png")
    print "Adding " + y_naija_headlines.get_name() + " scraper..."
    scrapers.append(y_naija_headlines)

    
    sahara = Scraper("Sahara Headlines", api_id="5ih3db3a", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/khums7ulp/sahara_reporter.png")
    print "Adding " + sahara.get_name() + " scraper..."
    scrapers.append(sahara)
    
    premium = Scraper("Premium Headlines", api_id="4r6sdgjm", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/5khkdgrzh/176x64xptn_logo_png_pagespeed.png")
    print "Adding " + premium.get_name() + " scraper..."
    scrapers.append(premium)

    guard_head = guardScraper("Guardian Headlines", api_id="egzuf672", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/6uokk00j1/The_guardian.png")
    print "Adding " + guard_head.get_name() + " scraper..."
    scrapers.append(guard_head)

    thisday_head = thisdayScraper("Thisday Headlines", api_id="4thturvi", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/79zud0mgd/This_daylive.png")
    print "Adding " + thisday_head.get_name() + " scraper..."
    scrapers.append(thisday_head)

    
    qz = qzScraper("Quartz Headlines", api_id="49j7pfyc", region="nigeria", category="Headlines", db_collection=collection,
                           logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBISmAJnq9x7AgT_vFrEYvYkf3UUmEeyC3Sbc3GDENAPxUuK3cjQ")
    print "Adding " + qz.get_name() + " scraper..."
    scrapers.append(qz)
    

    


    # Tech

    today_tech = Scraper("Today Tech", api_id="2f7vilp6", region="nigeria", category="Tech", db_collection=collection,
                            logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_tech.get_name() + " scraper..."
    scrapers.append(today_tech)

    tech_cabal = Scraper("Tech Cabal Tech", api_id="4bsxr58e", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/z506nmilp/tclogobig.png")
    print "Adding " + tech_cabal.get_name() + " scraper..."
    scrapers.append(tech_cabal)

    vanguard_tech = Scraper("Vanguard Tech", api_id="e9qp7s1a", region="nigeria", category="Tech", db_collection=collection,
                            logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_tech.get_name() + " scraper..."
    scrapers.append(vanguard_tech)

    techpoint = Scraper("Techpoint Tech", api_id="490y6x36", region="nigeria", category="Tech", db_collection=collection,
                        logo="http://s20.postimg.org/m24k4csdp/Techpoint_web_logo.png")
    print "Adding " + techpoint.get_name() + " scraper..."
    scrapers.append(techpoint)

    ventures_tech = Scraper("Ventures Africa Tech", api_id="bu960i24", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://s20.postimg.org/vf0juq6qx/Ventures.png")
    print "Adding " + ventures_tech.get_name() + " scraper..."
    scrapers.append(ventures_tech)
    
    ventures_tech_long = venturesScraper("Ventures Africa Tech Long", api_id="2dlebr7k", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://s20.postimg.org/vf0juq6qx/Ventures.png")
    print "Adding " + ventures_tech_long.get_name() + " scraper..."
    scrapers.append(ventures_tech_long)

    it_news = itnScraper("IT News Africa Tech", api_id="1youwujk", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://s20.postimg.org/4sjhs0d65/it_s_new_africa.png")
    print "Adding " + it_news.get_name() + " scraper..."
    scrapers.append(it_news)

    ms_techy = Scraper("Miss Techy Tech", api_id="an3p00uy", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://s20.postimg.org/57url0z3h/misstechy_header_logo.png")
    print "Adding " + ms_techy.get_name() + " scraper..."
    scrapers.append(ms_techy)

    tech_africa = Scraper("Tech Africa", api_id="dqa7uz7m", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://techafri.ca/wp-content/uploads/2014/01/techafrica-logo-small.png")
    print "Adding " + tech_africa.get_name() + " scraper..."
    scrapers.append(tech_africa)
    
    


    # Business
    
    ventures = Scraper("Ventures Africa Business", api_id="6vo0hr5a", region="nigeria", category="Business", db_collection=collection,
                       logo="http://s20.postimg.org/vf0juq6qx/Ventures.png")
    print "Adding " + ventures.get_name() + " scraper..."
    scrapers.append(ventures)
    
    ventures_biz_long = venturesScraper("Ventures Africa Business Long", api_id="bbudi886", region="nigeria", category="Business", db_collection=collection,
                       logo="http://s20.postimg.org/vf0juq6qx/Ventures.png")
    print "Adding " + ventures_biz_long.get_name() + " scraper..."
    scrapers.append(ventures_biz_long)
    
    vanguard_business = Scraper("Vanguard Business", api_id="cskj1sxo", region="nigeria", category="Business", db_collection=collection,
                                logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_business.get_name() + " scraper..."
    scrapers.append(vanguard_business)
    
    punch_biz = punchScraper("Punch Business", api_id="bdid5uka", region="nigeria", category="Business", db_collection=collection,
                        logo="http://s20.postimg.org/bk9wuv25p/punchh.png")
    print "Adding " + punch_biz.get_name() + " scraper..."
    scrapers.append(punch_biz)
    
    premium_biz = Scraper("Premium Business", api_id="8lc0dzni", region="nigeria", category="Business", db_collection=collection,
                           logo="http://s20.postimg.org/5khkdgrzh/176x64xptn_logo_png_pagespeed.png")
    print "Adding " + premium_biz.get_name() + " scraper..."
    scrapers.append(premium_biz)

    today_biz = Scraper("Today Business", api_id="5t4jj7j8", region="nigeria", category="Business", db_collection=collection,
                                 logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_biz.get_name() + " scraper..."
    scrapers.append(today_biz)

    guard_biz = guardScraper("Guardian Business", api_id="94g1s2v4", region="nigeria", category="Business", db_collection=collection,
                           logo="http://s20.postimg.org/6uokk00j1/The_guardian.png")
    print "Adding " + guard_biz.get_name() + " scraper..."
    scrapers.append(guard_biz)

    made_it = madeScraper("How We Made it In Africa", api_id="3igwmzsq", region="nigeria", category="Business", db_collection=collection,
                           logo="http://s20.postimg.org/d8929ig19/How_we_made_it_in_africa.png")
    print "Adding " + made_it.get_name() + " scraper..."
    scrapers.append(made_it)

    bizday_biz = Scraper("Businessday Business", api_id="6zzop1eu", region="nigeria", category="Business", db_collection=collection,
                           logo="http://s20.postimg.org/i1o80mn59/bd_mast_head_set.png")
    print "Adding " + bizday_biz.get_name() + " scraper..."
    scrapers.append(bizday_biz)

    stearsng_biz = stearsScraper("Stears Business", api_id="9ryzjpym", region="nigeria", category="Business", db_collection=collection,
                           logo="http://i.imgur.com/V27BUsU.png")
    print "Adding " + stearsng_biz.get_name() + " scraper..."
    scrapers.append(stearsng_biz)



    #Sport
    
    sahara_sport = Scraper("Sahara Sport", api_id="ayzkjxn6", region="nigeria", category="Sports", db_collection=collection,
                           logo="http://s20.postimg.org/khums7ulp/sahara_reporter.png")
    print "Adding " + sahara_sport.get_name() + " scraper..."
    scrapers.append(sahara_sport)
    

    guard_sport = guardScraper("Guardian Sport", api_id="2x0tlqrm", region="nigeria", category="Sports", db_collection=collection,
                           logo="http://s20.postimg.org/6uokk00j1/The_guardian.png")
    print "Adding " + guard_sport.get_name() + " scraper..."
    scrapers.append(guard_sport)    

    '''
    ynaija_sport = Scraper("Y Naija Sport", api_id="61gee0ww", region="nigeria", category="Sports", db_collection=collection,
                                logo="http://s20.postimg.org/k57tzs1pp/ynaija_logo.png")
    print "Adding " + ynaija_sport.get_name() + " scraper..."
    scrapers.append(ynaija_sport)
    '''

    
    sixty_sport = Scraper("360 Sport", api_id="82amsk5k", region="nigeria", category="Sports", db_collection=collection,
                             logo="http://s20.postimg.org/bpdo4j9gp/360nobs_logo.png")
    print "Adding " + sixty_sport.get_name() + " scraper..."
    scrapers.append(sixty_sport)


    premium_sport = Scraper("Premium Sport", api_id="43z2ds64", region="nigeria", category="Sports", db_collection=collection,
                           logo="http://s20.postimg.org/5khkdgrzh/176x64xptn_logo_png_pagespeed.png")
    print "Adding " + premium_sport.get_name() + " scraper..."
    scrapers.append(premium_sport)


    today_sport = Scraper("Today Sport", api_id="6230ic18", region="nigeria", category="Sports", db_collection=collection,
                                 logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_sport.get_name() + " scraper..."
    scrapers.append(today_sport)


    vanguard_sport = Scraper("Vanguard Sport", api_id="8h4jou12", region="nigeria", category="Sports", db_collection=collection,
                                logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_sport.get_name() + " scraper..."
    scrapers.append(vanguard_sport)


    pulse_sport = Scraper("Pulse Sport", api_id="atek2opq", region="nigeria", category="Sports", db_collection=collection,
                    logo="http://s20.postimg.org/po5s399d5/pulset.png")
    print "Adding " + pulse_sport.get_name() + " scraper..."
    scrapers.append(pulse_sport)


    #Fashion


    tss_style = Scraper("The September Style", api_id="46qaagqm", region="nigeria", category="Fashion", db_collection=collection,
                                logo="http://s20.postimg.org/fpg831ajx/The_September_Standard_Logo.png")
    print "Adding " + tss_style.get_name() + " scraper..."
    scrapers.append(tss_style)


    sixty_fash = Scraper("360 Fashion", api_id="9g7x0tow", region="nigeria", category="Fashion", db_collection=collection,
                             logo="http://s20.postimg.org/bpdo4j9gp/360nobs_logo.png")
    print "Adding " + sixty_fash.get_name() + " scraper..."
    scrapers.append(sixty_fash)

    
    style_vitae = Scraper("Style Vitae Fashion", api_id="ajm8bq7c", region="nigeria", category="Fashion", db_collection=collection,
                                logo="http://s20.postimg.org/cu7q9wvxp/Header_Style_Vitae.png")
    print "Adding " + style_vitae.get_name() + " scraper..."
    scrapers.append(style_vitae)
    

    pulse_fash = Scraper("Pulse Fashion", api_id="6iq08fpw", region="nigeria", category="Fashion", db_collection=collection,
                    logo="http://s20.postimg.org/po5s399d5/pulset.png")
    print "Adding " + pulse_fash.get_name() + " scraper..."
    scrapers.append(pulse_fash)

    
    bnaij_fash = Scraper("Bella Naija Fashion", api_id="7zpspzcs", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://s20.postimg.org/lb78ku0ml/bellanaija_mobile.png")
    print "Adding " + bnaij_fash.get_name() + " scraper..."
    scrapers.append(bnaij_fash)

    shirley = Scraper("Shirley's Wardrobe", api_id="3uwqzkjk", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://s20.postimg.org/yo16vyqp9/shirley_s_wardrobe.png")
    print "Adding " + shirley.get_name() + " scraper..."
    scrapers.append(shirley)

    blackfab_fashion = Scraper("Black Fabulosity Fashion", api_id="e1l2f700", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://www.blackfabulousity.com/wp-content/uploads/2014/07/bfy-logo-2.png")
    print "Adding " + blackfab_fashion.get_name() + " scraper..."
    scrapers.append(blackfab_fashion)

    stylehq_fashion = hqScraper("Style HQ Fashion", api_id="5ho7bmf4", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://i.imgur.com/PZslF5g.png")
    print "Adding " + stylehq_fashion.get_name() + " scraper..."
    scrapers.append(stylehq_fashion)    

    onobello_fashion = Scraper("Ono Bello Fashion", api_id="97yjawcw", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://onobello.com/wp-content/uploads/2014/06/logo35.jpg")
    print "Adding " + onobello_fashion.get_name() + " scraper..."
    scrapers.append(onobello_fashion)

    blackfab_style = Scraper("Black Fabulosity Style", api_id="b71iga7u", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://www.blackfabulousity.com/wp-content/uploads/2014/07/bfy-logo-2.png")
    print "Adding " + blackfab_style.get_name() + " scraper..."
    scrapers.append(blackfab_style)


    #Food
    stylehq_food = hqScraper("Style HQ Food", api_id="dj3e3z0i", region="nigeria", category="Food", db_collection=collection,
                     logo="http://i.imgur.com/PZslF5g.png")
    print "Adding " + stylehq_food.get_name() + " scraper..."
    scrapers.append(stylehq_food)

    butterfly_food = Scraper("Kitchen Butterfly Food", api_id="7i313vq6", region="nigeria", category="Food", db_collection=collection,
                     logo="http://www.kitchenbutterfly.com/wp-content/uploads/2015/01/logo-3.png")
    print "Adding " + butterfly_food.get_name() + " scraper..."
    scrapers.append(butterfly_food)

    naija_foodie = naija_food_Scraper("9ja Foodie", api_id="8k6tn98m", region="nigeria", category="Food", db_collection=collection,
                     logo="http://www.9jafoodie.com/wp-content/uploads/2015/04/9jafoodie_watermark_ret.jpg")
    print "Adding " + naija_foodie.get_name() + " scraper..."
    scrapers.append(naija_foodie)

    vegan_food = Scraper("Vegan", api_id="88rw04wo", region="nigeria", category="Food", db_collection=collection,
                     logo="http://yupitsvegan.com/wp-content/uploads/2015/04/cropped-yiv-logo-retina.png")
    print "Adding " + vegan_food.get_name() + " scraper..."
    scrapers.append(vegan_food)


    #Lifestyle

    stylehq_lifestyle = hqScraper("Style HQ Lifestyle", api_id="6uil7rwe", region="nigeria", category="Lifestyle", db_collection=collection,
                     logo="http://i.imgur.com/PZslF5g.png")
    print "Adding " + stylehq_lifestyle.get_name() + " scraper..."
    scrapers.append(stylehq_lifestyle)

    stylehq_living = hqScraper("Style HQ Living", api_id="e8wxf19s", region="nigeria", category="Lifestyle", db_collection=collection,
                     logo="http://i.imgur.com/PZslF5g.png")
    print "Adding " + stylehq_living.get_name() + " scraper..."
    scrapers.append(stylehq_living)

    blackfab_lifestyle1 = Scraper("Black Fabulosity Lifestyle 1", api_id="3iioys3c", region="nigeria", category="Lifestyle", db_collection=collection,
                     logo="http://www.blackfabulousity.com/wp-content/uploads/2014/07/bfy-logo-2.png")
    print "Adding " + blackfab_lifestyle1.get_name() + " scraper..."
    scrapers.append(blackfab_lifestyle1)

    blackfab_lifestyle2 = Scraper("Black Fabulosity Lifestyle 2", api_id="c0mpmajk", region="nigeria", category="Lifestyle", db_collection=collection,
                     logo="http://www.blackfabulousity.com/wp-content/uploads/2014/07/bfy-logo-2.png")
    print "Adding " + blackfab_lifestyle2.get_name() + " scraper..."
    scrapers.append(blackfab_lifestyle2)

    ours_lifestyle = Scraper("Ours Lifestyle", api_id="daotpyle", region="nigeria", category="Lifestyle", db_collection=collection,
                     logo="http://ours-mag.com/wp-content/uploads/2015/10/Logo_Ours_noir1.png")
    print "Adding " + ours_lifestyle.get_name() + " scraper..."
    scrapers.append(ours_lifestyle)    

    
    #Politics
    
    sahara_politics = Scraper("Sahara Politics", api_id="adq8oezk", region="nigeria", category="Politics", db_collection=collection,
                           logo="http://s20.postimg.org/khums7ulp/sahara_reporter.png")
    print "Adding " + sahara_politics.get_name() + " scraper..."
    scrapers.append(sahara_politics)
    
    
    guard_politics = guardScraper("Guardian Politics", api_id="dafhjgqo", region="nigeria", category="Politics", db_collection=collection,
                           logo="http://s20.postimg.org/6uokk00j1/The_guardian.png")
    print "Adding " + guard_politics.get_name() + " scraper..."
    scrapers.append(guard_politics)    
    
    
    ynaija_politics = Scraper("Y Naija Politics", api_id="46p6rxx6", region="nigeria", category="Politics", db_collection=collection,
                                logo="http://s20.postimg.org/k57tzs1pp/ynaija_logo.png")
    print "Adding " + ynaija_politics.get_name() + " scraper..."
    scrapers.append(ynaija_politics)
    
    
    today_politics = Scraper("Today Politics", api_id="5o03jioc", region="nigeria", category="Politics", db_collection=collection,
                                 logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_politics.get_name() + " scraper..."
    scrapers.append(today_politics)
    
    
    vanguard_politics = Scraper("Vanguard Politics", api_id="415802o6", region="nigeria", category="Politics", db_collection=collection,
                                logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_politics.get_name() + " scraper..."
    scrapers.append(vanguard_politics)

    punch_politics = punchScraper("Punch Politics", api_id="ei7tbc0y", region="nigeria", category="Politics", db_collection=collection,
                        logo="http://s20.postimg.org/bk9wuv25p/punchh.png")
    print "Adding " + punch_politics.get_name() + " scraper..."
    scrapers.append(punch_politics)
    

    #Beauty

    bnaij_beauty = Scraper("Bella Naija Beauty", api_id="81ifhajm", region="nigeria", category="Beauty", db_collection=collection,
                     logo="http://s20.postimg.org/lb78ku0ml/bellanaija_mobile.png")
    print "Adding " + bnaij_beauty.get_name() + " scraper..."
    scrapers.append(bnaij_beauty)

    stylehq_beauty = hqScraper("Style HQ Beauty", api_id="50eu30h6", region="nigeria", category="Beauty", db_collection=collection,
                     logo="http://i.imgur.com/PZslF5g.png")
    print "Adding " + stylehq_beauty.get_name() + " scraper..."
    scrapers.append(stylehq_beauty)

    natural_nigerian = Scraper("Natural Nigerian", api_id="cids7wge", region="nigeria", category="Beauty", db_collection=collection,
                     logo="http://naturalnigerian.com/wp-content/themes/nn/images/nn_logo.png")
    print "Adding " + natural_nigerian.get_name() + " scraper..."
    scrapers.append(natural_nigerian)    

    beauty_lagos = beautyScraper("Beauty in Lagos", api_id="b9uu2hyc", region="nigeria", category="Beauty", db_collection=collection,
                     logo="http://1.bp.blogspot.com/-1hYLUhAt6ck/Vai_l-n7PKI/AAAAAAAAE_U/mgeSjCBI1n4/s960/BANNER1.png")
    print "Adding " + beauty_lagos.get_name() + " scraper..."
    scrapers.append(beauty_lagos)

    onobello_beauty = Scraper("Ono Bello Beauty", api_id="9c157ol6", region="nigeria", category="Beauty", db_collection=collection,
                     logo="http://onobello.com/wp-content/uploads/2014/06/logo35.jpg")
    print "Adding " + onobello_beauty.get_name() + " scraper..."
    scrapers.append(onobello_beauty)   

    
    igbo_chick = Scraper("That Igbo Chick", api_id="cx2vef1m", region="nigeria", category="Beauty", db_collection=collection,
                     logo="http://i.imgur.com/ywlP1Z5.png")
    print "Adding " + igbo_chick.get_name() + " scraper..."
    scrapers.append(igbo_chick)    
    

    #Funny

    battabox_funny = Scraper("Battabox Funny", api_id="bz8q161w", region="nigeria", category="Funny", db_collection=collection,
                     logo="https://battabox-battabox.netdna-ssl.com/wp-content/uploads/2015/08/BattaBox-Logo-Nigeria.png")
    print "Adding " + battabox_funny.get_name() + " scraper..."
    scrapers.append(battabox_funny)

    zikoko_funny = Scraper("Zikoko Funny", api_id="6tyylw1s", region="nigeria", category="Funny", db_collection=collection,
                             logo="http://s20.postimg.org/ugk6sftf1/zikoko.png")
    print "Adding " + zikoko_funny.get_name() + " scraper..."
    scrapers.append(zikoko_funny)

    yabaleft_funny = yabaLeftScraper("Yaba Left Funny", api_id="2w2ous02", region="nigeria", category="Funny", db_collection=collection,
                             logo="http://yabaleftonline.com/wp-content/uploads/2014/11/YABALEFTONLINE-LOGO.png")
    print "Adding " + yabaleft_funny.get_name() + " scraper..."
    scrapers.append(yabaleft_funny)    

    #Art & Design

    ours_art = Scraper("Ours Art", api_id="62ddxayo", region="nigeria", category="Art", db_collection=collection,
                     logo="http://ours-mag.com/wp-content/uploads/2015/10/Logo_Ours_noir1.png")
    print "Adding " + ours_art.get_name() + " scraper..."
    scrapers.append(ours_art)        

    ada_art = Scraper("African Digital Art", api_id="7jji0dpo", region="nigeria", category="Art", db_collection=collection,
                     logo="http://i.imgur.com/DbWfwtB.png")
    print "Adding " + ada_art.get_name() + " scraper..."
    scrapers.append(ada_art)        

    indaba_art = Scraper("Desing Indaba", api_id="dyiz6gpi", region="nigeria", category="Art", db_collection=collection,
                     logo="http://i.imgur.com/avSP9b3.png")
    print "Adding " + indaba_art.get_name() + " scraper..."
    scrapers.append(indaba_art)        

    blackfab_art = Scraper("Black Fabulosity Art", api_id="9g24zlg2", region="nigeria", category="Art", db_collection=collection,
                     logo="http://www.blackfabulousity.com/wp-content/uploads/2014/07/bfy-logo-2.png")
    print "Adding " + blackfab_art.get_name() + " scraper..."
    scrapers.append(blackfab_art)


    #Travel

    stylehq_travel = hqScraper("Style HQ Travel", api_id="ekdq2bdq", region="nigeria", category="Travel", db_collection=collection,
                     logo="http://i.imgur.com/PZslF5g.png")
    print "Adding " + stylehq_travel.get_name() + " scraper..."
    scrapers.append(stylehq_travel)

    pursuits_travel = Scraper("Spirited Pursuits Travel", api_id="4q9638mm", region="nigeria", category="Travel", db_collection=collection,
                     logo="http://static1.squarespace.com/static/52ee7408e4b0d94885a12285/t/52eea240e4b01528abbad4f0/1446338588469/?format=1500w")
    print "Adding " + pursuits_travel.get_name() + " scraper..."
    scrapers.append(pursuits_travel)

    nomads_travel = Scraper("Nomads Travel", api_id="cm723she", region="nigeria", category="Travel", db_collection=collection,
                     logo="https://naijanomads.files.wordpress.com/2015/10/cropped-fullsizerender-2.jpg?w=1000")
    print "Adding " + nomads_travel.get_name() + " scraper..."
    scrapers.append(nomads_travel)

    gold_travel = Scraper("Gold Travel", api_id="bs04vyio", region="nigeria", category="Travel", db_collection=collection,
                     logo="http://static1.squarespace.com/static/533b44d9e4b0ac2733685dc4/t/5544f2dbe4b067ba8b423aa5/1446335979794/?format=1500w")
    print "Adding " + gold_travel.get_name() + " scraper..."
    scrapers.append(gold_travel)

    tastemakers_travel = Scraper("Tastemakers Travel", api_id="2b6efqsi", region="nigeria", category="Travel", db_collection=collection,
                     logo="http://tastemakersafrica.com/wp-content/uploads/2014/11/TMA_Logo_Short_WebLg.png")
    print "Adding " + tastemakers_travel.get_name() + " scraper..."
    scrapers.append(tastemakers_travel)

    hotels_travel = Scraper("Hotels Travel", api_id="apwqxsdi", region="nigeria", category="Travel", db_collection=collection,
                     logo="http://hotels.ng/media/v5/img/logo.png")
    print "Adding " + hotels_travel.get_name() + " scraper..."
    scrapers.append(hotels_travel)

    jovago_travel = Scraper("Jovago Travel", api_id="dwt47zq4", region="nigeria", category="Travel", db_collection=collection,
                     logo="http://techloy.com/wp-content/uploads/2015/04/164350-JovagoLogo-7e0f6d-large-1429700953.png")
    print "Adding " + jovago_travel.get_name() + " scraper..."
    scrapers.append(jovago_travel)


    #Weddings
    bnaij_weddings = Scraper("Bella Naija Weddings", api_id="aaem0hv6", region="nigeria", category="Weddings", db_collection=collection,
                     logo="http://s20.postimg.org/lb78ku0ml/bellanaija_mobile.png")
    print "Adding " + bnaij_weddings.get_name() + " scraper..."
    scrapers.append(bnaij_weddings)


    onobello_weddings = Scraper("Ono Bello Weddings", api_id="6991ib7o", region="nigeria", category="Weddings", db_collection=collection,
                     logo="http://onobello.com/wp-content/uploads/2014/06/logo35.jpg")
    print "Adding " + onobello_weddings.get_name() + " scraper..."
    scrapers.append(onobello_weddings)


    groom_weddings = Scraper("Groomspiration Weddings", api_id="8cl9n7l4", region="nigeria", category="Weddings", db_collection=collection,
                     logo="http://groominspiration.com/v2015/wp-content/uploads/2015/03/logoWhite1.png")
    print "Adding " + groom_weddings.get_name() + " scraper..."
    scrapers.append(groom_weddings)


    nigeria_weddings = Scraper("My Wedding Nigeria Weddings", api_id="2t8t85po", region="nigeria", category="Weddings", db_collection=collection,
                     logo="http://myweddingnigeria.com/wp-content/themes/sight/images/logo.png")
    print "Adding " + nigeria_weddings.get_name() + " scraper..."
    scrapers.append(nigeria_weddings)


    digest_weddings = wdigestScraper("Wedding Digest Weddings", api_id="62y68gyy", region="nigeria", category="Weddings", db_collection=collection,
                     logo="http://www.weddingdigestnaija.com/wp-content/uploads/2015/10/Large-Final.png")
    print "Adding " + digest_weddings.get_name() + " scraper..."
    scrapers.append(digest_weddings)    


    sugar_weddings = Scraper("Sugar Weddings", api_id="2n05s2kk", region="nigeria", category="Weddings", db_collection=collection,
                     logo="http://sugarweddings.com/sites/all/themes/sugar_2015/images/sugarlogo.png")
    print "Adding " + sugar_weddings.get_name() + " scraper..."
    scrapers.append(sugar_weddings)


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
