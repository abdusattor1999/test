from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, PostViewSet

router = DefaultRouter()
router.register(r"post", PostViewSet, basename="post")
router.register(r"", BlogViewSet, basename="blog")

urlpatterns = []+router.urls
