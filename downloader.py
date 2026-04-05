import yt_dlp
import sys

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',
        'cookiefile': 'cookies.txt',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        
        # NEW: Force the specific solver path inside the Python dictionary
        'javascript_path': '/usr/local/bin/node',
        
        'extractor_args': {
            'youtube': {
                # 'web' is the most compatible with Node.js signature solving
                'player_client': ['web'],
                # This forces yt-dlp to use our Node install for the n-challenge
                'n_challenge': ['nodejs'],
            }
        },
        
        # Bypasses 'Only images available' by ignoring the signature error 
        # and trying to fetch the stream anyway
        'check_formats': 'cached',
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