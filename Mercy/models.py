from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=20)
    greeting_1 = models.CharField(max_length=20)
    greeting_2 = models.CharField(max_length=20)
    picture = models.ImageField(upload_to= 'picture/')
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField()
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About, on_delete= CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'


    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    skill_name = models.CharField(max_length=20)


class Project(models.Model):
    img = models.ImageField(upload_to='Project/')
    link = models.URLField(max_length=200)


    def __str__(self):
        return f'Project {self.id}'




