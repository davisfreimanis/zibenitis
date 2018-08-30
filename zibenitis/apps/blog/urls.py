from django.urls import path
from zibenitis.apps.blog import views

urlpatterns = [
    # ex: /blog/
    path('', views.blog, name='blog'),
    # ex: /blog/5/
    path('<int:post_id>/', views.post, name='post')
]

