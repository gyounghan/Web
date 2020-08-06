from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):
    # ForeignKey : 다른 모델을 상속해옴
    # -> 게시글 작성자를 알기 위해 User 모델 상속함
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 글 작성자
    created_date = models.DateTimeField(auto_now_add=True, null=True) # 글 생성 일시
    title = models.CharField(max_length=50, null=True, blank=True) # 소개팅 제목
    content = models.TextField(max_length=1000, null=True, blank=True)
    place = models.TextField(max_length=100, null=True) # 소개팅 장소
    time = models.DateTimeField(null=True) # 소개팅 시간


class Notification(models.Model):
    sender = models.ForeignKey(User, related_name='%(class)s_noti_sender', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(User, related_name='%(class)s_noti_receiver',on_delete=models.CASCADE, null=True)
    sended_date = models.DateTimeField(auto_now_add=True, null=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=200, null=True) ## 짧은 메시지
