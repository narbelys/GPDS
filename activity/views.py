from django.template import Context, loader
from activity.models import Activity, Artifact, Technique
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from forms import import *
from models import *
from django.shortcuts import render_to_response, get_object_or_404

# Colocar def index aqui

# Technique Index
def indextec(request):
    latest_tec_list = Technique.objects.all()
    t = loader.get_template('indextec.html')
    c = Context({'latest_tec_list': latest_tec_list,})
    return HttpResponse(t.render(c))

# Technique Details
def detailtec(request, technique_id):
    try:
        p = Technique.objects.get(pk = technique_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detailtec.html', {'technique': p})

def artifacts(request, activity_id):
    p = get_object_or_404(Activity, pk=activity_id)
    artifacts = Artifact.objects.filter(activity__exact=p.id)
    return render_to_response('artifacts.html', {'artifacts': artifacts})

def create_artifact(request, project_id):
    if request.method=='GET':
        p = get_object_or_404(Project, pk=project_id)
        act = Activity.objects.filter(project__exact=p.id)
        tec = Technique.objects.all()
        form = upload_artifact()    
        return render_to_response('create_artifact.html', {'act': act,'tech':tec,'form': form},context_instance = RequestContext(request))
    form =upload_artifact(request.POST, request.FILES)
    if form.is_valid():
        f = form.get_fields()
        art= Artifact(name=f['name'],description=f['description'], content=request.FILES['content'], activity= (Activity.objects.get(name__exact=f['activity'])), technique= (Technique.objects.get(name__exact=f['technique'])))
        art.save()
        return render_to_response('home.html',{}, context_instance= RequestContext(request))
    else:
        p = get_object_or_404(Project, pk=project_id)
        act = Activity.objects.filter(project__exact=p.id)
        tec = Technique.objects.all()
        form = upload_artifact()    
        return render_to_response('create_artifact.html', {'act': act,'tech':tec,'form': form, 'msj':'Todos los campos son necesarios'},context_instance = RequestContext(request))
    
def open_artifact(request,artifact_id,activity_id): 
    art= get_object_or_404(Artifact, pk=artifact_id)
    (art.content).open()
    return HttpResponse('holagatito')
