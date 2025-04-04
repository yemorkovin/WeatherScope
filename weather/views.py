# weather/views.py
from django.views.generic import TemplateView
from .models import Location, WeatherData


class YandexWeatherView(TemplateView):
    template_name = "weather/yandex_weather.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем все локации и последние данные по каждой
        locations = Location.objects.all()
        weather_data = []

        for location in locations:
            try:
                latest_weather = WeatherData.objects.filter(
                    location=location
                ).latest('timestamp')
                weather_data.append({
                    'location': location,
                    'weather': latest_weather
                })
            except WeatherData.DoesNotExist:
                continue

        context['weather_data'] = weather_data
        return context