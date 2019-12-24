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
    downloaded = False

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
