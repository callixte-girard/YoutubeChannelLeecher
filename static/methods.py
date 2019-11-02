from static import constants as cst
from static import variables as var
from selenium import webdriver
from os import listdir


### to assemble item url part with main root url part
def reassembleUrl(url_prefix, url_partial):    ### must reassemble url first
    # print("url before:", url_partial)
    url_full = url_prefix + url_partial
    # print("url after:", url_full, end=cst.star)
    return url_full
    
def addsParamsToUrl(url, params_names, params_values):
    if len(params_names) == len(params_values):
        url += "?"
        for i in range(len(params_names)):
            param_name = params_names[i]
            param_value = params_values[i]
            url += param_name + "=" + str(param_value) ### if it's not a string
            if i < len(params_names)-1: url += "&"
    return url

### to init browser with proper settings
def initChromiumConfiguredProperly():
    ### tells to download in a custom path and sets it
    # profile = webdriver.ChromeOptions()
    # profile.set_preference("browser.download.folderList", 0)
    # profile.set_preference("browser.download.manager.showWhenStarting", False)
    # profile.set_preference("browser.download.dir", cst.path_downloads + "pipou")
    browser = webdriver.Chrome() 
    ### set half-part size for window
    browser.maximize_window()
    browser.set_window_size(browser.get_window_size()["width"] / 2, browser.get_window_size()["height"])
    browser.set_window_position(0, 0)
    return browser

def initFirefoxConfiguredProperly():
    ### tells to download in a custom path and sets it
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 0)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", cst.path_downloads + "pipou")
    browser = webdriver.Firefox(firefox_profile=profile) 
    ### set half-part size for window
    browser.maximize_window()
    browser.set_window_size(browser.get_window_size()["width"] / 2, browser.get_window_size()["height"])
    browser.set_window_position(0, 0)
    return browser

### to count downloads
def countUnfinishedDownloads(path):
    counter = 0
    files = listdir(path)
    for file in files:
        if ".part" in file: counter += 1
    return counter

def isDownloadFinished(path, filename):
    files = listdir(path)
    if filename + ".part" in files: 
        return False
    else: 
        return True