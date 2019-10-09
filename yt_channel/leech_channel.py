from static import constants as cst
from static import variables as var
from static import methods as mth
from yt_vid import playlists
from yt_vid import all_videos
from yt_vid import scrape_infos
# from yt_dl import dl_eytd
from yt_dl import dl_pytube
from notion_so import collections
from notion.block import HeaderBlock
from notion.block import TextBlock
from notion.block import DividerBlock
from yt_plst import Playlist


 ### must add manually a channel collection in Notion first.
def leechChannelFromUrl(channel_url, is_channel, cv_url, download_channel=True, force_english=False):
    ## - manually change yt language to "English (UK)"
    if force_english: pass ### TODO

    ## - get all videos links
    vids_urls = all_videos.getVideosLinksFromChannelUrl(channel_url, is_channel)
    print("total videos published by user/channel [ {} ] : {}".format(channel_url, len(vids_urls)), end=cst.star)

    ## - get all playlists links and builds playlists items from them
    plsts_urls = playlists.getPlaylistsLinksFromChannelUrl(channel_url, is_channel)
    print("total playlists published by user/channel [ {} ] : {}".format(channel_url, len(plsts_urls)), end=cst.star)
    plsts = []
    for plst_url in plsts_urls:
        plst = playlists.getPlaylistFromUrl(plst_url)
        plsts.append(plst)
        ### add playlist name to in_playlists options
        try: collection.addNewValueToCollectionMultiSelect(cv_url, "In Playlists", plst.title)
        except: pass

    ## - scrape all videos THEN download them
    channel_coll = collections.getCollectionFromViewUrl(cv_url)
    vid_counter = 0
    for vid_url in vids_urls:
        vid_counter += 1
        print("progress (scraping infos) : {} / {}".format(vid_counter, len(vids_urls)))
        ## 1) check if it is already present in channel's Notion collection (from URL). If not...
        vid = collections.getCorrespondingRowFromVidUrl(channel_coll, vid_url)
        if vid is None:
            print("video at [ {} ] doesn't exist. Let's scrape its infos.".format(vid_url))
            ## 2) ... create a Video with its url and the playlists it belongs. 
            vid = scrape_infos.scrapeVideoInfosFromLink(vid_url)
            # print("title: {} | published_on: {} —> scraped infos done :)".format(vid.title, vid.published_on), end=cst.line)
            row = channel_coll.add_row()
            ### basic video infos
            row.url = vid_url
            row.title = vid.title
            row.published_on = vid.published_on
            row.downloaded = vid.downloaded
            # row.n = 
            ### video description
            row.children.add_new(HeaderBlock, title=cst.label_description)
            row.children.add_new(DividerBlock)
            row.children.add_new(TextBlock, title=vid.description)
            ### in which playlist am I ?
            for plst in plsts:
                # print(plst.yt_url, plst.title, len(plst.vids_urls))
                if vid_url in plst.vids_urls: vid.in_playlists.append(plst.title)
            ### finally record tags
            row.in_playlists = vid.in_playlists
            print("video at [ {} ] — [ {} ] successfully scraped infos and inserted into Notion :)".format(vid_url, vid.title), end=cst.line)
        else:
            print("video at [ {} ] — [ {} ] already exists in Notion.".format(vid_url, vid.title), end=cst.line)
            ## 3) check if its labels are the same as the playlists it belongs.

    if download_channel:
        print("let's download all these cool vids now !", end=cst.star)
        ## - for each video, download it if "downloaded" is unchecked on Notion —> then check it.
        downloaded_videos = dl_pytube.downloadVideosFromLinks(vids_urls, channel_coll)

    print(downloaded_videos, "videos have been downloaded.")
    print("CONGRATS !!! YOU LEECHED THE CHANNEL [", channel_url, "] !!!", end=cst.star)