import os
import requests
import json
import sys

def get_repositories(api_url):
    # Визначаємо ім'я для папки
    name = api_url.split("/")[-2]

    # Створюємо папку для збереження репозиторіїв
    os.makedirs("reposgit", exist_ok=True)

    # Масив для збереження репозиторіїв
    repositories = []

    # Функція для збирання даних про репозиторії
    def fetch_repositories(page=1):
        response = requests.get(f"{api_url}?page={page}")

        # Перевірка статусу відповіді (200 означає успішний запит)
        if response.status_code != 200:
            print(f"Помилка отримання даних. Статус код: {response.status_code}")
            return

        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Помилка декодування JSON даних.")
            return

        # Збираємо посилання на репозиторії в масив
        for item in data:
            repositories.append(item["html_url"])

        # Перевіряємо чи є наступна сторінка пагінації
        if data:
            fetch_repositories(page + 1)

    print("Обробка:", api_url)
    fetch_repositories()

    # Записуємо посилання на репозиторії у JSON-файл
    with open(f"reposgit/{name}.json", "w") as file:
        json.dump({"urls": repositories}, file)

if __name__ == "__main__":
    # Передайте URL GitHub API як аргумент командного рядка
    if len(sys.argv) != 2:
        print("Використання: python script.py <GitHub API URL>")
    else:
        api_url = sys.argv[1]
        get_repositories(api_url)
