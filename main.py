from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from static import methods as mth
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

		for row_ch in all_channels:
			# print("{} | {}".format(ch.name, ch.url))
			ch = Channel(row_ch.name, row_ch.url, row_ch.episodes_url, row_ch.language)
			if (ch.yt_url != ""
			and ch.yt_url != "-" 
			and not (row_ch.language == "Music" or row_ch.language == "Musique") 
			and not row_ch.published_videos > cst.videos_number_limit
			and not row_ch.ignore
			and not row_ch.complete):
				leech.channel(ch, row_ch, download_videos=not mth.allVidsDownloaded(row_ch))
		
		# var.driver.quit()


app()

print("————— END OF PROGRAM —————")
################# DER MAIN END ######################
