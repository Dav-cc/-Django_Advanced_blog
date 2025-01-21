from django.urls import path,include
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # registration
    path('registraion/', views.RegistraionApiView.as_view(), name = 'registration'),
    # reset password
    # chenge password
    path('password-change/',views.ChangePasswordApiView.as_view(),name ='change-pass'),
    # login token
    path('token/login/',ObtainAuthToken.as_view(), name = 'token-login'),
    path('token/logout/', views.Customdiscardauthtoken.as_view(), name='token-deleter'),
    
    # login jwt
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-tk'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-tr'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-tv'),

]
