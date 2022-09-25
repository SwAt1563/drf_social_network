import datetime
from celery.schedules import crontab
from .models import Story
from api.celery import app
from datetime import datetime, timedelta



@app.task
def delete_expired_stories():
    last24HourDateTime = datetime.now() - timedelta(hours=24)
    stories = Story.objects.filter(created_date__lte=last24HourDateTime)
    if stories:
        stories.delete()


app.conf.beat_schedule = {
    'delete_expired_stories': {
        'task': 'tasks.delete_expired_stories',
        'schedule': crontab(),  # each minute check
        'args': (16, 16),
    },
}