from django_markdown.models import MarkdownField
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = MarkdownField()
    created = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='blog', default='dancers_pic/default_pic.png')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.title])
