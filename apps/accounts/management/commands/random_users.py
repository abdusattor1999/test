from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Creates 1000 random users"

    def handle(self, *args, **options):
        usernames = ["user", "link", "adam", "jecki", "nelli", "salah", "belfort", "sommi", "islam"]
        password = "testpass11"
        iterr = 0
        while iterr <= 1000:
            try:
                test_username = f"{random.choice(usernames)}{random.randrange(100, 90000)}"
                user = User.objects.create(username=test_username)
                user.set_password(password)
                user.save()
                iterr += 1
                self.stdout.write(
                    self.style.SUCCESS('Successfully created user "%s"' % test_username)
                )
            except:
                pass
        