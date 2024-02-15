from django.db import models
from django.contrib.auth.models import User
from apps.blog.models import Blog, Post


class Following(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    follower = models.ForeignKey(User, on_delete=models.CASCADE)


class WatchedPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)