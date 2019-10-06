from static import constants as cst
from static import methods as mth
from static import variables as var
from yt_vid import Video as v
from bs4 import BeautifulSoup as bs


### channel_name must be written exactly like in its urls. Check the channel's url on the real yt if you're not sure
def scrapeVideoInfosFromLink(vid_url):
    url_full = mth.reassembleUrl(cst.url_main, vid_url)
    print("now scraping infos for the vid [ {} ] :".format(vid_url), end=cst.star)

    browser = var.driver 
    browser.get(url_full)
    all_html = bs(browser.page_source, "html.parser")

    title = all_html.find('h1', attrs={'class':'title style-scope ytd-video-primary-info-renderer'}).find("yt-formatted-string").get_text()
    added_on = all_html.find('div', attrs={'id':'date'}).find("yt-formatted-string").get_text()
    description = all_html.find('div', attrs={'id':'description'}).find("yt-formatted-string").get_text()
    print("title:", title)
    print("added_on:", added_on)
    print("description:", description)

    vid = v.Video(vid_url, title, added_on, description)
    return vid
