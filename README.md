# Store_Django_Rest_Api
**Django REST API для управления складом**
**Описание**
Этот проект представляет собой API для управления складами и товарами с функционалом регистрации и аутентификации пользователей. В проекте реализованы два типа пользователей: поставщики и потребители. Поставщики могут добавлять товары на склады, а потребители — забирать товары.

**Функционал**
* Регистрация пользователей (поставщик/потребитель).
* Аутентификация.
* Создание складов.
* Добавление товаров на склады.
* Поставщики могут добавлять товары на склады.
* Потребители могут забирать товары со складов, но не больше доступного количества.

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

**Пользователи**

POST /users/ — регистрация нового пользователя.

GET /users/ - cписок всех пользователей

**Аунтификация**

http://127.0.0.1:8000/api-auth/login/?next=/

**Склады**

GET /storehouses/ — список складов.

POST /storehouses/ — создание нового склада.

**Товары**

GET /products/ — список товаров.

POST /products/ — добавление нового товара.

**Поставки**

GET /supplies/ — список поставок.

POST /supplies/ — добавление товара на склад (доступно только для поставщиков).

**Потребление**

GET /consumptions/

POST /consumptions/ — получение товара со склада (доступно только для потребителей и при достаточном количестве товаров).
    
**Примеры запросов**


**Создание нового поставщика**

POST /users/

Content-Type: application/json

{

    "username": "supplier1",
    "role": "supplier",
    "email": "1234@email.ru"
    "password": "12345"
}

**Создание нового потребителя**

POST /users/

Content-Type: application/json

{

    "username": "consumer1",
    "role": "consumer",
    "email": "consumer1234@email.ru"
    "password": "12345"
}

**Просмотр всех зарегестрированных пользователей**

GET  /users/

**После создания юзера нужно авторизоваться, чтобы были доступны все функции**

Вправом верхнем углу кнопка "Log in" или по ссылке http://127.0.0.1:8000/api-auth/login/?next=/ и вводим Username и пароль.

**Создание склада**

POST /storehouses/

Content-Type: application/json

{

    "name": "sklad",
}

**Просмотр списка складов**

GET /storehouses/

**Создание товара**

POST /products/

Content-Type: application/json

{

    "name": "potatoes",
    "quantity": 50,
    "storehouse": 1
    
}

**Просмотр списка складов**

GET /products/

**Поставка товара**

POST /supplies/

Content-Type: application/json

{

    "product": 1,
    "quantity": 100
}

**Просмотр списка поставок**

GET /supplies/


POST /consumptions/

Content-Type: application/json

{

    "product": 1,
    "quantity": 10
}

**Просмотр списка потреблений**

GET /consumptions/
