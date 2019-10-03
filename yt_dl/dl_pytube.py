from my_py import disp
from my_py import download_status as dl_st
from static import constants as cst
from static import variables as var
from pytube import YouTube


def downloadVideosFromLinks(vids_urls):
    video_counter = 0
    for vid_url in vids_urls:  
        # print(vid_url)
        video_counter += 1      
        full_url = cst.url_main + vid_url
        print("download video at :", full_url)
        vid = YouTube(full_url).streams.filter(mime_type='video/mp4', res='720p').first()
        # print(vid)
        vid.download('/Users/c/Downloads/')
        print(disp.line)
        print("video {} / {} has finished downloading ! :)".format(video_counter, len(vids_urls)))
        print(disp.star)
    return video_counter