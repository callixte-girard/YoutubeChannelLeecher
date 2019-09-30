# ———— YoutubeChannelLeecher ————

## HOW DO I HELP YOU, DEAR LAZY DEVELOPER ?
1) Go to the main videos page in channel you provided.
2) Get all videos' URLs. Of course, scrolling down until the playlist's end is included.
3) Goes to these individual videos URLs one by one, waiting for video `n` to be finished downloading before going to video `n+1`.
4) Once all videos from the channel are downloaded successfully, goes to all user's playlists and finds all URLs in these playlists' videos.
5) Playlist by playlist, compare all these URLs with the videos' URLs from step 3), and note which video is in which playlist.
6) Inserts all this data into your notion.so account and... we'll see for the rest what's next. ;-)

## REMAINING TO-DO :
- add error handling when video is private or deleted
✓ make video download async and run by 3 or 4 vids
x make window auto close (impossible)
✓ find a BETTER WAY to check if download has really started —> get filename by deduction : check which file popped the most recently !
x add a way to check download has really STARTED —> if a file named video_filename + ".part" is present in the same time as video_filename (indirectly done)
✓ after downloading supposed to be finished, check if number files downloaded == len(vids_urls)