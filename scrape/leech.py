from static import constants as cst
from static import variables as var
from static import methods as mth
from scrape import playlists
from scrape import all_videos
from scrape import infos
from scrape.insert import videoInfosInCollection
from static import collections
from objects.Channel import getChannelUrlPrefix
from objects.Video import Video
from objects.Video import getLinks
import time
from datetime import datetime


### must add manually a channel collection in Notion first.
### TODO: add somewhere assignation of videos (and consequently published_videos) of channel before updating it in Notion
def channel_or_playlist(ch, row_ch, my_playlists=False):

    if my_playlists:
        print("WILL NOW LEECH Playlist [ {} ] ...".format(ch.title), end=cst.star)
    else:
        print("WILL NOW LEECH Channel [ {} ] ...".format(ch.title), end=cst.star)


    ## get all videos links
    vids_urls = getLinks(ch.yt_url, my_playlists)
    print("total videos published in [ {} ] : {}".format(ch.title, len(vids_urls)), end=cst.star)

    ### compares old videos number with new number of videos found
    if len(vids_urls) > (row_ch.published_videos): 
        row_ch.more_vids = True
        row_ch.published_videos = len(vids_urls)
    ### records time of last inspection and update
    row_ch.updated_on = datetime.now()

    if row_ch.episodes_url != "":
        # print(">>>", type(row_ch.episodes_url), row_ch.episodes_url)
        ## if there is are new videos, scrape all videos and insert their infos in Notion
        channel_coll = collections.getCollectionFromViewUrl(row_ch.episodes_url)

        #if len(vids_urls) > len(channel_coll.get_rows()) or "Finished" not in str(row_ch.infos_status):
        # if len(vids_urls) > len(channel_coll.get_rows()) or not row_ch.indexed:
        if not row_ch.indexed:
            ### 1) playlists
            if my_playlists:
                plsts = None
            else:
                ## get all playlists links and builds playlists items from them
                plsts_urls = playlists.getPlaylistsLinksFromChannelUrl(ch.yt_url)
                print("total playlists published by {} [ {} ] : {}".format(getChannelUrlPrefix(ch.yt_url), ch.title, len(plsts_urls)), end=cst.star)
                plsts = []
                for plst_url in plsts_urls:
                    plst = playlists.getPlaylistFromUrl(plst_url, True)
                    plsts.append(plst)
                    # if not plst.title in cst.youtube_liked_videos_playlists_names: ### exclude liked videos playlist
                        ### add playlist name to in_playlists options if it doesn't already exist
                    try: 
                        collections.addNewValueToCollectionMultiSelect(ch.notion_url, cst.notion_tag_name_playlists, plst.title) ### slugifying included for prop
                        print("Property [ {} ] has been added to the playlists schema.".format(plst.title), end=cst.line)
                    except ValueError as already_exists: print(already_exists, end=cst.line)
                    # else: print("Ignoring playlist \"{}\".".format(plst.title), end=cst.line)
            ### 2) video infos
            videoInfosInCollection(ch, vids_urls, plsts)
            #row_ch.infos_status = "Finished" 
            row_ch.indexed = True
        else: 
            print("all infos are already scraped and don't need any update.")

        print("CONGRATS !!! YOU LEECHED THE CHANNEL [ {} ] !!!".format(ch.title), end=cst.star)
    else:
        print("!!! THE CHANNEL [ {} ] DOESNT HAVE AN EPISODES_URL. SKIPPING...".format(ch.title), end=cst.star)    
        
    ### THE END