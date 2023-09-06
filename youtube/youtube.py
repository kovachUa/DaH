import json
import os
import subprocess
import time

json_file_path = '/json/youtube.json'
download_path = '/youtube/' 
wait_time = 0
sleep_time = 0

def download_channel_videos(channel_url):
    os.makedirs(download_path, exist_ok=True)
    subprocess.run(['yt-dlp', channel_url, '-f', 'best', '--embed-thumbnail', '--add-metadata', '--write-info-json', '-o', f'{download_path}/%(title)s.%(ext)s'])
    print("2")
 
while True:
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            
            if 'youtube_urls' in data and isinstance(data['youtube_urls'], list) and len(data['youtube_urls']) > 0:
                for channel_url in data['youtube_urls']:
                    download_channel_videos(channel_url)
                    
        time.sleep(sleep_time)
    else:
        time.sleep(wait_time)
