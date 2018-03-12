from django.conf.urls import patterns, include, url
from django.contrib import admin

# Imports for static file treatmenet
from django.conf import settings
from django.conf.urls.static import static
from zibenitis import views

urlpatterns = [
    url(r'^$', views.front_page, name='home'),  # think about this!
    url(r'^blog/', include('blog.urls')),
    url(r'^dancers/', include('dancers.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', views.contact_persons, name='contact'),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^photos/', include('photologue.urls', namespace='photologue')),
    url(r'^stats/', include('stats.urls', namespace='stats')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Title for /admin
admin.site.site_header = 'Zibenitis admin'