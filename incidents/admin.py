from django.contrib import admin

from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("server", "incident_type", "created_at", "is_active", "resolved_at")
    list_filter = ("incident_type", "is_active")
    search_fields = ("server__name", "server__ip")
