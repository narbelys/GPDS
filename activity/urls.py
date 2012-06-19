from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Estos Url seran sustituidos por los News URL's
    url(r'^$', 'activity.views.indexact'),
    # Technique Index
    url(r'^indextec/$', 'activity.views.indextec'),
    # Technique Details
    url(r'^indextec/(?P<technique_id>\d+)/$', 'activity.views.detailtec'),
    # Technique Create
    url(r'^indextec/add$', 'activity.views.addtec'),
    # Technique Update
    url(r'^indextec/update/(?P<technique_id>\d+)/$', 'activity.views.updatetec'),

    # Estos URL's estan sujetos a cualquier cambio. Solo son de referencia de acuerdo al estandar definido
    
    # News URL's for Activity
    url(r'^manage_activity/$', 'activity.views.manage_activity'),
    url(r'^create_activity/$', 'activity.views.create_activity'),
    url(r'^read_activity/(?P<activity_id>\d+)/$', 'activity.views.read_activity'),
    url(r'^update_activity/$', 'activity.views.update_activity'),
    url(r'^delete_activity/$', 'activity.views.delete_activity'),
    
    # News URL's for Technique
    url(r'^manage_technique/$', 'activity.views.manage_technique'),
    url(r'^read_technique/(?P<technique_id>\d+)/$', 'activity.views.read_technique'),
    url(r'^add_technique/$', 'activity.views.read_technique'),
    
    # News URL's for Artifact
    #Manage Artifact
    url(r'^manage_artifact/$', 'activity.views.manage_artifact'),
    #Create Artifact
    url(r'^project/(?P<project_id>\d+)/create_artifact$', 'activity.views.create_artifact'),
    # Read Artifact
    url(r'^read_artifact/(?P<artifact_id>\d+)/$', 'activity.views.read_artifact'),
    # Read Artifact
    url(r'^update_artifact/(?P<artifact_id>\d+)/$', 'activity.views.update_artifact'),
    #Delete Artifact
    url(r'^delete_artifact/$', 'activity.views.delete_artifact'),      
    # Open Artifact
    url(r'^open_artifact/(?P<artifact_id>\d+)/$', 'activity.views.open_artifact'), 
    

)
