from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500)
    date = models.DateTimeField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def short_description(self):
        return