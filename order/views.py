from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status,generics

class OrderView(viewsets.ModelViewSet):
    """
    Viewset for managing orders.

    This viewset provides CRUD operations for the Order model.

    Attributes:
        queryset (QuerySet): The set of Order objects.
        serializer_class (Serializer): The serializer class for Order.

    """ 

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateStatusView(generics.GenericAPIView):
    """
    GenericAPIView for updating the status of an order.

    This view allows updating the status of an order by providing the order_id and new_status.

    Attributes:
        put (method): HTTP PUT method for updating the order status.

    Example Usage:
    ```
    order_update_status_view = OrderUpdateStatusView.as_view()
    ```

    Note: Ensure to set up appropriate URL patterns to link to this view.
    """
    
    
    
    def put(self,request,order_id):
        """
        Update the status of the order.

        Args:
            request (Request): The HTTP request object.
            order_id (int): The ID of the order to be updated.

        Returns:
            Response: The updated order details or an error response.
        """
        
        try:
            order=Order.objects.get(pk=order_id)
            
        except Order.DoesNotExist:
            return Response({'detail': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        
        new_status=request.data.get('status')
        if new_status  not in dict(Order.STATUS_CHOICES).keys():
             return Response({'detail': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
         
        order.status=new_status
        order.save()
        
        serializer=OrderSerializer(order)
        return Response(serializer.data) 