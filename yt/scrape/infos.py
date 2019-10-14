from static import constants as cst
from static import methods as mth
from static import variables as var
from yt.objects.Video import Video
from bs4 import BeautifulSoup as bs
import itertools
from datetime import datetime


### channel_name must be written exactly like in its urls. Check the channel's url on the real yt if you're not sure
def scrapeVideoInfosFromLink(vid_url):
    url_full = mth.reassembleUrl(cst.url_main, vid_url)
    print("now scraping infos for the vid [ {} ] ...".format(vid_url))

    var.driver.get(url_full)
    while True:
        all_html = bs(var.driver.page_source, "html.parser")

        title = all_html.find('h1', attrs={'class':'title style-scope ytd-video-primary-info-renderer'}).find("yt-formatted-string").get_text().strip()
        published_on = all_html.find('div', attrs={'id':'date'}).find("yt-formatted-string").get_text()
        description = all_html.find('div', attrs={'id':'description'}).find("yt-formatted-string").get_text()

        if title != "" and published_on != "" and description != "" : break

    ### lil date formatting
    date_spl = published_on.split(" ")
    month = date_spl[1]
    ### horrible fix for juin = jui (normal) | juil = jul (july)
    if "juil" in month: month = "july"
    ### truncate month and insert it back into array
    date_spl[1] = month[:3] 
    published_on = " ".join(date_spl)
    published_on = datetime.strptime(published_on, "%d %b %Y").date()
    ### truncate title to get episode title + episode number

    vid = Video(vid_url, title, published_on, description)
    return vid
