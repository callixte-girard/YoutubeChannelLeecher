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


async def closeWindowWhenDownloadFinished(path, filename, window_index):
    while True:
        files = rw.readFilesInPath(path)
        if not filename + ".part" in files:
            ### close window
            browser = var.gecko_driver
            windows = browser.window_handles
            # last_window_index = len(windows)-1
            # print("last_window_index:", last_window_index)
            browser.switch_to.window( windows[window_index] )
            browser.close()
            print("video [ {} ] finished downloading".format(filename))
            ### leave function
            break



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
    ### install easy yt downloader
    # driver_gecko.install_addon(cst.extensions_path + "4fanq78o.default/extensions/" + "{b9acf540-acba-11e1-8ccb-001fd0e08bd4}.xpi", True)
    # driver_gecko.maximize_window()
    return driver_gecko

