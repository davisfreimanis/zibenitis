from django.urls import path, include

from django.contrib import admin

# Imports for static file treatmenet
from django.conf import settings
from django.conf.urls.static import static
from zibenitis import views

urlpatterns = [
    path('', views.front_page, name='home'),
    path('blog/', include('zibenitis.apps.blog.urls')),
    path('dancers/', include('dancers.urls')),
    path('events/', include('zibenitis.apps.events.urls')),
    path('admin/', admin.site.urls),
    path('contact/', views.contact_persons, name='contact'),
    path('markdownx/', include('markdownx.urls')),
    path('photos', include('photologue.urls', namespace='photologue')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Title for /admin
admin.site.site_header = 'Zibenitis admin'
