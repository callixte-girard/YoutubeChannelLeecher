from my_py import disp
from static import constants as cst

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def reassembleUrl(url_prefix, url_partial):    ### must reassemble url first
    print("url before:", url_partial)
    url_full = url_prefix + url_partial
    print("url after:", url_full)
    print(disp.star)
    return url_full


def initBrowserConfiguredProperly():
    ### set preferences for file download
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.dir", cst.download_path);
    profile.set_preference("browser.download.folderList", 2);
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/mp4, video/mp4")
    ### then launch driver with these prefs
    driver_gecko = webdriver.Firefox(profile)
    return driver_gecko

