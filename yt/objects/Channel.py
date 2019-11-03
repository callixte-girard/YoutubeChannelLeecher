class Channel:
    yt_url = ""
    force_english = False
    videos = []

    def __init__(self, yt_url, force_english):
        self.yt_url = yt_url
        self.force_english = force_english
