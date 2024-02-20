from django.shortcuts import render
from rest_framework import viewsets
from .models import Accessory
from .serializers import AccessoriesSerializer
class AccessoriesView(viewsets.ModelViewSet):
    """
    Viewset for managing Accessories.

    This viewset provides CRUD operations for the Accessory model.

    Attributes:
        queryset (QuerySet): The set of Accessory objects.
        serializer_class (Serializer): The serializer class for Accessory.

    Example Usage:
    ```
    accessories_view = AccessoriesView.as_view({'get': 'list', 'post': 'create'})
    ```

    Note: Ensure to set up appropriate URL patterns to link to this view.
    """

    queryset = Accessory.objects.all()
    serializer_class = AccessoriesSerializer
