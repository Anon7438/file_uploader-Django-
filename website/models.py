from django.db import models
from django.forms import CharField
import datetime

# Create your models here.
class user(models.Model):
    email = models.CharField(max_length=30)
    username = models.CharField(max_length =15)
    password = models.CharField(max_length =20)
    datetime = datetime.datetime.now()
class myuploadfiles(models.Model):
    myfiles = models.FileField(upload_to="")
    datetime = datetime.datetime.now()
    
    
   
