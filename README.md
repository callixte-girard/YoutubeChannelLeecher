# ———— YoutubeChannelLeecher ————

## FUNCTIONALITIES

### How may I help you, lazy developer ?
1) Go to the main videos page in user/channel you provided.
2) Get all videos' URLs. 
3) Get all playlists' URLs. 
4) Scrape all playlists infos from their URLs obtained in 3) : title + the URLs of videos it contains.
5) Scrape all videos infos from their URLs obtained in 2) : title + basic infos + description + inspects in which playlist(s) the video appears.
6) At this point, all videos infos are written in Notion. Checkbox "downloaded" is off for every video.
7) Downloads all videos one by one and mark them as downloaded in Notion when completed. 

x) I update by myself : if a new video is published, it will appear on all videos section, and thus be automatically added in Notion and downloaded.
x) I can continue where I stopped, but —> !!! Maybe you will have to manually delete the last video info that might have been only partially recorded !!!
x) For each playlist / all videos section, I scroll down until the playlist's end is reached so that all URLs are present.

=> Why "Leecher" ? Because —> Scrape + Record in Notion (videos infos) + Download (videos in mp4) = Leech.

## SETUP

### Dependancies
- selenium webdriver
- pytube

### Quick fices for common issues
- If `pytube` gets you a `SSL Certificate` error, and you're on macOS, launch `Install Certificates.command` in `Applications/Python3.x/`

### TO-DO
[✓] recode the handler looper by calling itself recursively
[-] inspect all playlists and record matches in existing Notion rows
[-] force English with Selenium but only for channels spoken in English
[✓] fix problem with dates somewhere (july truncated in jui like juin)
[✓] add error handling when video is private or deleted (pytube throws an exception : `pytube.exceptions.VideoUnavailable`)
[x] add something in Notion collection description that shows this has been generated by this program (abandoned : useless)
[x] add video N° in Notion (impossible for some videos that don't contain their index in title)
[✓] add functionality to save progress video by video in Notion and thus continuing after last video downloaded
[x] make sure videos urls are FIRST saved in Notion (if not already) and then downloaded one by one, urls read directly from Notion and not from `vids_urls` array (irrelevant because downloader finds row corresponding to queried video url)
[✓] add bitrate and video format in debugger at each vid and, if necesary, and handling for video that don't have : `mime_type='video/mp4'` and `res='720p'`
[✓] fix error that makes playlist grabber get one less that actual number
[✓] make video download async and run by 3 or 4 vids
[x] make window auto close (impossible)
[✓] find a BETTER WAY to check if download has really started —> get filename by deduction : check which file popped the most recently !
[x] add a way to check download has really STARTED —> if a file named video_filename + ".part" is present in the same time as video_filename (indirectly done)
[✓] after downloading supposed to be finished, check if number files downloaded == len(vids_urls)