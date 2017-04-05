from django.db import models
from dancers.models import Person
from datetime import date


class Rehearsal(models.Model):
    date = models.DateField(default=date.today(), help_text="Mēģinājuma datums")
    present_persons = models.ManyToManyField(Person)