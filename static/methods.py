from static import constants as cst
from static import variables as var
from no import collections
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import listdir


### specific to Notion
def allVidsDownloaded(row_ch):
	### V1 : download_status column
	# return row_ch.download_status is not None and "Finished" in row_ch.download_status 
	### V2 : inspect if all videos are either downloaded (OneDrive) or to be ignored
    ch_videos = collections.getCollectionFromViewUrl(row_ch.episodes_url)
    vids = ch_videos.get_rows()
    all_vids_downloaded = all(vid.downloaded or vid.ignore for vid in vids)
    return all_vids_downloaded


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
    ### install addons (adblock plus)
    options = Options()
    options.add_argument("--load-extension={}".format(cst.path_extension_adblock))
    ### sets custom download path
    # prefs = {'download.default_directory' : cst.path_downloads + "pipou/"}
    # options.add_experimental_option('prefs', prefs)
    ### try headless
    # options.set_headless(True)
    print("running headless : {}".format(options.headless))
    ### launch chromium with options
    browser = webdriver.Chrome(options=options)
    ### set half-part size for window
    browser.maximize_window()
    browser.set_window_size(browser.get_window_size()["width"]/2, browser.get_window_size()["height"])
    browser.set_window_position(0, 0)
    ### close last tab mentioning that extension is installed
    if (len(browser.window_handles)) == 2:
        browser.switch_to.window(browser.window_handles[1])
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
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