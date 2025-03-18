# YouTube Video Downloader Terminal

A simple Python script to download YouTube videos in MP4 or MP3 format using `yt-dlp`.

## Features
- Download videos in **MP4 (720p/1080p)** or **MP3 (audio only)**
- Supports specifying video quality
- Requires `ffmpeg` for merging audio and video

## If Problem for pip? Can help you (Working) Linux

 - sudo apt install python3-venv
 - python3 -m venv ~/myenv
 - source ~/myenv/bin/activate
 
## To install dependencies from requirements.txt, run:
- pip install -r requirements.txt

## Download video as MP4 (best quality)
- python3 youtubevideo.py -d mp4 -u <video_url>

## Download MP3 (audio only)
- python3 youtubevideo.py -d mp3 -u <video_url>

## Download MP4 with specific quality (720p or 1080p)
- python3 youtubevideo.py -d mp4 -c 1080p -u <video_url>

## Installation
1. Install `yt-dlp` and `ffmpeg`:
   ```bash
   pip install yt-dlp
   sudo apt update && sudo apt install ffmpeg -y
