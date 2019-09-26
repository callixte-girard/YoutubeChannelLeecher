from my_py import disp
from static import constants as cst
from static import methods as mth
from yt_gecko import scroll_down as scrd

from bs4 import BeautifulSoup as bs
import requests


def getPlaylistsLinksFromChannelUrl(url_channel):

    return 



def getVideosLinksFromPlaylistUrl(url_playlist):

    url_full = mth.reassembleUrl(cst.url_main, url_playlist)

    vids = scrd.untilAllVideosLoaded(url_full, True)

    vids_urls = []
    for vid in vids :
        # print(vid)

        ### go one level deeper to the <a>
        # vid_details = vid.find('a')
        # print(vid_details)
        
        ### get interesting info
        # vid_title = vid.text
        vid_url = vid['href']

        # ### removing the list part of the url
        # ### !!! warning !!! remove this part in all_videos mode.
        split_index = vid_url.find('&')
        vid_url = vid_url[:split_index]
        
        vids_urls.append(vid_url)

        print(vid_url)
        print(disp.line)

    return vids_urls
