from static import constants as cst
from static import variables as var
from static import methods as mth
from static import collections
from scrape import infos
from notion.block import HeaderBlock
from notion.block import TextBlock
from notion.block import DividerBlock


def videoInfosInCollection(ch, vids_urls, plsts):
    channel_coll = collections.getCollectionFromViewUrl(ch.notion_url)
    vid_counter = 0
    time_counter = 0
    for vid_url in vids_urls:
        ### filter forbidden urls (videos that create unhandled bugs)
        # print(vid_url, cst.skip_urls[0])
        if vid_url in cst.skip_urls:
        # if False:
            print("video at [ {} ] has been manually forbidden because it has unhandled bugs. Skipping...".format(vid_url), end=cst.line)
        else:
            vid_counter += 1
            # print("before loading")
            vid = collections.getCorrespondingRowFromVidUrl(channel_coll, vid_url)
            # print("after loading")
            print("progress (scraping infos) : {} / {}".format(vid_counter, len(vids_urls)))
            ## 1) check if it is already present in channel's Notion collection (from URL). If not...
            # print(vid)
            if vid is None:
                print("video at [ {} ] doesn't exist in Notion yet. Let's scrape its infos.".format(vid_url))
                ## 2) ... create a Video with its url and the playlists it belongs.
                vid = infos.scrapeVideoInfosFromLink(vid_url)
                # print("title: {} | published_on: {} —> scraped infos done :)".format(vid.title, vid.published_on), end=cst.line)
                row_vid = channel_coll.add_row()
                ### basic video infos
                row_vid.url = vid_url
                if vid is not None:
                    row_vid.title = vid.title
                    if vid.number is not None: row_vid.number = vid.number
                    row_vid.duration = vid.duration
                    row_vid.published_on = vid.published_on
                    ### publisher name and url
                    #if not ch.title in vid.publisher_name: row_vid.publisher = vid.publisher_name
                    # if not ch.title in vid.publisher_url: row_vid.publisher_url = vid.publisher_url
                    ### video description
                    row_vid.children.add_new(HeaderBlock, title=cst.notion_description_label)
                    row_vid.children.add_new(DividerBlock)
                    row_vid.children.add_new(TextBlock, title=vid.description)
                    if plsts is not None:
                        ### in which playlist am I ?
                        vid.in_playlists = []
                        for plst in plsts:
                            # print(plst.yt_url, plst.title, len(plst.vids_urls))
                            if vid_url in plst.vids_urls: vid.in_playlists.append(plst.title)
                        print("here are the playlists in which this video appears :", vid.in_playlists)
                        ### finally record tags
                        if vid.in_playlists != []: row_vid.in_playlists = vid.in_playlists ### to manage channels that haven't any playlist
                    print("video at [ {} ] — [ {} ] successfully scraped infos and inserted into Notion :)".format(vid_url, vid.title), end=cst.line)
                else:
                    row_vid.title = cst.notion_title_error
                    row_vid.indexed = True
                    print("video at [ {} ] encountered a problem. Recording URL in Notion and going to next.".format(vid_url), end=cst.line)
            else:
                print("video at [ {} ] already exists in Notion.".format(vid_url), end=cst.line) ### cannot show title at this moment because not scraped yet
                ## 3) check if its labels are the same as the playlists it belongs.
