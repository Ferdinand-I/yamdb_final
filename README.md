# Проект API Yamdb <img src="https://static.vecteezy.com/system/resources/previews/000/496/671/original/chat-icon-design-vector.jpg" width=48>

![Workflow badge](https://github.com/Ferdinand-I/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Проект **API Yamdb** предоставляет API методы для работы с ресурсом. Это совместный проект, реализованный с помощью **Git**

Основные технологии, использованные в проекте:
* **Python 3.7**
* **Django 2.2.16**
* **Django REST Framework 3.12.4**

Основные фичи технической реализации:
* Подключение БД PostgreSQL
* Написание скрипты **manage**-команды для заполнения БД из файлов *csv*
* Кастомная модель для регистрации новых пользователей, наследованная от встроенной **Django**-модели AbstractUser. Плюс к расширяемости и изменяемости проекта
* Валидация данных на уровне **Django ORM**
* Описание моделей на базе кастомных абстрактных моделей
* Подключение бэкенда для отправки *e-mail*
* Кастомная аутентификация пользователей с помощью **JWT**-токена с отправкой кода подтверждения на *e-mail*
* Настройка *extra actions* для вью функций
* Описание кастомных пермишенов на базе **BasePermissions** из модуля *rest_framework.permissions*
* Описание кастомных фильтров на базе **FilterSet** из модуля *django_filters.rest_framework*
* Валидация полей сериализаторов
* Агрегация данных полей сериализаторов
* Развёртывание инфраструктуры проекта с помощью контейнеров **Docker**
* Автоматизация процессов тестирования, сборки и пуша на **DockerHub**, деплоя и оповещения в *Telegram* с помощью технологий **Git Workflow**

Как запустить:

*Приложение запускается в контейнерах Docker, поэтому вам пондобится установленный [docker](https://www.docker.com/)*

1. Клонируйте репозиторий себе на компьютер, находясь в директории, откуда вы хотите в будущем запускать проект (в примере испоьзуется ссылка для подключения с помощью протокола **SSH** в консоли **BASH** для **WINDOWS**)

```BASH
git clone git@github.com:Ferdinand-I/yamdb_final.git
```

2. Перейдите в директорию *infra*

```BASH
cd infra
```

3. Создайте *.env* файл и откройте его любым текстовым редактором, например, консольным nano

```BASH
touch .env
nano .env
```

4. Отредактируйте его по шаблону

```nano
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<ваш пароль>
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<django secret key>
```

> **Django SECRET-KEY** можно сгенерировать с помощью встроенной утилиты:

> ```python
> from django.core.management.utils import get_random_secret_key  
> get_random_secret_key()
> ```

5. Запустите сценарий **docker compose**:

```BASH
docker-compose up
```

6. Выполните миграции внутри контейнера с приложением **Python**

```BASH
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

7. Создайте суперпользователя для доступа в админку

```BASH
docker-compose exec web python manage.py createsuperuser
```

8. Соберите статику

```BASH
docker-compose exec web python manage.py collectstatic
```

9. Загрузите фикстуры БД из csv-файлов с помощью кастомной manage команды

```BASH
docker-compose exec web python manage.py loadfixtures
```

Проект доступен к изучению по адресу http://127.0.0.1/

Ссылки на репозитории авторов проекта:
* <a href="https://github.com/Ferdinand-I">Антон Борисов</a>
* <a href="https://github.com/xHYSTERIAx">Анастасия Жалненкова</a>
* <a href="https://github.com/ToxicAv3ng3r">Toxic Avenger</a>
