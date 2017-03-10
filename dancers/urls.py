from django.conf.urls import patterns, url
from dancers import views

urlpatterns = [
    url(r'^$', views.index, name='dancers'),
]
