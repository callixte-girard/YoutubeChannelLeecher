class Video:
    channel = ""
    yt_url = ""
    in_playlists = []
    title = ""
    added_on = ""
    description = ""
    downloaded = False

    def __init__(self, channel, yt_url, in_playlists, title, added_on, description):
        self.channel = channel
        self.yt_url = yt_url
        self.in_playlists = in_playlists
        self.title = title
        self.added_on = added_on
        self.description = description
