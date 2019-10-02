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

## get links of all videos in a playlist
url_playlist = "/playlist?list=LL4PasDd25MXqlXBogBw9CAg"
channel_name = "scilabus"
## get links of all videos in channel/videos
# vids_urls = plst.getVideosLinksFromPlaylistUrl(url_playlist)
vids_urls = all_v.getVideosLinksFromChannelUrl(channel_name)

## grab their infos
# for vid_url in vids_urls:
    # print(vid_url)
    # print(disp.line)
print("total at the end :", len(vids_urls), "urls")
print("let's download all these cool people now !")
print(disp.star)

## download them one by one
downloaded_videos = dl_pytube.downloadVideosFromLinks(vids_urls)
# if downloaded_videos == len(vids_urls): ### checks that no video has been accidentally skipped

print(disp.star)
print(disp.star)
print("CONGRATS !!! YOU SCRAPED THE CHANNEL [", channel_name, "] !!!")
print(disp.star)
print(disp.star)