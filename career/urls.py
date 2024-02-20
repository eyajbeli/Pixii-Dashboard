from django.urls import include, path
from rest_framework import routers
from .views import JobOfferView,CategoryView,ContractView
"""
DefaultRouter configuration for registering views with Django REST Framework.

Attributes:
    r'jobs' (str): URL pattern for the JobOfferView, registered with the name 'jobs'.
     JobOfferView (class): View for handling CRUD operations on JobOffer model.
     basename="jobs" (str): The base name for the 'jobs' URL pattern.
"""
router = routers.DefaultRouter()
router.register(r'jobs', JobOfferView, basename="jobs")
router.register(r'cat', CategoryView, basename="cat")
router.register(r'contract', ContractView, basename="contract")


"""
    Define URL patterns for your application using Django REST Framework and the provided views.

    Example Usage:
    ```
    urlpatterns = [
        path('', include(router.urls)),
    ]
    ```
"""
urlpatterns = [
    
    path('', include(router.urls)),
    
]