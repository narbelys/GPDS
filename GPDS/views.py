from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from django.contrib.auth.models import User

def home(request):
    return render_to_response('home.html', {} , context_instance=RequestContext(request))

def version(request):
    return render_to_response('version.html', {} , context_instance=RequestContext(request))

def authors(request):
    return render_to_response('authors.html', {} , context_instance=RequestContext(request))

def license(request):
    return render_to_response('license.html', {} , context_instance=RequestContext(request))

def tutorial(request):
    return render_to_response('tutorial.html', {} , context_instance=RequestContext(request))

def support(request):
    return render_to_response('support.html', {} , context_instance=RequestContext(request))

def help(request):
    return render_to_response('help.html', {} , context_instance=RequestContext(request))
