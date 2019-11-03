from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from yt import leech
from no import collections
import itertools

################ DER MAIN DEBUT #####################
def app():
	collection = collections.getCollectionFromViewUrl(cst.notion_collection_url)
	all_channels = collection.get_rows()
	print("total : {} channels".format(len(all_channels)), end=cst.star)
	for ch in all_channels:
		print("{} | {} | {}".format(ch.name, ch.url[0:2] == "UC", ch.url))
		######## scrape all unfinished channels now ;)dzadza

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
