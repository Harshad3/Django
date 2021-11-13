from django.db import models


# Create your models here.

class slider():
    title1 : str
    title2 : str
    desc : str
    img : str


class featuredpls(models.Model):
    img = models.ImageField(upload_to='Pictures', default='Pictures')
    title1 = models.CharField(max_length=50, default='title1')
    title2 = models.CharField(max_length=100, default='title2')
    desc = models.TextField(max_length=500, default='description')

class recentProj(models.Model):
    Small_image = models.ImageField(upload_to='Pictures', default='Pictures')
    Big_image = models.ImageField(upload_to='Pictures', default='Pictures')

class Blogs(models.Model):
    
    img = models.ImageField('Images', upload_to='Pictures', default='Pictures')
    Title = models.CharField(max_length=100, default='Title')
    desc = models.TextField('Description', max_length=500, default='Description')
    date = models.DateField('Date')


