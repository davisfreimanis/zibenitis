from django.urls import path
from zibenitis.apps.stats import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.RehearsalCreate.as_view(), name='rehearsal-add'),
    path('<int:pk>/', views.RehearsalUpdate.as_view(), name='rehearsal-update'),
    path('<int:pk>/delete', views.RehearsalDelete.as_view(), name='rehearsal-delete'),

]