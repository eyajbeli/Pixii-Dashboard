from django.urls import include, path
from rest_framework import routers
from .views import PostBlogView


router = routers.DefaultRouter()
"""
DefaultRouter configuration for registering views with Django REST Framework.

Attributes:
    r'posts' (str): URL pattern for the PostBlogView, registered with the name 'post'.
    PostBlogView (class): View for handling CRUD operations on the Blog model.
    basename="post" (str): The base name for the 'post' URL pattern.

router.register(r'posts', PostBlogView, basename="post")
Note: The DefaultRouter automatically generates URL patterns for the registered views.
"""
urlpatterns = [
    path('', include(router.urls)),
    
]