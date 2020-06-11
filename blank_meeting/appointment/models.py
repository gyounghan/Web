from django.db import models

# Create your models here.


class Appointment(models.Model):
    content = models.TextField(max_length=1000, null=True, blank=True)
