from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog 
from .serializers import BlogSerializer
class PostBlogView(viewsets.ModelViewSet):
    """
    Viewset for managing Blog posts.

    This viewset provides CRUD operations for the Blog model.

    Attributes:
        queryset (QuerySet): The set of Blog objects.
        serializer_class (Serializer): The serializer class for Blog.

    Example Usage:
    ```
    post_blog_view = PostBlogView.as_view({'get': 'list', 'post': 'create'})
    ```

   
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
