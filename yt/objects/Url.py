from static import constants as cst


class Url:
    route = ""
    end = ""
    params = {}

    def __init__(self, route="", end="", params={}):
        self.route = route
        self.end = end
        self.params = params


    def full(self):
        # root = "https://www.youtube.com"
        root = cst.youtube_main_url
        full_url = root
        if self.route is not (None or ""): full_url += "/" + self.route
        if self.end is not (None or ""): full_url += "/" + self.end
        if len(self.params) > 0:
            full_url += "?"
            for index, param in enumerate(self.params):
                full_url += param + "=" + self.params[param]
                if index < len(self.params)-1: full_url += "&"
        return full_url


### testing
# url = Url("playlists", "pipou")
# print(url.full())