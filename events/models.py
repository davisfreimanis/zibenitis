from django.db import models
from datetime import datetime, timedelta, time


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500)
    date = models.DateTimeField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def upcoming_events(self):
        events = Event.objects.filter(datetime.now(), datetime.now())
        return events