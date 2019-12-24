from static import constants as cst
from static import methods as mth
from static import variables as var
from yt.objects.Video import Video
from yt.objects.Channel import removeChannelUrlPrefix
from bs4 import BeautifulSoup as bs
import itertools
from datetime import datetime
import locale


### channel_name must be written exactly like in its urls. Check the channel's url on the real yt if you're not sure
def scrapeVideoInfosFromLink(vid_url):
    url_full = cst.youtube_main_url + vid_url
    print("now scraping infos for the vid [ {} ] ...".format(vid_url))

    var.driver.get(url_full)

    ### wait for main elements to appear and get them
    while True:
        try:
            all_html = bs(var.driver.page_source, "html.parser")
            
            title = all_html.find('h1', attrs={'class':'title style-scope ytd-video-primary-info-renderer'}).find("yt-formatted-string").get_text().strip()
            description = all_html.find('div', attrs={'id':'description'}).find("yt-formatted-string").get_text().strip()
            duration = all_html.find('span', attrs={'class':'ytp-time-duration'}).get_text().strip()
            published_on = all_html.find('div', attrs={'id':'date'}).find("yt-formatted-string").get_text().strip()
            publisher = all_html.find('a', attrs={'class':'yt-simple-endpoint style-scope yt-formatted-string'})
            ### publisher infos
            publisher_url = removeChannelUrlPrefix(publisher['href'].strip()) ### cleans it customly too
            # publisher_name = publisher.get_text().strip()

            if title != "" and published_on != "" and publisher_url != "" and duration != "" : break ### yes, description can be blank.
        except: pass ### wait for stuff to load

    ### lil date formatting
    date_spl = published_on.split(" ")
    ### 1) get only three last parts (for example, if there is a prefix before date)
    date_spl = date_spl[len(date_spl)-3:]
    ### 2) horrible fix for juin = jui (normal) | juil = jul (july)
    month = date_spl[len(date_spl)-2]
    if "juil" in month: month = "july"
    date_spl[1] = month[:3] ### truncate month and insert it back into array
    published_on = " ".join(date_spl)
    try: ### 3)a) attempt 1 : if date is in French (with 3|4 letters then dot)
        locale.setlocale(locale.LC_TIME, "fr_FR")
        published_on = datetime.strptime(published_on, "%d %b %Y").date()
    except: ### 3)b) attempt 2 : if date is in English (3 letters without dot)
        locale.setlocale(locale.LC_TIME, "en_US")
        published_on = datetime.strptime(published_on, "%d %b %Y").date()

    ### truncate title to get episode title + episode number
    # spl = separateVideoTitleAndNumber(title)
    # if spl is not None: ### splitted has occured
    #     title = spl[0]
    #     number = spl[1]
    # else: number = None ### title stays itself : number should be None
    number = None ### default : don't analyse episode number.

    ### format duration into date
    try: duration = datetime.strptime(duration, "%M:%S").time()
    except: duration = datetime.strptime(duration, "%H:%M:%S").time()
    duration = str(duration)

    ### now create Video element with gathered infos
    vid = Video(vid_url, title, number, publisher_url, published_on, description, duration)
    return vid


def separateVideoTitleAndNumber(title_raw):
    possible_separators = [
        " - ",
        " — ", ### special hyphen (`alt + -`)
        ":",
    ]
    for sep in possible_separators:
        if sep in title_raw:
            spl = title_raw.split(sep)
            # if len(spl) == 1: return spl
            # else: ### must get last part and reassemble the others
            reassembled_title= sep.join(spl[i] for i in range(0, len(spl)-1)).strip()
            number_part = spl[len(spl)-1]
            ### try to get number, else let it None
            try:
                number_parts = number_part.split("#")
                if len(number_parts) == 1: number_parts = number_part.split(" ")
                if len(number_parts) == 1: number_parts = number_part.split("°")
                number = number_parts[len(number_parts)-1]
                number = number.replace("-", ".").replace(" ", "").replace("/", ".") ### quick fix for formatting
                number = float(number) ### conversion to number
            except:
                number = -1
            spl = [ reassembled_title, number ]            
            print("spl:", spl)
            return spl