## Trudovyereservy / (Трудовые резервы)

Проект сайта для Общественно полезного фонда кадрового и спортивно-культурного развития "Трудовые резервы".
Проект представляет собой онлайн-сервис и API для него.
Реализован на Django и DjangoRestFramework.

- Целевая аудитория: c 7 лет

<details>
<summary>Stack</summary>

- Python 3.11
- Django 4.2.7
- DRF 3.14.0
- Docker
- Docker-Compose

</details>

<details>
<summary>Установка и запуск проекта</summary>

* Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Trudovyereservy/backend.git
```
```
cd talent_reserves
```

* Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```

* Установить зависимости из файла ```requirements.txt```:
```
pip install -r requirements.txt
```

* Запустить базу данных в Докере:
```
docker-compose up -d --build db
```

* Выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```

* Запустить проект:
```
python manage.py runserver
```

* Документация к API доступна по ссылке:
```
http://127.0.0.1:8000/doc/
```

</details>

<details>
<summary>Команда разработки</summary>

Тимлид:

- [Кирилл Лесников](https://github.com/lekirill)

Разработчики:

- [Вероника Лаптева](https://github.com/VeronikaLapteva)
- [Виктория Латышева](https://github.com/vikkilat)
- [Всеволод Зайковский](https://github.com/4lk4st)


</details>
