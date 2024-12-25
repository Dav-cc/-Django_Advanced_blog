from rest_framework import serializers

class PostSerializer(serializers.Serializer):
        title = serializers.CharField()
        
