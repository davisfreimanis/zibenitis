from django.db import models

# We define a single class, which corresponds to enteries of each person.


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_added = models.DateField()

    def __str__(self):
        return self.first_name+" "+self.last_name

class Picture(models.Model):
    pic = models.FileField(upload_to='dancers_pic')
