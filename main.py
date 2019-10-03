from my_py import disp
from static import constants as cst
from static import variables as var
from yt_vid import playlists as plst
from yt_vid import all_videos as all_v
# from yt_dl import dl_eytd
from yt_dl import dl_pytube


print(">>> welcome to YoutubePlaylistLeecher.")
print(disp.star)

################ DER MAIN LOOP ###################

## examples for testing
# url_playlist = "/playlist?list=LL4PasDd25MXqlXBogBw9CAg"
channel_name = "DirtyBiology"
# channel_name = "scilabus"

## 1) get all videos links
# vids_urls = all_v.getVideosLinksFromChannelUrl(channel_name)
# print("total at the end :", len(vids_urls), "urls")
print(disp.star)

## 2) get all playlists links
plsts_urls = plst.getPlaylistsLinksFromChannelUrl(channel_name)

## 3) download them one by one
# print("let's download all these cool vids now !")
# downloaded_videos = dl_pytube.downloadVideosFromLinks(vids_urls)
# if downloaded_videos == len(vids_urls): ### checks that no video has been accidentally skipped

print(disp.star)
print(disp.star)
print("CONGRATS !!! YOU LEECHED THE CHANNEL [", channel_name, "] !!!")
print(disp.star)
print(disp.star)