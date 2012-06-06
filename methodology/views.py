from django.template import Context, loader
from methodology.models import Methodology, SoftwareProcess
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required

def index(request):
    latest_meth_list = Methodology.objects.all()
    t = loader.get_template('index.html')
    c = Context({
        'latest_meth_list': latest_meth_list,
    })
    return HttpResponse(t.render(c))

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
        return render_to_response('create.html', {'latest_sw_list':latest_sw_list,}, context_instance=RequestContext(request))

@login_required
def crearacc(request):
        ps = SoftwareProcess.objects.get(pk=request.POST['sw'])
        if request.POST['ip']=="1":
            p = methodology(name=request.POST['name'],description=request.POST['descripcion'],software_process=ps, owner=request.user, is_private=True)
        else:
            p = methodology(name=request.POST['name'],description=request.POST['descripcion'],software_process=ps, owner=request.user, is_private=False)
        p.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('methodology.views.index', args=()))

# Software Process Index
@login_required
def indexswp(request):
    latest_swp_list = SoftwareProcess.objects.all()
    t = loader.get_template('indexswp.html')
    c = Context({'latest_swp_list': latest_swp_list,})
    return HttpResponse(t.render(c))

# Software Process Details
@login_required
def detailswp(request, software_process_id):
    try:
        p = SoftwareProcess.objects.get(pk = software_process_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detailswp.html', {'software_process': p})
