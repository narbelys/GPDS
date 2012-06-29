from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout, password_reset, password_change
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^sign_up/$', 'users.views.sign_up'),
    url(r'^login/$', login, {'template_name':'users/login.html'}),
    url(r'^logout/$', logout, {'next_page':'/'}),
    url(r'^password_change/$', password_change, {'template_name': 'users/password_change.html',
                                                 'post_change_redirect': '/'}),
    url(r'^password_reset/$', password_reset, {'template_name': 'users/password_reset.html',
                                               'email_template_name': 'users/password_reset_email.html',
                                               'subject_template_name': 'users/password_reset_subject.txt',
                                               'post_reset_redirect': '/'}),
    url(r'^read_user/(?P<user_id>\d+)/$', 'users.views.read_user'),
    url(r'^update_user/$', 'users.views.update_user'),
    url(r'^find_anywhere/$', 'users.views.find_anywhere'),
)
