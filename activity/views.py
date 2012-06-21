from django.template import Context, loader
from activity.models import Activity, Artifact, Technique
from users.models import User, Role
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


###################################################################################################
#                                Manage, CRUD for Activity                                        #
###################################################################################################


# Manage Activities
# FALTA que se muestren solo las actividades del proyecto actual!
@login_required 
def manage_activity(request):
    latest_act_list = Activity.objects.filter(enabled = True)
    return render_to_response('activity/manage_activity.html',
							{'latest_act_list': latest_act_list,},
							context_instance=RequestContext(request))


# Create Activity
@login_required
def create_activity(request):
    if request.method == 'POST':
        form = ActivityCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return manage_activity(request)
    else:
        form = ActivityCreateForm()
        return render_to_response('activity/create_activity.html',
                              {'form':form,
                               'action': 'create_activity',
                               'button': 'Guardar'},
                              context_instance=RequestContext(request))


# Read Activity
# FALTA interpretar fecha y hora
@login_required
def read_activity(request, activity_id):
	try:
		act = Activity.objects.get(pk = activity_id, enabled = True)
		# Listar roles de actividad
		roles = Role.objects.filter(activity = activity_id, enabled = True)
		# Listar participantes de actividad
		users = act.users.all()#.filter(enabled = True)
		# Consultar actividades precedentes
		required = act.activities_required.all().filter(enabled = True)
		# Consultar actividades sucesoras
		successor = Activity.objects.filter(activities_required = activity_id, enabled = True)
		# Consultar subactividades
		subs = Activity.objects.filter(activities_super = activity_id, enabled = True)
		# Manage Techniques
		techniques = Technique.objects.filter(activity = activity_id, enabled = True)
	except Pool.DoesNotExist:
		raise Http404
	return render_to_response('activity/read_activity.html',
							{'activity': act,
							'roles':roles,
							'users': users,
							'required': required,
							'successor': successor,
							'subacts': subs,
							'techniques': techniques},
							context_instance = RequestContext(request))


# Update Activity
@login_required
def update_activity(request, activity_id):    
    
    if request.method == 'POST':
        form = ActivityUpdateForm(request.POST, instance=Activity.objects.get(pk=activity_id))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('activity.views.manage_activity', args=()))
        
    else:
        form = ActivityUpdateForm(instance=Activity.objects.get(pk=activity_id))
        redirect_to = request.REQUEST.get('next', '')
    return render_to_response('activity/update_activity.html',
                              {'form':form,
                               'next':redirect_to,
                               'activity_id':activity_id},
                              context_instance=RequestContext(request))


# @login_required
# def delete_activity


###################################################################################################
#                                Manage, Read, Add for Technique                                  #
###################################################################################################


# Manage Techniques
# NO SE USA: se ve directamente del Read Activity
@login_required 
def manage_technique(request, activity_id):
	try:
		act = Activity.objects.get(pk=activity_id)
	except Poll.DoesNotExist:
		raise Http404
	return render_to_response('activity/manage_technique.html', 
							{'act': act},
							context_instance=RequestContext(request))

# Read Technique
@login_required 
def read_technique(request, technique_id):
    try:
        p = Technique.objects.get(pk=technique_id)
    except p.DoesNotExist:
        raise Http404
    return render_to_response('activity/read_technique.html',
							{'technique': p},
							context_instance=RequestContext(request))


# @login_required
# def add_technique

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
def updatetec(request, technique_id):
    tect = Technique.objects.get(id=technique_id)
    if request.method == 'POST':
        form = TechniqueForm(request.POST, instance=tect)
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


###################################################################################################
#                               Manage, CRUD, Open for Artifacts                                  #
###################################################################################################


# @login_required
# def manage_artifacts


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


#Consultar artefacto
@login_required 
def read_artifact(request, activity_id):
    p = get_object_or_404(Activity, pk=activity_id)
    artifacts = Artifact.objects.filter(activity__exact=p.id)
    return render_to_response('activity/read_artifact.html', {'artifacts': artifacts},
                                     context_instance=RequestContext(request))


#Descargar artefacto
@login_required   
def open_artifact(request, artifact_id):
	art = get_object_or_404(Artifact, pk=artifact_id)    
	path = art.content.path
	wrapper = FileWrapper(file(path))
	response = HttpResponse(wrapper, content_type='application/pdf')
	response['Content-Length'] = os.path.getsize(path)
	return response


# @login_required
# def update_artifacts

# @login_required
# def delete_artifacts

