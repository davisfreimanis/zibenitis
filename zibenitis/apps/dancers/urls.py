from django.urls import path
from zibenitis.apps.dancers import views

urlpatterns = [
    path('', views.index, name='dancers'),
]
