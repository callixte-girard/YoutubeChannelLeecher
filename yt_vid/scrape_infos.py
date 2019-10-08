from static import constants as cst
from static import methods as mth
from static import variables as var
from yt_vid import Video as v
from bs4 import BeautifulSoup as bs
import itertools
from datetime import datetime


### channel_name must be written exactly like in its urls. Check the channel's url on the real yt if you're not sure
def scrapeVideoInfosFromLink(vid_url):
    url_full = mth.reassembleUrl(cst.url_main, vid_url)
    print("now scraping infos for the vid [ {} ] :".format(vid_url), end=cst.star)

    browser = var.driver 
    browser.get(url_full)

    while True:
        all_html = bs(browser.page_source, "html.parser")

        title = all_html.find('h1', attrs={'class':'title style-scope ytd-video-primary-info-renderer'}).find("yt-formatted-string").get_text().strip()
        published_on = all_html.find('div', attrs={'id':'date'}).find("yt-formatted-string").get_text()
        description = all_html.find('div', attrs={'id':'description'}).find("yt-formatted-string").get_text()

        if title != "" and published_on != "" and description != "" : break

    ### lil date formatting
    spl = published_on.split(" ")
    spl[1] = spl[1][:3] ### truncate month
    published_on = " ".join(spl)
    published_on = datetime.strptime(published_on, "%d %b %Y").date()

    vid = v.Video(vid_url, title, published_on, description)
    return vid
