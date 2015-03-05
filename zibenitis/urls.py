from django.conf.urls import patterns, include, url
from django.contrib import admin

# Imports for static file treatmenet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('blog.urls'), name='home'),  # think about this!
    url(r'^blog/', include('blog.urls')),
    url(r'^dancers/', include('dancers.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
