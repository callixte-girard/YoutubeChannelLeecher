from static import constants as cst
from static import variables as var
from static import methods as mth
from yt.scrape import playlists
from yt.scrape import all_videos
from yt.scrape import infos
from yt.download import dl_pytube
from no import insert
from no import collections
from yt.objects.Channel import Channel


 ### must add manually a channel collection in Notion first.
def channel(ch_name, is_channel, cv_url, force_english=False, download_videos=True):
    ## - first create Channel object
    ch = Channel(ch_name, is_channel, cv_url, force_english)

    ## - insert this channel into Notion

    ## - manually change yt language to "English (UK)" ?
    if ch.force_english: pass ### TODO

    ## - get all videos links
    vids_urls = all_videos.getVideosLinksFromChannelUrl(ch.yt_url, ch.is_channel)
    print("total videos published by user/channel [ {} ] : {}".format(ch.yt_url, len(vids_urls)), end=cst.star)

    ## - get all playlists links and builds playlists items from them
    plsts_urls = playlists.getPlaylistsLinksFromChannelUrl(ch.yt_url, ch.is_channel)
    print("total playlists published by user/channel [ {} ] : {}".format(ch.yt_url, len(plsts_urls)), end=cst.star)
    plsts = []
    for plst_url in plsts_urls:
        plst = playlists.getPlaylistFromUrl(plst_url)
        plsts.append(plst)
        if not plst.title in cst.youtube_liked_videos_playlists_names: ### exclude liked videos playlist
            ### add playlist name to in_playlists options if it doesn't already exist
            try: 
                collections.addNewValueToCollectionMultiSelect(ch.notion_url, cst.notion_tag_name_playlists, plst.title) ### slugifying included for prop
                print("\"{}\" has been added to the schema.".format(plst.title), end=cst.line)
            except ValueError as already_exists: print(already_exists, end=cst.line)
        else: print("Ignoring playlist \"{}\".".format(plst.title), end=cst.line)

    ## - scrape all videos and insert their infos in Notion
    insert.videoInfosInCollection(ch, vids_urls, plsts)
    
    ## - download all videos
    if download_videos:
        print("let's download all these cool vids now !", end=cst.star)
        ## - for each video, download it if "downloaded" is unchecked on Notion —> then check it.
        channel_coll = collections.getCollectionFromViewUrl(ch.notion_url)
        downloaded_videos = dl_pytube.downloadVideosFromLinks(vids_urls, channel_coll)
        print(downloaded_videos, "videos have been downloaded.")

    ## - mark channel as finished on Notion
    ######
    print("CONGRATS !!! YOU LEECHED THE CHANNEL [", ch.yt_url, "] !!!", end=cst.star)
    return ch