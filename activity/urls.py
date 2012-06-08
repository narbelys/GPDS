from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'activity.views.indexact'),
    # Technique Index
    url(r'^indextec/$', 'activity.views.indextec'),
    # Technique Details
    url(r'^indextec/(?P<technique_id>\d+)/$', 'activity.views.detailtec'),
    # Technique Create
    url(r'^indextec/add$', 'activity.views.addtec'),
    # Technique Update
    url(r'^indextec/update/(?P<technique_id>\d+)/$', 'activity.views.updatetec'),
    url(r'^(?P<activity_id>\d+)/artifacts/(?P<artifact_id>\d+)$', 'activity.views.open_artifact'), 
    url(r'^(?P<activity_id>\d+)/artifacts$', 'activity.views.artifacts'), 
)
