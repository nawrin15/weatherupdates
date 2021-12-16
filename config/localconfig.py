#DO NOT COMMIT THE NON-TEMPLATE CONFIG TO FILE TO VERSION CONTROL!!!!
wwwConfig = {
        #set value to prod or local for production or local respectivly
        'serverType' : 'local',
        #absolute path to staicroot folder on the machine - should be outside the
        #git repo
        'STATIC_ROOT' : '/opt/weatherupdates/www',
        'STATIC_URL' : '/static/',
        # SECURITY WARNING: keep the secret key used in production secret!
        'SECRET_KEY' : '4',
        'IS_DEBUG' : True,
        'ALLOWED_HOSTS' : ['*'],
        'LOG_LOCATION' : '/var/log/weatherupdates/',
        'BASE_URL' : 'http://0.0.0.0:8000/',
	'CELERY_BROKER_URL' : 'redis://redis:6379/',  #'redis://0.0.0.0:6379/', #'redis://redis:6379/'
        'LOGSTASH_HOST' : 'logstash', #'logstash', #'0.0.0.0'
        'LOGSTASH_PORT' : 5000,
        'WEATHER_API_KEY' : '30024f9c0a2a0ce1eb0dbf7c6c05114f',
}
dbConfig = {
        'DB_NAME' : 'weatherupdates',
        'DB_USER' : 'testuser',
        'DB_PASSWORD' : '123456',
        'DB_HOST' :  'weatherupdatesdb', ##'127.0.0.1',## 'weatherupdatesdb',
        'DB_PORT' : 5432
}
