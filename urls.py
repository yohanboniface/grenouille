from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('django.views.static',
    (r'^%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'serve',
     {'document_root': settings.MEDIA_ROOT}),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('chimere.urls', namespace="chimere")),
)
