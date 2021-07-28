from rest_framework import serializers as se
from ..models import Post


class PostListSerializer(se.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image']


class PostSerializer(se.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'description', 'title', 'image']
