from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from yt import leech


################ DER MAIN DEBUT #####################

### MODE 1 : one by one ( that's already very long. :P )
# leech.channel("scilabus", False, "https://www.notion.so/496b868a1a154927ae2ebdb1cc2d1fdb?v=f0548ae1e0fa4414a0d88585bb208525", download_videos=False)
# leech.channel("Kurzgesagt", False, "https://www.notion.so/0a0de528e1bb4a2d94551dd856bae219?v=8bd5a6d739364e348c8c57035243b173", force_english=True)
leech.channel("UC7sXGI8p8PvKosLWagkK9wQ", True, "https://www.notion.so/62f774223ae14e9688c10977875170bb?v=89558962e1e0401493b3eb1967ac1eb8") ### Heu?Reka
leech.channel("UC8NJCimLOr_Uc4GhirgO7lg", True, "https://www.notion.so/9940558ed75f4fe5a732c43f22f4d9f8?v=77665db71fc74207ab3eb55dffdbd48d", download_videos=False) ### OTB 

### MODE 2 : loop
# for i in range(len(channels_to_leech)):

var.driver.quit()
print("————— END OF PROGRAM —————")

################# DER MAIN END ######################
