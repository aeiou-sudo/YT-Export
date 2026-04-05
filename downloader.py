import yt_dlp
import sys

def download_youtube_video(url):
    ydl_opts = {
        # High-quality selection
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',
        'outtmpl': '%(title)s.%(ext)s',
        
        # Authentication & Safety
        'cookiefile': 'cookies.txt',
        'noplaylist': True,
        'ignoreerrors': False,
        
        # The "Secret Sauce": Pivot to TV/Mobile clients to bypass web n-challenges
        'extractor_args': {
            'youtube': {
                'player_client': ['tv', 'mweb'],
                'player_skip': ['web', 'android'],
            }
        },
        
        # Explicit pathing for the JS solver
        'javascript_path': '/usr/local/bin/node',
        'n_client_allow_javascript': True,
        
        # Spoof a real browser to match your exported cookies
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting extraction for: {url}")
            # Extract and download
            info = ydl.extract_info(url, download=True)
            if info:
                print(f"\nSuccessfully processed: {info.get('title')}")
            else:
                print("\nFailed to extract video information.")
            
    except Exception as e:
        print(f"\nAn error occurred during the download process: {e}")
        # Exit with error code so GitHub Action reflects the failure
        sys.exit(1)

if __name__ == "__main__":
    # Standard way to read input from GitHub Action's 'run' block
    input_data = sys.stdin.read().strip()
    if not input_data:
        print("Error: No YouTube URL provided in the workflow input.")
        sys.exit(1)
        
    download_youtube_video(input_data)