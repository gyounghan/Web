from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null = True)
    updateDate = models.DateTimeField(auto_now = True)
    # Create your models here.
    #
    def __str__(self):
        return '%s %s' %(self.first_name,self.last_name)
