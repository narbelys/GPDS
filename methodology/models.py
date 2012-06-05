from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from users.models import Role

# Create your models here.

class Methodology(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    is_private = models.BooleanField(default=True)
    software_process = models.ForeignKey('SoftwareProcess')
    owner = models.ForeignKey(User, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class SoftwareProcess(models.Model):
    TYPE_CHOICES = (
          ('AG', 'Agile'),
          ('CF', 'Code_and_Fix'),
          ('WA', 'Waterfall'),
          ('SM', 'Spiral_Model'),
          ('II', 'Iterative_Incremental')
    )
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    kind = models.CharField(max_length=2, choices=TYPE_CHOICES, default='CA')
    roles = models.ManyToManyField(Role)
    
    def __unicode__(self):
        return self.name
    
admin.site.register(Methodology)
admin.site.register(SoftwareProcess)