import os 
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewProject.settings") # Все заводское , меняется только второй параметр , который должен указывать на сервер проекта
 
app = Celery("NewProject")
app.config_from_object("django.conf:settings", namespace= "CELERY")
app.autodiscover_tasks()

app = Celery('retail')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()