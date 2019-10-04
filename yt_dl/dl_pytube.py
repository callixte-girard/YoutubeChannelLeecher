from my_py import disp
from my_py import download_status as dl_st
from static import constants as cst
from static import variables as var
from pytube import YouTube
from pytube import exceptions as py_ex


def downloadVideosFromLinks(vids_urls):
    video_counter = 0
    for vid_url in vids_urls:
        # print(vid_url)
        video_counter += 1      
        full_url = cst.url_main + vid_url
        print("download video at :", full_url)
        vid = YouTube(full_url).streams.filter(mime_type='video/mp4', res='720p').first()
        print(vid)
        try:
            vid.download(cst.path_downloads)
            print("video {} / {} has finished downloading ! :-)".format(video_counter, len(vids_urls)))
        except py_ex.VideoUnavailable as e:
            print("video {} / {} could not be downloaded :-( here's why :".format(video_counter, len(vids_urls)))
            print(str(e))
        print(disp.line)
    return video_counter