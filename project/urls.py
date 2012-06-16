from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    # Estos Url seran sustituidos por los News URL's
    url(r'^$', 'project.views.indexProject'),
    url(r'^(?P<project_id>\d+)/$', 'project.views.detailProject'),
    url(r'^createProject/$', 'project.views.createProject'),
    url(r'^createProj/$', 'project.views.createProj'),
    url(r'^edit/(?P<project_id>\d+)/$', 'project.views.editProj'),
    url(r'^delete/(?P<project_id>\d+)/$', 'project.views.deleteProj'),
    url(r'^(?P<project_id>\d+)/create_artifact$', 'activity.views.create_artifact'),
    
    # Estos URL's estan sujetos a cualquier cambio. Solo son de referencia de acuerdo al estandar definido
    
    # News URL's for Project
    url(r'^manage_project/$', 'project.views.manage_project'),
    url(r'^manage_project/$', 'project.views.create_project'),
    url(r'^manage_project/(?P<project_id>\d+)/$', 'project.views.read_project'),
    url(r'^manage_project/$', 'project.views.update_project'),
    url(r'^manage_project/$', 'project.views.delete_project'),
    url(r'^quit_project/$', 'project.views.quit_project'),
)