# Picasso_test_project
Тестовое задание: Загрузка и обработка файлов

## Цель
Разработать Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.

## Выполненные требования
* Создать Django проект и приложение.
* Использовать Django REST Framework для создания API.
* Реализовать модель File, которая будет представлять загруженные файлы. 
### Модель должна содержать поля:
- file: поле типа FileField, используемое для загрузки файла.
- uploaded_at: поле типа DateTimeField, содержащее дату и время загрузки файла.
- processed: поле типа BooleanField, указывающее, был ли файл обработан.
* Реализовать сериализатор для модели File.
* Создать API эндпоинт upload/, который будет принимать POST-запросы для загрузки файлов. При загрузке файла необходимо создать объект модели File, сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.
* Реализовать Celery задачу для обработки файла. Задача должна быть запущена асинхронно и изменять поле processed модели File на True после обработки файла.
* Реализовать API эндпоинт files/, который будет возвращать список всех файлов с их данными, включая статус обработки.

## Выполненные дополнительные требования
* Использовать Docker для развертывания проекта.
* Реализовать механизм для обработки различных типов файлов (например, изображений, текстовых файлов и т.д.).

## Используемые технологии
* Python 3.9+ 
* Django 3+ 
* DRF 3.10+ 
* PostgreSQL 10+ 
* Redis 5.0.1 
* Celery 5.3.4

## Развертывание проекта
Для корректной работы проекта, вам необходимо выполнить следующие шаги:

1) Установить локально на свой компьютер Python версией не ниже 3.9.x!
2) Клонировать файлы проекта с GitHub репозитория.
3) Установите виртуальное окружение.
```bash
python -m venv venv 
```
4) Активировать виртуальное окружение (если есть необходимость).
```bash
venv/Scripts/activate.bat 
```
5) Установить необходимые зависимости проекта, указанные в файле `requirements.txt`
```bash
pip install -r requirements.txt
```
6) Установить Redis, глобально себе на компьютер (используйте wsl, терминал Ubuntu).
```bash
sudo apt-get install redis-server
```
7) Запустить Redis-сервер (Redis-сервер запустится на стандартном порту 6379).
```bash
sudo service redis-server start
```
8) Убедиться, что Redis-сервер работает правильно, выполните команду:
```bash
redis-cli ping
```
9) Установить БД PostreSQL (используйте wsl, терминал Ubuntu).
```bash
sudo apt-get install postgresql
```
10) Если БД PostreSQL уже была ранее установлена, то перезапустите сервер PostreSQL.
```bash
sudo service postgresql restart
```
11) Выполнить вход.
```bash
sudo -u postgres psql
```
12) Создать базу данных с помощью следующей команды:
```bash
create database picasso;
```
Если такая база данных уже используется, то возможно изменить ее название на свою.

13) Выйти.
```bash
\q
```
14) Создать файл .env
15) Добавить в файл настройки, как в .env.sample и заполнить их.
15) Применить миграции (локально, у себя в виртуальном окружении проекта).
```bash
python manage.py migrate
```

16) Запустить сервер
```bash
python manage.py runserver
```
17) Запустить Celery
```bash
celery -A config worker -l INFO
```
18) Собрать и запустить образ docker-compose
```bash
docker-compose up --build
```
