from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    This serializer includes all fields of the Order model.

    Attributes:
        Meta (class): Configuration class for the serializer.

    Example Usage:
    ```
    order_serializer = OrderSerializer(order_instance)
    serialized_data = order_serializer.data
    """

    class Meta:
        model = Order
        fields = '__all__'