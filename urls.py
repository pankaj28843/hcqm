from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('main.urls')),
    (r'^accounts/', include('accounts.urls')),
    (r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
