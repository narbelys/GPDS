from django import forms
from django.forms.models import ModelForm
from project.models import Project
from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required
from users.models import Membership

class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'date_start', 'date_end', 'cost', 'area', 'methodology', 'leader', )

class ProjectChangeForm(ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'date_start', 'date_end', 'cost', 'area', 'methodology', )
        
class ProjectManageParticipants(ModelForm):
    class Meta:
        model = Project
        fields = ('participants', )
        

class ProjectDeleteForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('name','description', 'date_start', 'date_end', 'cost', 'area', 'methodology', 'leader', 'participants')

class MembershipCreateForm(ModelForm):
    class Meta:
        model = Membership
        fields = ('project','user', 'role','date_joined','enabled',)

