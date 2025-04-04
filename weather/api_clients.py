import requests
from django.conf import settings

class YandexWeatherAPI:
    BASE_URL = "https://api.weather.yandex.ru/v2"
    access_key = 'e4ee901a-cccf-46ce-98d2-e5ddfd56c1a6'

    @classmethod
    def get_weather(cls, lat, lon):
        headers = {
            'X-Yandex-Weather-Key': cls.access_key
        }
        url = f"{cls.BASE_URL}/forecast?lat={lat}&lon={lon}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()


