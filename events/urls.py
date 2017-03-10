from django.conf.urls import patterns, url
from events import views

urlpatterns = [
    url(r'^$', views.event_brief, name='events'),
    url(r'^(?P<event_id>\d+)/$', views.event_detail, name='event'),
]

