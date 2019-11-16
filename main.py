from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from yt import leech
from no import collections
import itertools
from yt.objects.Channel import Channel


################ DER MAIN DEBUT #####################
test = False
def app():
	if test:
		### test for manual language change
		leech.channel(Channel("test", "url", "url", "Français"), 0)
	else:
		print("getting channels from Notion collection ... please wait")
		collection = collections.getCollectionFromViewUrl(cst.notion_collection_url)
		all_channels = collection.get_rows()
		nb_channels = len(all_channels)
		print("total channels : {}".format(nb_channels), end=cst.star)

		for row in all_channels:
			# print("{} | {}".format(ch.name, ch.url))
			ch = Channel(row.name, row.url, row.episodes_url, row.language)
			if (ch.yt_url != "" 
			and ch.yt_url != "-" 
			and not row.ignore):
				if is_already_downloaded(row):
					leech.channel(ch, row, download_videos=False)
				else:
					leech.channel(ch, row)
				row.infos_status = "Finished" ### not very clean but more logical : done in leech.channel()

def is_already_downloaded(row):
	already_downloaded = row.download_status is not None and "Finished" in row.download_status ### V1 : download_status column
	# already_downloaded =  ### V2 : all videos either downloaded (OneDrive) or ignored
	return already_downloaded



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
