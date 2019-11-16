from static import constants as cst
from static import variables as var
from static import methods as mth
from yt.scrape import playlists
from yt.scrape import all_videos
from yt.scrape import infos
from yt.download import dl_pytube
from no import insert
from no import collections
from yt.objects.Channel import getChannelUrlPrefix
import time


 ### must add manually a channel collection in Notion first.
def channel(ch, channel_row, download_videos=True):
    print("WILL NOW LEECH THE CHANNEL [ {} ] ...".format(ch.name), end=cst.star)

    ## first change yt language to the desired one
    ### click yt settings button
    btns = var.driver.find_elements_by_id("button")
    settings_button = next(btn for btn in btns if "Settings" in str(btn.get_attribute("aria-label")))
    settings_button.click()
    ### click change language
    change_language = var.driver.find_element_by_xpath('//*[@id="language"]')
    change_language.click()
    ### get available languages
    available_languages = None
    while available_languages is None:
        try: available_languages = var.driver.find_element_by_xpath(cst.youtube_xpath_languages)
        except: pass
    # print("available : {}".format(available_languages))
    ### click desired language
    lang_index = 0 ### LANGUAGES INDEXES START AT 1 !!!!!
    while True:
        try:
            lang_index += 1
            lang = var.driver.find_element_by_xpath(cst.youtube_xpath_languages + cst.youtube_xpath_lang_from_index.format(lang_index))
            print("lang n°{} : {}".format(lang_index, lang.text))
            if len(ch.language) > 0 and ch.language in lang.text: 
                desired_language = lang
                break
        except:
            print("!!! THE LANGUAGE FOR THIS CHANNEL DOES NOT SEEM TO EXIST ON YOUTUBE — PLEASE DOUBLE CHECK !!!")
            raise
    desired_language.click()

    ## get all videos links
    vids_urls = all_videos.getVideosLinksFromChannelUrl(ch.yt_url)
    print("total videos published by {} [ {} ] : {}".format(getChannelUrlPrefix(ch.yt_url), ch.name, len(vids_urls)), end=cst.star)

    ## if there is are new videos, scrape all videos and insert their infos in Notion
    channel_coll = collections.getCollectionFromViewUrl(ch.notion_url)
    if len(vids_urls) > len(channel_coll.get_rows()) or "Finished" not in str(channel_row.infos_status):
        ## get all playlists links and builds playlists items from them
        plsts_urls = playlists.getPlaylistsLinksFromChannelUrl(ch.yt_url)
        print("total playlists published by {} [ {} ] : {}".format(getChannelUrlPrefix(ch.yt_url), ch.name, len(plsts_urls)), end=cst.star)
        plsts = []
        for plst_url in plsts_urls:
            plst = playlists.getPlaylistFromUrl(plst_url)
            plsts.append(plst)
            if not plst.title in cst.youtube_liked_videos_playlists_names: ### exclude liked videos playlist
                ### add playlist name to in_playlists options if it doesn't already exist
                try: 
                    collections.addNewValueToCollectionMultiSelect(ch.notion_url, cst.notion_tag_name_playlists, plst.title) ### slugifying included for prop
                    print("\"{}\" has been added to the schema.".format(plst.title), end=cst.line)
                except ValueError as already_exists: print(already_exists, end=cst.line)
            else: print("Ignoring playlist \"{}\".".format(plst.title), end=cst.line)
        
        insert.videoInfosInCollection(ch, vids_urls, plsts, mark_all_as_downloaded = not download_videos)
        channel_row.infos_status = "Finished" 
    else: 
        print("all infos are already scraped and don't need any update.")

    ## download all videos
    # if download_videos and "error" not in str(channel_row.download_status):
    if True:
        print("let's download all these cool vids now !", end=cst.star)
        ## for each video, download it if "downloaded" is unchecked on Notion —> then check it.
        downloaded_videos = dl_pytube.downloadVideosFromLinks(vids_urls, channel_coll, ch.name)
        print(downloaded_videos, "videos have been downloaded.")
    else:
        print("all videos are already downloaded.")

    print("CONGRATS !!! YOU LEECHED THE CHANNEL [ {} ] !!!".format(ch.name), end=cst.star)
    return ch