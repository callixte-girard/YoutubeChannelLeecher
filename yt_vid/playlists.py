from static import constants as cst
from static import methods as mth
from yt_dl import scroll_down as scrd
from bs4 import BeautifulSoup as bs
import requests


def getPlaylistsLinksFromChannelUrl(channel_name):
    url_playlists = "/user/" + channel_name + "/playlists"
    url_full = mth.reassembleUrl(cst.url_main, url_playlists)
    ### !!! remove this in all other modes !!!
    url_full = mth.addsParamsToUrl(url_full, ["view"], [1]) ### 0 = all playlists, 1 = only created by user

    plsts = scrd.untilAllElementsLoaded(url_full, True, True)

    plsts_urls = []
    for plst in plsts:
        # print(plst)

        ### get interesting info
        plst_url = plst['href']
        # print(plst_url, end=cst.line)

        plsts_urls.append(plst_url)
    return plsts_urls


def getVideosLinksFromPlaylistUrl(url_playlist):
    url_full = mth.reassembleUrl(cst.url_main, url_playlist)
    vids = scrd.untilAllElementsLoaded(url_full, True, False)

    vids_urls = []
    for vid in vids :
        # print(vid)

        ### get interesting info
        # vid_title = vid.text
        vid_url = vid['href']

        # ### removing the list part of the url
        # ### !!! warning !!! remove this part in all other modes.
        split_index = vid_url.find('&')
        vid_url = vid_url[:split_index]
        # print(vid_url, end=cst.line)

        vids_urls.append(vid_url)
    return vids_urls
