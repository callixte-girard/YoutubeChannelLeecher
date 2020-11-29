from static import constants as cst
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import listdir


def addParamsToUrl(url, params_names, params_values):
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
    # options.add_argument("--mute-audio")
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    # options.add_argument("window-size=1920,1080")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    #options.add_argument("--load-extension={}".format(cst.path_extension_adblock))
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    ### launch chromium with options
    browser = webdriver.Chrome(options=options, executable_path=cst.path_executable)
    # browser = webdriver.Chrome(executable_path=cst.path_executable)
    ### set half-part size for window
    browser.maximize_window()
    browser.set_window_size(browser.get_window_size()["width"]/2, browser.get_window_size()["height"])
    browser.set_window_position(0, 0)
    ### close last tab mentioning that extension is installed
    if cst.wait_for_adblock:
        while (len(browser.window_handles)) != 2:
            pass
        browser.switch_to.window(browser.window_handles[1])
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    return browser
