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
	nb_channels = len(all_channels)
	print("total : {} channels".format(nb_channels), end=cst.star)

	for ch in all_channels:
		print("{} | {}".format(ch.name, ch.url))
		######## scrape all unfinished channels now ;)
		# print(row.children.get_rows()) ### test : collection not seeable
		if ch.url != "":
			if ch.download_status is not None and "Finished" not in ch.download_status :
				leech.channel(ch.url, ch.episodes_url, download_videos=False)
			else:
				leech.channel(ch.url, ch.episodes_url)
				# row.download_status = "Finished"
			ch.infos_status = "Finished"
			print(end=cst.line)

app()
# for i in itertools.count():
# 	try:
# 		app()
# 	except:
# 		if i > cst.max_retries: break
# 		else: app()

# var.driver.quit()
print("————— END OF PROGRAM —————")

################# DER MAIN END ######################
