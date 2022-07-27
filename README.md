# Employees

Техническое задание для python:
Реализовать веб-приложение которое предоставляет собой один API метод для получения списка определенных сотрудников. Приложение должно быть асинхронным и реализовано с использованием FastAPI и MongoDB.
Код должен выглядеть так, как отданный на ревью перед выпуском в продакшн. Если прод-реализация каких-то частей предполагает собой слишком сложный/большой кусок кода, то можно делать более простую реализацию и добавлять комментарий # TODO, в котором указать, какой вы видите окончательную реализацию данной фичи.
Список данных прикреплен в json файле.
Плюсом будет использование Docker, покрытие тестами.

## Run

- create .env file 

        HOST=0.0.0.0
        PORT=8000
        MONGO_HOST=127.0.0.1
        MONGO_PORT=27017
        MONGO_USERNAME=dev
        MONGO_PASSWORD=dev
        MONGO_DB=dev
        MONGO_URL=mongodb://${MONGO_USERNAME}:${MONGO_PASSWORD}@${MONGO_HOST}:${MONGO_PORT}

- docker
  - run app

        docker-compose up app

  - run tests

        docker-compose up app_tests
