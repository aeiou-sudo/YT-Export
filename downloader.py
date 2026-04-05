import yt_dlp
import sys

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',
        'cookiefile': 'cookies.txt',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        
        # NEW: Advanced Extractor Arguments
        'extractor_args': {
            'youtube': {
                # We prioritize 'web' because our Node.js solver handles its JS best
                'player_client': ['web'],
                # This forces the use of the specific solver we set up
                'n_challenge': ['nodejs'],
            }
        },
        
        # These flags are critical for Music Videos/Signatures
        'dynamic_mpd': True,
        'youtube_include_dash_manifest': True,
        'ignoreerrors': False, # Set to False so we see the exact error if it fails
        'quiet': False,
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