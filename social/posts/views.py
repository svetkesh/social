# from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model
from rest_framework import viewsets

from rest_framework import generics
from .serializers import (
    PostSerializer, UserSerializer,
    LikeSerializer, DislikeSerializer
)
from .permissions import IsAuthorOrReadOnly


from .models import Post, Like, Dislike


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LikeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DislikeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer

