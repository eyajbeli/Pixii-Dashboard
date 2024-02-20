from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from authentication.models import User 
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
       
    """
    Serializer for user registration.

    This serializer is used to validate and process user registration data.

    Attributes:
        password (serializers.CharField): A password field with specific constraints.

    Example:
    ```
    {
        "email": "user@example.com",
        "username": "example_user",
        "password": "secure_password",
        "phone_number": "1234567890"
    }
    ```

    Raises:
        serializers.ValidationError: If the username contains non-alphanumeric characters.

    Methods:
        validate(attrs): Custom validation method to check username constraints.
        create(validated_data): Custom method to create a new user using validated data.
    """
     
     
     
     
     
    password=serializers.CharField(max_length=68,min_length=8,write_only=True)
    
    class Meta:
        
        """
        Meta class to define model and fields for the serializer.
        """
        User = get_user_model()
        model=User
        fields=['email','username','password','phone_number']
       
        
    def validate(self, attrs):
        
        """
        Custom validation method to check username constraints.

        Args:
            attrs (dict): Dictionary containing user registration data.

        Raises:
            serializers.ValidationError: If the username contains non-alphanumeric characters.

        Returns:
            dict: Validated data.
        """
        
        email=attrs.get('email','')
        username=attrs.get('username','')
        
        if not username.isalnum():
            raise serializers.ValidationError('the username should only contain alphanumeric characters')
        
       
        return attrs
    
    def create(self, validated_data):
        """
        Custom method to create a new user using validated data.

        Args:
            validated_data (dict): Validated user registration data.

        Returns:
            User: Newly created user instance.
        """
        return User.objects.create_user(**validated_data)
    

class EmailVerificationSerializer(serializers.Serializer):
    """
    Serializer for email verification.

    This serializer is used to validate the token parameter provided for email verification.

    Attributes:
        token (serializers.CharField): CharField for the verification token.

    Example:
    ```
    {
        "token": "your_verification_token"
    }
    ```
    """
    token=serializers.CharField(max_length=555)
    
   
class  LoginSerializer(serializers.ModelSerializer):
    
    """
    Serializer for user login credentials.

    This serializer is used to validate user login credentials, including email and password.

    Attributes:
        email (serializers.EmailField): Email field for the user's email address.
        password (serializers.CharField): CharField for the user's password (write-only).

    Meta:
        model (User): The User model associated with the serializer.
        fields (list): List of fields to include in the serializer.

    Methods:
        validate(attrs): Custom validation method to authenticate the user based on provided credentials.
    """
    
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
   
    class Meta:
        """
        Meta class to define model and fields for the serializer.
        """
        model = User
        fields = ['email', 'password']
        
    def validate(self, attrs):
        
        """
        Custom validation method to authenticate the user based on provided credentials.

        Args:
            attrs (dict): Dictionary containing user login credentials.

        Raises:
            AuthenticationFailed: If the provided credentials are invalid, the account is disabled,
                or the email is not verified.

        Returns:
            User or dict: The authenticated user or a dictionary with user information.
        """
        
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        
        # Authenticate the user based on provided credentials
        user =authenticate(email=email, password=password)
        
       
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        
        if user and user.is_active and user.is_verified:
            return user 
        return {
            'email': user.email,
            'username': user.username,
          
        }
        
        

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for changing the password.

    This serializer is used to validate and handle the input for changing the password.

    Attributes:
        old_password (serializers.CharField): CharField for the old password.
        new_password (serializers.CharField): CharField for the new password.

    Example:
    ```
    {
        "old_password": "old_password_here",
        "new_password": "new_password_here"
    }
    ```
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    



class UpdateProfileSerializer(serializers.ModelSerializer):
    
    """
    Serializer for updating the profile details.

    This serializer is used to validate and handle the input for updating the profile details.

    Attributes:
        email (serializers.EmailField): EmailField for the email address.

    Meta:
        model (User): Django User model.
        fields (list): List of fields to be included in the serializer.

    Example:
    ```
    {
        "username": "new_username",
        "email": "new_email@example.com",
        "phone_number": "new_phone_number"
    }
    ```
    """
    
    email = serializers.EmailField(required=True) 
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']
        
    
    
class DeactivateAccountSerializer(serializers.Serializer):
    """
    Serializer for deactivating a user account.

    This serializer is used to validate and handle the input for deactivating a user account.

    Example:
    ```
    {
        "email": "user_email@example.com"
    }
    ```

    Note: This serializer does not have any specific fields since it only requires the 'email' field to identify the user
    whose account should be deactivated. The 'pass' keyword is used to indicate an empty serializer.
    """
    pass


 
class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    
    email=serializers.EmailField(min_length=2)
    
    class Meta:
        fields=['email']
        

        
        

