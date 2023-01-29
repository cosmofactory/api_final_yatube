Проект api_final_yatube предоставляет возможность взаимодействия приложений с социальной сетью yatube. В данном проекте реализована концепция CRUD по отношению к постам, комментариям, группам, подпискам. Подробности описаны в технической документации проекта.

### Как запустит проект:

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
