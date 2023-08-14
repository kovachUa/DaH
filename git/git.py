import os
import json
import subprocess

def download_repo(repo_url, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    subprocess.run(["git", "clone", repo_url, target_directory])

def update_repo(repo_directory):
    if os.path.exists(repo_directory):
        os.chdir(repo_directory)
        subprocess.run(["git", "pull"])
    else:
        print(f"Error: Repository directory '{repo_directory}' does not exist.")

def main():
    json_directory = "./dah/json/git"  # Замініть це на шлях до вашого каталогу з json файлами

    # Отримуємо список файлів з розширенням .json у каталозі
    json_files = [file for file in os.listdir(json_directory) if file.endswith('.json')]

    # Попросимо користувача вказати шлях для збереження репозиторіїв
    target_root_directory = "/dah/mirror/git"

    for json_file in json_files:
        with open(os.path.join(json_directory, json_file), 'r') as file:
            data = json.load(file)

            repo_urls = data["urls"]

            # Визначаємо ім'я підкаталогу для збереження репозиторіїв на основі назви json файлу
            source_name = json_file.split(".")[0]
            target_directory = os.path.join(target_root_directory, source_name)

            for repo_url in repo_urls:
                # Визначаємо ім'я каталогу з посилання
                repo_name = repo_url.split("/")[-1].replace(".git", "")
                repo_directory = os.path.join(target_directory, repo_name)

                download_repo(repo_url, repo_directory)

    # Попросимо користувача вказати дні оновлення
    days_to_update = int(input("Введіть кількість днів для оновлення репозиторіїв: "))

    for json_file in json_files:
        with open(os.path.join(json_directory, json_file), 'r') as file:
            data = json.load(file)

            repo_urls = data["urls"]

            # Визначаємо ім'я підкаталогу для оновлення репозиторіїв на основі назви json файлу
            source_name = json_file.split(".")[0]
            target_directory = os.path.join(target_root_directory, source_name)

            for repo_url in repo_urls:
                # Визначаємо ім'я каталогу з посилання
                repo_name = repo_url.split("/")[-1].replace(".git", "")
                repo_directory = os.path.join(target_directory, repo_name)

                update_repo(repo_directory)

if __name__ == "__main__":
    main()
