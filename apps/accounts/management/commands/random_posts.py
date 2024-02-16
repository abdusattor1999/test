from django.core.management.base import BaseCommand
from apps.blog.models import Post, Blog
import random

class Command(BaseCommand):
    help = "Creates 1000 random posts"

    def handle(self, *args, **options):
        titles = ["Title", "link", "Computer", "TP-Link", "Anywhere", "Intel", "Test", "PEXELL", "NOKIA"]
        iterr = 0
        while iterr <= 10000:
            try:
                test_title = f"{random.choice(titles)} - {random.randrange(100, 90000)}"
                random_blog = random.choice(Blog.objects.all())
                Post.objects.create(title=test_title, blog=random_blog) 
                iterr += 1
                self.stdout.write(
                    self.style.SUCCESS('Successfully published post "%s"' % test_title)
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR('Error: "%s"' % e.args)
                )
        