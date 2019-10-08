from django.db import models

# Create your models here.

class Slam(models.Model):
    photo = models.FileField(upload_to='photos/')
    user = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    zodic = models.CharField(max_length=20,null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    facebook = models.CharField(max_length=50,null=True,blank=True)
    instagram = models.CharField(max_length=50,null=True,blank=True)
    twitter = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    nick1 = models.CharField(max_length=50,null=True,blank=True)
    nick2 = models.CharField(max_length=50,null=True,blank=True)
    skils = models.CharField(max_length=50,null=True,blank=True)
    occupation = models.CharField(max_length=50,null=True,blank=True)
    food = models.CharField(max_length=50,null=True,blank=True)
    color = models.CharField(max_length=50,null=True,blank=True)
    music = models.CharField(max_length=50,null=True,blank=True)
    movie = models.CharField(max_length=50,null=True,blank=True)
    actor = models.CharField(max_length=50,null=True,blank=True)
    actress = models.CharField(max_length=50,null=True,blank=True)
    sport = models.CharField(max_length=50,null=True,blank=True)
    person = models.CharField(max_length=50,null=True,blank=True)
    place = models.CharField(max_length=50,null=True,blank=True)
    desc = models.CharField(max_length=500,null=True,blank=True)
  