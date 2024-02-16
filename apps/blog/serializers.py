from apps.blog.models import Blog, Post
from rest_framework.serializers import ModelSerializer

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

        