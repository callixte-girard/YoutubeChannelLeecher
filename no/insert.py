from static import constants as cst
from static import variables as var
from static import methods as mth
from no import collections
from yt.scrape import infos
from notion.block import HeaderBlock
from notion.block import TextBlock
from notion.block import DividerBlock


def videoInfosInCollection(ch, vids_urls, plsts):
    channel_coll = collections.getCollectionFromViewUrl(ch.notion_url)
    vid_counter = 0
    for vid_url in vids_urls:
        vid_counter += 1
        print("progress (scraping infos) : {} / {}".format(vid_counter, len(vids_urls)))
        ## 1) check if it is already present in channel's Notion collection (from URL). If not...
        vid = collections.getCorrespondingRowFromVidUrl(channel_coll, vid_url)
        if vid is None:
            print("video at [ {} ] doesn't exist in Notion yet. Let's scrape its infos.".format(vid_url))
            ## 2) ... create a Video with its url and the playlists it belongs.
            vid = infos.scrapeVideoInfosFromLink(vid_url)
            # print("title: {} | published_on: {} —> scraped infos done :)".format(vid.title, vid.published_on), end=cst.line)
            row = channel_coll.add_row()
            ### basic video infos
            row.url = vid_url
            row.title = vid.title
            if vid.number is not None: row.number = vid.number
            row.published_on = vid.published_on
            row.downloaded = vid.downloaded
            # row.n = 
            ### video description
            row.children.add_new(HeaderBlock, title=cst.label_description)
            row.children.add_new(DividerBlock)
            row.children.add_new(TextBlock, title=vid.description)
            ### in which playlist am I ?
            vid.in_playlists = []
            for plst in plsts:
                # print(plst.yt_url, plst.title, len(plst.vids_urls))
                if vid_url in plst.vids_urls: vid.in_playlists.append(plst.title)
            ### finally record tags
            print("here are the playlists in which this video appears :", vid.in_playlists)
            row.in_playlists = vid.in_playlists
            print("video at [ {} ] — [ {} ] successfully scraped infos and inserted into Notion :)".format(vid_url, vid.title), end=cst.line)
        else:
            print("video at [ {} ] — [ {} ] already exists in Notion.".format(vid_url, vid.title), end=cst.line)
            ## 3) check if its labels are the same as the playlists it belongs.
