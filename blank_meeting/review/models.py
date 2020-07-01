from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    # ForeignKey : 다른 모델을 상속해옴
    # -> 게시글 작성자를 알기 위해 User 모델 상속함
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=1000, null=True, blank=True)
    password = models.TextField(max_length=1000, null=False, blank=False)
    score = models.IntegerField(min_value=0, max_value=5)    
