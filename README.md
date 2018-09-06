# weakly-supervised-genre-classification-in-videos

This repo contains codes for weakly supervised genre classification. The codes downloads videos from playlist and uses 2 stream CNN to process audio and images.
1. playlist_downloader.py download all the videos in a playlist parallaly and saves them into download_folder folder. 
This code takes input the genre name and the playlist url
for example $ python playlist_downloader.py Fighting https://www.youtube.com/playlist?list=PLOJ49z5vFzH_vOtscrRR58zwR2s_G-Ro3

2. frame_extraction.py extract frames and audio for all the videos which we have downloaded for each genre. 
The code uses parallal processing to speed up the frame extracion process. This code assumes all the downloaded videos are present in 'download_folder' folder
We use ffmpeg to extract the image   and audio. We use multiprocessing toolkit for parallal processing

