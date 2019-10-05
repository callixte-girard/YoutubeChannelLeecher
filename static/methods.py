from static import constants as cst
from static import variables as var
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


### to assemble item url part with main root url part
def reassembleUrl(url_prefix, url_partial):    ### must reassemble url first
    print("url before:", url_partial)
    url_full = url_prefix + url_partial
    print("url after:", url_full, end=cst.star)
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

### to init gecko will cool addons
def initFirefoxConfiguredProperly():
    ### set preferences for file download
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.dir", cst.path_downloads);
    profile.set_preference("browser.download.folderList", 2);
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/mp4, video/mp4")
    ### then launch driver with these prefs
    driver_gecko = webdriver.Firefox(profile)
    ### install necesary addons
    # driver_gecko.install_addon(cst.path_extensions + "{b9acf540-acba-11e1-8ccb-001fd0e08bd4}.xpi", True) ### eytd
    # driver_gecko.install_addon(cst.path_extensions + "adguardadblocker@adguard.com.xpi", True)
    # driver_gecko.close()
    # driver_gecko.maximize_window()
    return driver_gecko
