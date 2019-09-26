from my_py import disp
from static import constants as cst
from static import methods as mth

from bs4 import BeautifulSoup as bs
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

    ### simulate firefox to scroll down
    driver = webdriver.Firefox()
    driver.get(url_full)
        
    ### loop infinitely on scroll down and stop only when prev elts number === next elts number
    delay = 0
    delays = []

    vids = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    loaded_init = len(vids)
    loaded_now = loaded_init
    loaded_prev = 0

    for turn in itertools.count():
        # time.sleep(.3)
        driver.execute_script('window.scrollBy(0, 100000)')
        spin = driver.find_elements_by_id('spinnerContainer')
        try:
            spinner = spin[1]
            # print("turn:", turn, " | ", "spinner:", spinner)
            vids = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
            loaded_now = len(vids)
            print(loaded_now, "videos loaded now ...")            
        except:
            break
        print(disp.line)

    vids = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    loaded_now = len(vids)
    print(loaded_now, "videos loaded at last ;-)")
    driver.quit()

    # find_elements_by_class_name('yt-lockup-title')
    # print(vids)

    ### simple classical BS version
    # r  = requests.get(url_full)
    # page = r.text
    # soup = bs(page, "html.parser")

    # vids = soup.findAll('h3', attrs={'class':'yt-lockup-title'},)
    # print(vids)

    vids_urls = []
    for vid in vids :
        print(vid)

        ### go one level deeper to the <a>
        vid = vid.find('a')
        
        ### get interesting info
        # vid_title = vid.text
        vid_url = vid['href']

        ### lil formatting
        vid_url = vid_url.replace('\n', '')
        vid_url = vid_url.strip(' ')
        
        vids_urls.append(vid_url)

        print(vid_url)
        print(disp.line)

    return vids_urls
