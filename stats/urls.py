from django.conf.urls import patterns, url
from stats import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.RehearsalCreate.as_view(), name='rehearsal-add'),
    url(r'^(?P<pk>[0-9]+)$', views.RehearsalUpdate.as_view(), name='rehearsal-update'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.RehearsalDelete.as_view(), name='rehearsal-delete'),
]
