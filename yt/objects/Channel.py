class Channel:
    name = ""
    yt_url = ""
    notion_url = ""
    force_english = False
    videos = []

    def __init__(self, name, yt_url, notion_url, force_english):
        self.name = name
        self.yt_url = str(yt_url)
        self.notion_url = str(notion_url)
        self.force_english = force_english


### is user or channel ?
def getChannelUrlPrefix(channel_url):
    if channel_url[0:2] == "UC": channel_or_user = "channel"
    else: channel_or_user = "user"
    return channel_or_user