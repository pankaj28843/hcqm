from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
        url(r'^$', 'main.views.home', name='home'),
        url(r'^show-ratings/(?P<hctype_id>\d+)/$', 'main.views.show_ratings',
            name='show-ratings'),
        url(r'^get-helth-centers/(?P<hctype_id>\d+)/$',
            'main.views.get_health_centers', name='get-health-centers'),
        url(r'^get-ratings/(?P<hctype_id>\d+)/(?P<rc_id>\d+)/$', 'main.views.get_ratings',
            name='get-ratings'),
        )
