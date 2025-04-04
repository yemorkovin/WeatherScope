from celery import shared_task

from .api_clients import YandexWeatherAPI
from .models import Location, WeatherData


@shared_task
def update_yandex_weather():
    print("Задача выполняется!")
    locations = Location.objects.all()
    for loc in locations:
        data = YandexWeatherAPI.get_weather(loc.latitude, loc.longitude)
        WeatherData.objects.create(
            location=loc,
            temp=data['fact']['temp'],
            feels_like=data['fact']['feels_like'],
            humidity=data['fact']['humidity'],
            wind_speed=data['fact']['wind_speed'],
            pressure=data['fact']['pressure_mm'],
            condition=data['fact']['condition'],
        )