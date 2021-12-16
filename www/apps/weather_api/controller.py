from rest_framework import response
from library.error.exceptions.invalidrequest import InvalidRequest
from datetime import datetime
from apps.weather_api.models import CityInfo
from apps.weather_api.serializer import CityInfoSerializer
import requests
from config import localconfig as weatherUpdatesConfig

def convertTimestampToDateTimeObject(timestamp: str) -> object:
    return datetime.fromtimestamp(timestamp)

def getCityInfo(cityName: str) -> object:
    """
    fetch a CityInfo object from the db by city name
    """
    if not cityName:
        raise InvalidRequest("City name is not given!")
    try:
        return CityInfo.objects.get(name=cityName)
    except CityInfo.DoesNotExist:
        raise InvalidRequest("Invalid city name is given.")

def getWeatherUpdates(requestData: dict) -> dict:
    """
    1. get longitute and latitute by city name from CityInfo model
    2. using avobe info call weather api to get the current weather info
    """
    cityName = requestData.get("cityName")
    cityInfo = getCityInfo(cityName)
    API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat" : cityInfo.lat,
        "lon" : cityInfo.lon,
        'appid': weatherUpdatesConfig.wwwConfig['WEATHER_API_KEY']
    }
    headers = { 'Content-Type': 'application/json; charset=UTF-8' }
    response = requests.get(
    		url = API_ENDPOINT,
    		params = params,
    		headers = headers
    	)
    if response.status_code != 200:
        raise InvalidRequest(response.json().get('message'))
    response = response.json()
    if response:
        return {
            "weather_des": response['weather'][0]['description'],
            "date_time": convertTimestampToDateTimeObject(response['dt']),
            "temp": response['main']['temp'],
            "city": response["name"]
        }
    else:
        raise InvalidRequest("Failed to fetch data from remote server!")


def getCityNames(requestData: dict) -> dict:
    """
    return top 3 matched city info with the chunk
    """
    if "chunk" not in requestData:
        raise InvalidRequest("chunk query parameter is not given.")
    chunk = requestData.get("chunk")
    if chunk:
        chunk = chunk.capitalize()
    cityInfo = CityInfo.objects.filter(name__startswith=chunk).order_by('name')[:3]
    serializer = CityInfoSerializer(cityInfo, many=True)
    return {
        "cityNames": [city_info.get('name') for city_info in serializer.data]
    }

      
