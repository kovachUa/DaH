import os
import sys

def add_youtube(data, youtube_url, txt_file_path):
    with open(txt_file_path, "a") as txt_file:
        txt_file.write(youtube_url + "\n")

def main():
    if len(sys.argv) != 2:
        return

    youtube_url = sys.argv[1]
    txt_file_path = "youtube_channels.txt"  # Назва файлу для збереження YouTube каналів

    add_youtube(None, youtube_url, txt_file_path)
    
if __name__ == "__main__":
    main()

