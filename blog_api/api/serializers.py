from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # Use the nested serializer

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'author', 'created_at')
        # Add this line to make author field read-only.
        read_only_fields = ('author',)