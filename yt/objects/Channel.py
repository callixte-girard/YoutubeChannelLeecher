class Channel:
    title = ""
    yt_url = ""
    notion_url = ""
    language = ""
    videos = []

    def __init__(self, title, yt_url, notion_url, language):
        self.title = title
        self.yt_url = yt_url
        self.notion_url = notion_url
        self.language = str(language)

def getPublishedVideos(self):
    return len(self.videos)

### is user or channel ?
def getChannelUrlPrefix(channel_url):
    if channel_url[0:2] == "UC": channel_or_user = "channel"
    else: channel_or_user = "user"
    return channel_or_user

def removeChannelUrlPrefix(channel_url):
    return channel_url.replace("channel", "").replace("user", "").replace("/", "")