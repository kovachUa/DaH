import os
import json
import sys

def add_website(data, site):
    if "urls" not in data:
        data["urls"] = []  # Додати ключ 'urls' зі значенням списку, якщо його немає
    data["urls"].append(site)

def main():
    if len(sys.argv) != 2:
        return

    website_address = sys.argv[1]

    # Задайте шлях до файлу в монтуваному каталозі
    site_file_path = "/json/site/site.json"

    try:
        # Відкриваємо файл для читання, якщо він існує
        with open(site_file_path, "r") as site_file:
            data = json.load(site_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"urls": []}

    add_website(data, website_address)

    # Записуємо зміни назад у файл в монтуваному каталозі
    with open(site_file_path, "w") as site_file:
        json.dump(data, site_file, indent=4)

if __name__ == "__main__":
    main()
