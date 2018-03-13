from django.urls import path
from events import views

urlpatterns = [
    path('', views.event_brief, name='events'),
    path('<int:event_id>/', views.event_detail, name='event'),
]
