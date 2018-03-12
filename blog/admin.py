from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from blog.models import Post
from blog.models import Carousel

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Carousel)

