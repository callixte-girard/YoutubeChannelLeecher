from static import constants as cst
from static import variables as var
from static import methods as mth
from yt.scrape import playlists
from yt.scrape import all_videos
from yt.scrape import infos
from yt.download import dl_pytube
from no import insert
from no import collections
from yt.objects.Channel import getChannelUrlPrefix


 ### must add manually a channel collection in Notion first.
def channel(ch, channel_row, download_videos=True):
    channel_or_user = getChannelUrlPrefix(ch.yt_url)

    ## manually change yt language to "English (US)" ?
    if ch.force_english: pass ### TODO

    ## get all videos links
    vids_urls = all_videos.getVideosLinksFromChannelUrl(ch.yt_url)
    print("total videos published by {} [ {} ] : {}".format(channel_or_user, ch.name, len(vids_urls)), end=cst.star)

    ## if there is are new videos, scrape all videos and insert their infos in Notion
    channel_coll = collections.getCollectionFromViewUrl(ch.notion_url)
    if len(vids_urls) > len(channel_coll.get_rows()) or "Finished" not in str(channel_row.infos_status):
        ## get all playlists links and builds playlists items from them
        plsts_urls = playlists.getPlaylistsLinksFromChannelUrl(ch.yt_url)
        print("total playlists published by {} [ {} ] : {}".format(channel_or_user, ch.name, len(plsts_urls)), end=cst.star)
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
        
        insert.videoInfosInCollection(ch, vids_urls, plsts, mark_all_as_downloaded = not download_videos)
        channel_row.infos_status = "Finished" 
    else: 
        print("infos are already scraped and don't need any update.")

    ## download all videos
    if download_videos and "error" not in str(channel_row.download_status):
        print("let's download all these cool vids now !", end=cst.star)
        ## for each video, download it if "downloaded" is unchecked on Notion —> then check it.
        channel_coll = collections.getCollectionFromViewUrl(ch.notion_url)
        downloaded_videos = dl_pytube.downloadVideosFromLinks(vids_urls, channel_coll)
        print(downloaded_videos, "videos have been downloaded.")
    else:
        print("videos are already downloaded.")

    print("CONGRATS !!! YOU LEECHED THE CHANNEL [ {} ] !!!".format(ch.name), end=cst.star)
    return ch