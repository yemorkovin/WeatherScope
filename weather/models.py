from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField("Название", max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temp = models.FloatField("Температура (°C)")
    feels_like = models.FloatField("Ощущается как (°C)")
    humidity = models.FloatField("Влажность (%)")
    wind_speed = models.FloatField("Скорость ветра (м/с)")
    pressure = models.FloatField("Давление (мм рт. ст.)")
    condition = models.CharField("Состояние", max_length=100)  # "ясно", "дождь" и т.д.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_locations = models.ManyToManyField(Location)
    units = models.CharField(max_length=10, default='metric')  # metric/imperial

