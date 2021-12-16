import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherupdates.settings')

app = Celery('weatherupdates')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'run-everyday-at-12-AM' : {
#         'task' : '',
#         'schedule' : crontab(hour=12, minute=0)  # UTC time everyday at 12:00 A.M.
#     }
# }
