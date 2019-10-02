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
        print("preparing to download video at :", full_url)
        vid = YouTube("https://www.youtube.com/watch?v=7HAGjU9Ldx4").streams.filter(mime_type='video/mp4', res='720p').first()
        print(vid)
        vid.download('/Users/c/Downloads/')
        print(disp.line)
        # print("video {} / {} is being downloaded ... Please be patient ...".format(video_counter, len(vids_urls)))
        ### une fois le DL lancé, faire une boucle dans le vide tant que video_filename + ".part" est présent dans ~/Downloads/
        videos_downloading = dl_st.countUnfinishedDownloads(cst.path_downloads)
        # while videos_downloading > cst.max_simultaneous_downloads: ### little slowdowner to limit nb of simlt dls
            # videos_downloading = dl_st.countUnfinishedDownloads(cst.path_downloads)
        # print("video [ {} ] finished downloading successfully.".format(video_filename))
        print("video {} / {} has finished downloading ! :)".format(video_counter, len(vids_urls)))
        print(disp.star)
    return video_counter