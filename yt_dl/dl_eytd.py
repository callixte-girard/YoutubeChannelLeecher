from static import constants as cst
from static import variables as var
from static import methods as mth
import asyncio
import time
import itertools
from bs4 import BeautifulSoup as bs
from slugify import slugify
from selenium.webdriver.common.action_chains import ActionChains
from os import listdir


def downloadVideosFromLinks(vids_urls):
    video_counter = 0
    for vid_url in vids_urls:  
        # print(vid_url)
        video_counter += 1      
        full_url = cst.url_main + vid_url
        print("preparing to download video at :", full_url)
        ### get page for video download
        var.driver.get(full_url) ### only working version haha
        ### wait for download button table to appear and perform dl by clicking adequate button
        while True:
            all_html = bs(var.driver.page_source, "html.parser")
            ### wait for the indicator to appear
            try:
                # eytd_button = all_html.find('button', attrs={'id':'eytd_btn'})
                # print("der button ist:", eytd_button)
                # act = ActionChains(var.driver)
                # act.click(eytd_button).perform()
                test_button = all_html.find("yt-formatted-string", text="J'ai compris")
                print("der test ist:", test_button)                
                act.click(test_button).perform()
                # eytd_button.click() ### not working !
                ### select one format : try 720p —> 360p —> take 1st available
                # dl_links = all_html.find_all('div', attrs={'class':'eytd_list_item'}) 
                dl_links = all_html.find_all('a', attrs={'target':"_blank"}) 
                # print("the dl links:", len(dl_links))
                row_index = getRowForQueriedBitrate(dl_links, '720p')
                if row_index is None: 
                    row_index = getRowForQueriedBitrate(dl_links, '360p')
                    if row_index is None:
                        row_index = 1 ### last resort : take the first one available ( [0] is headers)
                # print("row at index {} contains 720p".format(row_index))
                dl_link = dl_links[row_index]
                # print("dl link will be:", dl_link)
                # dl_link.click()
                dl_url = dl_link['href']
                if "feature=embeds_subscribe_title" in dl_url:
                    pass ### video link is not ready
                else: 
                    print("dl url will be:", dl_url, end=cst.line)
                    # var.driver.get(dl_url)
                    act = ActionChains(var.driver)
                    act.click(dl_link).perform()
                    ### sorry mah we needa leave :'(
                    # break
            except: pass
        print("video {} / {} is being downloaded ... Please be patient ...".format(video_counter, len(vids_urls)))
        ### une fois le DL lancé, faire une boucle dans le vide tant que video_filename + ".part" est présent dans ~/Downloads/
        videos_downloading = countUnfinishedDownloads(cst.path_downloads)
        # while videos_downloading > cst.max_simultaneous_downloads: ### little slowdowner to limit nb of simlt dls
            # videos_downloading = dl_st.countUnfinishedDownloads(cst.path_downloads)
        # print("video [ {} ] finished downloading successfully.".format(video_filename))
        print("video {} / {} has finished downloading ! :)".format(video_counter, len(vids_urls)), end=cst.star)
    var.driver.quit()
    return video_counter


def getRowForQueriedBitrate(rows, q_bitrate):
    row_index = 0
    for row in rows:
        # print(row)
        ### [0] is headers (th)
        ### [other] : any can be 720p !
        bitrate = row.get_text()
        # print(bitrate)
        if q_bitrate in bitrate:
            # print(bitrate)
            return row_index
        ### increment AFTER the return
        row_index += 1        


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