from django.contrib.auth.models import User
from django.db import models
from methology.models import Methology

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
    cost  = models.DecimalField()
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='CO')
    methology = models.ForeignKey(Methology)
    leader = models.ForeignKey(User)
    participants = models.ManyToManyField(User)
    