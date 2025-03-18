import argparse
import yt_dlp

def download_video(url, format_type, quality=None):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    if format_type == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    elif format_type == 'mp4':
        if quality:
            ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best'
        else:
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("-d", "--download", choices=['mp3', 'mp4'], required=True, help="Download format: mp3 or mp4")
    parser.add_argument("-u", "--url", required=True, help="YouTube video URL")
    parser.add_argument("-c", "--clear", choices=['720p', '1080p'], help="Video quality (for mp4 only)")
    
    args = parser.parse_args()
    quality = args.clear[:-1] if args.clear else None
    
    download_video(args.url, args.download, quality)

# Ensure ffmpeg is installed for merging video and audio
# Install it using: sudo apt update && sudo apt install ffmpeg -y
