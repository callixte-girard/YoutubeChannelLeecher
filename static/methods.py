from my_py import disp
from my_py import read_write as rw
from static import constants as cst
from static import variables as var

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from os import listdir

def isDownloadFinished(path, filename):
    files = listdir(path)
    if filename + ".part" in files: 
        return False
    else: 
        return True


def reassembleUrl(url_prefix, url_partial):    ### must reassemble url first
    print("url before:", url_partial)
    url_full = url_prefix + url_partial
    print("url after:", url_full)
    print(disp.star)
    return url_full


def initBrowserConfiguredProperly():
    ### set preferences for file download
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.dir", cst.path_downloads);
    profile.set_preference("browser.download.folderList", 2);
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/mp4, video/mp4")
    ### then launch driver with these prefs
    driver_gecko = webdriver.Firefox(profile)
    ### install necesary addons
    driver_gecko.install_addon(cst.path_extensions + "{b9acf540-acba-11e1-8ccb-001fd0e08bd4}.xpi", True)
    driver_gecko.install_addon(cst.path_extensions + "adguardadblocker@adguard.com.xpi", True)
    # driver_gecko.close()
    # driver_gecko.maximize_window()
    return driver_gecko

