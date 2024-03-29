from static import constants as cst
from static import variables as var
from static import methods as mth
from scrape import scroll_down
from objects.Channel import getChannelUrlPrefix


### channel_name must be written exactly like in its urls. Check the channel's url on the real yt if you're not sure
def getVideosLinksFromChannelUrl(channel_url):
    channel_or_user = getChannelUrlPrefix(channel_url)
    
    url_all_videos = "/{}/".format(channel_or_user) + channel_url + "/videos"
    url_full = cst.youtube_main_url + url_all_videos

    vids = scroll_down.untilAllElementsLoaded(url_full, False, False)

    vids_urls = []
    for vid in vids :
        # print(vid)

        ### go one level deeper to the <a>
        vid_details = vid.find('a')
        # print(vid_details)
        
        ### get interesting info
        # vid_title = vid.text
        vid_url = vid_details['href']
        # print(vid_url, end=cst.line)
        
        vids_urls.append(vid_url)
    return vids_urls
