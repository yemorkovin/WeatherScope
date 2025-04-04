Запуск celery:
celery -A WeatherScope worker -l info --pool=solo 
celery -A WeatherScope beat -l info  
Запуск сервера:
python manage.py runserver
