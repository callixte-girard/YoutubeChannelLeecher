from static import constants as cst
from static import variables as var
from yt_vid import playlists as plst
from yt_vid import all_videos as all_v
from yt_vid import scrape_infos as inf
# from yt_dl import dl_eytd
from yt_dl import dl_pytube
from notion_so import collection as coll
from notion.block import HeaderBlock
from notion.block import TextBlock
from notion.block import DividerBlock


def leechChannelFromUrl(channel_url, cv_url): ### must add manually a channel collection in Notion first.
    collection = coll.getCollectionFromViewUrl(cv_url)

    ## - get all videos links
    vids_urls = all_v.getVideosLinksFromChannelUrl(channel_url)
    print("total videos published by user [ {} ] : {}".format(channel_url, len(vids_urls)), end=cst.star)

    ## - get all playlists links
    plsts_urls = plst.getPlaylistsLinksFromChannelUrl(channel_url)
    print("total playlists published by user [ {} ] : {}".format(channel_url, len(plsts_urls)), end=cst.star)

    ## - scrape all videos THEN download them
    vid_counter = 0
    for vid_url in vids_urls:
        vid_counter += 1
        print("progress (scraping infos) : {} / {}".format(vid_counter, len(vids_urls)))
        ## 1) check if it is already present in channel's Notion collection (from URL). If not...
        vid = coll.getCorrespondingRowFromVidUrl(collection, vid_url)
        if vid is None:
            print("video at [ {} ] doesn't exist. Let's scrape its infos.".format(vid_url))
            ## 2) ... create a Video with its url and the playlists it belongs. 
            vid = inf.scrapeVideoInfosFromLink(vid_url)
            # print("title: {} | published_on: {} —> scraped infos done :)".format(vid.title, vid.published_on), end=cst.line)
            row = collection.add_row()
            row.url = vid_url
            row.title = vid.title
            row.published_on = vid.published_on
            row.downloaded = vid.downloaded
            # row.n = 
            ### video description
            row.children.add_new(HeaderBlock, title="Decription de la vidéo")
            row.children.add_new(DividerBlock)
            row.children.add_new(TextBlock, title=vid.description)
            print("video at [ {} ] successfully scraped infos and inserted into Notion :)".format(vid_url), end=cst.line)
        else:
            print("video at [ {} ] already exists in Notion yet. Here is its title : [ {} ]".format(vid_url, vid.title), end=cst.line)
            ## 3) check if its labels are the same as the playlists it belongs. (postponed)


    print("let's download all these cool vids now !", end=cst.star)
    ## - for each video, download it if "downloaded" is unchecked on Notion. Else, skip it.
    downloaded_videos = dl_pytube.downloadVideosFromLinks(vids_urls, collection)
    ## - check "downloaded" on notion if successful. Else, leave blank.
    

    print(downloaded_videos, "videos have been downloaded.")
    print("CONGRATS !!! YOU LEECHED THE CHANNEL [", channel_url, "] !!!", end=cst.star)