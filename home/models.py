from django.db import models
from django.conf import settings


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to ='', null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
