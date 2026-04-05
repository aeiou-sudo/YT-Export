import yt_dlp
import sys

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',
        'cookiefile': 'cookies.txt',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        
        # NEW: The "Music/Signature" bypass configuration
        'extractor_args': {
            'youtube': {
                # 'tv' and 'android' are often less restricted for signatures than 'web'
                'player_client': ['android', 'web'],
                # This is the "Secret Sauce": some signatures only unlock with this
                'skip': ['dash', 'hls'],
            }
        },
        
        # Force Node.js as the solver
        'javascript_path': '/usr/local/bin/node',
        
        # Add a real-world User-Agent to match your cookies
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # We use 'download=True' to fetch the actual media
            info = ydl.extract_info(url, download=True)
            if info:
                print(f"\nSuccessfully processed: {info.get('title')}")
            else:
                print("\nFailed to extract video information.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Reading from stdin allows the GitHub Action to 'pipe' the URL in
    video_url = sys.stdin.read().strip()
    if not video_url:
        print("Error: No URL provided.")
    else:
        download_youtube_video(video_url)