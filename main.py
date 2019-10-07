from static import constants as cst
from static import variables as var
from yt_channel import leech_channel as lch
from notion_so import table_insert
from notion_so import tests
from yt_vid import scrape_infos

print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)

### tests ###
# url_playlist = "/playlist?list=LL4PasDd25MXqlXBogBw9CAg"
# vids_urls = plst.getVideosLinksFromPlaylistUrl(url_playlist)
# print(vids_urls)
# scrape_infos.scrapeVideoInfosFromLink("/watch?v=4njWobbybnM")

############### DER MAIN LOOP DEBUT ####################

lch.leechChannelFromUrl("scilabus", "https://www.notion.so/496b868a1a154927ae2ebdb1cc2d1fdb?v=f0548ae1e0fa4414a0d88585bb208525")

################ DER MAIN LOOP END #####################

print("————— END OF PROGRAM —————")