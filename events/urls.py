from django.conf.urls import patterns, url
from events import views

urlpatterns = patterns('',
    url(r'^$', views.event_brief, name='events'),
)

