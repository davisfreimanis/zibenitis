from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('blog.urls'), name='home'),  # think about this!
    url(r'^blog/', include('blog.urls')),
    url(r'^dancers/', include('dancers.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
)
