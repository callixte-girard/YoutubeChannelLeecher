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
        video_counter += 1      
        ### first transform url for y2mate
        # print(vid_url)
        delimiter_index = vid_url.find("=")
        full_url = cst.url_y2mate + "/youtube/" + vid_url[delimiter_index+1:]
        # full_url = cst.url_main + vid_url
        print("preparing to download video at :", full_url)
        # print(disp.line)

        ### get page for video download
        browser = var.gecko_driver
        # browser.execute_script("window.open('" + full_url + "', '_blank');") ### SHIT DOESNT WORK
        # browser.find_element_by_tag_name('body').send_keys(mth.Keys.chord(mth.Keys.COMMAND, 't')) ### fucking shit don't work !!!     
        browser.get(full_url) ### only working version haha
        # windows = browser.window_handles
        # last_window_index = len(windows)-1
        # print("last_window_index:", last_window_index)

        ### wait for download button table to appear and perform dl by clicking adequate button
        while True: 
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
                dl_button_xpath = "/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div[4]/div[1]/div[2]/div/div[1]/table/tbody/tr[{}]/td[3]/a".format(str(row_index))
                dl_button = browser.find_element_by_xpath(dl_button_xpath)
                video_filename = dl_button.get_attribute("download")
                ## quick fix to avoid error with forbidden characters in filenames like '?' for example.
                # delimiter_index = video_filename.find('.mp4')
                # video_filename = video_filename[:delimiter_index]
                # video_filename = slugify(video_filename) + ".mp4"
                ## reinsert back. ### not working, sniffff :'(
                # browser.execute_script("arguments[0].setAttribute('{}','{}')".format("download", video_filename), dl_button)
                # print("dl_button:", dl_button.get_attribute("download"))
                ### now tries to download, else, close the banner and try again
                try:
                    dl_button.click()
                    break ### leave infinite loop as soon as download started !
                except:
                    banner_xpath = "/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div[4]/div[3]/div[2]/div/div[3]"
                    banner_close = browser.find_element_by_xpath(banner_xpath)
                    banner_close.click()

        ### une fois le DL lancé, faire une boucle dans le vide tant que video_filename + ".part" est présent dans ~/Downloads/
        print("video {} / {} — [ {} ] is being downloaded ... Please be patient ...".format(video_counter, len(vids_urls), video_filename))
        ### wait for download to have started then close WINDOW
        videos_downloading = dl_st.countUnfinishedDownloads(cst.path_downloads)
        # while videos_downloading != videos_downloading_before + 1:
        #     videos_downloading = dl_st.countUnfinishedDownloads(cst.path_downloads)
        # windows = browser.window_handles
        # last_window_index = len(windows)
        # print("last_window_index:", last_window_index)
        # browser.switch_to.window(windows[last_window_index-1])
        # browser.close()
        ### little slowdowner to limit nb of simlt dls
        while videos_downloading >= cst.max_simultaneous_downloads:
            # next_video = dl_st.isDownloadFinished(cst.path_downloads, video_filename)
            videos_downloading = dl_st.countUnfinishedDownloads(cst.path_downloads)
        # print("video [ {} ] finished downloading successfully.".format(video_filename))
        # print("{} / {} videos done !".format(video_counter, len(vids_urls)))
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