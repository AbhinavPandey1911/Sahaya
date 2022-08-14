from inspect import modulesbyfile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Supporter(models.Model):
    name = models. CharField(max_length=122)
    email = models. CharField(max_length=122)
    phone = models. CharField(max_length=12)
    type = models. CharField(max_length=12)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class my_users(models.Model):
    name = models. CharField(max_length=122)
    email = models. CharField(max_length=122)
    phone = models. CharField(max_length=12)
    type = models. CharField(max_length=12)
    password = models.CharField(max_length=50)
    desc=models.TextField()
    gforms=models.TextField()
    wlink=models.CharField(max_length=300)
    donation_required=models.CharField(max_length=10)
    def __str__(self):
        return self.name