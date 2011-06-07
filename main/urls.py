from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
        url(r'^$', 'main.views.home', name='home'),
        url(r'^show-ratings/(?P<hctype_id>\d+)/$', 'main.views.show_ratings',
            name='show-ratings'),
        )
