from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Descomentar al crear el index de actividades
    #url(r'^$', activity.views.index'),
    # Technique Index
    url(r'^indextec/$', 'activity.views.indextec'),
    # Technique Details
    url(r'^indextec/(?P<technique_id>\d+)/$', 'activity.views.detailtec'),
    url(r'^(?P<activity_id>\d+)/artifacts/(?P<artifact_id>\d+)$', 'activity.views.open_artifact'), 
    url(r'^(?P<activity_id>\d+)/artifacts$', 'activity.views.artifacts'),  
)
