### cool shortcuts for lazy dev ;)
line = "\n—————————————————————————————————————————————————————————————————————————————————\n"
star = "\n*********************************************************************************\n"

### Notion.so paths
notion_token = "f391879c9ea98ebaf5d5fb4e732f66c970a55e0a17f2c1000537e8aa64c9072d2042946c9303bb81bc26b97cb69378306886cb68d1d6b871494421f372c2848643e6519957c520b409e1ec4b9709"

notion_all_channels = "https://www.notion.so/5fa30b6001f3459a95a61946cee58e14?v=c6d5f6cd006748fa868a1e16eadb0875"
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
notion_title_error = "—— Error while trying to leech video"

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
youtube_errors = [
    "Your browser does not currently recognise any of the video formats available.", ### this one's a little bastard, he's different
    "Video unavailable",
    "Private video"
]
youtube_xpath_languages = '//*[@id="settings"]/ytd-account-settings/div/div[2]'
youtube_xpath_lang_from_index = '/paper-item[{}]/p'

### local paths
path_extensions = '/Users/c/Library/Application Support/Google/Chrome/Default/Extensions'
path_extension_adblock = path_extensions + 'gighmmpiobklfepjocnamgkkbiglidom/4.22.0_0/'

#path_executable = '../../chromedriver'
path_executable = '/Users/c/Documents/Local Code/—Python/YoutubeChannelLeecher/chromedriver'


### other URLs
url_y2mate = 'https://y2mate.com/fr'

### program settings
wait_for_adblock = False
videos_number_limit = 500 ### number of videos above which channel should be ignored
attempt_get_vid_number = False
change_language = False