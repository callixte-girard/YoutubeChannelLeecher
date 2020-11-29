from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from scrape import leech
from scrape.insert import videoInfosInCollection
from static import collections
import itertools
import os
import requests
from objects.Channel import Channel
from objects.Playlist import Playlist
from objects.Url import Url
### these are specifically for testing playlist-only
from scrape import playlists


##################################################################
# Making sure that the working directory is the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
os.environ["PATH"] += os.pathsep + script_dir

restart = False # By default. If a network error occurs somewhere, this will turn True and restart automatically
def app(mode=1):

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
			ch = Channel(row.title, str(row.uri), row.episodes_url, row.language)
			if (ch.yt_url != "" and row.uri != "—" and row.published_videos < cst.videos_number_limit and row.to_index):
				try:
					leech.channel_or_playlist(ch, row)
				except requests.exceptions.HTTPError as httpError:
					print("!!! The following error has occured :", httpError)
					print(">>> Will now restart software...")
					restart = True
				finally:
					var.driver.quit() ### empty process in RAM at each KeyboardInterrupt

		elif mode==2:
			plst = Playlist(row.title, row.url, row.episodes_url, None)
			leech.channel_or_playlist(plst, row, my_playlists=True)

	# Check if it should restart or no (yes if there has been a network / hasardous error, no if everything was successful)
	if restart: app(mode)

##################################################################
### Different values for mode :
## 1 : all channels
## 2 : my playlists
app(mode=1)

print("————— END OF PROGRAM —————")
##################################################################
