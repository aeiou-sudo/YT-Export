import yt_dlp
import sys

def download_youtube_video(url):
    ydl_opts = {
        # 1. Quality & Format Logic
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv', # MKV is the "Pro" choice for 4K/VP9/HDR
        'outtmpl': '%(title)s.%(ext)s',
        
        # 2. Preference Sorting (Ensures 4K/VP9/Opus)
        'format_sort': [
            'res:2160',      # Prefer 4K
            'codec:vp9',     # Higher efficiency than H.264
            'codec:opus',    # Best audio quality
        ],

        # 3. Security & Bypass Logic
        'cookiefile': 'cookies.txt', 
        'noplaylist': True,          # Safety switch for 1000+ item lists
        'ignoreerrors': True,
        'n_client_allow_javascript': True,
        
        # 4. Extractor Arguments (Matching our YAML Node.js setup)
        'extractor_args': {
            'youtube': {
                'player_client': ['web'],
                # This helps bypass the 'n-challenge' signature check
                'n_challenge': ['nodejs'], 
            }
        },

        # 5. Output Management
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