from django.db import models
from django.utils import timezone

class Story(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2048,blank=True,default='')
    create_date = models.DateTimeField(default=timezone.now())
    completion_date = models.DateTimeField(blank=True)
