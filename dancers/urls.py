from django.conf.urls import patterns, url
from dancers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='dancers'),
)
