from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.blog.models import Blog, Post
from apps.blog.serializers import BlogSerializer, PostSerializer
from apps.accounts.models import Following, WatchedPosts
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination



class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = AllowAny,
 
    def create(self, request, *args, **kwargs):
        return Response({"success":False, "error":"You have already one blog !"}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def subscribe(self, request, *args, **kwargs):
        try:
            blog = self.queryset.get(id=kwargs["pk"])
            following = Following.objects.filter(blog=blog, follower=request.user).last()
            if following:
                success = False
                answer = "You have already subscribed to this blog !"
                status_code = status.HTTP_400_BAD_REQUEST
            else:
                Following.objects.create(blog=blog, follower=request.user)
                success = True
                answer = "Subscribtion to the blog done"
                status_code = status.HTTP_200_OK
            return Response({"success":success, "data":answer}, status=status_code)
        
        except Blog.DoesNotExist:
            return Response({"success":False, "error":"Blog not found with given ID, Please give valid ID number"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(50, e, e.args)    
            return Response({"success":False, "error":"Something went wrong, please try agan"}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def unsubscribe(self, request, *args, **kwargs):
        try:
            blog = self.queryset.get(id=kwargs["pk"])
            following = Following.objects.filter(blog=blog, follower=request.user).last()
            if following:
                following.delete()
                success = True
                answer = "Unsubscribed successfully !"
                status_code = status.HTTP_204_NO_CONTENT
            else:
                success = False
                answer = "You have no subscribtion to this blog"
                status_code = status.HTTP_400_BAD_REQUEST
            return Response({"success":success, "data":answer}, status=status_code)
        
        except Blog.DoesNotExist:
            return Response({"success":False, "error":"Blog not found with given ID, Please give valid ID number"}, status=status.HTTP_404_NOT_FOUND)    
        except Exception as e:
            return Response({"success":False, "error":"Something went wrong, please try agan"}, status=status.HTTP_400_BAD_REQUEST)



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = IsAuthenticated,


    def list(self, request, *args, **kwargs):
        subscribed_blogs = Following.objects.filter(follower=request.user).values_list('id', flat=True)
        posts = Post.objects.filter(blog_id__in=subscribed_blogs).order_by('-created_at')
        blog_id = request.data.get("blog", None)
        print(555, blog_id)
        if blog_id:
            posts = posts.filter(blog_id=blog_id)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def mark_as_watched(self, request, *args, **kwargs):
        try:
            post = self.queryset.filter(id=kwargs['pk'])
            watched = WatchedPosts(user=request.user, post=post)
            if watched.exist():
                return Response({"success":False, "error":"Post already marked as viewed"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                watched.save()
                return Response({"success":True, "message":"Post marked as viewed"})
        except Post.DoesNotExist:
            return Response({"success":False, "error":"Post does not exist with given ID"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"success":False, "error":"Something is wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)