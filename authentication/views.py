from django.shortcuts import render
from rest_framework import generics,status, views, permissions
from rest_framework.response import Response 
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, ChangePasswordSerializer, UpdateProfileSerializer,ResetPasswordEmailRequestSerializer,DeactivateAccountSerializer
from knox.models import AuthToken
from .models import User 
from .utils import Util 
from rest_framework.permissions import AllowAny
from django.contrib.sites.shortcuts import get_current_site 
from django.urls import reverse 
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi 
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.views import LoginView
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import smart_str, force_str, smart_bytes

class RegisterView(generics.GenericAPIView):
    """
    View for user registration.

    - Requires a POST request with user data.
    - Validates the data using RegisterSerializer.
    - Creates a new user and sends a verification email with a token.
    - Returns the generated token.

    Example:
    ```
    POST /register/
    {
        "username": "example_user", #str
        "email": "user@example.com",#str
        "password": "secure_password" #str
    }
    ```
    """
    
    serializer_class = RegisterSerializer
    
    def post(self, request):
        """
        Handle POST requests for user registration.

        - Extract user data from the request.
        - Validate the data using RegisterSerializer.
        - Save the user.
        - Generate a verification token.
        - Construct a verification URL and send it via email.
        - Return the generated token in the response.
        Args:
        request (rest_framework.request.Request): The HTTP request object
        
        Returns:
        Response: A JSON response containing the generated token.
        """
        
        user=request.data 
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        
      
        user=User.objects.get(email=user_data['email'])
     
        token = AuthToken.objects.create(user) 
      
        current_site=get_current_site(request).domain 
        relativeLink=reverse('email-verify')
        absurl='http://'+current_site+relativeLink+"?token="+str(token)  
        
        email_body='Hi '+ user.username + ' Use link below to verify your email \n'+absurl
        data={'email_body':email_body,'to_email':user.email,'email_subject':'Verify your email'}
        Util.send_email(data)
    
        return Response({"token":token[1]} )
        
   
