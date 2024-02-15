from django.db import models
from django.core.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desctiption = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}:{self.name}"

@receiver(post_save, sender=User)
def create_blog_for_user(sender, **kwargs):
    if not sender.blog:
        Blog.objects.create(user=sender, name=sender.username)


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title