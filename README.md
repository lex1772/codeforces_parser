Парсер сайта codeforces
=======================
Парсер, который выдает 10 случайных задач по критериям пользователя, автоматически проверяет и добавляет новые задачи в базу данных при помощи периодических задач.

:white_check_mark: Написан парсер задач и их свойств

:white_check_mark: Сохраняются задачи в БД и дополняются, в случае если этой задачи нет - то добавлять

:white_check_mark: Настроен парсинг страниц codeforces периодичностью 1 час

:white_check_mark: Подключен Telegram-бот с возможностью выбрать сложность + тему и поиск по задачам 

Стек технологий:

- Django Rest Framework
- Celery
- PostgreSQL
- Unittest
- coverage
- drf-yasg
- Telegram
- Redis
- requests

### Начало работы
1. Установить зависимости командой `pip install -r requirements.txt`
2. Запустить Телеграм бота командой `python tg_bot.py`
3. Запустить локальный сервер командой python `manage.py runserver`
4. Запустить Celery worker командой `celery -A config worker -l INFO`
5. Запустить Celery beat для выполнения периодических задач командой `celery -A config beat -l INFO`
