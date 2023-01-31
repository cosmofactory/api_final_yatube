Проект api_final_yatube предоставляет возможность взаимодействия приложений с социальной сетью yatube. В данном проекте реализована концепция CRUD по отношению к постам, комментариям, группам, подпискам. Подробности описаны в технической документации проекта.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:cosmofactory/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Документация проекта находится по адресу (при запуске на локальном сервере):

```
http://127.0.0.1:8000/redoc/
```

Примеры некоторых запросов-ответов к API:

```
GET http://127.0.0.1:8000/api/v1/posts/
```

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```


```
POST http://127.0.0.1:8000/api/v1/posts/
```

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

```
GET http://127.0.0.1:8000/api/v1/follow/
```
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```


Автор: Никита Ассоров 
email 
```
nikssor@yandex.ru
```
```
https://github.com/cosmofactory
```
Используемые технологии: DRF, djoser+JWT, REST API, Redoc