from rest_framework import serializers
from apps.weather_api.models import CityInfo

class CityInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CityInfo
        fields = '__all__'