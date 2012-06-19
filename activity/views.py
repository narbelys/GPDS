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
from django.contrib.auth.decorators import login_required, login_required, permission_required

# Index de Actividad
@login_required 
def indexact(request):
    latest_act_list = Activity.objects.all()
    return render_to_response('activity/indexact.html',
                                    {'latest_act_list': latest_act_list,}, 
                                    context_instance=RequestContext(request))

# Manage Techniques
@login_required 
def manage_technique(request):
    latest_tec_list = Technique.objects.all()
    return render_to_response('activity/manage_technique.html', 
							{'latest_tec_list': latest_tec_list,}, 
							context_instance=RequestContext(request))

# Read Technique
# FALTA: Poner que solo se muestren las tecnicas de la actividad actual!
@login_required 
def read_technique(request, technique_id):
    try:
        p = Technique.objects.get(pk=technique_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('activity/read_technique.html', 
							{'technique': p},
							context_instance=RequestContext(request))


@login_required 
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

@login_required                              
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

#Consultar artefacto
@login_required 
def read_artifact(request, activity_id):
    p = get_object_or_404(Activity, pk=activity_id)
    artifacts = Artifact.objects.filter(activity__exact=p.id)
    return render_to_response('activity/read_artifact.html', {'artifacts': artifacts},
                                     context_instance=RequestContext(request))

#Crear artefacto
@login_required 
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

#Descargar artefacto
@login_required   
def open_artifact(request,artifact_id):
	art= get_object_or_404(Artifact, pk=artifact_id)    
	path = art.content.path
	wrapper = FileWrapper( file( path ) )
	response = HttpResponse(wrapper, content_type='application/pdf')
	response['Content-Length'] = os.path.getsize( path )
	return response

###################################################################################################
#                                Manage, CRUD for Activity                                        #
###################################################################################################

# @login_required
# def manage_activity

# @login_required
# def create_activity

# @login_required
# def read_activity

# @login_required
# def update_activity

# @login_required
# def delete_activity

###################################################################################################
#                                Manage, Read, Add for Technique                                  #
###################################################################################################

# @login_required
# def manage_technique

# @login_required
# def read_technique

# @login_required
# def add_technique


###################################################################################################
#                               Manage, CRUD, Open for Artifacts                                  #
###################################################################################################

# @login_required
# def manage_artifacts

# @login_required
# def create_artifacts

# @login_required
# def read_artifacts

# @login_required
# def update_artifacts

# @login_required
# def delete_artifacts

# @login_required
# def open_artifacts


