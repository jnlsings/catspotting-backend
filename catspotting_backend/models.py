from django.db import models

# Create your models here


class Post(models.Model):
    author = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000)
    img_url = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000)
