# Docker Проект для Зберігання та Завантаження Веб-сайтів, Репозиторіїв та YouTube Каналів

Цей репозиторій містить Docker проект, розроблений для зручного зберігання та завантаження веб-сайтів за допомогою інструменту `httrack`, а також посилань на репозиторії організацій на GitHub та YouTube канали. Використання Docker дозволяє легко ідентифікувати та ізолювати всі необхідні залежності, що робить робочий процес більш передбачуваним і спрощує розгортання.

## Структура Репозиторію

Репозиторій містить наступні файли та каталоги:

- `./data/mirror/site`: Каталог для зберігання зеркал веб-сайтів.
- `./data/json/`: JSON файли, які містять посилання на веб-сайти у форматі JSON.


## Формат Посилань

Для додавання посилань використовуйте такий формат:

- Для веб-сайтів: `https://site.si`
- Для репозиторіїв на GitHub: `https://github.com/repo`
- Для YouTube каналів: `https://www.youtube.com/@channel/

## Інструкції З Використання

1. Встановіть Docker на своєму комп'ютері, якщо він ще не встановлений.
2. Клонуйте цей репозиторій на свій комп'ютер.
3. В терміналі перейдіть до каталогу репозиторію.
4. Запустіть Docker контейнер, використовуючи команду `docker-compose up`.
5. Після запуску веб-сервер буде доступний за адресою http://127.0.0.1:9000.

6. # Docker Project for Storing and Downloading Websites, Repositories and YouTube Channels

This repository contains a Docker project designed to easily store and download websites using the `httrack' tool, as well as links to organizations' GitHub repositories and YouTube channels. Using Docker makes it easy to identify and isolate all required dependencies, making the workflow more predictable and simplifying deployment.

## Structure of the Repository

The repository contains the following files and directories:

- `./data/mirror/site`: Directory for storing website mirrors.
- `./data/json/`: JSON files that contain links to websites in JSON format.


## Link format

To add links, use the following format:

- For websites: `https://site.si`
- For GitHub repositories: `https://github.com/repo`
- For YouTube channels: `https://www.youtube.com/@channel/

## Instructions For Use

1. Install Docker on your computer if it is not already installed.
2. Clone this repository to your computer.
3. In the terminal, navigate to the repository directory.
4. Start the Docker container using the `docker-compose up' command.
5. Once started, the web server will be available at http://127.0.0.1:9000.
