from django.contrib.auth.models import User
from django.db import models
from users.models import Role

# Create your models here.

class Methology(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    software_process = models.ForeignKey('SoftwareProcess')
    owner = models.ForeignKey(User)
    

class SoftwareProcess(models.Model):
    TYPE_CHOICES = (
          ('AG', 'Agile'),
          ('CF', 'CodeAndFix'),
          ('WA', 'Waterfall'),
          ('SM', 'SpiralModel'),
          ('II', 'IterativeIncremental')
    )
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    kind = models.CharField(max_length=2, choices=TYPE_CHOICES, default='CA')
    roles = models.ManyToManyField(Role)