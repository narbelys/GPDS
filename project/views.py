from django.template import Context, loader
from project.models import Project 
from activity.models import Activity
from users.models import Membership
from methodology.models import Methodology, SoftwareProcess
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from project.form import ProjectChangeForm, ProjectDeleteForm, ProjectCreateForm
from sets import Set

@login_required
def manage(request):
    latest_project_list = Project.objects.all()
    latest_users_list = User.objects.all()
    return render_to_response('project/manage.html',
                                    {'latest_project_list': latest_project_list,}, 
                                    context_instance=RequestContext(request))   

#@login_required
#def read(request, project_id):
#    try:
#        p = Project.objects.get(pk=project_id)
#    except Poll.DoesNotExist:
#        raise Http404
#    return render_to_response('project/read.html', {'project': p},
#                                   context_instance=RequestContext(request))

@login_required
def create(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            form.save()
        latest_project_list = Project.objects.all()
        return render_to_response('project/manage.html', {'latest_project_list': latest_project_list},
                                   context_instance=RequestContext(request))
    else:
        form = ProjectCreateForm(request.POST)
        return render_to_response('project/create.html', {'form':form}, context_instance=RequestContext(request))


@login_required
def update(request, project_id):
    if request.method == 'POST':
        form = ProjectChangeForm(request.POST, instance=Project.objects.get(pk=project_id))
        redirect_to = request.REQUEST.get('next', reverse('project.views.manage', args=()))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('project.views.manage', args=()))
    else:
        form = ProjectChangeForm(instance=Project.objects.get(pk=project_id))
        redirect_to = request.REQUEST.get('next', '')
    return render_to_response('project/update.html',
                              {'form':form,
                               'next':redirect_to,
                               'project_id':project_id},
                              context_instance=RequestContext(request))

@login_required 
def delete(request, project_id):
    if request.method == 'POST':    
        form = ProjectDeleteForm(request.POST, instance=Project.objects.get(pk=project_id))
        redirect_to = request.REQUEST.get('next', reverse('project.views.manage', args=()))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('project.views.manage', args=()))
    else:
        form = ProjectDeleteForm(instance=Project.objects.get(pk=project_id))
        redirect_to = request.REQUEST.get('next', '')
    return render_to_response('project/delete.html',
                              {'form':form,
                               'next':redirect_to,
                               'project_id':project_id},
                              context_instance=RequestContext(request))

###################################################################################################
#                                 Manage, CRUD, Quit for Project                                  #
###################################################################################################

@login_required
def manage_project(request):
    projects_aux = Project.objects.filter(participants__id=request.user.id)
    projects = Set([])
    for project_aux in projects_aux:
        if (project_aux.enabled):
            projects.add(project_aux)
    return render_to_response('project/manage_project.html', {'projects':projects},
                              context_instance=RequestContext(request))

# @login_required
# def create_project

@login_required
def read_project(request,project_id):
    try:
        p = Project.objects.get(pk=project_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('project/read_project.html', {'project': p},
                                context_instance=RequestContext(request))
     

# @login_required
# def update_project

# @login_required
# def delete_project

@login_required
def quit_project(request,project_id):
    memberships = Membership.objects.filter(user_id=request.user.id,project_id=request.POST['project_id'])
    memberships.delete()
    return HttpResponseRedirect(reverse('project.views.manage_project', args=()))
