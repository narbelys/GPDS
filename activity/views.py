from django.template import Context, loader
from activity.models import Activity, Artifact, Technique
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from forms import *
from models import *
from django.shortcuts import render_to_response, get_object_or_404

# Index de Actividad
def indexact(request):
    latest_act_list = Activity.objects.all()
    t = loader.get_template('activity/indexact.html')
    c = Context({'latest_act_list': latest_act_list, })
    return HttpResponse(t.render(c))

# Technique Index
def indextec(request):
    latest_tec_list = Technique.objects.all()
    t = loader.get_template('activity/indextec.html')
    c = Context({'latest_tec_list': latest_tec_list, })
    return HttpResponse(t.render(c))

# Technique Details
def detailtec(request, technique_id):
    try:
        p = Technique.objects.get(pk=technique_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('activity/detailtec.html', {'technique': p})

def addtec(request):      
    if request.method == 'POST':
        form = TechniqueForm(request.POST)
        if form.is_valid():
            technique = form.save()
            return detailtec(request, technique_id=technique.id)
    else:
        form = TechniqueForm()
    return render_to_response('activity/formtec.html', 
                              {'form':form,
                               'action': 'add',
                               'button': 'Agregar'},
                              context_instance=RequestContext(request))
                              
def updatetec(request,technique_id):
    tect = Technique.objects.get(id=technique_id)
    if request.method == 'POST':
        form = TechniqueForm(request.POST,instance=tect)
        if form.is_valid():
            technique = form.save()
            return detailtec(request, technique_id=technique.id)
    else:
        form = TechniqueForm(instance=tect)
    return render_to_response('activity/formtec.html', 
                              {'form':form,
                               'action': 'update/' + technique_id + '/',
                               'button': 'Actualizar'},
                              context_instance=RequestContext(request))

def artifacts(request, activity_id):
    p = get_object_or_404(Activity, pk=activity_id)
    artifacts = Artifact.objects.filter(activity__exact=p.id)
    return render_to_response('activity/artifacts.html', {'artifacts': artifacts})

def create_artifact(request, project_id):
    if request.method == 'GET':
        p = get_object_or_404(Project, pk=project_id)
        act = Activity.objects.filter(project__exact=p.id)
        tec = Technique.objects.all()
        form = upload_artifact()    
        return render_to_response('activity/create_artifact.html', {'act': act, 'tech':tec, 'form': form}, context_instance=RequestContext(request))
    form = upload_artifact(request.POST, request.FILES)
    if form.is_valid():
        f = form.get_fields()
        art = Artifact(name=f['name'], description=f['description'], content=request.FILES['content'], activity=(Activity.objects.get(name__exact=f['activity'])), technique=(Technique.objects.get(name__exact=f['technique'])))
        art.save()
        return render_to_response('activity/home.html', {}, context_instance=RequestContext(request))
    else:
        p = get_object_or_404(Project, pk=project_id)
        act = Activity.objects.filter(project__exact=p.id)
        tec = Technique.objects.all()
        form = upload_artifact()    
        return render_to_response('activity/create_artifact.html', {'act': act, 'tech':tec, 'form': form, 'msj':'Todos los campos son necesarios'}, context_instance=RequestContext(request))
    
def open_artifact(request, artifact_id, activity_id): 
    art = get_object_or_404(Artifact, pk=artifact_id)
    (art.content).open()
    return HttpResponse('holagatito')

