from my_py import disp
from static import constants as cst
from yt_vid import playlists as plst
from yt_vid import all_videos as all_v
from dl_vid import dl_pytube
from dl_vid import dl_y2mate
# from notion_so import tests


### main instructions ###
# 1) get all playlist videos' urls
# 2) get all titles, descriptions, dates of publishing etc
# 3) after downloading all playlists, get all undownloaded videos from channels
# 4) add error handling when video is private
### end of main instr ###

print(">>> welcome to YoutubePlaylistLeecher.")
print(disp.star)

################ DER MAIN LOOP ###################

## get links of all videos in a playlist
url_playlist = "/playlist?list=LL4PasDd25MXqlXBogBw9CAg"
channel_name = "scilabus"
## get links of all videos in channel/videos
vids_urls = plst.getVideosLinksFromPlaylistUrl(url_playlist)
# vids_urls = all_v.getVideosLinksFromChannelUrl(channel_name)

## grab their infos
for vid_url in vids_urls:
    print(vid_url)
    print(disp.line)
print("total at the end :", len(vids_urls), "urls")
print(disp.star)


## download them : NOT WORKING :(
dl_y2mate.downloadVideosFromLinks(vids_urls)