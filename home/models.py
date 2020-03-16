from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to ='', null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)

    def get_imgae_url(self):
        return '%s%s' %(settings.MEDIA_URL, self.image)


class Comment(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


