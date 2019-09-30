from my_py import disp
from static import constants as cst
from static import methods as mth
from yt_dl import scroll_down as scrd

# from bs4 import BeautifulSoup as bs
import requests
import time
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


### channel_name must be written exactly like in its urls. Check the channel's url on the real yt if you're not sure
def getVideosLinksFromChannelUrl(channel_name):
    ### adds prefix and suffix
    url_channel = "/user/" + channel_name + "/videos"
    url_full = mth.reassembleUrl(cst.url_main, url_channel)

    vids = scrd.untilAllVideosLoaded(url_full, False)

    vids_urls = []
    for vid in vids :
        # print(vid)

        ### go one level deeper to the <a>
        vid_details = vid.find('a')
        # print(vid_details)
        
        ### get interesting info
        # vid_title = vid.text
        vid_url = vid_details['href']
        
        vids_urls.append(vid_url)

        # print(vid_url)
        # print(disp.line)

    return vids_urls
