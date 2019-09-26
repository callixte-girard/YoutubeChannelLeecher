from my_py import disp
from static import constants as cst

import time
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs
import re
import pprint


def downloadVideosFromLinks(vids_urls):

    for vid_url in vids_urls:        
        ### first transform url for y2mate
        # print("downloading video at :", vid_url)
        delimiter_index = vid_url.find("=")
        full_url = cst.download_site + "/youtube/" + vid_url[delimiter_index+1:]
        print("downloading video at :", full_url)
        # print(full_url)
        # print(disp.line)

        ### get page for video download
        driver = webdriver.Firefox()
        driver.get(full_url)


        for turn in itertools.count():
            all_html = bs(driver.page_source, "html.parser")
            tab = all_html.find_all('table', attrs={'class':'table table-bordered'})            
            if len(tab) > 0:
                table = tab[0] ### loading is complete
                # print("turn:", turn, " | ", "table:", tab)
                # print(disp.line)

                rows = all_html.find_all('a', attrs={'href':'#', 'rel':'nofollow'})
                ### select one format : try 720p —> 360p —> take 1st available
                row = getRowForQueriedBitrate(rows, '720p')
                if row is None: 
                    row = getRowForQueriedBitrate(rows, '360p')
                    if row is None:
                        row = rows[0] ### last resort : take the first one available

                ### do your downloading
                print("video at [", full_url, "] will be downloaded at [", row, "]")
                print(disp.star)

                ### once it's done —> go to next.
                driver.quit()
                break
        
        print("download finished successfully ;-)")
        print(disp.star)
    return 


def getRowForQueriedBitrate(rows, q_bitrate):
    for row in rows:
        # print(row)
        # print(disp.line)
        # print(row_soup)
        ### [0] is headers (th)
        ### [other] : any can be 720p !
        # soup = bs(row)
        bitrate = row.get_text()
        # print(bitrate)
        if q_bitrate in bitrate:
            # print(bitrate)
            # print(disp.line)
            return row