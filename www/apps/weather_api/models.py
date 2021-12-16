from django.db import models

# Create your models here.

class CityInfo(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64, default="BD")
    lon = models.DecimalField(max_digits = 20, decimal_places = 10)
    lat = models.DecimalField(max_digits = 20, decimal_places = 10)

    # class Meta:
    #     app_label = 'apps.weather_api'

    def __str__(self):
        return self.name
