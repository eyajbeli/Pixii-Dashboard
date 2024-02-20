from rest_framework import serializers
from .models import JobCategory,JobContract,JobOffer,JobOffer

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for JobCategory model.

    This serializer is used to convert JobCategory model instances to JSON representation.

    Attributes:
        Meta (class): Specifies metadata for the serializer.

    Example Usage:
    ```
    category_serializer = CategorySerializer(data={'category_name': 'IT'})
    ```

   
    """
    class Meta:
        model=JobCategory
      
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=JobContract
        fields = '__all__'
        

class OfferSerializer(serializers.ModelSerializer):
    
    cat=CategorySerializer
    contrat=ContractSerializer
    class Meta:
        model=JobOffer
        fields = '__all__'
       

