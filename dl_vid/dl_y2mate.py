from my_py import disp
from my_py import read_write as rw
from static import constants as cst
from static import variables as var
from static import methods as mth

import asyncio
import time
import itertools
from bs4 import BeautifulSoup as bs
# import re
# import pprint


def downloadVideosFromLinks(vids_urls):
    video_counter = 0
    for vid_url in vids_urls:  
        video_counter += 1      
        ### first transform url for y2mate
        # print(vid_url)
        delimiter_index = vid_url.find("=")
        full_url = cst.url_y2mate + "/youtube/" + vid_url[delimiter_index+1:]
        # full_url = cst.url_main + vid_url
        print("downloading video at :", full_url)
        # print(disp.line)

        ### get page for video download
        browser = var.gecko_driver
        # browser.execute_script("window.open('" + full_url + "', '_blank');") ### SHIT DOESNT WORK
        # browser.find_element_by_tag_name('body').send_keys(mth.Keys.chord(mth.Keys.COMMAND, 't')) ### fucking shit don't work !!!     
        browser.get(full_url) ### only working version haha
        # windows = browser.window_handles
        # last_window_index = len(windows)-1
        # print("last_window_index:", last_window_index)
        
        while True: ### wait for download button table to appear and perform dl by clicking adequate button
            all_html = bs(browser.page_source, "html.parser")
            indicator = all_html.find_all('table', attrs={'class':'table table-bordered'})            
            # indicator = all_html.find_all('button', attrs={'id':'eytd_btn'})            
            ### wait for the indicator to appear
            if len(indicator) > 0:
                ### select one format : try 720p —> 360p —> take 1st available
                dl_links = all_html.find_all('a', attrs={'href':'#', 'rel':'nofollow'}) ### includes header
                row_index = getRowForQueriedBitrate(dl_links, '720p')
                if row_index is None: 
                    row_index = getRowForQueriedBitrate(dl_links, '360p')
                    if row_index is None:
                        row_index = 1 ### last resort : take the first one available ( [0] is headers)
                
                ### find download button
                # dl_button = browser.find_element_by_id("eytd_btn")
                dl_button = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div[4]/div[1]/div[2]/div/div[1]/table/tbody/tr[" 
                    + str(row_index) 
                    + "]/td[3]/a"
                )
                video_filename = dl_button.get_attribute("download")

                ### now tries to download, else, close the banner and try again
                try:
                    dl_button.click()
                    break ### leave infinite loop as soon as download started !
                except:
                    banner_close = browser.find_element_by_xpath(
                        "/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div[4]/div[3]/div[2]/div/div[3]"
                    )
                    banner_close.click()

        ### une fois le DL lancé, faire une boucle dans le vide tant que video_filename + ".part" est présent dans ~/Downloads/
        print("video [ {} ] is being downloaded ... Please be patient ...".format(video_filename))
        downloadFinished = False
        while not downloadFinished:
            downloadFinished = mth.isDownloadFinished(cst.path_downloads, video_filename)
        print("video [ {} ] finished downloading successfully.".format(video_filename))
        print("{} / {} videos done !".format(video_counter, len(vids_urls)))
        print(disp.line)
    return video_counter


def getRowForQueriedBitrate(rows, q_bitrate):
    row_index = 0
    for row in rows:
        row_index += 1
        # print(row)
        # print(disp.line)
        # print(row_soup)
        ### [0] is headers (th)
        ### [other] : any can be 720p !
        # soup = bs(row)
        bitrate = row.get_text()
        # print(bitrate)
        if q_bitrate in bitrate:
            # print(bitrate)
            # print(disp.line)
            return row_index