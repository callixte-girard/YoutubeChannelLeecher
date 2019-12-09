from static import constants as cst
from static import variables as var
from pytube import YouTube
from pytube import exceptions as py_ex
from no import collections 
import itertools
import os


def downloadVideosFromLinks(vids_urls, channel_coll, channel_name):
    vid_counter = 0
    for vid_url in vids_urls:
        vid_counter += 1
        # print(vid_url)
        full_url = cst.youtube_main_url + vid_url
        print("progress (downloading) : {} / {}".format(vid_counter, len(vids_urls)))
        ### check on Notion if video has already been downloaded or not
        row_vid = None
        while row_vid is None: ### c'est honteur de devoir faire une while aussi dégueulasse mais la nullité de cette API Notion m'y oblige.
            row_vid = collections.getCorrespondingRowFromVidUrl(channel_coll, vid_url)
        if not row_vid.downloaded and not row_vid.ignore:
            print("video at [ {} ] — [ {} ] will be downloaded ...".format(vid_url, row_vid.title))
            try: 
                download_success = attemptStreamDownload(full_url, row_vid, channel_name) ### crashes program after all attempts failed
            except: 
                print("video at [ {} ] could not be downloaded for an unknown reason :( going to next one...".format(vid_url), end=cst.line)
        else:
            print("video at [ {} ] — [ {} ] has already been downloaded.".format(vid_url, row_vid.title), end=cst.line)
    print(vid_counter, "videos have been downloaded.")
    # return vid_counter


def attemptStreamDownload(full_url, row_vid, channel_name, ignore_higher_bitrate=True):
    try:
        attempt = 0
        if ignore_higher_bitrate: attempt = 1 ### set at 1 if not otherwise specified to skip 1080p
        vid = None
        while vid is None:
            bitrate = cst.youtube_bitrates[attempt]
            vid = YouTube(full_url).streams.filter(mime_type='video/mp4', res=bitrate).first()
            attempt += 1 ### increment attempt AFTER getting bitrate from array
            print("stream obtained at attempt n°{} — [ {} ]".format(attempt, bitrate))
        ### create folder named like channel if needed
        try: open(cst.path_downloads + channel_name) ### will throw a IsADirectoryException if existing
        except IsADirectoryError: pass ### okay
        except FileNotFoundError: os.system("mkdir '{}'".format(cst.path_downloads + channel_name))
        ### try to download video, if available
        vid.download(cst.path_downloads + channel_name)
        ### mark video as downloaded in Notion
        if row_vid is not None: row_vid.downloaded = True
        print("video at [{}] has finished downloading at attempt n°{} — [ {} ]".format(full_url, attempt, bitrate), end=cst.line)
        return True
    except IndexError:
        print("video at [{}] could not be downloaded at attempt n°{}".format(full_url, attempt), end=cst.line)
        return False
    except py_ex.VideoUnavailable:
        print("video at [{}] is unavailable".format(full_url), end=cst.line)
        return False