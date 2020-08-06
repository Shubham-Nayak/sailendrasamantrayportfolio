from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField



class OtherPages(models.Model):
    id=models.AutoField(primary_key=True) 
    title=models.CharField(max_length=25500,default="")
    featureimages=models.ImageField(default="")
    description=models.CharField(max_length=25000,default="")    

    def __str__(self):
        class Meta:
            ordering=['-time']

    def __str__(self):
        return self.title

class CommonMsters(models.Model):
    id=models.AutoField(primary_key=True) 
    title=models.CharField(max_length=25400,default="")
    imageurl=models.CharField(max_length=25400,default="")

    def __str__(self):
        class Meta:
            ordering=['-time']

    def __str__(self):
        return self.title

class Images(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=25400,default="")
    imageurl=models.ImageField(default="")

    def __str__(self):
        class Meta:
            ordering=['-time']

    def __str__(self):
        return self.title

class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=25400,default="")
    description=models.CharField(max_length=25000,default="")   
    createdon=models.CharField(max_length=25400,default="") 

    def __str__(self):
        class Meta:
            ordering=['-time']

    def __str__(self):
        return self.title