class VerifyEmail(views.APIView):
    
    """
    View for email verification.

    This view is used to verify the user's email based on the provided token.

    Attributes:
        serializer_class (EmailVerificationSerializer): Serializer class for email verification.
        token_param_config (openapi.Parameter): Configuration for the token parameter(swagger).

    Methods:
        get(request): Handles GET requests for email verification.
    """
    
    serializer_class = EmailVerificationSerializer
    token_param_config=openapi.Parameter('token',in_=openapi.IN_QUERY,description='Enter your token here',type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
       """
        Handle GET requests for email verification.

        Args:
            request (rest_framework.request.Request): The HTTP request object.

        Returns:
            Response: A JSON response indicating the result of the email verification.
       """
       try:
           # Attempt to retrieve the user and authentication token from the request
          auth_token = request.auth
          user = auth_token.user
          
           # Check if the user is not already verified
          if not user.is_verified:
              # Mark the user as verified and save
              user.is_verified=True
              user.save() 
          
          return Response({'email':'Succesfully activated'},status=status.HTTP_200_OK)

          
       except AuthToken.DoesNotExist:
         # Handle the case where the authentication token does not exist
         return Response({'error':'Invalid token'},status=status.HTTP_400_BAD_REQUEST)

      
       

class LoginAPIView(generics.GenericAPIView):
    
  """
    API view for user login.

    This view handles user login by validating the provided credentials and generating an authentication token.

    Attributes:
        serializer_class (LoginSerializer): Serializer class for login credentials.

    Methods:
        post(request, *args, **kwargs): Handles POST requests for user login.
    """
    
  serializer_class = LoginSerializer
  
  def post(self,request,*args, **kwargs):
      
        """
        Handle POST requests for user login.

        Args:
            request (rest_framework.request.Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response indicating the result of the login attempt.
        """
        serializer=self.serializer_class(data=request.data)
       
        serializer.is_valid(raise_exception=True)
       
        user=serializer.validated_data
        
          # Create an authentication token for the user
        token=AuthToken.objects.create(user) 
      
        return Response({
                         'msg':'you are sucessfully Login',
                        
                         'token':token[1]},
          )
  
 
class UserListView(generics.ListAPIView):
    
  """
    API view for listing all users.

    This view retrieves and lists all user instances from the User model.

    Attributes:
        queryset (QuerySet): QuerySet containing all user instances.
        serializer_class (RegisterSerializer): Serializer class for user instances.

    Methods:
        get(request, *args, **kwargs): Handles GET requests for listing users.
    Example:
    ```
    GET /users/
    ```
  """
  
  queryset=User.objects.all()
  serializer_class = RegisterSerializer
  
  
    
class CurrentUserView(generics.RetrieveAPIView):
   """
    API view for retrieving the current authenticated user.

    This view retrieves and returns the details of the currently authenticated user.

    Attributes:
        serializer_class (LoginSerializer): Serializer class for user details.
        permission_classes (list): List of permission classes for authentication.

    Methods:
        get_object(): Returns the current authenticated user.

    Example:
    ```
    GET /current-user/
    ```
   """
   
   serializer_class = LoginSerializer
   permission_classes = [permissions.IsAuthenticated]
   
   def get_object(self):
      """
        Returns the current authenticated user.

        
        """
      return self.request.user
    
    


class ChangePasswordView(generics.UpdateAPIView):
    
    """
    API view for changing the password of the current authenticated user.

    This view allows the current authenticated user to change their password.

    Attributes:
        authentication_classes (tuple): Tuple of authentication classes (TokenAuthentication).
        permission_classes (tuple): Tuple of permission classes (IsAuthenticated).
        serializer_class (ChangePasswordSerializer): Serializer class for changing the password.

    Methods:
        get_object(): Returns the current authenticated user.
        update(request, *args, **kwargs): Handles the update request for changing the password.

    Example:
    ```
    PUT /change-password/
    {
        "old_password": "old_password_here",
        "new_password": "new_password_here"
    }
    ```
    Note: The `generics.UpdateAPIView` class simplifies the implementation of updating objects
    by providing a generic framework, reducing the boilerplate code needed for update operations.
    """
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class=ChangePasswordSerializer 

    def get_object(self):
        """
        Returns the current authenticated user.

        
        """
        return self.request.user

    def update(self, request, *args, **kwargs):
        """
        Handles the update request for changing the password.

        Args:
            request (rest_framework.request.Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response indicating the result of the password change request.
        """
        user = self.get_object()
        
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not user.check_password(old_password):
                return Response({"old_password": ["Mot de passe incorrect."]}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"detail": "Mot de passe mis à jour avec succès."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
      
      
class UpdateProfileView(generics.UpdateAPIView):
    
    """
    API view for updating the profile of the current authenticated user.

    This view allows the current authenticated user to update their profile details.

    Attributes:
        permission_classes (tuple): Tuple of permission classes (IsAuthenticated).
        serializer_class (UpdateProfileSerializer): Serializer class for updating the profile.

    Methods:
        get_object(): Returns the current authenticated user.
        update(request, *args, **kwargs): Handles the update request for the profile.

    Example:
    ```
    PUT /update-profile/
    {
        "username": "new_username",
        "email": "new_email@example.com",
        "phone_number": "new_phone_number"
    }
    ```
    """
    
    
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateProfileSerializer 

    def get_object(self):
        """
        Returns the current authenticated user.

        
        """
       
        return self.request.user

    def update(self, request, *args, **kwargs):
        
        """
        Handles the update request for the profile.

        Args:
            request (rest_framework.request.Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response indicating the result of the profile update request.
        """
       
        user = self.get_object()

       
        serializer = UpdateProfileSerializer(user, data=request.data)

      
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Profil mis à jour avec succès."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeactivateAccountView(generics.GenericAPIView):
    
    """
    API view for deactivating a user account.

    This view allows deactivating a user account by setting the 'is_active' field to False.

    Attributes:
        serializer_class (DeactivateAccountSerializer): Serializer class for deactivating the account.

    Methods:
        post(request): Handles the POST request to deactivate the account.

    Example:
    ```
    POST /deactivate-account/
    {
        "email": "user_email@example.com"
    }
    ```
    """
    
    
    serializer_class = DeactivateAccountSerializer
    def post(self, request):
        
        """
        Handles the POST request to deactivate the account.

        Args:
            request (rest_framework.request.Request): The HTTP request object.

        Returns:
            Response: A JSON response indicating the result of the account deactivation request.
        """
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.is_active = False
        user.save()

        return Response({'detail': 'Account deactivated successfully'})
    







class  RequestPaswordResetEmail(generics.GenericAPIView):
    
    serializer_class = ResetPasswordEmailRequestSerializer
    
    def post(self,request):
       
        serializer=self.serializer_class(data=request.data)
        email = request.data.get('email', '')
        
        if User.objects.filter(email=email).exists():
              user=User.objects.get(email=email)
              uidb64=urlsafe_base64_encode(smart_bytes(user.id))
             
              token = AuthToken.objects.create(user) 
              current_site=get_current_site(request=request).domain 
              relativeLink=reverse('pasword-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
              absurl='http://'+current_site+relativeLink
        
              email_body='Hello, \nUse link below to reset your password \n'+absurl
              
              data={'email_body':email_body,'to_email':user.email,'email_subject':' reset your password'}
              
              Util.send_email(data)
    
     
              return Response({'success':'We have sent you a link to reset your password'},status=status.HTTP_200_OK)
              
        return Response({'error':'Invalid mail'}, status=status.HTTP_400_BAD_REQUEST)
    
    

