from scrape import playlists
from scrape import all_videos


class Video:
    publisher_name = ""
    publisher_url = ""
    yt_url = ""
    title = ""
    number = None
    published_on = ""
    description = ""
    duration = 0
    in_playlists = []

    def __init__(self, yt_url, title, number, publisher_name, published_on, description, duration):
        self.yt_url = yt_url
        self.title = title
        if number is not None and number > -1: self.number = number
        # self.publisher_url = publisher_url
        self.publisher_name = publisher_name
        self.published_on = published_on
        self.description = description
        self.duration = duration
        self.in_playlists = []


def getLinks(url, my_playlists):
    if my_playlists:
        plst = playlists.getPlaylistFromUrl(url, absolute_url=True)
        vids_urls = plst.vids_urls
    else:
        vids_urls = all_videos.getVideosLinksFromChannelUrl(url)
    return vids_urls