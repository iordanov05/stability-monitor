import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stability_monitor.settings")
app = Celery("stability_monitor")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
