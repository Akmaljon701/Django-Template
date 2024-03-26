import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Template.settings')

app = Celery('Template')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    from user.models import ModelForCeleryTest
    ModelForCeleryTest.objects.create(number=1)
    print('Celery is working!')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls 'add_data' every 5 seconds
    sender.add_periodic_task(5.0, debug_task.s(), name='add every 5')
