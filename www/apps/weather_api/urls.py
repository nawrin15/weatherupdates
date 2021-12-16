from django.urls import path
import apps.weather_api.views as weatherApi

urlpatterns = [
    path('weather', weatherApi.weatherUpdates),
    path('cityInfo', weatherApi.cityInfo),
]
