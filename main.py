from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from yt import leech
import itertools

################ DER MAIN DEBUT #####################
def app():
	### I)a) channels already downloaded : redo table with intelligent video index detected
	# leech.channel("UC8NJCimLOr_Uc4GhirgO7lg", True, "https://www.notion.so/9940558ed75f4fe5a732c43f22f4d9f8?v=77665db71fc74207ab3eb55dffdbd48d", download_videos=False) ### OTB 
	### I)b) channels already downloaded : redo table in English (for later)
	# leech.channel("Kurzgesagt", False, "https://www.notion.so/0a0de528e1bb4a2d94551dd856bae219?v=8bd5a6d739364e348c8c57035243b173", force_english=True)
	### I)c) channels already downloaded
	# leech.channel("UC7sXGI8p8PvKosLWagkK9wQ", True, "https://www.notion.so/62f774223ae14e9688c10977875170bb?v=89558962e1e0401493b3eb1967ac1eb8") ### Heu?Reka
	# leech.channel("UCcueC-4NWGuPFQKzQWn5heA", True, "https://www.notion.so/03b597b7607c4728bcb570e814e02a99?v=2396f2f45e3c4c4e97da84321f486d5e") ### Victor Ferry
	### I)d) channels already downloaded but with some mysterious errors somewhere
	leech.channel("UCLXDNUOO3EQ80VmD9nQBHPg", True, "https://www.notion.so/1a9d23934b244ca6be4c2085a5b7a231?v=5a0aa53c5ca640e4be2130b142447257") ### Fouloscopie
	### II) channels that need the program to be adjusted to work correctly
	# leech.channel("Micmaths", False, "https://www.notion.so/930c45af3d1a401b952b0a1da57fb02d?v=9afa56a8a17641e99b4db486e81e3f80")
	### III) channels remaining to download

app()
# for i in itertools.count():
# 	try:
# 		app()
# 	except:
# 		if i > cst.max_retries: break
# 		else: app()

var.driver.quit()
print("————— END OF PROGRAM —————")

################# DER MAIN END ######################
