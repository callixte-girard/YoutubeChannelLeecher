from static import constants as cst
from static import variables as var
from pytube import YouTube
from pytube import exceptions as py_ex
from notion_so import collection as coll


def downloadVideosFromLinks(vids_urls, collection):
    vid_counter = 0
    for vid_url in vids_urls:
        # print(vid_url)
        vid_counter += 1      
        full_url = cst.url_main + vid_url
        print("progress (downloading) : {} / {}".format(vid_counter, len(vids_urls)))
        ### check on Notion if video has already been downloaded or not
        row = coll.getCorrespondingRowFromVidUrl(collection, vid_url)
        if not row.downloaded:
            print("video at [ {} ] will be downloaded ...".format(vid_url))
            ### get appropriate bitrate and format
            try:
                vid = YouTube(full_url).streams.filter(mime_type='video/mp4', res='720p').first()
                print(vid)
                ### try to download video, if available
                try:
                    vid.download(cst.path_downloads)
                    ### mark video as downloaded in Notion
                    row.downloaded = True
                    print("video has finished downloading ! :)", end=cst.line)
                except py_ex.VideoUnavailable as e:
                    print("video could not be downloaded :( here's why :", end=cst.line)
                    print(str(e))
            except:
                print("wanted bitrate does not exist...")
        else:
            print("video at [ {} ] — [ {} ] has already been downloaded.".format(vid_url, row.title), end=cst.line)
    return vid_counter