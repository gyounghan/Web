from django.db import models

# Create your models here.
class User(models.Model) :
    userid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    user_score = models.IntegerField()
    matchmaker_score = models.IntegerField()
    
