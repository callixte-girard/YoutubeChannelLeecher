from static import constants as cst
from static import variables as var
from yt_channel import leech_channel as lch
from notion_so import table_insert
from notion_so import tests


print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)

################ DER MAIN LOOP DEBUT ###################

## examples for testing
# url_playlist = "/playlist?list=LL4PasDd25MXqlXBogBw9CAg"
# vids_urls = plst.getVideosLinksFromPlaylistUrl(url_playlist)
# print(vids_urls)

table_insert.addNewValueToCollectionMultiSelect(
    # var.client.get_collection_view("https://www.notion.so/0a266ac37e0a4333ae9eab86596dd3bb?v=7787edb7a07d4f489a28678b3d1eff6e", force_refresh=True), ### science etonnante
    var.client.get_collection_view("https://www.notion.so/496b868a1a154927ae2ebdb1cc2d1fdb?v=f0548ae1e0fa4414a0d88585bb208525", force_refresh=True), ### scilabus
    "Playlist(s)",
    "Pipou"
)


################ DER MAIN LOOP END ###################

print("————— END OF PROGRAM —————")