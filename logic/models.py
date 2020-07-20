from django.db import models

# Create your models here.
class vsong(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    vid=models.FileField(upload_to='vids')
    thumb=models.ImageField(upload_to='pics')
class asong(models.Model):
    name=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='pics')
    aud=models.FileField(upload_to='songs')
class ysong(models.Model):
    link=models.TextField()
    name=models.CharField(max_length=100)
    desc=models.TextField()
    artist=models.CharField(max_length=100)
    thumb=models.ImageField(upload_to='pics')
class event:
    name:str
    venue:str
    date:str
    pic:str
class service:
    name:str
    pic:str
    desc:str
    



