from django.db import models

# Create your models here.
class Songs(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now=True)

# class Participants(models.Model):
#     name = models.CharField(max_length=100)

class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now=True)
    host = models.CharField(max_length=100)
    participants = models.ManyToManyField('Podcast', default=None)

class AudioBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now=True)

