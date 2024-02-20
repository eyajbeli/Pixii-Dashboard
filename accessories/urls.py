from django.urls import include, path
from rest_framework import routers
from .views import AccessoriesView


router = routers.DefaultRouter()
"""
DefaultRouter configuration for registering views with Django REST Framework.

Attributes:
    r'accessory' (str): URL pattern for the AccessoriesView, registered with the name 'accessory'.
    AccessoriesView (class): View for handling CRUD operations on the Accessory model.
    basename="accessory" (str): The base name for the 'accessory' URL pattern.

router.register(r'accessory', AccessoriesView, basename="accessory")
"""
urlpatterns = [
    path('', include(router.urls)),
    
]