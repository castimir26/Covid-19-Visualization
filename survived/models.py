from django.db import models
import pandas as pd
# Create your models here.

class Survived(models.Model):
    province = models.CharField(default='none',max_length=200)
    country = models.CharField(default='none',max_length=200)
    last_update = models.DateTimeField()
    confirmed = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    active = models.IntegerField(default=0)
    filler = models.IntegerField(default=0)

class World(models.Model):

    updated = models.DateTimeField(auto_now_add=True)
    confirmed = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    active = models.IntegerField(default=0)
