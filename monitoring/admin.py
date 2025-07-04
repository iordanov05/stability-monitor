from django.contrib import admin

from .models import Metric, Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ("name", "ip", "description")
    search_fields = ("name", "ip")


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ("server", "timestamp", "cpu", "mem", "disk", "uptime")
    list_filter = ("server", "timestamp")
    search_fields = ("server__name", "server__ip")
