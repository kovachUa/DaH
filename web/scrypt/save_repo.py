import os
import requests
import json
import sys

def get_repositories(api_url):
    # каталог подефолту
    dname = '/json/repos'
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
            return

        # Збираємо посилання на репозиторії в масив
        for item in data:
            repositories.append(item["html_url"])

        # Перевіряємо чи є наступна сторінка пагінації
        if data:
            fetch_repositories(page + 1)
    
    fetch_repositories()

    # Записуємо посилання на репозиторії у JSON-файл
    with open(f"{dname}/{name}.json", "w") as file:
        json.dump({"urls": repositories}, file)

if __name__ == "__main__":
    # Передайте URL GitHub API як аргумент командного рядка
        api_url = sys.argv[1]
        get_repositories(api_url)
