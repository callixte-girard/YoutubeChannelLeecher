from my_py import disp
from static import constants as cst
from static import variables as var
from yt_channel import leech_channel as lch


print(">>> welcome to YoutubePlaylistLeecher.")
print(disp.star)

################ DER MAIN LOOP DEBUT ###################

## examples for testing
# url_playlist = "/playlist?list=LL4PasDd25MXqlXBogBw9CAg"
# vids_urls = plst.getVideosLinksFromPlaylistUrl(url_playlist)
# print(vids_urls)

lch.leechChannelFromUrl("scilabus", "put the channel's notion page url here")

################ DER MAIN LOOP END ###################

print(disp.star)
print(disp.star)
print("————— END OF PROGRAM —————")
print(disp.star)
print(disp.star)
