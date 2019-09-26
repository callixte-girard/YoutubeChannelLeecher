from my_py import disp
from static import constants as cst

import pytube


def downloadVideosFromLinks(vids_urls):

    for vid_url in vids_urls:
        print("downloading video at :", vid_url)

        ### first, add youtube main prefix
        full_url = cst.url_main + vid_url

        # print(full_url)
        # print(disp.line)

        ### à toi de jouer mtn :)
        # pytube.YouTube(full_url).streams.first().download('/Users/c/Downloads')
        pytube.YouTube(full_url).streams.first().download('/Users/c/Downloads')
        
        print("download finished successfully ;-)")
        print(disp.line)
    return 

