from methodology.models import Methodology, SoftwareProcess
from methodology.form import MethodologyChangeForm, MethodologyDeleteForm
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required

@login_required
def index(request):
    latest_meth_list = Methodology.objects.all()
    t = loader.get_template('methodology/index.html')
    c = Context({
        'latest_meth_list': latest_meth_list,
    })
    return HttpResponse(t.render(c))

@login_required
def detail(request, methodology_id):
    try:
        p = Methodology.objects.get(pk=methodology_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'methodology': p})

@login_required
def crear(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('methodology.views.index', args=()))
    else:
        latest_sw_list = SoftwareProcess.objects.all().order_by('-id')
        return render_to_response('methodology/create.html', {'latest_sw_list':latest_sw_list, }, context_instance=RequestContext(request))

@login_required
def crearacc(request):
        ps = SoftwareProcess.objects.get(pk=request.POST['sw'])
        if request.POST['ip'] == "1":
            p = Methodology(name=request.POST['name'], description=request.POST['descripcion'], software_process=ps, owner=request.user, is_private=True)
        else:
            p = Methodology(name=request.POST['name'], description=request.POST['descripcion'], software_process=ps, owner=request.user, is_private=False)
        p.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('methodology.views.index', args=()))

@login_required
def update(request, methodology_id):    
    
    if request.method == 'POST':
        form = MethodologyChangeForm(request.POST, instance=Methodology.objects.get(pk=methodology_id))
        redirect_to = request.REQUEST.get('next', reverse('methodology.views.index', args=()))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('methodology.views.index', args=()))
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
        redirect_to = request.REQUEST.get('next', reverse('methodology.views.index', args=()))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('methodology.views.index', args=()))
    else:
        form = MethodologyDeleteForm(instance=Methodology.objects.get(pk=methodology_id))
        redirect_to = request.REQUEST.get('next', '')
    return render_to_response('methodology/delete.html',
                              {'form':form,
                               'next':redirect_to,
                               'methodology_id':methodology_id},
                              context_instance=RequestContext(request))
    
        
# Software Process Index
@login_required
def indexswp(request):
    latest_swp_list = SoftwareProcess.objects.all()
    t = loader.get_template('methodology/indexswp.html')
    c = Context({'latest_swp_list': latest_swp_list, })
    return HttpResponse(t.render(c))

# Software Process Details
@login_required
def detailswp(request, software_process_id):
    try:
        p = SoftwareProcess.objects.get(pk=software_process_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('methodology/detailswp.html', {'software_process': p})
