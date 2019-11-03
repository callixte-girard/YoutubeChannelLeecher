class Channel:
    yt_url = ""
    notion_url = ""
    force_english = False
    videos = []

    def __init__(self, yt_url, notion_url, force_english):
        self.yt_url = str(yt_url)
        self.notion_url = str(notion_url)
        self.force_english = force_english
