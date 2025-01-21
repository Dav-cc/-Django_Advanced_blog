from rest_framework import serializers
from ...models import User
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length = 255, write_only = True )
    
    class Meta:
        model = User
        fields = ['email', 'password', 'password1']
        
        
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'detail':'passwords arent match'})
        
        try:
            validate_password(attrs.get('password'))
        
        except exceptions.ValidationError as e :
            raise serializers.ValidationError({'password': list(e.messages)})
        
                    
        
        return super().validate(attrs)
    
    
    def create(self, validated_data):
        validated_data.pop('password1',None)
        return User.objects.create_user(**validated_data)    
    
    
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)        
    new_password1 = serializers.CharField(required = True)   
    
    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password1'):
            raise serializers.ValidationError({'detail':'passwords dosent match'})
        
        try:
            validate_password(attrs.get('new_password'))
        
        except exceptions.ValidationError as e :
            raise serializers.ValidationError({'new_password': list(e.messages)})
        
        
        
        return super().validate(attrs)         
    