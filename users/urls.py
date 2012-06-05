from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout, password_reset
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^sign_up/$', 'users.views.sign_up'),                   
    url(r'^login/$',  login, {'template_name':'login.html'}),
    url(r'^logout/$', logout, {'next_page':'/'}),
    url(r'^password_reset/$', password_reset, {'template_name': 'password_reset.html',
                                               'email_template_name': 'password_reset_email.html',
                                               'subject_template_name': 'password_reset_subject.txt',
                                               'post_reset_redirect': '/'}),
                          
                                            
)