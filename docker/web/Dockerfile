# Використовуємо базовий образ Python 3.8 Slim
FROM python:3.8-slim

# Встановлюємо робочий каталог /app
WORKDIR /web

# Копіюємо усі файли проекту до контейнера
COPY . .

# Встановлюємо залежності з файлу requirements.txt
RUN pip install -r requirements.txt

# Відкриваємо порт 5001 для зовнішніх з'єднань
EXPOSE 5001

# Запускаємо додаток Flask при запуску контейнера
CMD ["python3", "web.py"]

