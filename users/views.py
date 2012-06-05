# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext

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
