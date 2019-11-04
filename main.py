from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from yt import leech
from no import collections
import itertools
from yt.objects.Channel import Channel


################ DER MAIN DEBUT #####################
def app():
	collection = collections.getCollectionFromViewUrl(cst.notion_collection_url)
	all_channels = collection.get_rows()
	nb_channels = len(all_channels)
	print("total channels : {}".format(nb_channels), end=cst.star)
	
	for row in all_channels:
		# print("{} | {}".format(ch.name, ch.url))
		ch = Channel(row.name, row.url, row.episodes_url, row.language == "English")
		######## scrape all unfinished channels now ;)
		if (ch.yt_url != "" 
		and ch.yt_url != "-" 
		and not row.ignore):
			if row.download_status is not None and "Finished" in row.download_status :
				leech.channel(ch, row, download_videos=False)
			else:
				leech.channel(ch, row)
				row.download_status = "Finished"
			# row.infos_status = "Finished" ### not very clean but more logical : done in leech.channel()

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
