from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, Like, Dislike


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'post', 'created_at',)
        model = Like


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'post', 'created_at',)
        model = Dislike


class PostSerializer(serializers.ModelSerializer):

    likes = LikeSerializer(many=True, read_only=True)
    dislikes = DislikeSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id', 'author', 'body',
            'created_at',
            'likes', 'dislikes',
        )
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)



