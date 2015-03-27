from django.db import models
from datetime import datetime, timedelta, time


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500)
    date = models.DateTimeField()
    duration = models.FloatField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    #returns the time when the events ends
    def finish_time(self):
        return self.date + timedelta(hours=self.duration)
