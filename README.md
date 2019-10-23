# KODE_backend_task

## Инструкция по запуску сервиса
#### 1.	Запуск redis-сервера

    sudo service redis-server start
    
#### 2. Запуск сервера Django   

    python manage.py runserver
    
#### 3. Запуск celery

    celery -A Service worker -B -l INFO
    
## Дополнительный запрос для вывода всей информации с БД
    GET /subscription
