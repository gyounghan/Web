from django.db import models

# Create your models here.
class Account(models.Model) :
    userid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    user_score = models.IntegerField(null=True)
    matchmaker_score = models.IntegerField(null=True)
    email_address = models.CharField(max_length=100)