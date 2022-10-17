from django.db import models
from datetime import datetime


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=200)
    time = models.IntegerField()
    person = models.CharField(max_length=200)

    def __str__(self):
        return self.description
