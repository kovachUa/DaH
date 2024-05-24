import json
import os
import sys

def add_youtube(data, youtube_url, json_file_path):
    # Перевірка наявності файлу JSON та завантаження даних
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
    else:
        data = {"channels": []}

    # Додавання URL до списку каналів
    data["channels"].append(youtube_url)

    # Збереження оновлених даних у файл JSON
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

def main():
    if len(sys.argv) != 2:
        return

    youtube_url = sys.argv[1]
    json_file_path = "/json/youtube_channels.json"  # Назва файлу для збереження YouTube каналів у форматі JSON

    add_youtube(None, youtube_url, json_file_path)

if __name__ == "__main__":
    main()
