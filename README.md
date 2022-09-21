# Проект API Yamdb.

![Workflow badge](https://github.com/Ferdinand-I/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Проект API yamdb предоставляет методы для работы с ресурсом.

Подробная документация доступна [здесь](http://158.160.6.0/redoc/).

### Основные технологии, использованные в проекте:

```text
Python 3.7
Django 2.2.16
Django REST Framework 3.12.4
```


### Как запустить:

Клонируем репозиторий на компьютер и переходим в директорию 
<b style="color:green">infra</b>:

```bash
git clone git@github.com:Ferdinand-I/yamdb_final.git
cd infra
```
Приложение упаковано в docker контейнеры, поэтому вам пондобится
установленный [docker](https://www.docker.com/).

Но прежде создайте .env файл:

```bash
touch .env
```

И отредактируйте его по шаблону:

```text
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<ваш пароль>
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<django secret key>

```
Секретный ключ джанго можно сгенерировать с помощью встроенной утилиты:

```python
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

После этого запускает docker compose:


```bash
docker-compose up
```

Выполняем миграции:

```bash
docker-compose exec web python manage.py makemigrations reviews
docker-compose exec web python manage.py migrate
```

Для доступа в админку создаём суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

Собираем статику:

```bash
docker-compose exec web python manage.py collectstatic
```

Загружаем фикстуры БД из csv-файлов:

```bash
docker-compose exec web python manage.py loadfixtures
```

Проект доступен к изучению по адресу http://127.0.0.1/

Автор проекта Антон Борисов, студент 34 когорты Яндекс.Практикум.