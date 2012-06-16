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
    
    # Estos URL's estan sujetos a cualquier cambio. Solo son de referencia de acuerdo al estandar definido
    
    # News URL's for Methodology
    url(r'^manage_methodology/$', 'methodology.views.manage_methodology'),
    url(r'^create_methodology/$', 'methodology.views.create_methodology'),
    url(r'^read_methodology/(?P<methodology_id>\d+)/$', 'methodology.views.read_methodology'),
    url(r'^update_methodology/$', 'methodology.views.update_methodology'),
    url(r'^delete_methodology/$', 'methodology.views.delete_methodology'),
    
    # News URL's for Software Process
    url(r'^manage_softwareprocess/$', 'methodology.views.manage_softwareprocess'),
    url(r'^read_softwareprocess/(?P<softwareprocess_id>\d+)/$', 'methodology.views.read_softwareprocess'),
    
    # News URL's for Role
    url(r'^manage_role/$', 'methodology.views.manage_role'),
    url(r'^read_role/(?P<role_id>\d+)/$', 'methodology.views.read_role'),
)

