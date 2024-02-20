from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin, AbstractUser 


class UserManager(BaseUserManager):
    
    """
    Custom manager for the User model.

    This manager provides methods to create regular users and superusers.

    Methods:
        create_user(username, email, password, phone_number=None): Creates a regular user.
        create_superuser(username, email, password, phone_number=None): Creates a superuser.

    Example Usage:
    ```
    user_manager = UserManager()

    # Creating a regular user
    regular_user = user_manager.create_user(username='john_doe', email='john@example.com', password='password123')

    # Creating a superuser
    superuser = user_manager.create_superuser(username='admin', email='admin@example.com', password='admin123')
    ```
    """
    
    def create_user(self,username,email,password=None,phone_number=None):
        """
        Creates a regular user.

        Args:
            username (str): The username for the user.
            email (str): The email address for the user.
            password (str): The password for the user.
            phone_number (str, optional): The phone number for the user (default is None).

        Returns:
            User: The newly created regular user.
        """
        if username is None:
            raise TypeError('username must not be None')
        
        if email is None:
            raise TypeError('email must not be None')
        
        user=self.model(username=username, email=self.normalize_email(email),  phone_number=phone_number )
        user.set_password(password) 
        user.save()
        return user 
        
    #create superuser
    def create_superuser(self,username,email,password=None,phone_number=None):
        """
        Creates a superuser.

        Args:
            username (str): The username for the superuser.
            email (str): The email address for the superuser.
            password (str): The password for the superuser.
            phone_number (str, optional): The phone number for the superuser (default is None).

        Returns:
            User: The newly created superuser.
        """
        if password is None:
            raise TypeError('Password must not be None')
        
        
        user=self.create_user(username, email, password, phone_number)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user 
    

class User(AbstractBaseUser,PermissionsMixin):
    """
    Custom user model extending AbstractBaseUser and PermissionsMixin.

    This model represents a user in the system with extended fields and custom functionality.

    Attributes:
        username (str): The username for the user.
        email (str): The email address for the user.
        phone_number (int, optional): The phone number for the user (default is None).
        is_verified (bool): Indicates whether the user's email is verified.
        is_active (bool): Indicates whether the user account is active.
        is_staff (bool): Indicates whether the user has staff privileges.
        created_at (DateTime): The timestamp when the user account was created.
        updated_at (DateTime): The timestamp when the user account was last updated.

    Methods:
        __str__(): Returns a string representation of the user.

    Example Usage:
    ```
    user = User.objects.create_user(username='john_doe', email='john@example.com', password='password123')
    ```

    
    """
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    phone_number = models.IntegerField(blank=True, null=True)
    is_verified=models.BooleanField(default=False)
  
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='email' 
    REQUIRED_FIELD=['username']
    
    objects=UserManager() 
    
    def __str__(self):
        """
        Returns a string representation of the user.

        
        """
        return self.email 
    
    
