from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post
from .models import Carousel

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Carousel)

