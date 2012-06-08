from project.models import Project 
from activity.models import Activity
from methodology.models import Methodology, SoftwareProcess
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, login_required, permission_required
from users.models import UserProfile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

@login_required
def indexProject(request):
    latest_project_list = Project.objects.all()
    latest_users_list = UserProfile.objects.all()
    t = loader.get_template('project/indexProject.html')
    c = Context({
        'latest_project_list': latest_project_list, 'latest_users_list': latest_users_list,
    })
    return HttpResponse(t.render(c))

@login_required
def detailProject(request, project_id):
    try:
        p = Project.objects.get(pk=project_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('project/detailProject.html', {'project': p})

@login_required
def createProject(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('project.views.indexProject', args=()))
    else:
        latest_methodology_list = Methodology.objects.all().order_by('-id')
        latest_users_list = UserProfile.objects.all().order_by('-user')
        return render_to_response('project/createProject.html', {'latest_methodology_list':latest_methodology_list, 'latest_users_list': latest_users_list, }, context_instance=RequestContext(request))

@login_required
def createProj(request):
        mt = Methodology.objects.get(pk=request.POST['methodology'])
       # l  = UserProfile.objects.get(pk=request.POST['leader'])
#        usr = User.objects.get(pk=request.POST['participants'])
        p = Project    (name=request.POST['name'], description=request.POST['description'], date_start=request.POST['date_start'], date_end=request.POST['date_end'], cost=request.POST['cost'], area=request.POST['area'], methodology=mt, leader=request.user,)
#participants=request.user)

        p.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('project.views.indexProject', args=()))

@login_required
def editProject(request, project_id):
        #mt = Methodology.objects.get(pk=request.POST['methodology'])
        latest_methodology_list = Methodology.objects.all().order_by('-id')
        p = Project.objects.get(pk=project_id)
        #pi = Project    (name= project_id,description=request.POST['description'],date_start=request.POST['date_start'],date_end=request.POST['date_end'],cost=request.POST['cost'],area=request.POST['area'], methodology=mt,leader=request.user,)
        #pi.save()
        return render_to_response('project/editProject.html', {'project': p, 'latest_methodology_list':latest_methodology_list})


#@csrf_protect
@login_required
def editProj(request, project_id):
        mt = Methodology.objects.get(pk=request.POST['methodology'])
       # project_id.description=request.POST['description']
        #project_id.date_start=request.POST['date_start']
        #project_id.date_end=request.POST['date_end']
        #project_id.cost=request.POST['cost']
        #project_id.area=request.POST['area']
        #project_id.methodology=mt
        #project_id.leader=request.user
        #project_id.save()
        return render_to_response('project.views.indexProject', args=())
