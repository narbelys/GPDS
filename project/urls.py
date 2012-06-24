from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Estos Url seran sustituidos por los News URL's
    #url(r'^$', 'project.views.manage'),
    #url(r'^(?P<project_id>\d+)/$', 'project.views.read'),
    #url(r'^create/$', 'project.views.create'),
    #url(r'^update/(?P<project_id>\d+)/$', 'project.views.update'),
    #url(r'^delete/(?P<project_id>\d+)/$', 'project.views.delete'),
    url(r'^(?P<project_id>\d+)/create_artifact$', 'activity.views.create_artifact'),
    
    # Estos URL's estan sujetos a cualquier cambio. Solo son de referencia de acuerdo al estandar definido
    
    # News URL's for Project
    url(r'^$', 'project.views.manage_project'),
    url(r'^create_project/$', 'project.views.create_project'),
    url(r'^read_project/(?P<project_id>\d+)/$', 'project.views.read_project'),
    url(r'^update_project/(?P<project_id>\d+)/$', 'project.views.update_project'),
    url(r'^delete_project/$', 'project.views.delete_project'),
    url(r'^quit_project/$', 'project.views.quit_project'),
    url(r'^manage_participants/(?P<project_id>\d+)/$','project.views.manage_participants'),
)
