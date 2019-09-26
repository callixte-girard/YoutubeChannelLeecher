from my_py import disp
from static import constants as cst

from pytube import YouTube


def downloadVideosFromLinks(vids_urls):

    count=0
    for vid_url in vids_urls:
        count+=1

        ### first, add youtube maix prefix
        full_url = cst.url_main + vid_url

        print(full_url)
        print(disp.line)

        ### à toi de jouer mtn :)
        

    return count == vids_urls.len()


def downloadVideosFromLinks_old(vids_urls): ### pytube version : not working

    count=0
    for vid_url in vids_urls:
        count+=1

        ### first, add youtube maix prefix
        full_url = cst.url_main + vid_url

        print(full_url)
        print(disp.line)
            
        yt = YouTube(full_url)
        strs = yt.streams.all()
        print(strs)

        # grab the video:
        video = strs.get_video('mp4', '360p')
    
        # download the video:
        video.download(cst.download_path)

    return count == vids_urls.len()
