from static import constants as cst
from static import variables as var
from pytube import YouTube
from pytube import exceptions as py_ex
from no import collections 
import itertools


def downloadVideosFromLinks(vids_urls, collection):
    vid_counter = 0
    for vid_url in vids_urls:
        vid_counter += 1
        # print(vid_url)
        full_url = cst.url_main + vid_url
        print("progress (downloading) : {} / {}".format(vid_counter, len(vids_urls)))
        ### check on Notion if video has already been downloaded or not
        row = collections.getCorrespondingRowFromVidUrl(collection, vid_url)
        if not row.downloaded:
            print("video at [ {} ] — [ {} ] will be downloaded ...".format(vid_url, row.title))
            attemptStreamDownload(full_url, row, 1) ### crashes program after attempt 2 failed
        else:
            print("video at [ {} ] — [ {} ] has already been downloaded.".format(vid_url, row.title), end=cst.line)
    return vid_counter


def attemptStreamDownload(full_url, row, attempt):
    try:
        if attempt == 1: vid = YouTube(full_url).streams.filter(mime_type='video/mp4', res='720p').first()
        elif attempt == 2: vid = YouTube(full_url).streams.filter(mime_type='video/mp4').first()
        # elif attempt == 3: vid = YouTube(full_url).streams.first()
        else: raise py_ex.VideoUnavailable
        print(vid)
        ### try to download video, if available
        vid.download(cst.path_downloads)
        ### mark video as downloaded in Notion
        row.downloaded = True
        print("video has finished downloading at attempt n°{}".format(attempt), end=cst.line)
        return True
    except py_ex.VideoUnavailable:
        print("video could not be downloaded at attempt n°{}".format(attempt), end=cst.line)
        # print(e)
        return attemptStreamDownload(full_url, row, attempt + 1)