import os
from celery import Celery
from celery.schedules import crontab

# Указывает где находятся файлы Django, и файл settings
# Делается это для того чтобы один раз указать настройки Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_mail.settings')

app = Celery('send_email')

# Считывает настройки Celery из файла settings.py где будет слово CELERY

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  # Автоматическое подцепление тасков


# celery beat task
app.conf.beat_schedule = {
    'send-spam-every-1-minute': {
        'task': 'main.tasks.send_beat_email',
        'schedule': crontab(minute='*/5')
    }
}
