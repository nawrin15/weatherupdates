Go run the project >>>
```sh
./runlocal.sh
```

### Application Url: http://0.0.0.0:8000/
### Admin Panel Url: http://0.0.0.0:8000/admin/
*** username: admin, password: 123456
## Weather Apis 
***
| Description | API | Example
| ------ | ------ | ------ |
| get current weather according to city name | http://0.0.0.0:8000/api/v.0/weather?cityName={cityName}|http://0.0.0.0:8000/api/v.0/weather?cityName=Mymensingh
| get top 3 city names accoding to search key | http://0.0.0.0:8000/api/v.0/cityInfo?chunk={searchLetters} | http://0.0.0.0:8000/api/v.0/cityInfo?chunk=""  http://0.0.0.0:8000/api/v.0/cityInfo?chunk="c"

