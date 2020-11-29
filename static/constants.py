### cool shortcuts for lazy dev ;)
line = "\n—————————————————————————————————————————————————————————————————————————————————\n"
star = "\n*********************************************************************************\n"

### Notion.so paths
notion_token = "a6ed6fe70ca4b44c588c640618b27bac91cc7a0b94847f2d2f3cb0aac19992447a4a4b459027605b8e5dd9c325d8b9b515b6056485e11ad51a39e6e30b1d0582e62aca0b1575330e15e75d74ae95"

notion_all_channels = "https://www.notion.so/5fa30b6001f3459a95a61946cee58e14?v=c6d5f6cd006748fa868a1e16eadb0875"
notion_my_playlists = "https://www.notion.so/cabda9baa7e54c2cb985b562054122b3?v=dadb592a1eca40c7a2ab2254d2c4f497"

notion_description_label = "Description"
notion_tag_name_playlists = "in playlists"
notion_colors = [ ### you can comment the ones you don't want to be elected during random color selection
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
notion_title_blank = "!!! The title of this video was blank on YouTube !!!"


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
youtube_date_formats = [
    "%d %b %Y", #date_format_fr,
    "%d %b, %Y", #date_format_fr_comma,
    "%b %d %Y", #date_format_en,
    "%b %d, %Y", #date_format_en_comma
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
### html elements
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