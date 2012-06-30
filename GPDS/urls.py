from GPDS import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GPDS.views.home', name='home'),
    # url(r'^GPDS/', include('GPDS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^$', 'GPDS.views.home', name='home'),
    url(r'^version/$', 'GPDS.views.version', name='version'),
    url(r'^authors/$', 'GPDS.views.authors', name='authors'),
    url(r'^license/$', 'GPDS.views.license', name='license'),
    url(r'^tutorial/$', 'GPDS.views.tutorial', name='tutorial'),
    url(r'^support/$', 'GPDS.views.support', name='support'),
    url(r'^help/$', 'GPDS.views.help', name='help'),
    url(r'^users/',     include('users.urls')),
    url(r'^methodology/', include('methodology.urls')),
    url(r'^project/',   include('project.urls')),
    url(r'^activity/',  include('activity.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
