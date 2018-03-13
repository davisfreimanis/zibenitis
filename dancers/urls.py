from django.urls import path
from dancers import views

urlpatterns = [
    path('', views.index, name='dancers'),
]
