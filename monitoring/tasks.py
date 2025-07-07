# monitoring/tasks.py
import requests
from celery import shared_task
from django.utils import timezone

from .models import Metric, Server


@shared_task
def collect_metrics():
    for server in Server.objects.all():
        try:
            port = 8080 + server.id
            url = f"http://host.docker.internal:{port}/metrics"
            response = requests.get(url, timeout=5)
            data = response.json()
            Metric.objects.create(
                server=server,
                cpu=data["cpu"],
                mem=int(data["mem"].replace("%", "")),
                disk=int(data["disk"].replace("%", "")),
                uptime=data["uptime"],
                timestamp=timezone.now(),
            )
        except Exception as e:
            print(f"Failed to collect metrics from {server}: {e}")
