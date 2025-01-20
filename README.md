# Store_Django_Rest_Api
**Django REST API для управления складом**
**Описание**
Этот проект представляет собой API для управления складами и товарами с функционалом регистрации и аутентификации пользователей. В проекте реализованы два типа пользователей: поставщики и потребители. Поставщики могут добавлять товары на склады, а потребители — забирать товары.

**Функционал**
Регистрация пользователей (поставщик/потребитель).
Аутентификация.
Создание складов.
Добавление товаров на склады.
Поставщики могут добавлять товары на склады.
Потребители могут забирать товары со складов, но не больше доступного количества.

**Установка**
**Клонируйте репозиторий на ваш локальный компьютер:**

git clone https://github.com/username/repository.git
cd repository
**Создайте и активируйте виртуальное окружение:**

python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate  # для Windows

**Установите зависимости:**

pip install -r requirements.txt

**Выполните миграции базы данных:**

python manage.py makemigrations
python manage.py migrate

**Запустите сервер разработки:**

python manage.py runserver

**API будет доступно по адресу:**

http://127.0.0.1:8000/

API Endpoints
Пользователи
POST /users/ — регистрация нового пользователя.
GET /users/ - cписок всех пользователей
Аунтификация
http://127.0.0.1:8000/api-auth/login/?next=/
Склады
GET /storehouse/ — список складов.
POST /storehouse/ — создание нового склада.
Товары
GET /product/ — список товаров.
POST /product/ — добавление нового товара.
Поставки
GET /supply/ — список поставок.
POST /supply/ — добавление товара на склад (доступно только для поставщиков).
Потребление
GET /consumption/
POST /consumption/ — получение товара со склада (доступно только для потребителей и при достаточном количестве товаров).
Настройки JWT
В файле settings.py добавлены настройки для JWT-аутентификации. Срок действия токена доступа составляет 15 минут, токена обновления — 1 день.

Пример настроек:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
Примеры запросов
Регистрация
POST /api/register/
Content-Type: application/json

{
    "username": "supplier1",
    "password": "password123",
    "user_type": "supplier"
}
Получение токена
POST /api/token/
Content-Type: application/json

{
    "username": "supplier1",
    "password": "password123"
}
Ответ:

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
Создание склада
POST /api/warehouses/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "name": "Склад №1",
    "address": "ул. Примерная, 1"
}
Поставка товара
POST /api/supplies/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "product": 1,
    "quantity": 100
}
Потребление товара
POST /api/consumptions/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "product": 1,
    "quantity": 10
}

