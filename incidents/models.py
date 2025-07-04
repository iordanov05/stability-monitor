from django.db import models

from monitoring.models import Server


class Incident(models.Model):
    """Инцидент — превышение порога метрики по серверу."""

    TYPE_CHOICES = [
        ("cpu", "CPU"),
        ("mem", "Memory"),
        ("disk", "Disk"),
    ]

    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="incidents"
    )
    incident_type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        status = "active" if self.is_active else "resolved"
        return f"{self.server} {self.incident_type} ({status}) {self.created_at:%Y-%m-%d %H:%M}"
