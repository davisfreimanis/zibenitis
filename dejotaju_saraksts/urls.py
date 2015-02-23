from django.conf.urls import patterns, url
from dejotaju_saraksts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
)
