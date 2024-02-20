from django.urls import path, include
from .views import RegisterView, VerifyEmail, LoginAPIView, UserListView, CurrentUserView,ChangePasswordView, UpdateProfileView,  RequestPaswordResetEmail, DeactivateAccountView

from knox import views as knox_views

"""
    Define URL patterns for the authentication and user-related views.

    path('chemin/', NomDeLaVue.as_view(), name='nom-de-la-vue'),

 
    """
urlpatterns = [
    
    
    path('Register/',RegisterView.as_view(), name="Register"),
    path('login/',LoginAPIView.as_view(), name="login"),
    
    path('email_verify/',VerifyEmail.as_view(), name="email-verify"),
    path('users/',UserListView.as_view(), name="user-List"),
    path('current-user/',CurrentUserView.as_view(), name="current-user"),
   
    path('changepassword/', ChangePasswordView.as_view(), name='change_password'),
    path('changeprofile/', UpdateProfileView.as_view(), name='change_profile'),
    
  
    path('request-reset-email/', RequestPaswordResetEmail.as_view(), name="request-reset-mail"),
   
     path('deactivate-account/', DeactivateAccountView.as_view(), name='deactivate-account'),
    path('logout/',knox_views.LogoutView.as_view(),name='knox_logout_all')
   
    
    ]
   