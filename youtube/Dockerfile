# Використовуємо базовий образ Python
FROM python:3.8
#Завантажуємо та налаштовуємо yt-dlp
RUN wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
RUN chmod a+rx /usr/local/bin/yt-dlp
RUN useradd -ms /bin/bash user
# Створюємо робочий каталог в контейнері
WORKDIR /app
COPY * /app
USER user
# Копіюємо ваш скрипт у робочий каталог контейнера

# Команда, яка виконується при запуску контейнера
CMD ["chown","user:user","/mirror"]
CMD ["python3", "youtube.py"]
