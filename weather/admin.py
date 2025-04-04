from django.contrib import admin
from .models import Location, WeatherData, UserProfile

# Простая регистрация
admin.site.register(Location)
admin.site.register(WeatherData)
admin.site.register(UserProfile)


from .tasks import update_yandex_weather

@admin.action(description="Запустить обновление погоды")
def run_update_weather(modeladmin, request, queryset):
    update_yandex_weather.delay()

class WeatherDataAdmin(admin.ModelAdmin):
    actions = [run_update_weather]