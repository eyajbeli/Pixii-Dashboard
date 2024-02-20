from django.shortcuts import render
from rest_framework import viewsets
from .models import JobOffer,JobCategory,JobContract
from .serializers import  OfferSerializer,CategorySerializer,ContractSerializer

class JobOfferView(viewsets.ModelViewSet):
    """
    Viewset for JobOffer model.

    This viewset provides CRUD operations for the JobOffer model.

    Attributes:
        queryset (QuerySet): The set of JobOffer objects.
        serializer_class (Serializer): The serializer class for JobOffer.

    Example Usage:
    ```
    job_offer_view = JobOfferView.as_view({'get': 'list', 'post': 'create'})
    ```

    Note: Ensure to set up appropriate URL patterns to link to these views.
    """
    queryset = JobOffer.objects.all()
    serializer_class =OfferSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class =CategorySerializer
    
class ContractView(viewsets.ModelViewSet):
    queryset = JobContract.objects.all()
    serializer_class =ContractSerializer
