import os
import json
import sys

def add_youtube(data, youtube_url):
    if "youtube_urls" not in data:
        data["youtube_urls"] = []
    data["youtube_urls"].append(youtube_url)

def main():
    if len(sys.argv) != 2:
        return

    youtube_url = sys.argv[1]
    youtube_file_path = "/json/youtube/youtube.json"  # Шлях до вашого JSON-файлу для YouTube URL

    try:
        with open(youtube_file_path, "r") as youtube_file:
            data = json.load(youtube_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"youtube_urls": []}

    add_youtube(data, youtube_url)
    
    with open(youtube_file_path, "w") as youtube_file:
        json.dump(data, youtube_file, indent=4)

if __name__ == "__main__":
    main()
