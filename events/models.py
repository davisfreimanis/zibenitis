from django.db import models
from datetime import datetime, timedelta, time


class Event(models.Model):
    title = models.CharField(max_length=50, help_text="Pasākuma nosaukums")
    description = models.TextField(max_length=2500, help_text="Pasākuma apraksts")
    date = models.DateTimeField(help_text="Datums un pūlkstenis kad pasākums sāksies")
    duration = models.FloatField(default=5, help_text="Pasākuma ilgums stundās")
    location = models.CharField(max_length=50, help_text="Adrese ko Google maps mēģinās atrast")
    information = models.CharField(max_length=50, default="", blank=True, help_text="Links kur var atrast vairāk informāciju")

    def __str__(self):
        return self.title

    #returns the time when the events ends
    def finish_time(self):
        return self.date + timedelta(hours=self.duration)
