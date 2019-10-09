from static import variables as var
from static import constants as cst
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs


def getEltsFromDriver(driver, for_plst, get_plst): ### if !for_plst —> all_videos
    all_html = bs(driver.page_source, "html.parser")
    # print(all_html)
    if for_plst:
        if not get_plst: ### get videos in playlist
            elts = all_html.find_all('a', attrs={'class':'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})
            elts.pop(0) ### only needed with firefox        
        else: ### get playlist 
            elts = all_html.find_all('a', attrs={'class':'yt-simple-endpoint style-scope yt-formatted-string'})
    else: ### get all videos
        elts = all_html.find_all('h3', attrs={'class':'style-scope ytd-grid-video-renderer'})
        elts.pop(0) ### only needed with firefox
    # for vid in vids:
    #     print(vid, end=cst.line)
    return elts


### simulate firefox to scroll down
def untilAllElementsLoaded(url_full, for_plst, get_plst):
    var.driver.get(url_full)
    # var.driver.execute_script("window.open('" + url_full + "', '_blank');")

    elts = getEltsFromDriver(var.driver, for_plst, get_plst)
    loaded_init = len(elts)
    loaded_now = loaded_init

    for turn in itertools.count(): ### turn is used in debug
        var.driver.execute_script('window.scrollBy(0, 100000)')
        spinners = var.driver.find_elements_by_id('spinnerContainer')
        try:
            # print(len(spin), "spinners")
            if for_plst:
                spinner = spinners[2] ### just suppose to throw an exc is there are only 2 spinners
            else:
                if not get_plst: ### normal case
                    spinner = spinners[1] ### throw an exception if only 1 spinner –> loading is complete
                else: ### shoud behave the same 
                    spinner = spinners[1]
            # print("turn:", turn, " | ", "spinner:", spinner)
            elts = getEltsFromDriver(var.driver, for_plst, get_plst)
            loaded_now = len(elts)
            print(loaded_now, "elements loaded now ...")            
        except:
            break

    elts = getEltsFromDriver(var.driver, for_plst, get_plst)
    loaded_now = len(elts)
    print(loaded_now, "elements loaded at last ;-)", end=cst.star)
    return elts
