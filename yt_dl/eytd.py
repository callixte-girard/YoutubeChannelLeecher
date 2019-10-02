from my_py import disp
from my_py import read_write as rw
from my_py import download_status as dl_st
from static import constants as cst
from static import variables as var
from static import methods as mth

import asyncio
import time
import itertools
from bs4 import BeautifulSoup as bs
from slugify import slugify


def downloadVideosFromLinks(vids_urls):
    video_counter = 0
    for vid_url in vids_urls:  
        # print(vid_url)
        video_counter += 1      
        full_url = cst.url_main + vid_url
        print("preparing to download video at :", full_url)
        # print(disp.line)
        ### get page for video download
        browser = var.driver 
        browser.get(full_url) ### only working version haha
        ### wait for download button table to appear and perform dl by clicking adequate button
        while True:
            all_html = bs(browser.page_source, "html.parser")
            ### wait for the indicator to appear
            try:
                eytd_button = all_html.find('button', attrs={'id':'eytd_btn'})
                # print("der button ist:", eytd_button)
                # eytd_button.click()
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
                print("dl url will be:", dl_url)
                browser.get(dl_url)
            except: pass
            print(disp.line)
        print("video {} / {} is being downloaded ... Please be patient ...".format(video_counter, len(vids_urls)))
        ### une fois le DL lancé, faire une boucle dans le vide tant que video_filename + ".part" est présent dans ~/Downloads/
        videos_downloading = dl_st.countUnfinishedDownloads(cst.path_downloads)
        while videos_downloading >= cst.max_simultaneous_downloads: ### little slowdowner to limit nb of simlt dls
            videos_downloading = dl_st.countUnfinishedDownloads(cst.path_downloads)
        # print("video [ {} ] finished downloading successfully.".format(video_filename))
        print("{} / {} videos done !".format(video_counter, len(vids_urls)))
        print(disp.star)
    return video_counter


def getRowForQueriedBitrate(rows, q_bitrate):
    row_index = 0
    for row in rows:
        # print(row)
        # print(disp.line)
        ### [0] is headers (th)
        ### [other] : any can be 720p !
        bitrate = row.get_text()
        # print(bitrate)
        if q_bitrate in bitrate:
            # print(bitrate)
            # print(disp.line)
            return row_index
        ### increment AFTER the return
        row_index += 1        