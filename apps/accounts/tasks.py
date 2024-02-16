from celery import shared_task
from .models import User, Following
from django.core.mail import send_mail
from apps.blog.models import Post, Blog

@shared_task
def send_feeds():
    print("Task implemeted")
    users = User.objects.all()
    for user in users:
        subscribed_blogs = Following.objects.filter(follower=user).values_list('id', flat=True)
        posts = Post.objects.filter(blog_id__in=subscribed_blogs).order_by('-created_at')[:5]
        post_texts = ""
        for post in posts:
            post_texts += f"{post.title}\n"
        if user.email is not None:
            send_mail(
                "Daily digest",
                post_texts,
                "from@example.com",
                ["to@example.com"],
                fail_silently=False,
            )
            