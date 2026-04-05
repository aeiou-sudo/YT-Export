import yt_dlp
import sys

def download_youtube_video(url):
    # Data extracted from your v1/player JSON
    VISITOR_DATA = 'CgtBMlRtazhLUDlGQSic2cjOBjIKCgJJThIEGgAgMA%3D%3D'
    PO_TOKEN = 'k5_fmPxhoXZROVAXXi-sdDLYgPJUuTCA3FSYYtb4ShsILhf4llMgI49oqzRMkuMYNLBwOcCw59TLtslLKPQGSS'

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',
        'outtmpl': '%(title)s.%(ext)s',
        'cookiefile': 'cookies.txt',
        'noplaylist': True,
        
        'extractor_args': {
            'youtube': {
                'player_client': ['web'],
                'visitor_data': VISITOR_DATA,
                'po_token': PO_TOKEN,
            }
        },
        
        # User-Agent matching the 'WEB' client version 2.20260403
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        
        'allow_unplayable_formats': True,
        'dynamic_mpd': True,
        'javascript_path': '/usr/local/bin/node',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Extraction started for: {url}")
            info = ydl.extract_info(url, download=True)
            if info:
                print(f"\nSuccess: {info.get('title')}")
            
    except Exception as e:
        print(f"\nDownload error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if not input_data:
        sys.exit(1)
    download_youtube_video(input_data)