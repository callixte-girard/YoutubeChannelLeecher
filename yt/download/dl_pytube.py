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
        full_url = cst.youtube_main_url + vid_url
        print("progress (downloading) : {} / {}".format(vid_counter, len(vids_urls)))
        ### check on Notion if video has already been downloaded or not
        row = collections.getCorrespondingRowFromVidUrl(collection, vid_url)
        if not row.downloaded:
            print("video at [ {} ] — [ {} ] will be downloaded ...".format(vid_url, row.title))
            try: 
                download_success = attemptStreamDownload(full_url, row) ### crashes program after all attempts failed
            except: 
                print("video at [ {} ] could not be downloaded for an unknown reason :( going to next one...".format(vid_url), end=cst.line)
        else:
            print("video at [ {} ] — [ {} ] has already been downloaded.".format(vid_url, row.title), end=cst.line)
    return vid_counter


def attemptStreamDownload(full_url, row):
    try:
        attempt = 0 
        vid = None
        while vid is None:
            bitrate = cst.youtube_bitrates[attempt]
            vid = YouTube(full_url).streams.filter(mime_type='video/mp4', res=bitrate).first()
            attempt += 1 ### increment attempt AFTER getting bitrate from array
            print("stream obtained at attempt n°{} — [ {} ]".format(attempt, bitrate))
        ### try to download video, if available
        vid.download(cst.path_downloads)
        ### mark video as downloaded in Notion
        row.downloaded = True
        print("video has finished downloading at attempt n°{} — [ {} ]".format(attempt, bitrate), end=cst.line)
        return True
    except IndexError:
        print("video could not be downloaded at attempt n°{}".format(attempt), end=cst.line)
        return False
    except py_ex.VideoUnavailable:
        print("video is unavailable", end=cst.line)
        return False