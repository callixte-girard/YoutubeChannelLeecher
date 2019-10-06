class Channel:
    name = ""
    notion_url = ""
    videos = []
    complete = False

    def __init__(self, name, notion_url, videos):
        self.name = name
        self.notion_url = notion_url
        self.videos = videos


channels_urls = [
    # "fauxsceptique" ### DONE
    # "DirtyBiology" ### DONE
    "Micmaths"
    "Kurzgesagt",
    "scilabus",
]