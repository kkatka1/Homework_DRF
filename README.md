# LMS Backend API

Этот проект представляет собой серверную часть LMS (Learning Management System), разработанную на Django с использованием Django REST Framework (DRF). Система позволяет управлять курсами, уроками и профилями пользователей, предоставляя REST API для интеграции с клиентскими приложениями.

##  Задачи проекта

- Разработка бэкенд-сервера для SPA-приложения.
- Управление пользователями, курсами и уроками.
- Реализация CRUD-операций для работы с сущностями.
- Проверка работы эндпоинтов через **Postman**.
- Для сериализатора для модели курса реализовано поле вывода уроков, с помощью сериализатора для связанной модели.Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.
- Настроена фильтрация для эндпоинта вывода списка платежей с возможностями:
    менять порядок сортировки по дате оплаты,
    фильтровать по курсу или уроку,
    фильтровать по способу оплаты.

---

##  Функциональность

### Пользователи (`users`)
- Авторизация по email.
- Дополнительные поля:
  - Телефон
  - Город
  - Аватарка

### Платежи ('payments')
- пользователь,
-  дата оплаты,
-  оплаченный курс или урок,
-  сумма оплаты,
-  способ оплаты: наличные или перевод на счет.
   
Записаны в таблицу, соответствующую этой модели данные через кастомную команду.


### Курсы (`courses`)
- Название
- Превью (изображение)
- Описание


SerializerMethodField()

### Уроки (`lessons`)
- Название
- Описание
- Превью (изображение)
- Ссылка на видео
- Привязка к курсу (один курс содержит несколько уроков)

---

##  Установка и настройка

### 1. Создание виртуального окружения
Для Linux/macOS:
```bash
python3 -m venv env
source env/bin/activate

Для Windows:

python -m venv env  
.\env\Scripts\activate  

2. Установка зависимостей

Установите необходимые пакеты:

pip install -r requirements.txt  

3. Выполнение миграций

Примените миграции базы данных:

python manage.py migrate  

4. Создание суперпользователя

Создайте суперпользователя для админ-панели:

python manage.py createsuperuser  

5. Запуск сервера

Запустите локальный сервер разработки:

python manage.py runserver  

Сервер будет доступен по адресу: http://127.0.0.1:8000

6. Основные технологии

Django: веб-фреймворк для разработки серверной части.
Django REST Framework: реализация REST API.
PostgreSQL: база данных.
Pillow: обработка изображений.
django-filter



7. Проверка эндпоинтов

Работу каждого эндпоинта необходимо проверять с помощью Postman:

Получение, создание, изменение и удаление курсов (CRUD).
Работа с уроками (CRUD).
Редактирование профилей пользователей.
