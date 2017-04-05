from django.conf.urls import patterns, url
from stats import views

urlpatterns = [
    url(r'^$', views.index, name='stats'),
    url(r'^new/', views.RehearsalCreate.as_view(), name='rehearsal-add'),
    # url(r'^update/',),
    # url(r'^delete/',),
]
