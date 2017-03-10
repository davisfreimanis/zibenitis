from django.conf.urls import patterns, url
from blog import views

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.blog, name='blog'),
    # ex: /blog/5/
    url(r'^(?P<post_id>\d+)/$', views.post, name='post')
]

