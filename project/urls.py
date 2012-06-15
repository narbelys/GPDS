from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'project.views.manage'),
    url(r'^(?P<project_id>\d+)/$', 'project.views.read'),
    url(r'^create/$', 'project.views.create'),
    url(r'^update/(?P<project_id>\d+)/$', 'project.views.update'),
    url(r'^delete/(?P<project_id>\d+)/$', 'project.views.delete'),
    url(r'^(?P<project_id>\d+)/create_artifact$', 'activity.views.create_artifact'),

)
