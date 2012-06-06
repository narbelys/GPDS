from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'methodology.views.index'),
    url(r'^(?P<methodology_id>\d+)/$', 'methodology.views.detail'),
    url(r'^create/$', 'methodology.views.crear'),
    url(r'^createacc/$', 'methodology.views.crearacc'),
    # Software Process Index
    url(r'^indexswp/$', 'methodology.views.indexswp'),
    # Software Process Details
    url(r'^indexswp/(?P<software_process_id>\d+)/$', 'methodology.views.detailswp'),
)