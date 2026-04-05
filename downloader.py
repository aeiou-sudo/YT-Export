import yt_dlp

def download_youtube_video(url):
    ydl_opts = {
        # 'bestvideo+bestaudio' ensures we get the highest quality of both.
        # 'best' is the fallback if separate streams aren't available.
        'format': 'bestvideo+bestaudio/best',
        
        # Merge into MKV to support the most advanced codecs without re-encoding.
        # Use 'mp4' if you need high compatibility with older players.
        'merge_output_format': 'mkv',
        
        # Output template: Title.Extension
        'outtmpl': '%(title)s.%(ext)s',
        
        # Ensure we use the best encoders/codecs by sorting preference
        'format_sort': [
            'res:2160', # Prefer 4K if available
            'codec:vp9', # High-efficiency video codec
            'codec:opus', # Superior audio codec
        ],
        
        # Post-processor to ensure the file is correctly muxed
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
        # Try pretending to be a different client to bypass the bot check
        'extractor_args': {
            'youtube': {
                'player_client': ['ios', 'android'],
            }
        },
        
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract info to show user what is being downloaded
            info = ydl.extract_info(url, download=True)
            print(f"\nSuccessfully downloaded: {info.get('title')}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube URL: ")
    download_youtube_video(video_url)
