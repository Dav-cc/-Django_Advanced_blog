from django.db import models
from django.contrib.auth.models import (BaseUserManager , AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email ,password, **other_fieldes):
        if not email :
            raise ValueError(_('email must be set'))
        email = self.normalize_email(email)
        user = self.model(email = email, **other_fieldes)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,password, **other_fields):
        other_fields.setdefault('is_superuser', True)  
        other_fields.setdefault('is_staff', True)  
        other_fields.setdefault('is_active', True)  
        
        if other_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if other_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **other_fields)

             

class User(AbstractBaseUser,PermissionsMixin):
    """
    custom user model for project
    """
    email = models.EmailField(max_length=225, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    
    object = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    