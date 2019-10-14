class Video:
    channel = ""
    yt_url = ""
    title = ""
    number = None
    published_on = ""
    description = ""
    in_playlists = []
    downloaded = False

    def __init__(self, yt_url, title, number, published_on, description):
        # self.channel = channel
        self.yt_url = yt_url
        self.title = title
        if number is not None and number > -1: self.number = number
        self.published_on = published_on
        self.description = description
        self.in_playlists = []
