from methodology.models import Methodology, SoftwareProcess
from methodology.form import MethodologyChangeForm, MethodologyDeleteForm, MethodologyCreateForm
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required

@login_required
def manage_methodology(request):
    latest_meth_list = Methodology.objects.all()
    return render_to_response('methodology/manage_methodology.html',
                                    {'latest_meth_list': latest_meth_list,}, 
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
                               'action': 'create',
                               'button': 'Guardar'},
                              context_instance=RequestContext(request))


@login_required
def update(request, methodology_id):    
    
    if request.method == 'POST':
        form = MethodologyChangeForm(request.POST, instance=Methodology.objects.get(pk=methodology_id))
        redirect_to = request.REQUEST.get('next', reverse('methodology.views.manage_methodology', args=()))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('methodology.views.manage_methodology', args=()))
    else:
        form = MethodologyChangeForm(instance=Methodology.objects.get(pk=methodology_id))
        redirect_to = request.REQUEST.get('next', '')
    return render_to_response('methodology/update.html',
                              {'form':form,
                               'next':redirect_to,
                               'methodology_id':methodology_id},
                              context_instance=RequestContext(request))
    
@login_required 
def delete(request, methodology_id):
    if request.method == 'POST':    
        form = MethodologyDeleteForm(request.POST, instance=Methodology.objects.get(pk=methodology_id))
        redirect_to = request.REQUEST.get('next', reverse('methodology.views.manage_methodology', args=()))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('methodology.views.manage_methodology', args=()))
    else:
        form = MethodologyDeleteForm(instance=Methodology.objects.get(pk=methodology_id))
        redirect_to = request.REQUEST.get('next', '')
    return render_to_response('methodology/delete.html',
                              {'form':form,
                               'next':redirect_to,
                               'methodology_id':methodology_id},
                              context_instance=RequestContext(request))
    
#Consultar rol

@login_required 
def consultarRol(request, methodology_id):
    return render_to_response('methodology/consultarRol.html')

#Listar roles del participante

@login_required 
def ListarRol(request, methodology_id):
    return render_to_response('methodology/ListarRol.html')
    
    
        
# Software Process Index
@login_required
def indexswp(request):
    latest_swp_list = SoftwareProcess.objects.all()
    return render_to_response('methodology/indexswp.html', 
                                     {'latest_swp_list':latest_swp_list, }, 
                                     context_instance=RequestContext(request))

# Software Process Details
@login_required
def detailswp(request, software_process_id):
    try:
        p = SoftwareProcess.objects.get(pk=software_process_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('methodology/detailswp.html', {'software_process': p},        
                                       context_instance=RequestContext(request))
