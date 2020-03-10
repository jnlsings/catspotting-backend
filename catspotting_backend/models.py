from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Post(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    body = models.CharField(max_length=180)
    img_url = models.TextField()

    def __str__(self):
        return self.body


class Comment(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=180)

    def __str__(self):
        return self.body
