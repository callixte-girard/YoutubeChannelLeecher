# ———— YoutubeChannelLeecher ————

## How may I help you, lazy developer ?
1) Go to the main videos page in channel you provided.
2) Get all videos' URLs. Of course, scrolling down until the playlist's end is included.
3) Goes to these individual videos URLs one by one, waiting for video `n` to be finished downloading before going to video `n+1`.
4) Once all videos from the channel are downloaded successfully, goes to all user's playlists and finds all URLs in these playlists' videos.
5) Playlist by playlist, compare all these URLs with the videos' URLs from step 3), and note which video is in which playlist.
6) Inserts all this data into your notion.so account and... we'll see for the rest what's next. ;-)

## Dependancies
- selenium webdriver
- pytube

## Quick fices for common issues
- If `pytube` gets you a `SSL Certificate` error, and you're on macOS, launch `Install Certificates.command` in `Applications/Python3.x/`

## Remaining TO-DO :
- add functionality to save progress video by video in Notion and thus continuing after last video downloaded
- add video N° in Notion
- add error handling when video is private or deleted (pytube throws an exception : `pytube.exceptions.VideoUnavailable`)
x make sure videos urls are FIRST saved in Notion (if not already) and then downloaded one by one, urls read directly from Notion and not from `vids_urls` array (irrelevant because downloader finds row corresponding to queried video url)
✓ add bitrate and video format in debugger at each vid and, if necesary, and handling for video that don't have : `mime_type='video/mp4'` and `res='720p'`
✓ fix error that makes playlist grabber get one less that actual number
✓ make video download async and run by 3 or 4 vids
x make window auto close (impossible)
✓ find a BETTER WAY to check if download has really started —> get filename by deduction : check which file popped the most recently !
x add a way to check download has really STARTED —> if a file named video_filename + ".part" is present in the same time as video_filename (indirectly done)
✓ after downloading supposed to be finished, check if number files downloaded == len(vids_urls)