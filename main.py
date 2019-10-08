from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
test = False

### tests ###
if test:
    # url_playlist = "/playlist?list=LL4PasDd25MXqlXBogBw9CAg"
    # vids_urls = plst.getVideosLinksFromPlaylistUrl(url_playlist)
    # print(vids_urls)
    # scrape_infos.scrapeVideoInfosFromLink("/watch?v=4njWobbybnM")
    from dateutil import parser
    from datetime import datetime
    import locale
    locale.setlocale(locale.LC_TIME, "fr_FR")
    # test = parser.parse() 
    # print(test)
    date = "10 août 2019"
    date = "sept."
    date = date[:2]
    print(date)

############### DER MAIN DEBUT ####################
else:
    from static import variables as var
    from yt_channel import leech_channel as lch
    from notion_so import tests
    from yt_vid import scrape_infos
    import locale
    locale.setlocale(locale.LC_TIME, "fr_FR")

    lch.leechChannelFromUrl("scilabus", "https://www.notion.so/496b868a1a154927ae2ebdb1cc2d1fdb?v=f0548ae1e0fa4414a0d88585bb208525")

################ DER MAIN END #####################

print("————— END OF PROGRAM —————")