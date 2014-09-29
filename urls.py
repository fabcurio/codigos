from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fadgames.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document.root':settings.MEDIA_ROOT}),
    url(r'^',include('apps.noticias.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
