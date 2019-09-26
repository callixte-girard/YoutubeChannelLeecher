from my_py import disp

import time
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs

### FOR NOW WORKS ONLY WITH ALL_VIDEOS

def getVidsFromDriver(driver, for_plst): ### if !for_plst —> all_videos
    all_html = bs(driver.page_source, "html.parser")
    # print(all_html)
    if not for_plst:
        vids = all_html.find_all('h3', attrs={'class':'style-scope ytd-grid-video-renderer'})
    else:
        # vids = all_html.find_all('div', attrs={'class':'style-scope ytd-playlist-video-renderer'})
        vids = all_html.find_all('a', attrs={'class':'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})
    vids.pop(0) ### to remove the first one, which is empty
    ### lil debug
    # for vid in vids:
    #     print(vid)
    #     print(disp.line)
    print(disp.star)
    return vids


### simulate firefox to scroll down
def untilAllVideosLoaded(url_full, for_plst):
    driver = webdriver.Firefox()
    driver.get(url_full)

    vids = getVidsFromDriver(driver, for_plst)
    loaded_init = len(vids)
    loaded_now = loaded_init

    for turn in itertools.count():
        # time.sleep(.3)
        driver.execute_script('window.scrollBy(0, 100000)')
        spin = driver.find_elements_by_id('spinnerContainer')
        try:
            # print(len(spin), "spinners")
            spinnou = spin[2] ### just suppose to throw an exc is there are only 2 spinners
            # print("turn:", turn, " | ", "spinnou:", spinnou)
            vids = getVidsFromDriver(driver, for_plst)
            loaded_now = len(vids)
            print(loaded_now, "videos loaded now ...")            
        except:
            break
        print(disp.line)

    vids = getVidsFromDriver(driver, for_plst)
    loaded_now = len(vids)
    print(loaded_now, "videos loaded at last ;-)")

    print(disp.star)
    driver.quit()
    return vids