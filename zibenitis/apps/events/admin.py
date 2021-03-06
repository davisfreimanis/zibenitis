from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # What fields to display in adming

admin.site.register(Event, EventAdmin)
