# API Yatube
### Описание
YATUBE - cоциальная сеть блогеров для публикации личных дневников.
Это сайт, на котором можно создать свою страницу. Если на нее зайти, то можно посмотреть все записи автора.
Пользователи могут заходить на чужие страницы, подписываться на авторов и комментировать их записи.
Записи можно отправить в сообщество и посмотреть там записи разных авторов.
### Технологии
- Python 3.7.15
- Django 2.2.19
- Django Rest Framework 3.12.4
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DmitriiParshin/api_to_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Документация для API Yatube с примерами доступна:

```
http://127.0.0.1:8000/redoc/
```

### Автор
Dmitry Parshin
