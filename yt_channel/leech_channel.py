from my_py import disp
from yt_vid import playlists as plst
from yt_vid import all_videos as all_v
# from yt_dl import dl_eytd
from yt_dl import dl_pytube

def leechChannelFromUrl(channel_url, notion_url): ### must add manually a channel collection in Notion first.

    ## - get all videos links
    vids_urls = all_v.getVideosLinksFromChannelUrl(channel_url)
    print("total videos published by user [ {} ] :".format(channel_url), len(vids_urls))
    print(disp.star)

   ## - get all playlists links
    plsts_urls = plst.getPlaylistsLinksFromChannelUrl(channel_url)
    print("total playlists published by user [ {} ] :".format(channel_url), len(plsts_urls))
    print(disp.star)

    ## - for each video :
    ## 1) create a Video with its url and the playlists it belongs
    ## 2) check if it is already present in channel's Notion collection. If not, add it.
    ## 3) check if its labels are the same as the playlists it belongs. (postponed)



    print("let's download all these cool vids now !")
    print(disp.star)
    ## - for each video, download it if "downloaded" is unchecked on Notion. Else, skip it.
    downloaded_videos = dl_pytube.downloadVideosFromLinks(vids_urls)
    ## - check "downloaded" on notion if successful. Else, leave blank.
    

    print(disp.star)
    print(len(downloaded_videos), "videos have been downloaded.")
    print("CONGRATS !!! YOU LEECHED THE CHANNEL [", channel_url, "] !!!")
    print(disp.star)