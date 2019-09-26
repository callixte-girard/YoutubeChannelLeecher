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
                
                ### select one format : try 720p | else, take 1st available
                # rows = all_html.find_all('tr', recursive=True, text="720p")
                rows = all_html.find_all('a', attrs={'href':'#', 'rel':'nofollow'})
                # rows = driver.find_elements_by_tag_name('tr')
                # table_html = bs(table, "html.parser")
                for row in rows:
                    # print(row)
                    # print(disp.line)
                    # print(row_soup)
                    ### [0] is headers (th)
                    ### [other] : any can be 720p !
                    # soup = bs(row)
                    bitrate = row.get_text()
                    # print(bitrate)
                    if '720p' in bitrate:
                        print(bitrate)
                        print(disp.line)
                        ### download from its parent.
                        par = row.parent() ### yeah it works !
                        print(par)
                    print(disp.star)

                ### do your downloading
                

                ### once it's done —> go to next.
                driver.quit()
                break
        
        print("download finished successfully ;-)")
        print(disp.star)
    return 