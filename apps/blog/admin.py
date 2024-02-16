from django.contrib import admin
from apps.blog.models import Blog, Post

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "created_at"]
    list_display_links = list_display
    list_filter = ['user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "blog", "title", "created_at"]
    list_display_links = list_display
    