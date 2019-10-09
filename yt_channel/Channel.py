class Channel:
    name = ""
    yt_url = ""
    is_channel = True
    notion_url = ""
    force_english = False
    videos = []
    complete = False

    def __init__(self, yt_url, is_channel, notion_url, force_english):
        self.yt_url = yt_url
        self.is_channel = is_channel
        self.notion_url = notion_url
        self.force_english = force_english
        self.complete = False
