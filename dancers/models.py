from django.db import models

from django.conf import settings
from datetime import datetime

# We define a single class, which corresponds to enteries of each person.


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50)
    date_added = models.DateField(default=datetime.now())
    picture = models.ImageField(upload_to='dancers_pic', max_length=500, default='dancers_pic/default_pic.png' )

    def __str__(self):
        return self.first_name+" "+self.last_name

