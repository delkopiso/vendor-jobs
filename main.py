import os
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from pytz import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
import logging
from pymongo.mongo_client import MongoClient
from scraper import Scraper
from ioScraper import ioScraper
from special_scraper import SaharaScraper, RadrScraper, venturesScraper, guardScraper, punchScraper, itnScraper, todayScraper, madeScraper, thisdayScraper, naija_food_Scraper, qzScraper, hqScraper, beautyScraper, stearsScraper, wdigestScraper, yabaLeftScraper, styleDocScraper, lagosStreetScraper, nairametricsScraper

logging.basicConfig()
ARTICLE_COLLECTION = "article"
scrapers = []


def define_scrapers(collection):
    


    ###################################################### GOSSIP SOUCRES ##########################################################
    
    bnaij_gossip = Scraper("Bella Naija Gossip", api_id="5u0c0qoi", region="nigeria", category="Gossip", db_collection=collection,
                     logo="http://s20.postimg.org/lb78ku0ml/bellanaija_mobile.png")
    print "Adding " + bnaij_gossip.get_name() + " scraper..."
    scrapers.append(bnaij_gossip)

    ##Pulse Sources
    pulse_gossip_io_0600 = ioScraper("Pulse Naija Gossip IO - 6:00", site="http%3A%2F%2Fpulse.ng%2Ffashion%2F&&" , api_id="f2d2670a-93d9-43c0-9569-7280f09deb95", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/po5s399d5/pulset.png")
    print "Adding " + pulse_gossip_io_0600.get_name() + " scraper..."
    scrapers.append(pulse_gossip_io_0600)

    pulse_gossip_io_1330 = ioScraper("Pulse Naija Gossip IO - 13:30", site="http%3A%2F%2Fpulse.ng%2Ffashion%2F&&" , api_id="db4343e4-13f9-4e46-b578-a9a5101112cd", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/po5s399d5/pulset.png")
    print "Adding " + pulse_gossip_io_1330.get_name() + " scraper..."
    scrapers.append(pulse_gossip_io_1330)
    
    ##360 Nobs Gossip Sources
    sixty_gossip_io_0600 = ioScraper("360 Gossip IO - 0600", site="http%3A%2F%2Fwww.360nobs.com%2Fcategory%2Fnews%2Fentertainment_news%2F&&" , api_id="919f81ac-9084-4168-b6ad-189317367074", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/bpdo4j9gp/360nobs_logo.png")
    print "Adding " + sixty_gossip_io_0600.get_name() + " scraper..."
    scrapers.append(sixty_gossip_io_0600)

    sixty_gossip_io_1800 = ioScraper("360 Gossip IO - 1800", site="http%3A%2F%2Fwww.360nobs.com%2Fcategory%2Fnews%2Fentertainment_news%2F&&" , api_id="ac72a90c-f09c-4e95-a832-89b50e4f6fc1", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/bpdo4j9gp/360nobs_logo.png")
    print "Adding " + sixty_gossip_io_1800.get_name() + " scraper..."
    scrapers.append(sixty_gossip_io_1800)

    ##YNaija Gossip Sources
    ynaij_gossip_io = ioScraper("Ynaija Gossip IO", site="http%3A%2F%2Fynaija.com%2Fcelebrity%2F&&", api_id="3fda0fa5-3a11-4863-a36c-33d07e0f365d", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/k57tzs1pp/ynaija_logo.png")
    print "Adding " + ynaij_gossip_io.get_name() + " scraper..."
    scrapers.append(ynaij_gossip_io)

    ##Linda Gossip Sources
    linda_gossip_io_0000 = ioScraper("Linda Ikeji Gossip IO 0000", site="http%3A%2F%2Fwww.lindaikejisblog.com%2F&&", api_id="5d600d18-3a8c-4b95-a76f-97c2f69b6f94", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://i.imgur.com/7wOUVhV.png")
    print "Adding " + linda_gossip_io_0000.get_name() + " scraper..."
    scrapers.append(linda_gossip_io_0000)
    
    linda_gossip_io_0600 = ioScraper("Linda Ikeji Gossip IO 0600", site="http%3A%2F%2Fwww.lindaikejisblog.com%2F&&", api_id="472989dd-8729-46cc-bd4b-1e97c035c947", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://i.imgur.com/7wOUVhV.png")
    print "Adding " + linda_gossip_io_0600.get_name() + " scraper..."
    scrapers.append(linda_gossip_io_0600)

    linda_gossip_io_0900 = ioScraper("Linda Ikeji Gossip IO 0900", site="http%3A%2F%2Fwww.lindaikejisblog.com%2F&&", api_id="b892fcb5-357e-4664-8590-cb61160be6a9", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://i.imgur.com/7wOUVhV.png")
    print "Adding " + linda_gossip_io_0900.get_name() + " scraper..."
    scrapers.append(linda_gossip_io_0900)

    linda_gossip_io_1330 = ioScraper("Linda Ikeji Gossip IO 1200", site="http%3A%2F%2Fwww.lindaikejisblog.com%2F&&", api_id="7c93a470-7c70-432b-9176-43820e5c057d", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://i.imgur.com/7wOUVhV.png")
    print "Adding " + linda_gossip_io_1330.get_name() + " scraper..."
    scrapers.append(linda_gossip_io_1330)

    linda_gossip_io_1800 = ioScraper("Linda Ikeji Gossip IO 1800", site="http%3A%2F%2Fwww.lindaikejisblog.com%2F&&", api_id="c090a1f6-0d8c-4f2e-9283-c37c41d99990", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://i.imgur.com/7wOUVhV.png")
    print "Adding " + linda_gossip_io_1800.get_name() + " scraper..."
    scrapers.append(linda_gossip_io_1800)

    linda_gossip_io_2100 = ioScraper("Linda Ikeji Gossip IO 2100", site="http%3A%2F%2Fwww.lindaikejisblog.com%2F&&", api_id="3aebdf54-bce4-4744-aa45-48f88f5130cf", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://i.imgur.com/7wOUVhV.png")
    print "Adding " + linda_gossip_io_2100.get_name() + " scraper..."
    scrapers.append(linda_gossip_io_2100)

    ###################################################### HEADLINES SOUCRES ##########################################################
    
    ##Today Headline Sources##
    today_headlines_io_0600 = ioScraper("Today Headlines IO 0600 ", site="https%3A%2F%2Fwww.today.ng%2Fnews%2F&&", api_id="cb7bffab-02e7-4bb7-959a-f771f763b81c", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_headlines_io_0600.get_name() + " scraper..."
    scrapers.append(today_headlines_io_0600)

    today_headlines_io_0900 = ioScraper("Today Headlines IO 0900 ", site="https%3A%2F%2Fwww.today.ng%2Fnews%2F&&", api_id="0c4b9106-4573-4389-914c-aff1790581ba", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_headlines_io_0900.get_name() + " scraper..."
    scrapers.append(today_headlines_io_0900)

    today_headlines_io_1800 = ioScraper("Today Headlines IO 1800 ", site="https%3A%2F%2Fwww.today.ng%2Fnews%2F&&", api_id="2e051a53-e29a-4f52-bbbe-0da36b1a7761", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_headlines_io_1800.get_name() + " scraper..."
    scrapers.append(today_headlines_io_1800)
    
    ##Vanguard Headline Sources##
    vanguard_headlines_io_0900 = ioScraper("Vanguard Headlines IO 0900 ", site="http%3A%2F%2Fwww.vanguardngr.com%2Fcategory%2Fbusiness%2F&&", api_id="dda2c15f-52b1-46e5-b2c2-33ca1e60bfea", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_headlines_io_0900.get_name() + " scraper..."
    scrapers.append(vanguard_headlines_io_0900)

    vanguard_headlines_io_1330 = ioScraper("Vanguard Headlines IO 1330 ", site="http%3A%2F%2Fwww.vanguardngr.com%2Fcategory%2Fbusiness%2F&&", api_id="e657a791-f6ba-41bc-ad5e-e7a6f8ea997b", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_headlines_io_1330.get_name() + " scraper..."
    scrapers.append(vanguard_headlines_io_1330)

    vanguard_headlines_io_1800 = ioScraper("Vanguard Headlines IO 1800 ", site="http%3A%2F%2Fwww.vanguardngr.com%2Fcategory%2Fbusiness%2F&&", api_id="78e26784-cd14-44e6-bdf7-a27b3049cd33", region="nigeria", category="Headlines", db_collection=collection,
                                 logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_headlines_io_1800.get_name() + " scraper..."
    scrapers.append(vanguard_headlines_io_1800)
    

    ##Ynaija Headline Sources##
    ynaij_headlines_io = ioScraper("Ynaija Headlines IO", site="http%3A%2F%2Fynaija.com%2Fnews%2F&&", api_id="a5987e28-e976-46f7-afa4-16370a37d13f", region="nigeria", category="Gossip", db_collection=collection,
                             logo="http://s20.postimg.org/k57tzs1pp/ynaija_logo.png")
    print "Adding " + ynaij_headlines_io.get_name() + " scraper..."
    scrapers.append(ynaij_headlines_io)
    
    
    ##Premium Headline Sources##
    premium_io_0600 = ioScraper("Premium Headlines 0600", site="http%3A%2F%2Fwww.premiumtimesng.com%2Fcategory%2Fnews%2Fheadlines&&", api_id="3edb5b4a-fa43-4e37-b332-79f3639c517b", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/5khkdgrzh/176x64xptn_logo_png_pagespeed.png")
    print "Adding " + premium_io_0600.get_name() + " scraper..."
    scrapers.append(premium_io_0600)

    premium_io_1800 = ioScraper("Premium Headlines 1800", site="http%3A%2F%2Fwww.premiumtimesng.com%2Fcategory%2Fnews%2Fheadlines&&", api_id="3b15da009-ab9d-4610-adcf-9503d64b1ef5", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/5khkdgrzh/176x64xptn_logo_png_pagespeed.png")
    print "Adding " + premium_io_1800.get_name() + " scraper..."
    scrapers.append(premium_io_1800)


    ##Guardian Headline Sources##
    guard_head_io_0000 = ioScraper("Guardian Headlines IO 0000 ", site="http%3A%2F%2Fwww.ngrguardiannews.com%2Fnews%2Fnational%2F&&", api_id="370b095f-3ee8-457d-a957-c2076250582c", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/6uokk00j1/The_guardian.png")
    print "Adding " + guard_head_io_0000.get_name() + " scraper..."
    scrapers.append(guard_head_io_0000)

    guard_head_io_0600 = ioScraper("Guardian Headlines IO 0600 ", site="http%3A%2F%2Fwww.ngrguardiannews.com%2Fnews%2Fnational%2F&&", api_id="5ab2e92e-bb99-48c7-aafb-022f049f2ec1", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/6uokk00j1/The_guardian.png")
    print "Adding " + guard_head_io_0600.get_name() + " scraper..."
    scrapers.append(guard_head_io_0600)    

    '''
    guard_head_io_1330 = ioScraper("Guardian Headlines IO 1330 ", site="http%3A%2F%2Fwww.ngrguardiannews.com%2Fnews%2Fnational%2F&&", api_id="", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/6uokk00j1/The_guardian.png")
    print "Adding " + guard_head_io_1330.get_name() + " scraper..."
    scrapers.append(guard_head_io_1330)
    '''

    guard_head_io_2100 = ioScraper("Guardian Headlines IO 2100 ", site="http%3A%2F%2Fwww.ngrguardiannews.com%2Fnews%2Fnational%2F&&", api_id="e06e2677-8237-455f-843b-bd6ae34b0832", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/6uokk00j1/The_guardian.png")
    print "Adding " + guard_head_io_2100.get_name() + " scraper..."
    scrapers.append(guard_head_io_2100)


    ##Thisday Headline Sources##
    thisday_head_io_0600 = ioScraper("Thisday Headlines IO 0600", site="http%3A%2F%2Fwww.thisdaylive.com%2Fnews%2F&&", api_id="8038fdd9-a64e-4924-b8a1-66b7bbb99618", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/79zud0mgd/This_daylive.png")
    print "Adding " + thisday_head_io_0600.get_name() + " scraper..."
    scrapers.append(thisday_head_io_0600)

    thisday_head_io_0900 = ioScraper("Thisday Headlines IO 0900", site="http%3A%2F%2Fwww.thisdaylive.com%2Fnews%2F&&", api_id="4621095d-a210-451c-85c1-d3a2494682cf", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/79zud0mgd/This_daylive.png")
    print "Adding " + thisday_head_io_0900.get_name() + " scraper..."
    scrapers.append(thisday_head_io_0900)

    thisday_head_io_1330 = ioScraper("Thisday Headlines IO 1330", site="http%3A%2F%2Fwww.thisdaylive.com%2Fnews%2F&&", api_id="bcaa7eb6-b433-4b06-bca0-827afcc8f3f7", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/79zud0mgd/This_daylive.png")
    print "Adding " + thisday_head_io_1330.get_name() + " scraper..."
    scrapers.append(thisday_head_io_1330)

    thisday_head_io_1800 = ioScraper("Thisday Headlines IO 1800", site="http%3A%2F%2Fwww.thisdaylive.com%2Fnews%2F&&", api_id="2b37b2a8-756e-4889-af81-84d26876bdb1", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/79zud0mgd/This_daylive.png")
    print "Adding " + thisday_head_io_1800.get_name() + " scraper..."
    scrapers.append(thisday_head_io_1800)

    thisday_head_io_2100 = ioScraper("Thisday Headlines IO 2100", site="http%3A%2F%2Fwww.thisdaylive.com%2Fnews%2F&&", api_id="e822442c-e434-4d8f-9b03-4f52984717a9", region="nigeria", category="Headlines", db_collection=collection,
                           logo="http://s20.postimg.org/79zud0mgd/This_daylive.png")
    print "Adding " + thisday_head_io_2100.get_name() + " scraper..."
    scrapers.append(thisday_head_io_2100)


    ##Quartz Headline Sources##
    qz_io_0600 = ioScraper("Quartz Headlines IO 0600", site="http%3A%2F%2Fqz.com%2Flatest%2F&&", api_id="f639464f-1466-421f-b9ae-aa3a6b0dc851", region="nigeria", category="Headlines", db_collection=collection,
                           logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBISmAJnq9x7AgT_vFrEYvYkf3UUmEeyC3Sbc3GDENAPxUuK3cjQ")
    print "Adding " + qz_io_0600.get_name() + " scraper..."
    scrapers.append(qz_io_0600)

    qz_io_2100 = ioScraper("Quartz Headlines IO 0600", site="http%3A%2F%2Fqz.com%2Flatest%2F&&", api_id="0829fafc-9a4a-49ca-8dff-8ba7533794b6", region="nigeria", category="Headlines", db_collection=collection,
                           logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBISmAJnq9x7AgT_vFrEYvYkf3UUmEeyC3Sbc3GDENAPxUuK3cjQ")
    print "Adding " + qz_io_2100.get_name() + " scraper..."
    scrapers.append(qz_io_2100)


    ###################################################### TECH SOUCRES ##########################################################

    ##Techcabal Tech Sources##
    tech_cabal_io_0000 = ioScraper("Tech Cabal Tech IO 0000", site="http%3A%2F%2Ftechcabal.com%2F&&", api_id="d6485476-ba8d-426b-8145-6d8f146795bb", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/z506nmilp/tclogobig.png")
    print "Adding " + tech_cabal_io_0000.get_name() + " scraper..."
    scrapers.append(tech_cabal_io_0000)

    tech_cabal_io_0600 = ioScraper("Tech Cabal Tech IO 0600", site="http%3A%2F%2Ftechcabal.com%2F&&", api_id="31d7e734-cdf3-4787-be89-043a77b2ea9c", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/z506nmilp/tclogobig.png")
    print "Adding " + tech_cabal_io_0600.get_name() + " scraper..."
    scrapers.append(tech_cabal_io_0600)

    tech_cabal_io_1330 = ioScraper("Tech Cabal Tech IO 1330", site="http%3A%2F%2Ftechcabal.com%2F&&", api_id="6c197c1f-81e7-49ac-bc67-8d3465519747", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/z506nmilp/tclogobig.png")
    print "Adding " + tech_cabal_io_1330.get_name() + " scraper..."
    scrapers.append(tech_cabal_io_1330)

    tech_cabal_io_2100 = ioScraper("Tech Cabal Tech IO 2100", site="http%3A%2F%2Ftechcabal.com%2F&&", api_id="4414d2e1-1f3f-4002-aa4b-46dc4cbd69b0", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/z506nmilp/tclogobig.png")
    print "Adding " + tech_cabal_io_2100.get_name() + " scraper..."
    scrapers.append(tech_cabal_io_2100)

    
    ##Techpoint Tech Sources##
    techpoint_io_0900 = ioScraper("Techpoint Tech IO 0900", site="https%3A%2F%2Ftechpoint.ng%2F&&", api_id="6eef3f05-0448-4f6f-9dfd-7bc9b323b498", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/m24k4csdp/Techpoint_web_logo.png")
    print "Adding " + techpoint_io_0900.get_name() + " scraper..."
    scrapers.append(techpoint_io_0900)

    techpoint_io_1330 = ioScraper("Techpoint Tech IO 1330", site="https%3A%2F%2Ftechpoint.ng%2F&&", api_id="d1c14ff0-f8d2-4836-8def-ffb2e8540fba", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/m24k4csdp/Techpoint_web_logo.png")
    print "Adding " + techpoint_io_1330.get_name() + " scraper..."
    scrapers.append(techpoint_io_1330)
    
    techpoint_io_1800 = ioScraper("Techpoint Tech IO 1800", site="https%3A%2F%2Ftechpoint.ng%2F&&", api_id="49c9e388-4ffe-40bf-936a-9e59746aa653", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/m24k4csdp/Techpoint_web_logo.png")
    print "Adding " + techpoint_io_1800.get_name() + " scraper..."
    scrapers.append(techpoint_io_1800)

    techpoint_io_2100 = ioScraper("Techpoint Tech IO 2100", site="https%3A%2F%2Ftechpoint.ng%2F&&", api_id="7d55e7d9-a56b-465c-bd9f-876b45c1ed16", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/m24k4csdp/Techpoint_web_logo.png")
    print "Adding " + techpoint_io_2100.get_name() + " scraper..."
    scrapers.append(techpoint_io_2100)

    ##ITN News Tech Sources##
    itn_io_0000 = ioScraper("ITN Tech IO 0000", site="http%3A%2F%2Fwww.itnewsafrica.com%2Fcategory%2Ftop-stories%2F&&", api_id="f3cf62eb-41e0-4cba-9a0a-54263f7323d8", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/4sjhs0d65/it_s_new_africa.png")
    print "Adding " + itn_io_0000.get_name() + " scraper..."
    scrapers.append(itn_io_0000)

    itn_io_1330 = ioScraper("ITN Tech IO 1330", site="http%3A%2F%2Fwww.itnewsafrica.com%2Fcategory%2Ftop-stories%2F&&", api_id="8ae78c39-02e9-482f-9af5-294e960ede09", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/4sjhs0d65/it_s_new_africa.png")
    print "Adding " + itn_io_1330.get_name() + " scraper..."
    scrapers.append(itn_io_1330)

    ##Ms. Techy Tech Sources
    techy_io_1330 = ioScraper("Miss Techy IO 1330", site="http%3A%2F%2Fmisstechy.com%2F&&", api_id="0b3ca1ee-b00a-40cd-8e18-3992fcbf9b5e", region="nigeria", category="Tech", db_collection=collection,
                         logo="http://s20.postimg.org/57url0z3h/misstechy_header_logo.png")
    print "Adding " + techy_io_1330.get_name() + " scraper..."
    scrapers.append(techy_io_1330)

    ##Tech Africa Sources##
    tech_africa_io = ioScraper("Tech Africa IO", site="http%3A%2F%2Ftechafri.ca%2F&&", api_id="b6abdf74-21f7-4f0d-b69d-0bcf889eff92", region="nigeria", category="Tech", db_collection=collection,
                       logo="http://techafri.ca/wp-content/uploads/2014/01/techafrica-logo-small.png")
    print "Adding " + tech_africa_io.get_name() + " scraper..."
    scrapers.append(tech_africa_io)
    
    
    
    ###################################################### BUSINESS SOUCRES ##########################################################
    
    ventures_biz = venturesScraper("Ventures Africa Business Long", api_id="6vo0hr5a", region="nigeria", category="Business", db_collection=collection,
                       logo="http://s20.postimg.org/vf0juq6qx/Ventures.png")
    print "Adding " + ventures_biz.get_name() + " scraper..."
    scrapers.append(ventures_biz)

    ventures_io_0900 = ioScraper("Ventures Africa IO 0900", site="http%3A%2F%2Fventuresafrica.com%2Fcategory%2Fbusiness%2F&&", api_id="5c28aef0-a90d-4025-bda4-6c3a682f8686", region="nigeria", category="Business", db_collection=collection, 
                        logo="http://s20.postimg.org/vf0juq6qx/Ventures.png")
    print "Adding " + ventures_io_0900.get_name() + " scraper..."
    scrapers.append(ventures_io_0900)

    ventures_io_1800 = ioScraper("Ventures Africa IO 1800", site="http%3A%2F%2Fventuresafrica.com%2Fcategory%2Fbusiness%2F&&", api_id="ac2d4502-a628-4521-b44f-b06ae49bc750", region="nigeria", category="Business", db_collection=collection, 
                        logo="http://s20.postimg.org/vf0juq6qx/Ventures.png")
    print "Adding " + ventures_io_1800.get_name() + " scraper..."
    scrapers.append(ventures_io_1800)
    
    
    vanguard_biz_io_0000 = iioScraper("Vanguard Biz IO 0000", site="http%3A%2F%2Fwww.vanguardngr.com%2Fcategory%2Fbusiness%2F&&", api_id="237441cb-8425-481b-acdb-66bb2dca0674", region="nigeria", category="Business", db_collection=collection, 
                        logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_biz_io_0000.get_name() + " scraper..."
    scrapers.append(vanguard_biz_io_0000)

    vanguard_biz_io_0900 = ioScraper("Vanguard Biz IO 0900", site="http%3A%2F%2Fwww.vanguardngr.com%2Fcategory%2Fbusiness%2F&&", api_id="a1107ea4-3050-462b-814c-966caa8420cd", region="nigeria", category="Business", db_collection=collection, 
                        logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_biz_io_0900.get_name() + " scraper..."
    scrapers.append(vanguard_biz_io_0900)

    vanguard_biz_io_1330 = ioScraper("Vanguard Biz IO 1330", site="http%3A%2F%2Fwww.vanguardngr.com%2Fcategory%2Fbusiness%2F&&", api_id="8b85b2ec-fe9b-4de8-81e7-1579e40c65c0", region="nigeria", category="Business", db_collection=collection, 
                        logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_biz_io_0000.get_name() + " scraper..."
    scrapers.append(vanguard_biz_io_0000)





    vanguard_business = Scraper("Vanguard Business", api_id="cskj1sxo", region="nigeria", category="Business", db_collection=collection,
                                logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_business.get_name() + " scraper..."
    scrapers.append(vanguard_business)
    
    punch_biz = punchScraper("Punch Business", api_id="7r88v2se", region="nigeria", category="Business", db_collection=collection,
                        logo="http://s20.postimg.org/bk9wuv25p/punchh.png")
    print "Adding " + punch_biz.get_name() + " scraper..."
    scrapers.append(punch_biz)
    
    premium_biz = Scraper("Premium Business", api_id="8lc0dzni", region="nigeria", category="Business", db_collection=collection,
                           logo="http://s20.postimg.org/5khkdgrzh/176x64xptn_logo_png_pagespeed.png")
    print "Adding " + premium_biz.get_name() + " scraper..."
    scrapers.append(premium_biz)

    today_biz = todayScraper("Today Business", api_id="5t4jj7j8", region="nigeria", category="Business", db_collection=collection,
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

    nairametrics_biz = nairametricsScraper("Nairametrics Business", api_id="alrs1xdw", region="nigeria", category="Business", db_collection=collection,
                           logo="http://nairametrics.com/wp-content/uploads/2015/10/quango115.png")
    print "Adding " + nairametrics_biz.get_name() + " scraper..."
    scrapers.append(nairametrics_biz)

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


    today_sport = todayScraper("Today Sport", api_id="6230ic18", region="nigeria", category="Sports", db_collection=collection,
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

    '''
    blackfab_fashion = Scraper("Black Fabulosity Fashion", api_id="e1l2f700", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://www.blackfabulousity.com/wp-content/uploads/2014/07/bfy-logo-2.png")
    print "Adding " + blackfab_fashion.get_name() + " scraper..."
    scrapers.append(blackfab_fashion)
    '''

    '''
    stylehq_fashion = hqScraper("Style HQ Fashion", api_id="5ho7bmf4", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://i.imgur.com/PZslF5g.png")
    print "Adding " + stylehq_fashion.get_name() + " scraper..."
    scrapers.append(stylehq_fashion)    
    '''

    onobello_fashion = Scraper("Ono Bello Fashion", api_id="97yjawcw", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://onobello.com/wp-content/uploads/2014/06/logo35.jpg")
    print "Adding " + onobello_fashion.get_name() + " scraper..."
    scrapers.append(onobello_fashion)

    
    lagos_street_fashion = lagosStreetScraper("Lagos Street Style", api_id="8tu1hpka", region="nigeria", category="Fashion", db_collection=collection,
                     logo="http://i.imgur.com/RiV9YZl.png")
    print "Adding " + lagos_street_fashion.get_name() + " scraper..."
    scrapers.append(lagos_street_fashion)



    #Food
    
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

    dooney_food = Scraper("Dooney Food", api_id="5pn5cwsu", region="nigeria", category="Food", db_collection=collection,
                     logo="http://i.imgur.com/PC0Y6ov.png")
    print "Adding " + dooney_food.get_name() + " scraper..."
    scrapers.append(dooney_food)


    #Lifestyle

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
    
    
    today_politics = todayScraper("Today Politics", api_id="5o03jioc", region="nigeria", category="Politics", db_collection=collection,
                                 logo="http://s20.postimg.org/ic4xbggj1/today.png")
    print "Adding " + today_politics.get_name() + " scraper..."
    scrapers.append(today_politics)
    
    
    vanguard_politics = Scraper("Vanguard Politics", api_id="415802o6", region="nigeria", category="Politics", db_collection=collection,
                                logo="http://s20.postimg.org/i0ea77lbh/250x55xvanguardlogo.png")
    print "Adding " + vanguard_politics.get_name() + " scraper..."
    scrapers.append(vanguard_politics)

    punch_politics = punchScraper("Punch Politics", api_id="8id0ixuu", region="nigeria", category="Politics", db_collection=collection,
                        logo="http://s20.postimg.org/bk9wuv25p/punchh.png")
    print "Adding " + punch_politics.get_name() + " scraper..."
    scrapers.append(punch_politics)
    

    #Beauty

    bnaij_beauty = Scraper("Bella Naija Beauty", api_id="81ifhajm", region="nigeria", category="Beauty", db_collection=collection,
                     logo="http://s20.postimg.org/lb78ku0ml/bellanaija_mobile.png")
    print "Adding " + bnaij_beauty.get_name() + " scraper..."
    scrapers.append(bnaij_beauty)

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

    funnyafrica_funny = Scraper("Funny Africa Funny", api_id="2jeixwo8", region="nigeria", category="Funny", db_collection=collection,
                             logo="http://i.imgur.com/ZF9Xjaa.jpg")
    print "Adding " + funnyafrica_funny.get_name() + " scraper..."
    scrapers.append(funnyafrica_funny)

    partyjollof_funny = ioScraper("Party Jollof Funny", site="http%3A%2F%2Fpartyjollof.com%2F&&" , api_id="149f2867-f608-41c2-9538-61bf0e4c7945", region="nigeria", category="Funny", db_collection=collection,
                             logo="http://partyjollof.com/wp-content/uploads/2015/12/NEW-LOGOS-RED-BRANDS_PartyJollof1.png")
    print "Adding " + partyjollof_funny.get_name() + " scraper..."
    scrapers.append(partyjollof_funny)

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


    #Travel

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

    hotels_travel = Scraper("Hotels Travel", api_id="3eoeilro", region="nigeria", category="Travel", db_collection=collection,
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
                     logo="http://myweddingnigeria.com/wp-content/uploads/2012/01/My-Wedding-Nigeria-Logo-Small.png")
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
