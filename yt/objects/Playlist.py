class Playlist:
    title = ""
    yt_url = ""
    notion_url = ""
    channel = ""
    updated_on = ""
    vids_urls = []

    def __init__(self, title, yt_url, notion_url, vids_urls):
        # self.channel = channel
        self.title = title
        self.yt_url = yt_url
        self.notion_url = notion_url
        # self.updated_on = updated_on
        self.vids_urls = vids_urls

    def __str__(self):
        l = self.title + ' @ ' + self.yt_url + " : " + "\n"
        for vid_url in self.vids_urls:
            l += vid_url + "\n"
        return l

