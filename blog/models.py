from django_markdown.models import MarkdownField
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = MarkdownField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.title])
