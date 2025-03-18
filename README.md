# YouTube Video Downloader

A simple Python script to download YouTube videos in MP4 or MP3 format using `yt-dlp`.

## Features
- Download videos in **MP4 (720p/1080p)** or **MP3 (audio only)**
- Supports specifying video quality
- Requires `ffmpeg` for merging audio and video

## Installation
1. Install `yt-dlp` and `ffmpeg`:
   ```bash
   pip install yt-dlp
   sudo apt update && sudo apt install ffmpeg -y
