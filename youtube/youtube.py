import json
import subprocess
import time
import os

yt_dlp_conf_path = '/app/yt-dlp.conf'
check_interval = 6
wait_interval_after_download = 6
download_directory = '/mirror/youtube'

def create_channel(channel_url):
    channel_name = channel_url.split("@")[-1]
    channel_directory = os.path.join(download_directory, channel_name)
    if not os.path.exists(channel_directory):
        os.makedirs(channel_directory)
    print(f"Створено канал {channel_name} у каталозі {channel_directory}")

def download_channel_videos(channel_url):
    channel_name = channel_url.split("@")[-1]
    cmd = [
        'yt-dlp',
        '-i',
        '--config-location', yt_dlp_conf_path,
        '-o', os.path.join(download_directory, channel_name, '%(title)s.%(ext)s'),
        channel_url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Відео з каналу {channel_name} успішно завантажено.")
    except subprocess.CalledProcessError as e:
        print(f"Помилка під час завантаження відео з каналу {channel_name}:", e)

def main():
    while True:
        if os.path.exists("/json/youtube/channels.json"):
            with open("/json/youtube/channels.json", 'r') as f:
                channels_data = json.load(f)
            
            for url in channels_data.get("urls", []):
                create_channel(url)
                download_channel_videos(url)
                
            time.sleep(wait_interval_after_download)
        else:
            print("Файл channels.json не знайдено. Очікування...")
            time.sleep(check_interval)

if __name__ == "__main__":
    main()
