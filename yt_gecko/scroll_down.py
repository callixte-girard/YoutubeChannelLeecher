from my_py import disp

import time
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs


def getVidsFromDriver(driver):
    ### seems not really working.
    # all_html = driver.execute_script('return arguments.innerHTML')
    # all_html = driver.execute_script('return arguments[0].innerHTML')
    all_html = bs(driver.page_source)
    # print(all_html)
    vids = all_html.find_all('h3', attrs={'class':'style-scope ytd-grid-video-renderer'})
    vids.pop(0) ### to remove the first one which is empty
    print(disp.star)
    ### test ###
    vids_html = []
    for vid in vids:
        print(vid)
        # vid_html = driver.execute_script("return arguments[0].innerHTML", vid)
        # vid_html = vid.find_element_by_id('details').get_attribute('href')
        # vid_html = driver.find_element_by_css_selector('#details')
        # vid_html = 
        print(disp.line)        
        # print(vid_html)
        # vid_details = driver.execute_script("return arguments[0].getElementById('details')", vid_html)
        # print(vid_details)
        # vid_url = vid.get_attribute("href")
        # print(vid_url)
        # print(disp.star)
        vids_html.append(vid)        
    # print(vids_html)
    return vids_html

### simulate firefox to scroll down
def untilAllVideosLoaded(url_full):
    driver = webdriver.Firefox()
    driver.get(url_full)

    vids = getVidsFromDriver(driver)
    loaded_init = len(vids)
    loaded_now = loaded_init

    for turn in itertools.count():
        # time.sleep(.3)
        driver.execute_script('window.scrollBy(0, 100000)')
        spin = driver.find_elements_by_id('spinnerContainer')
        try:
            spinner = spin[1] ### this is the one with the loading symbol
            # print("turn:", turn, " | ", "spinner:", spinner)
            vids = getVidsFromDriver(driver)
            loaded_now = len(vids)
            print(loaded_now, "videos loaded now ...")            
        except:
            break
        # print(disp.line)

    vids = getVidsFromDriver(driver)
    loaded_now = len(vids)
    print(loaded_now, "videos loaded at last ;-)")

    ### not gets html from eleme
    # vids_html = 

    print(disp.star)
    driver.quit()
    return vids