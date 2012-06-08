from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GPDS.views.home', name='home'),
    # url(r'^GPDS/', include('GPDS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'project.views.indexProject'),
    url(r'^(?P<project_id>\d+)/$', 'project.views.detailProject'),
    url(r'^createProject/$', 'project.views.createProject'),
    url(r'^createProj/$', 'project.views.createProj'),
    url(r'^edit/(?P<project_id>\d+)/$', 'project.views.editProj'),
    url(r'^delete/(?P<project_id>\d+)/$', 'project.views.deleteProj'),
    url(r'^(?P<project_id>\d+)/create_artifact$', 'activity.views.create_artifact'),

)