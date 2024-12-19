from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User ,Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Register your models here.

class CustomUserCreationForm(UserCreationForm):
    class Meta :
        models = User
        fields = ['email']
        
class CustomUserChengForm(UserChangeForm):
    class Meta:
        models = User
        fields = ['email']         
    





class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChengForm
    
    model = User
    list_display = ['email','is_superuser', 'is_active' ]
    list_filter = ['email', 'is_active']
    search_fields = ['email', 'is_superuser']
    ordering = ['is_active']
    
    fieldsets = (
        ('authentication', {
            "fields": (
                
                'email' , 'password'
            ),
        }),
          ('important dates', {
            "fields": (
                
                'last_login' ,
            ),
        }),
          ('group permissions', {
            "fields": (
                
                'groups' , 'user_permissions'
            ),
        }),
              ('permissions', {
            "fields": (
                
                'is_staff' , 'is_active', 'is_superuser'
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1","password2", "is_staff",
                "is_active", "is_superuser"
            )}
        ),
    )
    
    
admin.site.register(User, CustomUserAdmin)  
admin.site.register(Profile)  