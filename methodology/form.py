from django import forms
from django.forms.models import ModelForm
from methodology.models import Methodology, SoftwareProcess
from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required


class MethodologyChangeForm(ModelForm):
    class Meta:
        model = Methodology
        fields = ('name', 'description', 'is_private', 'software_process', 'owner', 'enabled')
        
class MethodologyDeleteForm(ModelForm):
    class Meta:
        model = Methodology
        exclude = ('name', 'description', 'is_private', 'software_process', 'owner')