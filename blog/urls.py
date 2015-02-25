from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/5/
    url(r'^(?P<post_id>\d+)/$', views.post, name='post')
)

