import json
import sys
import argparse
import os

def add_youtube_channel(data, url):
    data["urls"].append(url)

def save_to_file(data):
    with open("/json/youtube/youtube.json", "w") as youtube_file:
        json.dump(data, youtube_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Додавання YouTube-каналу до списку')
    parser.add_argument('url', type=str, help='URL-адреса YouTube-каналу')

    args = parser.parse_args()

    if not os.path.exists("youtube.json"):
        initial_data = {"urls": []}
        with open("/json/youtube/youtube.json", "w") as youtube_file:
            json.dump(initial_data, youtube_file, indent=4)

    try:
        with open("/json/youtube/youtube.json", "r") as youtube_file:
            data = json.load(youtube_file)
    except FileNotFoundError:
        data = {"urls": []}

    add_youtube_channel(data, args.url)
    save_to_file(data)

if __name__ == "__main__":
    main()
