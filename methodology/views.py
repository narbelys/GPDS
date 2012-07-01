from methodology.models import Methodology, SoftwareProcess
from methodology.form import MethodologyUpdateForm, MethodologyDeleteForm, MethodologyCreateForm
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required
from users.models import Role, Membership
from project.models import Project


###################################################################################################
#                                Manage, CRUD for Methodology                                     #
###################################################################################################


@login_required
def manage_methodology(request):
    latest_meth_list = Methodology.objects.filter(enabled=True)
    return render_to_response('methodology/manage_methodology.html',
                                    {'latest_meth_list': latest_meth_list, },
                                    context_instance=RequestContext(request))

@login_required
def read_methodology(request, methodology_id):
    try:
        p = Methodology.objects.get(pk=methodology_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('methodology/read_methodology.html', {'methodology': p},
                                   context_instance=RequestContext(request))

@login_required
def create_methodology(request):
    if request.method == 'POST':
        form = MethodologyCreateForm(request.POST)
        if form.is_valid():
	    is_private = request.POST.get('is_private', False)
            p = Methodology(name=request.POST['name'], description=request.POST['description'], software_process=SoftwareProcess.objects.get(pk=request.POST['software_process']), owner=request.user, is_private=is_private)
	    p.save()
            return read_methodology(request, methodology_id=p.id)
    else:
        form = MethodologyCreateForm()
        return render_to_response('methodology/create_methodology.html',
                              {'form':form,
                               'action': 'create_methodology',
                               'button': 'Guardar'},
                              context_instance=RequestContext(request))


@login_required
def update_methodology(request, methodology_id):    
    
    if request.method == 'POST':
        form = MethodologyUpdateForm(request.POST, instance=Methodology.objects.get(pk=methodology_id))
        redirect_to = request.REQUEST.get('next', reverse('methodology.views.manage_methodology', args=()))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('methodology.views.manage_methodology', args=()))
    else:
        form = MethodologyUpdateForm(instance=Methodology.objects.get(pk=methodology_id))
        redirect_to = request.REQUEST.get('next', '')
    return render_to_response('methodology/update_methodology.html',
                              {'form':form,
                               'next':redirect_to,
                               'methodology_id':methodology_id},
                              context_instance=RequestContext(request))
    
@login_required 
def delete_methodology(request, methodology_id):
    m = Methodology.objects.get(pk=methodology_id)
    m.enabled = False
    m.save()
    form = MethodologyUpdateForm(instance=m)
    if form.is_valid():
        form.save()
        redirect_to = request.REQUEST.get('next', reverse('methodology.views.manage_methodology', args=()))
    return HttpResponseRedirect(reverse('methodology.views.manage_methodology', args=()))
    

###################################################################################################
#                                Manage, Read for Software Process                                #
###################################################################################################


# Manage Software Process
@login_required
def manage_softwareprocess(request):
    latest_swp_list = SoftwareProcess.objects.filter(enabled=True)
    return render_to_response('methodology/manage_softwareprocess.html',
							{'latest_swp_list':latest_swp_list, },
							context_instance=RequestContext(request))

# Read Software Process
@login_required
def read_softwareprocess(request, softwareprocess_id):
    try:
        p = SoftwareProcess.objects.get(pk=softwareprocess_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('methodology/read_softwareprocess.html',
							{'software_process': p},
							context_instance=RequestContext(request))


###################################################################################################
#                                        Manage, Read for Role                                    #
###################################################################################################


@login_required
def consultar_rol(request):
    if request.method == 'POST':
       	return read_methodology(request, methodology_id=p.id)
    else:
       	Lista_Roles = Role.objects.all()
        return render_to_response('methodology/consultar_rol.html',
				{
        			'Lista_Roles': Lista_Roles,
    				},
                              context_instance=RequestContext(request))

        



###################################################################################################
#                                Manage, CRUD for Methodology                                     #
###################################################################################################

# @login_required
# def manage_methodology

# @login_required
# def create_methodology

# @login_required
# def read_methodology

# @login_required
# def update_methodology

# @login_required
# def delete_methodology

###################################################################################################
#                                Manage, Read for Software Process                                #
###################################################################################################

# @login_required
# def manage_softwareprocess

# @login_required
# def read_softwareprocess

###################################################################################################
#                                        Manage, Read for Role                                    #
###################################################################################################

# @login_required
# def manage_role

# @login_required
# def read_role


