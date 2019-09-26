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


def downloadVideosFromLinks(vids_urls):

    for vid_url in vids_urls:
        print("downloading video at :", vid_url)

        ### transform for y2mate
        delimiter_index = vid_url.find("=")
        full_url = cst.download_site + "/youtube/" + vid_url[delimiter_index+1:]
        # print(full_url)
        # print(disp.line)

        ### get page for video download
        driver = webdriver.Firefox()
        driver.get(full_url)


        for turn in itertools.count():
            all_html = bs(driver.page_source, "html.parser")
            tab = all_html.find_all('table', attrs={'class':'table table-bordered'})            
            if len(tab) > 0:
                # table = tab[0] ### loading is complete
                # print("turn:", turn, " | ", "table:", tab)
                
                ### do your downloading



                ### once it's done —> go to next.
                driver.quit()
                break
        
        print("download finished successfully ;-)")
        print(disp.line)
    return 