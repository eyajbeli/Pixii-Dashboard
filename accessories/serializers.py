from rest_framework import serializers
from .models import Accessory

class AccessoriesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Accessory model.

    This serializer is used to convert Accessory model instances to JSON representation.

    Attributes:
        Meta (class): Specifies metadata for the serializer.

    Example Usage:
    ```
    accessories_serializer = AccessoriesSerializer(data={'accessory_name': 'Casque'})
    ```

    """
    class Meta:
        model = Accessory
        fields = '__all__' 