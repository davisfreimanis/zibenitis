from django.db import models

from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone


# A class, specifically for our short history section
class History(models.Model):
    title = models.CharField(max_length=255)
    content = MarkdownField()
    modified = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog', default='dancers_pic/default_pic.png')

    def __str__(self):
        return self.title


# We define a single class, which corresponds to enteries of each person.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    date_added = models.DateField(default=timezone.now)
    picture = models.ImageField(upload_to='dancers_pic', max_length=500, default='dancers_pic/default_pic.png')
    active = models.BooleanField(default=True)

    email_n = models.CharField(max_length=50, default='tdk.zibenitis')
    email_d = models.CharField(max_length=50, default='gmail.com')

    # Just some temporary email generation :)
    def email(self):
        mail = self.first_name[:2] + self.last_name[:3] + "@zibenitis.se"
        return mail.lower()

    def __str__(self):
        return self.first_name+" "+self.last_name


# We define a class, which stores contant/administrative persons for the contact section
class Contact_person(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.role+" "+self.person.first_name