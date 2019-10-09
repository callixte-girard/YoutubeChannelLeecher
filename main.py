from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
# test = False

from static import variables as var
from yt_channel import leech_channel as lch
from notion_so import tests
from yt_vid import scrape_infos
import locale
locale.setlocale(locale.LC_TIME, "fr_FR")

# lch.leechChannelFromUrl("scilabus", False, "https://www.notion.so/496b868a1a154927ae2ebdb1cc2dt1fdb?v=f0548ae1e0fa4414a0d88585bb208525")
# lch.leechChannelFromUrl("Kurzgesagt", False, "https://www.notion.so/2f06110eb4f642acb44750581c667430?v=efdf0a31f4cc4a98bd177fe1fdec092c", True) ### to finish
# lch.leechChannelFromUrl("UC7sXGI8p8PvKosLWagkK9wQ", True, "https://www.notion.so/2f06110eb4f642acb44750581c667430?v=efdf0a31f4cc4a98bd177fe1fdec092c") ### Heu?Reka
lch.leechChannelFromUrl("UC8NJCimLOr_Uc4GhirgO7lg", True, "https://www.notion.so/9940558ed75f4fe5a732c43f22f4d9f8?v=77665db71fc74207ab3eb55dffdbd48d") ### OTB

################ DER MAIN END #####################

print("————— END OF PROGRAM —————")