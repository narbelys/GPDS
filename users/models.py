from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    roles = models.ManyToManyField('Role', null=True, blank=True)
        
class Role(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

admin.site.register(Role)