# Docker Проект для Зберігання та Завантаження Веб-сайтів

Цей репозиторій містить Docker проект, розроблений для зручного зберігання та завантаження веб-сайтів за допомогою інструменту `httrack`. Використання Docker дозволяє легко ідентифікувати та ізолювати всі необхідні залежності, що робить робочий процес більш передбачуваним і спрощує розгортання.

## Структура Репозиторію

Репозиторій містить наступні файли та каталоги:

- `./data/mirror/site`: Каталог для зберігання зеркал веб-сайтів.
- `./data/json/site`: JSON файли, які містять посилання на веб-сайти у форматі JSON.

## Формат Посилань

Для додавання посилань використовуйте такий формат:

- Для веб-сайтів: `https://site.si`

## Інструкції З Використання

1. Встановіть Docker на своєму комп'ютері, якщо він ще не встановлений.
2. Клонуйте цей репозиторій на свій комп'ютер.
3. В терміналі перейдіть до каталогу репозиторію.
4. Запустіть Docker контейнер, використовуючи команду `docker-compose up`.
5. Після запуску веб-сервер буде доступний за адресою http://127.0.0.1:9000.

# Docker Project for Storing and Downloading Websites

This repository contains a Docker project designed for convenient storage and downloading of websites using the `httrack` tool. Utilizing Docker makes it easy to identify and isolate all necessary dependencies, making the workflow more predictable and simplifying deployment.

## Repository Structure

The repository includes the following files and directories:

- `./data/mirror/site`: A directory for storing mirrors of websites.
- `./data/json/site`: JSON files containing links to websites in JSON format.

## Link Format

To add links, use the following format:

- For websites: `https://site.si`

## Usage Instructions

1. Install Docker on your computer if it's not already installed.
2. Clone this repository to your computer.
3. In the terminal, navigate to the repository directory.
4. Launch the Docker container using the `docker-compose up` command.
5. After launching, the web server will be accessible at http://127.0.0.1:9000.
