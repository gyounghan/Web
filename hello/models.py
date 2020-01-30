from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null = True)
    # Create your models here.
    #
    def __str__(self):
        return '%s %s' %(self.first_name,self.last_name)

class User_Info(models.Model):
    UserId = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 30)
