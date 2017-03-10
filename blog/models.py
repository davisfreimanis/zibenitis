from django_markdown.models import MarkdownField
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = MarkdownField()
    created = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='blog', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.title])

    def check_if_picture(self):
        if not self.image:
            return False
        else:
            return True


class Carousel(models.Model):
    title = models.CharField(max_length=255, default='Zibenitis')
    description = models.TextField()
    image = models.ImageField(upload_to='carousel', default='carousel/zib1.png')

    SLIDE_NUMBERS = (
        (0, 'Invisible'),
        (1, 'Slide 1'),
        (2, 'Slide 2'),
        (3, 'Slide 3'),
    )
    slide = models.IntegerField(default=1, choices=SLIDE_NUMBERS)

    def __str__(self):
        return self.title
