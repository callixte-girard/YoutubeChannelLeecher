# FUNCTIONALITIES

## How may I help you, lazy developer friend ?
1) Go to the main videos page in user/channel you provided.
2) Get all videos' URLs. 
3) Get all playlists' URLs. 
4) Scrape all playlists infos from their URLs obtained in 3) : title + the URLs of videos it contains.
5) Scrape all videos infos from their URLs obtained in 2) : title + basic infos + description + inspects in which playlist(s) the video appears.
6) At this point, all videos infos are written in Notion. Checkbox "downloaded" is off for every video.
7) Downloads all videos one by one and mark them as downloaded in Notion when completed. 

## Notes :
- I update by myself : if a new video is published, it will appear on all videos section, and thus be automatically added in Notion and downloaded.
- I can continue where I stopped, but —> !!! Maybe you will have to manually delete the last video info that might have been only partially recorded !!!
- For each playlist / all videos section, I scroll down until the playlist's end is reached so that all URLs are present.
- When Selenium browser is launched, AdGuard (or AdBlock, don't remember exactly) is automatically installed as an extension to avoid download errors with video scraping if there is an ad (in video length notably).
- Puts YouTube in proper language (the one you indicated in Notion) before scraping each channel to make sure the infos will be in proper language.

<br>

# SETUP

## Python Dependancies. Install them with : `pip install dependancy_name` ; you might replace `pip` with `pip3` if python3 is used (recommended)
- `selenium` : webdriver with Chrome driver (Firefox abandoned, because too buggy)
- `bs4` (BeautifulSoup) : HTML parser to get infos when page loaded in Selenium
- `notion` : Notion.so wrapper for Python (thanks to jamalex for its wrapper : https://github.com/jamalex/notion_py)
- `pytube` : download YouTube video from URL
- `slugify` : transform resource into a URI (unique resource identifier)
## Other dependancies. 
- You must use latest version of Chromium. 78 was buggy, I updated to version 79 and it worked great : https://chromium.woolyss.com/
- If Chromium gets some bugs sometimes, use latest official Chrome version.

## Quick fixes for common issues
- If `pytube` gets you a `SSL Certificate` error, and you're on macOS, launch `Install Certificates.command` in `Applications/Python3.x/`

<br>

# PROGRESS

## To-do
- create a `URL` object class that can be in 3 states :
    - minimal (odijzaoidza)
    - partial (/playlist?list=odijzaoidza)
    - absolute (https://www.youtube.com/playlist?list=odijzaoidza)
- add a way to recognise videos that come from already known channels / users.
- maybe differentiate `/channel/` and `/user/` cases ?
- grab publisher of each video too (when not scraping a whole channel but just a playlist)
- calculate number of vids in channels collection intelligently (just count number of links in `All Videos`)
- auto-detect failed videos and mark them as so before continuing
- maintain binding between OneDrive files and Notion entries :
    - inspect each video each time and validate or report (+ download) present or missing ones each time program is launched. 
    — download only files that are not present and mark them the same way in Notion.
    - add the link to the OneDrive video in Notion (add a URL attribute)
- auto-detect which part of the raw title contains video number, if any

## Done
- grab a playlist similarly to a channel, which means, with saving video infos and downloading them.
- programmatically check that every video in channel is either `Downloaded` or `Ignored` and thus remove column to manually ignore column `Download status`
- change logic from `Ignore` to `Complete`
- force English/French with Selenium for channels spoken in English/French (follow language indicated in Notion, if blank, raise en exception !)
- download videos directly in a folder named like user/channel name (after creating folder if needed)
- transform `Finished -n errors` into an attribute `Ignore` for video row in channel. —> added attribute in videos template
- close last window (adblock plus) —> seems to work correctly.
- install addon to ignore ads so as to fix length errors in some videos :( installed successfully, now test it —> working fine :) but not working with headless option.
- test headless option —> working but makes bugs, like in videos durations :'(
- handle the case when video has NO DESCRIPTION at all
- detect video length —> possibility to ignore videos above a certain length
- remove attribute `is_channel` in Channel objects —> if channel url starts with 'UC', it needs `/channel/` prefix. Else : `/user/`
- scrape and insert video duration properly (but Notion refuses dates alone)
- manage direct videos : 'Diffusé en direct le 30 nov. 2017'
- switch from Firefox to Chromium and NEVER USE FIREFOX AGAIN
- launch Firefox in custom size : max height but half width, on the left of the screen
- fix problem with method `attemptStreamDownload()` / error with `vid.download(cst.path_downloads)` —> put priority order for bitrates —> if it still fails, it means that no mp4 format is available —> CRY.
- try to split video raw title into title and video number 
- make tests with slugifier to make `in_playlists` correspond to `In playlists`
- inspect all playlists and record matches in existing Notion rows
- fix problem with dates somewhere (july truncated in jui like juin)
- recode the handler looper by calling itself recursively
- add error handling when video is private or deleted (pytube throws an exception : `pytube.exceptions.VideoUnavailable`)
- add functionality to save progress video by video in Notion and thus continuing after last video downloaded
- add bitrate and video format in debugger at each vid and, if necesary, and handling for video that don't have : `mime_type='video/mp4'` and `res='720p'`
- fix error that makes playlist grabber get one less that actual number
- make video download async and run by 3 or 4 vids

## Abandoned | Not useful anymore
- prevent video loading from stalling when window is not visible/active with Chrome. —> seems impossible, except with headless options, but it's a bit buggy with other functionalities
- create children from template in collection's rows —> impossible due to Notion API limitations
- mysterious errors : maybe it's because of video title containing forbidden characters : `|` or `#` or `/` etc —> no it's not.
- ignore Liked videos playlist (not really necesary.)
- find a BETTER WAY to check if download has really started —> get filename by deduction : check which file popped the most recently !
- after downloading supposed to be finished, check if number files downloaded == len(vids_urls)
- add something in Notion collection description that shows this has been generated by this program (abandoned : useless)
- add video N° in Notion (impossible for some videos that don't contain their index in title)
- make sure videos urls are FIRST saved in Notion (if not already) and then downloaded one by one, urls read directly from Notion and not from `vids_urls` array (irrelevant because downloader finds row corresponding to queried video url)
- make window auto close (impossible)
- add a way to check download has really STARTED —> if a file named video_filename + ".part" is present in the same time as video_filename (indirectly done)