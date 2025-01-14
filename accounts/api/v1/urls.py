from django.urls import path,include
from . import views


urlpatterns = [
    # registration
    path('registraion/', views.RegistraionApiView.as_view(), name = 'registration')
    # reset password
    # chenge password
    # login token
    # login jwt
]
