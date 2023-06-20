from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            'body',
            "author",
            "created_at",
        )
        
        model = Post
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "username")
        model = get_user_model()