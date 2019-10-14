from static import constants as cst
from static import variables as var
from static import methods as mth
from yt.scrape import scroll_down
from bs4 import BeautifulSoup as bs
import requests
from yt.objects.Playlist import Playlist


def getPlaylistsLinksFromChannelUrl(channel_name, is_channel):
    if is_channel: channel_or_user = "channel"
    else: channel_or_user = "user"

    url_playlists = "/{}/".format(channel_or_user) + channel_name + "/playlists"
    url_full = mth.reassembleUrl(cst.url_main, url_playlists)
    ### !!! remove this in all other modes !!!
    url_full = mth.addsParamsToUrl(url_full, ["view"], [1]) ### 0 = all playlists, 1 = only created by user
    
    plsts = scroll_down.untilAllElementsLoaded(url_full, True, True)
    plsts_urls = []
    for plst in plsts:
        # print(plst)

        ### get interesting info
        plst_url = plst['href']
        # print(plst_url, end=cst.line)

        plsts_urls.append(plst_url)
    return plsts_urls


def getPlaylistFromUrl(plst_url):
    full_url = mth.reassembleUrl(cst.url_main, plst_url)

    ### first scroll down
    vids = scroll_down.untilAllElementsLoaded(full_url, True, False)

    ### 1) get title
    while True:
        all_html = bs(var.driver.page_source, "html.parser")
        plst_title = all_html.find("a", attrs={"class":"yt-simple-endpoint style-scope yt-formatted-string"}).get_text()
        # print(plst_title)
        if plst_title is not None: break

    ### 2) get vids urls
    vids_urls = []
    for vid in vids :
        # print(vid, end=cst.line)

        ### get interesting info
        # vid_title = vid.get_text()
        vid_url = vid['href']

        # ### removing the list part of the url
        # ### !!! warning !!! remove this part in all other modes.
        split_index = vid_url.find('&')
        vid_url = vid_url[:split_index]
        # print(vid_url, end=cst.line)
        
        vids_urls.append(vid_url)
    
    plst = Playlist(plst_url, plst_title, vids_urls)
    return plst