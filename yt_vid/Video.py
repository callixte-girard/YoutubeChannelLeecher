class Video:
    channel = ""
    yt_url = ""
    title = ""
    added_on = ""
    description = ""
    in_playlists = []
    downloaded = False

    def __init__(self, yt_url, title, added_on, description):
        # self.channel = channel
        self.yt_url = yt_url
        self.title = title
        self.added_on = added_on
        self.description = description
        # self.in_playlists = in_playlists
