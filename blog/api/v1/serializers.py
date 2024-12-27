from rest_framework import serializers
from blog.models import Post




class PostSerializer(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields ='__all__'
        # ['id', 'title', 'content', 'created_date', 'status', 'published_date']
