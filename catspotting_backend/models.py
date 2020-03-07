from django.db import models

# Create your models here


class Post(models.Model):
    author = models.CharField(max_length=1000)
    location = models.CharField(max_length=200)
    body = models.CharField(max_length=180)
    img_url = models.TextField()

    def __str__(self):
        return self.author


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=1000)
    body = models.CharField(max_length=180)

    def __str__(self):
        return self.body
