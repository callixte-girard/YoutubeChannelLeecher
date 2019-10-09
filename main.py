from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)

from static import variables as var
from yt_channel import leech_channel
from yt_channel.Channel import Channel
from yt_vid import scrape_infos
import locale
locale.setlocale(locale.LC_TIME, "fr_FR")

################ DER MAIN DEBUT #####################

scilabus = Channel("scilabus", False, "https://www.notion.so/496b868a1a154927ae2ebdb1cc2d1fdb?v=f0548ae1e0fa4414a0d88585bb208525", False)
kurzgesagt = Channel("Kurzgesagt", False, "https://www.notion.so/2f06110eb4f642acb44750581c667430?v=efdf0a31f4cc4a98bd177fe1fdec092c", True)
heureka = Channel("UC7sXGI8p8PvKosLWagkK9wQ", True, "https://www.notion.so/2f06110eb4f642acb44750581c667430?v=efdf0a31f4cc4a98bd177fe1fdec092c", False)
otb = Channel("UC8NJCimLOr_Uc4GhirgO7lg", True, "https://www.notion.so/9940558ed75f4fe5a732c43f22f4d9f8?v=77665db71fc74207ab3eb55dffdbd48d", False)

### MODE 1 : one by one ( that's already very long. :P )
leech_channel.leechChannel(scilabus, False)
leech_channel.leechChannel(kurzgesagt, False)
leech_channel.leechChannel(heureka)
leech_channel.leechChannel(otb)

### MODE 2 : loop
# for i in range(len(channels_to_leech)):

var.driver.quit()

################# DER MAIN END ######################

print("————— END OF PROGRAM —————")