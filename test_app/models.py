from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length = 60)

class User(models.Model):
    labels = models.ManyToManyField(Label)
