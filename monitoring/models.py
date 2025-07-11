from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=128)
    ip = models.GenericIPAddressField()
    port = models.IntegerField(default=8080)
    description = models.TextField(blank=True)

    def get_metrics_url(self):
        return f"http://{self.ip}:{self.port}/metrics"

    def __str__(self):
        return f"{self.name} ({self.ip}:{self.port})"


class Metric(models.Model):
    """Одиночный замер состояния сервера."""

    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="metrics")
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    cpu = models.PositiveSmallIntegerField(help_text="CPU usage, %")
    mem = models.PositiveSmallIntegerField(help_text="RAM usage, %")
    disk = models.PositiveSmallIntegerField(help_text="Disk usage, %")
    uptime = models.CharField(
        max_length=64, help_text="Uptime in '1d 2h 37m 6s' format"
    )

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Metric({self.server}, {self.timestamp}, cpu={self.cpu}%)"
