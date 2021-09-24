import os

## Making sure that the working directory is the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
os.environ["PATH"] += os.pathsep + script_dir

from static import constants as cst
print(">>> welcome to YoutubePlaylistLeecher.", end=cst.star)
from static import variables as var
from static import collections
from static import methods as mth
from scrape import leech
from scrape.insert import videoInfosInCollection
import itertools
import time
import requests
from static.methods import my_pp as pp
from objects.Channel import Channel
from objects.Playlist import Playlist
from objects.Url import Url
### these are specifically for testing playlist-only
from scrape import playlists


##################################################################


def app(mode=1):
	restart = False ## By default. If a network error occurs somewhere, this will turn True and restart automatically

	if mode==1:
		print("getting channels from Notion — All YouTube Channels ... please wait")
		collection = collections.getCollectionFromViewUrl(cst.notion_all_channels)
	elif mode==2:
		print("getting playlists from Notion — My Playlists ... please wait")
		collection = collections.getCollectionFromViewUrl(cst.notion_my_playlists)

	try:
		rows = collection.get_rows()
		print("total nb of items in collection : {}".format(len(rows)), end=cst.star)

		for row in rows:
			if mode==1:
				ch = Channel(row.title, str(row.uri), row.episodes_url, row.language)
				if (row.to_index and ch.yt_url != "" and row.uri != "—"):
					leech.channel_or_playlist(ch, row)

			elif mode==2:
				plst = Playlist(row.title, row.url, row.episodes_url, None)
				leech.channel_or_playlist(plst, row, my_playlists=True)
				
	# except requests.exceptions.HTTPError as httpError:
	except Exception as exc:
		print("!!! The following error has occured :", exc, end=cst.line)
		# mth.beep(cst.beeps_number_crash, 0.5) # alert user
		
		## Raise it and stop or continue and retry ?
		raise exc
		# restart = True

	finally:
		var.driver.quit() ## Always empty process in RAM whatever happens

	## Check if it should restart or no (yes if there has been a network / hasardous error, no if everything was successful)
	if restart: 
		print(">>> Will now restart software...", end=cst.star)
		app(mode)
		return
	else: # finish stuff and beep to tell user
		mth.beep(cst.beeps_number_finish, 0.2)


##################################################################
### Different values for mode :
## 1 : all channels
## 2 : my playlists
app(mode=1)

print("————— END OF PROGRAM —————")
##################################################################
