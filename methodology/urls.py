from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'methodology.views.manage_methodology'),
    url(r'^(?P<methodology_id>\d+)/$', 'methodology.views.read_methodology'),
    url(r'^create/$', 'methodology.views.create_methodology'),
    url(r'^change/(?P<methodology_id>\d+)/$', 'methodology.views.update'),
    url(r'^delete/(?P<methodology_id>\d+)/$', 'methodology.views.delete'),
    # Software Process Index
    url(r'^indexswp/$', 'methodology.views.indexswp'),
    # Software Process Details
    url(r'^indexswp/(?P<software_process_id>\d+)/$', 'methodology.views.detailswp'),
)
