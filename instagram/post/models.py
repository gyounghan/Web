from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    photo = models.ImageField(upload_to='post')

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    content = models.TextField()

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'