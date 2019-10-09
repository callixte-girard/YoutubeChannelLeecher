class Playlist:
    channel = ""
    yt_url = ""
    title = ""
    updated_on = ""
    vids_urls = []

    def __init__(self, yt_url, title, vids_urls):
        # self.channel = channel
        self.yt_url = yt_url
        self.title = title
        # self.updated_on = updated_on
        self.vids_urls = vids_urls

    def __call__(self, yt_url, title):
        pass