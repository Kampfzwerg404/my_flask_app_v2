# Используем базовый образ Ubuntu 20.04
FROM ubuntu:20.04

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y python3 python3-pip

# Копируем приложение в контейнер
COPY . /app
WORKDIR /app

# Устанавливаем зависимости
RUN pip3 install Flask Flask-RESTful

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python3", "app.py"]
