from static import constants as cst


class Url:
    route = ""
    uri = ""
    params = {}

    def __init__(self, route="", uri="", params={}):
        self.route = route
        self.uri = uri
        self.params = params


    def full(self):
        # root = "https://www.youtube.com"
        root = cst.youtube_main_url
        full_url = root
        if self.route != "": full_url += "/" + self.route
        if self.uri != "": full_url += "/" + self.uri
        if len(self.params) > 0:
            full_url += "?"
            for index, param_name in enumerate(self.params):
                param_value = self.params[param_name]
                full_url += param_name + "=" + param_value
                if index < len(self.params)-1: full_url += "&"
        return str(full_url)


### testing
# url = Url(uri="playlist", params={"list": "pioupoupi"})
# print(type(url.full()), url.full())
