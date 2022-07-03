from pickle import TRUE
#from pickle import FALSE
import datetime
from django.db import models
class users(models.Model):
     email=models.EmailField(max_length=30, blank=TRUE)
     password=models.CharField(max_length=30,blank=TRUE)