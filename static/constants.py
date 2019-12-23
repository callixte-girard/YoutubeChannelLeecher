### cool shortcuts for lazy dev ;)
line = "\n—————————————————————————————————————————————————————————————————————————————————\n"
star = "\n*********************************************************************************\n"

### Notion.so paths
# notion_token = "aecb30784b091b5754d38501093f8230d4dbf60db6d7a727852a931fda4fc596c80126ece221c4b4f3910268a63425eeaf9b62c9b606d7437141d88b85d0e0a039061cdfb4d8ae172e7fef8dff75"
notion_token = "bf4044268d0760e2af9cdd98060904e3b89f6f2c413e32a0f490472cbb87351e86fcb3ed5628cc1ecb31fa092f100f6e4d62eca8d5a47fd86f22c8691cbdfc1b97013c1993afcea524375c1dea61"

notion_all_channels = "https://www.notion.so/5fa30b6001f3459a95a61946cee58e14?v=a1ea3de2e305490dafd42bf537688d81"
notion_my_playlists = "https://www.notion.so/cabda9baa7e54c2cb985b562054122b3?v=dadb592a1eca40c7a2ab2254d2c4f497"

notion_description_label = "Description"
notion_tag_name_playlists = "in playlists"
notion_colors = [
    "default",
    "gray",
    "brown",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "red",
]

### YouTube constants
youtube_main_url = "https://www.youtube.com"
youtube_bitrates = [
    "1080p", ### too high : ignored else explicitly specified (for music notably)
    "720p",
    "480p",
    "360p",
    "240p",
    "144p", ### beeeeaaark
]
youtube_liked_videos_playlists_names = [
    "Liked videos",
    "Vidéos \"J'aime\""
]
youtube_xpath_languages = '//*[@id="settings"]/ytd-account-settings/div/div[2]'
youtube_xpath_lang_from_index = '/paper-item[{}]/p'

### local paths
path_downloads = '/Users/c/Downloads/'
path_extensions = '/Users/c/Library/Application Support/BraveSoftware/Brave-Browser/Default/Extensions/'
path_extension_adblock = path_extensions + 'cfhdojbkjhnklbpkdaibdccddilifddb/3.7_0/'

### other URLs
url_y2mate = 'https://y2mate.com/fr'

### program settings
videos_number_limit = 100 ### number of videos above which channel should be ignored
attempt_get_vid_number = False