from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from methodology.models import Methodology

# Create your models here.

class Project(models.Model):
    AREA_CHOICES = (
          ('EL', 'Electrical'),
          ('CO', 'Computer')
    )
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    date_start = models.DateTimeField('date started')
    date_end = models.DateTimeField('date ended')
    cost  = models.DecimalField(max_digits=19, decimal_places=10)
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='CO')
    methodology = models.ForeignKey(Methodology)
    leader = models.ForeignKey(User, related_name='project_leader',null=True, blank=True)
    participants = models.ManyToManyField(User,null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
admin.site.register(Project)
    
