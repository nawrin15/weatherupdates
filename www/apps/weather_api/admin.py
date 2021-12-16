from django.contrib import admin
from apps.weather_api.models import CityInfo
from django.contrib.auth.models import Group

@admin.register(CityInfo)
class CityInfoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'country',
        'lon',
        'lat'
    ]

    def has_add_permission(self, request):
      return False
    
    def has_delete_permission(self, request, obj=None):
      return False

admin.site.unregister(Group)
