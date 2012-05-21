from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
        
class Role(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    