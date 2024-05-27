FROM python:3.10-alpine3.20

WORKDIR /
 
# Копируем файлы проекта в контейнер.
COPY . .
# Выполняем установку зависимостей внутри контейнера.
RUN apk upgrade --update --no-cache
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

# Выполнить запуск сервера при старте контейнера. 
CMD ["python3", "realtime_graph/manage.py", "runserver", "0:8000"] 