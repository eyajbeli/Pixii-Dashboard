from django.db import models

# Create your models here.
class Order(models.Model):
    
    """
    Model representing an order.

    Attributes:
        username (CharField): The username associated with the order.
        email (EmailField): The email associated with the order.
        adresse (CharField): The address for delivering the order.
        phone (IntegerField): The phone number associated with the order.
        pays (CharField): The country associated with the order.
        produit (CharField): The product associated with the order.
        STATUS_CHOICES (tuple): Choices for the status field.
        status (CharField): The status of the order.

    Example Usage:
    ```
    order = Order(
        username='John Doe',
        email='john.doe@example.com',
        adresse='123 Main St',
        phone=123456789,
        pays='Country',
        produit='Product',
        status='pending'
    )
    ```

    Note: Adjust the attributes and choices as per your specific requirements.
    """

    
    username=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    adresse=models.CharField(max_length=100)
    phone=models.IntegerField
    pays=models.CharField(max_length=100)
    produit=models.CharField(max_length=100)
    STATUS_CHOICES = (
        ('pending', 'En attente'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
    )
    
    status=models.CharField(max_length=10, choices=STATUS_CHOICES,default='pending')

   
    