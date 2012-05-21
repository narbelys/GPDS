from django.contrib.auth.models import User
from django.db import models
from project.models import Project
from users.models import Role
from methology.models import SoftwareProcess

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    progress = models.IntegerField()
    date_start = models.DateTimeField('date started')
    date_end = models.DateTimeField('date ended')
    project = models.ForeignKey(Project)
    users = models.ManyToManyField(User)
    activities_required = models.ManyToManyField('self',null=True, blank=True)
    roles = models.ManyToManyField(Role)
    software_process = models.ForeignKey(SoftwareProcess)

class Artifact(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    content = models.FileField()
    activity = models.ForeignKey(Activity, through='Technique')
    
class Technique(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    
    