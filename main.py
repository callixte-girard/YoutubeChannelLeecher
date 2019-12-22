from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from static import methods as mth
from yt import leech
from no import collections
import itertools
from yt.objects.Channel import Channel
from yt.objects.Playlist import Playlist
### these are specifically for testing playlist-only
from yt.scrape import playlists


##################################################################
def app(mode=0):
	if mode==0:
		plst_url = "/playlist?list=PLVQpIsq9oH7QIS14bfZ6DBAz1gHth9lml" ### test : dicey dungeons ost
		leech.playlist_audio_only(plst_url)

	else:
		if mode==1:
			print("getting channels from Notion — All YouTube Channels ... please wait")
			collection = collections.getCollectionFromViewUrl(cst.notion_all_channels)
		elif mode==2:
			print("getting playlists from Notion — My Playlists ... please wait")
			collection = collections.getCollectionFromViewUrl(cst.notion_my_playlists)

		rows = collection.get_rows()
		print("total nb of items in collection : {}".format(len(rows)), end=cst.star)

		for row in rows:
			if mode==1:
				ch = Channel(row.title, row.url, row.episodes_url, row.language)
				if (ch.yt_url != ""
				and ch.yt_url != "-"
				and not (row.language == "Music" or row.language == "Musique") 
				and not row.published_videos > cst.videos_number_limit
				and not row.ignore
				and not row.complete):
					leech.channel_or_playlist(ch, row, download_videos=not mth.allVidsDownloaded(row))

			elif mode==2:
				plst = Playlist(row.title, row.url, row.episodes_url, None)
				leech.channel_or_playlist(plst, row, download_videos=not mth.allVidsDownloaded(row), my_playlists=True)

	# var.driver.quit()

##################################################################
### Different values for mode :
## 0 : custom playlist — audio only [DEFAULT]
## 1 : all channels
## 2 : my playlists
app(mode=2)

print("————— END OF PROGRAM —————")
##################################################################
