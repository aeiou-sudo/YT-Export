import yt_dlp
import sys

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',
        'cookiefile': 'cookies.txt',
        'noplaylist': True,
        'extractor_args': {
            'youtube': {
                # Force 'tv' or 'mweb' which are less prone to n-challenges
                'player_client': ['tv', 'mweb'],
                # This bypasses the 'n-challenge' by using a different API endpoint
                'player_skip': ['web', 'android'],
            }
        },
        'n_client_allow_javascript': True,
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