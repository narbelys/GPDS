from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from methodology.models import SoftwareProcess
from project.models import Project
from users.models import Role
# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    progress = models.IntegerField(null=True, blank=True)
    date_start = models.DateTimeField('date started')
    date_end = models.DateTimeField('date ended')
    project = models.ForeignKey(Project)
    users = models.ManyToManyField(User,null=True, blank=True)
    activities_required = models.ManyToManyField('self',null=True, blank=True)
    activities_super = models.ManyToManyField('self',null=True, blank=True)
    activities_successor = models.ManyToManyField('self',null=True, blank=True)
    roles = models.ManyToManyField(Role)
    software_process = models.ForeignKey(SoftwareProcess)
    techniques = models.ManyToManyField('Technique')
    
    def __unicode__(self):
        return self.name

class Artifact(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    content = models.FileField(upload_to='artifacts')
    activity = models.ForeignKey('Activity')
    technique = models.ForeignKey('Technique')
    
    def __unicode__(self):
        return self.name
    
class Technique(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
    
admin.site.register(Activity)
admin.site.register(Artifact)
admin.site.register(Technique)

    