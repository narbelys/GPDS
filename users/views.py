# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext
from users.forms import BasicUserChangeForm
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have signed up successfully.")
            return HttpResponseRedirect("/")
        messages.error(request, "Please verify your data and try again.")
    else:
        form = UserCreationForm()
    return render_to_response('sign_up.html',
                                    {'form': form}, 
                                    context_instance=RequestContext(request))

@login_required
def update(request):      
    if request.method == 'POST':
        form = BasicUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            redirect_to = request.REQUEST.get('next', reverse('home'))
            return HttpResponseRedirect(redirect_to)
    else:
        form = BasicUserChangeForm(instance=request.user)
    redirect_to = request.REQUEST.get('next','')
    return render_to_response('update.html', 
                              {'form':form,
                               'next':redirect_to},
                              context_instance=RequestContext(request))