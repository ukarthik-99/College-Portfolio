from django.db import models

# Create your models here.

class schoolApp(models.Model):
    name=models.CharField(max_length=100)
    classname=models.IntegerField()
    fathername=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
   

class Teacher1(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    exp=models.IntegerField()
    contact=models.CharField(max_length=100)
    

