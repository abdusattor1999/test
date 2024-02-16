from django.contrib import admin
from apps.accounts.models import Following, WatchedPosts


admin.site.register(Following)
admin.site.register(WatchedPosts)

