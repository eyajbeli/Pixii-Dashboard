# models.py
from django.db import models

class Accessory(models.Model):
    """
    Model representing different accessories.

    Attributes:
        ACCESSORY_CHOICES (list): Choices for the accessory_name field.
        accessory_name (CharField): The name of the accessory, selected from predefined choices.

    Methods:
        __str__(): Returns a human-readable string representation of the accessory.

    Example Usage:
    ```
    accessory = Accessory(accessory_name='Casque')
    ```

    Note: Adjust the choices and attributes as per your specific requirements.
    """
    ACCESSORY_CHOICES = [
        ('casque', 'Casque'),
        ('Cockpit', 'Cockpit'),
        ('X', 'X'),
        ('Y', 'Y'),
        
    ]

    accessory_name = models.CharField(max_length=50, choices=ACCESSORY_CHOICES, unique=True)

    def __str__(self):
        return self.accessory_name
