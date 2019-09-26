from my_py import disp
from static import constants as cst
from yt_vid import playlists as plst
from yt_vid import all_videos as all_v
from yt_vid import download
# from notion_so import tests


### main instructions ###
# 1) get all playlist videos' urls
# 2) get all titles, descriptions, dates of publishing etc
# 3) after downloading all playlists, get all undownloaded videos from channels
### end of main instr ###

print(">>> welcome to YoutubePlaylistLeecher.")
print(disp.star)

################ DER MAIN LOOP ###################

## get links of all videos in a playlist
url_playlist = "/playlist?list=PLNefH6S6myiOfykOcgIc2sYrpr1Zk5Mhi"
channel_name = "scilabus"
## get links of all videos in channel/videos
# plst_vids_urls = plst.getVideosLinksFromPlaylistUrl(url_playlist)
all_vids_urls = all_v.getVideosLinksFromChannelUrl(channel_name)

## grab their infos
for vid in all_vids_urls:
    print(vid)
    print(disp.line)
print(len(all_vids_urls))


## download them : NOT WORKING :(
# download.downloadVideosFromLinks(vids_urls)